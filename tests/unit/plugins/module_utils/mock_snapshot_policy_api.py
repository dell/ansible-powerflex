# Copyright: (c) 2023, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of snapshot policy module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSnapshotPolicyApi:
    SNAPSHOT_POLICY_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "snapshot_policy_name": None,
        "snapshot_policy_id": None,
        "new_name": None,
        "access_mode": None,
        "secure_snapshots": None,
        "auto_snapshot_creation_cadence": {
            "time": None,
            "unit": "Minute"},
        "num_of_retained_snapshots_per_level": None,
        "source_volume": None,
        "source_volume_state": None,
        "pause": None,
        "state": None
    }

    SNAPSHOT_POLICY_GET_LIST = [
        {
            "autoSnapshotCreationCadenceInMin": 120,
            "id": "15ae842500000004",
            "lastAutoSnapshotCreationFailureReason": "NR",
            "lastAutoSnapshotFailureInFirstLevel": False,
            "maxVTreeAutoSnapshots": 40,
            "name": "Ansible_snap_policy_1",
            "nextAutoSnapshotCreationTime": 1683617581,
            "numOfAutoSnapshots": 0,
            "numOfCreationFailures": 0,
            "numOfExpiredButLockedSnapshots": 0,
            "numOfLockedSnapshots": 0,
            "numOfRetainedSnapshotsPerLevel": [
                40
            ],
            "numOfSourceVolumes": 0,
            "secureSnapshots": False,
            "snapshotAccessMode": "ReadWrite",
            "snapshotPolicyState": "Active",
            "systemId": "0e7a082862fedf0f",
            "timeOfLastAutoSnapshot": 0,
            "timeOfLastAutoSnapshotCreationFailure": 0
        }
    ]

    SNAPSHOT_POLICY_2_GET_LIST = [
        {
            "autoSnapshotCreationCadenceInMin": 120,
            "id": "15ae842500000005",
            "lastAutoSnapshotCreationFailureReason": "NR",
            "lastAutoSnapshotFailureInFirstLevel": False,
            "maxVTreeAutoSnapshots": 40,
            "name": "testing_2",
            "nextAutoSnapshotCreationTime": 1683617581,
            "numOfAutoSnapshots": 0,
            "numOfCreationFailures": 0,
            "numOfExpiredButLockedSnapshots": 0,
            "numOfLockedSnapshots": 0,
            "numOfRetainedSnapshotsPerLevel": [
                40
            ],
            "numOfSourceVolumes": 1,
            "secureSnapshots": False,
            "snapshotAccessMode": "ReadWrite",
            "snapshotPolicyState": "Paused",
            "systemId": "0e7a082862fedf0f",
            "timeOfLastAutoSnapshot": 0,
            "timeOfLastAutoSnapshotCreationFailure": 0
        }
    ]

    VOLUME_GET_LIST = [
        {
            'storagePoolId': 'test_pool_id_1',
            'dataLayout': 'MediumGranularity',
            'vtreeId': 'vtree_id_1',
            'sizeInKb': 8388608,
            'snplIdOfAutoSnapshot': None,
            'volumeType': 'ThinProvisioned',
            'consistencyGroupId': None,
            'ancestorVolumeId': None,
            'notGenuineSnapshot': False,
            'accessModeLimit': 'ReadWrite',
            'secureSnapshotExpTime': 0,
            'useRmcache': False,
            'managedBy': 'ScaleIO',
            'lockedAutoSnapshot': False,
            'lockedAutoSnapshotMarkedForRemoval': False,
            'autoSnapshotGroupId': None,
            'compressionMethod': 'Invalid',
            'pairIds': None,
            'timeStampIsAccurate': False,
            'mappedSdcInfo': None,
            'originalExpiryTime': 0,
            'retentionLevels': [
            ],
            'snplIdOfSourceVolume': None,
            'volumeReplicationState': 'UnmarkedForReplication',
            'replicationJournalVolume': False,
            'replicationTimeStamp': 0,
            'creationTime': 1655878090,
            'name': 'source_volume_name',
            'id': 'source_volume_id'
        }
    ]

    VOLUME_2_GET_LIST = [
        {
            'storagePoolId': 'test_pool_id_1',
            'dataLayout': 'MediumGranularity',
            'vtreeId': 'vtree_id_1',
            'sizeInKb': 8388608,
            'snplIdOfAutoSnapshot': None,
            'volumeType': 'ThinProvisioned',
            'consistencyGroupId': None,
            'ancestorVolumeId': None,
            'notGenuineSnapshot': False,
            'accessModeLimit': 'ReadWrite',
            'secureSnapshotExpTime': 0,
            'useRmcache': False,
            'managedBy': 'ScaleIO',
            'lockedAutoSnapshot': False,
            'lockedAutoSnapshotMarkedForRemoval': False,
            'autoSnapshotGroupId': None,
            'compressionMethod': 'Invalid',
            'pairIds': None,
            'timeStampIsAccurate': False,
            'mappedSdcInfo': None,
            'originalExpiryTime': 0,
            'retentionLevels': [
            ],
            'snplIdOfSourceVolume': "15ae842500000005",
            'volumeReplicationState': 'UnmarkedForReplication',
            'replicationJournalVolume': False,
            'replicationTimeStamp': 0,
            'creationTime': 1655878090,
            'name': 'source_volume_name_2',
            'id': 'source_volume_id_2'
        }
    ]

    SNAPSHOT_POLICY_STATISTICS = {
        "autoSnapshotVolIds": [],
        "expiredButLockedSnapshotsIds": [],
        "numOfAutoSnapshots": 0,
        "numOfExpiredButLockedSnapshots": 0,
        "numOfSrcVols": 0,
        "srcVolIds": []
    }

    @staticmethod
    def get_snapshot_policy_exception_response(response_type):
        if response_type == 'get_vol_details_exception':
            return "Failed to get the volume source_volume_id_2 with error "
        elif response_type == 'get_snapshot_policy_details_exception':
            return "Failed to get the snapshot policy with error "
        elif response_type == 'create_exception':
            return "Creation of snapshot policy failed with error "
        elif response_type == 'create_id_exception':
            return "Creation of snapshot policy is allowed using snapshot_policy_name only, snapshot_policy_id given."
        elif response_type == 'delete_exception':
            return "Deletion of snapshot policy 15ae842500000004 failed with error "
        elif response_type == 'modify_exception':
            return "Failed to update the snapshot policy 15ae842500000004 with error "
        elif response_type == 'source_volume_exception':
            return "Failed to manage the source volume source_volume_id with error "
        elif response_type == 'add_source_volume_wo_vol':
            return "Either id or name of source volume needs to be passed with state of source volume"
        elif response_type == 'add_source_volume_vol_id_name':
            return "id and name of source volume are mutually exclusive"
        elif response_type == 'add_non_existing_source_volume':
            return "Failed to get the volume non_existing_source_volume_name with error Volume with identifier non_existing_source_volume_name not found"
        elif response_type == 'pause_exception':
            return "Failed to pause/resume 15ae842500000004 with error"
