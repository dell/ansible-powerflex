# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of protection domain module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockProtectionDomainApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerflex.plugins.modules.protection_domain.PowerFlexProtectionDomain'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils'

    PD_COMMON_ARGS = {
        'hostname': '**.***.**.***',
        'protection_domain_id': None,
        'protection_domain_name': None,
        'protection_domain_new_name': None,
        'is_active': None,
        'network_limits': None,
        'rf_cache_limits': None,
        'state': 'present'
    }
    PD_NAME = 'test_domain'
    PD_NEW_NAME = 'test_domain_new'
    PD_ID = '7bd6457000000000'

    PROTECTION_DOMAIN = [
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

    PROTECTION_DOMAIN_1 = [
        {
            "id": "7bd6457000000000",
            "name": "test_domain",
            "protectionDomainState": "Inactive",
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

    STORAGE_POOL = [
        {
            "protectionDomainId": "7bd6457000000000",
            "rebuildEnabled": True,
            "mediaType": "HDD",
            "name": "pool1",
            "id": "8d1cba1700000000"
        }
    ]

    @staticmethod
    def get_failed_msgs(response_type):
        error_msg = {
            'get_pd_failed_msg': "Failed to get the protection domain ",
            'empty_pd_msg': "Please provide the valid protection_domain_name",
            'overall_limit_msg': "Overall limit cannot be negative. Provide a valid value",
            'new_name_in_create': "protection_domain_new_name/protection_domain_id are not supported during creation of protection domain",
            'create_pd_exception': "operation failed with error",
            'rename_pd_exception': "Failed to update the protection domain 7bd6457000000000 with error",
            'modify_network_limits_exception': "Failed to update the network limits of protection domain",
            'rf_cache_limits_exception': "Failed to update the rf cache limits of protection domain",
            'delete_pd_exception': "Delete protection domain '7bd6457000000000' operation failed with error ''",
            'get_sp_exception': "Failed to get the storage pools present in protection domain",
        }
        return error_msg.get(response_type)
