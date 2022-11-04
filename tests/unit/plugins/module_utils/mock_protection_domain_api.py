# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock Api response for Unit tests of protection domain module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockProtectionDomainApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerflex.plugins.modules.protection_domain.PowerFlexProtectionDomain'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils'

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
    STORAGE_POOL = {
        "storagepool": [
            {
                "protectionDomainId": "7bd6457000000000",
                "rebuildEnabled": True,
                "mediaType": "HDD",
                "name": "pool1",
                "id": "8d1cba1700000000"
            }
        ]
    }

    @staticmethod
    def modify_pd_with_failed_msg(protection_domain_name):
        return "Failed to update the rf cache limits of protection domain " + protection_domain_name + " with error "

    @staticmethod
    def delete_pd_failed_msg(protection_domain_id):
        return "Delete protection domain '" + protection_domain_id + "' operation failed with error ''"

    @staticmethod
    def rename_pd_failed_msg(protection_domain_name):
        return "Failed to update the protection domain " + protection_domain_name + " with error "

    @staticmethod
    def version_pd_failed_msg():
        return "Getting PyPowerFlex SDK version, failed with Error The 'PyPowerFlex' distribution was " \
               "not found and is required by the application"
