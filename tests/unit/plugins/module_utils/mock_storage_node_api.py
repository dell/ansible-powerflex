# Copyright: (c) 2026, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of Storage Node module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockStorageNodeApi:
    STORAGE_NODE_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "storage_node_name": "node1",
        "storage_node_id": None,
        "storage_node_new_name": None,
        "node_ip_list": None,
        "node_ip_state": None,
        "update_pathnames": None,
        "force_failed_devices": None,
        "state": "present"
    }

    STORAGE_NODE_ID_1 = "8f3bb0cc00000002"
    PROTECTION_DOMAIN_ID_1 = "9300c1f900000000"
    PROTECTION_DOMAIN_NAME_1 = "test_domain"

    STORAGE_NODE_GET_LIST = [
        {
            "id": STORAGE_NODE_ID_1,
            "name": "node1",
            "ipList": [
                {
                    "ip": "10.47.xxx.xxx",
                    "role": "StorageOnly"
                },
                {
                    "ip": "10.46.xxx.xxx",
                    "role": "HostOnly"
                }
            ],
            "protectionDomainId": PROTECTION_DOMAIN_ID_1,
            "links": []
        }
    ]

    PROTECTION_DOMAIN_GET_LIST = [
        {
            "id": PROTECTION_DOMAIN_ID_1,
            "name": PROTECTION_DOMAIN_NAME_1
        }
    ]

    RESPONSE_EXEC_DICT = {
        "get_storage_node_exception": "Failed to get the storage node 'node1' with error ",
        "get_storage_node_not_found": "Storage node with identifier 'node1' not found",
        "add_ip_exception": f"Add IP to storage node '{STORAGE_NODE_ID_1}' operation failed with error ",
        "remove_ip_exception": f"Remove IP from storage node '{STORAGE_NODE_ID_1}' operation failed with error ",
        "update_role_exception": f"Update role of IP for storage node '{STORAGE_NODE_ID_1}' operation failed with error ",
        "rename_exception": f"Rename storage node '{STORAGE_NODE_ID_1}' operation failed with error ",
        "update_pathnames_exception": f"Update pathnames for storage node '{STORAGE_NODE_ID_1}' operation failed with error ",
        "rename_empty_name": "Provide valid value for name for the modification of the storage node.",
        "add_ip_empty_list": "Provide valid values for node_ip_list as 'ip' and 'role' for the modification of the storage node.",
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockStorageNodeApi.RESPONSE_EXEC_DICT.get(response_type, "")
