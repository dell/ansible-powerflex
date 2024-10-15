# Copyright: (c) 2023, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of Device module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockDeviceApi:
    MODULE_UTILS_PATH = "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"

    DEVICE_NAME_1 = "ansible_device_1"
    DEVICE_ID_1 = "3fef781c00080000"
    PD_ID_1 = "4eeb305100000001"
    PD_NAME_1 = "domain1"
    SDS_ID_1 = "6af03fc500000008"
    SDS_NAME_1 = "ansible_sds_1"
    SP_ID_1 = "7644c68600000008"
    SP_NAME_1 = "ansible_sp_1"
    PATH_1 = "/dev/sdb"

    DEVICE_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "current_pathname": None,
        "device_id": None,
        "device_name": None,
        "sds_name": None,
        "sds_id": None,
        "storage_pool_name": None,
        "storage_pool_id": None,
        "acceleration_pool_name": None,
        "acceleration_pool_id": None,
        "protection_domain_name": None,
        "protection_domain_id": None,
        "external_acceleration_type": None,
        "media_type": None,
        "state": None
    }

    DEVICE_GET_LIST = [
        {
            "accelerationPoolId": SP_ID_1,
            "accelerationPoolName": SP_NAME_1,
            "autoDetectMediaType": "Unknown",
            "capacityLimitInKb": 124718080,
            "deviceCurrentPathName": PATH_1,
            "deviceOriginalPathName": PATH_1,
            "externalAccelerationType": "ReadAndWrite",
            "fglNvdimmWriteCacheSize": 16,
            "id": DEVICE_ID_1,
            "mediaType": "HDD",
            "name": DEVICE_NAME_1,
            "protectionDomainId": PD_ID_1,
            "protectionDomainName": PD_NAME_1,
            "sdsId": SDS_ID_1,
            "sdsName": SDS_NAME_1,
            "spSdsId": "bfe791ff00080000",
            "storagePoolId": SP_ID_1,
            "storagePoolName": SP_NAME_1
        }
    ]
    SDS_DETAILS_1 = [
        {
            "name": SDS_NAME_1,
            "id": SDS_ID_1
        }
    ]
    PD_DETAILS_1 = [
        {
            "name": PD_NAME_1,
            "id": PD_ID_1
        }
    ]
    SP_DETAILS_1 = [
        {
            "name": SP_NAME_1,
            "protectionDomainId": PD_ID_1,
            "id": SP_ID_1
        }
    ]
    AP_DETAILS_1 = [
        {
            "name": SP_NAME_1,
            "protectionDomainId": PD_ID_1,
            "id": SP_ID_1
        }
    ]

    @staticmethod
    def get_device_exception_response(response_type):
        if response_type == 'get_dev_without_SDS':
            return "sds_name or sds_id is mandatory along with device_name. Please enter a valid value"
        elif response_type == 'get_device_details_without_path':
            return "sds_name or sds_id is mandatory along with current_pathname. Please enter a valid value"
        elif response_type == 'get_device_exception':
            return "Failed to get the device with error"
        elif response_type == 'create_id_exception':
            return "Addition of device is allowed using device_name only, device_id given."
        elif response_type == 'empty_path':
            return "Please enter a valid value for current_pathname"
        elif response_type == 'empty_device_name':
            return "Please enter a valid value for device_name."
        elif response_type == 'empty_sds':
            return "Please enter a valid value for "
        elif response_type == 'empty_dev_id':
            return "Please provide valid device_id value to identify a device"
        elif response_type == 'space_in_name':
            return "current_pathname or device_name is mandatory along with sds"
        elif response_type == 'with_required_params':
            return "Please specify a valid parameter combination to identify a device"

    @staticmethod
    def get_device_exception_response1(response_type):
        if response_type == 'modify_exception':
            return "Modification of device attributes is currently not supported by Ansible modules."
        elif response_type == 'delete_exception':
            return f"Remove device '{MockDeviceApi.DEVICE_ID_1}' operation failed with error"
        elif response_type == 'sds_exception':
            return f"Unable to find the SDS with '{MockDeviceApi.SDS_NAME_1}'. Please enter a valid SDS name/id."
        elif response_type == 'pd_exception':
            return f"Unable to find the protection domain with " \
                   f"'{MockDeviceApi.PD_NAME_1}'. Please enter a valid " \
                   f"protection domain name/id"
        elif response_type == 'sp_exception':
            return f"Unable to find the storage pool with " \
                   f"'{MockDeviceApi.SP_NAME_1}'. Please enter a valid " \
                   f"storage pool name/id."
        elif response_type == 'ap_exception':
            return f"Unable to find the acceleration pool with " \
                   f"'{MockDeviceApi.SP_NAME_1}'. Please enter a valid " \
                   f"acceleration pool name/id."
        elif response_type == 'add_exception':
            return "Adding device ansible_device_1 operation failed with error"
        elif response_type == 'add_dev_name_exception':
            return "Please provide valid device_name value for adding a device"
        elif response_type == 'add_dev_path_exception':
            return "Current pathname of device is a mandatory parameter for adding a device. Please enter a valid value"
        elif response_type == 'ext_type_exception':
            return "Storage Pool ID/name or Acceleration Pool ID/name is mandatory along with external_acceleration_type."
        elif response_type == 'add_without_pd':
            return "Protection domain name/id is required to uniquely identify"
