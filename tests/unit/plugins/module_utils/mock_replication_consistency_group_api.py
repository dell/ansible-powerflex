# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of volume module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockReplicationConsistencyGroupApi:
    RCG_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "rcg_name": None,
        "rcg_id": None,
        "create_snapshot": None, "new_rcg_name": None,
        "rpo": None, "protection_domain_name": None, "protection_domain_id": None,
        "activity_mode": None, "pause": None, "pause_mode": None, "freeze": None,
        "remote_peer": {"hostname": None, "username": None, "password": None,
                        "verifycert": None, "port": None, "protection_domain_name": None,
                        "protection_domain_id": None},
        "target_volume_access_mode": None, "is_consistent": None,
        "rcg_state": None, "force": None,
        "state": None
    }
    RCG_ID = "aadc17d500000000"
    FAIL_MSG = " failed with error"

    @staticmethod
    def get_rcg_details(pause_mode="None", freeze_state="Unfrozen", activity_mode="Active", consistency="Consistent"):
        return [{"protectionDomainId": "b969400500000000",
                 "peerMdmId": "6c3d94f600000000",
                 "remoteId": "2130961a00000000",
                 "remoteMdmId": "0e7a082862fedf0f",
                 "currConsistMode": consistency,
                 "freezeState": freeze_state,
                 "lifetimeState": "Normal",
                 "pauseMode": pause_mode,
                 "snapCreationInProgress": False,
                 "lastSnapGroupId": "e58280b300000001",
                 "lastSnapCreationRc": "SUCCESS",
                 "targetVolumeAccessMode": "NoAccess",
                 "remoteProtectionDomainId": "4eeb304600000000",
                 "remoteProtectionDomainName": "domain1",
                 "failoverType": "None",
                 "failoverState": "None",
                 "activeLocal": True,
                 "activeRemote": True,
                 "abstractState": "Ok",
                 "localActivityState": activity_mode,
                 "remoteActivityState": "Active",
                 "inactiveReason": 11,
                 "rpoInSeconds": 30,
                 "replicationDirection": "LocalToRemote",
                 "disasterRecoveryState": "None",
                 "remoteDisasterRecoveryState": "None",
                 "error": 65,
                 "name": "test_rcg",
                 "type": "User",
                 "id": "aadc17d500000000"}]

    @staticmethod
    def get_exception_response(response_type):
        return "Failed to get the replication consistency group "

    @staticmethod
    def create_snapshot_exception_response(response_type, rcg_id):
        return "Create RCG snapshot for RCG with id " + rcg_id + " operation failed"
