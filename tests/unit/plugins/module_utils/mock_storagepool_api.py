# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock Api response for Unit tests of storage pool module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockStoragePoolApi:
    STORAGE_POOL_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "storage_pool_name": None,
        "storage_pool_id": None,
        "storage_pool_new_name": None,
        "protection_domain_name": None,
        "protection_domain_id": None,
        "use_rmcache": None,
        "use_rfcache": None,
        "media_type": None,
        'state': None
    }

    STORAGE_POOL_GET_LIST = [
        {
            'protectionDomainId': '4eeb304600000000',
            'rebuildEnabled': True,
            'dataLayout': 'MediumGranularity',
            'persistentChecksumState': 'Protected',
            'addressSpaceUsage': 'Normal',
            'externalAccelerationType': 'None',
            'rebalanceEnabled': True,
            'sparePercentage': 10,
            'rmcacheWriteHandlingMode': 'Cached',
            'checksumEnabled': False,
            'useRfcache': False,
            'compressionMethod': 'Invalid',
            'fragmentationEnabled': True,
            'numOfParallelRebuildRebalanceJobsPerDevice': 2,
            'capacityAlertHighThreshold': 80,
            'capacityAlertCriticalThreshold': 90,
            'capacityUsageState': 'Normal',
            'capacityUsageType': 'NetCapacity',
            'addressSpaceUsageType': 'DeviceCapacityLimit',
            'bgScannerCompareErrorAction': 'ReportAndFix',
            'bgScannerReadErrorAction': 'ReportAndFix',
            'fglExtraCapacity': None,
            'fglOverProvisioningFactor': None,
            'fglWriteAtomicitySize': None,
            'fglMaxCompressionRatio': None,
            'fglPerfProfile': None,
            'replicationCapacityMaxRatio': 0,
            'persistentChecksumEnabled': True,
            'persistentChecksumBuilderLimitKb': 3072,
            'persistentChecksumValidateOnRead': False,
            'useRmcache': False,
            'fglAccpId': None,
            'rebuildIoPriorityPolicy': 'limitNumOfConcurrentIos',
            'rebalanceIoPriorityPolicy': 'favorAppIos',
            'vtreeMigrationIoPriorityPolicy': 'favorAppIos',
            'protectedMaintenanceModeIoPriorityPolicy': 'limitNumOfConcurrentIos',
            'rebuildIoPriorityNumOfConcurrentIosPerDevice': 1,
            'rebalanceIoPriorityNumOfConcurrentIosPerDevice': 1,
            'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': 1,
            'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': 1,
            'rebuildIoPriorityBwLimitPerDeviceInKbps': 10240,
            'rebalanceIoPriorityBwLimitPerDeviceInKbps': 10240,
            'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': 10240,
            'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': 10240,
            'rebuildIoPriorityAppIopsPerDeviceThreshold': None,
            'rebalanceIoPriorityAppIopsPerDeviceThreshold': None,
            'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None,
            'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None,
            'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'rebuildIoPriorityQuietPeriodInMsec': None,
            'rebalanceIoPriorityQuietPeriodInMsec': None,
            'vtreeMigrationIoPriorityQuietPeriodInMsec': None,
            'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None,
            'zeroPaddingEnabled': True,
            'backgroundScannerMode': 'DataComparison',
            'backgroundScannerBWLimitKBps': 3072,
            'fglMetadataSizeXx100': None,
            'fglNvdimmWriteCacheSizeInMb': None,
            'fglNvdimmMetadataAmortizationX100': None,
            'mediaType': 'HDD',
            'name': 'test_pool',
            'id': 'test_pool_id_1'
        }
    ]

    STORAGE_POOL_STATISTICS = {
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
            'test_vol_id_1'
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
            'dv_id_1',
            'dv_id_2',
            'dv_id_3'
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
            'vtree_id_1'
        ],
        'activeMovingCapacityInKb': 1,
        'targetWriteLatency': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'pendingExitProtectedMaintenanceModeCapacityInKb': 1,
        'rfcacheIosSkipped': 1,
        'userDataWriteBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'inMaintenanceVacInKb': 1,
        'exitProtectedMaintenanceModeReadBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'netFglSparesInKb': 1,
        'rfcacheReadsSkipped': 1,
        'activeExitProtectedMaintenanceModeCapacityInKb': 1,
        'activeMovingOutExitProtectedMaintenanceModeJobs': 1,
        'numOfUnmappedVolumes': 2,
        'tempCapacityVacInKb': 1,
        'volumeAddressSpaceInKb': 80000,
        'currentFglMigrationSizeInKb': 1,
        'rfcacheWritesSkippedMaxIoSize': 1,
        'netMaxUserDataCapacityInKb': 380600000,
        'numOfMigratingVtrees': 1,
        'atRestCapacityInKb': 1,
        'rfacheWriteHit': 1,
        'bckRebuildReadBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'rfcacheSourceDeviceWrites': 1,
        'spareCapacityInKb': 84578000,
        'enterProtectedMaintenanceModeWriteBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'rfcacheIoErrors': 1,
        'inaccessibleCapacityInKb': 1,
        'normRebuildWriteBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'capacityInUseInKb': 1,
        'rebalanceReadBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'rfcacheReadsSkippedMaxIoSize': 1,
        'activeMovingInExitProtectedMaintenanceModeJobs': 1,
        'secondaryReadFromDevBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'secondaryReadBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'rfcacheWritesSkippedStuckIo': 1,
        'secondaryReadFromRmcacheBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'inMaintenanceCapacityInKb': 1,
        'exposedCapacityInKb': 1,
        'netFglCompressedDataSizeInKb': 1,
        'userDataSdcWriteLatency': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'inUseVacInKb': 16777000,
        'fwdRebuildCapacityInKb': 1,
        'thickCapacityInUseInKb': 1,
        'backgroundScanReadErrorCount': 1,
        'activeMovingInRebalanceJobs': 1,
        'migratingVolumeIds': [
            '1xxx'
        ],
        'rfcacheWritesSkippedLowResources': 1,
        'capacityInUseNoOverheadInKb': 1,
        'exitProtectedMaintenanceModeWriteBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'rfcacheSkippedUnlinedWrite': 1,
        'netCapacityInUseInKb': 1,
        'numOfOutgoingMigrations': 1,
        'rfcacheAvgWriteTime': 1,
        'pendingNormRebuildCapacityInKb': 1,
        'pendingMovingOutNormrebuildJobs': 1,
        'rfcacheSourceDeviceReads': 1,
        'rfcacheReadsPending': 1,
        'volumeAllocationLimitInKb': 3791650000,
        'rfcacheReadsSkippedHeavyLoad': 1,
        'fwdRebuildWriteBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'rfcacheReadMiss': 1,
        'targetReadLatency': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'userDataCapacityInKb': 1,
        'activeMovingInBckRebuildJobs': 1,
        'movingCapacityInKb': 1,
        'activeEnterProtectedMaintenanceModeCapacityInKb': 1,
        'backgroundScanCompareErrorCount': 1,
        'pendingMovingInFwdRebuildJobs': 1,
        'rfcacheReadsReceived': 1,
        'spSdsIds': [
            'sp_id_1',
            'sp_id_2',
            'sp_id_3'
        ],
        'pendingEnterProtectedMaintenanceModeCapacityInKb': 1,
        'vtreeAddresSpaceInKb': 8388000,
        'snapCapacityInUseOccupiedInKb': 1,
        'activeFwdRebuildCapacityInKb': 1,
        'rfcacheReadsSkippedStuckIo': 1,
        'activeMovingOutNormRebuildJobs': 1,
        'rfcacheWritePending': 1,
        'numOfThinBaseVolumes': 2,
        'degradedFailedVacInKb': 1,
        'userDataTrimBwc': {
            'numSeconds': 1,
            'totalWeightInKb': 1,
            'numOccured': 1
        },
        'numOfIncomingVtreeMigrations': 1
    }

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'get_details':
            return "Failed to get the storage pool test_pool with error "
