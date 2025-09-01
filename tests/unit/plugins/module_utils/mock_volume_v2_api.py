# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of volume module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockVolumeApi:
    VOLUME_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "vol_name": None,
        "vol_id": None,
        "vol_type": None,
        "storage_pool_name": None,
        "storage_pool_id": None,
        "protection_domain_name": None,
        "protection_domain_id": None,
        "snapshot_policy_name": None,
        "snapshot_policy_id": None,
        "auto_snap_remove_type": None,
        "refresh_src_vol_name": None,
        "refresh_src_vol_id": None,
        "restore_src_vol_name": None,
        "restore_src_vol_id": None,
        "size": None,
        "cap_unit": None,
        "vol_new_name": None,
        "sdc": {},
        "sdc_state": None,
        "delete_snapshots": None,
        "state": None,
    }

    VOLUME_GET_LIST = [
        {
            "genType": "EC",
            "managedBy": "ScaleIO",
            "retentionLevels": [],
            "replicationJournalVolume": False,
            "replicationTimeStamp": 0,
            'snplIdOfSourceVolume': "snplIdOfSourceVolume",
            "originalExpiryTime": 0,
            "volumeReplicationState": "UnmarkedForReplication",
            "mappedSdcInfo": [
                {
                    "limitIops": 0,
                    "limitBwInMbps": 0,
                    "isDirectBufferMapping": False,
                    "sdcIp": "10.225.106.67",
                    "sdcId": "fdc050ed00000002",
                    "sdcName": "SDC1",
                    "nqn": None,
                    "accessMode": "ReadWrite",
                    "hostType": "SdcHost",
                }
            ],
            "name": "test_vol",
            "creationTime": 1756099981,
            "storagePoolId": "3726599c00000000",
            "dataLayout": "ErasureCoding",
            "vtreeId": "0643ccac00000000",
            "sizeInKb": 83886080,
            "compressionMethod": "NotApplicable",
            "volumeClass": "defaultclass",
            "accessModeLimit": "ReadWrite",
            "lockedAutoSnapshotMarkedForRemoval": False,
            "snplIdOfAutoSnapshot": None,
            "pairIds": None,
            "useRmcache": False,
            "volumeType": "ThinProvisioned",
            "consistencyGroupId": None,
            "ancestorVolumeId": None,
            "notGenuineSnapshot": False,
            "secureSnapshotExpTime": 0,
            "lockedAutoSnapshot": False,
            "autoSnapshotGroupId": None,
            "timeStampIsAccurate": False,
            "nsid": 1,
            "id": "17c851e200000000",
        }
    ]

    VOLUME_STORAGEPOOL_DETAILS = {
        "genType": "EC",
        "name": "SP_EC",
        "protectionDomainId": "e597f3dd00000000",
        "id": "3726599c00000000",
    }

    VOLUME_PD_DETAILS = {
        "genType": "EC",
        "name": "PD_EC",
        "systemId": "6f3adbac60d7730f",
        "id": "95d9520100000000",
    }

    VOLUME_STATISTICS = {
        "format": "ID_TIMESTAMP_METRIC",
        "resource_type": "volume",
        "timestamps": ["2025-07-31T06:40:48Z"],
        "resources": [
            {
                "id": "04d17a4e0000000d",
                "metrics": [
                    {"name": "host_trim_bandwidth", "values": [0]},
                    {"name": "host_trim_iops", "values": [0]},
                    {"name": "avg_host_write_latency", "values": [0]},
                    {"name": "logical_provisioned", "values": [85899345920]},
                    {"name": "avg_host_read_latency", "values": [0]},
                    {"name": "host_read_bandwidth", "values": [0]},
                    {"name": "host_read_iops", "values": [0]},
                    {"name": "logical_used", "values": [0]},
                    {"name": "host_write_bandwidth", "values": [0]},
                    {"name": "host_write_iops", "values": [0]},
                    {"name": "avg_host_trim_latency", "values": [0]},
                ],
            }
        ],
    }

    SDC_RESPONSE = [
        {
            "id": "5e0c91620000000a",
        }
    ]

    SDC_RESPONSE_EMPTY = []

    GET_STORAGE_POOL = {"dataLayout": "MediumGranularity"}

    GET_STORAGE_POOL_FINE = {
        "dataLayout": "FineGranularity",
    }

    PROTECTION_DETAILS = [{"pd_id": "pd_id", "pd_name": "pd_name"}]

    GET_ID = {"id": "e0d8f6c900000000"}
    PROTECTION_DETAILS_MULTI = [
        {"pd_id": "pd_id", "pd_name": "pd_name"},
        {"pd_id": "pd_id", "pd_name": "pd_name"},
    ]

    RESPONSE_EXEC_DICT = {
        "get_details": "Failed to get the volume",
        "get_sds": "Failed to get the SDC sdc_name with error ",
        "create_vol_name": "Please provide valid volume name.",
        "create_vol_size": "Size is a mandatory parameter",
        "create_vol_ctype": "compression_type for volume can only be",
        "create_vol_exc": "Create volume vol_name operation failed with error",
        "modify_access": "Modify access mode of SDC operation failed",
        "modify_limits": "Modify bandwidth/iops limits of SDC",
        "delete_volume": "Delete volume vol_id operation failed with",
        'val_params_err1': "sdc_id, sdc_ip and sdc_name are mutually exclusive",
        'val_params_err2': "cap_unit can be specified along with size only",
        'val_params_err3': "To remove/detach snapshot policy, please provide",
        'val_params_err4': "delete_snapshots can be specified only when the state",
        "modify_volume_exp": "Failed to update the volume",
        "to_modify_err1": "To remove/detach a snapshot policy, provide the ",
        "snap_pol_id_err": "Entered snapshot policy id does not ",
        "snap_pol_name_err": "Entered snapshot policy name does not ",
        "pd_id_err": "Entered protection domain id does not ",
        "pool_id_err": "Entered storage pool id does ",
        "pd_name_err": "Entered protection domain name does ",
        "pool_name_err": "Entered storage pool name does ",
        "get_pd_exception": "Failed to get the protection domain ",
        "get_sp_exception": "Failed to get the snapshot policy ",
        "get_spool_error1": "More than one storage pool found with",
        "get_spool_error2": "Failed to get the storage pool",
        "map_vol_exception": "Mapping volume name to SDC sdc_id1 failed with error",
        "unmap": "Unmap SDC sdc_id from volume vol_id failed with error",
        "perform_error1": "vol_new_name parameter is not supported during creation of a volume",
        "refresh_exception": "Failed to refresh volume",
        "restore_exception": "Failed to restore volume",
        "refresh_invalid_vol_name_exception": "Invalid refresh src vol name",
        "restore_invalid_vol_name_exception": "Invalid restore src vol name",
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockVolumeApi.RESPONSE_EXEC_DICT.get(response_type, "")
