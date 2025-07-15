#!/usr/bin/python

# Copyright: (c) 2021-24, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing Dell Technologies (Dell) PowerFlex storage pool"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: storage_pool

version_added: '1.0.0'

short_description: Managing Dell PowerFlex storage pool

description:
- Dell PowerFlex storage pool module includes getting the details of
  storage pool, creating a new storage pool, and modifying the attribute of
  a storage pool.

extends_documentation_fragment:
  - dellemc.powerflex.powerflex

author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

options:
  storage_pool_name:
    description:
    - The name of the storage pool.
    - If more than one storage pool is found with the same name then
      protection domain id/name is required to perform the task.
    - Mutually exclusive with I(storage_pool_id).
    type: str
  storage_pool_id:
    description:
    - The id of the storage pool.
    - It is auto generated, hence should not be provided during
      creation of a storage pool.
    - Mutually exclusive with I(storage_pool_name).
    type: str
  protection_domain_name:
    description:
    - The name of the protection domain.
    - During creation of a pool, either protection domain name or id must be
      mentioned.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - The id of the protection domain.
    - During creation of a pool, either protection domain name or id must
      be mentioned.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  media_type:
    description:
    - Type of devices in the storage pool.
    type: str
    choices: ['HDD', 'SSD', 'TRANSITIONAL']
  storage_pool_new_name:
    description:
    - New name for the storage pool can be provided.
    - This parameter is used for renaming the storage pool.
    type: str
  use_rfcache:
    description:
    - Enable/Disable RFcache on a specific storage pool.
    type: bool
  use_rmcache:
    description:
    - Enable/Disable RMcache on a specific storage pool.
    type: bool
  enable_zero_padding:
    description:
    - Enable/Disable zero padding on a specific storage pool.
    type: bool
  rep_cap_max_ratio:
    description:
    - Set replication journal capacity of a storage pool.
    type: int
  enable_rebalance:
    description:
    - Enable/Disable rebalance on a specific storage pool.
    type: bool
  spare_percentage:
    description:
    - Set the spare percentage of a specific storage pool.
    type: int
  rmcache_write_handling_mode :
    description:
    - Set RM cache write handling mode of a storage pool.
    - I(Passthrough) Writes skip the cache and are stored in storage only.
    - I(Cached) Writes are stored in both cache and storage (the default).
    - Caching is only performed for IOs whose size is a multiple of 4k bytes.
    type: str
    choices: ['Cached', 'Passthrough']
    default: 'Cached'
  enable_rebuild:
    description:
    - Enable/Disable rebuild of a specific storage pool.
    type: bool
  enable_fragmentation:
    description:
    - Enable/Disable fragmentation of a specific storage pool.
    type: bool
  parallel_rebuild_rebalance_limit:
    description:
    - Set rebuild/rebalance parallelism limit of a storage pool.
    type: int
  persistent_checksum:
    description:
    - Enable/Disable persistent checksum of a specific storage pool.
    type: dict
    suboptions:
      enable:
        description:
        - Enable / disable persistent checksum.
        type: bool
      validate_on_read:
        description:
        - Validate checksum upon reading data.
        type: bool
      builder_limit:
        description:
        - Bandwidth limit in KB/s for the checksum building process.
        - Valid range is 1024 to 10240.
        default: 3072
        type: int
  protected_maintenance_mode_io_priority_policy:
    description:
    - Set protected maintenance mode I/O priority policy of a storage pool.
    type: dict
    suboptions:
      policy:
        description:
        - The I/O priority policy for protected maintenance mode.
        - C(unlimited) Protected maintenance mode IOPS are not limited
        - C(limitNumOfConcurrentIos)Limit the number of allowed concurrent protected maintenance mode
          migration I/Os to the value defined for I(concurrent_ios_per_device).
        - C(favorAppIos) Always limit the number of allowed concurrent protected maintenance mode
          migration I/Os to value defined for I(concurrent_ios_per_device).
        - If application I/Os are in progress, should also limit the bandwidth of
          protected maintenance mode migration I/Os to the limit defined for the I(bw_limit_per_device).
        type: str
        choices: ['unlimited', 'limitNumOfConcurrentIos', 'favorAppIos']
        default: 'limitNumOfConcurrentIos'
      concurrent_ios_per_device:
        description:
        - The maximum number of concurrent protected maintenance mode migration I/Os per device.
        - Valid range is 1 to 20.
        type: int
      bw_limit_per_device:
        description:
        - The maximum bandwidth of protected maintenance mode migration I/Os,
          in KB per second, per device.
        - Valid range is 1024 to 1048576.
        type: int
  vtree_migration_io_priority_policy:
    description:
    - Set the I/O priority policy for V-Tree migration for a specific Storage Pool.
    type: dict
    suboptions:
      policy:
        description:
        - The I/O priority policy for protected maintenance mode.
        - C(limitNumOfConcurrentIos) Limit the number of allowed concurrent V-Tree
          migration I/Os (default) to the I(concurrent_ios_per_device).
        - C(favorAppIos) Always limit the number of allowed concurrent
          V-Tree migration I/Os to defined for I(concurrent_ios_per_device).
        - If application I/Os are in progress, should also limit the bandwidth of
          V-Tree migration I/Os to the limit defined for the I(bw_limit_per_device).
        type: str
        choices: ['limitNumOfConcurrentIos', 'favorAppIos']
      concurrent_ios_per_device:
        description:
        - The maximum number of concurrent V-Tree migration I/Os per device.
        - Valid range is 1 to 20
        type: int
      bw_limit_per_device:
        description:
        - The maximum bandwidth of V-Tree migration I/Os,
          in KB per second, per device.
        - Valid range is 1024 to 25600.
        type: int
  rebalance_io_priority_policy:
    description:
    - Set the rebalance I/O priority policy for a Storage Pool.
    type: dict
    suboptions:
      policy:
        description:
        - Policy to use for rebalance I/O priority.
        - C(unlimited) Rebalance I/Os are not limited.
        - C(limitNumOfConcurrentIos) Limit the number of allowed concurrent rebalance I/Os.
        - C(favorAppIos) Limit the number and bandwidth of rebalance I/Os when application I/Os are in progress.
        type: str
        choices: ['unlimited', 'limitNumOfConcurrentIos', 'favorAppIos']
        default: 'favorAppIos'
      concurrent_ios_per_device:
        description:
        - The maximum number of concurrent rebalance I/Os per device.
        - Valid range is 1 to 20.
        type: int
      bw_limit_per_device:
        description:
        - The maximum bandwidth of rebalance I/Os, in KB/s, per device.
        - Valid range is 1024 to 1048576.
        type: int
  cap_alert_thresholds:
    description:
    - Set the threshold for triggering capacity usage alerts.
    - Alerts thresholds are calculated from each Storage Pool
      capacity after deducting the defined amount of spare capacity.
    type: dict
    suboptions:
      high_threshold:
        description:
        - Threshold of the non-spare capacity of the Storage Pool that will trigger a
          high-priority alert, expressed as a percentage.
        - This value must be lower than the I(critical_threshold).
        type: int
      critical_threshold:
        description:
        - Threshold of the non-spare capacity of the Storage Pool that will trigger a
          critical-priority alert, expressed as a percentage.
        type: int
  state:
    description:
    - State of the storage pool.
    type: str
    choices: ["present", "absent"]
    required: true
notes:
  - TRANSITIONAL media type is supported only during modification.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get the details of storage pool by name
  dellemc.powerflex.storagepool:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_pool_name: "sample_pool_name"
    protection_domain_name: "sample_protection_domain"
    state: "present"

- name: Get the details of storage pool by id
  dellemc.powerflex.storagepool:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_pool_id: "abcd1234ab12r"
    state: "present"

- name: Create a new Storage pool
  dellemc.powerflex.storagepool:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    storage_pool_name: "{{ pool_name }}"
    protection_domain_name: "{{ protection_domain_name }}"
    cap_alert_thresholds:
      high_threshold: 30
      critical_threshold: 50
    media_type: "TRANSITIONAL"
    enable_zero_padding: true
    rep_cap_max_ratio: 40
    rmcache_write_handling_mode: "Passthrough"
    spare_percentage: 80
    enable_rebalance: false
    enable_fragmentation: false
    enable_rebuild: false
    use_rmcache: true
    use_rfcache: true
    parallel_rebuild_rebalance_limit: 3
    protected_maintenance_mode_io_priority_policy:
      policy: "unlimited"
    rebalance_io_priority_policy:
      policy: "unlimited"
    vtree_migration_io_priority_policy:
      policy: "limitNumOfConcurrentIos"
      concurrent_ios_per_device: 10
    persistent_checksum:
      enable: false
    state: "present"

- name: Modify a Storage pool by name
  dellemc.powerflex.storagepool:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    storage_pool_name: "{{ pool_name }}"
    protection_domain_name: "{{ protection_domain_name }}"
    storage_pool_new_name: "pool_name_new"
    cap_alert_thresholds:
      high_threshold: 50
      critical_threshold: 70
    enable_zero_padding: false
    rep_cap_max_ratio: 60
    rmcache_write_handling_mode: "Passthrough"
    spare_percentage: 90
    enable_rebalance: true
    enable_fragmentation: true
    enable_rebuild: true
    use_rmcache: true
    use_rfcache: true
    parallel_rebuild_rebalance_limit: 6
    protected_maintenance_mode_io_priority_policy:
      policy: "limitNumOfConcurrentIos"
      concurrent_ios_per_device: 4
    rebalance_io_priority_policy:
      policy: "favorAppIos"
      concurrent_ios_per_device: 10
      bw_limit_per_device: 4096
    vtree_migration_io_priority_policy:
      policy: "limitNumOfConcurrentIos"
      concurrent_ios_per_device: 10
    persistent_checksum:
      enable: true
      validate_on_read: true
      builder_limit: 1024
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
storage_pool_details:
    description: Details of the storage pool.
    returned: When storage pool exists
    type: dict
    contains:
        mediaType:
            description: Type of devices in the storage pool.
            type: str
        useRfcache:
            description: Enable/Disable RFcache on a specific storage pool.
            type: bool
        useRmcache:
            description: Enable/Disable RMcache on a specific storage pool.
            type: bool
        id:
            description: ID of the storage pool under protection domain.
            type: str
        name:
            description: Name of the storage pool under protection domain.
            type: str
        protectionDomainId:
            description: ID of the protection domain in which pool resides.
            type: str
        protectionDomainName:
            description: Name of the protection domain in which pool resides.
            type: str
        "statistics":
            description: Statistics details of the storage pool.
            type: dict
            contains:
                "capacityInUseInKb":
                    description: Total capacity of the storage pool.
                    type: str
                "unusedCapacityInKb":
                    description: Unused capacity of the storage pool.
                    type: str
                "deviceIds":
                    description: Device Ids of the storage pool.
                    type: list
    sample: {
        "addressSpaceUsage": "Normal",
        "addressSpaceUsageType": "DeviceCapacityLimit",
        "backgroundScannerBWLimitKBps": 3072,
        "backgroundScannerMode": "DataComparison",
        "bgScannerCompareErrorAction": "ReportAndFix",
        "bgScannerReadErrorAction": "ReportAndFix",
        "capacityAlertCriticalThreshold": 90,
        "capacityAlertHighThreshold": 80,
        "capacityUsageState": "Normal",
        "capacityUsageType": "NetCapacity",
        "checksumEnabled": false,
        "compressionMethod": "Invalid",
        "dataLayout": "MediumGranularity",
        "externalAccelerationType": "None",
        "fglAccpId": null,
        "fglExtraCapacity": null,
        "fglMaxCompressionRatio": null,
        "fglMetadataSizeXx100": null,
        "fglNvdimmMetadataAmortizationX100": null,
        "fglNvdimmWriteCacheSizeInMb": null,
        "fglOverProvisioningFactor": null,
        "fglPerfProfile": null,
        "fglWriteAtomicitySize": null,
        "fragmentationEnabled": true,
        "id": "e0d8f6c900000000",
        "links": [
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000",
                "rel": "self"
            },
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000
                        /relationships/Statistics",
                "rel": "/api/StoragePool/relationship/Statistics"
            },
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000
                        /relationships/SpSds",
                "rel": "/api/StoragePool/relationship/SpSds"
            },
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000
                        /relationships/Volume",
                "rel": "/api/StoragePool/relationship/Volume"
            },
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000
                        /relationships/Device",
                "rel": "/api/StoragePool/relationship/Device"
            },
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000
                        /relationships/VTree",
                "rel": "/api/StoragePool/relationship/VTree"
            },
            {
                "href": "/api/instances/ProtectionDomain::9300c1f900000000",
                "rel": "/api/parent/relationship/protectionDomainId"
            }
        ],
        "statistics": {
                "BackgroundScannedInMB": 3466920,
                "activeBckRebuildCapacityInKb": 0,
                "activeEnterProtectedMaintenanceModeCapacityInKb": 0,
                "aggregateCompressionLevel": "Uncompressed",
                "atRestCapacityInKb": 1248256,
                "backgroundScanCompareErrorCount": 0,
                "backgroundScanFixedCompareErrorCount": 0,
                "bckRebuildReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "bckRebuildWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "capacityAvailableForVolumeAllocationInKb": 369098752,
                "capacityInUseInKb": 2496512,
                "capacityInUseNoOverheadInKb": 2496512,
                "capacityLimitInKb": 845783040,
                "compressedDataCompressionRatio": 0.0,
                "compressionRatio": 1.0,
                "currentFglMigrationSizeInKb": 0,
                "deviceIds": [
                ],
                "enterProtectedMaintenanceModeCapacityInKb": 0,
                "enterProtectedMaintenanceModeReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "enterProtectedMaintenanceModeWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "exitProtectedMaintenanceModeReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "exitProtectedMaintenanceModeWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "exposedCapacityInKb": 0,
                "failedCapacityInKb": 0,
                "fwdRebuildReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "fwdRebuildWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "inMaintenanceCapacityInKb": 0,
                "inMaintenanceVacInKb": 0,
                "inUseVacInKb": 184549376,
                "inaccessibleCapacityInKb": 0,
                "logWrittenBlocksInKb": 0,
                "maxCapacityInKb": 845783040,
                "migratingVolumeIds": [
                ],
                "migratingVtreeIds": [
                ],
                "movingCapacityInKb": 0,
                "netCapacityInUseInKb": 1248256,
                "normRebuildCapacityInKb": 0,
                "normRebuildReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "normRebuildWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "numOfDeviceAtFaultRebuilds": 0,
                "numOfDevices": 3,
                "numOfIncomingVtreeMigrations": 0,
                "numOfVolumes": 8,
                "numOfVolumesInDeletion": 0,
                "numOfVtrees": 8,
                "overallUsageRatio": 73.92289,
                "pendingBckRebuildCapacityInKb": 0,
                "pendingEnterProtectedMaintenanceModeCapacityInKb": 0,
                "pendingExitProtectedMaintenanceModeCapacityInKb": 0,
                "pendingFwdRebuildCapacityInKb": 0,
                "pendingMovingCapacityInKb": 0,
                "pendingMovingInBckRebuildJobs": 0,
                "persistentChecksumBuilderProgress": 100.0,
                "persistentChecksumCapacityInKb": 414720,
                "primaryReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "primaryReadFromDevBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "primaryReadFromRmcacheBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "primaryVacInKb": 92274688,
                "primaryWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "protectedCapacityInKb": 2496512,
                "protectedVacInKb": 184549376,
                "provisionedAddressesInKb": 2496512,
                "rebalanceCapacityInKb": 0,
                "rebalanceReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "rebalanceWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "rfacheReadHit": 0,
                "rfacheWriteHit": 0,
                "rfcacheAvgReadTime": 0,
                "rfcacheAvgWriteTime": 0,
                "rfcacheIoErrors": 0,
                "rfcacheIosOutstanding": 0,
                "rfcacheIosSkipped": 0,
                "rfcacheReadMiss": 0,
                "rmPendingAllocatedInKb": 0,
                "rmPendingThickInKb": 0,
                "rplJournalCapAllowed": 0,
                "rplTotalJournalCap": 0,
                "rplUsedJournalCap": 0,
                "secondaryReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "secondaryReadFromDevBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "secondaryReadFromRmcacheBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "secondaryVacInKb": 92274688,
                "secondaryWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "semiProtectedCapacityInKb": 0,
                "semiProtectedVacInKb": 0,
                "snapCapacityInUseInKb": 0,
                "snapCapacityInUseOccupiedInKb": 0,
                "snapshotCapacityInKb": 0,
                "spSdsIds": [
                    "abdfe71b00030001",
                    "abdce71d00040001",
                    "abdde71e00050001"
                ],
                "spareCapacityInKb": 84578304,
                "targetOtherLatency": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "targetReadLatency": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "targetWriteLatency": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "tempCapacityInKb": 0,
                "tempCapacityVacInKb": 0,
                "thickCapacityInUseInKb": 0,
                "thinAndSnapshotRatio": 73.92289,
                "thinCapacityAllocatedInKm": 184549376,
                "thinCapacityInUseInKb": 0,
                "thinUserDataCapacityInKb": 2496512,
                "totalFglMigrationSizeInKb": 0,
                "totalReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "totalWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "trimmedUserDataCapacityInKb": 0,
                "unreachableUnusedCapacityInKb": 0,
                "unusedCapacityInKb": 758708224,
                "userDataCapacityInKb": 2496512,
                "userDataCapacityNoTrimInKb": 2496512,
                "userDataReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "userDataSdcReadLatency": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "userDataSdcTrimLatency": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "userDataSdcWriteLatency": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "userDataTrimBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "userDataWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "volMigrationReadBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "volMigrationWriteBwc": {
                    "numOccured": 0,
                    "numSeconds": 0,
                    "totalWeightInKb": 0
                },
                "volumeAddressSpaceInKb": 922XXXXX,
                "volumeAllocationLimitInKb": 3707XXXXX,
                "volumeIds": [
                    "456afc7900XXXXXXXX"
                ],
                "vtreeAddresSpaceInKb": 92274688,
                "vtreeIds": [
                    "32b1681bXXXXXXXX",
                ]
        },
        "mediaType": "HDD",
        "name": "pool1",
        "numOfParallelRebuildRebalanceJobsPerDevice": 2,
        "persistentChecksumBuilderLimitKb": 3072,
        "persistentChecksumEnabled": true,
        "persistentChecksumState": "Protected",
        "persistentChecksumValidateOnRead": false,
        "protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold": null,
        "protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps": 10240,
        "protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice": 1,
        "protectedMaintenanceModeIoPriorityPolicy": "limitNumOfConcurrentIos",
        "protectedMaintenanceModeIoPriorityQuietPeriodInMsec": null,
        "protectionDomainId": "9300c1f900000000",
        "protectionDomainName": "domain1",
        "rebalanceEnabled": true,
        "rebalanceIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "rebalanceIoPriorityAppIopsPerDeviceThreshold": null,
        "rebalanceIoPriorityBwLimitPerDeviceInKbps": 10240,
        "rebalanceIoPriorityNumOfConcurrentIosPerDevice": 1,
        "rebalanceIoPriorityPolicy": "favorAppIos",
        "rebalanceIoPriorityQuietPeriodInMsec": null,
        "rebuildEnabled": true,
        "rebuildIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "rebuildIoPriorityAppIopsPerDeviceThreshold": null,
        "rebuildIoPriorityBwLimitPerDeviceInKbps": 10240,
        "rebuildIoPriorityNumOfConcurrentIosPerDevice": 1,
        "rebuildIoPriorityPolicy": "limitNumOfConcurrentIos",
        "rebuildIoPriorityQuietPeriodInMsec": null,
        "replicationCapacityMaxRatio": 32,
        "rmcacheWriteHandlingMode": "Cached",
        "sparePercentage": 10,
        "useRfcache": false,
        "useRmcache": false,
        "vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "vtreeMigrationIoPriorityAppIopsPerDeviceThreshold": null,
        "vtreeMigrationIoPriorityBwLimitPerDeviceInKbps": 10240,
        "vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice": 1,
        "vtreeMigrationIoPriorityPolicy": "favorAppIos",
        "vtreeMigrationIoPriorityQuietPeriodInMsec": null,
        "zeroPaddingEnabled": true
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('storage_pool')


class PowerFlexStoragePool(PowerFlexBase):
    """Class with storage pool operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        """ initialize the ansible module """
        argument_spec = dict(
            id=dict(type='str'),
            name=dict(type='str'),
            protection_domain_id=dict(type='str'),
            device_group_id=dict(type='str'),
            cap_alert_thresholds=dict(type='dict', options=dict(
                high_threshold=dict(type='int'),
                critical_threshold=dict(type='int'),
            )),
            over_provisioning_factor=dict(type='int'),
            physical_size_gb=dict(type='int'),
            protection_scheme=dict(type='str', choices=['TwoPlusTwo', 'EightPlusTwo']),
            compression_method=dict(type='str', choices=['None', 'Normal']),
            state=dict(required=True, type='str', choices=['present', 'absent']),
        )

        required_one_of = [['id', 'protection_domain_id']]
        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': False,
            'required_one_of': required_one_of,
        }

        super().__init__(module_params)


    def validate_input_params(self):
        """Validate the input parameters"""

    def get(self, id, protection_domain_id, name):
        """
        Get storage pool details
        :param id: Storage pool ID
        :type id: str
        :param protection_domain_id: Protection domain ID
        :type protection_domain_id: str
        :param name: Storage pool name
        :type name: str
        :return: Storage pool details
        """
        name_or_id = id if id else name
        try:
            if id:
                sp_details = self.powerflex_conn.storage_pool.get_by_id(id)
            else:
                sp_details = self.powerflex_conn.storage_pool.get_by_name(protection_domain_id, name)
            return sp_details
        except Exception as e:
            error_msg = "Failed to get the storage pool {0} with error " \
                       "{1}".format(name_or_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def delete(self, id):
        """
        Delete storage pool
        :param id: Storage pool ID
        :type id: str
        :rtype: None
        """
        try:
            self.powerflex_conn.storage_pool.delete(id)
            LOG.info("Storage pool deleted successfully.")
        except Exception as e:
            error_msg = "Delete storage pool '%s' operation failed" \
                        " with error '%s'" % (id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def create(self, storage_pool):
        """
        Create storage pool
        :param storage_pool: Dict of the storage pool
        :type storage_pool: dict
        :return: Dict representation of the created storage pool
        """
        try:
            LOG.info("Creating storage pool with name: %s ", storage_pool['name'])
            return self.powerflex_conn.storage_pool.create(storage_pool)
        except Exception as e:
            error_msg = "Create storage pool '%s' operation failed" \
                        " with error '%s'" % (storage_pool['name'], str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update(self, storage_pool):
        """
        Modify storage pool attributes
        :param storage_pool: Dictionary containing the attributes of
                            storage pool which are to be updated
        :type storage_pool: dict
        :return: Bool to indicate if storage pool is updated, 
                 Dict representation of the updated storage pool
        """
        try:
            LOG.info("Updating storage pool with id: %s ", storage_pool['id'])
            return self.powerflex_conn.storage_pool.update(storage_pool)
        except Exception as e:
            err_msg = "Failed to update the storage pool {0}" \
                    " with error {1}".format(storage_pool['id'],str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """
        Perform different actions on protection domain based on parameters
        passed in the playbook
        """
        storage_pool_id = self.module.params['id']
        storage_pool_name = self.module.params['name']
        protection_domain_id = self.module.params['protection_domain_id']
        device_group_id = self.module.params['device_group_id']
        cap_alert_thresholds = self.module.params['cap_alert_thresholds']
        cap_alert_high_threshold = None if cap_alert_thresholds is None else cap_alert_thresholds['high_threshold']
        cap_alert_critical_threshold = None if cap_alert_thresholds is None else cap_alert_thresholds['critical_threshold']
        over_provisioning_factor = self.module.params['over_provisioning_factor']
        physical_size_gb = self.module.params['physical_size_gb']
        protection_scheme = self.module.params['protection_scheme']
        compression_method = self.module.params['compression_method']
        state = self.module.params['state']

        result = dict(
            changed=False,
            storage_pool_details=None
        )

        self.validate_input_params()

        sp_details = self.get(
            storage_pool_id,
            protection_domain_id,
            storage_pool_name,
        )

        if state == 'absent':
            if sp_details:
                self.delete(sp_details['id'])
                result['changed'] = True
            self.module.exit_json(**result)
            return

        storage_pool = {}
        if storage_pool_name is not None:
            storage_pool['name'] = storage_pool_name
        if protection_domain_id is not None:
            storage_pool['protectionDomainId'] = protection_domain_id
        if device_group_id is not None:
            storage_pool['deviceGroupId'] = device_group_id
        if cap_alert_high_threshold is not None:
            storage_pool['capacityAlertHighThreshold'] = cap_alert_high_threshold
        if cap_alert_critical_threshold is not None:
            storage_pool['capacityAlertCriticalThreshold'] = cap_alert_critical_threshold
        if over_provisioning_factor is not None:
            storage_pool['overProvisioningFactor'] = over_provisioning_factor
        if physical_size_gb is not None:
            storage_pool['physicalSizeGB'] = physical_size_gb
        if protection_scheme is not None:
            storage_pool['protectionScheme'] = protection_scheme
        if compression_method is not None:
            storage_pool['compressionMethod'] = compression_method
        
        if not sp_details:
            result['storage_pool_details'] = self.create(storage_pool)
            result['changed'] = True
        else:
            storage_pool['id'] = sp_details['id']
            result['changed'], result['storage_pool_details'] = self.update(storage_pool)

        self.module.exit_json(**result)


def main():
    """ Create PowerFlex storage pool object and perform action on it
        based on user input from playbook"""
    obj = PowerFlexStoragePool()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
