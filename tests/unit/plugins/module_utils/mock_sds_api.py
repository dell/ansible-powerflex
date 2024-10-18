# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of SDS module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSDSApi:
    SDS_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "sds_name": "test_node0",
        "sds_id": None,
        "sds_new_name": None,
        "sds_ip_list": None,
        "sds_ip_state": None,
        "rfcache_enabled": None,
        "rmcache_enabled": None,
        "rmcache_size": None,
        "performance_profile": None,
        "protection_domain_name": None,
        "protection_domain_id": None,
        "fault_set_name": None,
        "fault_set_id": None,
        "fault_set_new_name": None,
        "state": None
    }

    SDS_GET_LIST = [
        {
            "authenticationError": "None",
            "certificateInfo": None,
            "configuredDrlMode": "Volatile",
            "drlMode": "Volatile",
            "faultSetId": "test_id_1",
            "fglMetadataCacheSize": 0,
            "fglMetadataCacheState": "Disabled",
            "fglNumConcurrentWrites": 1000,
            "id": "8f3bb0cc00000002",
            "ipList": [
                {
                    "ip": "10.47.xxx.xxx",
                    "role": "all"
                },
                {
                    "ip": "10.46.xxx.xxx",
                    "role": "sdcOnly"
                }
            ],
            "lastUpgradeTime": 0,
            "links": [],
            "maintenanceState": "NoMaintenance",
            "maintenanceType": "NoMaintenance",
            "mdmConnectionState": "Connected",
            "membershipState": "Joined",
            "name": "test_node0",
            "numOfIoBuffers": None,
            "numRestarts": 2,
            "onVmWare": True,
            "perfProfile": "HighPerformance",
            "port": 7072,
            "protectionDomainId": "9300c1f900000000",
            "protectionDomainName": "test_domain",
            "raidControllers": None,
            "rfcacheEnabled": True,
            "rfcacheErrorApiVersionMismatch": False,
            "rfcacheErrorDeviceDoesNotExist": False,
            "rfcacheErrorInconsistentCacheConfiguration": False,
            "rfcacheErrorInconsistentSourceConfiguration": False,
            "rfcacheErrorInvalidDriverPath": False,
            "rfcacheErrorLowResources": False,
            "rmcacheEnabled": True,
            "rmcacheFrozen": False,
            "rmcacheMemoryAllocationState": "AllocationPending",
            "rmcacheSizeInKb": 131072,
            "rmcacheSizeInMb": 128,
            "sdsConfigurationFailure": None,
            "sdsDecoupled": None,
            "sdsReceiveBufferAllocationFailures": None,
            "sdsState": "Normal",
            "softwareVersionInfo": "R3_6.0.0"
        }
    ]

    PROTECTION_DOMAIN = {
        "protectiondomain": [
            {
                "id": "7bd6457000000000",
                "name": "test_domain",
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

    FAULT_SET_GET_LIST = [
        {
            "protectionDomainId": "test_domain",
            "name": "fault_set_name",
            "id": "fault_set_id",
            "links": []
        }
    ]

    RESPONSE_EXEC_DICT = {
        "delete_sds_exception": "Delete SDS '8f3bb0cc00000002' operation failed with error",
        "rename_sds_exception": "Failed to update the SDS",
        "create_sds_exception": "Create SDS test_node0 operation failed with error",
        "get_sds_exception": "Failed to get the SDS",
        "rmcache_size_exception": "RM cache size can be set only when RM cache is enabled",
        "create_sds_wo_sds_name": "Please provide valid sds_name value for creation of SDS.",
        "create_sds_wo_pd": "Protection Domain is a mandatory parameter",
        "create_sds_wo_sds_ip_list": "Please provide valid sds_ip_list values for " +
                                     "creation of SDS.",
        "create_sds_incorrect_sds_ip_state": "Incorrect IP state given for creation of SDS.",
        "create_sds_sds_id": "Creation of SDS is allowed using sds_name " +
                             "only, sds_id given.",
        "create_sds_sds_new_name": "sds_new_name parameter is not supported " +
                                   "during creation of a SDS. Try renaming the " +
                                   "SDS after the creation.",
        "rename_sds_empty_exception": "Provide valid value for name for the creation/modification of the SDS.",
        "add_ip_exception": "Add IP to SDS '8f3bb0cc00000002' operation failed with error ",
        "remove_ip_exception": "Remove IP from SDS '8f3bb0cc00000002' operation failed with error ",
        "set_ip_role_exception": "Update role of IP for SDS '8f3bb0cc00000002' operation failed"
    }

    @staticmethod
    def get_sds_exception_response(response_type):
        return MockSDSApi.RESPONSE_EXEC_DICT.get(response_type, "")
