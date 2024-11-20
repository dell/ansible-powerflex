# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of SDT module on Dell Technologies PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockSDTApi:
    SDT_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "sdt_name": None,
        "sdt_new_name": None,
        "sdt_ip_list": None,
        "storage_port": None,
        "nvme_port": None,
        "discovery_port": None,
        "maintenance_mode": None,
        "protection_domain_name": None,
        "protection_domain_id": None,
        "state": None,
    }

    SDT_GET_LIST = [
        {
            "ipList": [
                {"role": "StorageAndHost", "ip": "10.47.xxx.xxx"},
                {"role": "StorageAndHost", "ip": "10.46.xxx.xxx"},
            ],
            "sdtState": "Normal",
            "name": "sdt1",
            "systemId": "804696a4dbe1d90f",
            "storagePort": 12200,
            "nvmePort": 4420,
            "discoveryPort": 8009,
            "protectionDomainId": "b4787fa100000000",
            "certificateInfo": None,
            "mdmConnectionState": "Connected",
            "membershipState": "Joined",
            "faultSetId": None,
            "softwareVersionInfo": "R4_5.2100.0",
            "maintenanceState": "NoMaintenance",
            "persistentDiscoveryControllersNum": 0,
            "authenticationError": "None",
            "id": "917d28ed00000000",
            "links": [],
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
                "storagePools": [{"id": "8d1cba1700000000", "name": "pool1"}],
            }
        ]
    }

    RESPONSE_EXEC_DICT = {
        "delete_sdt_exception": "Delete SDT 'sdt1' operation failed with error",
        "rename_sdt_exception": "Failed to update the SDT",
        "create_sdt_exception": "Create SDT sdt2 operation failed with error",
        "get_sdt_exception": "Failed to get the SDT",
        "create_sdt_without_sdt_name": "Provide valid value for name for the creation or modification of the SDT.",
        "create_sdt_without_pd": "Protection Domain is a mandatory parameter",
        "create_sdt_without_sdt_ip_list": "Provide valid values for sdt_ip_list as 'ip' and 'role' for Create or Modify operations",
        "rename_sdt_empty_exception": "Provide valid value for name for the creation or modification of the SDT.",
        "add_ip_list_exception": "Add IP to SDT 'sdt1' operation failed with error",
        "remove_ip_list_exception": "Remove IP from SDT 'sdt1' operation failed with error",
        "set_ip_role_exception": "Update role of IP for SDT 'sdt1' operation failed",
    }

    @staticmethod
    def get_sdt_exception_response(response_type):
        return MockSDTApi.RESPONSE_EXEC_DICT.get(response_type, "")
