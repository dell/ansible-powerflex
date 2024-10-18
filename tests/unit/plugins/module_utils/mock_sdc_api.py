# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of SDC module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSdcApi:
    MODULE_UTILS_PATH = "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"
    COMMON_ARGS = {
        "sdc_id": None,
        "sdc_ip": None,
        "sdc_name": None, "sdc_new_name": None,
        "performance_profile": None,
        "state": None
    }
    SDC_ID = "07335d3d00000006"

    @staticmethod
    def get_sdc_details():
        return [{
            "id": "07335d3d00000006",
            "installedSoftwareVersionInfo": "R3_6.0.0",
            "kernelBuildNumber": None,
            "kernelVersion": "3.10.0",
            "mapped_volumes": [],
            "mdmConnectionState": "Disconnected",
            "memoryAllocationFailure": None,
            "name": "LGLAP203",
            "osType": "Linux",
            "peerMdmId": None,
            "perfProfile": "HighPerformance",
            "sdcApproved": True,
            "sdcApprovedIps": None,
            "sdcGuid": "F8ECB844-23B8-4629-92BB-B6E49A1744CB",
            "sdcIp": "N/A",
            "sdcIps": None,
            "sdcType": "AppSdc",
            "sdrId": None,
            "socketAllocationFailure": None,
            "softwareVersionInfo": "R3_6.0.0",
            "systemId": "4a54a8ba6df0690f",
            "versionInfo": "R3_6.0.0"
        }]

    RESPONSE_EXEC_DICT = {
        'get_sdc_details_empty_sdc_id_exception': "Please provide valid sdc_id",
        'get_sdc_details_with_exception': "Failed to get the SDC 07335d3d00000006 with error",
        'get_sdc_details_mapped_volumes_with_exception': "Failed to get the volumes mapped to SDC",
        'modify_sdc_throws_exception': "Modifying performance profile of SDC 07335d3d00000006 failed with error",
        'rename_sdc_empty_new_name_exception': "Provide valid SDC name to rename to.",
        'rename_sdc_throws_exception': "Failed to rename SDC",
        'remove_sdc_throws_exception': "Removing SDC 07335d3d00000006 failed with error"
    }

    @staticmethod
    def get_sdc_exception_response(response_type):
        return MockSdcApi.RESPONSE_EXEC_DICT.get(response_type, "")
