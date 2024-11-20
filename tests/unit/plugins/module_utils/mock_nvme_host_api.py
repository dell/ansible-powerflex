# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of NVMe host module on Dell Technologies PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockNVMeHostApi:
    MODULE_UTILS_PATH = (
        "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"
    )
    COMMON_ARGS = {
        "nqn": None,
        "max_num_paths": None,
        "max_num_sys_ports": None,
        "nvme_host_name": None,
        "nvme_host_new_name": None,
        "state": None,
    }

    @staticmethod
    def create_nvme_host():
        return {"id": "da8f60fd00010000"}

    NVME_HOST_DETAILS = [
        {
            "nqn": "test_nqn",
            "maxNumPaths": 3,
            "maxNumSysPorts": 3,
            "name": "nvme_host_test",
            "hostType": "NVMeHost",
            "id": "da8f60fd00010000",
        }
    ]

    NVME_HOST_NO_NAME_DETAILS = [
        {
            "nqn": "test_nqn",
            "maxNumPaths": 3,
            "maxNumSysPorts": 3,
            "hostType": "NVMeHost",
            "name": None,
            "id": "da8f60fd00010000",
        }
    ]

    RESPONSE_EXEC_DICT = {
        "modify_host": "Failed to modify NVMe host",
        "create_host": "Create NVMe host operation failed",
        "delete_host": "Failed to remove NVMe host",
        "get_host": "Failed to get NVMe host",
        "invalid_params": "Provide valid nqn",
        "modify_host_version_check": "not supported in PowerFlex versions earlier than 4.6"
    }

    INFO_ARRAY_DETAILS = [{
        'mdmCluster': {
            'master': {
                'versionInfo': 'R4_6.0.0'
            }
        }
    }]

    INFO_ARRAY_DETAILS_4_5 = [{
        'mdmCluster': {
            'master': {
                'versionInfo': 'R4_5.0.0'
            }
        }
    }]

    @staticmethod
    def get_exception_response(response_type):
        return MockNVMeHostApi.RESPONSE_EXEC_DICT.get(response_type, "")
