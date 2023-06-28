# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock Api response for Unit tests of sdc module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSdcApi:
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
