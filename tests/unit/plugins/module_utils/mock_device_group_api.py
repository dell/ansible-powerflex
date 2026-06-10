# Copyright: (c) 2026, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Api response for Unit tests of Device Group module on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockDeviceGroupApi:
    """Mock data and helpers for the device_group module unit tests."""

    MODULE_PATH = 'ansible_collections.dellemc.powerflex.plugins.modules.device_group.PowerFlexDeviceGroup'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils'

    DG_COMMON_ARGS = {
        'hostname': '**.***.**.***',
        'device_group_name': None,
        'device_group_id': None,
        'new_device_group_name': None,
        'protection_domain_name': None,
        'protection_domain_id': None,
        'media_type': None,
        'spare_node_count': None,
        'spare_device_count': None,
        'query_usable_capacity': False,
        'state': 'present',
    }

    DG_NAME = 'test_dg'
    DG_NEW_NAME = 'test_dg_renamed'
    DG_ID = '39a898be00000000'
    PD_NAME = 'test_pd'
    PD_ID = '7bd6457000000000'

    DEVICE_GROUP = {
        "id": "39a898be00000000",
        "name": "test_dg",
        "protectionDomainId": "7bd6457000000000",
        "mediaType": "SSD",
        "spareNodeCount": 1,
        "spareDeviceCount": 1,
        "links": [],
    }

    PROTECTION_DOMAIN = {
        "id": "7bd6457000000000",
        "name": "test_pd",
    }

    USABLE_CAPACITY = {
        "39a898be00000000": {"numProtectionSlices": 2},
    }

    @staticmethod
    def get_failed_msgs(response_type):
        """Return the expected failure-message fragment for a given scenario."""
        error_msg = {
            'get_dg_failed_msg': "Failed to get the device group",
            'empty_dg_msg': "Please provide a valid device_group_name",
            'dg_not_found': "not found",
            'rename_dg_exception': "Failed to modify device group",
            'modify_dg_exception': "Failed to modify device group",
            'pd_not_found': "Protection domain",
            'capacity_query_exception': "Failed to query usable capacity",
            'mutually_exclusive': "mutually exclusive",
            'required_one_of': "one of",
        }
        return error_msg.get(response_type)
