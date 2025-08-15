# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of snapshot module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockSnapshotApi:
    MODULE_UTILS_PATH = "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"
    SNAPSHOT_ID = "04d17a4400000016"
    SNAPSHOT_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "snapshot_name": None,
        "snapshot_id": None,
        "snapshot_new_name": None,
        "vol_name": None,
        "vol_id": None,
        "desired_retention": None,
        "retention_unit": None,
        "remove_mode": None,
        "state": None,
    }

    SNAPSHOT_GET_LIST = [
        {
            "genType": "EC",
            "mappedSdcInfo": None,
            "managedBy": "ScaleIO",
            "originalExpiryTime": 0,
            "retentionLevels": [],
            "snplIdOfSourceVolume": None,
            "volumeReplicationState": "UnmarkedForReplication",
            "replicationJournalVolume": False,
            "replicationTimeStamp": 0,
            "name": "test_snapshot",
            "creationTime": 1751957191,
            "compressionMethod": "NotApplicable",
            "vtreeId": "c2579d4c0000000c",
            "sizeInKb": 1048576,
            "storagePoolId": "68cb3e3400000000",
            "dataLayout": "ErasureCoding",
            "volumeClass": "defaultclass",
            "accessModeLimit": "ReadOnly",
            "pairIds": None,
            "useRmcache": False,
            "volumeType": "ReadOnlySnapshot",
            "consistencyGroupId": "a8b4901c00000001",
            "ancestorVolumeId": "test_vol_id",
            "notGenuineSnapshot": False,
            "secureSnapshotExpTime": 3,
            "snplIdOfAutoSnapshot": None,
            "lockedAutoSnapshot": False,
            "lockedAutoSnapshotMarkedForRemoval": False,
            "autoSnapshotGroupId": None,
            "timeStampIsAccurate": False,
            "nsid": 23,
            "id": "04d17a4400000016",
            "links": [
                {"rel": "self", "href": "/api/instances/Volume::04d17a4400000016"},
                {
                    "rel": "/dtapi/rest/v1/metrics/query",
                    "href": "/dtapi/rest/v1/metrics/query",
                    "body": {"resource_type": "volume", "ids": ["04d17a4400000016"]},
                },
                {
                    "rel": "/api/parent/relationship/ancestorVolumeId",
                    "href": "/api/instances/Volume::04d17a290000000f",
                },
                {
                    "rel": "/api/parent/relationship/vtreeId",
                    "href": "/api/instances/VTree::c2579d4c0000000c",
                },
                {
                    "rel": "/api/parent/relationship/storagePoolId",
                    "href": "/api/instances/StoragePool::68cb3e3400000000",
                },
            ],
        }
    ]

    RESPONSE_EXEC_DICT = {
        "get_snapshot_details_empty_snapshot_id_exception": "Please provide valid snapshot_id",
        "get_snapshot_details_exception": "Failed to get the snapshot",
        "create_snapshot_with_exception": "Create snapshot test_snapshot operation failed",
        "rename_snapshot_exception": "Rename snapshot 04d17a4400000016 operation failed",
        "modify_retention_snapshot_exception": "Modify retention of snapshot 04d17a4400000016 operation failed",
        "remove_snapshot_exception": "Delete snapshot 04d17a4400000016 operation failed",
        "get_storage_pool_with_exception": "Failed to get the storage pool",
        "snapshot_details_multi_instance_exception": "Multiple instances of snapshot exist",
        "create_snapshot_vol_id_conflict_exception": "Given volume ID do not match with",
        "create_snapshot_vol_name_conflict_exception": "Given volume name do not match with",
        "get_volume_with_exception": "Failed to get the volume",
        "get_system_with_exception": "Failed to get system id",
        "create_snapshot_with_sp_id_exception" : "Creation of snapshot is allowed using snapshot_name only",
        "create_snapshot_without_name_exception": "Please provide valid snapshot name",
        "create_snapshot_without_vol_exception": "Please provide volume details to create new snapshot",
        "create_snapshot_with_new_name_exception": "snapshot_new_name is not required while creating snapshot",
        "create_snapshot_with_rm_mode_exception": "remove_mode is not required while creating snapshot",
        "retention_hours_exception": "the desired retention between 1 and 744",
        "retention_days_exception": "the desired retention between 1 and 31",
        "create_snapshot_unit_exception": "retention_unit can only be specified along with desired_retention",
    }

    @staticmethod
    def get_snapshot_exception_response(response_type):
        return MockSnapshotApi.RESPONSE_EXEC_DICT.get(response_type, "")
