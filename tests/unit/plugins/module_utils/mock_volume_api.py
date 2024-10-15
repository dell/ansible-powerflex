# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of volume module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storagepool_api import MockStoragePoolApi

__metaclass__ = type


class MockVolumeApi:
    VOLUME_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "vol_name": None,
        "vol_id": None,
        "vol_type": None,
        "compression_type": None,
        "storage_pool_name": None,
        "storage_pool_id": None,
        "protection_domain_name": None,
        "protection_domain_id": None,
        "snapshot_policy_name": None,
        "snapshot_policy_id": None,
        "auto_snap_remove_type": None,
        "use_rmcache": None,
        "size": None,
        "cap_unit": None,
        "vol_new_name": None,
        "sdc": {},
        "sdc_state": None,
        "delete_snapshots": None,
        "state": None
    }

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
            'snplIdOfSourceVolume': "snplIdOfSourceVolume",
            'snapshotPolicyId': 'snapshotPolicyId',
            'snapshotPolicyName': 'snapshotPolicyName',
            'volumeReplicationState': 'UnmarkedForReplication',
            'replicationJournalVolume': False,
            'replicationTimeStamp': 0,
            'creationTime': 1655878090,
            'name': 'testing',
            'id': 'test_id_1'
        }
    ]

    VOLUME_STORAGEPOOL_DETAILS = MockStoragePoolApi.STORAGE_POOL_GET_LIST[0]

    VOLUME_PD_DETAILS = {
        'rebalanceNetworkThrottlingEnabled': False,
        'vtreeMigrationNetworkThrottlingEnabled': False,
        'overallIoNetworkThrottlingEnabled': False,
        'rfcacheEnabled': True,
        'rfcacheAccpId': None,
        'rebuildNetworkThrottlingEnabled': False,
        'sdrSdsConnectivityInfo': {
            'clientServerConnStatus': 'CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED',
            'disconnectedClientId': None,
            'disconnectedClientName': None,
            'disconnectedServerId': None,
            'disconnectedServerName': None,
            'disconnectedServerIp': None
        },
        'protectionDomainState': 'Active',
        'rebuildNetworkThrottlingInKbps': None,
        'rebalanceNetworkThrottlingInKbps': None,
        'overallIoNetworkThrottlingInKbps': None,
        'vtreeMigrationNetworkThrottlingInKbps': None,
        'sdsDecoupledCounterParameters': {
            'shortWindow': {
                'threshold': 300,
                'windowSizeInSec': 60
            },
            'mediumWindow': {
                'threshold': 500,
                'windowSizeInSec': 3600
            },
            'longWindow': {
                'threshold': 700,
                'windowSizeInSec': 86400
            }
        },
        'sdsConfigurationFailureCounterParameters': {
            'shortWindow': {
                'threshold': 300,
                'windowSizeInSec': 60
            },
            'mediumWindow': {
                'threshold': 500,
                'windowSizeInSec': 3600
            },
            'longWindow': {
                'threshold': 700,
                'windowSizeInSec': 86400
            }
        },
        'mdmSdsNetworkDisconnectionsCounterParameters': {
            'shortWindow': {
                'threshold': 300,
                'windowSizeInSec': 60
            },
            'mediumWindow': {
                'threshold': 500,
                'windowSizeInSec': 3600
            },
            'longWindow': {
                'threshold': 700,
                'windowSizeInSec': 86400
            }
        },
        'sdsSdsNetworkDisconnectionsCounterParameters': {
            'shortWindow': {
                'threshold': 300,
                'windowSizeInSec': 60
            },
            'mediumWindow': {
                'threshold': 500,
                'windowSizeInSec': 3600
            },
            'longWindow': {
                'threshold': 700,
                'windowSizeInSec': 86400
            }
        },
        'rfcacheOpertionalMode': 'WriteMiss',
        'rfcachePageSizeKb': 64,
        'rfcacheMaxIoSizeKb': 128,
        'sdsReceiveBufferAllocationFailuresCounterParameters': {
            'shortWindow': {
                'threshold': 20000,
                'windowSizeInSec': 60
            },
            'mediumWindow': {
                'threshold': 200000,
                'windowSizeInSec': 3600
            },
            'longWindow': {
                'threshold': 2000000,
                'windowSizeInSec': 86400
            }
        },
        'fglDefaultNumConcurrentWrites': 1000,
        'fglMetadataCacheEnabled': False,
        'fglDefaultMetadataCacheSize': 0,
        'protectedMaintenanceModeNetworkThrottlingEnabled': False,
        'protectedMaintenanceModeNetworkThrottlingInKbps': None,
        'rplCapAlertLevel': 'normal',
        'systemId': 'syst_id_1',
        'name': 'domain1',
        'id': '4eeb304600000000',
    }

    VOLUME_STATISTICS = {
        'backgroundScanFixedReadErrorCount': 0,
        'pendingMovingOutBckRebuildJobs': 0,
        'degradedHealthyCapacityInKb': 0,
        'activeMovingOutFwdRebuildJobs': 0,
        'bckRebuildWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'netFglUncompressedDataSizeInKb': 0,
        'primaryReadFromDevBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'BackgroundScannedInMB': 3209584,
        'volumeIds': [
            '456ad22e00000003'
        ],
        'maxUserDataCapacityInKb': 761204736,
        'persistentChecksumBuilderProgress': 100.0,
        'rfcacheReadsSkippedAlignedSizeTooLarge': 0,
        'pendingMovingInRebalanceJobs': 0,
        'rfcacheWritesSkippedHeavyLoad': 0,
        'unusedCapacityInKb': 761204736,
        'userDataSdcReadLatency': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'totalReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'numOfDeviceAtFaultRebuilds': 0,
        'totalWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'persistentChecksumCapacityInKb': 414720,
        'rmPendingAllocatedInKb': 0,
        'numOfVolumes': 1,
        'rfcacheIosOutstanding': 0,
        'capacityAvailableForVolumeAllocationInKb': 377487360,
        'numOfMappedToAllVolumes': 0,
        'netThinUserDataCapacityInKb': 0,
        'backgroundScanFixedCompareErrorCount': 0,
        'volMigrationWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'thinAndSnapshotRatio': 'Infinity',
        'fglUserDataCapacityInKb': 0,
        'pendingMovingInEnterProtectedMaintenanceModeJobs': 0,
        'activeMovingInNormRebuildJobs': 0,
        'aggregateCompressionLevel': 'Uncompressed',
        'targetOtherLatency': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'netUserDataCapacityInKb': 0,
        'pendingMovingOutExitProtectedMaintenanceModeJobs': 0,
        'overallUsageRatio': 'Infinity',
        'volMigrationReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'netCapacityInUseNoOverheadInKb': 0,
        'pendingMovingInBckRebuildJobs': 0,
        'rfcacheReadsSkippedInternalError': 0,
        'activeBckRebuildCapacityInKb': 0,
        'rebalanceCapacityInKb': 0,
        'pendingMovingInExitProtectedMaintenanceModeJobs': 0,
        'rfcacheReadsSkippedLowResources': 0,
        'rplJournalCapAllowed': 0,
        'thinCapacityInUseInKb': 0,
        'userDataSdcTrimLatency': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'activeMovingInEnterProtectedMaintenanceModeJobs': 0,
        'rfcacheWritesSkippedInternalError': 0,
        'netUserDataCapacityNoTrimInKb': 0,
        'rfcacheWritesSkippedCacheMiss': 0,
        'degradedFailedCapacityInKb': 0,
        'activeNormRebuildCapacityInKb': 0,
        'fglSparesInKb': 0,
        'snapCapacityInUseInKb': 0,
        'numOfMigratingVolumes': 0,
        'compressionRatio': 0.0,
        'rfcacheWriteMiss': 0,
        'primaryReadFromRmcacheBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'migratingVtreeIds': [
        ],
        'numOfVtrees': 1,
        'userDataCapacityNoTrimInKb': 0,
        'rfacheReadHit': 0,
        'compressedDataCompressionRatio': 0.0,
        'rplUsedJournalCap': 0,
        'pendingMovingCapacityInKb': 0,
        'numOfSnapshots': 0,
        'pendingFwdRebuildCapacityInKb': 0,
        'tempCapacityInKb': 0,
        'totalFglMigrationSizeInKb': 0,
        'normRebuildCapacityInKb': 0,
        'logWrittenBlocksInKb': 0,
        'primaryWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'numOfThickBaseVolumes': 0,
        'enterProtectedMaintenanceModeReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'activeRebalanceCapacityInKb': 0,
        'numOfReplicationJournalVolumes': 0,
        'rfcacheReadsSkippedLockIos': 0,
        'unreachableUnusedCapacityInKb': 0,
        'netProvisionedAddressesInKb': 0,
        'trimmedUserDataCapacityInKb': 0,
        'provisionedAddressesInKb': 0,
        'numOfVolumesInDeletion': 0,
        'pendingMovingOutFwdRebuildJobs': 0,
        'maxCapacityInKb': 845783040,
        'rmPendingThickInKb': 0,
        'protectedCapacityInKb': 0,
        'secondaryWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'normRebuildReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'thinCapacityAllocatedInKb': 16777216,
        'netFglUserDataCapacityInKb': 0,
        'metadataOverheadInKb': 0,
        'thinCapacityAllocatedInKm': 16777216,
        'rebalanceWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'primaryVacInKb': 8388608,
        'deviceIds': [
            'bbd7580800030001',
            'bbd4580a00040001',
            'bbd5580b00050001'
        ],
        'netSnapshotCapacityInKb': 0,
        'secondaryVacInKb': 8388608,
        'numOfDevices': 3,
        'rplTotalJournalCap': 0,
        'failedCapacityInKb': 0,
        'netMetadataOverheadInKb': 0,
        'activeMovingOutBckRebuildJobs': 0,
        'rfcacheReadsFromCache': 0,
        'activeMovingOutEnterProtectedMaintenanceModeJobs': 0,
        'enterProtectedMaintenanceModeCapacityInKb': 0,
        'pendingMovingInNormRebuildJobs': 0,
        'failedVacInKb': 0,
        'primaryReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'fglUncompressedDataSizeInKb': 0,
        'fglCompressedDataSizeInKb': 0,
        'pendingRebalanceCapacityInKb': 0,
        'rfcacheAvgReadTime': 0,
        'semiProtectedCapacityInKb': 0,
        'pendingMovingOutEnterProtectedMaintenanceModeJobs': 0,
        'mgUserDdataCcapacityInKb': 0,
        'snapshotCapacityInKb': 0,
        'netMgUserDataCapacityInKb': 0,
        'fwdRebuildReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheWritesReceived': 0,
        'netUnusedCapacityInKb': 380602368,
        'thinUserDataCapacityInKb': 0,
        'protectedVacInKb': 16777216,
        'activeMovingRebalanceJobs': 0,
        'bckRebuildCapacityInKb': 0,
        'activeMovingInFwdRebuildJobs': 0,
        'netTrimmedUserDataCapacityInKb': 0,
        'pendingMovingRebalanceJobs': 0,
        'numOfMarkedVolumesForReplication': 0,
        'degradedHealthyVacInKb': 0,
        'semiProtectedVacInKb': 0,
        'userDataReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'pendingBckRebuildCapacityInKb': 0,
        'capacityLimitInKb': 845783040,
        'vtreeIds': [
            '32b13de900000003'
        ],
        'activeMovingCapacityInKb': 0,
        'targetWriteLatency': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'pendingExitProtectedMaintenanceModeCapacityInKb': 0,
        'rfcacheIosSkipped': 0,
        'userDataWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'inMaintenanceVacInKb': 0,
        'exitProtectedMaintenanceModeReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'netFglSparesInKb': 0,
        'rfcacheReadsSkipped': 0,
        'activeExitProtectedMaintenanceModeCapacityInKb': 0,
        'activeMovingOutExitProtectedMaintenanceModeJobs': 0,
        'numOfUnmappedVolumes': 1,
        'tempCapacityVacInKb': 0,
        'volumeAddressSpaceInKb': 8388608,
        'currentFglMigrationSizeInKb': 0,
        'rfcacheWritesSkippedMaxIoSize': 0,
        'netMaxUserDataCapacityInKb': 380602368,
        'numOfMigratingVtrees': 0,
        'atRestCapacityInKb': 0,
        'rfacheWriteHit': 0,
        'bckRebuildReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheSourceDeviceWrites': 0,
        'spareCapacityInKb': 84578304,
        'enterProtectedMaintenanceModeWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheIoErrors': 0,
        'inaccessibleCapacityInKb': 0,
        'normRebuildWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'capacityInUseInKb': 0,
        'rebalanceReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheReadsSkippedMaxIoSize': 0,
        'activeMovingInExitProtectedMaintenanceModeJobs': 0,
        'secondaryReadFromDevBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'secondaryReadBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheWritesSkippedStuckIo': 0,
        'secondaryReadFromRmcacheBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'inMaintenanceCapacityInKb': 0,
        'exposedCapacityInKb': 0,
        'netFglCompressedDataSizeInKb': 0,
        'userDataSdcWriteLatency': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'inUseVacInKb': 16777216,
        'fwdRebuildCapacityInKb': 0,
        'thickCapacityInUseInKb': 0,
        'backgroundScanReadErrorCount': 0,
        'activeMovingInRebalanceJobs': 0,
        'migratingVolumeIds': [
        ],
        'rfcacheWritesSkippedLowResources': 0,
        'capacityInUseNoOverheadInKb': 0,
        'exitProtectedMaintenanceModeWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheSkippedUnlinedWrite': 0,
        'netCapacityInUseInKb': 0,
        'numOfOutgoingMigrations': 0,
        'rfcacheAvgWriteTime': 0,
        'pendingNormRebuildCapacityInKb': 0,
        'pendingMovingOutNormrebuildJobs': 0,
        'rfcacheSourceDeviceReads': 0,
        'rfcacheReadsPending': 0,
        'volumeAllocationLimitInKb': 3791650816,
        'rfcacheReadsSkippedHeavyLoad': 0,
        'fwdRebuildWriteBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'rfcacheReadMiss': 0,
        'targetReadLatency': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'userDataCapacityInKb': 0,
        'activeMovingInBckRebuildJobs': 0,
        'movingCapacityInKb': 0,
        'activeEnterProtectedMaintenanceModeCapacityInKb': 0,
        'backgroundScanCompareErrorCount': 0,
        'pendingMovingInFwdRebuildJobs': 0,
        'rfcacheReadsReceived': 0,
        'spSdsIds': [
            'abdfe71b00030001',
            'abdce71d00040001',
            'abdde71e00050001'
        ],
        'pendingEnterProtectedMaintenanceModeCapacityInKb': 0,
        'vtreeAddresSpaceInKb': 8388608,
        'snapCapacityInUseOccupiedInKb': 0,
        'activeFwdRebuildCapacityInKb': 0,
        'rfcacheReadsSkippedStuckIo': 0,
        'activeMovingOutNormRebuildJobs': 0,
        'rfcacheWritePending': 0,
        'numOfThinBaseVolumes': 1,
        'degradedFailedVacInKb': 0,
        'userDataTrimBwc': {
            'numSeconds': 0,
            'totalWeightInKb': 0,
            'numOccured': 0
        },
        'numOfIncomingVtreeMigrations': 0
    }

    SDC_RESPONSE = [
        {
            'id': 'abdfe71b00030001',
        }
    ]

    SDC_RESPONSE_EMPTY = []

    GET_STORAGE_POOL = {
        'dataLayout': 'MediumGranularity'
    }

    GET_STORAGE_POOL_FINE = {
        'dataLayout': 'FineGranularity',
    }

    PROTECTION_DETAILS = [{"pd_id": "pd_id", "pd_name": "pd_name"}]

    GET_ID = {"id": "e0d8f6c900000000"}
    PROTECTION_DETAILS_MULTI = [
        {"pd_id": "pd_id", "pd_name": "pd_name"},
        {"pd_id": "pd_id", "pd_name": "pd_name"},
    ]

    RESPONSE_EXEC_DICT = {
        'get_details': "Failed to get the volume test_id_1 with error ",
        'get_sds': "Failed to get the SDC sdc_name with error ",
        'create_vol_name': "Please provide valid volume name.",
        'create_vol_size': "Size is a mandatory parameter",
        'create_vol_ctype': "compression_type for volume can only be",
        'create_vol_exc': "Create volume vol_name operation failed with error",
        'modify_access': "Modify access mode of SDC operation failed",
        'modify_limits': "Modify bandwidth/iops limits of SDC",
        'delete_volume': "Delete volume vol_id operation failed with",
        'val_params_err1': "sdc_id, sdc_ip and sdc_name are mutually exclusive",
        'val_params_err2': "cap_unit can be specified along with size only",
        'val_params_err3': "To remove/detach snapshot policy, please provide",
        'val_params_err4': "delete_snapshots can be specified only when the state",
        'modify_volume_exp': "Failed to update the volume",
        'to_modify_err1': "To remove/detach a snapshot policy, provide the ",
        'snap_pol_id_err': "Entered snapshot policy id does not ",
        'snap_pol_name_err': "Entered snapshot policy name does not ",
        'pd_id_err': "Entered protection domain id does not ",
        'pool_id_err': "Entered storage pool id does ",
        'pd_name_err': "Entered protection domain name does ",
        'pool_name_err': "Entered storage pool name does ",
        'get_pd_exception': "Failed to get the protection domain ",
        'get_sp_exception': "Failed to get the snapshot policy ",
        'get_spool_error1': "More than one storage pool found with",
        'get_spool_error2': "Failed to get the storage pool",
        'map_vol_exception': "Mapping volume name to SDC sdc_id1 failed with error",
        'unmap': "Unmap SDC sdc_id from volume vol_id failed with error",
        'perform_error1': "vol_new_name parameter is not supported during creation of a volume"
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockVolumeApi.RESPONSE_EXEC_DICT.get(response_type, "")
