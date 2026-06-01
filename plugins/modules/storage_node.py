#!/usr/bin/python

# Copyright: (c) 2025, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing storage nodes on Dell Technologies (Dell) PowerFlex 5.x"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: storage_node
version_added: '3.0.0'
short_description: Managing storage nodes on Dell PowerFlex 5.x

description:
- Managing storage nodes on Dell PowerFlex 5.x.
- This module manages existing storage nodes only. It supports getting
  details, renaming, managing IP addresses (single or bulk via I(node_ips)),
  updating device pathnames, and querying related PDS and DGWT objects.
- Creation and deletion of storage nodes are not supported by this module.

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

author:
- Tao He (@taohe1012) <ansible.team@dell.com>

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
    - Name of the protection domain for node identification and validation.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - ID of the protection domain for node identification and validation.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  node_ips:
    description:
    - List of IP/role configurations for bulk IP management on an existing node.
    - Each item is reconciled independently (add, set role, or remove).
    - Mutually exclusive with I(ip_address).
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
        - IP role. Required when adding or changing the role of an IP.
        type: str
        choices: ['Storage', 'App', 'StorageAndApp']
      ip_state:
        description:
        - Desired state of this IP on the node.
        type: str
        choices: ['present-in-node', 'absent-in-node']
        default: present-in-node
  ip_address:
    description:
    - IP address for single add/remove/set-role operations.
    - Mutually exclusive with I(node_ips).
    type: str
  ip_role:
    description:
    - Role for the IP address.
    type: str
    choices: ['Storage', 'App', 'StorageAndApp']
  ip_state:
    description:
    - State of the IP address on the node (used with I(ip_address)).
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
    - Whether to query PDS details through the storage node.
    type: bool
    default: false
  query_dgwt:
    description:
    - Whether to query DGWT details through the storage node.
    type: bool
    default: false
  state:
    description:
    - State of the storage node.
    - Only C(present) is supported. The module manages existing nodes
      (modify) and does not create or delete storage nodes.
    type: str
    choices: ['present']
    default: present
notes:
  - This module is supported on Dell PowerFlex 5.x and later versions.
  - Storage node creation and deletion are not supported.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get storage node details by name
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    state: "present"

- name: Get storage node details by ID
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_id: "abc12300000000"
    state: "present"

- name: Rename storage node
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    new_storage_node_name: "node1_renamed"
    state: "present"

- name: Add a single IP address to storage node
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    ip_address: "10.0.0.5"
    ip_role: "Storage"
    ip_state: "present-in-node"
    state: "present"

- name: Remove a single IP address from storage node
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    ip_address: "10.0.0.5"
    ip_state: "absent-in-node"
    state: "present"

- name: Manage multiple IP addresses in one task (bulk)
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    node_ips:
      - ip: "10.0.0.5"
        role: "Storage"
        ip_state: "present-in-node"
      - ip: "10.0.0.6"
        role: "App"
        ip_state: "present-in-node"
      - ip: "10.0.0.2"
        ip_state: "absent-in-node"
    state: "present"

- name: Update original pathnames
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    update_original_pathnames: true
    force_failed_devices: true
    state: "present"

- name: Query PDS details through storage node
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    query_pds: true
    state: "present"

- name: Query DGWT details through storage node
  dellemc.powerflex.storage_node:
    hostname: "<your_powerflex_host>"
    username: "<your_username>"
    password: "<your_password>"
    validate_certs: false
    storage_node_name: "node1"
    query_dgwt: true
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
            description: Storage node name.
            type: str
        protectionDomainId:
            description: Protection domain ID.
            type: str
        ipsList:
            description: List of IP addresses and roles.
            type: list
            elements: dict
        pdsPort:
            description: PDS port.
            type: int
        dgwtPort:
            description: DGWT port.
            type: int
    sample: {
        "id": "9aa2541300000000",
        "name": "SN_node1.lab.emc.com",
        "protectionDomainId": "d39bff0700000000",
        "ipsList": [
            {"ip": "10.0.0.1", "role": "StorageAndApp"}
        ],
        "pdsPort": 9022,
        "dgwtPort": 9033
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase, powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils


LOG = utils.get_logger('storage_node')


@powerflex_compatibility(min_ver='5.0')
class PowerFlexStorageNode(PowerFlexBase):
    """Class with storage node operations (modify and query only)"""

    def __init__(self):
        """Define all parameters required by this module"""
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
                    role=dict(type='str',
                              choices=['Storage', 'App', 'StorageAndApp']),
                    ip_state=dict(
                        type='str',
                        choices=['present-in-node', 'absent-in-node'],
                        default='present-in-node'),
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
            state=dict(type='str', choices=['present'], default='present'),
        )

        mut_ex_args = [
            ['storage_node_name', 'storage_node_id'],
            ['protection_domain_name', 'protection_domain_id'],
            ['ip_address', 'node_ips'],
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
        :return: Storage node details if it exists else None
        :rtype: dict or None
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

    def rename(self, node_id, new_name):
        """
        Rename storage node
        :param node_id: ID of the storage node
        :param new_name: New name
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
        :param ip_address: IP address to add
        :param ip_role: Role for the IP
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
        :param ip_address: IP address to remove
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
        :param ip_address: IP address
        :param ip_role: New role
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
        :param force: Force failed devices
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

    @staticmethod
    def _find_ip_in_node(sn_details, ip_address):
        """
        Find an IP in the storage node's IP list
        :param sn_details: Storage node details
        :param ip_address: IP address to find
        :return: IP dict if found, else None
        :rtype: dict or None
        """
        ips = sn_details.get('ipsList', sn_details.get('ips', [])) or []
        for ip_entry in ips:
            if ip_entry.get('ip') == ip_address:
                return ip_entry
        return None

    def _reconcile_ip(self, node_id, sn_details, ip_address, ip_role,
                      ip_state):
        """
        Reconcile a single IP entry against the node's current state.
        :return: tuple (changed, updated_sn_details)
        :rtype: tuple
        """
        existing_ip = self._find_ip_in_node(sn_details, ip_address)

        if ip_state == 'present-in-node':
            if existing_ip:
                if ip_role and existing_ip.get('role') != ip_role:
                    if not self.module.check_mode:
                        sn_details = self.set_ip_role(
                            node_id, ip_address, ip_role) or sn_details
                    return True, sn_details
                return False, sn_details
            if not self.module.check_mode:
                sn_details = self.add_ip(
                    node_id, ip_address, ip_role or 'StorageAndApp') \
                    or sn_details
            return True, sn_details

        # absent-in-node
        if existing_ip:
            if not self.module.check_mode:
                sn_details = self.remove_ip(node_id, ip_address) or sn_details
            return True, sn_details
        return False, sn_details

    def validate_input_params(self):
        """Validate the input parameters"""
        params = self.module.params
        msg = "Please provide the valid {0}"

        for n_item in ['storage_node_name', 'new_storage_node_name',
                       'storage_node_id']:
            value = params.get(n_item)
            if value is not None and value.strip() == '':
                self.module.fail_json(msg=msg.format(n_item))

        if params.get('ip_address') and params.get('node_ips'):
            self.module.fail_json(
                msg="ip_address and node_ips are mutually exclusive. "
                    "Provide only one.")

        if (params.get('ip_state') or params.get('ip_role')) \
                and not params.get('ip_address') and not params.get('node_ips'):
            self.module.fail_json(
                msg="ip_address is required for IP management operations.")

    def perform_module_operation(self):
        """
        Perform different actions on a storage node based on the parameters
        passed in the playbook. This module manages existing nodes only.
        """
        params = self.module.params
        result = dict(
            changed=False,
            storage_node_details=None,
            pds_details=None,
            dgwt_details=None,
        )

        self.validate_input_params()

        sn_details = self.get(params['storage_node_id'],
                              params['storage_node_name'])

        if not sn_details:
            self.module.fail_json(
                msg="Storage node '%s' not found. This module manages "
                    "existing nodes only and does not create nodes."
                    % (params['storage_node_id']
                       or params['storage_node_name']))

        node_id = sn_details['id']
        changed = False

        # Rename
        if params['new_storage_node_name'] and \
                params['new_storage_node_name'] != sn_details.get('name'):
            changed = True
            if not self.module.check_mode:
                self.rename(node_id, params['new_storage_node_name'])
                sn_details = self.get(node_id, None) or sn_details

        # Single IP management
        if params['ip_address']:
            ip_changed, sn_details = self._reconcile_ip(
                node_id, sn_details, params['ip_address'],
                params['ip_role'], params['ip_state'] or 'present-in-node')
            changed = changed or ip_changed

        # Bulk IP management via node_ips
        if params['node_ips']:
            for entry in params['node_ips']:
                ip_changed, sn_details = self._reconcile_ip(
                    node_id, sn_details, entry['ip'], entry.get('role'),
                    entry.get('ip_state') or 'present-in-node')
                changed = changed or ip_changed

        # Update original pathnames
        if params['update_original_pathnames']:
            changed = True
            if not self.module.check_mode:
                sn_details = self.update_pathnames(
                    node_id, force=params['force_failed_devices']) \
                    or sn_details

        # Queries (read-only)
        if params['query_pds']:
            result['pds_details'] = self.query_pds(node_id)

        if params['query_dgwt']:
            result['dgwt_details'] = self.query_dgwt(node_id)

        result['storage_node_details'] = sn_details
        result['changed'] = changed
        self.module.exit_json(**result)


def main():
    """Create PowerFlex storage node object and perform actions on it
       based on user input from the playbook"""
    obj = PowerFlexStorageNode()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
