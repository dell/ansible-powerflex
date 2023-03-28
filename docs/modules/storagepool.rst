.. _storagepool_module:


storagepool -- Managing Dell PowerFlex storage pool
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Dell PowerFlex storage pool module includes getting the details of storage pool, creating a new storage pool, and modifying the attribute of a storage pool.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.12 or later.
- PyPowerFlex 1.6.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  storage_pool_name (optional, str, None)
    The name of the storage pool.

    If more than one storage pool is found with the same name then protection domain id/name is required to perform the task.

    Mutually exclusive with *storage_pool_id*.


  storage_pool_id (optional, str, None)
    The id of the storage pool.

    It is auto generated, hence should not be provided during creation of a storage pool.

    Mutually exclusive with *storage_pool_name*.


  protection_domain_name (optional, str, None)
    The name of the protection domain.

    During creation of a pool, either protection domain name or id must be mentioned.

    Mutually exclusive with *protection_domain_id*.


  protection_domain_id (optional, str, None)
    The id of the protection domain.

    During creation of a pool, either protection domain name or id must be mentioned.

    Mutually exclusive with *protection_domain_name*.


  media_type (optional, str, None)
    Type of devices in the storage pool.


  storage_pool_new_name (optional, str, None)
    New name for the storage pool can be provided.

    This parameter is used for renaming the storage pool.


  use_rfcache (optional, bool, None)
    Enable/Disable RFcache on a specific storage pool.


  use_rmcache (optional, bool, None)
    Enable/Disable RMcache on a specific storage pool.


  state (True, str, None)
    State of the storage pool.


  hostname (True, str, None)
    IP or FQDN of the PowerFlex host.


  username (True, str, None)
    The username of the PowerFlex host.


  password (True, str, None)
    The password of the PowerFlex host.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    ``true`` - Indicates that the SSL certificate should be verified.

    ``false`` - Indicates that the SSL certificate should not be verified.


  port (optional, int, 443)
    Port number through which communication happens with PowerFlex host.


  timeout (False, int, 120)
    Time after which connection will get terminated.

    It is to be mentioned in seconds.





Notes
-----

.. note::
   - TRANSITIONAL media type is supported only during modification.
   - The *check_mode* is not supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

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

    - name: Create a new storage pool by name
      dellemc.powerflex.storagepool:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_pool_name: "ansible_test_pool"
        protection_domain_id: "1c957da800000000"
        media_type: "HDD"
        state: "present"

    - name: Modify a storage pool by name
      dellemc.powerflex.storagepool:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_pool_name: "ansible_test_pool"
        protection_domain_id: "1c957da800000000"
        use_rmcache: True
        use_rfcache: True
        state: "present"

    - name: Rename storage pool by id
      dellemc.powerflex.storagepool:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_pool_id: "abcd1234ab12r"
        storage_pool_new_name: "new_ansible_pool"
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


storage_pool_details (When storage pool exists, dict, {'addressSpaceUsage': 'Normal', 'addressSpaceUsageType': 'DeviceCapacityLimit', 'backgroundScannerBWLimitKBps': 3072, 'backgroundScannerMode': 'DataComparison', 'bgScannerCompareErrorAction': 'ReportAndFix', 'bgScannerReadErrorAction': 'ReportAndFix', 'capacityAlertCriticalThreshold': 90, 'capacityAlertHighThreshold': 80, 'capacityUsageState': 'Normal', 'capacityUsageType': 'NetCapacity', 'checksumEnabled': False, 'compressionMethod': 'Invalid', 'dataLayout': 'MediumGranularity', 'externalAccelerationType': 'None', 'fglAccpId': None, 'fglExtraCapacity': None, 'fglMaxCompressionRatio': None, 'fglMetadataSizeXx100': None, 'fglNvdimmMetadataAmortizationX100': None, 'fglNvdimmWriteCacheSizeInMb': None, 'fglOverProvisioningFactor': None, 'fglPerfProfile': None, 'fglWriteAtomicitySize': None, 'fragmentationEnabled': True, 'id': 'e0d8f6c900000000', 'links': [{'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': 'self'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/Statistics', 'rel': '/api/StoragePool/relationship/Statistics'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/SpSds', 'rel': '/api/StoragePool/relationship/SpSds'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/Volume', 'rel': '/api/StoragePool/relationship/Volume'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/Device', 'rel': '/api/StoragePool/relationship/Device'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/VTree', 'rel': '/api/StoragePool/relationship/VTree'}, {'href': '/api/instances/ProtectionDomain::9300c1f900000000', 'rel': '/api/parent/relationship/protectionDomainId'}], 'statistics': {'BackgroundScannedInMB': 3466920, 'activeBckRebuildCapacityInKb': 0, 'activeEnterProtectedMaintenanceModeCapacityInKb': 0, 'aggregateCompressionLevel': 'Uncompressed', 'atRestCapacityInKb': 1248256, 'backgroundScanCompareErrorCount': 0, 'backgroundScanFixedCompareErrorCount': 0, 'bckRebuildReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'bckRebuildWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'capacityAvailableForVolumeAllocationInKb': 369098752, 'capacityInUseInKb': 2496512, 'capacityInUseNoOverheadInKb': 2496512, 'capacityLimitInKb': 845783040, 'compressedDataCompressionRatio': 0.0, 'compressionRatio': 1.0, 'currentFglMigrationSizeInKb': 0, 'deviceIds': [], 'enterProtectedMaintenanceModeCapacityInKb': 0, 'enterProtectedMaintenanceModeReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'enterProtectedMaintenanceModeWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'exitProtectedMaintenanceModeReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'exitProtectedMaintenanceModeWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'exposedCapacityInKb': 0, 'failedCapacityInKb': 0, 'fwdRebuildReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'fwdRebuildWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'inMaintenanceCapacityInKb': 0, 'inMaintenanceVacInKb': 0, 'inUseVacInKb': 184549376, 'inaccessibleCapacityInKb': 0, 'logWrittenBlocksInKb': 0, 'maxCapacityInKb': 845783040, 'migratingVolumeIds': [], 'migratingVtreeIds': [], 'movingCapacityInKb': 0, 'netCapacityInUseInKb': 1248256, 'normRebuildCapacityInKb': 0, 'normRebuildReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'normRebuildWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'numOfDeviceAtFaultRebuilds': 0, 'numOfDevices': 3, 'numOfIncomingVtreeMigrations': 0, 'numOfVolumes': 8, 'numOfVolumesInDeletion': 0, 'numOfVtrees': 8, 'overallUsageRatio': 73.92289, 'pendingBckRebuildCapacityInKb': 0, 'pendingEnterProtectedMaintenanceModeCapacityInKb': 0, 'pendingExitProtectedMaintenanceModeCapacityInKb': 0, 'pendingFwdRebuildCapacityInKb': 0, 'pendingMovingCapacityInKb': 0, 'pendingMovingInBckRebuildJobs': 0, 'persistentChecksumBuilderProgress': 100.0, 'persistentChecksumCapacityInKb': 414720, 'primaryReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'primaryReadFromDevBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'primaryReadFromRmcacheBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'primaryVacInKb': 92274688, 'primaryWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'protectedCapacityInKb': 2496512, 'protectedVacInKb': 184549376, 'provisionedAddressesInKb': 2496512, 'rebalanceCapacityInKb': 0, 'rebalanceReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'rebalanceWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'rfacheReadHit': 0, 'rfacheWriteHit': 0, 'rfcacheAvgReadTime': 0, 'rfcacheAvgWriteTime': 0, 'rfcacheIoErrors': 0, 'rfcacheIosOutstanding': 0, 'rfcacheIosSkipped': 0, 'rfcacheReadMiss': 0, 'rmPendingAllocatedInKb': 0, 'rmPendingThickInKb': 0, 'rplJournalCapAllowed': 0, 'rplTotalJournalCap': 0, 'rplUsedJournalCap': 0, 'secondaryReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'secondaryReadFromDevBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'secondaryReadFromRmcacheBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'secondaryVacInKb': 92274688, 'secondaryWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'semiProtectedCapacityInKb': 0, 'semiProtectedVacInKb': 0, 'snapCapacityInUseInKb': 0, 'snapCapacityInUseOccupiedInKb': 0, 'snapshotCapacityInKb': 0, 'spSdsIds': ['abdfe71b00030001', 'abdce71d00040001', 'abdde71e00050001'], 'spareCapacityInKb': 84578304, 'targetOtherLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'targetReadLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'targetWriteLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'tempCapacityInKb': 0, 'tempCapacityVacInKb': 0, 'thickCapacityInUseInKb': 0, 'thinAndSnapshotRatio': 73.92289, 'thinCapacityAllocatedInKm': 184549376, 'thinCapacityInUseInKb': 0, 'thinUserDataCapacityInKb': 2496512, 'totalFglMigrationSizeInKb': 0, 'totalReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'totalWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'trimmedUserDataCapacityInKb': 0, 'unreachableUnusedCapacityInKb': 0, 'unusedCapacityInKb': 758708224, 'userDataCapacityInKb': 2496512, 'userDataCapacityNoTrimInKb': 2496512, 'userDataReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcReadLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcTrimLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcWriteLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataTrimBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'volMigrationReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'volMigrationWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'volumeAddressSpaceInKb': '922XXXXX', 'volumeAllocationLimitInKb': '3707XXXXX', 'volumeIds': ['456afc7900XXXXXXXX'], 'vtreeAddresSpaceInKb': 92274688, 'vtreeIds': ['32b1681bXXXXXXXX']}, 'mediaType': 'HDD', 'name': 'pool1', 'numOfParallelRebuildRebalanceJobsPerDevice': 2, 'persistentChecksumBuilderLimitKb': 3072, 'persistentChecksumEnabled': True, 'persistentChecksumState': 'Protected', 'persistentChecksumValidateOnRead': False, 'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None, 'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None, 'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': 10240, 'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': 1, 'protectedMaintenanceModeIoPriorityPolicy': 'limitNumOfConcurrentIos', 'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None, 'protectionDomainId': '9300c1f900000000', 'protectionDomainName': 'domain1', 'rebalanceEnabled': True, 'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebalanceIoPriorityAppIopsPerDeviceThreshold': None, 'rebalanceIoPriorityBwLimitPerDeviceInKbps': 10240, 'rebalanceIoPriorityNumOfConcurrentIosPerDevice': 1, 'rebalanceIoPriorityPolicy': 'favorAppIos', 'rebalanceIoPriorityQuietPeriodInMsec': None, 'rebuildEnabled': True, 'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebuildIoPriorityAppIopsPerDeviceThreshold': None, 'rebuildIoPriorityBwLimitPerDeviceInKbps': 10240, 'rebuildIoPriorityNumOfConcurrentIosPerDevice': 1, 'rebuildIoPriorityPolicy': 'limitNumOfConcurrentIos', 'rebuildIoPriorityQuietPeriodInMsec': None, 'replicationCapacityMaxRatio': 32, 'rmcacheWriteHandlingMode': 'Cached', 'sparePercentage': 10, 'useRfcache': False, 'useRmcache': False, 'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None, 'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None, 'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': 10240, 'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': 1, 'vtreeMigrationIoPriorityPolicy': 'favorAppIos', 'vtreeMigrationIoPriorityQuietPeriodInMsec': None, 'zeroPaddingEnabled': True})
  Details of the storage pool.


  mediaType (, str, )
    Type of devices in the storage pool.


  useRfcache (, bool, )
    Enable/Disable RFcache on a specific storage pool.


  useRmcache (, bool, )
    Enable/Disable RMcache on a specific storage pool.


  id (, str, )
    ID of the storage pool under protection domain.


  name (, str, )
    Name of the storage pool under protection domain.


  protectionDomainId (, str, )
    ID of the protection domain in which pool resides.


  protectionDomainName (, str, )
    Name of the protection domain in which pool resides.


  statistics (, dict, )
    Statistics details of the storage pool.


    capacityInUseInKb (, str, )
      Total capacity of the storage pool.


    unusedCapacityInKb (, str, )
      Unused capacity of the storage pool.


    deviceIds (, list, )
      Device Ids of the storage pool.







Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

