#!/usr/bin/python

# Copyright: (c) 2024, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" Ansible module for managing Fault Sets on Dell Technologies (Dell) PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
module: fault_set
version_added: '2.2.0'
short_description: Manage Fault Sets on Dell PowerFlex
description:
- Managing fault sets on PowerFlex storage system includes getting details, creating, modifying, and deleting of fault set.
author:
- Carlos Tronco (@ctronco) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerflex.powerflex
options:
  fault_set_name:
    description:
    - Name of the Fault Set.
    - It is unuique across the PowerFlex array.
    - Mutually exclusive with I(fault_set_id).
    type: str
  fault_set_id:
    description:
    - ID of the Fault Set.
    - Mutually exclusive with I(fault_set_name).
    type: str
  protection_domain_name:
    description:
    - Name of protection domain.
    - Specify either I(protection_domain_name) or I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - ID of the protection domain.
    - Specify either I(protection_domain_name) or I(protection_domain_id).
    type: str
  fault_set_new_name:
    description: 
    - New name of the Fault Set.
    - This parameter is used to rename the Fault Set.
    type: str
  state:
    description:
    - State of the Fault Set.
    choices: ['present', 'absent']
    required: True
    type: str
    default: present
notes:
  - The I(check_mode) is supported.
'''


EXAMPLES = r'''

- name: Create Fault Set on Protection Domain
  dellemc.powerflex.fault_set:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    fault_set_name: "{{fault_set_name}}"
    protection_domain_name: "{{pd_name}}"
    state: present

- name: Get Fault Set on Protection Domain
  dellemc.powerflex.fault_set:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    fault_set_name: "{{fault_set_name}}"

- name: Rename Fault Set
  dellemc.powerflex.fault_set:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    fault_set_name: "{{fault_set_name}}"
    fault_set_new_name: "{{fault_set_new_name}}"
    

- name: Delete Fault Set
  dellemc.powerflex.fault_set:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    fault_set_name: "{{fault_set_name}}"
    state: absent

- name: Delete Fault Set
  dellemc.powerflex.fault_set:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    fault_set_id: "{{fault_set_id}}"
    state: absent
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'

fault_set_details:
    description: Details of fault set.
    returned: always
    type: dict
    contains:
        protectionDomainId:
            description: The ID of the protection domain.
            type: str
        protectionDomainName:
            description: The name of the protection domain.
            type: str
        name:
            description: fault set name.
            type: str
        id:
            description: fault set id.
            type: str
        links:
            description: Fault set links.
            type: list
            contains:
                href:
                    description: Fault Set instance URL.
                    type: str
                rel:
                    description: Relationship of fault set with different
                                 entities.
                    type: str
    sample: {
        "protectionDomainId": "da721a8300000000",
        "protectionDomainName": "pd_001",
        "name": "fs_001",
        "id": "eb44b70500000000",
        "links": [
            { "rel": "self", "href": "/api/instances/FaultSet::eb44b70500000000" },
            {
                "rel": "/api/FaultSet/relationship/Statistics",
                "href": "/api/instances/FaultSet::eb44b70500000000/relationships/Statistics"
            },
            {
                "rel": "/api/FaultSet/relationship/Sds",
                "href": "/api/instances/FaultSet::eb44b70500000000/relationships/Sds"
            },
            {
                "rel": "/api/parent/relationship/protectionDomainId",
                "href": "/api/instances/ProtectionDomain::da721a8300000000"
            }
        ]
        }

'''


from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import (
    utils,
)
from ansible.module_utils.basic import AnsibleModule


LOG = utils.get_logger("fault_set")


class PowerFlexFaultSet(object):
    """Class with FaultSet operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powerflex_gateway_host_parameters()
        self.module_params.update(get_powerflex_fault_set_parameters())

        mutually_exclusive = [
            ["fault_set_name", "fault_set_id"],
            ["protection_domain_name", "protection_domain_id"],
        ]

        required_if = [
            ("state", "present", ("protection_domain_id",
             "protection_domain_name"), True),
            ("state", "absent", ("fault_set_id", "fault_set_name"), True),
            ("state", "present", ("fault_set_id", "fault_set_name"), True),
        ]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive,
            # required_one_of=required_one_of,
            required_if=required_if,
        )

        utils.ensure_required_libs(self.module)

        try:
            self.powerflex_conn = utils.get_powerflex_gateway_host_connection(
                self.module.params
            )
            LOG.info("Got the PowerFlex system connection object instance")
        except Exception as e:
            LOG.error(str(e))
            self.module.fail_json(msg=str(e))

    # Borrowed from the protection_domain module with slight modification.
    def get_protection_domain(
        self, protection_domain_name=None, protection_domain_id=None
    ):
        """
        Get protection domain details
        :param protection_domain_name: Name of the protection domain
        :param protection_domain_id: ID of the protection domain
        :return: Protection domain details if exists
        :rtype: dict
        """

        name_or_id = (
            protection_domain_id if protection_domain_id else protection_domain_name
        )

        try:
            if protection_domain_id:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={"id": protection_domain_id}
                )

            else:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={"name": protection_domain_name}
                )

            if len(pd_details) == 0:
                error_msg = (
                    "Unable to find the protection domain with " "'%s'." % name_or_id
                )
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            return pd_details[0]

        except Exception as e:
            error_msg = (
                "Failed to get the protection domain '%s' with "
                "error '%s'" % (name_or_id, str(e))
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def create_fault_set(self, fault_set_name, protection_domain_id):
        """
        Create Fault Set
        :param fault_set_name: Name of the fault set
        :type fault_set_name: str
        :param protection_domain_id: ID of the protection domain
        :type protection_domain_id: str
        :return: Boolean indicating if create operation is successful
        """
        try:
            msg = "Creating fault set with name: %s on protection domain with id: %s" \
                % (fault_set_name, protection_domain_id)
            LOG.info(msg)
            self.powerflex_conn.fault_set.create(
                name=fault_set_name, protection_domain_id=protection_domain_id
            )
            return True

        except Exception as e:
            error_msg = "Create fault set '%s' operation failed" " with error '%s'" % (
                fault_set_name,
                str(e),
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_fault_set(
        self, fault_set_name=None, fault_set_id=None, protection_domain_id=None
    ):
        """Get the Fault Set Details
        :param fault_set_name: The name of the fault set
        :param fault_set_id: The ID of the fault set
        :param protection_domain_id: The ID of the Protection Domain
        :return: The dict containing FaultSet details
        """

        if fault_set_name:
            id_name = fault_set_name
            filter_fields = {"name": fault_set_name}
        else:
            id_name = fault_set_id
            filter_fields = {"id": fault_set_id}
        if protection_domain_id:
            filter_fields["protectionDomainId"] = protection_domain_id

        try:
            fs_details = self.powerflex_conn.fault_set.get(
                filter_fields=filter_fields)
            if len(fs_details) == 0:
                error_msg = "Unable to find Fault Set with identifier %s in Protection Domain %s" % (
                    id_name, protection_domain_id)
                LOG.info(error_msg)
                return None
            return fs_details[0]
        except Exception as e:
            errormsg = "Failed to get the Fault Set %s with error %s" % (
                id_name,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def remove_fault_set(self, fault_set_id):
        """Remove the Fault Set"""
        try:
            LOG.info(msg=f"Removing Fault Set {fault_set_id}")
            self.powerflex_conn.fault_set.delete(fault_set_id)
            return True
        except Exception as e:
            errormsg = f"Removing Fault Set {fault_set_id} failed with error {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def rename_fault_set(self, fault_set_id, fault_set_new_name):
        try:
            LOG.info(msg=f"Renaming Fault Set {fault_set_id} to {fault_set_new_name}")
            self.powerflex_conn.fault_set.rename(fault_set_id=fault_set_id, name=fault_set_new_name)
            return True
        except Exception as e:
            errormsg = f"Renaming Fault Set {fault_set_id} to {new_name} failed with error {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def perform_module_operation(self):
        """
        Perform different actions on Fault Set based on parameters passed in
        the playbook
        """
        fault_set_name = self.module.params["fault_set_name"]
        fault_set_id = self.module.params["fault_set_id"]
        fault_set_new_name = self.module.params["fault_set_new_name"]        
        protection_domain_name = self.module.params["protection_domain_name"]
        protection_domain_id = self.module.params["protection_domain_id"]
        state = self.module.params["state"]


        # result is a dictionary to contain end state and Fault Set details
        changed = False
        result = {"changed": False, "fault_set_details": None}

        pd_info = {"id": None}
        if protection_domain_name:
            pd_info = self.get_protection_domain(
                protection_domain_name=protection_domain_name
            )
        elif protection_domain_id:
            pd_info = self.get_protection_domain(
                protection_domain_id=protection_domain_id
            )
        fault_set_details = self.get_fault_set(
            fault_set_name=fault_set_name,
            fault_set_id=fault_set_id,
            protection_domain_id=pd_info['id'],
        )

        if state == "present" and not fault_set_details:
            changed = self.create_fault_set(
                fault_set_name=fault_set_name, protection_domain_id=pd_info['id']
            )
            fault_set_details = self.get_fault_set(
                fault_set_name=fault_set_name,
                fault_set_id=fault_set_id,
                protection_domain_id=pd_info["id"],
            )
        if state == "present" and fault_set_details and fault_set_new_name:
            changed = self.rename_fault_set(fault_set_id=fault_set_details['id'], fault_set_new_name=fault_set_new_name)
            fault_set_details = self.get_fault_set(
                fault_set_name=fault_set_new_name,
                fault_set_id=fault_set_id,
                protection_domain_id=pd_info['id'],
            )
        if state == "present":
            fault_set_details.update({"protectionDomainName": pd_info['name']})

        if state == "absent" and fault_set_details:
            changed = self.remove_fault_set(fault_set_id=fault_set_details['id'])
            fault_set_details = {}

        result["changed"] = changed
        result["fault_set_details"] = fault_set_details
        self.module.exit_json(**result)


def get_powerflex_fault_set_parameters():
    """This method provide parameter required for the Ansible FaultSet module on
    PowerFlex"""
    return {
        "fault_set_name": {},
        "fault_set_id": {},
        "fault_set_new_name": {"required": False, "type": "str", "default": None},        
        "protection_domain_name": {},
        "protection_domain_id": {},
        "state": {"required": True, "type": "str", "choices": ["present", "absent"]},
        #"zz": {"required": False, "type": "str", "default": None, "no_log": True},
    }


def main():
    """Create PowerFlex FaultSet object and perform actions on it
    based on user input from playbook"""
    obj = PowerFlexFaultSet()
    obj.perform_module_operation()


if __name__ == "__main__":
    main()
