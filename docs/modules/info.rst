.. _info_module:


info -- Gathering information about Dell PowerFlex
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gathering information about Dell PowerFlex storage system includes getting the api details, list of volumes, SDSs, SDCs, storage pools, protection domains, snapshot policies, and devices.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.12 or later.
- PyPowerFlex 1.6.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  gather_subset (optional, list, None)
    List of string variables to specify the Powerflex storage system entities for which information is required.

    Volumes - ``vol``.

    Storage pools - ``storage_pool``.

    Protection domains - ``protection_domain``.

    SDCs - ``sdc``.

    SDSs - ``sds``.

    Snapshot policies - ``snapshot_policy``.

    Devices - ``device``.

    Replication consistency groups - ``rcg``.

    Replication pairs - ``replication_pair``.


  filters (optional, list, None)
    List of filters to support filtered output for storage entities.

    Each filter is a list of *filter_key*, *filter_operator*, *filter_value*.

    Supports passing of multiple filters.


    filter_key (True, str, None)
      Name identifier of the filter.


    filter_operator (True, str, None)
      Operation to be performed on filter key.


    filter_value (True, str, None)
      Value of the filter key.



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
   - The *check_mode* is supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get detailed list of PowerFlex entities
      dellemc.powerflex.info:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        gather_subset:
          - vol
          - storage_pool
          - protection_domain
          - sdc
          - sds
          - snapshot_policy
          - device
          - rcg
          - replication_pair

    - name: Get a subset list of PowerFlex volumes
      dellemc.powerflex.info:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        gather_subset:
          - vol
        filters:
          - filter_key: "name"
            filter_operator: "equal"
            filter_value: "ansible_test"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


Array_Details (always, dict, {'addressSpaceUsage': 'Normal', 'authenticationMethod': 'Native', 'capacityAlertCriticalThresholdPercent': 90, 'capacityAlertHighThresholdPercent': 80, 'capacityTimeLeftInDays': '24', 'cliPasswordAllowed': True, 'daysInstalled': 66, 'defragmentationEnabled': True, 'enterpriseFeaturesEnabled': True, 'id': '4a54a8ba6df0690f', 'installId': '38622771228e56db', 'isInitialLicense': True, 'lastUpgradeTime': 0, 'managementClientSecureCommunicationEnabled': True, 'maxCapacityInGb': 'Unlimited', 'mdmCluster': {'clusterMode': 'ThreeNodes', 'clusterState': 'ClusteredNormal', 'goodNodesNum': 3, 'goodReplicasNum': 2, 'id': '5356091375512217871', 'master': {'id': '6101582c2ca8db00', 'ips': ['10.47.xxx.xxx'], 'managementIPs': ['10.47.xxx.xxx'], 'name': 'node0', 'opensslVersion': 'OpenSSL 1.0.2k-fips  26 Jan 2017', 'port': 9011, 'role': 'Manager', 'status': 'Normal', 'versionInfo': 'R3_6.0.0', 'virtualInterfaces': ['ens160']}, 'slaves': [{'id': '23fb724015661901', 'ips': ['10.47.xxx.xxx'], 'managementIPs': ['10.47.xxx.xxx'], 'opensslVersion': 'OpenSSL 1.0.2k-fips  26 Jan 2017', 'port': 9011, 'role': 'Manager', 'status': 'Normal', 'versionInfo': 'R3_6.0.0', 'virtualInterfaces': ['ens160']}], 'tieBreakers': [{'id': '6ef27eb20d0c1202', 'ips': ['10.47.xxx.xxx'], 'managementIPs': ['10.47.xxx.xxx'], 'opensslVersion': 'N/A', 'port': 9011, 'role': 'TieBreaker', 'status': 'Normal', 'versionInfo': 'R3_6.0.0'}]}, 'mdmExternalPort': 7611, 'mdmManagementPort': 6611, 'mdmSecurityPolicy': 'None', 'showGuid': True, 'swid': '', 'systemVersionName': 'DellEMC PowerFlex Version: R3_6.0.354', 'tlsVersion': 'TLSv1.2', 'upgradeState': 'NoUpgrade'})
  System entities of PowerFlex storage array.


  addressSpaceUsage (, str, )
    Address space usage.


  authenticationMethod (, str, )
    Authentication method.


  capacityAlertCriticalThresholdPercent (, int, )
    Capacity alert critical threshold percentage.


  capacityAlertHighThresholdPercent (, int, )
    Capacity alert high threshold percentage.


  capacityTimeLeftInDays (, str, )
    Capacity time left in days.


  cliPasswordAllowed (, bool, )
    CLI password allowed.


  daysInstalled (, int, )
    Days installed.


  defragmentationEnabled (, bool, )
    Defragmentation enabled.


  enterpriseFeaturesEnabled (, bool, )
    Enterprise features enabled.


  id (, str, )
    The ID of the system.


  installId (, str, )
    installation Id.


  isInitialLicense (, bool, )
    Initial license.


  lastUpgradeTime (, int, )
    Last upgrade time.


  managementClientSecureCommunicationEnabled (, bool, )
    Management client secure communication enabled.


  maxCapacityInGb (, dict, )
    Maximum capacity in GB.


  mdmCluster (, dict, )
    MDM cluster details.


  mdmExternalPort (, int, )
    MDM external port.


  mdmManagementPort (, int, )
    MDM management port.


  mdmSecurityPolicy (, str, )
    MDM security policy.


  showGuid (, bool, )
    Show guid.


  swid (, str, )
    SWID.


  systemVersionName (, str, )
    System version and name.


  tlsVersion (, str, )
    TLS version.


  upgradeState (, str, )
    Upgrade state.



API_Version (always, str, 3.5)
  API version of PowerFlex API Gateway.


Protection_Domains (always, list, [{'id': '9300e90900000001', 'name': 'domain2'}, {'id': '9300c1f900000000', 'name': 'domain1'}])
  Details of all protection domains.


  id (, str, )
    protection domain id.


  name (, str, )
    protection domain name.



SDCs (always, list, [{'id': '07335d3d00000006', 'name': 'LGLAP203'}, {'id': '07335d3c00000005', 'name': 'LGLAP178'}, {'id': '0733844a00000003'}])
  Details of storage data clients.


  id (, str, )
    storage data client id.


  name (, str, )
    storage data client name.



SDSs (always, list, [{'id': '8f3bb0cc00000002', 'name': 'node0'}, {'id': '8f3bb0ce00000000', 'name': 'node1'}, {'id': '8f3bb15300000001', 'name': 'node22'}])
  Details of storage data servers.


  id (, str, )
    storage data server id.


  name (, str, )
    storage data server name.



Snapshot_Policies (always, list, [{'id': '2b380c5c00000000', 'name': 'sample_snap_policy'}, {'id': '2b380c5d00000001', 'name': 'sample_snap_policy_1'}])
  Details of snapshot policies.


  id (, str, )
    snapshot policy id.


  name (, str, )
    snapshot policy name.



Storage_Pools (always, list, [{'addressSpaceUsage': 'Normal', 'addressSpaceUsageType': 'DeviceCapacityLimit', 'backgroundScannerBWLimitKBps': 3072, 'backgroundScannerMode': 'DataComparison', 'bgScannerCompareErrorAction': 'ReportAndFix', 'bgScannerReadErrorAction': 'ReportAndFix', 'capacityAlertCriticalThreshold': 90, 'capacityAlertHighThreshold': 80, 'capacityUsageState': 'Normal', 'capacityUsageType': 'NetCapacity', 'checksumEnabled': False, 'compressionMethod': 'Invalid', 'dataLayout': 'MediumGranularity', 'externalAccelerationType': 'None', 'fglAccpId': None, 'fglExtraCapacity': None, 'fglMaxCompressionRatio': None, 'fglMetadataSizeXx100': None, 'fglNvdimmMetadataAmortizationX100': None, 'fglNvdimmWriteCacheSizeInMb': None, 'fglOverProvisioningFactor': None, 'fglPerfProfile': None, 'fglWriteAtomicitySize': None, 'fragmentationEnabled': True, 'id': 'e0d8f6c900000000', 'links': [{'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': 'self'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/Statistics', 'rel': '/api/StoragePool/relationship/Statistics'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/SpSds', 'rel': '/api/StoragePool/relationship/SpSds'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/Volume', 'rel': '/api/StoragePool/relationship/Volume'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/Device', 'rel': '/api/StoragePool/relationship/Device'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000 /relationships/VTree', 'rel': '/api/StoragePool/relationship/VTree'}, {'href': '/api/instances/ProtectionDomain::9300c1f900000000', 'rel': '/api/parent/relationship/protectionDomainId'}], 'statistics': {'BackgroundScannedInMB': 3466920, 'activeBckRebuildCapacityInKb': 0, 'activeEnterProtectedMaintenanceModeCapacityInKb': 0, 'aggregateCompressionLevel': 'Uncompressed', 'atRestCapacityInKb': 1248256, 'backgroundScanCompareErrorCount': 0, 'backgroundScanFixedCompareErrorCount': 0, 'bckRebuildReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'bckRebuildWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'capacityAvailableForVolumeAllocationInKb': 369098752, 'capacityInUseInKb': 2496512, 'capacityInUseNoOverheadInKb': 2496512, 'capacityLimitInKb': 845783040, 'compressedDataCompressionRatio': 0.0, 'compressionRatio': 1.0, 'currentFglMigrationSizeInKb': 0, 'deviceIds': [], 'enterProtectedMaintenanceModeCapacityInKb': 0, 'enterProtectedMaintenanceModeReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'enterProtectedMaintenanceModeWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'exitProtectedMaintenanceModeReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'exitProtectedMaintenanceModeWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'exposedCapacityInKb': 0, 'failedCapacityInKb': 0, 'fwdRebuildReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'fwdRebuildWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'inMaintenanceCapacityInKb': 0, 'inMaintenanceVacInKb': 0, 'inUseVacInKb': 184549376, 'inaccessibleCapacityInKb': 0, 'logWrittenBlocksInKb': 0, 'maxCapacityInKb': 845783040, 'migratingVolumeIds': [], 'migratingVtreeIds': [], 'movingCapacityInKb': 0, 'netCapacityInUseInKb': 1248256, 'normRebuildCapacityInKb': 0, 'normRebuildReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'normRebuildWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'numOfDeviceAtFaultRebuilds': 0, 'numOfDevices': 3, 'numOfIncomingVtreeMigrations': 0, 'numOfVolumes': 8, 'numOfVolumesInDeletion': 0, 'numOfVtrees': 8, 'overallUsageRatio': 73.92289, 'pendingBckRebuildCapacityInKb': 0, 'pendingEnterProtectedMaintenanceModeCapacityInKb': 0, 'pendingExitProtectedMaintenanceModeCapacityInKb': 0, 'pendingFwdRebuildCapacityInKb': 0, 'pendingMovingCapacityInKb': 0, 'pendingMovingInBckRebuildJobs': 0, 'persistentChecksumBuilderProgress': 100.0, 'persistentChecksumCapacityInKb': 414720, 'primaryReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'primaryReadFromDevBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'primaryReadFromRmcacheBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'primaryVacInKb': 92274688, 'primaryWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'protectedCapacityInKb': 2496512, 'protectedVacInKb': 184549376, 'provisionedAddressesInKb': 2496512, 'rebalanceCapacityInKb': 0, 'rebalanceReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'rebalanceWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'rfacheReadHit': 0, 'rfacheWriteHit': 0, 'rfcacheAvgReadTime': 0, 'rfcacheAvgWriteTime': 0, 'rfcacheIoErrors': 0, 'rfcacheIosOutstanding': 0, 'rfcacheIosSkipped': 0, 'rfcacheReadMiss': 0, 'rmPendingAllocatedInKb': 0, 'rmPendingThickInKb': 0, 'rplJournalCapAllowed': 0, 'rplTotalJournalCap': 0, 'rplUsedJournalCap': 0, 'secondaryReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'secondaryReadFromDevBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'secondaryReadFromRmcacheBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'secondaryVacInKb': 92274688, 'secondaryWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'semiProtectedCapacityInKb': 0, 'semiProtectedVacInKb': 0, 'snapCapacityInUseInKb': 0, 'snapCapacityInUseOccupiedInKb': 0, 'snapshotCapacityInKb': 0, 'spSdsIds': ['abdfe71b00030001', 'abdce71d00040001', 'abdde71e00050001'], 'spareCapacityInKb': 84578304, 'targetOtherLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'targetReadLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'targetWriteLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'tempCapacityInKb': 0, 'tempCapacityVacInKb': 0, 'thickCapacityInUseInKb': 0, 'thinAndSnapshotRatio': 73.92289, 'thinCapacityAllocatedInKm': 184549376, 'thinCapacityInUseInKb': 0, 'thinUserDataCapacityInKb': 2496512, 'totalFglMigrationSizeInKb': 0, 'totalReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'totalWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'trimmedUserDataCapacityInKb': 0, 'unreachableUnusedCapacityInKb': 0, 'unusedCapacityInKb': 758708224, 'userDataCapacityInKb': 2496512, 'userDataCapacityNoTrimInKb': 2496512, 'userDataReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcReadLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcTrimLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcWriteLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataTrimBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'volMigrationReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'volMigrationWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'volumeAddressSpaceInKb': '922XXXXX', 'volumeAllocationLimitInKb': '3707XXXXX', 'volumeIds': ['456afc7900XXXXXXXX'], 'vtreeAddresSpaceInKb': 92274688, 'vtreeIds': ['32b1681bXXXXXXXX']}, 'mediaType': 'HDD', 'name': 'pool1', 'numOfParallelRebuildRebalanceJobsPerDevice': 2, 'persistentChecksumBuilderLimitKb': 3072, 'persistentChecksumEnabled': True, 'persistentChecksumState': 'Protected', 'persistentChecksumValidateOnRead': False, 'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None, 'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None, 'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': 10240, 'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': 1, 'protectedMaintenanceModeIoPriorityPolicy': 'limitNumOfConcurrentIos', 'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None, 'protectionDomainId': '9300c1f900000000', 'protectionDomainName': 'domain1', 'rebalanceEnabled': True, 'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebalanceIoPriorityAppIopsPerDeviceThreshold': None, 'rebalanceIoPriorityBwLimitPerDeviceInKbps': 10240, 'rebalanceIoPriorityNumOfConcurrentIosPerDevice': 1, 'rebalanceIoPriorityPolicy': 'favorAppIos', 'rebalanceIoPriorityQuietPeriodInMsec': None, 'rebuildEnabled': True, 'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebuildIoPriorityAppIopsPerDeviceThreshold': None, 'rebuildIoPriorityBwLimitPerDeviceInKbps': 10240, 'rebuildIoPriorityNumOfConcurrentIosPerDevice': 1, 'rebuildIoPriorityPolicy': 'limitNumOfConcurrentIos', 'rebuildIoPriorityQuietPeriodInMsec': None, 'replicationCapacityMaxRatio': 32, 'rmcacheWriteHandlingMode': 'Cached', 'sparePercentage': 10, 'useRfcache': False, 'useRmcache': False, 'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None, 'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None, 'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': 10240, 'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': 1, 'vtreeMigrationIoPriorityPolicy': 'favorAppIos', 'vtreeMigrationIoPriorityQuietPeriodInMsec': None, 'zeroPaddingEnabled': True}])
  Details of storage pools.


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




Volumes (always, list, [{'accessModeLimit': 'ReadWrite', 'ancestorVolumeId': None, 'autoSnapshotGroupId': None, 'compressionMethod': 'Invalid', 'consistencyGroupId': None, 'creationTime': 1661234220, 'dataLayout': 'MediumGranularity', 'id': '456afd7XXXXXXX', 'lockedAutoSnapshot': False, 'lockedAutoSnapshotMarkedForRemoval': False, 'managedBy': 'ScaleIO', 'mappedSdcInfo': [{'accessMode': 'ReadWrite', 'isDirectBufferMapping': False, 'limitBwInMbps': 0, 'limitIops': 0, 'sdcId': 'c42425cbXXXXX', 'sdcIp': '10.XXX.XX.XX', 'sdcName': None}], 'name': 'vol-1', 'notGenuineSnapshot': False, 'originalExpiryTime': 0, 'pairIds': None, 'replicationJournalVolume': False, 'replicationTimeStamp': 0, 'retentionLevels': [], 'secureSnapshotExpTime': 0, 'sizeInKb': 8388608, 'snplIdOfAutoSnapshot': None, 'snplIdOfSourceVolume': None, 'statistics': {'childVolumeIds': [], 'descendantVolumeIds': [], 'initiatorSdcId': None, 'mappedSdcIds': ['c42425XXXXXX'], 'numOfChildVolumes': 0, 'numOfDescendantVolumes': 0, 'numOfMappedSdcs': 1, 'registrationKey': None, 'registrationKeys': [], 'replicationJournalVolume': False, 'replicationState': 'UnmarkedForReplication', 'reservationType': 'NotReserved', 'rplTotalJournalCap': 0, 'rplUsedJournalCap': 0, 'userDataReadBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcReadLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcTrimLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataSdcWriteLatency': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataTrimBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}, 'userDataWriteBwc': {'numOccured': 0, 'numSeconds': 0, 'totalWeightInKb': 0}}, 'storagePoolId': '7630a248XXXXXXX', 'timeStampIsAccurate': False, 'useRmcache': False, 'volumeReplicationState': 'UnmarkedForReplication', 'volumeType': 'ThinProvisioned', 'vtreeId': '32b168bXXXXXX'}])
  Details of volumes.


  id (, str, )
    The ID of the volume.


  mappedSdcInfo (, dict, )
    The details of the mapped SDC.


    sdcId (, str, )
      ID of the SDC.


    sdcName (, str, )
      Name of the SDC.


    sdcIp (, str, )
      IP of the SDC.


    accessMode (, str, )
      mapping access mode for the specified volume.


    limitIops (, int, )
      IOPS limit for the SDC.


    limitBwInMbps (, int, )
      Bandwidth limit for the SDC.



  name (, str, )
    Name of the volume.


  sizeInKb (, int, )
    Size of the volume in Kb.


  sizeInGb (, int, )
    Size of the volume in Gb.


  storagePoolId (, str, )
    ID of the storage pool in which volume resides.


  storagePoolName (, str, )
    Name of the storage pool in which volume resides.


  protectionDomainId (, str, )
    ID of the protection domain in which volume resides.


  protectionDomainName (, str, )
    Name of the protection domain in which volume resides.


  snapshotPolicyId (, str, )
    ID of the snapshot policy associated with volume.


  snapshotPolicyName (, str, )
    Name of the snapshot policy associated with volume.


  snapshotsList (, str, )
    List of snapshots associated with the volume.


  statistics (, dict, )
    Statistics details of the storage pool.


    numOfChildVolumes (, int, )
      Number of child volumes.


    numOfMappedSdcs (, int, )
      Number of mapped Sdcs of the volume.




Devices (always, list, [{'id': 'b6efa59900000000', 'name': 'device230'}, {'id': 'b6efa5fa00020000', 'name': 'device_node0'}, {'id': 'b7f3a60900010000', 'name': 'device22'}])
  Details of devices.


  id (, str, )
    device id.


  name (, str, )
    device name.



Replication_Consistency_Groups (always, list, {'protectionDomainId': 'b969400500000000', 'peerMdmId': '6c3d94f600000000', 'remoteId': '2130961a00000000', 'remoteMdmId': '0e7a082862fedf0f', 'currConsistMode': 'Consistent', 'freezeState': 'Unfrozen', 'lifetimeState': 'Normal', 'pauseMode': 'None', 'snapCreationInProgress': False, 'lastSnapGroupId': 'e58280b300000001', 'lastSnapCreationRc': 'SUCCESS', 'targetVolumeAccessMode': 'NoAccess', 'remoteProtectionDomainId': '4eeb304600000000', 'remoteProtectionDomainName': 'domain1', 'failoverType': 'None', 'failoverState': 'None', 'activeLocal': True, 'activeRemote': True, 'abstractState': 'Ok', 'localActivityState': 'Active', 'remoteActivityState': 'Active', 'inactiveReason': 11, 'rpoInSeconds': 30, 'replicationDirection': 'LocalToRemote', 'disasterRecoveryState': 'None', 'remoteDisasterRecoveryState': 'None', 'error': 65, 'name': 'test_rcg', 'type': 'User', 'id': 'aadc17d500000000'})
  Details of rcgs.


  id (, str, )
    The ID of the replication consistency group.


  name (, str, )
    The name of the replication consistency group.


  protectionDomainId (, str, )
    The Protection Domain ID of the replication consistency group.


  peerMdmId (, str, )
    The ID of the peer MDM of the replication consistency group.


  remoteId (, str, )
    The ID of the remote replication consistency group.


  remoteMdmId (, str, )
    The ID of the remote MDM of the replication consistency group.


  currConsistMode (, str, )
    The current consistency mode of the replication consistency group.


  freezeState (, str, )
    The freeze state of the replication consistency group.


  lifetimeState (, str, )
    The Lifetime state of the replication consistency group.


  pauseMode (, str, )
    The Lifetime state of the replication consistency group.


  snapCreationInProgress (, bool, )
    Whether the process of snapshot creation of the replication consistency group is in progress or not.


  lastSnapGroupId (, str, )
    ID of the last snapshot of the replication consistency group.


  lastSnapCreationRc (, int, )
    The return code of the last snapshot of the replication consistency group.


  targetVolumeAccessMode (, str, )
    The access mode of the target volume of the replication consistency group.


  remoteProtectionDomainId (, str, )
    The ID of the remote Protection Domain.


  remoteProtectionDomainName (, str, )
    The Name of the remote Protection Domain.


  failoverType (, str, )
    The type of failover of the replication consistency group.


  failoverState (, str, )
    The state of failover of the replication consistency group.


  activeLocal (, bool, )
    Whether the local replication consistency group is active.


  activeRemote (, bool, )
    Whether the remote replication consistency group is active


  abstractState (, str, )
    The abstract state of the replication consistency group.


  localActivityState (, str, )
    The state of activity of the local replication consistency group.


  remoteActivityState (, str, )
    The state of activity of the remote replication consistency group..


  inactiveReason (, int, )
    The reason for the inactivity of the replication consistency group.


  rpoInSeconds (, int, )
    The RPO value of the replication consistency group in seconds.


  replicationDirection (, str, )
    The direction of the replication of the replication consistency group.


  disasterRecoveryState (, str, )
    The state of disaster recovery of the local replication consistency group.


  remoteDisasterRecoveryState (, str, )
    The state of disaster recovery of the remote replication consistency group.


  error (, int, )
    The error code of the replication consistency group.


  type (, str, )
    The type of the replication consistency group.



Replication_pairs (Always, list, {'copyType': 'OnlineCopy', 'id': '23aa0bc900000001', 'initialCopyPriority': -1, 'initialCopyState': 'Done', 'lifetimeState': 'Normal', 'localActivityState': 'RplEnabled', 'localVolumeId': 'e2bc1fab00000008', 'name': None, 'peerSystemName': None, 'remoteActivityState': 'RplEnabled', 'remoteCapacityInMB': 8192, 'remoteId': 'a058446700000001', 'remoteVolumeId': '1cda7af20000000d', 'remoteVolumeName': 'vol', 'replicationConsistencyGroupId': 'e2ce036b00000002', 'userRequestedPauseTransmitInitCopy': False})
  Details of the replication pairs.


  id (, str, )
    The ID of the replication pair.


  name (, str, )
    The name of the replication pair.


  remoteId (, str, )
    The ID of the remote replication pair.


  localVolumeId (, str, )
    The ID of the local volume.


  replicationConsistencyGroupId (, str, )
    The ID of the replication consistency group.


  copyType (, str, )
    The copy type of the replication pair.


  initialCopyState (, str, )
    The inital copy state of the replication pair.


  localActivityState (, str, )
    The state of activity of the local replication pair.


  remoteActivityState (, str, )
    The state of activity of the remote replication pair.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

