#!/usr/bin/python

# Copyright: (c) 2025, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" Ansible module for managing device on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
module: device_v2
version_added: '3.0.0'
short_description: Manage Device on Dell PowerFlex
description:
- Managing device on PowerFlex storage system includes
  adding new device, getting details of device,
  modifying attributes of device, and removing device.
- Support only for Powerflex 5.0 versions and above.

author:
- Tao He (@taohe1012) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

options:
  current_pathname:
    description:
    - Full path of the device to be added.
    - Required while adding a device.
    type: str
  device_name:
    description:
    - Device name.
    - Mutually exclusive with I(device_id).
    type: str
  device_id:
    description:
    - Device ID.
    - Mutually exclusive with I(device_name).
    type: str
  device_group_name:
    description:
    - The name of the device group.
    - Required while adding a device.
    - Mutually exclusive with I(device_group_id).
    type: str
  device_group_id:
    description:
    - The ID of the device group.
    - Required while adding a device.
    - Mutually exclusive with I(device_group_name).
    type: str
  storage_node_name:
    description:
    - The name of the storage node.
    - Required while adding a device.
    - Mutually exclusive with I(storage_node_id).
    type: str
  storage_node_id:
    description:
    - The ID of the storage node.
    - Required while adding a device.
    - Mutually exclusive with I(storage_node_name).
    type: str
  new_device_name:
    description:
    - New name of the device.
    type: str
  capacity_limit_gb:
    description:
    - Device capacity limit in GB.
    type: int
  media_type:
    description:
    - Device media types.
    - Required while adding a device.
    type: str
    choices: ['SSD', 'PMEM']
  clear_error:
    description:
    - Using the flag to clear error on a device.
    - If the error continues to exist, the device will return
      to an error state as soon as it is accessed.
    type: bool
  state:
    description:
    - State of the device.
    choices: ['present', 'absent']
    default: 'present'
    type: str
  force:
    description:
    - Using the Force flag to add a device.
    - Using the flag to clear device error state without checking.
    - Use this flag with caution, because all data on the device will be
      destroyed.
    type: bool
attributes:
  check_mode:
    description: Runs task to validate without performing action on the target machine.
    support: full
  diff_mode:
    description: Runs the task to report the changes made or to be made.
    support: full
'''

EXAMPLES = r'''
- name: Create device
  register: device1_result
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    current_pathname: "/dev/sdc"
    device_group_name: "DG1"
    media_type: "SSD"
    storage_node_name: "Node1"

- name: Create device using name with force flag
  register: device2_result
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    current_pathname: "/dev/sdd"
    device_group_id: "39a898be00000000"
    storage_node_id: "03b589bf00000003"
    media_type: "SSD"
    device_name: "node1-d2"
    force: true
    state: "present"

- name: Get device details using device_id
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    device_id: "{{ device1_result.device_details.id }}"
    state: "present"

- name: Get device details using (current_pathname, storage_node_name)
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    current_pathname: "/dev/sdd"
    storage_node_name: "Node1"
    state: "present"

- name: Get device details using (current_pathname, storage_node_id)
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    current_pathname: "/dev/sdd"
    storage_node_id: "03b589bf00000003"
    state: "present"

- name: Rename device
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    device_id: "{{ device1_result.device_details.id }}"
    new_device_name: "node1-d3"
    state: "present"

- name: Clear device error
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    device_id: "{{ device1_result.device_details.id }}"
    clear_error: true
    force: true
    state: "present"

- name: Clear device error with force flag
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    device_name: "{{ device2_result.device_details.name }}"
    clear_error: true
    force: true
    state: "present"

- name: Modify device capacity limit
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    device_name: "{{ device2_result.device_details.name }}"
    capacity_limit_gb: 500
    state: "present"

- name: Remove device using device_id
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    device_id: "{{ device1_result.device_details.id }}"
    state: "absent"

- name: Remove device using (current_pathname, storage_node_name)
  dellemc.powerflex.device_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    current_pathname: "/dev/sdd"
    storage_node_name: "Node1"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
device_details:
    description: Details of the device.
    returned: When device exists
    type: dict
    contains:
        id:
            description: Device ID.
            type: str
        name:
            description: Device name.
            type: str
        deviceCurrentPathname:
            description: Device current path name.
            type: str
        deviceOriginalPathname:
            description: Device original path name.
            type: str
        deviceState:
            description: Indicates device state.
            type: str
        errorState:
            description: Indicates error state.
            type: str
        capacityLimitInKb:
            description: Device capacity limit in KB.
            type: int
        maxCapacityInKb:
            description: Maximum device capacity in KB.
            type: int
        deviceGroupId:
            description: Device group ID.
            type: str
        longSuccessfulIos:
            description: Indicates long successful I/O operations.
            type: dict
        storageNodeId:
            description: Storage node ID.
            type: str
        updateConfiguration:
            description: Indicates whether configuration update is enabled.
            type: bool
        ledSetting:
            description: LED setting state.
            type: str
        aggregatedState:
            description: Indicates aggregated device state.
            type: str
        temperatureState:
            description: Indicates temperature state.
            type: str
        ssdEndOfLifeState:
            description: Indicates SSD end of life state.
            type: str
        modelName:
            description: Device model name.
            type: str
        serialNumber:
            description: Device serial number.
            type: str
        deviceType:
            description: Indicates device type.
            type: str
        mediaType:
            description: Indicates media type.
            type: str
        vendorName:
            description: Device vendor name.
            type: str
        raidControllerSerialNumber:
            description: RAID controller serial number.
            type: str
        firmwareVersion:
            description: Device firmware version.
            type: str
        cacheLookAheadActive:
            description: Indicates cache look-ahead active state.
            type: bool
        writeCacheActive:
            description: Indicates write cache active state.
            type: bool
        ataSecurityActive:
            description: Indicates ATA security active state.
            type: bool
        capacity:
            description: Device capacity in bytes.
            type: int
        logicalSectorSizeInBytes:
            description: Logical sector size in bytes.
            type: int
        physicalSectorSizeInBytes:
            description: Physical sector size in bytes.
            type: int
        mediaFailing:
            description: Indicates if media is failing.
            type: bool
        autoDetectMediaType:
            description: Auto-detection result of media type.
            type: str
        storageProps:
            description: Storage device properties.
            type: dict
        persistentChecksumState:
            description: Indicates persistent checksum state.
            type: str
    sample: {
        "fglNvdimmWriteCacheSize": null,
        "deviceCurrentPathName": "/dev/sdd",
        "rfcacheErrorDeviceDoesNotExist": false,
        "logicalSectorSizeInBytes": 0,
        "deviceOriginalPathName": "/dev/sdd",
        "fglNvdimmMetadataAmortizationX100": null,
        "capacity": 0,
        "name": null,
        "serialNumber": null,
        "mediaType": "SSD",
        "accelerationPoolId": null,
        "rfcacheProps": null,
        "sdsId": null,
        "storagePoolId": null,
        "capacityLimitInKb": 1073479680,
        "errorState": "None",
        "storageNodeId": "03b589bf00000003",
        "externalAccelerationType": "None",
        "accelerationProps": null,
        "ssdEndOfLifeState": "NeverFailed",
        "temperatureState": "NeverFailed",
        "aggregatedState": "NeverFailed",
        "spSdsId": null,
        "deviceState": "Normal",
        "storageProps": null,
        "autoDetectMediaType": null,
        "longSuccessfulIos": {
        "shortWindow": null,
        "mediumWindow": null,
        "longWindow": null
        },
        "maxCapacityInKb": 1073479680,
        "ledSetting": "Off",
        "modelName": null,
        "deviceType": "Unknown",
        "vendorName": null,
        "raidControllerSerialNumber": null,
        "firmwareVersion": null,
        "cacheLookAheadActive": false,
        "writeCacheActive": false,
        "ataSecurityActive": false,
        "physicalSectorSizeInBytes": 0,
        "mediaFailing": false,
        "slotNumber": "N/A",
        "persistentChecksumState": "StateInvalid",
        "capacityInMb": 1048576,
        "usableCapacityInMb": 1048320,
        "deviceGroupId": "39a898be00000000",
        "id": "e7ffaabf00030002",
        "links": [
        {
            "rel": "self",
            "href": "/api/instances/Device::e7ffaabf00030002"
        },
        {
            "rel": "/dtapi/rest/v1/metrics/query",
            "href": "/dtapi/rest/v1/metrics/query",
            "body": {
            "resource_type": "device",
            "ids": [
                "e7ffaabf00030002"
            ]
            }
        },
        {
            "rel": "/api/parent/relationship/deviceGroupId",
            "href": "/api/instances/DeviceGroup::39a898be00000000"
        },
        {
            "rel": "/api/parent/relationship/storageNodeId",
            "href": "/api/instances/StorageNode::03b589bf00000003"
        }
        ]
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import utils
import copy

LOG = utils.get_logger('device_v2')


@powerflex_compatibility(min_ver='5.0', predecessor='device')
class PowerFlexDeviceV2(PowerFlexBase):
    """Class with device operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        mutually_exclusive = [["storage_node_name", "storage_node_id"],
                              ['device_group_name', 'device_group_id'],
                              ['device_name', 'device_id']]
        ansible_module_params = {
            'argument_spec': get_powerflex_device_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive
        }
        super().__init__(AnsibleModule, ansible_module_params)
        super().check_module_compatibility()

        self.result = dict(
            changed=False,
            device_details={},
            diff={}
        )

    def validate_create_parameters(self, device_params):
        """Validate the input parameters
        :param device_params: The dict of device parameters
        :type device_params: dict
        """

        if device_params['device_id']:
            self.module.fail_json(msg="Should Not provide device_id for creation of device.")
        if device_params['media_type'] is None or len(device_params['media_type'].strip()) == 0:
            self.module.fail_json(msg="Provide media_type for creation of device.")
        if device_params['current_pathname'] is None or len(device_params['current_pathname'].strip()) == 0:
            self.module.fail_json(msg="Provide current_pathname for creation of device.")
        if device_params['device_name'] is not None and len(device_params['device_name'].strip()) == 0:
            self.module.fail_json(msg="Provide valid device_name for creation of device.")

        dg_identify = device_params["device_group_id"] \
            if device_params["device_group_id"] else device_params["device_group_name"]
        if dg_identify is None or len(dg_identify.strip()) == 0:
            self.module.fail_json(msg="Either device_group_id or device_group_name "
                                  "needs to be provided for creation of device.")

        node_identify = device_params["storage_node_id"] \
            if device_params["storage_node_id"] else device_params["storage_node_name"]
        if node_identify is None or len(node_identify.strip()) == 0:
            self.module.fail_json(msg="Either storage_node_id or storage_node_name "
                                  "needs to be provided for creation of device.")

    def get_storage_node(self, storage_node_name=None, storage_node_id=None):
        """Get storage node details
            :param storage_node_name: Name of the storage node
            :param storage_node_id: ID of the storage node
            :return: storage node details
            :rtype: dict
        """
        name_or_id = storage_node_name if storage_node_name \
            else storage_node_id
        try:
            node_details = None
            if storage_node_id:
                node_details = self.powerflex_conn.storage_node.get(
                    filter_fields={'id': storage_node_id})

            if storage_node_name:
                node_details = self.powerflex_conn.storage_node.get(
                    filter_fields={'name': storage_node_name})

            if not node_details or len(node_details) == 0:
                error_msg = (f"Unable to find the storage node with {name_or_id}. "
                             "Please enter a valid storage node name/id.")
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            return node_details[0]

        except Exception as e:
            error_msg = (f"Failed to get the storage node {name_or_id} with "
                         f"error {str(e)}")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_device_group(self, device_group_id=None, device_group_name=None):
        """Get device group details
            :param device_group_name: Name of the device group.
            :param device_group_id: ID of the device group.
            :return: device group details
            :rtype: dict
        """
        name_or_id = device_group_name if device_group_name \
            else device_group_id
        try:
            dg_details = None
            if device_group_id:
                dg_details = self.powerflex_conn.device_group.get(
                    filter_fields={'id': device_group_id})

            if device_group_name:
                dg_details = self.powerflex_conn.device_group.get(
                    filter_fields={'name': device_group_name})

            if not dg_details or len(dg_details) == 0:
                error_msg = (f"Unable to find the device group with {name_or_id}. "
                             "Please enter a valid device group name/id.")
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            return dg_details[0]

        except Exception as e:
            error_msg = (f"Failed to get the device group {name_or_id} with "
                         f"error {str(e)}")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_device(self, current_pathname=None, storage_node_name=None,
                   storage_node_id=None, device_id=None, device_name=None):
        """Get device details
            :param current_pathname: Device path name.
            :type current_pathname: str
            :param storage_node_name: Storage node name.
            :type storage_node_name: str
            :param storage_node_id: Storage node ID.
            :type storage_node_id: str
            :param device_name: Name of the device.
            :param device_id: ID of the device.
            :return: device details
        """
        try:
            device_details = None
            if device_id:
                device_details = self.powerflex_conn.device.get(
                    filter_fields={'id': device_id})
            elif device_name:
                device_details = self.powerflex_conn.device.get(
                    filter_fields={'name': device_name})
            elif current_pathname:
                if storage_node_name and not storage_node_id:
                    storage_node_id = self.get_storage_node(storage_node_name=storage_node_name)['id']
                if storage_node_id:
                    device_details = self.powerflex_conn.device.get(
                        filter_fields={'deviceCurrentPathName': current_pathname,
                                       'storageNodeId': storage_node_id})

            if not device_details or len(device_details) == 0:
                msg = "Unable to find the device."
                LOG.info(msg)
                return None

            node_details = self.get_storage_node(storage_node_id=device_details[0]['storageNodeId'])
            dg_details = self.get_device_group(device_group_id=device_details[0]['deviceGroupId'])
            device_details[0]['storageNodeName'] = node_details['name']
            device_details[0]['deviceGroupName'] = dg_details['name']
            return device_details[0]

        except Exception as e:
            errormsg = f'Failed to get the device with error {str(e)}'
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def create_device(self, media_type, device_group_id, storage_node_id,
                      current_pathname, device_name=None, force=None):
        """Create device
            :param media_type: Media type of device.
            :type media_type: str
            :param device_group_id: Device group ID.
            :type device_group_id: str
            :param storage_node_id: Storage node ID.
            :type storage_node_id: str
            :param device_name: Name of the device.
            :type device_name: str
            :param current_pathname: Pathname of the device.
            :type current_pathname: str
            :param force: Force adding the device.
            :type force: bool
            :return: Details of the device, if created.
            :rtype: dict
        """

        try:
            device_id = None
            if not self.module.check_mode:
                device_id = self.powerflex_conn.device.create(
                    current_pathname=current_pathname,
                    media_type=media_type,
                    device_group_id=device_group_id,
                    node_id=storage_node_id,
                    force=force,
                    name=device_name)['id']
            return self.get_device(device_id=device_id)

        except Exception as e:
            errormsg = f'Creation of device failed with error {str(e)}'
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def delete_device(self, device_id):
        """Delete device
            :param device_id: The ID of the device.
            :return: Details of the device.
        """
        try:
            if not self.module.check_mode:
                self.powerflex_conn.device.delete(device_id)
            return self.get_device(device_id=device_id)

        except Exception as e:
            errormsg = (f'Deletion of device {device_id} '
                        f'failed with error {str(e)}')
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_diff_after(self, device_params, device_details):
        """Get diff between playbook input and device details
        :param device_details: Dictionary of device details
        :param device_params: Dictionary of parameters input from playbook
        :return: Dictionary of parameters of differences"""

        if device_params["state"] == "absent":
            return {}
        diff_dict = {}
        if device_details is None:
            diff_dict = {
                "media_type": device_params['media_type'],
                "device_group_id": device_params['device_group_id'],
                "storage_node_id": device_params['storage_node_id'],
                "current_pathname": device_params['current_pathname']
            }
            if device_params["device_name"]:
                diff_dict["device_name"] = device_params["device_name"]
            if device_params["force"]:
                diff_dict["force"] = device_params["force"]
        else:
            diff_dict = copy.deepcopy(device_details)
            diff_dict.pop("links", None)
            modify_dict = self.to_modify(diff_dict, device_params)
            for key in modify_dict.keys():
                diff_dict[key] = modify_dict[key]
        return diff_dict

    def to_modify(self, device_details, device_params):
        """Whether to modify the device or not
        :param device_details: Dictionary of device details
        :param device_params: Dictionary of parameters input from playbook
        :return: Dictionary containing the attributes of device which are to be updated.
        """
        modify_dict = {}

        new_name = device_params["new_device_name"]
        if new_name is not None:
            if len(new_name.strip()) == 0:
                self.module.fail_json(msg="Provide valid name.")
            if device_details["name"] is None or new_name != device_details['name']:
                modify_dict['new_device_name'] = new_name

        if device_params["capacity_limit_gb"] is not None and\
                device_params["capacity_limit_gb"] * 1024 * 1024 < device_details['capacityLimitInKb']:
            modify_dict["capacity_limit_gb"] = device_params["capacity_limit_gb"]

        if device_params["clear_error"] is not None and device_params["clear_error"]:
            modify_dict["clear_error"] = True
            if device_params["force"] is not None and device_params["force"]:
                modify_dict["force"] = True

        return modify_dict

    def modify_device(self, device_id, modify_dict):
        """
        Modify the device attributes
        :param device_details: Details of the device.
        :param modify_dict: Dictionary containing the attributes of device which are to be updated.
        :return: True, if the operation is successful.
        """
        try:
            msg = (f"Dictionary containing attributes which are to be"
                   f" updated is {str(modify_dict)}.")
            LOG.info(msg)

            if not self.module.check_mode:
                if "new_device_name" in modify_dict:
                    self.powerflex_conn.device.rename(device_id, modify_dict["new_device_name"])
                    msg = f"The name of the Device is updated to {modify_dict['new_device_name']} successfully."
                    LOG.info(msg)

                if "capacity_limit_gb" in modify_dict:
                    self.powerflex_conn.device.set_capacity_limit(device_id, modify_dict["capacity_limit_gb"])
                    msg = f"The capacity limit is updated to {modify_dict['capacity_limit_gb']} successfully."
                    LOG.info(msg)

                if "clear_error" in modify_dict:
                    self.powerflex_conn.device.clear_errors(device_id, modify_dict["force"])
                    LOG.info("The device error is cleared successfully.")

            return True, self.get_device(device_id=device_id)

        except Exception as e:
            err_msg = (f"Failed to update the device {device_id} "
                       f"with error {str(e)}")
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)


def get_powerflex_device_parameters():
    """This method provide parameter required for the device_v2 module on PowerFlex"""
    return dict(
        device_name=dict(type='str'),
        device_id=dict(type='str'),
        new_device_name=dict(type='str'),
        device_group_name=dict(type='str'),
        device_group_id=dict(type='str'),
        storage_node_id=dict(type='str'),
        storage_node_name=dict(type='str'),
        current_pathname=dict(type='str'),
        media_type=dict(type='str', choices=['SSD', 'PMEM']),
        capacity_limit_gb=dict(type='int'),
        force=dict(type='bool'),
        clear_error=dict(type='bool'),
        state=dict(default='present', choices=['present', 'absent'])
    )


class DeviceCreateHandler():
    def handle(self, device_object, device_params, device_details):
        if device_params['state'] == 'present' and not device_details:
            device_object.validate_create_parameters(device_params=device_params)
            device_group_id = device_params["device_group_id"]
            if device_params["device_group_name"]:
                device_group_id = device_object.get_device_group(
                    device_group_name=device_params["device_group_name"])["id"]
            storage_node_id = device_params["storage_node_id"]
            if device_params["storage_node_name"]:
                storage_node_id = device_object.get_storage_node(
                    storage_node_name=device_params["storage_node_name"])["id"]

            device_details = device_object.create_device(
                media_type=device_params["media_type"],
                device_group_id=device_group_id,
                storage_node_id=storage_node_id,
                current_pathname=device_params["current_pathname"],
                device_name=device_params["device_name"],
                force=device_params["force"])
            device_object.result['changed'] = True
        DeviceModifyHandler().handle(device_object, device_params, device_details)


class DeviceModifyHandler():
    def handle(self, device_object, device_params, device_details):
        if device_params['state'] == 'present' and device_details:
            modify_dict = device_object.to_modify(device_details, device_params)
            if modify_dict:
                changed, device_details = device_object.modify_device(device_details['id'], modify_dict)
                device_object.result['changed'] |= changed
        DeviceDeleteHandler().handle(device_object, device_params, device_details)


class DeviceDeleteHandler():
    def handle(self, device_object, device_params, device_details):
        deleteFlag = False
        if device_params['state'] == 'absent' and device_details:
            device_details = device_object.delete_device(device_details['id'])
            device_object.result['changed'] = True
            deleteFlag = True
        DeviceExitHandler().handle(device_object, device_details, deleteFlag)


class DeviceExitHandler():
    def handle(self, device_object, device_details, deleteFlag=False):
        if device_object.module._diff:
            after_dict = copy.deepcopy(device_details) if device_details else {}
            after_dict = {} if deleteFlag else after_dict
            after_dict.pop("links", None)
            device_object.result["diff"]["after"].update(after_dict)
        device_object.result['device_details'] = device_details
        device_object.module.exit_json(**device_object.result)


class DeviceHandler():
    def handle(self, device_object, device_params):
        device_details = device_object.get_device(
            current_pathname=device_params['current_pathname'],
            storage_node_name=device_params['storage_node_name'],
            storage_node_id=device_params['storage_node_id'],
            device_name=device_params['device_name'],
            device_id=device_params['device_id'])

        before_dict = {}
        diff_dict = {}
        diff_dict = device_object.get_diff_after(device_params, device_details)
        if device_details is None:
            before_dict = {}
        else:
            before_dict = device_details
            before_dict.pop("links", None)
        if device_object.module._diff:
            device_object.result["diff"] = dict(before=before_dict, after=diff_dict)
        DeviceCreateHandler().handle(device_object, device_params, device_details)


def main():
    """ Create PowerFlex device object and perform action on it
        based on user input from playbook"""
    device_obj = PowerFlexDeviceV2()
    DeviceHandler().handle(device_obj, device_obj.module.params)


if __name__ == '__main__':
    main()
