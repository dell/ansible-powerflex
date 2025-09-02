# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of Device V2 module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockDeviceV2Api:
    MODULE_UTILS_PATH = "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"

    DEVICE_NAME_1 = "ansible_device_1"
    DEVICE_ID_1 = "3fef781c00080000"
    DG_ID_1 = "4eeb305100000001"
    DG_NAME_1 = "DG_1"
    NODE_ID_1 = "6af03fc500000008"
    NODE_NAME_1 = "NODE_1"
    PATH_1 = "/dev/sdb"

    DEVICE_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "current_pathname": None,
        "device_id": None,
        "device_name": None,
        "storage_node_name": None,
        "storage_node_id": None,
        "device_group_name": None,
        "device_group_id": None,
        "media_type": None,
        "new_device_name": None,
        "capacity_limit_gb": None,
        "force": None,
        "clear_error": None,
        "state": None
    }

    DEVICE_GET_LIST = [
        {
            "capacityLimitInKb": 1073479680,
            "deviceCurrentPathName": PATH_1,
            "deviceOriginalPathName": PATH_1,
            "id": DEVICE_ID_1,
            "mediaType": "SSD",
            "name": DEVICE_NAME_1,
            "deviceGroupId": DG_ID_1,
            "storageNodeId": NODE_ID_1,
        }
    ]
    NODE_DETAILS_1 = [
        {
            "name": NODE_NAME_1,
            "id": NODE_ID_1
        }
    ]
    DG_DETAILS_1 = [
        {
            "name": DG_NAME_1,
            "id": DG_ID_1
        }
    ]

    RESPONSE_EXEC_DICT = {
        "get_device_exception": "Failed to get the device with error ",
        "get_storage_node_empty": (f"Unable to find the storage node with {NODE_ID_1}. "
                                   "Please enter a valid storage node name/id."),
        "get_storage_node_exception": f"Failed to get the storage node {NODE_ID_1} with error ",
        "get_device_group_exception": f"Failed to get the device group {DG_ID_1} with error ",
        "get_device_group_empty": (f"Unable to find the device group with {DG_ID_1}. "
                                   "Please enter a valid device group name/id."),
        "create_device_exception": "Creation of device failed with error ",
        "create_device_with_id": "Should Not provide device_id for creation of device.",
        "create_device_with_empty_name": "Provide valid device_name for creation of device.",
        "create_device_without_node": ("Either storage_node_id or storage_node_name "
                                       "needs to be provided for creation of device."),
        "create_device_without_device_group": ("Either device_group_id or device_group_name "
                                               "needs to be provided for creation of device."),
        "create_device_without_path": "Provide current_pathname for creation of device.",
        "create_device_without_media_type": "Provide media_type for creation of device.",
        "rename_device_with_empty_name": "Provide valid name.",
        "rename_exception": f"Failed to update the device {DEVICE_ID_1} with error ",
        "delete_exception": f"Deletion of device {DEVICE_ID_1} failed with error ",
    }

    @staticmethod
    def get_device_exception_response(response_type):
        return MockDeviceV2Api.RESPONSE_EXEC_DICT.get(response_type, "")
