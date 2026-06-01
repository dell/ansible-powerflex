# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of storage node module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockStorageNodeApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerflex.plugins.modules.storage_node.PowerFlexStorageNode'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils'

    SN_COMMON_ARGS = {
        'hostname': '**.***.**.***',
        'storage_node_name': None,
        'storage_node_id': None,
        'new_storage_node_name': None,
        'protection_domain_name': None,
        'protection_domain_id': None,
        'node_ips': None,
        'ip_address': None,
        'ip_role': None,
        'ip_state': None,
        'update_original_pathnames': False,
        'force_failed_devices': None,
        'query_pds': False,
        'query_dgwt': False,
        'state': 'present',
    }

    SN_NAME = 'test_node'
    SN_NEW_NAME = 'test_node_renamed'
    SN_ID = 'abc12300000000'

    STORAGE_NODE = {
        "id": "abc12300000000",
        "name": "test_node",
        "protectionDomainId": "7bd6457000000000",
        "ipsList": [
            {"ip": "10.0.0.1", "role": "StorageAndApp"},
        ],
        "pdsPort": 9022,
        "dgwtPort": 9033,
        "links": [],
    }

    STORAGE_NODE_MULTI_IPS = {
        "id": "abc12300000000",
        "name": "test_node",
        "protectionDomainId": "7bd6457000000000",
        "ipsList": [
            {"ip": "10.0.0.1", "role": "StorageAndApp"},
            {"ip": "10.0.0.2", "role": "Storage"},
        ],
        "pdsPort": 9022,
        "dgwtPort": 9033,
        "links": [],
    }

    PDS_DETAILS = [
        {"id": "pds00100000000", "name": "pds_1", "storageNodeId": "abc12300000000"},
    ]

    DGWT_DETAILS = [
        {"id": "dgwt00100000000", "name": "dgwt_1", "storageNodeId": "abc12300000000"},
    ]

    @staticmethod
    def get_failed_msgs(response_type):
        error_msg = {
            'get_sn_failed_msg': "Failed to get the storage node",
            'empty_sn_msg': "Please provide the valid storage_node_name",
            'node_not_found': "not found",
            'rename_sn_exception': "Failed to rename storage node",
            'add_ip_exception': "Failed to add IP to storage node",
            'remove_ip_exception': "Failed to remove IP from storage node",
            'set_ip_role_exception': "Failed to set IP role for storage node",
            'update_pathnames_exception': "Failed to update original pathnames",
            'query_pds_exception': "Failed to query PDS details",
            'query_dgwt_exception': "Failed to query DGWT details",
            'ip_addr_required': "ip_address is required",
            'mutually_exclusive': "mutually exclusive",
        }
        return error_msg.get(response_type)
