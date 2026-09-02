#!/usr/bin/python

# Copyright: (c) 2026, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" Ansible module for managing storage node on Dell Technologies (Dell) PowerFlex 5.x"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: storage_node
version_added: '3.1.0'
short_description: Manage storage node on Dell PowerFlex 5.x

description:
- Dell PowerFlex storage node module includes getting the details of a
  storage node, adding/removing IP addresses, modifying IP roles,
  renaming a storage node, and updating device pathnames.
- This module is supported only on Dell PowerFlex 5.x and later versions.
  There is no Gen1 predecessor module for this entity — the Gen1
  equivalent for SDS management is M(dellemc.powerflex.sds).

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

author:
- Saksham Nautiyal (@Saksham-Nautiyal) <ansible.team@dell.com>

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
  storage_node_new_name:
    description:
    - Used to rename the storage node.
    - Mutually exclusive with I(update_pathnames).
    type: str
  node_ip_list:
    description:
    - Dictionary of IPs and their roles for the storage node.
    - Mutually exclusive with I(update_pathnames).
    - Required together with I(node_ip_state).
    type: list
    elements: dict
    suboptions:
      ip:
        description:
        - IP address of the storage node.
        type: str
        required: true
      role:
        description:
        - Role assigned to the storage node IP address.
        choices: ['Storage', 'App', 'StorageAndApp']
        type: str
        required: true
  node_ip_state:
    description:
    - State of IP with respect to the storage node.
    - Required together with I(node_ip_list).
    choices: ['present-in-node', 'absent-in-node']
    type: str
  update_pathnames:
    description:
    - Trigger a device pathname refresh on the storage node.
    - This is a non-idempotent action — C(changed) is always reported as
      C(true) when set to C(true) (outside check mode).
    - Mutually exclusive with I(node_ip_list) and I(storage_node_new_name).
    type: bool
    default: false
  force_failed_devices:
    description:
    - Force the pathname update for failed devices.
    - Only applicable when I(update_pathnames) is C(true).
    type: bool
    default: false
  state:
    description:
      - The state of the storage node. Only C(present) is supported.
    required: true
    choices: ['present']
    type: str
notes:
  - This module is supported on Dell PowerFlex 5.x and later versions.
  - IP role values are C(Storage), C(App), and C(StorageAndApp).
  - I(state=absent) is not supported — storage node creation and deletion
    are out of scope for this module.
  - I(update_pathnames) always reports C(changed=true) and is mutually
    exclusive with I(node_ip_list) and I(storage_node_new_name).
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get storage node details using name
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    state: "present"

- name: Get storage node details using ID
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_id: "5718253c00000004"
    state: "present"

- name: Add IP to storage node
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    node_ip_list:
      - ip: "10.0.0.2"
        role: "App"
    node_ip_state: "present-in-node"
    state: "present"

- name: Remove IP from storage node
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    node_ip_list:
      - ip: "10.0.0.2"
        role: "App"
    node_ip_state: "absent-in-node"
    state: "present"

- name: Change IP role on storage node
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    node_ip_list:
      - ip: "10.0.0.1"
        role: "StorageAndApp"
    node_ip_state: "present-in-node"
    state: "present"

- name: Rename storage node
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    storage_node_new_name: "node1_new"
    state: "present"

- name: Update device pathnames on storage node
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    update_pathnames: true
    state: "present"

- name: Update device pathnames with force for failed devices
  dellemc.powerflex.storage_node:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_node_name: "node1"
    update_pathnames: true
    force_failed_devices: true
    state: "present"
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
            description: Name of the storage node.
            type: str
        ipsList:
            description: List of IPs and their roles.
            type: list
            contains:
                ip:
                    description: IP address.
                    type: str
                role:
                    description: Role assigned to the IP.
                    type: str
        protectionDomainId:
            description: Associated protection domain ID.
            type: str
        protectionDomainName:
            description: Associated protection domain name.
            type: str
    sample: {
        "id": "e59841fd00000002",
        "name": "node1",
        "ipsList": [
            {
                "ip": "10.0.0.1",
                "role": "Storage"
            }
        ],
        "protectionDomainId": "e59841fd00000001",
        "protectionDomainName": "domain1"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.configuration \
    import Configuration
import copy

LOG = utils.get_logger('storage_node')

IP_ROLE_CHOICES = ['Storage', 'App', 'StorageAndApp']


def get_powerflex_storage_node_parameters():
    """This method provides parameters required for the storage_node module
    on PowerFlex"""
    return dict(
        storage_node_name=dict(),
        storage_node_id=dict(),
        storage_node_new_name=dict(),
        node_ip_list=dict(
            type='list', elements='dict', options=dict(
                ip=dict(required=True),
                role=dict(required=True, choices=IP_ROLE_CHOICES)
            )
        ),
        node_ip_state=dict(choices=['present-in-node', 'absent-in-node']),
        update_pathnames=dict(type='bool', default=False),
        force_failed_devices=dict(type='bool', default=False),
        state=dict(required=True, type='str', choices=['present'])
    )


@powerflex_compatibility(min_ver='5.0')
class PowerFlexStorageNode(PowerFlexBase):
    """Class with storage node operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerflex_gateway_host_parameters()
        self.module_params.update(get_powerflex_storage_node_parameters())

        mut_ex_args = [
            ['storage_node_name', 'storage_node_id'],
            ['update_pathnames', 'node_ip_list'],
            ['update_pathnames', 'storage_node_new_name'],
        ]

        required_one_of_args = [['storage_node_name', 'storage_node_id']]

        required_together_args = [['node_ip_list', 'node_ip_state']]

        ansible_module_params = {
            'argument_spec': get_powerflex_storage_node_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mut_ex_args,
            'required_one_of': required_one_of_args,
            'required_together': required_together_args
        }
        super().__init__(AnsibleModule, ansible_module_params)
        super().check_module_compatibility()

        self.result = dict(
            changed=False,
            storage_node_details={}
        )

    def get_storage_node_details(self, storage_node_name=None, storage_node_id=None):
        """Get storage node details
            :param storage_node_name: Name of the storage node
            :type storage_node_name: str
            :param storage_node_id: ID of the storage node
            :type storage_node_id: str
            :return: Details of storage node if it exists
            :rtype: dict
        """

        id_or_name = storage_node_id if storage_node_id else storage_node_name

        try:
            if storage_node_name:
                storage_node_details = self.powerflex_conn.storage_node.get(
                    filter_fields={'name': storage_node_name})
            else:
                storage_node_details = self.powerflex_conn.storage_node.get(
                    filter_fields={'id': storage_node_id})

            if len(storage_node_details) == 0:
                msg = "Storage node with identifier '%s' not found" % id_or_name
                LOG.info(msg)
                return None

            return storage_node_details[0]

        except Exception as e:
            error_msg = "Failed to get the storage node '%s' with error '%s'" \
                        % (id_or_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_protection_domain(self, protection_domain_id):
        """Get the details of a protection domain in a given PowerFlex storage
        system"""
        return Configuration(self.powerflex_conn, self.module).get_protection_domain(
            protection_domain_id=protection_domain_id)

    def show_output(self, storage_node_id):
        """Show storage node details
            :param storage_node_id: ID of the storage node
            :type storage_node_id: str
            :return: Details of storage node
            :rtype: dict
        """

        try:
            storage_node_details = self.powerflex_conn.storage_node.get(
                filter_fields={'id': storage_node_id})

            if len(storage_node_details) == 0:
                msg = "Storage node with identifier '%s' not found" % storage_node_id
                LOG.error(msg)
                return None

            storage_node_details = storage_node_details[0]

            if 'protectionDomainId' in storage_node_details \
                    and storage_node_details['protectionDomainId']:
                pd_details = self.get_protection_domain(
                    protection_domain_id=storage_node_details['protectionDomainId'])
                storage_node_details['protectionDomainName'] = pd_details['name']

            return storage_node_details

        except Exception as e:
            error_msg = "Failed to get the storage node '%s' with error '%s'" \
                        % (storage_node_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def validate_parameters(self, storage_node_params):
        """Validate the input parameters"""
        new_name = storage_node_params['storage_node_new_name']
        if new_name is not None and len(new_name.strip()) == 0:
            error_msg = "Provide valid value for name for the " \
                        "modification of the storage node."
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def validate_ip_parameter(self, node_ip_list):
        """Validate the IP list input parameters"""
        if node_ip_list is None or len(node_ip_list) == 0:
            error_msg = "Provide valid values for node_ip_list as 'ip' " \
                        "and 'role' for the modification of the storage node."
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def identify_ip_role_add(self, node_ip_list, storage_node_details):
        """Identify IPs to add and roles to update

            :param node_ip_list: List of one or more IP addresses and roles
            :type node_ip_list: list[dict]
            :param storage_node_details: Existing storage node details
            :type storage_node_details: dict
            :return: Tuple of (ips_to_add, roles_to_update)
        """
        existing_ip_role_list = storage_node_details['ipsList'] or []
        ips_to_add = []
        remaining_ip_list = []

        existing_ip_list = [ip['ip'] for ip in existing_ip_role_list]
        for given_ip in node_ip_list:
            if given_ip['ip'] not in existing_ip_list:
                ips_to_add.append(given_ip)
            else:
                remaining_ip_list.append(given_ip)
        LOG.info("IP(s) to be added: %s", ips_to_add)

        roles_to_update = [ip for ip in remaining_ip_list
                           if ip not in existing_ip_role_list]
        LOG.info("Role update needed for: %s", roles_to_update)
        return ips_to_add, roles_to_update

    def identify_ip_role_remove(self, node_ip_list, storage_node_details):
        """Identify IPs to remove

            :param node_ip_list: List of one or more IP addresses and roles
            :type node_ip_list: list[dict]
            :param storage_node_details: Existing storage node details
            :type storage_node_details: dict
            :return: List of IPs to remove
        """
        existing_ip_list = [ip['ip'] for ip in (storage_node_details['ipsList'] or [])]
        ips_to_remove = [ip for ip in node_ip_list if ip['ip'] in existing_ip_list]
        if ips_to_remove:
            LOG.info("IP(s) to remove: %s", ips_to_remove)
        else:
            LOG.info("IP(s) do not exist.")
        return ips_to_remove

    def add_ip(self, storage_node_id, node_ip_list):
        """Add IPs to storage node
            :param storage_node_id: Storage node ID
            :type storage_node_id: str
            :param node_ip_list: List of one or more IP addresses and roles
            :type node_ip_list: list[dict]
            :return: Boolean indicating if add IP operation is successful
        """
        try:
            if not self.module.check_mode:
                for ip in node_ip_list:
                    LOG.info("IP to add: %s", ip)
                    self.powerflex_conn.storage_node.add_ip(
                        storage_node_id, {"ip": ip['ip'], "role": ip['role']})
                    LOG.info("IP added successfully.")
            return True
        except Exception as e:
            error_msg = "Add IP to storage node '%s' operation failed with " \
                        "error '%s'" % (storage_node_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update_role(self, storage_node_id, node_ip_list):
        """Update IP role(s) for a storage node
            :param storage_node_id: Storage node ID
            :type storage_node_id: str
            :param node_ip_list: List of one or more IP addresses and roles
            :type node_ip_list: list[dict]
            :return: Boolean indicating if role update operation is successful
        """
        try:
            if not self.module.check_mode:
                LOG.info("Role updates for: %s", node_ip_list)
                for ip in node_ip_list:
                    LOG.info("ip-role: %s", ip)
                    self.powerflex_conn.storage_node.set_ip_role(
                        storage_node_id, ip['ip'], ip['role'])
                    msg = "The role '%s' for IP '%s' is updated " \
                          "successfully." % (ip['role'], ip['ip'])
                    LOG.info(msg)
            return True
        except Exception as e:
            error_msg = "Update role of IP for storage node '%s' operation " \
                        "failed with error '%s'" % (storage_node_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def remove_ip(self, storage_node_id, node_ip_list):
        """Remove IPs from storage node
            :param storage_node_id: Storage node ID
            :type storage_node_id: str
            :param node_ip_list: List of one or more IP addresses and roles
            :type node_ip_list: list[dict]
            :return: Boolean indicating if remove IP operation is successful
        """
        try:
            if not self.module.check_mode:
                for ip in node_ip_list:
                    LOG.info("IP to remove: %s", ip)
                    self.powerflex_conn.storage_node.remove_ip(
                        storage_node_id, ip['ip'])
                    LOG.info("IP removed successfully.")
            return True
        except Exception as e:
            error_msg = "Remove IP from storage node '%s' operation failed " \
                        "with error '%s'" % (storage_node_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def rename(self, storage_node_id, new_name):
        """Rename storage node
            :param storage_node_id: Storage node ID
            :type storage_node_id: str
            :param new_name: New name for the storage node
            :type new_name: str
            :return: Boolean indicating if rename operation is successful
        """
        try:
            if not self.module.check_mode:
                self.powerflex_conn.storage_node.rename(storage_node_id, new_name)
                LOG.info("Storage node renamed successfully.")
            return True
        except Exception as e:
            error_msg = "Rename storage node '%s' operation failed with " \
                        "error '%s'" % (storage_node_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update_pathnames(self, storage_node_id, force_failed_devices):
        """Trigger device pathname update on storage node
            :param storage_node_id: Storage node ID
            :type storage_node_id: str
            :param force_failed_devices: Force update for failed devices
            :type force_failed_devices: bool
            :return: Boolean indicating if pathname update is successful
        """
        try:
            if not self.module.check_mode:
                LOG.info("Updating pathnames for storage node '%s' with "
                        "force_failed_devices=%s", storage_node_id, force_failed_devices)
                self.powerflex_conn.storage_node.update_original_pathnames(
                    storage_node_id, force=force_failed_devices)
                LOG.info("Storage node pathnames updated successfully.")
            return True
        except Exception as e:
            error_msg = "Update pathnames for storage node '%s' operation " \
                        "failed with error '%s'" % (storage_node_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)


class StorageNodeExitHandler():
    def handle(self, storage_node_obj, storage_node_details):
        if storage_node_details:
            storage_node_obj.result["storage_node_details"] = \
                storage_node_obj.show_output(storage_node_id=storage_node_details['id'])
        else:
            storage_node_obj.result["storage_node_details"] = None
        storage_node_obj.module.exit_json(**storage_node_obj.result)


class StorageNodePathnameUpdateHandler():
    def handle(self, storage_node_obj, storage_node_params, storage_node_details):
        if storage_node_params['state'] == 'present' and storage_node_details \
                and storage_node_params['update_pathnames']:
            storage_node_obj.update_pathnames(
                storage_node_details['id'],
                storage_node_params['force_failed_devices'])
            storage_node_obj.result['changed'] = True

        StorageNodeExitHandler().handle(storage_node_obj, storage_node_details)


class StorageNodeRemoveIPHandler():
    def handle(self, storage_node_obj, storage_node_params, storage_node_details, node_ip_list):
        if storage_node_params['state'] == 'present' and storage_node_details:
            remove_ip_changed = False
            if storage_node_params['node_ip_state'] == "absent-in-node":
                storage_node_obj.validate_ip_parameter(node_ip_list)
                ips_to_remove = storage_node_obj.identify_ip_role_remove(
                    node_ip_list, storage_node_details)
                if ips_to_remove:
                    remove_ip_changed = storage_node_obj.remove_ip(
                        storage_node_details['id'], ips_to_remove)

                if remove_ip_changed:
                    storage_node_obj.result['changed'] = True

        StorageNodePathnameUpdateHandler().handle(
            storage_node_obj, storage_node_params, storage_node_details)


class StorageNodeAddIPHandler():
    def handle(self, storage_node_obj, storage_node_params, storage_node_details, node_ip_list):
        if storage_node_params['state'] == 'present' and storage_node_details:
            add_ip_changed = False
            update_role_changed = False
            if storage_node_params['node_ip_state'] == "present-in-node":
                storage_node_obj.validate_ip_parameter(node_ip_list)
                ips_to_add, roles_to_update = storage_node_obj.identify_ip_role_add(
                    node_ip_list, storage_node_details)
                if ips_to_add:
                    add_ip_changed = storage_node_obj.add_ip(
                        storage_node_details['id'], ips_to_add)
                if roles_to_update:
                    update_role_changed = storage_node_obj.update_role(
                        storage_node_details['id'], roles_to_update)

            if add_ip_changed or update_role_changed:
                storage_node_obj.result['changed'] = True

        StorageNodeRemoveIPHandler().handle(
            storage_node_obj, storage_node_params, storage_node_details, node_ip_list)


class StorageNodeRenameHandler():
    def handle(self, storage_node_obj, storage_node_params, storage_node_details, node_ip_list):
        if storage_node_params['state'] == 'present' and storage_node_details:
            new_name = storage_node_params['storage_node_new_name']
            if new_name is not None and new_name != storage_node_details['name']:
                storage_node_obj.rename(storage_node_details['id'], new_name)
                storage_node_obj.result['changed'] = True

        StorageNodeAddIPHandler().handle(
            storage_node_obj, storage_node_params, storage_node_details, node_ip_list)


class StorageNodeHandler():
    def handle(self, storage_node_obj, storage_node_params):
        storage_node_details = storage_node_obj.get_storage_node_details(
            storage_node_params['storage_node_name'], storage_node_params['storage_node_id'])

        if storage_node_details is None:
            id_or_name = storage_node_params['storage_node_id'] or \
                storage_node_params['storage_node_name']
            error_msg = "Storage node with identifier '%s' not found" % id_or_name
            LOG.error(error_msg)
            storage_node_obj.module.fail_json(msg=error_msg)

        storage_node_obj.validate_parameters(storage_node_params=storage_node_params)
        node_ip_list = copy.deepcopy(storage_node_params['node_ip_list']) \
            if storage_node_params['node_ip_list'] else []

        StorageNodeRenameHandler().handle(
            storage_node_obj, storage_node_params, storage_node_details, node_ip_list)


def main():
    """ Create PowerFlex storage node object and perform action on it
        based on user input from playbook."""
    obj = PowerFlexStorageNode()
    StorageNodeHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
