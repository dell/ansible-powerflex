.. _info_v2_module:


info_v2 -- Gathering information about Dell PowerFlex
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gathering information about Dell PowerFlex storage system includes getting the api details, list of devices, NVMe host, protection domains, SDCs, SDT, snapshot policies, storage pools, volumes.

Gathering information about Dell PowerFlex Manager includes getting the list of deployments, firmware repository, managed devices, service templates.

Support only for Powerflex 5.0 versions and above.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

  gather_subset (optional, list, None)
    List of string variables to specify the PowerFlex storage system entities for which information is required.

    Devices - :literal:`device`.

    Deployments - :literal:`deployment`.

    FirmwareRepository - :literal:`firmware\_repository`.

    Managed devices - :literal:`managed\_device`.

    NVMe host - :literal:`nvme\_host`

    NVMe Storage Data Target - :literal:`sdt`.

    Protection domains - :literal:`protection\_domain`.

    SDCs - :literal:`sdc`.

    Service templates - :literal:`service\_template`.

    Snapshot policies - :literal:`snapshot\_policy`.

    Storage pools - :literal:`storage\_pool`.

    Volumes - :literal:`vol`.


  filters (optional, list, None)
    List of filters to support filtered output for storage entities.

    Each filter is a dictionary with keys :emphasis:`filter\_key`\ , :emphasis:`filter\_operator`\ , :emphasis:`filter\_value`.

    Supports passing of multiple filters.


    filter_key (True, str, None)
      Name identifier of the filter.


    filter_operator (True, str, None)
      Operation to be performed on filter key.

      Choice :literal:`contains` is supported for :emphasis:`gather\_subset` keys :literal:`service\_template`\ , :literal:`managed\_device`\ , :literal:`deployment`\ , :literal:`firmware\_repository`.


    filter_value (True, str, None)
      Value of the filter key.



  limit (optional, int, 50)
    Page limit.

    Supported for :emphasis:`gather\_subset` keys :literal:`service\_template`\ , :literal:`managed\_device`\ , :literal:`deployment`\ , :literal:`firmware\_repository`.


  offset (optional, int, 0)
    Pagination offset.

    Supported for :emphasis:`gather\_subset` keys :literal:`service\_template`\ , :literal:`managed\_device`\ , :literal:`deployment`\ , :literal:`firmware\_repository`.


  sort (optional, str, None)
    Sort the returned components based on specified field.

    Supported for :emphasis:`gather\_subset` keys :literal:`service\_template`\ , :literal:`managed\_device`\ , :literal:`deployment`\ , :literal:`firmware\_repository`.

    The supported sort keys for the :emphasis:`gather\_subset` can be referred from PowerFlex Manager API documentation in \ `https://developer.dell.com <https://developer.dell.com>`__.


  include_devices (optional, bool, True)
    Include devices in response.

    Applicable when :emphasis:`gather\_subset` is :literal:`deployment`.


  include_template (optional, bool, True)
    Include service templates in response.

    Applicable when :emphasis:`gather\_subset` is :literal:`deployment`.


  full (optional, bool, False)
    Specify if response is full or brief.

    Applicable when :emphasis:`gather\_subset` is :literal:`deployment`\ , :literal:`service\_template`.

    For :literal:`deployment` specify to use full templates including resources in response.


  include_attachments (optional, bool, True)
    Include attachments.

    Applicable when :emphasis:`gather\_subset` is :literal:`service\_template`.


  include_bundles (optional, bool, False)
    Include software bundle entities.

    Applicable when :emphasis:`gather\_subset` is :literal:`firmware\_repository`.


  hostname (True, str, None)
    IP or FQDN of the PowerFlex host.


  username (True, str, None)
    The username of the PowerFlex host.


  password (True, str, None)
    The password of the PowerFlex host.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    :literal:`true` - Indicates that the SSL certificate should be verified.

    :literal:`false` - Indicates that the SSL certificate should not be verified.


  port (optional, int, 443)
    Port number through which communication happens with PowerFlex host.


  timeout (False, int, 120)
    Time after which connection will get terminated.

    It is to be mentioned in seconds.





Notes
-----

.. note::
   - The supported filter keys for the :emphasis:`gather\_subset` can be referred from PowerFlex Manager API documentation in \ `https://developer.dell.com <https://developer.dell.com>`__.
   - The :emphasis:`filter`\ , :emphasis:`sort`\ , :emphasis:`limit` and :emphasis:`offset` options will be ignored when more than one :emphasis:`gather\_subset` is specified along with :literal:`deployment`\ , :literal:`firmware\_repository`\ , :literal:`managed\_device` or :literal:`service\_template`.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get detailed list of PowerFlex entities
      dellemc.powerflex.info_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - vol
          - storage_pool
          - protection_domain
          - sdc
          - snapshot_policy
          - device
          - nvme_host
          - sdt

    - name: Get specific volume details
      dellemc.powerflex.info_v2:
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

    - name: Get specific NVMe hosts details
      dellemc.powerflex.info_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - nvme_host
        filters:
          - filter_key: "name"
            filter_operator: "equal"
            filter_value: "ansible_test"

    - name: Get deployment and resource provisioning info
      dellemc.powerflex.info_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - managed_device
          - deployment
          - service_template

    - name: Get deployment with filter, sort, pagination
      dellemc.powerflex.info_v2:
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
      dellemc.powerflex.info_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - firmware_repository

    - name: Get the list of firmware repository
      dellemc.powerflex.info_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        gather_subset:
          - firmware_repository
        include_bundles: true

    - name: Get the list of firmware repository with filter
      dellemc.powerflex.info_v2:
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
        include_bundles: true
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


Array_Details (always, dict, {'addressSpaceUsage': 'Normal', 'authenticationMethod': 'Mno', 'capacityAlertCriticalThresholdPercent': 90, 'capacityAlertHighThresholdPercent': 80, 'capacityTimeLeftInDays': '78', 'cliPasswordAllowed': True, 'daysInstalled': 12, 'defragmentationEnabled': True, 'enterpriseFeaturesEnabled': True, 'id': '815945c41cd8460f', 'installId': '0076d6af044b5481', 'isInitialLicense': True, 'lastUpgradeTime': 0, 'managementClientSecureCommunicationEnabled': True, 'maxCapacityInGb': 'Unlimited', 'mdmCluster': {'clusterMode': 'ThreeNodes', 'clusterState': 'ClusteredNormal', 'goodNodesNum': 3, 'goodReplicasNum': 2, 'id': '-9126186461289757169', 'master': {'id': '2d5f17673e35a101', 'ips': ['10.225.106.68'], 'managementIPs': ['10.225.106.68'], 'opensslVersion': 'OpenSSL 3.1.4 24 Oct 2023', 'port': 9011, 'role': 'Manager', 'status': 'Normal', 'versionInfo': 'R5_0.0.0', 'virtualInterfaces': ['ens160']}, 'slaves': [{'id': '5c613b076fb30100', 'ips': ['10.225.106.67'], 'managementIPs': ['10.225.106.67'], 'opensslVersion': 'OpenSSL 3.1.4 24 Oct 2023', 'port': 9011, 'role': 'Manager', 'status': 'Normal', 'versionInfo': 'R5_0.0.0', 'virtualInterfaces': ['ens160']}], 'standbyMDMs': [{'id': '1ef63c213b382503', 'ips': ['10.225.106.48'], 'managementIPs': ['10.225.106.48'], 'opensslVersion': 'N/A', 'port': 9011, 'role': 'Manager', 'virtualInterfaces': []}], 'tieBreakers': [{'id': '6b5ae1c7248e0c02', 'ips': ['10.225.106.69'], 'managementIPs': ['10.225.106.69'], 'opensslVersion': 'N/A', 'port': 9011, 'role': 'TieBreaker', 'status': 'Normal', 'versionInfo': 'R5_0.0.0'}]}, 'mdmExternalPort': 7611, 'mdmManagementPort': 8611, 'mdmSecurityPolicy': 'Authentication', 'showGuid': True, 'swid': '', 'systemVersionName': 'DellEMC PowerFlex Version: R5_0.0.937', 'tlsVersion': 'TLSv1.2', 'upgradeState': 'NoUpgrade'})
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


  maxCapacityInGb (, str, )
    Maximum capacity in GB.


  mdmCluster (, dict, )
    MDM cluster details.


    clusterMode (, str, )
      Cluster mode.


    clusterState (, str, )
      Cluster state.


    goodNodesNum (, int, )
      Number of good nodes.


    goodReplicasNum (, int, )
      Number of good replicas.


    id (, str, )
      Cluster ID.


    master (, dict, )
      Master MDM node details.


      id (, str, )
        Node ID.


      ips (, list, )
        List of IP addresses.


      managementIPs (, list, )
        List of management IP addresses.


      opensslVersion (, str, )
        OpenSSL version.


      port (, int, )
        Communication port.


      role (, str, )
        Node role.


      status (, str, )
        Node status.


      versionInfo (, str, )
        Version information.


      virtualInterfaces (, list, )
        List of virtual interfaces.



    slaves (, list, )
      Slave MDM nodes.


      id (, str, )
        Node ID.


      ips (, list, )
        List of IP addresses.


      managementIPs (, list, )
        List of management IP addresses.


      opensslVersion (, str, )
        OpenSSL version.


      port (, int, )
        Communication port.


      role (, str, )
        Node role.


      status (, str, )
        Node status.


      versionInfo (, str, )
        Version information.


      virtualInterfaces (, list, )
        List of virtual interfaces.



    standbyMDMs (, list, )
      Standby MDM nodes.


      id (, str, )
        Node ID.


      ips (, list, )
        List of IP addresses.


      managementIPs (, list, )
        List of management IP addresses.


      opensslVersion (, str, )
        OpenSSL version.


      port (, int, )
        Communication port.


      role (, str, )
        Node role.


      virtualInterfaces (, list, )
        List of virtual interfaces.



    tieBreakers (, list, )
      Tie-breaker nodes.


      id (, str, )
        Node ID.


      ips (, list, )
        List of IP addresses.


      managementIPs (, list, )
        List of management IP addresses.


      opensslVersion (, str, )
        OpenSSL version.


      port (, int, )
        Communication port.


      role (, str, )
        Node role.


      status (, str, )
        Node status.


      versionInfo (, str, )
        Version information.




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



API_Version (always, str, 5.0)
  API version of PowerFlex API Gateway.


Protection_Domains (always, list, [{'bandwidthLimitBgDevScanner': 15, 'bandwidthLimitDoublyImpactedRebuild': 400, 'bandwidthLimitNodeNetwork': 30, 'bandwidthLimitOther': 10, 'bandwidthLimitOverallIos': 500, 'bandwidthLimitRebalance': 50, 'bandwidthLimitSinglyImpactedRebuild': 500, 'fglDefaultMetadataCacheSize': 0, 'fglDefaultNumConcurrentWrites': 0, 'fglMetadataCacheEnabled': False, 'genType': 'EC', 'id': 'e597f3dd00000000', 'links': [{'href': '/api/instances/ProtectionDomain::e597f3dd00000000', 'rel': 'self'}], 'mdmSdsNetworkDisconnectionsCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'name': 'PD_EC', 'overallConcurrentIoLimit': 5, 'overallIoNetworkThrottlingEnabled': False, 'overallIoNetworkThrottlingInKbps': None, 'protectedMaintenanceModeNetworkThrottlingEnabled': False, 'protectedMaintenanceModeNetworkThrottlingInKbps': None, 'protectionDomainState': 'Active', 'rebalanceEnabled': True, 'rebalanceNetworkThrottlingEnabled': False, 'rebalanceNetworkThrottlingInKbps': None, 'rebuildEnabled': True, 'rebuildNetworkThrottlingEnabled': False, 'rebuildNetworkThrottlingInKbps': None, 'rfcacheAccpId': None, 'rfcacheEnabled': True, 'rfcacheMaxIoSizeKb': 0, 'rfcacheOpertionalMode': 'WriteMiss', 'rfcachePageSizeKb': 0, 'rplCapAlertLevel': 'invalid', 'sdrSdsConnectivityInfo': {'clientServerConnStatus': 'CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED', 'disconnectedClientId': None, 'disconnectedClientName': None, 'disconnectedServerId': None, 'disconnectedServerIp': None, 'disconnectedServerName': None}, 'sdsConfigurationFailureCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'sdsDecoupledCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'sdsReceiveBufferAllocationFailuresCounterParameters': {'longWindow': {'threshold': 2000000, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 200000, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 20000, 'windowSizeInSec': 60}}, 'sdsSdsNetworkDisconnectionsCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'sdtSdsConnectivityInfo': {'clientServerConnStatus': 'CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED', 'disconnectedClientId': None, 'disconnectedClientName': None, 'disconnectedServerId': None, 'disconnectedServerIp': None, 'disconnectedServerName': None}, 'systemId': '815945c41cd8460f', 'vtreeMigrationNetworkThrottlingEnabled': False, 'vtreeMigrationNetworkThrottlingInKbps': None}])
  Details of all protection domains.


  id (, str, )
    protection domain id.


  name (, str, )
    protection domain name.


  bandwidthLimitBgDevScanner (, int, )
    Bandwidth limit for background device scanner.


  bandwidthLimitDoublyImpactedRebuild (, int, )
    Bandwidth limit for doubly impacted rebuild operations.


  bandwidthLimitNodeNetwork (, int, )
    Bandwidth limit for node network.


  bandwidthLimitOther (, int, )
    Bandwidth limit for other I/O operations.


  bandwidthLimitOverallIos (, int, )
    Overall bandwidth limit for all I/O operations.


  bandwidthLimitRebalance (, int, )
    Bandwidth limit for rebalance operations.


  bandwidthLimitSinglyImpactedRebuild (, int, )
    Bandwidth limit for singly impacted rebuild operations.


  fglDefaultMetadataCacheSize (, int, )
    Default metadata cache size for fine-grained logging.


  fglDefaultNumConcurrentWrites (, int, )
    Default number of concurrent writes for fine-grained logging.


  fglMetadataCacheEnabled (, bool, )
    Whether metadata cache is enabled for fine-grained logging.


  genType (, str, )
    Generation type of the protection domain (e.g., EC for Erasure Coding).


  links (, list, )
    Hypermedia links related to the protection domain.


    href (, str, )
      The URI reference.


    rel (, str, )
      The relation type of the link.



  mdmSdsNetworkDisconnectionsCounterParameters (, dict, )
    MDM-SDS network disconnection counter thresholds.


    longWindow (, dict, )
      Long time window threshold settings.


      threshold (, int, )
        Disconnection threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    mediumWindow (, dict, )
      Medium time window threshold settings.


      threshold (, int, )
        Disconnection threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    shortWindow (, dict, )
      Short time window threshold settings.


      threshold (, int, )
        Disconnection threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.




  overallConcurrentIoLimit (, int, )
    Overall concurrent I/O limit for the protection domain.


  overallIoNetworkThrottlingEnabled (, bool, )
    Whether overall I/O network throttling is enabled.


  protectedMaintenanceModeNetworkThrottlingEnabled (, bool, )
    Whether network throttling is enabled in protected maintenance mode.


  protectionDomainState (, str, )
    Current state of the protection domain (e.g., Active).


  rebalanceEnabled (, bool, )
    Whether rebalance operations are enabled.


  rebalanceNetworkThrottlingEnabled (, bool, )
    Whether network throttling is enabled for rebalance operations.


  rebuildEnabled (, bool, )
    Whether rebuild operations are enabled.


  rebuildNetworkThrottlingEnabled (, bool, )
    Whether network throttling is enabled for rebuild operations.


  rfcacheEnabled (, bool, )
    Whether RF-Cache is enabled.


  rfcacheMaxIoSizeKb (, int, )
    Maximum I/O size in KB for RF-Cache.


  rfcacheOpertionalMode (, str, )
    Operational mode of RF-Cache (e.g., WriteMiss).


  rfcachePageSizeKb (, int, )
    Page size in KB used by RF-Cache.


  rplCapAlertLevel (, str, )
    Replication capacity alert level.


  sdrSdsConnectivityInfo (, dict, )
    Connectivity information between SDR client and SDS server.


    clientServerConnStatus (, str, )
      Status of client-server connection.


    disconnectedClientId (, str, )
      ID of disconnected client (null if connected).


    disconnectedClientName (, str, )
      Name of disconnected client (null if connected).


    disconnectedServerId (, str, )
      ID of disconnected server (null if connected).


    disconnectedServerIp (, str, )
      IP of disconnected server (null if connected).


    disconnectedServerName (, str, )
      Name of disconnected server (null if connected).



  sdsConfigurationFailureCounterParameters (, dict, )
    SDS configuration failure counter thresholds.


    longWindow (, dict, )
      Long time window threshold settings.


      threshold (, int, )
        Failure threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    mediumWindow (, dict, )
      Medium time window threshold settings.


      threshold (, int, )
        Failure threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    shortWindow (, dict, )
      Short time window threshold settings.


      threshold (, int, )
        Failure threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.




  sdsDecoupledCounterParameters (, dict, )
    SDS decoupled state counter thresholds.


    longWindow (, dict, )
      Long time window threshold settings.


      threshold (, int, )
        Decoupled threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    mediumWindow (, dict, )
      Medium time window threshold settings.


      threshold (, int, )
        Decoupled threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    shortWindow (, dict, )
      Short time window threshold settings.


      threshold (, int, )
        Decoupled threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.




  sdsReceiveBufferAllocationFailuresCounterParameters (, dict, )
    SDS receive buffer allocation failure counter thresholds.


    longWindow (, dict, )
      Long time window threshold settings.


      threshold (, int, )
        Buffer allocation failure threshold.


      windowSizeInSec (, int, )
        Time window size in seconds.



    mediumWindow (, dict, )
      Medium time window threshold settings.


      threshold (, int, )
        Buffer allocation failure threshold.


      windowSizeInSec (, int, )
        Time window size in seconds.



    shortWindow (, dict, )
      Short time window threshold settings.


      threshold (, int, )
        Buffer allocation failure threshold.


      windowSizeInSec (, int, )
        Time window size in seconds.




  sdsSdsNetworkDisconnectionsCounterParameters (, dict, )
    SDS-SDS network disconnection counter thresholds.


    longWindow (, dict, )
      Long time window threshold settings.


      threshold (, int, )
        Disconnection threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    mediumWindow (, dict, )
      Medium time window threshold settings.


      threshold (, int, )
        Disconnection threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.



    shortWindow (, dict, )
      Short time window threshold settings.


      threshold (, int, )
        Disconnection threshold count.


      windowSizeInSec (, int, )
        Time window size in seconds.




  sdtSdsConnectivityInfo (, dict, )
    Connectivity information between SDT and SDS.


    clientServerConnStatus (, str, )
      Status of client-server connection.


    disconnectedClientId (, str, )
      ID of disconnected client (null if connected).


    disconnectedClientName (, str, )
      Name of disconnected client (null if connected).


    disconnectedServerId (, str, )
      ID of disconnected server (null if connected).


    disconnectedServerIp (, str, )
      IP of disconnected server (null if connected).


    disconnectedServerName (, str, )
      Name of disconnected server (null if connected).



  systemId (, str, )
    ID of the associated storage system.


  vtreeMigrationNetworkThrottlingEnabled (, bool, )
    Whether network throttling is enabled for vTree migration.



SDCs (always, list, [{'hostOsFullType': None, 'hostType': 'SdcHost', 'id': 'fdc050eb00000000', 'installedSoftwareVersionInfo': 'R5_0.0.0', 'kernelBuildNumber': None, 'kernelVersion': '6.4.0', 'links': [{'href': '/api/instances/Sdc::fdc050eb00000000', 'rel': 'self'}], 'maxNumPaths': None, 'maxNumSysPorts': None, 'mdmConnectionState': 'Connected', 'mdmIpAddressesCurrent': False, 'memoryAllocationFailure': None, 'name': 'SDC3', 'nqn': None, 'osType': 'Linux', 'peerMdmId': None, 'perfProfile': 'HighPerformance', 'sdcAgentActive': False, 'sdcApproved': True, 'sdcApprovedIps': None, 'sdcGuid': '89843E55-2B2A-42F7-A970-505467F81981', 'sdcIp': '10.225.106.69', 'sdcIps': ['10.225.106.69'], 'sdcType': 'AppSdc', 'sdrId': None, 'sdtId': None, 'socketAllocationFailure': None, 'softwareVersionInfo': 'R5_0.0.0', 'systemId': '815945c41cd8460f', 'versionInfo': 'R5_0.0.0'}])
  Details of storage data clients.


  id (, str, )
    storage data client id.


  name (, str, )
    storage data client name.


  hostOsFullType (, str, )
    Full operating system type of the storage data client.


  hostType (, str, )
    Host type of the storage data client.


  installedSoftwareVersionInfo (, str, )
    Installed software version information on the SDC.


  kernelBuildNumber (, str, )
    Kernel build number of the SDC's operating system.


  kernelVersion (, str, )
    Kernel version of the SDC's operating system.


  links (, list, )
    List of hypermedia links related to the SDC.


    href (, str, )
      The URI of the resource.


    rel (, str, )
      The relation type of the link.



  maxNumPaths (, str, )
    Maximum number of paths allowed for the SDC.


  maxNumSysPorts (, str, )
    Maximum number of system ports allowed for the SDC.


  mdmConnectionState (, str, )
    Current MDM (Management Domain Manager) connection state of the SDC.


  mdmIpAddressesCurrent (, bool, )
    Indicates whether the MDM IP addresses are current.


  memoryAllocationFailure (, str, )
    Indicates if there was a memory allocation failure on the SDC.


  nqn (, str, )
    NVMe Qualified Name used for NVMe-o-Fabrics connectivity.


  osType (, str, )
    Operating system type of the SDC.


  peerMdmId (, str, )
    Identifier of the peer MDM that the SDC is connected to.


  perfProfile (, str, )
    Performance profile configured for the SDC.


  sdcAgentActive (, bool, )
    Indicates whether the SDC agent is currently active.


  sdcApproved (, bool, )
    Indicates whether the SDC is approved to connect to the system.


  sdcApprovedIps (, list, )
    List of approved IP addresses for the SDC.


  sdcGuid (, str, )
    Globally unique identifier for the SDC.


  sdcIp (, str, )
    Primary IP address of the SDC.


  sdcIps (, list, )
    List of all IP addresses associated with the SDC.


  sdcType (, str, )
    Type of the SDC (e.g., AppSdc).


  sdrId (, str, )
    Identifier of the SDR (Storage Data Resilience) associated with the SDC.


  sdtId (, str, )
    Identifier of the SDT (Storage Data Tunnel) associated with the SDC.


  socketAllocationFailure (, str, )
    Indicates if there was a socket allocation failure on the SDC.


  softwareVersionInfo (, str, )
    Current software version running on the SDC.


  systemId (, str, )
    Identifier of the system to which the SDC belongs.


  versionInfo (, str, )
    Version information of the SDC software.



Snapshot_Policies (always, list, [{'autoSnapshotCreationCadenceInMin': 5, 'id': 'dc095e4d00000000', 'isLastAutoSnapshotDataTimeAccurate': None, 'lastAutoSnapshotCreationFailureReason': 'NR', 'lastAutoSnapshotDataTime': None, 'lastAutoSnapshotFailureInFirstLevel': False, 'links': [{'href': '/api/instances/SnapshotPolicy::dc095e4d00000000', 'rel': 'self'}], 'maxVTreeAutoSnapshots': 1, 'name': 'Sample_snap_policy_Ray', 'nextAutoSnapshotCreationTime': 0, 'numOfAutoSnapshots': 0, 'numOfCreationFailures': 0, 'numOfExpiredButLockedSnapshots': 0, 'numOfLockedSnapshots': 0, 'numOfRetainedSnapshotsPerLevel': [1], 'numOfSourceVolumes': 0, 'rcgId': None, 'rcgName': None, 'secureSnapshots': False, 'snapshotAccessMode': 'ReadOnly', 'snapshotPolicyState': 'Paused', 'systemId': '815945c41cd8460f', 'timeOfLastAutoSnapshot': 0, 'timeOfLastAutoSnapshotCreationFailure': 0}])
  Details of snapshot policies.


  id (, str, )
    snapshot policy id.


  name (, str, )
    snapshot policy name.


  autoSnapshotCreationCadenceInMin (, int, )
    Interval in minutes between automatic snapshot creations.


  isLastAutoSnapshotDataTimeAccurate (, str, )
    Indicates whether the timestamp of the last auto-snapshot data is accurate.


  lastAutoSnapshotCreationFailureReason (, str, )
    Reason code for the last automatic snapshot creation failure.


  lastAutoSnapshotDataTime (, str, )
    Timestamp of the last auto-snapshot data creation.


  lastAutoSnapshotFailureInFirstLevel (, bool, )
    Indicates if the last automatic snapshot failed at the first level.


  links (, list, )
    List of hypermedia links related to the snapshot policy.


    href (, str, )
      The URI of the linked resource.


    rel (, str, )
      The relation type of the link.



  maxVTreeAutoSnapshots (, int, )
    Maximum number of automatic snapshots allowed per VTree.


  nextAutoSnapshotCreationTime (, int, )
    Timestamp (in seconds) of the next scheduled automatic snapshot.


  numOfAutoSnapshots (, int, )
    Total number of automatic snapshots created under this policy.


  numOfCreationFailures (, int, )
    Number of failed automatic snapshot creation attempts.


  numOfExpiredButLockedSnapshots (, int, )
    Number of snapshots that have expired but are still locked.


  numOfLockedSnapshots (, int, )
    Total number of snapshots currently locked.


  numOfRetainedSnapshotsPerLevel (, list, )
    Number of snapshots retained per storage level.


  numOfSourceVolumes (, int, )
    Number of source volumes associated with this snapshot policy.


  rcgId (, str, )
    Identifier of the replication consistency group (RCG) associated with the policy.


  rcgName (, str, )
    Name of the replication consistency group (RCG) associated with the policy.


  secureSnapshots (, bool, )
    Indicates whether snapshots are secure (immutable).


  snapshotAccessMode (, str, )
    Access mode of the created snapshots (e.g., ReadOnly).


  snapshotPolicyState (, str, )
    Current state of the snapshot policy (e.g., Paused, Active).


  systemId (, str, )
    Identifier of the system to which the snapshot policy belongs.


  timeOfLastAutoSnapshot (, int, )
    Timestamp (in seconds) of the last successfully created automatic snapshot.


  timeOfLastAutoSnapshotCreationFailure (, int, )
    Timestamp (in seconds) of the last automatic snapshot creation failure.



Storage_Pools (always, list, [{'addressSpaceUsage': 'Normal', 'addressSpaceUsageType': 'TypeHardLimit', 'backgroundScannerBWLimitKBps': None, 'backgroundScannerMode': None, 'bgScannerCompareErrorAction': 'Invalid', 'bgScannerReadErrorAction': 'Invalid', 'capacityAlertCriticalThreshold': 90, 'capacityAlertHighThreshold': 80, 'capacityUsageState': 'Normal', 'capacityUsageType': 'NetCapacity', 'checksumEnabled': False, 'compressionMethod': 'Normal', 'dataLayout': 'ErasureCoding', 'deviceGroupId': 'd291d60100000000', 'externalAccelerationType': 'None', 'fglAccpId': None, 'fglExtraCapacity': None, 'fglMaxCompressionRatio': None, 'fglMetadataSizeXx100': None, 'fglNvdimmMetadataAmortizationX100': None, 'fglNvdimmWriteCacheSizeInMb': None, 'fglOverProvisioningFactor': None, 'fglPerfProfile': None, 'fglWriteAtomicitySize': None, 'fragmentationEnabled': False, 'genType': 'EC', 'id': '372743fc00000000', 'links': [{'href': '/api/instances/StoragePool::372743fc00000000', 'rel': 'self'}], 'statistics': [{'name': 'avg_host_read_latency', 'values': [0]}, {'name': 'raw_used', 'values': [13190918307840]}, {'name': 'logical_used', 'values': [0]}, {'name': 'host_write_bandwidth', 'values': [0]}, {'name': 'host_write_iops', 'values': [0]}, {'name': 'storage_fe_write_bandwidth', 'values': [0]}, {'name': 'storage_fe_write_iops', 'values': [0]}, {'name': 'avg_fe_write_io_size', 'values': [0]}, {'name': 'storage_fe_read_bandwidth', 'values': [0]}, {'name': 'storage_fe_read_iops', 'values': [0]}, {'name': 'avg_fe_read_io_size', 'values': [0]}, {'name': 'utilization_ratio', 'values': [0.008140671]}, {'name': 'compression_reducible_ratio', 'values': [0.0]}, {'name': 'host_read_bandwidth', 'values': [0]}, {'name': 'host_read_iops', 'values': [0]}, {'name': 'data_reduction_ratio', 'values': [0.0]}, {'name': 'thin_provisioning_ratio', 'values': ['0.8']}, {'name': 'avg_wrc_write_latency', 'values': [0]}, {'name': 'unreducible_data', 'values': [0]}, {'name': 'avg_wrc_read_latency', 'values': [0]}, {'name': 'storage_fe_read_latency', 'values': [0]}, {'name': 'over_provisioning_limit', 'values': [4611686017353646080]}, {'name': 'patterns_saving_ratio', 'values': [0.0]}, {'name': 'avg_host_write_latency', 'values': [0]}, {'name': 'storage_fe_write_latency', 'values': [0]}, {'name': 'logical_provisioned', 'values': [42949672960]}, {'name': 'efficiency_ratio', 'values': ['0.8']}, {'name': 'storage_fe_trim_latency', 'values': [0]}, {'name': 'physical_system', 'values': [53687091200]}, {'name': 'data_reduction_reducible_ratio', 'values': [0.0]}, {'name': 'storage_fe_trim_bandwidth', 'values': [0]}, {'name': 'storage_fe_trim_iops', 'values': [0]}, {'name': 'avg_fe_trim_io_size', 'values': [0]}, {'name': 'compression_ratio', 'values': [0.0]}, {'name': 'reducible_ratio', 'values': [1.0]}, {'name': 'physical_used', 'values': [0]}, {'name': 'snapshot_saving_ratio', 'values': [0.0]}, {'name': 'physical_free', 'values': [6541235191808]}, {'name': 'host_trim_bandwidth', 'values': [0]}, {'name': 'host_trim_iops', 'values': [0]}, {'name': 'total_wrc_write_bandwidth', 'values': [0]}, {'name': 'total_wrc_write_iops', 'values': [0]}, {'name': 'avg_wrc_write_io_size', 'values': [0]}, {'name': 'total_wrc_read_bandwidth', 'values': [0]}, {'name': 'total_wrc_read_iops', 'values': [0]}, {'name': 'avg_wrc_read_io_size', 'values': [0]}, {'name': 'physical_total', 'values': [6594922283008]}, {'name': 'logical_owned', 'values': [0]}, {'name': 'patterns_saving_reducible_ratio', 'values': [0.0]}, {'name': 'avg_host_trim_latency', 'values': [0]}], 'mediaType': None, 'name': 'SP_EC', 'numOfParallelRebuildRebalanceJobsPerDevice': None, 'overProvisioningFactor': 0, 'persistentChecksumBuilderLimitKb': None, 'persistentChecksumEnabled': False, 'persistentChecksumState': 'StateInvalid', 'persistentChecksumValidateOnRead': None, 'physicalSizeGB': 4095, 'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None, 'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None, 'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': None, 'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': None, 'protectedMaintenanceModeIoPriorityPolicy': None, 'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None, 'protectionDomainId': 'e597f3dd00000000', 'protectionScheme': 'TwoPlusTwo', 'rawSizeGB': 8190, 'rebalanceEnabled': None, 'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebalanceIoPriorityAppIopsPerDeviceThreshold': None, 'rebalanceIoPriorityBwLimitPerDeviceInKbps': None, 'rebalanceIoPriorityNumOfConcurrentIosPerDevice': None, 'rebalanceIoPriorityPolicy': None, 'rebalanceIoPriorityQuietPeriodInMsec': None, 'rebuildEnabled': None, 'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebuildIoPriorityAppIopsPerDeviceThreshold': None, 'rebuildIoPriorityBwLimitPerDeviceInKbps': None, 'rebuildIoPriorityNumOfConcurrentIosPerDevice': None, 'rebuildIoPriorityPolicy': None, 'rebuildIoPriorityQuietPeriodInMsec': None, 'replicationCapacityMaxRatio': None, 'rmcacheWriteHandlingMode': 'Invalid', 'spClass': 'Default', 'spHealthState': 'Protected', 'sparePercentage': None, 'useRfcache': False, 'useRmcache': False, 'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None, 'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None, 'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': None, 'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': None, 'vtreeMigrationIoPriorityPolicy': None, 'vtreeMigrationIoPriorityQuietPeriodInMsec': None, 'wrcDeviceGroupId': 'd291d60100000000', 'zeroPaddingEnabled': True}])
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


  addressSpaceUsage (, str, )
    Address space usage level of the storage pool.


  addressSpaceUsageType (, str, )
    Type of address space usage (e.g., hard limit or soft limit).


  backgroundScannerBWLimitKBps (, int, )
    Bandwidth limit in KBps for background scanner operations.


  backgroundScannerMode (, str, )
    Mode of the background scanner (e.g., disabled, full, etc.).


  bgScannerCompareErrorAction (, str, )
    Action to take when a compare error is detected during background scanning.


  bgScannerReadErrorAction (, str, )
    Action to take when a read error is detected during background scanning.


  capacityAlertCriticalThreshold (, int, )
    Threshold percentage for triggering critical capacity alerts.


  capacityAlertHighThreshold (, int, )
    Threshold percentage for triggering high capacity alerts.


  capacityUsageState (, str, )
    Current state of capacity usage (e.g., Normal, Critical).


  capacityUsageType (, str, )
    Type of capacity usage metric being reported.


  checksumEnabled (, bool, )
    Indicates whether checksum is enabled for data integrity.


  compressionMethod (, str, )
    Compression method used in the storage pool.


  dataLayout (, str, )
    Data layout scheme used in the storage pool (e.g., ErasureCoding).


  deviceGroupId (, str, )
    ID of the device group associated with the storage pool.


  externalAccelerationType (, str, )
    Type of external acceleration used.


  fglAccpId (, str, )
    Acceleration policy ID for FlashGuard Log (FGL) if applicable.


  fglExtraCapacity (, int, )
    Extra capacity allocated for FlashGuard Log.


  fglMaxCompressionRatio (, int, )
    Maximum compression ratio allowed for FlashGuard Log.


  fglMetadataSizeXx100 (, int, )
    Metadata size for FlashGuard Log as a percentage (multiplied by 100).


  fglNvdimmMetadataAmortizationX100 (, int, )
    NVDIMM metadata amortization factor for FlashGuard Log (multiplied by 100).


  fglNvdimmWriteCacheSizeInMb (, int, )
    Write cache size in MB for NVDIMM in FlashGuard Log.


  fglOverProvisioningFactor (, int, )
    Over-provisioning factor for FlashGuard Log.


  fglPerfProfile (, str, )
    Performance profile setting for FlashGuard Log.


  fglWriteAtomicitySize (, int, )
    Write atomicity size for FlashGuard Log.


  fragmentationEnabled (, bool, )
    Indicates whether fragmentation is enabled in the storage pool.


  genType (, str, )
    Generation type of the storage pool (e.g., EC for Erasure Coding).


  links (, list, )
    HATEOAS links related to the storage pool.


    href (, str, )
      URL reference for the link.


    rel (, str, )
      Relation type of the link (e.g., self).



  numOfParallelRebuildRebalanceJobsPerDevice (, int, )
    Number of parallel rebuild and rebalance jobs allowed per device.


  overProvisioningFactor (, int, )
    Over-provisioning factor applied to the storage pool.


  persistentChecksumBuilderLimitKb (, int, )
    Limit in KB for persistent checksum builder operations.


  persistentChecksumEnabled (, bool, )
    Indicates whether persistent checksum is enabled.


  persistentChecksumState (, str, )
    Current state of persistent checksum (e.g., StateInvalid, Valid).


  persistentChecksumValidateOnRead (, bool, )
    Whether to validate persistent checksum on read operations.


  physicalSizeGB (, int, )
    Physical size of the storage pool in gigabytes.


  protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps (, int, )
    Application bandwidth threshold per device in Kbps during protected maintenance mode.


  protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold (, int, )
    Application IOPS threshold per device during protected maintenance mode.


  protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps (, int, )
    Bandwidth limit per device in Kbps during protected maintenance mode.


  protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice (, int, )
    Maximum number of concurrent IOs per device during protected maintenance mode.


  protectedMaintenanceModeIoPriorityPolicy (, str, )
    IO priority policy during protected maintenance mode.


  protectedMaintenanceModeIoPriorityQuietPeriodInMsec (, int, )
    Quiet period in milliseconds during protected maintenance mode.


  protectionDomainName (, str, )
    Name of the protection domain in which pool resides.


  protectionScheme (, str, )
    Data protection scheme used (e.g., TwoPlusTwo).


  rawSizeGB (, int, )
    Raw (unformatted) size of the storage pool in gigabytes.


  rebalanceEnabled (, bool, )
    Indicates whether rebalancing is enabled for the storage pool.


  rebalanceIoPriorityAppBwPerDeviceThresholdInKbps (, int, )
    Application bandwidth threshold per device in Kbps during rebalance.


  rebalanceIoPriorityAppIopsPerDeviceThreshold (, int, )
    Application IOPS threshold per device during rebalance.


  rebalanceIoPriorityBwLimitPerDeviceInKbps (, int, )
    Bandwidth limit per device in Kbps during rebalance.


  rebalanceIoPriorityNumOfConcurrentIosPerDevice (, int, )
    Maximum number of concurrent IOs per device during rebalance.


  rebalanceIoPriorityPolicy (, str, )
    IO priority policy during rebalance operations.


  rebalanceIoPriorityQuietPeriodInMsec (, int, )
    Quiet period in milliseconds during rebalance operations.


  rebuildEnabled (, bool, )
    Indicates whether rebuilding is enabled for the storage pool.


  rebuildIoPriorityAppBwPerDeviceThresholdInKbps (, int, )
    Application bandwidth threshold per device in Kbps during rebuild.


  rebuildIoPriorityAppIopsPerDeviceThreshold (, int, )
    Application IOPS threshold per device during rebuild.


  rebuildIoPriorityBwLimitPerDeviceInKbps (, int, )
    Bandwidth limit per device in Kbps during rebuild.


  rebuildIoPriorityNumOfConcurrentIosPerDevice (, int, )
    Maximum number of concurrent IOs per device during rebuild.


  rebuildIoPriorityPolicy (, str, )
    IO priority policy during rebuild operations.


  rebuildIoPriorityQuietPeriodInMsec (, int, )
    Quiet period in milliseconds during rebuild operations.


  replicationCapacityMaxRatio (, int, )
    Maximum replication capacity ratio allowed.


  rmcacheWriteHandlingMode (, str, )
    Write handling mode for RMcache.


  spClass (, str, )
    Storage pool class (e.g., Default).


  spHealthState (, str, )
    Health state of the storage pool (e.g., Protected).


  sparePercentage (, int, )
    Percentage of spare capacity reserved in the storage pool.


  vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps (, int, )
    Application bandwidth threshold per device in Kbps during vTree migration.


  vtreeMigrationIoPriorityAppIopsPerDeviceThreshold (, int, )
    Application IOPS threshold per device during vTree migration.


  vtreeMigrationIoPriorityBwLimitPerDeviceInKbps (, int, )
    Bandwidth limit per device in Kbps during vTree migration.


  vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice (, int, )
    Maximum number of concurrent IOs per device during vTree migration.


  vtreeMigrationIoPriorityPolicy (, str, )
    IO priority policy during vTree migration.


  vtreeMigrationIoPriorityQuietPeriodInMsec (, int, )
    Quiet period in milliseconds during vTree migration.


  wrcDeviceGroupId (, str, )
    Write Reduction Cache (WRC) device group ID.


  zeroPaddingEnabled (, bool, )
    Indicates whether zero padding is enabled for the storage pool.


  statistics (, list, )
    List of performance and capacity statistics for the storage pool.


    name (, str, )
      Name of the statistic (e.g., avg\_host\_read\_latency).


    values (, list, )
      Values for the statistic.




Volumes (always, list, [{'accessModeLimit': 'ReadWrite', 'ancestorVolumeId': None, 'autoSnapshotGroupId': None, 'compressionMethod': 'NotApplicable', 'consistencyGroupId': None, 'creationTime': 1757086835, 'dataLayout': 'ErasureCoding', 'genType': 'EC', 'id': 'ae4f49db00000000', 'links': [{'href': '/api/instances/Volume::ae4f49db00000000', 'rel': 'self'}], 'statistics': [{'name': 'host_trim_bandwidth', 'values': [0]}, {'name': 'host_trim_iops', 'values': [0]}, {'name': 'avg_host_write_latency', 'values': [0]}, {'name': 'avg_host_read_latency', 'values': [0]}, {'name': 'logical_provisioned', 'values': [10737418240]}, {'name': 'host_read_bandwidth', 'values': [0]}, {'name': 'host_read_iops', 'values': [0]}, {'name': 'logical_used', 'values': [0]}, {'name': 'host_write_bandwidth', 'values': [0]}, {'name': 'host_write_iops', 'values': [0]}, {'name': 'avg_host_trim_latency', 'values': [0]}], 'lockedAutoSnapshot': False, 'lockedAutoSnapshotMarkedForRemoval': False, 'managedBy': 'ScaleIO', 'mappedSdcInfo': [{'accessMode': 'ReadWrite', 'hostType': 'SdcHost', 'isDirectBufferMapping': False, 'limitBwInMbps': 0, 'limitIops': 0, 'nqn': None, 'sdcId': 'e5282d9800000001', 'sdcIp': '10.225.106.98', 'sdcName': 'SDC2'}], 'name': 'ans_dev_1', 'notGenuineSnapshot': False, 'nsid': 1, 'originalExpiryTime': 0, 'pairIds': None, 'replicationJournalVolume': False, 'replicationTimeStamp': 0, 'retentionLevels': [], 'secureSnapshotExpTime': 0, 'sizeInKb': 10485760, 'snplIdOfAutoSnapshot': None, 'snplIdOfSourceVolume': '5026b97c00000000', 'storagePoolId': 'ea96090d00000000', 'timeStampIsAccurate': False, 'useRmcache': False, 'volumeClass': 'defaultclass', 'volumeReplicationState': 'UnmarkedForReplication', 'volumeType': 'ThinProvisioned', 'vtreeId': 'c7c9baf500000000'}])
  Details of volumes.


  accessModeLimit (, str, )
    Access mode limit for the volume (e.g., ReadWrite).


  ancestorVolumeId (, str, )
    ID of the ancestor volume, if this is a snapshot.


  autoSnapshotGroupId (, str, )
    ID of the auto-snapshot group associated with the volume.


  compressionMethod (, str, )
    Compression method used for the volume (e.g., NotApplicable).


  consistencyGroupId (, str, )
    ID of the consistency group the volume belongs to.


  creationTime (, int, )
    Unix timestamp (in seconds) when the volume was created.


  dataLayout (, str, )
    Data layout type of the volume (e.g., ErasureCoding).


  genType (, str, )
    Generation type of the volume (e.g., EC).


  id (, str, )
    Unique identifier of the volume.


  links (, list, )
    List of hypermedia links related to the volume.


    href (, str, )
      URL reference for the link.


    rel (, str, )
      Relationship of the link (e.g., self, query).



  lockedAutoSnapshot (, bool, )
    Indicates whether the auto-snapshot is locked.


  lockedAutoSnapshotMarkedForRemoval (, bool, )
    Indicates whether the locked auto-snapshot is marked for removal.


  managedBy (, str, )
    System or component managing the volume (e.g., ScaleIO).


  mappedSdcInfo (, list, )
    Information about SDCs (hosts) mapped to this volume.


    accessMode (, str, )
      Access mode granted to the SDC (e.g., ReadWrite).


    hostType (, str, )
      Type of host (e.g., SdcHost).


    isDirectBufferMapping (, bool, )
      Indicates whether direct buffer mapping is used.


    limitBwInMbps (, int, )
      Bandwidth limit in Mbps (0 means unlimited).


    limitIops (, int, )
      IOPS limit (0 means unlimited).


    nqn (, str, )
      NVMe Qualified Name, if applicable.


    sdcId (, str, )
      Unique ID of the SDC (host).


    sdcIp (, str, )
      IP address of the SDC.


    sdcName (, str, )
      Name of the SDC.



  name (, str, )
    Name of the volume.


  notGenuineSnapshot (, bool, )
    Indicates whether the snapshot is not a genuine point-in-time copy.


  nsid (, int, )
    Namespace ID assigned to the volume.


  originalExpiryTime (, int, )
    Original expiry time for the volume or snapshot.


  pairIds (, str, )
    List of paired volume IDs, if volume is part of a pair.


  replicationJournalVolume (, bool, )
    Indicates whether the volume is used as a journal for replication.


  replicationTimeStamp (, int, )
    Timestamp of the last replication event.


  retentionLevels (, list, )
    List of retention levels configured for the volume.


  secureSnapshotExpTime (, int, )
    Expiration time for secure snapshots.


  sizeInKb (, int, )
    Size of the volume in kilobytes.


  snplIdOfAutoSnapshot (, str, )
    Snapshot policy ID associated with auto-snapshot.


  snplIdOfSourceVolume (, str, )
    Snapshot policy ID of the source volume.


  storagePoolId (, str, )
    ID of the storage pool where the volume resides.


  timeStampIsAccurate (, bool, )
    Indicates whether the timestamp is accurate.


  useRmcache (, bool, )
    Indicates whether remote cache is enabled for the volume.


  volumeClass (, str, )
    Class or QoS policy assigned to the volume.


  volumeReplicationState (, str, )
    Replication state of the volume (e.g., UnmarkedForReplication).


  volumeType (, str, )
    Type of the volume (e.g., ThinProvisioned).


  vtreeId (, str, )
    ID of the VTree (virtual tree) to which the volume belongs.


  statistics (, list, )
    List of performance and capacity statistics for the volume.


    name (, str, )
      Name of the statistic (e.g., avg\_host\_read\_latency).


    values (, list, )
      Values for the statistic.




Devices (always, list, [{'accelerationPoolId': None, 'accelerationProps': None, 'aggregatedState': 'NeverFailed', 'ataSecurityActive': False, 'autoDetectMediaType': None, 'cacheLookAheadActive': False, 'capacity': 0, 'capacityInMb': 1048576, 'capacityLimitInKb': 1073479680, 'deviceCurrentPathName': '/dev/sdf', 'deviceGroupId': 'd291d60100000000', 'deviceOriginalPathName': '/dev/sdf', 'deviceState': 'Normal', 'deviceType': 'Unknown', 'errorState': 'None', 'externalAccelerationType': 'None', 'fglNvdimmMetadataAmortizationX100': None, 'fglNvdimmWriteCacheSize': None, 'firmwareVersion': None, 'id': '63efabfb00000004', 'ledSetting': 'Off', 'links': [{'href': '/api/instances/Device::63efabfb00000004', 'rel': 'self'}], 'logicalSectorSizeInBytes': 0, 'longSuccessfulIos': {'longWindow': None, 'mediumWindow': None, 'shortWindow': None}, 'maxCapacityInKb': 1073479680, 'mediaFailing': False, 'mediaType': 'SSD', 'modelName': None, 'name': 'sdf', 'persistentChecksumState': 'StateInvalid', 'physicalSectorSizeInBytes': 0, 'raidControllerSerialNumber': None, 'rfcacheErrorDeviceDoesNotExist': False, 'rfcacheProps': None, 'sdsId': None, 'serialNumber': None, 'slotNumber': 'N/A', 'spSdsId': None, 'ssdEndOfLifeState': 'NeverFailed', 'storageNodeId': '876859f300000000', 'storagePoolId': None, 'storageProps': None, 'temperatureState': 'NeverFailed', 'usableCapacityInMb': 1048320, 'vendorName': None, 'writeCacheActive': False}])
  Details of devices.


  id (, str, )
    device id.


  name (, str, )
    device name.


  accelerationPoolId (, str, )
    ID of the acceleration pool associated with the device.


  accelerationProps (, str, )
    Acceleration properties of the device.


  aggregatedState (, str, )
    Aggregated health state of the device (e.g., NeverFailed).


  ataSecurityActive (, bool, )
    Indicates whether ATA security is active on the device.


  autoDetectMediaType (, str, )
    Indicates whether media type auto-detection is enabled.


  cacheLookAheadActive (, bool, )
    Indicates whether cache look-ahead is enabled for the device.


  capacity (, int, )
    Total capacity of the device (in KB or other unit, context-dependent).


  capacityInMb (, int, )
    Total capacity of the device in megabytes.


  capacityLimitInKb (, int, )
    Capacity limit of the device in kilobytes.


  deviceCurrentPathName (, str, )
    Current device path name (e.g., /dev/sdf).


  deviceGroupId (, str, )
    ID of the device group to which the device belongs.


  deviceOriginalPathName (, str, )
    Original device path name at time of discovery.


  deviceState (, str, )
    Current operational state of the device (e.g., Normal).


  deviceType (, str, )
    Type of the device (e.g., Unknown, SSD).


  errorState (, str, )
    Current error state of the device (e.g., None).


  externalAccelerationType (, str, )
    Type of external acceleration used (e.g., None).


  fglNvdimmMetadataAmortizationX100 (, str, )
    Metadata amortization factor for FlashGuard Log (FGL) devices.


  fglNvdimmWriteCacheSize (, str, )
    NVDIMM write cache size for FlashGuard Log (FGL) devices.


  firmwareVersion (, str, )
    Firmware version of the device.


  ledSetting (, str, )
    Current LED indicator setting of the device (e.g., Off).


  links (, list, )
    List of hypermedia links related to the device.


    href (, str, )
      The URI of the linked resource.


    rel (, str, )
      The relation type of the link.



  logicalSectorSizeInBytes (, int, )
    Logical sector size of the device in bytes.


  longSuccessfulIos (, dict, )
    Long-term successful I/O statistics for the device.


    longWindow (, str, )
      Number of successful I/Os in the long time window.


    mediumWindow (, str, )
      Number of successful I/Os in the medium time window.


    shortWindow (, str, )
      Number of successful I/Os in the short time window.



  maxCapacityInKb (, int, )
    Maximum supported capacity of the device in kilobytes.


  mediaFailing (, bool, )
    Indicates whether the device media is failing.


  mediaType (, str, )
    Type of media used in the device (e.g., SSD).


  modelName (, str, )
    Model name of the device.


  persistentChecksumState (, str, )
    State of persistent checksum on the device (e.g., StateInvalid).


  physicalSectorSizeInBytes (, int, )
    Physical sector size of the device in bytes.


  raidControllerSerialNumber (, str, )
    Serial number of the RAID controller managing the device.


  rfcacheErrorDeviceDoesNotExist (, bool, )
    Indicates if there is an RFcache error due to missing device.


  rfcacheProps (, str, )
    RFcache properties associated with the device.


  sdsId (, str, )
    ID of the SDS (ScaleIO Data Server) managing the device.


  serialNumber (, str, )
    Serial number of the device.


  slotNumber (, str, )
    Physical slot number where the device is installed (e.g., N/A).


  spSdsId (, str, )
    SDS ID specific to the storage pool.


  ssdEndOfLifeState (, str, )
    SSD end-of-life status (e.g., NeverFailed).


  storageNodeId (, str, )
    ID of the storage node hosting the device.


  storagePoolId (, str, )
    ID of the storage pool to which the device is assigned.


  storageProps (, str, )
    Storage-related properties of the device.


  temperatureState (, str, )
    Temperature health state of the device (e.g., NeverFailed).


  usableCapacityInMb (, int, )
    Usable capacity of the device in megabytes.


  vendorName (, str, )
    Manufacturer/vendor name of the device.


  writeCacheActive (, bool, )
    Indicates whether write cache is currently active on the device.



ManagedDevices (when I(gather_subset) is I(managed_device), list, [{'chassisId': None, 'compliance': 'NONCOMPLIANT', 'complianceCheckDate': '2025-09-04T16:00:51.857+00:00', 'config': None, 'cpuType': None, 'credId': 'e938b574-8a0d-4b20-aea6-e0dd557d766d', 'currentIpAddress': '10.43.1.67', 'customFirmware': False, 'detailLink': {'href': '/AsmManager/ManagedDevice/scaleio-block-legacy-gateway', 'rel': 'describedby', 'title': 'scaleio-block-legacy-gateway', 'type': None}, 'deviceGroupList': {'deviceGroup': [{'createdBy': 'admin', 'createdDate': None, 'groupDescription': None, 'groupName': 'Global', 'groupSeqId': -1, 'groupUserList': None, 'link': None, 'managedDeviceList': None, 'updatedBy': None, 'updatedDate': None}], 'paging': None}, 'deviceType': 'scaleio', 'discoverDeviceType': 'SCALEIO', 'discoveredDate': '2025-08-22T15:48:05.477+00:00', 'displayName': 'block-legacy-gateway', 'esxiMaintMode': 0, 'failuresCount': 0, 'firmwareName': 'Default Catalog - Intelligent Catalog 50.390.00', 'flexosMaintMode': 0, 'health': 'GREEN', 'healthMessage': 'OK', 'hostname': None, 'inUse': False, 'infraTemplateDate': None, 'infraTemplateId': None, 'inventoryDate': None, 'ipAddress': 'block-legacy-gateway', 'lastJobs': None, 'managedState': 'MANAGED', 'manufacturer': 'Dell EMC', 'memoryInGB': 0, 'model': 'PowerFlex Gateway', 'needsAttention': False, 'nics': 0, 'numberOfCPUs': 0, 'operatingSystem': 'N/A', 'osAdminCredential': None, 'osImageType': None, 'osIpAddress': None, 'parsedFacts': None, 'puppetCertName': 'scaleio-block-legacy-gateway', 'refId': 'scaleio-block-legacy-gateway', 'refType': None, 'serverTemplateDate': None, 'serverTemplateId': None, 'serviceReferences': [], 'serviceTag': 'block-legacy-gateway', 'state': 'UPDATE_FAILED', 'statusMessage': None, 'svmAdminCredential': None, 'svmImageType': None, 'svmIpAddress': None, 'svmName': None, 'systemId': None, 'vmList': []}])
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


  chassisId (, str, )
    Chassis ID to which the device belongs, if applicable.


  complianceCheckDate (, str, )
    Timestamp when the compliance check was last performed.


  config (, str, )
    Configuration details of the device.


  cpuType (, str, )
    Type of CPU installed on the device.


  credId (, str, )
    Credential ID used for device authentication.


  currentIpAddress (, str, )
    Current IP address assigned to the device.


  customFirmware (, bool, )
    Indicates whether custom firmware is applied to the device.


  detailLink (, dict, )
    Hypermedia link providing more details about the device.


    href (, str, )
      The URI of the detailed resource.


    rel (, str, )
      The relation type of the link.


    title (, str, )
      Human-readable title of the linked resource.


    type (, str, )
      Media type of the linked resource.



  deviceGroupList (, dict, )
    List of device groups the device belongs to.


    deviceGroup (, list, )
      List of device group entries.


      createdBy (, str, )
        User who created the device group.


      createdDate (, str, )
        Date when the device group was created.


      groupDescription (, str, )
        Description of the device group.


      groupName (, str, )
        Name of the device group.


      groupSeqId (, int, )
        Sequential ID of the device group.


      groupUserList (, str, )
        List of users associated with the device group.


      link (, str, )
        Link to the device group resource.


      managedDeviceList (, str, )
        List of managed devices in the group.


      updatedBy (, str, )
        User who last updated the device group.


      updatedDate (, str, )
        Date when the device group was last updated.



    paging (, str, )
      Pagination information for the device group list.



  discoverDeviceType (, str, )
    Discovered device type (e.g., SCALEIO).


  discoveredDate (, str, )
    Timestamp when the device was discovered.


  displayName (, str, )
    Display name of the device.


  esxiMaintMode (, int, )
    ESXi maintenance mode status of the device.


  failuresCount (, int, )
    Number of failures reported for the device.


  firmwareName (, str, )
    Name of the firmware or catalog applied to the device.


  flexosMaintMode (, int, )
    FlexOS maintenance mode status of the device.


  health (, str, )
    Overall health status of the device (e.g., GREEN).


  healthMessage (, str, )
    Health status message (e.g., OK).


  hostname (, str, )
    Hostname of the device.


  inUse (, bool, )
    Indicates whether the device is currently in use.


  infraTemplateDate (, str, )
    Date of the infrastructure template applied.


  infraTemplateId (, str, )
    ID of the infrastructure template applied.


  inventoryDate (, str, )
    Timestamp when the device inventory was last updated.


  ipAddress (, str, )
    IP address of the device.


  lastJobs (, str, )
    List of recent jobs executed on the device.


  manufacturer (, str, )
    Manufacturer of the device (e.g., Dell EMC).


  memoryInGB (, int, )
    Total memory of the device in gigabytes.


  model (, str, )
    Model name of the device (e.g., PowerFlex Gateway).


  needsAttention (, bool, )
    Indicates whether the device requires attention.


  nics (, int, )
    Number of network interface cards on the device.


  numberOfCPUs (, int, )
    Number of CPUs installed on the device.


  operatingSystem (, str, )
    Operating system running on the device (e.g., N/A).


  osAdminCredential (, str, )
    Credential for OS-level administrative access.


  osImageType (, str, )
    Type of OS image used.


  osIpAddress (, str, )
    IP address assigned to the OS instance.


  parsedFacts (, str, )
    Parsed system facts collected from the device.


  puppetCertName (, str, )
    Puppet certificate name for the device.


  refId (, str, )
    Reference ID of the device.


  refType (, str, )
    Reference type of the device.


  serverTemplateDate (, str, )
    Date of the server template applied.


  serviceReferences (, list, )
    List of service references associated with the device.


  statusMessage (, str, )
    Additional status message for the device.


  svmAdminCredential (, str, )
    Credential for SVM (Storage Virtual Machine) access.


  svmImageType (, str, )
    Type of SVM image used.


  svmIpAddress (, str, )
    IP address assigned to the SVM.


  svmName (, str, )
    Name of the SVM.


  vmList (, list, )
    List of virtual machines associated with the device.



Deployments (when I(gather_subset) is I(deployment), list, [{'allUsersAllowed': True, 'assignedUsers': [], 'brownfield': False, 'compliant': False, 'configurationChange': False, 'createdBy': 'admin', 'createdDate': '2025-09-09T13:42:55.611+00:00', 'currentBatchCount': None, 'currentStepCount': None, 'currentStepMessage': None, 'customImage': 'rcm_linux', 'deploymentDescription': None, 'deploymentDevice': [{'brownfield': False, 'brownfieldStatus': 'NOT_APPLICABLE', 'cloudLink': False, 'compliantState': 'COMPLIANT', 'componentId': None, 'currentIpAddress': '10.226.197.13', 'dasCache': False, 'deviceGroupName': 'Global', 'deviceHealth': 'GREEN', 'deviceState': 'DEPLOYING', 'deviceType': 'RackServer', 'healthMessage': 'OK', 'ipAddress': '10.226.197.13', 'logDump': None, 'model': 'PowerFlex custom node R650 S', 'puppetCertName': 'rackserver-bdwmcx3', 'refId': '8aaa07b2992a323a01992bc3945606cc', 'refType': None, 'serviceTag': 'BDWMCX3', 'status': None, 'statusEndTime': None, 'statusMessage': None, 'statusStartTime': None}], 'deploymentFinishedDate': None, 'deploymentHealthStatusType': 'yellow', 'deploymentName': 'ECBlock', 'deploymentScheduledDate': None, 'deploymentStartedDate': '2025-09-09T14:21:11.073+00:00', 'deploymentValid': None, 'deploymentValidationResponse': None, 'disruptiveFirmware': False, 'firmwareInit': False, 'firmwareRepository': {'bundleCount': 0, 'componentCount': 0, 'createdBy': None, 'createdDate': None, 'custom': False, 'defaultCatalog': False, 'deployments': [], 'diskLocation': None, 'downloadProgress': 0, 'downloadStatus': None, 'esxiOSRepository': None, 'esxiSoftwareBundle': None, 'esxiSoftwareComponent': None, 'extractProgress': 0, 'fileSizeInGigabytes': None, 'filename': None, 'id': '8aaa07b2992a323a01992bc015d30135', 'jobId': None, 'md5Hash': None, 'minimal': False, 'name': 'Intelligent Catalog 50.390.00', 'needsAttention': False, 'password': None, 'rcmapproved': False, 'signature': None, 'signedKeySourceLocation': None, 'softwareBundles': [], 'softwareComponents': [], 'sourceLocation': None, 'sourceType': None, 'state': None, 'updatedBy': None, 'updatedDate': None, 'userBundleCount': 0, 'username': None}, 'firmwareRepositoryId': '8aaa07b2992a323a01992bc015d30135', 'id': '8aaa07af992e959c01992eb7197b0150', 'individualTeardown': False, 'jobDetails': None, 'jobId': None, 'licenseRepository': None, 'licenseRepositoryId': None, 'lifecycleMode': False, 'lifecycleModeReasons': [], 'noOp': False, 'numberOfDeployments': 0, 'operationData': None, 'operationStatus': None, 'operationType': 'RETRY', 'originalDeploymentId': None, 'owner': 'admin', 'precalculatedDeviceHealth': None, 'preconfigureSVM': False, 'preconfigureSVMAndUpdate': False, 'removeService': False, 'retry': False, 'scaleUp': False, 'scheduleDate': None, 'serviceTemplate': {'allUsersAllowed': True, 'assignedUsers': [], 'blockServiceOperationsMap': {}, 'brownfieldTemplateType': 'NONE', 'category': 'block', 'clusterCount': 1, 'components': [{'asmGUID': 'scaleio-block-legacy-gateway', 'brownfield': False, 'cloned': False, 'clonedFromAsmGuid': None, 'clonedFromId': None, 'componentID': 'component-scaleio-gateway-1', 'componentValid': {'messages': [], 'valid': True}, 'configFile': None, 'helpText': None, 'id': '92511015-2a1e-498b-8b93-41455253dabf', 'identifier': None, 'instances': 1, 'ip': None, 'manageFirmware': False, 'managementIpAddress': None, 'name': 'block-legacy-gateway', 'osPuppetCertName': None, 'puppetCertName': 'scaleio-block-legacy-gateway', 'refId': None, 'relatedComponents': {'068e82fc-3767-49ee-a052-f2d8cac50d87': 'Storage Only Node-4', '37e5ab99-ee64-4122-9eb0-92c7d76b8233': 'Storage Only Node', '73dda7ab-dc46-411a-aae4-99bdb0d0e47a': 'Storage Only Node-2', 'c01f69a4-a1f9-4bba-8471-15285db1f18e': 'Storage Only Node-5', 'fb7b47e0-5da0-497e-a579-98a9557e1682': 'Storage Only Node-3'}, 'resources': [], 'serialNumber': None, 'subType': 'STORAGEONLY', 'teardown': False, 'type': 'SCALEIO'}], 'configuration': None, 'createdBy': None, 'createdDate': '2025-09-09T13:43:03.001+00:00', 'draft': False, 'firmwareRepository': None, 'hideTemplateActive': False, 'id': '8aaa07af992e959c01992eb7197b0150', 'inConfiguration': False, 'lastDeployedDate': None, 'licenseRepository': None, 'manageFirmware': True, 'networks': [{'description': '', 'destinationIpAddress': '10.230.45.0', 'id': '8aaa2600992a26d601992c06ec8e0021', 'name': 'Data-345', 'static': True, 'staticNetworkConfiguration': {'dnsSuffix': 'pie.lab.emc.com', 'gateway': '10.230.45.1', 'ipAddress': None, 'ipRange': [{'endingIp': '10.230.45.30', 'id': '8aaa2600992a26d601992c06ec8e0022', 'role': None, 'startingIp': '10.230.45.21'}], 'primaryDns': '10.230.44.169', 'secondaryDns': '10.230.44.170', 'staticRoute': None, 'subnet': '255.255.255.0'}, 'type': 'SCALEIO_DATA', 'vlanId': 345}], 'originalTemplateId': 'e3deed3d-25ac-4154-8696-b65293213cfd', 'sdnasCount': 0, 'serverCount': 5, 'serviceCount': 0, 'storageCount': 0, 'switchCount': 0, 'templateDescription': 'Storage Only 5 Node deployment using Erasure Coding', 'templateLocked': False, 'templateName': 'SO NVMe Enabled Clone (8aaa07af992e959c01992eb7197b0150)', 'templateType': 'VxRack FLEX', 'templateValid': {'messages': [], 'valid': True}, 'templateVersion': '5.0.0.0', 'updatedBy': None, 'updatedDate': None, 'useDefaultCatalog': False, 'vmCount': 0}, 'servicesDeployed': 'NONE', 'status': 'in_progress', 'teardown': False, 'teardownAfterCancel': False, 'templateValid': True, 'totalBatchCount': None, 'totalNumOfSteps': None, 'updateServerFirmware': True, 'updatedBy': 'system', 'updatedDate': '2025-09-10T02:00:17.092+00:00', 'useDefaultCatalog': False, 'vds': False, 'vms': None}])
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



  allUsersAllowed (, bool, )
    Whether the deployment is accessible to all users.


  assignedUsers (, list, )
    List of users assigned to this deployment.


  brownfield (, bool, )
    Indicates if this is a brownfield (existing infrastructure) deployment.


  compliant (, bool, )
    Indicates whether the deployment is compliant with its template.


  configurationChange (, bool, )
    Indicates if there has been a configuration change in the deployment.


  createdBy (, str, )
    User who created the deployment.


  createdDate (, str, )
    Timestamp when the deployment was created.


  currentBatchCount (, int, )
    Current batch number being processed in the deployment workflow.


  currentStepCount (, int, )
    Current step number within the current batch of the deployment.


  currentStepMessage (, str, )
    Message or status detail for the current step in deployment.


  customImage (, str, )
    Name of the custom image used for deployment.


  deploymentDescription (, str, )
    Description of the deployment.


  deploymentDevice (, list, )
    List of devices involved in the deployment.


    brownfield (, bool, )
      Indicates if the device is part of a brownfield deployment.


    brownfieldStatus (, str, )
      Status indicating brownfield applicability for the device.


    cloudLink (, bool, )
      Indicates if CloudLink is enabled on the device.


    compliantState (, str, )
      Compliance state of the device (e.g., COMPLIANT, NON\_COMPLIANT).


    componentId (, str, )
      Component ID associated with the device.


    currentIpAddress (, str, )
      Current IP address assigned to the device.


    dasCache (, bool, )
      Indicates if DAS cache is enabled on the device.


    deviceGroupName (, str, )
      Name of the group to which the device belongs.


    deviceHealth (, str, )
      Health status of the device (e.g., GREEN, YELLOW, RED).


    deviceState (, str, )
      Current state of the device in the deployment lifecycle.


    deviceType (, str, )
      Type of device (e.g., RackServer, Switch).


    healthMessage (, str, )
      Detailed health message for the device.


    ipAddress (, str, )
      IP address configured for the device.


    logDump (, str, )
      Log dump information from the device.


    model (, str, )
      Hardware model of the device.


    puppetCertName (, str, )
      Puppet certificate name used for managing the device.


    refId (, str, )
      Reference ID of the device in the system.


    refType (, str, )
      Type of reference for the device.


    serviceTag (, str, )
      Service tag identifier of the physical device.


    status (, str, )
      Current operational status of the device.


    statusEndTime (, str, )
      Timestamp when the current status ended.


    statusMessage (, str, )
      Additional message explaining the current status.


    statusStartTime (, str, )
      Timestamp when the current status began.



  deploymentFinishedDate (, str, )
    Timestamp when the deployment was completed.


  deploymentHealthStatusType (, str, )
    Aggregated health status of the deployment (e.g., green, yellow, red).


  deploymentScheduledDate (, str, )
    Scheduled start time for the deployment.


  deploymentStartedDate (, str, )
    Timestamp when the deployment actually started.


  deploymentValid (, bool, )
    Indicates if the deployment configuration is valid.


  deploymentValidationResponse (, str, )
    Detailed response from the validation process.


  disruptiveFirmware (, bool, )
    Indicates if firmware update is disruptive (requires reboot).


  firmwareInit (, bool, )
    Indicates if firmware initialization has started.


  firmwareRepositoryId (, str, )
    ID of the firmware repository used.


  individualTeardown (, bool, )
    Indicates if individual components can be torn down separately.


  jobDetails (, str, )
    Details about the background job handling the deployment.


  jobId (, str, )
    ID of the associated background job.


  licenseRepository (, str, )
    License repository configuration used in deployment.


  licenseRepositoryId (, str, )
    ID of the license repository used.


  lifecycleMode (, bool, )
    Indicates if the deployment is in lifecycle management mode.


  lifecycleModeReasons (, list, )
    List of reasons why lifecycle mode is active.


  noOp (, bool, )
    Indicates if the deployment is running in dry-run (no-op) mode.


  numberOfDeployments (, int, )
    Number of deployments associated with this record.


  operationData (, str, )
    Additional data related to the current operation.


  operationStatus (, str, )
    Status of the current operation (e.g., running, failed).


  operationType (, str, )
    Type of operation being performed (e.g., RETRY, CREATE).


  originalDeploymentId (, str, )
    ID of the original deployment if this is a retry or clone.


  owner (, str, )
    Owner of the deployment.


  precalculatedDeviceHealth (, str, )
    Pre-calculated health status of devices.


  preconfigureSVM (, bool, )
    Indicates if SVM (ScaleIO Volume Manager) should be preconfigured.


  preconfigureSVMAndUpdate (, bool, )
    Indicates if SVM should be preconfigured and updated.


  removeService (, bool, )
    Indicates if services should be removed during teardown.


  retry (, bool, )
    Indicates if this deployment is a retry of a previous attempt.


  scaleUp (, bool, )
    Indicates if this is a scale-up deployment.


  scheduleDate (, str, )
    Date when the deployment is scheduled to run.


  serviceTemplate (, dict, )
    Template used to define the structure and components of the service.


    allUsersAllowed (, bool, )
      Whether the template is accessible to all users.


    assignedUsers (, list, )
      List of users assigned to use this template.


    brownfieldTemplateType (, str, )
      Type of brownfield support in the template.


    category (, str, )
      Category of the service (e.g., block, compute).


    clusterCount (, int, )
      Number of clusters defined in the template.


    components (, list, )
      List of components included in the service template.


      asmGUID (, str, )
        Unique identifier for the component in ASM.


      brownfield (, bool, )
        Indicates if the component supports brownfield deployment.


      cloned (, bool, )
        Indicates if the component was cloned from another.


      clonedFromAsmGuid (, str, )
        ASM GUID of the source component if cloned.


      clonedFromId (, str, )
        ID of the source component if cloned.


      componentID (, str, )
        Internal ID of the component.


      componentValid (, dict, )
        Validation result for the component.


        messages (, list, )
          List of validation messages.


        valid (, bool, )
          Whether the component is valid.



      configFile (, str, )
        Path or name of the configuration file.


      helpText (, str, )
        Help text describing the component.


      id (, str, )
        Unique identifier for the component.


      identifier (, str, )
        External identifier for the component.


      instances (, int, )
        Number of instances of this component.


      ip (, str, )
        Static IP assigned to the component.


      manageFirmware (, bool, )
        Indicates if firmware management is enabled for this component.


      managementIpAddress (, str, )
        IP address used for managing the component.


      name (, str, )
        Name of the component.


      osPuppetCertName (, str, )
        Puppet certificate name for the OS layer.


      puppetCertName (, str, )
        Puppet certificate name for the component.


      refId (, str, )
        Reference ID in external systems.


      resources (, list, )
        List of resources allocated to the component.


      serialNumber (, str, )
        Serial number of the hardware component.


      subType (, str, )
        Sub-type of the component (e.g., STORAGEONLY).


      teardown (, bool, )
        Indicates if the component should be removed on teardown.


      type (, str, )
        Type of the component (e.g., SCALEIO).



    configuration (, str, )
      Full configuration payload for the service.


    createdDate (, str, )
      Timestamp when the template was created.


    draft (, bool, )
      Indicates if the template is a draft version.


    hideTemplateActive (, bool, )
      Indicates if the template is hidden from users.


    id (, str, )
      Template ID.


    inConfiguration (, bool, )
      Indicates if the template is currently in use.


    lastDeployedDate (, str, )
      Timestamp of the last deployment using this template.


    licenseRepository (, str, )
      License repository associated with the template.


    manageFirmware (, bool, )
      Indicates if firmware updates are managed for this template.


    networks (, list, )
      List of network configurations in the template.


      description (, str, )
        Description of the network.


      destinationIpAddress (, str, )
        Destination IP range for routing.


      id (, str, )
        Network ID.


      name (, str, )
        Name of the network.


      static (, bool, )
        Indicates if the network uses static addressing.


      staticNetworkConfiguration (, dict, )
        Static network settings.


        dnsSuffix (, str, )
          DNS suffix for the network.


        gateway (, str, )
          Default gateway IP.


        ipAddress (, str, )
          Specific IP assigned.


        ipRange (, list, )
          Range of IPs available for allocation.


          endingIp (, str, )
            Last IP in the range.


          id (, str, )
            ID of the IP range.


          role (, str, )
            Role of IPs in this range.


          startingIp (, str, )
            First IP in the range.



        primaryDns (, str, )
          Primary DNS server IP.


        secondaryDns (, str, )
          Secondary DNS server IP.


        staticRoute (, str, )
          Static route configuration.


        subnet (, str, )
          Subnet mask in dotted decimal format.



      type (, str, )
        Type of network (e.g., SCALEIO\_DATA).


      vlanId (, int, )
        VLAN ID associated with the network.



    originalTemplateId (, str, )
      ID of the base template if this is a derived version.


    sdnasCount (, int, )
      Number of SDNAS nodes in the template.


    serverCount (, int, )
      Number of servers defined in the template.


    serviceCount (, int, )
      Number of services in the template.


    storageCount (, int, )
      Number of storage units.


    switchCount (, int, )
      Number of switches included.


    templateDescription (, str, )
      Description of the service template.


    templateLocked (, bool, )
      Indicates if the template is locked for editing.


    templateName (, str, )
      Name of the service template.


    templateType (, str, )
      Type of template (e.g., VxRack FLEX).


    templateValid (, dict, )
      Validation status of the template.


      messages (, list, )
        List of validation messages.


      valid (, bool, )
        Whether the template is valid.



    templateVersion (, str, )
      Version of the template.


    updatedDate (, str, )
      Timestamp when the template was last updated.


    useDefaultCatalog (, bool, )
      Indicates if the default firmware catalog is used.


    vmCount (, int, )
      Number of virtual machines in the template.



  servicesDeployed (, str, )
    Status of services deployed (e.g., NONE, PARTIAL, ALL).


  teardown (, bool, )
    Indicates if the deployment is scheduled for teardown.


  teardownAfterCancel (, bool, )
    Indicates if teardown should occur after cancellation.


  templateValid (, bool, )
    Indicates if the associated service template is valid.


  totalBatchCount (, int, )
    Total number of batches in the deployment workflow.


  totalNumOfSteps (, int, )
    Total number of steps across all batches.


  updateServerFirmware (, bool, )
    Indicates if server firmware should be updated during deployment.


  updatedBy (, str, )
    User who last updated the deployment.


  updatedDate (, str, )
    Timestamp when the deployment was last updated.


  useDefaultCatalog (, bool, )
    Indicates if the default firmware catalog is used.


  vds (, bool, )
    Indicates if Virtual Distributed Switches are used.


  vms (, list, )
    Virtual machine configurations or status.



ServiceTemplates (when I(gather_subset) is I(service_template), list, [{'allUsersAllowed': False, 'assignedUsers': [], 'blockServiceOperationsMap': {}, 'brownfieldTemplateType': 'NONE', 'category': 'Sample Templates', 'clusterCount': 1, 'components': [{'asmGUID': None, 'brownfield': False, 'cloned': False, 'clonedFromAsmGuid': None, 'clonedFromId': None, 'componentID': 'component-scaleio-gateway-1', 'componentValid': {'messages': [], 'valid': True}, 'configFile': None, 'helpText': None, 'id': 'f9adcdba-e0e7-4977-938e-9e5ca626d037', 'identifier': None, 'instances': 1, 'ip': None, 'manageFirmware': False, 'managementIpAddress': None, 'name': 'PowerFlex Cluster', 'osPuppetCertName': None, 'puppetCertName': None, 'refId': None, 'relatedComponents': {'db582229-d23e-4ce2-b242-ecfc17f1c16b': 'Storage Only Node'}, 'resources': [], 'serialNumber': None, 'subType': 'STORAGEONLY', 'teardown': False, 'type': 'SCALEIO'}], 'configuration': None, 'createdBy': 'system', 'createdDate': '2025-08-22T15:48:20.369+00:00', 'draft': False, 'firmwareRepository': None, 'hideTemplateActive': True, 'id': '4d0468be-6827-4c41-bbaf-01086de116a8', 'inConfiguration': False, 'lastDeployedDate': None, 'licenseRepository': None, 'manageFirmware': True, 'networks': [{'description': '', 'destinationIpAddress': '192.168.104.0', 'id': 'ff80808177f8823b0177f8ba236b0004', 'name': 'flex-data1', 'static': True, 'staticNetworkConfiguration': {'dnsSuffix': None, 'gateway': None, 'ipAddress': None, 'ipRange': None, 'primaryDns': None, 'secondaryDns': None, 'staticRoute': None, 'subnet': '255.255.255.0'}, 'type': 'SCALEIO_DATA', 'vlanId': 104}], 'originalTemplateId': 'ff80808177f880fc0177f883bf1e0027', 'sdnasCount': 0, 'serverCount': 4, 'serviceCount': 0, 'storageCount': 0, 'switchCount': 0, 'templateDescription': 'Storage Only 4 Node deployment with 100Gb networking', 'templateLocked': True, 'templateName': 'Mirroring - Storage 100Gb - 2 Data - LACP', 'templateType': 'VxRack FLEX', 'templateValid': {'messages': [], 'valid': True}, 'templateVersion': '5.0.0-2956', 'updatedBy': None, 'updatedDate': None, 'useDefaultCatalog': True, 'vmCount': 0}])
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


  allUsersAllowed (, bool, )
    Indicates whether the template is available to all users.


  assignedUsers (, list, )
    List of users explicitly assigned to use this template.


  brownfieldTemplateType (, str, )
    Type of brownfield deployment supported by the template (e.g., NONE).


  clusterCount (, int, )
    Number of clusters defined in the template.


  components (, list, )
    List of components included in the service template.


    asmGUID (, str, )
      ASM GUID of the component, if applicable.


    brownfield (, bool, )
      Indicates whether the component supports brownfield deployment.


    cloned (, bool, )
      Indicates whether the component is cloned from another.


    clonedFromAsmGuid (, str, )
      ASM GUID of the source component if cloned.


    clonedFromId (, str, )
      ID of the source component if cloned.


    componentID (, str, )
      Unique identifier for the component.


    componentValid (, dict, )
      Validation status of the component.


      messages (, list, )
        List of validation messages.


      valid (, bool, )
        Indicates whether the component is valid.



    configFile (, str, )
      Configuration file associated with the component.


    helpText (, str, )
      Help text or description for the component.


    id (, str, )
      Unique ID of the component instance.


    identifier (, str, )
      Identifier for the component.


    instances (, int, )
      Number of instances of this component.


    ip (, str, )
      IP address assigned to the component.


    manageFirmware (, bool, )
      Indicates whether firmware management is enabled for the component.


    managementIpAddress (, str, )
      Management IP address of the component.


    name (, str, )
      Name of the component (e.g., PowerFlex Cluster).


    osPuppetCertName (, str, )
      Puppet certificate name for the OS instance.


    puppetCertName (, str, )
      Puppet certificate name for the component.


    refId (, str, )
      Reference ID of the component.


    resources (, list, )
      List of resources associated with the component.


    serialNumber (, str, )
      Serial number of the component.


    subType (, str, )
      Subtype of the component (e.g., STORAGEONLY).


    teardown (, bool, )
      Indicates whether the component should be torn down.


    type (, str, )
      Type of the component (e.g., SCALEIO).



  configuration (, str, )
    Full configuration data of the service template.


  createdBy (, str, )
    User who created the service template.


  createdDate (, str, )
    Timestamp when the template was created.


  draft (, bool, )
    Indicates whether the template is a draft.


  firmwareRepository (, str, )
    Firmware repository used by the template.


  hideTemplateActive (, bool, )
    Indicates whether the template is hidden from users.


  id (, str, )
    Unique identifier of the service template.


  inConfiguration (, bool, )
    Indicates whether the template is currently being configured.


  lastDeployedDate (, str, )
    Timestamp when the template was last deployed.


  licenseRepository (, str, )
    License repository used by the template.


  manageFirmware (, bool, )
    Indicates whether firmware management is enabled for the template.


  networks (, list, )
    List of network configurations defined in the template.


    description (, str, )
      Description of the network.


    destinationIpAddress (, str, )
      Destination IP address range for the network.


    id (, str, )
      Unique ID of the network.


    name (, str, )
      Name of the network (e.g., flex-data1).


    static (, bool, )
      Indicates whether the network uses static configuration.


    staticNetworkConfiguration (, dict, )
      Static network settings for the network.


      dnsSuffix (, str, )
        DNS suffix for the network.


      gateway (, str, )
        Gateway IP address.


      ipAddress (, str, )
        Assigned IP address.


      ipRange (, str, )
        Range of IP addresses.


      primaryDns (, str, )
        Primary DNS server IP.


      secondaryDns (, str, )
        Secondary DNS server IP.


      staticRoute (, str, )
        Static routing configuration.


      subnet (, str, )
        Subnet mask in dotted-decimal format.



    type (, str, )
      Type of the network (e.g., SCALEIO\_DATA).


    vlanId (, int, )
      VLAN ID associated with the network.



  originalTemplateId (, str, )
    ID of the original template from which this was derived.


  sdnasCount (, int, )
    Number of SDNAS instances in the template.


  serviceCount (, int, )
    Number of services defined in the template.


  storageCount (, int, )
    Number of storage components in the template.


  switchCount (, int, )
    Number of switch components in the template.


  templateLocked (, bool, )
    Indicates whether the template is locked for editing.


  templateValid (, dict, )
    Validation status of the entire template.


    messages (, list, )
      List of validation messages.


    valid (, bool, )
      Indicates whether the template is valid.



  updatedBy (, str, )
    User who last updated the template.


  updatedDate (, str, )
    Timestamp when the template was last updated.


  useDefaultCatalog (, bool, )
    Indicates whether the default firmware catalog is used.


  vmCount (, int, )
    Number of virtual machines defined in the template.



FirmwareRepository (when I(gather_subset) is C(firmware_repository), list, [{'bundleCount': 54, 'componentCount': 2783, 'createdBy': 'admin', 'createdDate': '2025-08-26T06:46:30.994+00:00', 'custom': False, 'defaultCatalog': True, 'deployments': [], 'diskLocation': 'https://xxxx', 'downloadProgress': 100, 'downloadStatus': 'available', 'esxiOSRepository': None, 'esxiSoftwareBundle': None, 'esxiSoftwareComponent': None, 'extractProgress': 100, 'fileSizeInGigabytes': 21.7, 'filename': 'catalog.xml', 'id': '8aaa80a998e515080198e520d5520000', 'jobId': 'Job-a3129599-9702-4abc-b041-0724b82087bc', 'md5Hash': None, 'minimal': False, 'name': 'Intelligent Catalog 50.390.00', 'needsAttention': False, 'password': None, 'rcmapproved': False, 'signature': 'Signed', 'signedKeySourceLocation': None, 'softwareBundles': [], 'softwareComponents': [], 'sourceLocation': 'https://xxx.zip', 'sourceType': 'FILE', 'state': 'available', 'updatedBy': 'system', 'updatedDate': '2025-09-03T05:52:58.636+00:00', 'userBundleCount': 0, 'username': ''}])
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


  bundleCount (, int, )
    Total number of bundles in the firmware repository.


  componentCount (, int, )
    Total number of software components in the firmware repository.


  createdBy (, str, )
    User who created the firmware repository.


  createdDate (, str, )
    Timestamp when the firmware repository was created.


  custom (, bool, )
    Indicates whether the firmware repository is a custom catalog.


  defaultCatalog (, bool, )
    Indicates whether this is the default firmware catalog.


  diskLocation (, str, )
    Disk path or URL where the firmware repository is stored.


  downloadProgress (, int, )
    Progress percentage of the download process.


  downloadStatus (, str, )
    Current status of the download (e.g., available).


  esxiOSRepository (, str, )
    ESXi operating system repository, if applicable.


  esxiSoftwareBundle (, str, )
    ESXi software bundle included in the repository.


  esxiSoftwareComponent (, str, )
    ESXi software component included in the repository.


  extractProgress (, int, )
    Progress percentage of the extraction process.


  fileSizeInGigabytes (, float, )
    Size of the firmware repository in gigabytes.


  filename (, str, )
    Name of the catalog file (e.g., catalog.xml).


  jobId (, str, )
    Job ID associated with the firmware repository creation or update.


  md5Hash (, str, )
    MD5 hash of the firmware repository file.


  minimal (, bool, )
    Indicates whether the repository is a minimal catalog.


  needsAttention (, bool, )
    Indicates whether the repository requires user attention.


  password (, str, )
    Password used to access the source location, if applicable.


  rcmapproved (, bool, )
    Indicates whether the repository is RCM (Recommended Configuration Management) approved.


  signature (, str, )
    Signature status of the catalog (e.g., Signed).


  signedKeySourceLocation (, str, )
    Source location of the signed key for catalog verification.


  sourceType (, str, )
    Type of source (e.g., FILE).


  updatedBy (, str, )
    User who last updated the firmware repository.


  updatedDate (, str, )
    Timestamp when the firmware repository was last updated.


  userBundleCount (, int, )
    Number of user-defined bundles in the repository.


  username (, str, )
    Username used to access the source location.



NVMe_Hosts (always, list, [{'hostOsFullType': 'Generic', 'hostType': 'NVMeHost', 'id': 'fdc0ed2b00010000', 'installedSoftwareVersionInfo': None, 'kernelBuildNumber': None, 'kernelVersion': None, 'links': [{'href': '/api/instances/Host::fdc0ed2b00010000', 'rel': 'self'}], 'maxNumPaths': 4, 'maxNumSysPorts': 10, 'mdmConnectionState': None, 'mdmIpAddressesCurrent': None, 'memoryAllocationFailure': None, 'name': 'nvme_host', 'nqn': 'nqn.2014-08.org.nvmexpress:uuid:e6e80a42-b1d3-5ec2-5ba6-d46d4df291234', 'osType': None, 'peerMdmId': None, 'perfProfile': None, 'sdcAgentActive': None, 'sdcApproved': None, 'sdcApprovedIps': None, 'sdcGuid': None, 'sdcIp': None, 'sdcIps': None, 'sdcType': None, 'sdrId': None, 'sdtId': None, 'socketAllocationFailure': None, 'softwareVersionInfo': None, 'systemId': '815945c41cd8460f', 'versionInfo': None}])
  Details of all NVMe hosts.


  hostOsFullType (, str, )
    Full type of the host OS.


  hostType (, str, )
    Type of the host.


  id (, str, )
    ID of the NVMe host.


  installedSoftwareVersionInfo (, str, )
    Installed software version information.


  kernelBuildNumber (, str, )
    Kernel build number.


  kernelVersion (, str, )
    Kernel version.


  links (, list, )
    Links related to the NVMe host.


    href (, str, )
      Hyperlink reference.


    rel (, str, )
      Relation type.



  max_num_paths (, int, )
    Maximum number of paths per volume. Used to create or modify the NVMe host.


  max_num_sys_ports (, int, )
    Maximum number of ports per protection domain. Used to create or modify the NVMe host.


  mdmConnectionState (, str, )
    MDM connection state.


  mdmIpAddressesCurrent (, list, )
    Current MDM IP addresses.


  memoryAllocationFailure (, str, )
    Memory allocation failure status.


  name (, str, )
    Name of the NVMe host.


  nqn (, str, )
    NQN of the NVMe host. Used to create, get or modify the NVMe host.


  osType (, str, )
    OS type.


  peerMdmId (, str, )
    Peer MDM ID.


  perfProfile (, str, )
    Performance profile.


  sdcAgentActive (, bool, )
    Whether the SDC agent is active.


  sdcApproved (, bool, )
    Whether an SDC has approved access to the system.


  sdcApprovedIps (, list, )
    SDC approved IPs.


  sdcGuid (, str, )
    SDC GUID.


  sdcIp (, str, )
    SDC IP address.


  sdcIps (, list, )
    SDC IP addresses.


  sdcType (, str, )
    SDC type.


  sdrId (, str, )
    SDR ID.


  sdtId (, str, )
    SDT ID.


  socketAllocationFailure (, str, )
    Socket allocation failure status.


  softwareVersionInfo (, str, )
    Software version information.


  systemId (, str, )
    ID of the system.


  versionInfo (, str, )
    Version information.



sdt (when I(gather_subset) is C(sdt), list, [{'authenticationError': 'None', 'certificateInfo': {'issuer': '/GN=MDM/CN=CA-db69bee9dc6c0d0f/L=Hopkinton/ST=Massachusetts/C=US/O=EMC/OU=ASD', 'subject': '/GN=sdt-comp-1/CN=pie104074/L=Hopkinton/ST=Massachusetts/C=US/O=EMC/OU=ASD', 'thumbprint': '51:5E:FB:ED:91:43:54:8C:46:C3:60:ED:AD:0A:60:5E:90:3E:30:2D', 'validFrom': 'Sep  8 15:37:05 2025 GMT', 'validFromAsn1Format': '250908153705Z', 'validTo': 'Sep  7 16:37:05 2035 GMT', 'validToAsn1Format': '350907163705Z'}, 'discoveryPort': 8009, 'faultSetId': None, 'id': '19b7d6c700000001', 'ipList': [{'ip': '10.2.3.4', 'role': 'StorageAndHost'}, {'ip': '10.1.2.3', 'role': 'StorageAndHost'}], 'links': [{'href': '/api/instances/Sdt::19b7d6c700000001', 'rel': 'self'}], 'maintenanceState': 'NoMaintenance', 'mdmConnectionState': 'Connected', 'membershipState': 'Joined', 'name': 'sdt_pie104074.pie.lab.emc.com', 'nvmePort': 4420, 'nvme_hosts': [], 'persistentDiscoveryControllersNum': 0, 'protectionDomainId': '19af22f800000000', 'sdtState': 'Normal', 'softwareVersionInfo': 'R5_0.0.0', 'storagePort': 12200, 'systemId': 'db69bee9dc6c0d0f'}])
  Details of NVMe storage data targets.


  authenticationError (, str, )
    The authentication error details of the SDT object.


  certificateInfo (, dict, )
    The certificate information of the SDT object.


    issuer (, str, )
      The issuer of the certificate.


    subject (, str, )
      The subject of the certificate.


    thumbprint (, str, )
      The thumbprint of the certificate.


    validFrom (, str, )
      The date from which the certificate is valid.


    validFromAsn1Format (, str, )
      The validity start date in ASN.1 format.


    validTo (, str, )
      The date until which the certificate is valid.


    validToAsn1Format (, str, )
      The validity end date in ASN.1 format.



  discoveryPort (, int, )
    The discovery port number of the SDT object.


  faultSetId (, str, )
    The fault set ID associated with the SDT object.


  id (, str, )
    The unique identifier of the SDT object.


  ipList (, list, )
    The list of IP addresses of the SDT object.


    ip (, str, )
      The IP address of the SDT object.


    role (, str, )
      The role associated with the IP address of the SDT object.



  links (, list, )
    Hyperlinks related to the SDT object.


    href (, str, )
      The URL of the link.


    rel (, str, )
      The relation type of the link.



  maintenanceState (, str, )
    The maintenance state of the SDT object.


  mdmConnectionState (, str, )
    The MDM connection state of the SDT object.


  membershipState (, str, )
    The membership state of the SDT object.


  name (, str, )
    The name of the SDT object.


  nvmePort (, int, )
    The NVMe port number of the SDT object.


  nvme_hosts (, list, )
    The list of NVMe hosts associated with the SDT object.


    controllerId (, int, )
      The controller ID.


    hostId (, str, )
      The host ID associated with the NVMe controller.


    hostIp (, str, )
      The IP address of the host.


    id (, str, )
      The unique identifier of the NVMe controller.


    isAssigned (, bool, )
      Indicates if the NVMe controller is assigned.


    isConnected (, bool, )
      Indicates if the NVMe controller is connected.


    links (, list, )
      Hyperlinks related to the NVMe controller.


      href (, str, )
        The URL of the link.


      rel (, str, )
        The relation type of the link.



    name (, str, )
      The name of the NVMe controller. Can be null.


    sdtId (, str, )
      The SDT ID associated with the NVMe controller.


    subsystem (, str, )
      The subsystem associated with the NVMe controller.


    sysPortId (, int, )
      The system port ID.


    sysPortIp (, str, )
      The IP address of the system port.



  persistentDiscoveryControllersNum (, int, )
    Number of persistent discovery controllers.


  protectionDomainId (, str, )
    The Protection Domain ID associated with the SDT object.


  sdtState (, str, )
    The state of the SDT object.


  softwareVersionInfo (, str, )
    The software version information of the SDT object.


  storagePort (, int, )
    The storage port number of the SDT object.


  systemId (, str, )
    ID of the system.






Status
------





Authors
~~~~~~~

- Tao He (@taohe1012) <ansible.team@dell.com>

