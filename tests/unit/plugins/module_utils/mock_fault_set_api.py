# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of fault set module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFaultSetApi:
    FAULT_SET_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "protection_domain_name": None,
        "protection_domain_id": None,
        "fault_set_name": None,
        "fault_set_id": None,
        "fault_set_new_name": None,
        "state": None
    }

    FAULT_SET_GET_LIST = [
        {
            "protectionDomainId": "7bd6457000000000",
            "name": "fault_set_name_1",
            "id": "fault_set_id_1",
            "links": []
        }
    ]

    PROTECTION_DOMAIN = {
        "protectiondomain": [
            {
                "id": "7bd6457000000000",
                "name": "test_pd_1",
                "protectionDomainState": "Active",
                "overallIoNetworkThrottlingInKbps": 20480,
                "rebalanceNetworkThrottlingInKbps": 10240,
                "rebuildNetworkThrottlingInKbps": 10240,
                "vtreeMigrationNetworkThrottlingInKbps": 10240,
                "rfcacheEnabled": "false",
                "rfcacheMaxIoSizeKb": 128,
                "rfcacheOpertionalMode": "None",
                "rfcachePageSizeKb": 64,
                "storagePools": [
                    {
                        "id": "8d1cba1700000000",
                        "name": "pool1"
                    }
                ]
            }
        ]
    }

    RESPONSE_EXEC_DICT = {
        'delete_fault_set_exception': "Removing Fault Set fault_set_id_1 failed with error",
        'rename_fault_set_exception': "Failed to rename the fault set instance",
        'create_fault_set_exception': "Create fault set test_fs_1 operation failed",
        'get_fault_set_exception': "Failed to get the Fault Set",
        'create_fault_set_wo_pd_exception': "Provide protection_domain_id/protection_domain_name with fault_set_name.",
        'create_fault_set_empty_name_exception': "Provide valid value for name for the creation/modification of the fault set."
    }

    @staticmethod
    def get_fault_set_exception_response(response_type):
        return MockFaultSetApi.RESPONSE_EXEC_DICT.get(response_type, "")
