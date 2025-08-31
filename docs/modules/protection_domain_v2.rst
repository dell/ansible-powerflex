.. _protection_domain_v2_module:


protection_domain_v2 -- Managing protection domain on Dell PowerFlex 5.x
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Dell PowerFlex protection domain module includes getting the details of protection domain, creating a new protection domain, and modifying the attribute of a protection domain.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

  protection_domain_name (optional, str, None)
    The name of the protection domain.

    Mandatory for create operation.

    It is unique across the PowerFlex array.

    Mutually exclusive with :emphasis:`protection\_domain\_id`.


  protection_domain_id (optional, str, None)
    The ID of the protection domain.

    Except for create operation, all other operations can be performed using protection\_domain\_id.

    Mutually exclusive with :emphasis:`protection\_domain\_name`.


  protection_domain_new_name (optional, str, None)
    Used to rename the protection domain.


  is_active (False, str, None)
    Used to indicate the state of the protection domain and to activate or deactivate it.


  state (True, str, None)
    The state of the protection domain. Can be 'present' or 'absent'.


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
   - This module is supported on Dell PowerFlex 5.x and later versions.
   - The protection domain can only be deleted if all its related objects have been dissociated from the protection domain.
   - If the protection domain set to inactive, then no operation can be performed on protection domain.
   - The :emphasis:`check\_mode` is not supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create protection domain
      dellemc.powerflex.protection_domain_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        protection_domain_name: "domain1"
        state: "present"

    - name: Create protection domain with all parameters
      dellemc.powerflex.protection_domain_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        protection_domain_name: "domain1"
        is_active: True
        state: present

    - name: Get protection domain details using name
      dellemc.powerflex.protection_domain_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1"
        state: "present"

    - name: Get protection domain details using ID
      dellemc.powerflex.protection_domain_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_id: "5718253c00000004"
        state: "present"

    - name: Modify protection domain attributes
      dellemc.powerflex.protection_domain_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        protection_domain_name: "domain1"
        protection_domain_new_name: "domain1_new"
        state: "present"

    - name: Delete protection domain using name
      dellemc.powerflex.protection_domain_v2:
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


protection_domain_details (When protection domain exists, dict, {'genType': 'EC', 'rebuildNetworkThrottlingEnabled': False, 'rebalanceNetworkThrottlingEnabled': False, 'vtreeMigrationNetworkThrottlingEnabled': False, 'overallIoNetworkThrottlingEnabled': False, 'rfcacheEnabled': True, 'rfcacheAccpId': None, 'rebuildEnabled': True, 'rebalanceEnabled': True, 'name': 'domain1', 'systemId': '815945c41cd8460f', 'sdrSdsConnectivityInfo': {'clientServerConnStatus': 'CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED', 'disconnectedClientId': None, 'disconnectedClientName': None, 'disconnectedServerId': None, 'disconnectedServerName': None, 'disconnectedServerIp': None}, 'rplCapAlertLevel': 'invalid', 'protectionDomainState': 'Active', 'rebalanceNetworkThrottlingInKbps': None, 'rebuildNetworkThrottlingInKbps': None, 'overallIoNetworkThrottlingInKbps': None, 'vtreeMigrationNetworkThrottlingInKbps': None, 'sdsDecoupledCounterParameters': {'shortWindow': {'windowSizeInSec': 60, 'threshold': 300}, 'mediumWindow': {'windowSizeInSec': 3600, 'threshold': 500}, 'longWindow': {'windowSizeInSec': 86400, 'threshold': 700}}, 'sdsConfigurationFailureCounterParameters': {'shortWindow': {'windowSizeInSec': 60, 'threshold': 300}, 'mediumWindow': {'windowSizeInSec': 3600, 'threshold': 500}, 'longWindow': {'windowSizeInSec': 86400, 'threshold': 700}}, 'mdmSdsNetworkDisconnectionsCounterParameters': {'shortWindow': {'windowSizeInSec': 60, 'threshold': 300}, 'mediumWindow': {'windowSizeInSec': 3600, 'threshold': 500}, 'longWindow': {'windowSizeInSec': 86400, 'threshold': 700}}, 'sdsSdsNetworkDisconnectionsCounterParameters': {'shortWindow': {'windowSizeInSec': 60, 'threshold': 300}, 'mediumWindow': {'windowSizeInSec': 3600, 'threshold': 500}, 'longWindow': {'windowSizeInSec': 86400, 'threshold': 700}}, 'rfcacheOpertionalMode': 'WriteMiss', 'rfcachePageSizeKb': 64, 'rfcacheMaxIoSizeKb': 128, 'sdsReceiveBufferAllocationFailuresCounterParameters': {'shortWindow': {'windowSizeInSec': 60, 'threshold': 20000}, 'mediumWindow': {'windowSizeInSec': 3600, 'threshold': 200000}, 'longWindow': {'windowSizeInSec': 86400, 'threshold': 2000000}}, 'fglDefaultNumConcurrentWrites': 1000, 'fglMetadataCacheEnabled': False, 'fglDefaultMetadataCacheSize': 0, 'protectedMaintenanceModeNetworkThrottlingEnabled': False, 'protectedMaintenanceModeNetworkThrottlingInKbps': None, 'sdtSdsConnectivityInfo': {'clientServerConnStatus': 'CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED', 'disconnectedClientId': None, 'disconnectedClientName': None, 'disconnectedServerId': None, 'disconnectedServerName': None, 'disconnectedServerIp': None}, 'overallConcurrentIoLimit': 4, 'bandwidthLimitOverallIos': 400, 'bandwidthLimitBgDevScanner': 10, 'bandwidthLimitSinglyImpactedRebuild': 400, 'bandwidthLimitDoublyImpactedRebuild': 400, 'bandwidthLimitRebalance': 40, 'bandwidthLimitOther': 10, 'bandwidthLimitNodeNetwork': 25, 'id': 'e59841fd00000002', 'links': [{'rel': 'self', 'href': '/api/instances/ProtectionDomain::e59841fd00000002'}, {'rel': '/dtapi/rest/v1/metrics/query', 'href': '/dtapi/rest/v1/metrics/query', 'body': {'resource_type': 'protection_domain', 'ids': ['e59841fd00000002']}}, {'rel': '/api/ProtectionDomain/relationship/Sdr', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/Sdr'}, {'rel': '/api/ProtectionDomain/relationship/Dgwt', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/Dgwt'}, {'rel': '/api/ProtectionDomain/relationship/AccelerationPool', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/AccelerationPool'}, {'rel': '/api/ProtectionDomain/relationship/Sdt', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/Sdt'}, {'rel': '/api/ProtectionDomain/relationship/StoragePool', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/StoragePool'}, {'rel': '/api/ProtectionDomain/relationship/Sds', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/Sds'}, {'rel': '/api/ProtectionDomain/relationship/ReplicationConsistencyGroup', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/ReplicationConsistencyGroup'}, {'rel': '/api/ProtectionDomain/relationship/DeviceGroup', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/DeviceGroup'}, {'rel': '/api/ProtectionDomain/relationship/FaultSet', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/FaultSet'}, {'rel': '/api/ProtectionDomain/relationship/StorageNode', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/StorageNode'}, {'rel': '/api/ProtectionDomain/relationship/Pds', 'href': '/api/instances/ProtectionDomain::e59841fd00000002/relationships/Pds'}, {'rel': '/api/parent/relationship/systemId', 'href': '/api/instances/System::815945c41cd8460f'}]})
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

- Luis Liu (@vangork) <ansible.team@dell.com>

