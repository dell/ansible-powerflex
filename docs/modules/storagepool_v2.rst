.. _storagepool_v2_module:


storagepool_v2 -- Managing storage pool on Dell PowerFlex 5.x
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Dell PowerFlex storage pool module includes getting the details of storage pool, creating a new storage pool, and modifying the attribute of a storage pool.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

  storage_pool_name (optional, str, None)
    The name of the storage pool.

    If more than one storage pool is found with the same name then protection domain id/name is required to perform the task.

    Mutually exclusive with :emphasis:`storage\_pool\_id`.


  storage_pool_id (optional, str, None)
    The id of the storage pool.

    It is auto generated, hence should not be provided during creation of a storage pool.

    Mutually exclusive with :emphasis:`storage\_pool\_name`.


  storage_pool_new_name (optional, str, None)
    New name for the storage pool can be provided.

    This parameter is used for renaming the storage pool.


  protection_domain_name (optional, str, None)
    The name of the protection domain.

    During creation of a pool, either protection domain name or id must be mentioned.

    Mutually exclusive with :emphasis:`protection\_domain\_id`.


  protection_domain_id (optional, str, None)
    The id of the protection domain.

    During creation of a pool, either protection domain name or id must be mentioned.

    Mutually exclusive with :emphasis:`protection\_domain\_name`.


  device_group_id (False, str, None)
    The ID of the device group.


  device_group_name (False, str, None)
    The name of the device group.


  cap_alert_thresholds (False, dict, None)
    The capacity alert thresholds.


    high_threshold (False, int, None)
      The high threshold.


    critical_threshold (False, int, None)
      The critical threshold.



  compression_method (False, str, None)
    The compression method.


  over_provisioning_factor (False, int, None)
    The over-provisioning factor.


  physical_size_gb (False, int, None)
    The physical size in GB.


  use_all_available_capacity (False, bool, None)
    Whether to use all available capacity for storage pool.


  protection_scheme (False, str, None)
    The protection scheme.


  state (True, str, None)
    The state of the storage pool. Can be 'present' or 'absent'.


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
   - The :emphasis:`check\_mode` is supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get the details of storage pool by name
      dellemc.powerflex.storagepool_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_pool_name: "sample_pool_name"
        protection_domain_name: "sample_protection_domain"
        state: "present"

    - name: Get the details of storage pool by id
      dellemc.powerflex.storagepool_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_pool_id: "abcd1234ab12r"
        state: "present"

    - name: Create a new Storage pool
      dellemc.powerflex.storagepool_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        storage_pool_name: "{{ pool_name }}"
        protection_domain_name: "{{ protection_domain_name }}"
        device_group_name: "{{ device_group_name }}"
        cap_alert_thresholds:
          high_threshold: 80
          critical_threshold: 90
        compression_method: Normal
        over_provisioning_factor: 2
        physical_size_gb: 100
        protection_scheme: TwoPlusTwo
        state: "present"

    - name: Modify a Storage pool by name
      dellemc.powerflex.storagepool_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        storage_pool_name: "{{ pool_name }}"
        protection_domain_name: "{{ protection_domain_name }}"
        storage_pool_new_name: "pool_name_new"
        cap_alert_thresholds:
          high_threshold: 85
          critical_threshold: 95
        compression_method: None
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


storage_pool_details (When storage pool exists, dict, {'addressSpaceUsage': 'Normal', 'addressSpaceUsageType': 'TypeHardLimit', 'backgroundScannerBWLimitKBps': None, 'backgroundScannerMode': None, 'bgScannerCompareErrorAction': 'Invalid', 'bgScannerReadErrorAction': 'Invalid', 'capacityAlertCriticalThreshold': 90, 'capacityAlertHighThreshold': 80, 'capacityUsageState': 'Normal', 'capacityUsageType': 'NetCapacity', 'checksumEnabled': False, 'compressionMethod': 'Normal', 'dataLayout': 'ErasureCoding', 'deviceGroupId': '39a898be00000000', 'deviceGroupName': 'DG1', 'externalAccelerationType': 'None', 'fglAccpId': None, 'fglExtraCapacity': None, 'fglMaxCompressionRatio': None, 'fglMetadataSizeXx100': None, 'fglNvdimmMetadataAmortizationX100': None, 'fglNvdimmWriteCacheSizeInMb': None, 'fglOverProvisioningFactor': None, 'fglPerfProfile': None, 'fglWriteAtomicitySize': None, 'fragmentationEnabled': False, 'genType': 'EC', 'id': '5dabf3f800000000', 'links': [{'href': '/api/instances/StoragePool::5dabf3f800000000', 'rel': 'self'}, {'body': {'ids': ['5dabf3f800000000'], 'resource_type': 'storage_pool'}, 'href': '/dtapi/rest/v1/metrics/query', 'rel': '/dtapi/rest/v1/metrics/query'}, {'href': '/api/instances/StoragePool::5dabf3f800000000/relationships/SpSds', 'rel': '/api/StoragePool/relationship/SpSds'}, {'href': '/api/instances/StoragePool::5dabf3f800000000/relationships/Volume', 'rel': '/api/StoragePool/relationship/Volume'}, {'href': '/api/instances/StoragePool::5dabf3f800000000/relationships/Device', 'rel': '/api/StoragePool/relationship/Device'}, {'href': '/api/instances/StoragePool::5dabf3f800000000/relationships/VTree', 'rel': '/api/StoragePool/relationship/VTree'}, {'href': '/api/instances/ProtectionDomain::f3d03dcf00000000', 'rel': '/api/parent/relationship/protectionDomainId'}, {'href': '/api/instances/DeviceGroup::39a898be00000000', 'rel': '/api/parent/relationship/deviceGroupId'}, {'href': '/api/instances/WrcDeviceGroup::39a898be00000000', 'rel': '/api/parent/relationship/wrcDeviceGroupId'}], 'mediaType': None, 'name': 'SP_EC', 'numOfParallelRebuildRebalanceJobsPerDevice': None, 'overProvisioningFactor': 0, 'persistentChecksumBuilderLimitKb': None, 'persistentChecksumEnabled': False, 'persistentChecksumState': 'StateInvalid', 'persistentChecksumValidateOnRead': None, 'physicalSizeGB': 5120, 'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None, 'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None, 'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': None, 'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': None, 'protectedMaintenanceModeIoPriorityPolicy': None, 'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None, 'protectionDomainId': 'f3d03dcf00000000', 'protectionDomainName': 'PD_EC', 'protectionScheme': 'TwoPlusTwo', 'rawSizeGB': 10240, 'rebalanceEnabled': None, 'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebalanceIoPriorityAppIopsPerDeviceThreshold': None, 'rebalanceIoPriorityBwLimitPerDeviceInKbps': None, 'rebalanceIoPriorityNumOfConcurrentIosPerDevice': None, 'rebalanceIoPriorityPolicy': None, 'rebalanceIoPriorityQuietPeriodInMsec': None, 'rebuildEnabled': None, 'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None, 'rebuildIoPriorityAppIopsPerDeviceThreshold': None, 'rebuildIoPriorityBwLimitPerDeviceInKbps': None, 'rebuildIoPriorityNumOfConcurrentIosPerDevice': None, 'rebuildIoPriorityPolicy': None, 'rebuildIoPriorityQuietPeriodInMsec': None, 'replicationCapacityMaxRatio': None, 'rmcacheWriteHandlingMode': 'Invalid', 'spClass': 'Default', 'spHealthState': 'Protected', 'sparePercentage': None, 'statistics': {'format': 'ID_TIMESTAMP_METRIC', 'resource_type': 'storage_pool', 'resources': [{'id': '5dabf3f800000000', 'metrics': [{'name': 'physical_free', 'values': [5443871047680]}, {'name': 'logical_provisioned', 'values': [0]}, {'name': 'raw_used', 'values': [10995116277760]}, {'name': 'logical_used', 'values': [0]}, {'name': 'physical_total', 'values': [5497558138880]}, {'name': 'physical_used', 'values': [0]}, {'name': 'over_provisioning_limit', 'values': [4611686017353646080]}]}], 'timestamps': ['2025-08-25T05:24:06Z']}, 'useRfcache': False, 'useRmcache': False, 'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None, 'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None, 'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': None, 'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': None, 'vtreeMigrationIoPriorityPolicy': None, 'vtreeMigrationIoPriorityQuietPeriodInMsec': None, 'wrcDeviceGroupId': '39a898be00000000', 'zeroPaddingEnabled': True})
  Details of the storage pool.


  id (, str, )
    ID of the storage pool.


  name (, str, )
    Name of the storage pool.


  protectionDomainId (, str, )
    ID of the protection domain in which the storage pool resides.


  zeroPaddingEnabled (, bool, )
    Indicates whether zero padding is enabled for the storage pool.


  capacityAlertHighThreshold (, int, )
    High threshold for capacity alert (percentage).


  capacityAlertCriticalThreshold (, int, )
    Critical threshold for capacity alert (percentage).


  capacityUsageState (, str, )
    Current capacity usage state of the storage pool.


  capacityUsageType (, str, )
    Type of capacity usage being monitored.


  addressSpaceUsage (, str, )
    Current address space usage state.


  addressSpaceUsageType (, str, )
    Type of address space usage limit.


  fragmentationEnabled (, bool, )
    Indicates whether fragmentation is enabled for the storage pool.


  inflightRequestsFactor (, int, )
    In-flight requests factor for performance tuning.


  inflightBandwidthFactor (, int, )
    In-flight bandwidth factor for performance tuning.


  compressionMethod (, str, )
    Compression method used in the storage pool.


  spClass (, str, )
    Class of the storage pool.


  genType (, str, )
    Data protection generation type of the storage pool.


  deviceGroupId (, str, )
    ID of the device group associated with the storage pool.


  wrcDeviceGroupId (, str, )
    ID of the WRC device group.


  rawSizeGb (, int, )
    Raw size of the storage pool in GB.


  numDataSlices (, int, )
    Number of data slices used in erasure coding.


  numProtectionSlices (, int, )
    Number of protection slices used in erasure coding.


  physicalSizeGb (, int, )
    Physical size of the storage pool in GB.


  overProvisioningFactor (, int, )
    Over-provisioning factor for the storage pool.


  protectionScheme (, str, )
    Data protection scheme used in the storage pool.


  spHealthState (, str, )
    Health state of the storage pool.


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

- Luis Liu (@vangork) <ansible.team@dell.com>
- Yiming Bao (@baoy1) <ansible.team@dell.com>

