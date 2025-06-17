.. _protection_domain_module:


protection_domain -- Manage Protection Domain on Dell PowerFlex
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing Protection Domain on PowerFlex storage system includes creating, modifying attributes, deleting and getting details of Protection Domain.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  protection_domain_name (optional, str, None)
    The name of the protection domain.

    Mandatory for create operation.

    It is unique across the PowerFlex array.

    Mutually exclusive with \ :emphasis:`protection\_domain\_id`\ .


  protection_domain_id (optional, str, None)
    The ID of the protection domain.

    Except for create operation, all other operations can be performed using protection\_domain\_id.

    Mutually exclusive with \ :emphasis:`protection\_domain\_name`\ .


  protection_domain_new_name (optional, str, None)
    Used to rename the protection domain.


  is_active (optional, bool, None)
    Used to activate or deactivate the protection domain.


  network_limits (optional, dict, None)
    Network bandwidth limit used by all SDS in protection domain.


    rebuild_limit (optional, int, None)
      Limit the network bandwidth for rebuild.


    rebalance_limit (optional, int, None)
      Limit the network bandwidth for rebalance.


    vtree_migration_limit (optional, int, None)
      Limit the network bandwidth for vtree migration.


    overall_limit (optional, int, None)
      Limit the overall network bandwidth.


    bandwidth_unit (optional, str, KBps)
      Unit for network bandwidth limits.



  rf_cache_limits (optional, dict, None)
    Used to set the RFcache parameters of the protection domain.


    is_enabled (optional, bool, None)
      Used to enable or disable RFcache in the protection domain.


    page_size (optional, int, None)
      Used to set the cache page size in KB.


    max_io_limit (optional, int, None)
      Used to set cache maximum I/O limit in KB.


    pass_through_mode (optional, str, None)
      Used to set the cache mode.



  state (True, str, None)
    State of the protection domain.


  hostname (True, str, None)
    IP or FQDN of the PowerFlex host.


  username (True, str, None)
    The username of the PowerFlex host.


  password (True, str, None)
    The password of the PowerFlex host.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    \ :literal:`true`\  - Indicates that the SSL certificate should be verified.

    \ :literal:`false`\  - Indicates that the SSL certificate should not be verified.


  port (optional, int, 443)
    Port number through which communication happens with PowerFlex host.


  timeout (False, int, 120)
    Time after which connection will get terminated.

    It is to be mentioned in seconds.





Notes
-----

.. note::
   - The protection domain can only be deleted if all its related objects have been dissociated from the protection domain.
   - If the protection domain set to inactive, then no operation can be performed on protection domain.
   - The \ :emphasis:`check\_mode`\  is not supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create protection domain
      dellemc.powerflex.protection_domain:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1"
        state: "present"

    - name: Create protection domain with all parameters
      dellemc.powerflex.protection_domain:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1"
        is_active: true
        network_limits:
          rebuild_limit: 10
          rebalance_limit: 17
          vtree_migration_limit: 14
          overall_limit: 20
          bandwidth_unit: "MBps"
        rf_cache_limits:
          is_enabled: true
          page_size: 16
          max_io_limit: 128
          pass_through_mode: "Read"
        state: "present"

    - name: Get protection domain details using name
      dellemc.powerflex.protection_domain:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1"
        state: "present"

    - name: Get protection domain details using ID
      dellemc.powerflex.protection_domain:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_id: "5718253c00000004"
        state: "present"

    - name: Modify protection domain attributes
      dellemc.powerflex.protection_domain:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1"
        protection_domain_new_name: "domain1_new"
        network_limits:
          rebuild_limit: 14
          rebalance_limit: 20
          overall_limit: 25
          bandwidth_unit: "MBps"
        rf_cache_limits:
          page_size: 64
          pass_through_mode: "WriteMiss"
        state: "present"

    - name: Delete protection domain using name
      dellemc.powerflex.protection_domain:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1_new"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


protection_domain_details (When protection domain exists, dict, {'fglDefaultMetadataCacheSize': 0, 'fglDefaultNumConcurrentWrites': 1000, 'fglMetadataCacheEnabled': False, 'id': '7bd6457000000000', 'links': [{'href': '/api/instances/ProtectionDomain::7bd6457000000000', 'rel': 'self'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/Statistics', 'rel': '/api/ProtectionDomain/relationship/Statistics'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/Sdr', 'rel': '/api/ProtectionDomain/relationship/Sdr'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/AccelerationPool', 'rel': '/api/ProtectionDomain/relationship/AccelerationPool'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/StoragePool', 'rel': '/api/ProtectionDomain/relationship/StoragePool'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/Sds', 'rel': '/api/ProtectionDomain/relationship/Sds'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/ReplicationConsistencyGroup', 'rel': '/api/ProtectionDomain/relationship/ ReplicationConsistencyGroup'}, {'href': '/api/instances/ProtectionDomain::7bd6457000000000/ relationships/FaultSet', 'rel': '/api/ProtectionDomain/relationship/FaultSet'}, {'href': '/api/instances/System::0989ce79058f150f', 'rel': '/api/parent/relationship/systemId'}], 'mdmSdsNetworkDisconnectionsCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'name': 'domain1', 'overallIoNetworkThrottlingEnabled': False, 'overallIoNetworkThrottlingInKbps': None, 'protectedMaintenanceModeNetworkThrottlingEnabled': False, 'protectedMaintenanceModeNetworkThrottlingInKbps': None, 'protectionDomainState': 'Active', 'rebalanceNetworkThrottlingEnabled': False, 'rebalanceNetworkThrottlingInKbps': None, 'rebuildNetworkThrottlingEnabled': False, 'rebuildNetworkThrottlingInKbps': None, 'rfcacheAccpId': None, 'rfcacheEnabled': True, 'rfcacheMaxIoSizeKb': 128, 'rfcacheOpertionalMode': 'WriteMiss', 'rfcachePageSizeKb': 64, 'sdrSdsConnectivityInfo': {'clientServerConnStatus': 'CLIENT_SERVER_CONN_STATUS_ALL _CONNECTED', 'disconnectedClientId': None, 'disconnectedClientName': None, 'disconnectedServerId': None, 'disconnectedServerIp': None, 'disconnectedServerName': None}, 'sdsConfigurationFailureCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'sdsDecoupledCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'sdsReceiveBufferAllocationFailuresCounterParameters': {'longWindow': {'threshold': 2000000, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 200000, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 20000, 'windowSizeInSec': 60}}, 'sdsSdsNetworkDisconnectionsCounterParameters': {'longWindow': {'threshold': 700, 'windowSizeInSec': 86400}, 'mediumWindow': {'threshold': 500, 'windowSizeInSec': 3600}, 'shortWindow': {'threshold': 300, 'windowSizeInSec': 60}}, 'storagePool': [{'id': '8d1cba1700000000', 'name': 'pool1'}], 'systemId': '0989ce79058f150f', 'vtreeMigrationNetworkThrottlingEnabled': False, 'vtreeMigrationNetworkThrottlingInKbps': None})
  Details of the protection domain.


  fglDefaultMetadataCacheSize (, int, )
    FGL metadata cache size.


  fglDefaultNumConcurrentWrites (, str, )
    FGL concurrent writes.


  fglMetadataCacheEnabled (, bool, )
    Whether FGL cache enabled.


  id (, str, )
    Protection domain ID.


  links (, list, )
    Protection domain links.


    href (, str, )
      Protection domain instance URL.


    rel (, str, )
      Protection domain's relationship with different entities.



  mdmSdsNetworkDisconnectionsCounterParameters (, dict, )
    MDM's SDS counter parameter.


    longWindow (, int, )
      Long window for Counter Parameters.


    mediumWindow (, int, )
      Medium window for Counter Parameters.


    shortWindow (, int, )
      Short window for Counter Parameters.



  name (, str, )
    Name of the protection domain.


  overallIoNetworkThrottlingEnabled (, bool, )
    Whether overall network throttling enabled.


  overallIoNetworkThrottlingInKbps (, int, )
    Overall network throttling in KBps.


  protectedMaintenanceModeNetworkThrottlingEnabled (, bool, )
    Whether protected maintenance mode network throttling enabled.


  protectedMaintenanceModeNetworkThrottlingInKbps (, int, )
    Protected maintenance mode network throttling in KBps.


  protectionDomainState (, int, )
    State of protection domain.


  rebalanceNetworkThrottlingEnabled (, int, )
    Whether rebalance network throttling enabled.


  rebalanceNetworkThrottlingInKbps (, int, )
    Rebalance network throttling in KBps.


  rebuildNetworkThrottlingEnabled (, int, )
    Whether rebuild network throttling enabled.


  rebuildNetworkThrottlingInKbps (, int, )
    Rebuild network throttling in KBps.


  rfcacheAccpId (, str, )
    Id of RF cache acceleration pool.


  rfcacheEnabled (, bool, )
    Whether RF cache is enabled or not.


  rfcacheMaxIoSizeKb (, int, )
    RF cache maximum I/O size in KB.


  rfcacheOpertionalMode (, str, )
    RF cache operational mode.


  rfcachePageSizeKb (, bool, )
    RF cache page size in KB.


  sdrSdsConnectivityInfo (, dict, )
    Connectivity info of SDR and SDS.


    clientServerConnStatus (, str, )
      Connectivity status of client and server.


    disconnectedClientId (, str, )
      Disconnected client ID.


    disconnectedClientName (, str, )
      Disconnected client name.


    disconnectedServerId (, str, )
      Disconnected server ID.


    disconnectedServerIp (, str, )
      Disconnected server IP.


    disconnectedServerName (, str, )
      Disconnected server name.



  sdsSdsNetworkDisconnectionsCounterParameters (, dict, )
    Counter parameter for SDS-SDS network.


    longWindow (, int, )
      Long window for Counter Parameters.


    mediumWindow (, int, )
      Medium window for Counter Parameters.


    shortWindow (, int, )
      Short window for Counter Parameters.



  storagePool (, list, )
    List of storage pools.


  systemId (, str, )
    ID of system.


  vtreeMigrationNetworkThrottlingEnabled (, bool, )
    Whether V-Tree migration network throttling enabled.


  vtreeMigrationNetworkThrottlingInKbps (, int, )
    V-Tree migration network throttling in KBps.






Status
------





Authors
~~~~~~~

- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

