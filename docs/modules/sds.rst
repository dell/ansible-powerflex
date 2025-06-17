.. _sds_module:


sds -- Manage SDS on Dell PowerFlex
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SDS on PowerFlex storage system includes creating new SDS, getting details of SDS, adding/removing IP to/from SDS, modifying attributes of SDS, and deleting SDS.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  sds_name (optional, str, None)
    The name of the SDS.

    Mandatory for create operation.

    It is unique across the PowerFlex array.

    Mutually exclusive with \ :emphasis:`sds\_id`\ .


  sds_id (optional, str, None)
    The ID of the SDS.

    Except create operation, all other operations can be performed using \ :emphasis:`sds\_id`\ .

    Mutually exclusive with \ :emphasis:`sds\_name`\ .


  protection_domain_name (optional, str, None)
    The name of the protection domain.

    Mutually exclusive with \ :emphasis:`protection\_domain\_id`\ .


  protection_domain_id (optional, str, None)
    The ID of the protection domain.

    Mutually exclusive with \ :emphasis:`protection\_domain\_name`\ .


  sds_ip_list (optional, list, None)
    Dictionary of IPs and their roles for the SDS.

    At least one IP-role is mandatory while creating a SDS.

    IP-roles can be updated as well.


    ip (True, str, None)
      IP address of the SDS.


    role (True, str, None)
      Role assigned to the SDS IP address.



  sds_ip_state (optional, str, None)
    State of IP with respect to the SDS.


  rfcache_enabled (optional, bool, None)
    Whether to enable the Read Flash cache.


  rmcache_enabled (optional, bool, None)
    Whether to enable the Read RAM cache.


  rmcache_size (optional, int, None)
    Read RAM cache size (in MB).

    Minimum size is 128 MB.

    Maximum size is 3911 MB.


  sds_new_name (optional, str, None)
    SDS new name.


  performance_profile (optional, str, None)
    Performance profile to apply to the SDS.

    The HighPerformance profile configures a predefined set of parameters for very high performance use cases.

    Default value by API is \ :literal:`HighPerformance`\ .


  fault_set_name (optional, str, None)
    Name of the fault set.

    Mutually exclusive with \ :emphasis:`fault\_set\_id`\ .


  fault_set_id (optional, str, None)
    Unique identifier of the fault set.

    Mutually exclusive with \ :emphasis:`fault\_set\_name`\ .


  state (True, str, None)
    State of the SDS.


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
   - The maximum limit for the IPs that can be associated with an SDS is 8.
   - There needs to be at least 1 IP for SDS communication and 1 for SDC communication.
   - If only 1 IP exists, it must be with role 'all'; else 1 IP can be with role 'all'and other IPs with role 'sdcOnly'; or 1 IP must be with role 'sdsOnly' and others with role 'sdcOnly'.
   - There can be 1 or more IPs with role 'sdcOnly'.
   - There must be only 1 IP with SDS role (either with role 'all' or 'sdsOnly').
   - SDS can be created with RF cache disabled, but, be aware that the RF cache is not always updated. In this case, the user should re-try the operation.
   - The \ :emphasis:`check\_mode`\  is supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create SDS
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node0"
        protection_domain_name: "domain1"
        sds_ip_list:
          - ip: "198.10.xxx.xxx"
            role: "all"
        sds_ip_state: "present-in-sds"
        state: "present"

    - name: Create SDS with all parameters
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node1"
        protection_domain_name: "domain1"
        fault_set_name: "faultset1"
        sds_ip_list:
          - ip: "198.10.xxx.xxx"
            role: "sdcOnly"
        sds_ip_state: "present-in-sds"
        rmcache_enabled: true
        rmcache_size: 128
        performance_profile: "HighPerformance"
        state: "present"

    - name: Get SDS details using name
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node0"
        state: "present"

    - name: Get SDS details using ID
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_id: "5718253c00000004"
        state: "present"

    - name: Modify SDS attributes using name
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node0"
        sds_new_name: "node0_new"
        rfcache_enabled: true
        rmcache_enabled: true
        rmcache_size: 256
        performance_profile: "HighPerformance"
        state: "present"

    - name: Modify SDS attributes using ID
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_id: "5718253c00000004"
        sds_new_name: "node0_new"
        rfcache_enabled: true
        rmcache_enabled: true
        rmcache_size: 256
        performance_profile: "HighPerformance"
        state: "present"

    - name: Add IP and role to an SDS
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node0"
        sds_ip_list:
          - ip: "198.10.xxx.xxx"
            role: "sdcOnly"
        sds_ip_state: "present-in-sds"
        state: "present"

    - name: Remove IP and role from an SDS
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node0"
        sds_ip_list:
          - ip: "198.10.xxx.xxx"
            role: "sdcOnly"
        sds_ip_state: "absent-in-sds"
        state: "present"

    - name: Delete SDS using name
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_name: "node0"
        state: "absent"

    - name: Delete SDS using ID
      dellemc.powerflex.sds:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        sds_id: "5718253c00000004"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


sds_details (When SDS exists, dict, {'authenticationError': 'None', 'certificateInfo': None, 'configuredDrlMode': 'Volatile', 'drlMode': 'Volatile', 'faultSetId': None, 'fglMetadataCacheSize': 0, 'fglMetadataCacheState': 'Disabled', 'fglNumConcurrentWrites': 1000, 'id': '8f3bb0cc00000002', 'ipList': [{'ip': '10.47.xxx.xxx', 'role': 'all'}], 'lastUpgradeTime': 0, 'links': [{'href': '/api/instances/Sds::8f3bb0cc00000002', 'rel': 'self'}, {'href': '/api/instances/Sds::8f3bb0cc00000002/relationships /Statistics', 'rel': '/api/Sds/relationship/Statistics'}, {'href': '/api/instances/Sds::8f3bb0cc00000002/relationships /SpSds', 'rel': '/api/Sds/relationship/SpSds'}, {'href': '/api/instances/Sds::8f3bb0cc00000002/relationships /Device', 'rel': '/api/Sds/relationship/Device'}, {'href': '/api/instances/ProtectionDomain::9300c1f900000000', 'rel': '/api/parent/relationship/protectionDomainId'}], 'maintenanceState': 'NoMaintenance', 'maintenanceType': 'NoMaintenance', 'mdmConnectionState': 'Connected', 'membershipState': 'Joined', 'name': 'node0', 'numOfIoBuffers': None, 'numRestarts': 2, 'onVmWare': True, 'perfProfile': 'HighPerformance', 'port': 7072, 'protectionDomainId': '9300c1f900000000', 'protectionDomainName': 'domain1', 'raidControllers': None, 'rfcacheEnabled': True, 'rfcacheErrorApiVersionMismatch': False, 'rfcacheErrorDeviceDoesNotExist': False, 'rfcacheErrorInconsistentCacheConfiguration': False, 'rfcacheErrorInconsistentSourceConfiguration': False, 'rfcacheErrorInvalidDriverPath': False, 'rfcacheErrorLowResources': False, 'rmcacheEnabled': True, 'rmcacheFrozen': False, 'rmcacheMemoryAllocationState': 'AllocationPending', 'rmcacheSizeInKb': 131072, 'rmcacheSizeInMb': 128, 'sdsConfigurationFailure': None, 'sdsDecoupled': None, 'sdsReceiveBufferAllocationFailures': None, 'sdsState': 'Normal', 'softwareVersionInfo': 'R3_6.0.0'})
  Details of the SDS.


  authenticationError (, str, )
    Indicates authentication error.


  certificateInfo (, str, )
    Information about certificate.


  configuredDrlMode (, str, )
    Configured DRL mode.


  drlMode (, str, )
    DRL mode.


  faultSetId (, str, )
    Fault set ID.


  fglMetadataCacheSize (, int, )
    FGL metadata cache size.


  fglMetadataCacheState (, str, )
    FGL metadata cache state.


  fglNumConcurrentWrites (, int, )
    FGL concurrent writes.


  id (, str, )
    SDS ID.


  ipList (, list, )
    SDS IP list.


    ip (, str, )
      IP present in the SDS.


    role (, str, )
      Role of the SDS IP.



  lastUpgradeTime (, str, )
    Last time SDS was upgraded.


  links (, list, )
    SDS links.


    href (, str, )
      SDS instance URL.


    rel (, str, )
      SDS's relationship with different entities.



  maintenanceState (, str, )
    Maintenance state.


  maintenanceType (, str, )
    Maintenance type.


  mdmConnectionState (, str, )
    MDM connection state.


  membershipState (, str, )
    Membership state.


  name (, str, )
    Name of the SDS.


  numOfIoBuffers (, int, )
    Number of IO buffers.


  numRestarts (, int, )
    Number of restarts.


  onVmWare (, bool, )
    Presence on VMware.


  perfProfile (, str, )
    Performance profile.


  port (, int, )
    SDS port.


  protectionDomainId (, str, )
    Protection Domain ID.


  protectionDomainName (, str, )
    Protection Domain Name.


  raidControllers (, int, )
    Number of RAID controllers.


  rfcacheEnabled (, bool, )
    Whether RF cache is enabled or not.


  rfcacheErrorApiVersionMismatch (, bool, )
    RF cache error for API version mismatch.


  rfcacheErrorDeviceDoesNotExist (, bool, )
    RF cache error for device does not exist.


  rfcacheErrorInconsistentCacheConfiguration (, bool, )
    RF cache error for inconsistent cache configuration.


  rfcacheErrorInconsistentSourceConfiguration (, bool, )
    RF cache error for inconsistent source configuration.


  rfcacheErrorInvalidDriverPath (, bool, )
    RF cache error for invalid driver path.


  rfcacheErrorLowResources (, bool, )
    RF cache error for low resources.


  rmcacheEnabled (, bool, )
    Whether Read RAM cache is enabled or not.


  rmcacheFrozen (, bool, )
    RM cache frozen.


  rmcacheMemoryAllocationState (, bool, )
    RM cache memory allocation state.


  rmcacheSizeInKb (, int, )
    RM cache size in KB.


  rmcacheSizeInMb (, int, )
    RM cache size in MB.


  sdsConfigurationFailure (, str, )
    SDS configuration failure.


  sdsDecoupled (, str, )
    SDS decoupled.


  sdsReceiveBufferAllocationFailures (, str, )
    SDS receive buffer allocation failures.


  sdsState (, str, )
    SDS state.


  softwareVersionInfo (, str, )
    SDS software version information.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

