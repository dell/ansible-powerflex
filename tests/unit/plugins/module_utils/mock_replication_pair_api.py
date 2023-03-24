# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock Api response for Unit tests of replication pair module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockReplicationPairApi:
    REPLICATION_PAIR_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "rcg_name": None, "rcg_id": None,
        "pair_id": None, "pair_name": None,
        "pairs": [{"source_volume_name": None, "source_volume_id": None, "target_volume_name": None,
                   "target_volume_id": None}], "pause": None,
        "remote_peer": {"hostname": None, "username": None, "password": None,
                        "verifycert": None, "port": None}, "state": None
    }
    PAIR_ID = "23aa0bc900000001"
    FAIL_MSG = " failed with error"

    @staticmethod
    def get_pair_details(copy_state="Done"):
        return [{"copyType": "OnlineCopy",
                 "id": "23aa0bc900000001",
                 "initialCopyPriority": -1,
                 "initialCopyState": copy_state,
                 "lifetimeState": "Normal",
                 "localActivityState": "RplEnabled",
                 "localVolumeId": "e2bc1fab00000008",
                 "name": None,
                 "peerSystemName": None,
                 "remoteActivityState": "RplEnabled",
                 "remoteCapacityInMB": 8192,
                 "remoteId": "a058446700000001",
                 "remoteVolumeId": "1cda7af20000000d",
                 "remoteVolumeName": "vol",
                 "replicationConsistencyGroupId": "e2ce036b00000002",
                 "userRequestedPauseTransmitInitCopy": False,
                 "links": []}]

    @staticmethod
    def get_volume_details():
        return [{"id": "0001",
                 "name": "volume1"}]
