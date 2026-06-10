#!/usr/bin/python

# Copyright: (c) 2026, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" Ansible module for managing device groups on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
module: device_group
version_added: '3.0.0'
short_description: Manage Device Groups on Dell PowerFlex
description:
- Managing device groups on PowerFlex Gen2 storage systems includes getting
  details of a device group, renaming a device group, updating spare node and
  spare device counts, and querying usable capacity.
- Device group creation and deletion are not supported by this module.
- Support only for PowerFlex 5.0 versions and above.

author:
- Dell Technologies (@dellemc) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

options:
  device_group_name:
    description:
    - The name of the device group.
    - Mutually exclusive with I(device_group_id).
    type: str
  device_group_id:
    description:
    - The ID of the device group.
    - Mutually exclusive with I(device_group_name).
    type: str
  new_device_group_name:
    description:
    - New name for the device group (rename operation).
    type: str
  protection_domain_name:
    description:
    - Name of the protection domain for device group identification/validation.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - ID of the protection domain for device group identification/validation.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  media_type:
    description:
    - Media type of the device group.
    - Query and validation only; it cannot be modified.
    type: str
    choices: ['SSD', 'PMEM']
  spare_node_count:
    description:
    - Spare node count for the device group.
    type: int
  spare_device_count:
    description:
    - Spare device count for the device group.
    type: int
  query_usable_capacity:
    description:
    - Whether to query the usable capacity of the device group.
    - This is a read-only operation.
    type: bool
    default: false
  state:
    description:
    - State of the device group.
    - Only C(present) is supported; the module manages existing device groups
      and does not create or delete them.
    default: present
    choices: ['present']
    type: str
attributes:
  check_mode:
    description: Runs task to validate without performing action on the target machine.
    support: full
  diff_mode:
    description: Runs the task to report the changes made or to be made.
    support: full
'''

EXAMPLES = r'''
- name: Get device group details by name
  dellemc.powerflex.device_group:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "<your_password>"
    validate_certs: "{{ validate_certs }}"
    device_group_name: "DG1"
    state: "present"

- name: Get device group details by ID
  dellemc.powerflex.device_group:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "<your_password>"
    validate_certs: "{{ validate_certs }}"
    device_group_id: "39a898be00000000"
    state: "present"

- name: Rename device group and update spare counts
  dellemc.powerflex.device_group:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "<your_password>"
    validate_certs: "{{ validate_certs }}"
    device_group_name: "DG1"
    new_device_group_name: "DG1_renamed"
    spare_node_count: 2
    spare_device_count: 1
    state: "present"

- name: Query usable capacity for a device group
  dellemc.powerflex.device_group:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "<your_password>"
    validate_certs: "{{ validate_certs }}"
    device_group_id: "39a898be00000000"
    query_usable_capacity: true
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
device_group_details:
    description: Details of the device group.
    returned: When device group exists
    type: dict
    contains:
        id:
            description: Device group ID.
            type: str
        name:
            description: Device group name.
            type: str
        protectionDomainId:
            description: Protection domain ID.
            type: str
        mediaType:
            description: Media type of the device group.
            type: str
        spareNodeCount:
            description: Spare node count.
            type: int
        spareDeviceCount:
            description: Spare device count.
            type: int
        links:
            description: Related resource links.
            type: list
    sample: {
        "id": "39a898be00000000",
        "name": "test_dg",
        "protectionDomainId": "7bd6457000000000",
        "mediaType": "SSD",
        "spareNodeCount": 1,
        "spareDeviceCount": 1,
        "links": []
    }
usable_capacity_details:
    description: Usable capacity details for the device group.
    returned: When query_usable_capacity is true
    type: dict
    sample: {
        "39a898be00000000": {
            "numProtectionSlices": 2
        }
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import utils
import copy

LOG = utils.get_logger('device_group')


@powerflex_compatibility(min_ver='5.0', predecessor=None)
class PowerFlexDeviceGroup(PowerFlexBase):
    """Class with device group operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        mutually_exclusive = [['device_group_name', 'device_group_id'],
                              ['protection_domain_name', 'protection_domain_id']]
        required_one_of = [['device_group_name', 'device_group_id']]
        ansible_module_params = {
            'argument_spec': get_powerflex_device_group_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive,
            'required_one_of': required_one_of,
        }
        super().__init__(AnsibleModule, ansible_module_params)
        super().check_module_compatibility()

        self.result = dict(
            changed=False,
            device_group_details={},
            diff={}
        )

    def validate_input_params(self, dg_params):
        """Validate the input parameters
        :param dg_params: The dict of device group parameters
        :type dg_params: dict
        """
        name = dg_params['device_group_name']
        dg_id = dg_params['device_group_id']
        new_name = dg_params['new_device_group_name']

        if name is not None and len(name.strip()) == 0:
            self.module.fail_json(
                msg="Please provide a valid device_group_name.")
        if new_name is not None and len(new_name.strip()) == 0:
            self.module.fail_json(
                msg="Please provide a valid device_group_name or "
                    "new_device_group_name.")

        if name and dg_id:
            self.module.fail_json(
                msg="parameters are mutually exclusive: "
                    "device_group_name|device_group_id")
        if not name and not dg_id:
            self.module.fail_json(
                msg="one of the following is required: "
                    "device_group_name, device_group_id")

    def get_protection_domain(self, protection_domain_name=None,
                              protection_domain_id=None):
        """Get protection domain details
            :param protection_domain_name: Name of the protection domain.
            :param protection_domain_id: ID of the protection domain.
            :return: protection domain details
            :rtype: dict
        """
        name_or_id = protection_domain_name if protection_domain_name \
            else protection_domain_id
        pd_details = None
        try:
            if protection_domain_id:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={'id': protection_domain_id})
            elif protection_domain_name:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={'name': protection_domain_name})
        except Exception as e:
            error_msg = (f"Failed to get the protection domain {name_or_id} "
                         f"with error {str(e)}")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        if not pd_details or len(pd_details) == 0:
            error_msg = (f"Protection domain with identifier {name_or_id} "
                         "not found. Please enter a valid protection "
                         "domain name/id.")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        return pd_details[0]

    def get_device_group(self, device_group_name=None, device_group_id=None,
                         protection_domain_id=None):
        """Get device group details
            :param device_group_name: Name of the device group.
            :param device_group_id: ID of the device group.
            :param protection_domain_id: ID of the protection domain to scope.
            :return: device group details or None
            :rtype: dict
        """
        try:
            filter_fields = {}
            if device_group_id:
                filter_fields['id'] = device_group_id
            elif device_group_name:
                filter_fields['name'] = device_group_name
            if protection_domain_id:
                filter_fields['protectionDomainId'] = protection_domain_id

            dg_details = self.powerflex_conn.device_group.get(
                filter_fields=filter_fields)

            if not dg_details or len(dg_details) == 0:
                return None
            return dg_details[0]
        except Exception as e:
            error_msg = f"Failed to get the device group with error {str(e)}"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def to_modify(self, device_group_details, dg_params):
        """Determine which attributes need to be modified
        :param device_group_details: Dictionary of device group details
        :param dg_params: Dictionary of parameters input from playbook
        :return: Dictionary of attributes to update
        """
        modify_dict = {}

        new_name = dg_params['new_device_group_name']
        if new_name is not None and len(new_name.strip()) != 0 \
                and new_name != device_group_details.get('name'):
            modify_dict['new_name'] = new_name

        spare_node_count = dg_params['spare_node_count']
        if spare_node_count is not None and \
                spare_node_count != device_group_details.get('spareNodeCount'):
            modify_dict['spare_node_count'] = spare_node_count

        spare_device_count = dg_params['spare_device_count']
        if spare_device_count is not None and \
                spare_device_count != device_group_details.get('spareDeviceCount'):
            modify_dict['spare_device_count'] = spare_device_count

        return modify_dict

    def modify_device_group(self, device_group_id, modify_dict):
        """Modify the device group attributes
        :param device_group_id: ID of the device group.
        :param modify_dict: Dictionary of attributes to update.
        :return: Updated device group details
        """
        try:
            if not self.module.check_mode:
                self.powerflex_conn.device_group.modify(
                    device_group_id,
                    new_name=modify_dict.get('new_name'),
                    spare_node_count=modify_dict.get('spare_node_count'),
                    spare_device_count=modify_dict.get('spare_device_count'))
                msg = (f"Device group {device_group_id} modified with "
                       f"attributes {str(modify_dict)} successfully.")
                LOG.info(msg)
            return self.get_device_group(device_group_id=device_group_id)
        except Exception as e:
            error_msg = (f"Failed to modify device group {device_group_id} "
                         f"with error {str(e)}")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def query_usable_capacity(self, device_group_id):
        """Query the usable capacity of a device group (read-only)
        :param device_group_id: ID of the device group.
        :return: usable capacity details
        """
        try:
            return self.powerflex_conn.device_group.query_usable_capacity(
                device_group_id)
        except Exception as e:
            error_msg = (f"Failed to query usable capacity for device group "
                         f"{device_group_id} with error {str(e)}")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)


def get_powerflex_device_group_parameters():
    """This method provides parameters required for the device_group module"""
    return dict(
        device_group_name=dict(type='str'),
        device_group_id=dict(type='str'),
        new_device_group_name=dict(type='str'),
        protection_domain_name=dict(type='str'),
        protection_domain_id=dict(type='str'),
        media_type=dict(type='str', choices=['SSD', 'PMEM']),
        spare_node_count=dict(type='int'),
        spare_device_count=dict(type='int'),
        query_usable_capacity=dict(type='bool', default=False),
        state=dict(default='present', choices=['present']),
    )


class DeviceGroupModifyHandler():
    def handle(self, device_group_object, dg_params, device_group_details):
        """Apply modifications to the device group when required."""
        if dg_params['state'] == 'present' and device_group_details:
            modify_dict = device_group_object.to_modify(
                device_group_details, dg_params)
            if modify_dict:
                device_group_details = device_group_object.modify_device_group(
                    device_group_details['id'], modify_dict)
                device_group_object.result['changed'] = True
        DeviceGroupQueryHandler().handle(
            device_group_object, dg_params, device_group_details)


class DeviceGroupQueryHandler():
    def handle(self, device_group_object, dg_params, device_group_details):
        """Query usable capacity for the device group when requested."""
        if dg_params['query_usable_capacity'] and device_group_details:
            device_group_object.result['usable_capacity_details'] = \
                device_group_object.query_usable_capacity(
                    device_group_details['id'])
        DeviceGroupExitHandler().handle(
            device_group_object, device_group_details)


class DeviceGroupExitHandler():
    def handle(self, device_group_object, device_group_details):
        """Populate diff and exit the module with the final result."""
        if device_group_object.module._diff:
            after_dict = copy.deepcopy(device_group_details) \
                if device_group_details else {}
            after_dict.pop("links", None)
            device_group_object.result["diff"]["after"] = after_dict
        device_group_object.result['device_group_details'] = \
            device_group_details
        device_group_object.module.exit_json(**device_group_object.result)


class DeviceGroupHandler():
    def handle(self, device_group_object, dg_params):
        """Entry handler: validate, resolve, fetch, then modify/query."""
        device_group_object.validate_input_params(dg_params)

        protection_domain_id = dg_params['protection_domain_id']
        if dg_params['protection_domain_name'] or protection_domain_id:
            protection_domain_id = device_group_object.get_protection_domain(
                protection_domain_name=dg_params['protection_domain_name'],
                protection_domain_id=protection_domain_id)['id']

        device_group_details = device_group_object.get_device_group(
            device_group_name=dg_params['device_group_name'],
            device_group_id=dg_params['device_group_id'],
            protection_domain_id=protection_domain_id)

        if device_group_details is None:
            identifier = dg_params['device_group_name'] \
                if dg_params['device_group_name'] else dg_params['device_group_id']
            error_msg = (f"Device group with identifier {identifier} "
                         "not found.")
            LOG.error(error_msg)
            device_group_object.module.fail_json(msg=error_msg)

        if device_group_object.module._diff:
            before_dict = copy.deepcopy(device_group_details)
            before_dict.pop("links", None)
            device_group_object.result["diff"] = dict(
                before=before_dict, after={})

        DeviceGroupModifyHandler().handle(
            device_group_object, dg_params, device_group_details)


def main():
    """ Create PowerFlex device group object and perform action on it
        based on user input from playbook"""
    device_group_obj = PowerFlexDeviceGroup()
    DeviceGroupHandler().handle(
        device_group_obj, device_group_obj.module.params)


if __name__ == '__main__':
    main()
