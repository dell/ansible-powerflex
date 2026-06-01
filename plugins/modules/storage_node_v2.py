#!/usr/bin/python

# Copyright: (c) 2021-25, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing storage nodes on Dell Technologies (Dell) PowerFlex 5.x"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: storage_node_v2
version_added: '3.0.0'
short_description: Managing storage nodes on Dell PowerFlex 5.x

description:
- Dell PowerFlex storage node module includes getting details of storage nodes,
  creating, deleting, renaming storage nodes, managing IP addresses
  (add, remove, set role), updating device pathnames, and querying
  related PDS and DGWT objects.

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

author:
- Ansible Team <ansible.team@dell.com>

options:
  storage_node_name:
    description:
    - The name of the storage node.
    - Mutually exclusive with I(storage_node_id).
    type: str
  storage_node_id:
    description:
    - The ID of the storage node.
    - Mutually exclusive with I(storage_node_name).
    type: str
  new_storage_node_name:
    description:
    - New name for the storage node (rename operation).
    type: str
  protection_domain_name:
    description:
    - Name of protection domain. Required for create.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - ID of protection domain. Required for create.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  node_ips:
    description:
    - List of IP/role configurations for node creation.
    - Each item has C(ip) and C(role) keys.
    type: list
    elements: dict
    suboptions:
      ip:
        description:
        - IP address.
        type: str
        required: true
      role:
        description:
        - IP role.
        type: str
        required: true
        choices: ['Storage', 'App', 'StorageAndApp']
  ip_address:
    description:
    - IP address for add/remove/set-role operations.
    type: str
  ip_role:
    description:
    - Role for IP address.
    type: str
    choices: ['Storage', 'App', 'StorageAndApp']
  ip_state:
    description:
    - State of the IP address on the node.
    type: str
    choices: ['present-in-node', 'absent-in-node']
  update_original_pathnames:
    description:
    - Whether to update original pathnames for node devices.
    type: bool
    default: false
  force_failed_devices:
    description:
    - Force update for failed devices during pathname update.
    type: bool
  query_pds:
    description:
    - Whether to query PDS details through storage node.
    type: bool
    default: false
  query_dgwt:
    description:
    - Whether to query DGWT details through storage node.
    type: bool
    default: false
  state:
    description:
    - The state of the storage node.
    required: true
    choices: ['present', 'absent']
    type: str
notes:
  - This module is supported on Dell PowerFlex 5.x and later versions.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get storage node details by name
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    state: "present"

- name: Get storage node details by ID
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_id: "abc12300000000"
    state: "present"

- name: Rename storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    new_storage_node_name: "node1_renamed"
    state: "present"

- name: Add IP address to storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    ip_address: "10.0.0.5"
    ip_role: "Storage"
    ip_state: "present-in-node"
    state: "present"

- name: Remove IP address from storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    ip_address: "10.0.0.5"
    ip_state: "absent-in-node"
    state: "present"

- name: Set IP role on storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    ip_address: "10.0.0.1"
    ip_role: "App"
    ip_state: "present-in-node"
    state: "present"

- name: Update original pathnames
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    update_original_pathnames: true
    force_failed_devices: true
    state: "present"

- name: Query PDS details through storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    query_pds: true
    state: "present"

- name: Query DGWT details through storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    query_dgwt: true
    state: "present"

- name: Delete storage node
  dellemc.powerflex.storage_node_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
storage_node_details:
    description: Details of the storage node.
    returned: When storage node exists
    type: dict
    contains:
        id:
            description: Storage node ID.
            type: str
        name:
            description: Storage node name.
            type: str
        protectionDomainId:
            description: Protection domain ID.
            type: str
        ips:
            description: List of IP addresses and roles.
            type: list
            elements: dict
        port:
            description: Storage node port.
            type: int
        softwareVersionInfo:
            description: Software version.
            type: str
        authenticationError:
            description: Authentication error status.
            type: str
        links:
            description: Related resource links.
            type: list
    sample: {
        "id": "abc12300000000",
        "name": "node1",
        "protectionDomainId": "7bd6457000000000",
        "ips": [
            {"ip": "10.0.0.1", "role": "StorageAndApp"}
        ],
        "port": 7072,
        "softwareVersionInfo": "R4_5.2100.0",
        "authenticationError": "None"
    }
pds_details:
    description: PDS details queried through storage node.
    returned: When query_pds is true
    type: list
    sample: [
        {"id": "pds001", "name": "pds_1"}
    ]
dgwt_details:
    description: DGWT details queried through storage node.
    returned: When query_dgwt is true
    type: list
    sample: [
        {"id": "dgwt001", "name": "dgwt_1"}
    ]
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase, powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils


LOG = utils.get_logger('storage_node_v2')


@powerflex_compatibility(min_ver='5.0')
class PowerFlexStorageNodeV2(PowerFlexBase):
    """Class with storage node operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        argument_spec = dict(
            storage_node_name=dict(type='str'),
            storage_node_id=dict(type='str'),
            new_storage_node_name=dict(type='str'),
            protection_domain_name=dict(type='str'),
            protection_domain_id=dict(type='str'),
            node_ips=dict(
                type='list', elements='dict',
                options=dict(
                    ip=dict(type='str', required=True),
                    role=dict(type='str', required=True,
                              choices=['Storage', 'App', 'StorageAndApp']),
                )
            ),
            ip_address=dict(type='str'),
            ip_role=dict(type='str',
                         choices=['Storage', 'App', 'StorageAndApp']),
            ip_state=dict(type='str',
                          choices=['present-in-node', 'absent-in-node']),
            update_original_pathnames=dict(type='bool', default=False),
            force_failed_devices=dict(type='bool'),
            query_pds=dict(type='bool', default=False),
            query_dgwt=dict(type='bool', default=False),
            state=dict(required=True, type='str',
                       choices=['present', 'absent']),
        )

        mut_ex_args = [
            ['storage_node_name', 'storage_node_id'],
            ['protection_domain_name', 'protection_domain_id'],
        ]

        required_one_of_args = [
            ['storage_node_name', 'storage_node_id'],
        ]

        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': True,
            'mutually_exclusive': mut_ex_args,
            'required_one_of': required_one_of_args,
        }

        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get(self, node_id, node_name):
        """
        Get storage node details
        :param node_id: ID of the storage node
        :type node_id: str
        :param node_name: Name of the storage node
        :type node_name: str
        :return: Storage node details if exists
        :rtype: dict
        """
        name_or_id = node_id if node_id else node_name
        try:
            if node_id:
                sn_details = self.powerflex_conn.storage_node.get(
                    entity_id=node_id)
            else:
                sn_details = self.powerflex_conn.storage_node.get(
                    filter_fields={'name': node_name})

            if isinstance(sn_details, list):
                return sn_details[0] if len(sn_details) > 0 else None
            return sn_details
        except Exception as e:
            error_msg = (
                "Failed to get the storage node '%s' with "
                "error '%s'" % (name_or_id, str(e))
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def create(self, node_name, node_ips, protection_domain_id):
        """
        Create storage node
        :param node_name: Name of the storage node
        :type node_name: str
        :param node_ips: List of IP/role dicts
        :type node_ips: list
        :param protection_domain_id: Protection domain ID
        :type protection_domain_id: str
        :return: Created storage node details
        :rtype: dict
        """
        try:
            LOG.info("Creating storage node with name: %s", node_name)
            if self.module.check_mode:
                return {"name": node_name, "ips": node_ips,
                        "protectionDomainId": protection_domain_id}
            return self.powerflex_conn.storage_node.create(
                name=node_name,
                node_ips=node_ips,
                protection_domain_id=protection_domain_id,
            )
        except Exception as e:
            error_msg = (
                f"Create storage node '{node_name}' "
                f"operation failed with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def delete(self, sn):
        """
        Delete storage node
        :param sn: storage node details
        :type sn: dict
        :rtype: None
        """
        try:
            self.powerflex_conn.storage_node.delete(sn["id"])
            LOG.info("Storage node deleted successfully.")
        except Exception as e:
            error_msg = (
                f"Delete storage node '{sn['name']}' "
                f"operation failed with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def rename(self, node_id, new_name):
        """
        Rename storage node
        :param node_id: ID of the storage node
        :type node_id: str
        :param new_name: New name
        :type new_name: str
        :return: Updated storage node details
        :rtype: dict
        """
        try:
            LOG.info("Renaming storage node %s to %s", node_id, new_name)
            return self.powerflex_conn.storage_node.rename(node_id, new_name)
        except Exception as e:
            error_msg = (
                f"Failed to rename storage node '{node_id}' "
                f"with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def add_ip(self, node_id, ip_address, ip_role):
        """
        Add IP address to storage node
        :param node_id: ID of the storage node
        :type node_id: str
        :param ip_address: IP address to add
        :type ip_address: str
        :param ip_role: Role for the IP
        :type ip_role: str
        :return: Updated storage node details
        :rtype: dict
        """
        try:
            LOG.info("Adding IP %s to storage node %s", ip_address, node_id)
            return self.powerflex_conn.storage_node.add_ip(
                node_id, {"ip": ip_address, "role": ip_role})
        except Exception as e:
            error_msg = (
                f"Failed to add IP to storage node '{node_id}' "
                f"with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def remove_ip(self, node_id, ip_address):
        """
        Remove IP address from storage node
        :param node_id: ID of the storage node
        :type node_id: str
        :param ip_address: IP address to remove
        :type ip_address: str
        :return: Updated storage node details
        :rtype: dict
        """
        try:
            LOG.info("Removing IP %s from storage node %s",
                     ip_address, node_id)
            return self.powerflex_conn.storage_node.remove_ip(
                node_id, ip_address)
        except Exception as e:
            error_msg = (
                f"Failed to remove IP from storage node '{node_id}' "
                f"with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def set_ip_role(self, node_id, ip_address, ip_role):
        """
        Set IP address role on storage node
        :param node_id: ID of the storage node
        :type node_id: str
        :param ip_address: IP address
        :type ip_address: str
        :param ip_role: New role
        :type ip_role: str
        :return: Updated storage node details
        :rtype: dict
        """
        try:
            LOG.info("Setting IP role for %s on storage node %s",
                     ip_address, node_id)
            return self.powerflex_conn.storage_node.set_ip_role(
                node_id, ip_address, ip_role)
        except Exception as e:
            error_msg = (
                f"Failed to set IP role for storage node '{node_id}' "
                f"with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update_pathnames(self, node_id, force=None):
        """
        Update original pathnames for storage node devices
        :param node_id: ID of the storage node
        :type node_id: str
        :param force: Force failed devices
        :type force: bool
        :return: Updated storage node details
        :rtype: dict
        """
        try:
            LOG.info("Updating original pathnames for storage node %s",
                     node_id)
            return self.powerflex_conn.storage_node.update_original_pathnames(
                node_id, force=force)
        except Exception as e:
            error_msg = (
                f"Failed to update original pathnames for storage node "
                f"'{node_id}' with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def query_pds(self, node_id):
        """
        Query PDS details through storage node relationship
        :param node_id: ID of the storage node
        :type node_id: str
        :return: List of PDS details
        :rtype: list
        """
        try:
            LOG.info("Querying PDS details for storage node %s", node_id)
            return self.powerflex_conn.storage_node.get_related(
                node_id, 'Pds')
        except Exception as e:
            error_msg = (
                f"Failed to query PDS details for storage node "
                f"'{node_id}' with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def query_dgwt(self, node_id):
        """
        Query DGWT details through storage node relationship
        :param node_id: ID of the storage node
        :type node_id: str
        :return: List of DGWT details
        :rtype: list
        """
        try:
            LOG.info("Querying DGWT details for storage node %s", node_id)
            return self.powerflex_conn.storage_node.get_related(
                node_id, 'Dgwt')
        except Exception as e:
            error_msg = (
                f"Failed to query DGWT details for storage node "
                f"'{node_id}' with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_protection_domain(self, pd_name, pd_id):
        """
        Get protection domain details for create validation
        :param pd_name: Protection domain name
        :type pd_name: str
        :param pd_id: Protection domain ID
        :type pd_id: str
        :return: Protection domain details
        :rtype: dict
        """
        try:
            if pd_id:
                pd_details = self.powerflex_conn.protection_domain.get(
                    entity_id=pd_id)
            else:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={'name': pd_name})

            if isinstance(pd_details, list):
                return pd_details[0] if len(pd_details) > 0 else None
            return pd_details
        except Exception as e:
            error_msg = (
                f"Failed to get protection domain with error '{str(e)}'"
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def _find_ip_in_node(self, sn_details, ip_address):
        """
        Find an IP in the storage node's IP list
        :param sn_details: Storage node details
        :type sn_details: dict
        :param ip_address: IP address to find
        :type ip_address: str
        :return: IP dict if found, else None
        :rtype: dict or None
        """
        ips = sn_details.get('ips', [])
        for ip_entry in ips:
            if ip_entry.get('ip') == ip_address:
                return ip_entry
        return None

    def validate_input_params(self):
        """Validate the input parameters"""
        name_params = ['storage_node_name', 'new_storage_node_name',
                       'storage_node_id']
        msg = "Please provide the valid {0}"

        for n_item in name_params:
            if self.module.params[n_item] is not None and (len(
                    self.module.params[n_item].strip()) or self.
                    module.params[n_item].count(" ") > 0) == 0:
                err_msg = msg.format(n_item)
                self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """
        Perform different actions on storage node based on parameters
        passed in the playbook
        """
        storage_node_name = self.module.params['storage_node_name']
        storage_node_id = self.module.params['storage_node_id']
        new_storage_node_name = self.module.params['new_storage_node_name']
        protection_domain_name = self.module.params['protection_domain_name']
        protection_domain_id = self.module.params['protection_domain_id']
        node_ips = self.module.params['node_ips']
        ip_address = self.module.params['ip_address']
        ip_role = self.module.params['ip_role']
        ip_state = self.module.params['ip_state']
        update_original_pathnames = self.module.params[
            'update_original_pathnames']
        force_failed_devices = self.module.params['force_failed_devices']
        do_query_pds = self.module.params['query_pds']
        do_query_dgwt = self.module.params['query_dgwt']
        state = self.module.params['state']

        result = dict(
            changed=False,
            storage_node_details=None,
            pds_details=None,
            dgwt_details=None,
        )

        # Validate input parameters
        self.validate_input_params()

        # Get current storage node details
        sn_details = self.get(storage_node_id, storage_node_name)

        # Handle absent state (delete)
        if state == 'absent':
            if sn_details:
                result['changed'] = True
                result['diff'] = dict(before=sn_details, after={})
                if not self.module.check_mode:
                    self.delete(sn_details)
            self.module.exit_json(**result)
            return

        # Handle present state
        changed = False

        if not sn_details:
            # Node not found — create if we have create params
            if (protection_domain_name or protection_domain_id) and node_ips:
                # Validate no new_name during create
                if new_storage_node_name:
                    self.module.fail_json(
                        msg="new_storage_node_name is not supported during "
                            "creation of storage node. Please try with "
                            "storage_node_name.")
                    return

                # Get protection domain
                pd = self.get_protection_domain(
                    protection_domain_name, protection_domain_id)
                if not pd:
                    self.module.fail_json(
                        msg=f"Protection domain "
                            f"'{protection_domain_name or protection_domain_id}'"
                            f" not found.")
                    return

                # Format IPs for SDK
                sdk_ips = [{"ip": ip_conf["ip"], "role": ip_conf["role"]}
                           for ip_conf in node_ips]

                sn_details = self.create(
                    storage_node_name, sdk_ips, pd['id'])
                changed = True
            else:
                self.module.fail_json(
                    msg=f"Storage node "
                        f"'{storage_node_name or storage_node_id}' "
                        f"not found.")
                return
        else:
            # Node exists — handle modifications
            node_id = sn_details['id']

            # Rename
            if (new_storage_node_name and
                    new_storage_node_name != sn_details.get('name')):
                changed = True
                if not self.module.check_mode:
                    self.rename(node_id, new_storage_node_name)
                    sn_details = self.get(node_id, None) or sn_details

            # IP operations
            if ip_address and ip_state:
                existing_ip = self._find_ip_in_node(sn_details, ip_address)

                if ip_state == 'present-in-node':
                    if existing_ip:
                        # IP exists — check if role change needed
                        if (ip_role and
                                existing_ip.get('role') != ip_role):
                            changed = True
                            if not self.module.check_mode:
                                sn_details = self.set_ip_role(
                                    node_id, ip_address, ip_role)
                        # else: IP exists with same role — idempotent
                    else:
                        # IP doesn't exist — add it
                        changed = True
                        if not self.module.check_mode:
                            sn_details = self.add_ip(
                                node_id, ip_address, ip_role or 'StorageAndApp')

                elif ip_state == 'absent-in-node':
                    if existing_ip:
                        changed = True
                        if not self.module.check_mode:
                            sn_details = self.remove_ip(node_id, ip_address)
                    # else: IP not on node — idempotent

            # Update original pathnames
            if update_original_pathnames:
                changed = True
                if not self.module.check_mode:
                    sn_details = self.update_pathnames(
                        node_id, force=force_failed_devices)

            # Query PDS
            if do_query_pds:
                result['pds_details'] = self.query_pds(node_id)

            # Query DGWT
            if do_query_dgwt:
                result['dgwt_details'] = self.query_dgwt(node_id)

        result['storage_node_details'] = sn_details
        result['changed'] = changed
        self.module.exit_json(**result)


def main():
    """ Create PowerFlex storage node object and perform actions on it
        based on user input from playbook"""
    obj = PowerFlexStorageNodeV2()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
