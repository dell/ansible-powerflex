.. _info_module:


info -- Gathering information about Dell PowerFlex
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gathering information about Dell PowerFlex storage system includes getting the api details, list of volumes, SDSs, SDCs, storage pools, protection domains, snapshot policies, and devices.

Gathering information about Dell PowerFlex Manager includes getting the list of managed devices, deployments, service templates and firmware repository.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.12.0.



Parameters
----------

  gather_subset (optional, list, None)
    List of string variables to specify the PowerFlex storage system entities for which information is required.

    Volumes - ``vol``.

    Storage pools - ``storage_pool``.

    Protection domains - ``protection_domain``.

    SDCs - ``sdc``.

    SDSs - ``sds``.

    Snapshot policies - ``snapshot_policy``.

    Devices - ``device``.

    Replication consistency groups - ``rcg``.

    Replication pairs - ``replication_pair``.

    Fault Sets - ``fault_set``.

    Service templates - ``service_template``.

    Managed devices - ``managed_device``.

    Deployments - ``deployment``.

    FirmwareRepository - ``firmware_repository``.


  filters (optional, list, None)
    List of filters to support filtered output for storage entities.

    Each filter is a list of *filter_key*, *filter_operator*, *filter_value*.

    Supports passing of multiple filters.


    filter_key (True, str, None)
      Name identifier of the filter.


    filter_operator (True, str, None)
      Operation to be performed on filter key.

      Choice ``contains`` is supported for *gather_subset* keys ``service_template``, ``managed_device``, ``deployment``, ``firmware_repository``.


    filter_value (True, str, None)
      Value of the filter key.



  limit (optional, int, 50)
    Page limit.

    Supported for *gather_subset* keys ``service_template``, ``managed_device``, ``deployment``, ``firmware_repository``.


  offset (optional, int, 0)
    Pagination offset.

    Supported for *gather_subset* keys ``service_template``, ``managed_device``, ``deployment``, ``firmware_repository``.


  sort (optional, str, None)
    Sort the returned components based on specified field.

    Supported for *gather_subset* keys ``service_template``, ``managed_device``, ``deployment``, ``firmware_repository``.

    The supported sort keys for the *gather_subset* can be referred from PowerFlex Manager API documentation in https://developer.dell.com.


  include_devices (optional, bool, True)
    Include devices in response.

    Applicable when *gather_subset* is ``deployment``.


  include_template (optional, bool, True)
    Include service templates in response.

    Applicable when *gather_subset* is ``deployment``.


  full (optional, bool, False)
    Specify if response is full or brief.

    Applicable when *gather_subset* is ``deployment``, ``service_template``.

    For ``deployment`` specify to use full templates including resources in response.


  include_attachments (optional, bool, True)
    Include attachments.

    Applicable when *gather_subset* is ``service_template``.


  include_related (optional, bool, False)
    Include related entities.

    Applicable when *gather_subset* is ``firmware_repository``.


  include_bundles (optional, bool, False)
    Include software bundle entities.

    Applicable when *gather_subset* is ``firmware_repository``.


  include_components (optional, bool, False)
    Include software component entities.

    Applicable when *gather_subset* is ``firmware_repository``.


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
   - The supported filter keys for the *gather_subset* can be referred from PowerFlex Manager API documentation in https://developer.dell.com.
   - The *filter*, *sort*, *limit* and *offset* options will be ignored when more than one *gather_subset* is specified along with ``service_template``, ``managed_device``, ``deployment`` or ``firmware_repository``.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get detailed list of PowerFlex entities
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
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
          - fault_set

    - name: Get a subset list of PowerFlex volumes
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - vol
        filters:
          - filter_key: "name"
            filter_operator: "equal"
            filter_value: "ansible_test"

    - name: Get deployment and resource provisioning info
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - managed_device
          - deployment
          - service_template

    - name: Get deployment with filter, sort, pagination
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - deployment
        filters:
          - filter_key: "name"
            filter_operator: "contains"
            filter_value: "partial"
        sort: name
        limit: 10
        offset: 10
        include_devices: true
        include_template: true

    - name: Get the list of firmware repository.
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - firmware_repository

    - name: Get the list of firmware repository
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - firmware_repository
        include_related: true
        include_bundles: true
        include_components: true

    - name: Get the list of firmware repository with filter
      dellemc.powerflex.info:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - firmware_repository
        filters:
          - filter_key: "createdBy"
            filter_operator: "equal"
            filter_value: "admin"
        sort: createdDate
        limit: 10
        include_related: true
        include_bundles: true
        include_components: true
      register: result_repository_out

    - name: Get the list of available firmware repository
      ansible.builtin.debug:
        msg: "{{ result_repository_out.FirmwareRepository | selectattr('state', 'equalto', 'available') }}"

    - name: Get the list of software components in the firmware repository
      ansible.builtin.debug:
        msg: "{{ result_repository_out.FirmwareRepository |
            selectattr('id', 'equalto', '8aaa80788b7') | map(attribute='softwareComponents') | flatten }}"

    - name: Get the list of software bundles in the firmware repository
      ansible.builtin.debug:
        msg: "{{ result_repository_out.FirmwareRepository |
            selectattr('id', 'equalto', '8aaa80788b7') | map(attribute='softwareBundles') | flatten }}"



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



Fault_Sets (always, list, [{'protectionDomainId': 'da721a8300000000', 'protectionDomainName': 'fault_set_1', 'name': 'at1zbs1t6cp2sds1d1fs1', 'SDS': [], 'id': 'eb44b70500000000', 'links': [{'rel': 'self', 'href': '/api/instances/FaultSet::eb44b70500000000'}, {'rel': '/api/FaultSet/relationship/Statistics', 'href': '/api/instances/FaultSet::eb44b70500000000/relationships/Statistics'}, {'rel': '/api/FaultSet/relationship/Sds', 'href': '/api/instances/FaultSet::eb44b70500000000/relationships/Sds'}, {'rel': '/api/parent/relationship/protectionDomainId', 'href': '/api/instances/ProtectionDomain::da721a8300000000'}]}, {'protectionDomainId': 'da721a8300000000', 'protectionDomainName': 'fault_set_2', 'name': 'at1zbs1t6cp2sds1d1fs3', 'SDS': [], 'id': 'eb44b70700000002', 'links': [{'rel': 'self', 'href': '/api/instances/FaultSet::eb44b70700000002'}, {'rel': '/api/FaultSet/relationship/Statistics', 'href': '/api/instances/FaultSet::eb44b70700000002/relationships/Statistics'}, {'rel': '/api/FaultSet/relationship/Sds', 'href': '/api/instances/FaultSet::eb44b70700000002/relationships/Sds'}, {'rel': '/api/parent/relationship/protectionDomainId', 'href': '/api/instances/ProtectionDomain::da721a8300000000'}]}])
  Details of fault sets.


  protectionDomainId (, str, )
    The ID of the protection domain.


  name (, str, )
    device name.


  id (, str, )
    device id.



ManagedDevices (when I(gather_subset) is I(managed_device), list, [{'refId': 'softwareOnlyServer-10.1.1.1', 'refType': None, 'ipAddress': '10.1.1.1', 'currentIpAddress': '10.1.1.1', 'serviceTag': 'VMware-42 15 a5 f9 65 e6 63 0e-36 79 59 73 7b 3a 68 cd-SW', 'model': 'VMware Virtual Platform', 'deviceType': 'SoftwareOnlyServer', 'discoverDeviceType': 'SOFTWAREONLYSERVER_CENTOS', 'displayName': 'vpi1011-c1n1', 'managedState': 'UNMANAGED', 'state': 'READY', 'inUse': False, 'serviceReferences': [], 'statusMessage': None, 'firmwareName': 'Default Catalog - PowerFlex 4.5.0.0', 'customFirmware': False, 'needsAttention': False, 'manufacturer': 'VMware, Inc.', 'systemId': None, 'health': 'RED', 'healthMessage': 'Inventory run failed.', 'operatingSystem': 'N/A', 'numberOfCPUs': 0, 'cpuType': None, 'nics': 0, 'memoryInGB': 0, 'infraTemplateDate': None, 'infraTemplateId': None, 'serverTemplateDate': None, 'serverTemplateId': None, 'inventoryDate': None, 'complianceCheckDate': '2024-02-05T18:31:31.213+00:00', 'discoveredDate': '2024-02-05T18:31:30.992+00:00', 'deviceGroupList': {'paging': None, 'deviceGroup': [{'link': None, 'groupSeqId': -1, 'groupName': 'Global', 'groupDescription': None, 'createdDate': None, 'createdBy': 'admin', 'updatedDate': None, 'updatedBy': None, 'managedDeviceList': None, 'groupUserList': None}]}, 'detailLink': {'title': 'softwareOnlyServer-10.1.1.1', 'href': '/AsmManager/ManagedDevice/softwareOnlyServer-10.1.1.1', 'rel': 'describedby', 'type': None}, 'credId': 'bc97cefb-5eb4-4c20-8e39-d1a2b809c9f5', 'compliance': 'NONCOMPLIANT', 'failuresCount': 0, 'chassisId': None, 'parsedFacts': None, 'config': None, 'hostname': 'vpi1011-c1n1', 'osIpAddress': None, 'osAdminCredential': None, 'osImageType': None, 'lastJobs': None, 'puppetCertName': 'red_hat-10.1.1.1', 'svmAdminCredential': None, 'svmName': None, 'svmIpAddress': None, 'svmImageType': None, 'flexosMaintMode': 0, 'esxiMaintMode': 0, 'vmList': []}])
  Details of all devices from inventory.


  deviceType (, str, )
    Device Type.


  serviceTag (, str, )
    Service Tag.


  serverTemplateId (, str, )
    The ID of the server template.


  state (, str, )
    The state of the device.


  managedState (, str, )
    The managed state of the device.


  compliance (, str, )
    The compliance state of the device.


  systemId (, str, )
    The system ID.



Deployments (when I(gather_subset) is I(deployment), list, [{'id': '8aaa80658cd602e0018cda8b257f78ce', 'deploymentName': 'Test-Update - K', 'deploymentDescription': 'Test-Update - K', 'deploymentValid': None, 'retry': False, 'teardown': False, 'teardownAfterCancel': False, 'removeService': False, 'createdDate': '2024-01-05T16:53:21.407+00:00', 'createdBy': 'admin', 'updatedDate': '2024-02-11T17:00:05.657+00:00', 'updatedBy': 'system', 'deploymentScheduledDate': None, 'deploymentStartedDate': '2024-01-05T16:53:22.886+00:00', 'deploymentFinishedDate': None, 'serviceTemplate': {'id': '8aaa80658cd602e0018cda8b257f78ce', 'templateName': 'block-only (8aaa80658cd602e0018cda8b257f78ce)', 'templateDescription': 'Storage - Software Only deployment', 'templateType': 'VxRack FLEX', 'templateVersion': '4.5.0.0', 'templateValid': {'valid': True, 'messages': []}, 'originalTemplateId': 'c44cb500-020f-4562-9456-42ec1eb5f9b2', 'templateLocked': False, 'draft': False, 'inConfiguration': False, 'createdDate': '2024-01-05T16:53:22.083+00:00', 'createdBy': None, 'updatedDate': '2024-02-09T06:00:09.602+00:00', 'lastDeployedDate': None, 'updatedBy': None, 'components': [{'id': '6def7edd-bae2-4420-93bf-9ceb051bbb65', 'componentID': 'component-scaleio-gateway-1', 'identifier': None, 'componentValid': {'valid': True, 'messages': []}, 'puppetCertName': 'scaleio-block-legacy-gateway', 'osPuppetCertName': None, 'name': 'block-legacy-gateway', 'type': 'SCALEIO', 'subType': 'STORAGEONLY', 'teardown': False, 'helpText': None, 'managementIpAddress': None, 'configFile': None, 'serialNumber': None, 'asmGUID': 'scaleio-block-legacy-gateway', 'relatedComponents': {'625b0e17-9b91-4bc0-864c-d0111d42d8d0': 'Node (Software Only)', '961a59eb-80c3-4a3a-84b7-2101e9831527': 'Node (Software Only)-2', 'bca710a5-7cdf-481e-b729-0b53e02873ee': 'Node (Software Only)-3'}, 'resources': [], 'refId': None, 'cloned': False, 'clonedFromId': None, 'manageFirmware': False, 'brownfield': False, 'instances': 1, 'clonedFromAsmGuid': None, 'ip': None}], 'category': 'block-only', 'allUsersAllowed': True, 'assignedUsers': [], 'manageFirmware': True, 'useDefaultCatalog': False, 'firmwareRepository': None, 'licenseRepository': None, 'configuration': None, 'serverCount': 3, 'storageCount': 1, 'clusterCount': 1, 'serviceCount': 0, 'switchCount': 0, 'vmCount': 0, 'sdnasCount': 0, 'brownfieldTemplateType': 'NONE', 'networks': [{'id': '8aaa80648cd5fb9b018cda46e4e50000', 'name': 'mgmt', 'description': '', 'type': 'SCALEIO_MANAGEMENT', 'vlanId': 850, 'static': True, 'staticNetworkConfiguration': {'gateway': '10.1.1.1', 'subnet': '1.1.1.0', 'primaryDns': '10.1.1.1', 'secondaryDns': '10.1.1.1', 'dnsSuffix': None, 'ipRange': [{'id': '8aaa80648cd5fb9b018cda46e5080001', 'startingIp': '10.1.1.1', 'endingIp': '10.1.1.1', 'role': None}], 'ipAddress': None, 'staticRoute': None}, 'destinationIpAddress': '10.1.1.1'}], 'blockServiceOperationsMap': {'scaleio-block-legacy-gateway': {'blockServiceOperationsMap': {}}}}, 'scheduleDate': None, 'status': 'complete', 'compliant': True, 'deploymentDevice': [{'refId': 'scaleio-block-legacy-gateway', 'refType': None, 'logDump': None, 'status': None, 'statusEndTime': None, 'statusStartTime': None, 'deviceHealth': 'GREEN', 'healthMessage': 'OK', 'compliantState': 'COMPLIANT', 'brownfieldStatus': 'NOT_APPLICABLE', 'deviceType': 'scaleio', 'deviceGroupName': None, 'ipAddress': 'block-legacy-gateway', 'currentIpAddress': '10.1.1.1', 'serviceTag': 'block-legacy-gateway', 'componentId': None, 'statusMessage': None, 'model': 'PowerFlex Gateway', 'cloudLink': False, 'dasCache': False, 'deviceState': 'READY', 'puppetCertName': 'scaleio-block-legacy-gateway', 'brownfield': False}], 'vms': None, 'updateServerFirmware': True, 'useDefaultCatalog': False, 'firmwareRepository': {'id': '8aaa80658cd602e0018cd996a1c91bdc', 'name': 'Intelligent Catalog 45.373.00', 'sourceLocation': None, 'sourceType': None, 'diskLocation': None, 'filename': None, 'md5Hash': None, 'username': None, 'password': None, 'downloadStatus': None, 'createdDate': None, 'createdBy': None, 'updatedDate': None, 'updatedBy': None, 'defaultCatalog': False, 'embedded': False, 'state': None, 'softwareComponents': [], 'softwareBundles': [], 'deployments': [], 'bundleCount': 0, 'componentCount': 0, 'userBundleCount': 0, 'minimal': False, 'downloadProgress': 0, 'extractProgress': 0, 'fileSizeInGigabytes': None, 'signedKeySourceLocation': None, 'signature': None, 'custom': False, 'needsAttention': False, 'jobId': None, 'rcmapproved': False}, 'firmwareRepositoryId': '8aaa80658cd602e0018cd996a1c91bdc', 'licenseRepository': None, 'licenseRepositoryId': None, 'individualTeardown': False, 'deploymentHealthStatusType': 'green', 'assignedUsers': [], 'allUsersAllowed': True, 'owner': 'admin', 'noOp': False, 'firmwareInit': False, 'disruptiveFirmware': False, 'preconfigureSVM': False, 'preconfigureSVMAndUpdate': False, 'servicesDeployed': 'NONE', 'precalculatedDeviceHealth': None, 'lifecycleModeReasons': [], 'jobDetails': None, 'numberOfDeployments': 0, 'operationType': 'NONE', 'operationStatus': None, 'operationData': None, 'deploymentValidationResponse': None, 'currentStepCount': None, 'totalNumOfSteps': None, 'currentStepMessage': None, 'customImage': 'os_sles', 'originalDeploymentId': None, 'currentBatchCount': None, 'totalBatchCount': None, 'templateValid': True, 'lifecycleMode': False, 'vds': False, 'scaleUp': False, 'brownfield': False, 'configurationChange': False}])
  Details of all deployments.


  id (, str, )
    Deployment ID.


  deploymentName (, str, )
    Deployment name.


  status (, str, )
    The status of deployment.


  firmwareRepository (, dict, )
    The firmware repository.


    signature (, str, )
      The signature details.


    downloadStatus (, str, )
      The download status.


    rcmapproved (, bool, )
      If RCM approved.




ServiceTemplates (when I(gather_subset) is I(service_template), list, [{'id': '2434144f-7795-4245-a04b-6fcb771697d7', 'templateName': 'Storage- 100Gb', 'templateDescription': 'Storage Only 4 Node deployment with 100Gb networking', 'templateType': 'VxRack FLEX', 'templateVersion': '4.5-213', 'templateValid': {'valid': True, 'messages': []}, 'originalTemplateId': 'ff80808177f880fc0177f883bf1e0027', 'templateLocked': True, 'draft': False, 'inConfiguration': False, 'createdDate': '2024-01-04T19:47:23.534+00:00', 'createdBy': 'system', 'updatedDate': None, 'lastDeployedDate': None, 'updatedBy': None, 'components': [{'id': '43dec024-85a9-4901-9e8e-fa0d3c417f7b', 'componentID': 'component-scaleio-gateway-1', 'identifier': None, 'componentValid': {'valid': True, 'messages': []}, 'puppetCertName': None, 'osPuppetCertName': None, 'name': 'PowerFlex Cluster', 'type': 'SCALEIO', 'subType': 'STORAGEONLY', 'teardown': False, 'helpText': None, 'managementIpAddress': None, 'configFile': None, 'serialNumber': None, 'asmGUID': None, 'relatedComponents': {'c5c46733-012c-4dca-af9b-af46d73d045a': 'Storage Only Node'}, 'resources': [], 'refId': None, 'cloned': False, 'clonedFromId': None, 'manageFirmware': False, 'brownfield': False, 'instances': 1, 'clonedFromAsmGuid': None, 'ip': None}], 'category': 'Sample Templates', 'allUsersAllowed': False, 'assignedUsers': [], 'manageFirmware': True, 'useDefaultCatalog': True, 'firmwareRepository': None, 'licenseRepository': None, 'configuration': None, 'serverCount': 4, 'storageCount': 0, 'clusterCount': 1, 'serviceCount': 0, 'switchCount': 0, 'vmCount': 0, 'sdnasCount': 0, 'brownfieldTemplateType': 'NONE', 'networks': [{'id': 'ff80808177f8823b0177f8bb82d80005', 'name': 'flex-data2', 'description': '', 'type': 'SCALEIO_DATA', 'vlanId': 105, 'static': True, 'staticNetworkConfiguration': {'gateway': None, 'subnet': '1.1.1.0', 'primaryDns': None, 'secondaryDns': None, 'dnsSuffix': None, 'ipRange': None, 'ipAddress': None, 'staticRoute': None}, 'destinationIpAddress': '1.1.1.0'}], 'blockServiceOperationsMap': {}}])
  Details of all service templates.


  templateName (, str, )
    Template name.


  templateDescription (, str, )
    Template description.


  templateType (, str, )
    Template type.


  templateVersion (, str, )
    Template version.


  category (, str, )
    The template category.


  serverCount (, int, )
    Server count.



FirmwareRepository (when I(gather_subset) is C(firmware_repository), list, [{'id': '8aaa03a78de4b2a5018de662818d000b', 'name': 'https://192.168.0.1/artifactory/path/pfxmlogs-bvt-pfmp-swo-upgrade-402-to-451-56.tar.gz', 'sourceLocation': 'https://192.168.0.2/artifactory/path/pfxmlogs-bvt-pfmp-swo-upgrade-402-to-451-56.tar.gz', 'sourceType': None, 'diskLocation': '', 'filename': '', 'md5Hash': None, 'username': '', 'password': '', 'downloadStatus': 'error', 'createdDate': '2024-02-26T17:07:11.884+00:00', 'createdBy': 'admin', 'updatedDate': '2024-03-01T06:21:10.917+00:00', 'updatedBy': 'system', 'defaultCatalog': False, 'embedded': False, 'state': 'errors', 'softwareComponents': [], 'softwareBundles': [], 'deployments': [], 'bundleCount': 0, 'componentCount': 0, 'userBundleCount': 0, 'minimal': True, 'downloadProgress': 100, 'extractProgress': 0, 'fileSizeInGigabytes': 0.0, 'signedKeySourceLocation': None, 'signature': 'Unknown', 'custom': False, 'needsAttention': False, 'jobId': 'Job-10d75a23-d801-4fdb-a2d0-7f6389ab75cf', 'rcmapproved': False}])
  Details of all firmware repository.


  id (, str, )
    ID of the firmware repository.


  name (, str, )
    Name of the firmware repository.


  sourceLocation (, str, )
    Source location of the firmware repository.


  state (, str, )
    State of the firmware repository.


  softwareComponents (, list, )
    Software components of the firmware repository.


  softwareBundles (, list, )
    Software bundles of the firmware repository.


  deployments (, list, )
    Deployments of the firmware repository.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
- Jennifer John (@Jennifer-John) <ansible.team@dell.com>
- Felix Stephen (@felixs88) <ansible.team@dell.com>

