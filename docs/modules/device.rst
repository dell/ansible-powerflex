.. _device_module:


device -- Manage device on Dell PowerFlex
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing device on PowerFlex storage system includes adding new device, getting details of device, and removing a device.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  current_pathname (optional, str, None)
    Full path of the device to be added.

    Required while adding a device.


  device_name (optional, str, None)
    Device name.

    Mutually exclusive with \ :emphasis:`device\_id`\ .


  device_id (optional, str, None)
    Device ID.

    Mutually exclusive with \ :emphasis:`device\_name`\ .


  sds_name (optional, str, None)
    The name of the SDS.

    Required while adding a device.

    Mutually exclusive with \ :emphasis:`sds\_id`\ .


  sds_id (optional, str, None)
    The ID of the SDS.

    Required while adding a device.

    Mutually exclusive with \ :emphasis:`sds\_name`\ .


  storage_pool_name (optional, str, None)
    Storage Pool name.

    Used while adding a storage device.

    Mutually exclusive with \ :emphasis:`storage\_pool\_id`\ , \ :emphasis:`acceleration\_pool\_id`\  and \ :emphasis:`acceleration\_pool\_name`\ .


  storage_pool_id (optional, str, None)
    Storage Pool ID.

    Used while adding a storage device.

    Media type supported are \ :literal:`SSD`\  and \ :literal:`HDD`\ .

    Mutually exclusive with \ :emphasis:`storage\_pool\_name`\ , \ :emphasis:`acceleration\_pool\_id`\  and \ :emphasis:`acceleration\_pool\_name`\ .


  acceleration_pool_name (optional, str, None)
    Acceleration Pool Name.

    Used while adding an acceleration device.

    Media type supported are \ :literal:`SSD`\  and \ :literal:`NVDIMM`\ .

    Mutually exclusive with \ :emphasis:`storage\_pool\_id`\ , \ :emphasis:`storage\_pool\_name`\  and \ :emphasis:`acceleration\_pool\_name`\ .


  acceleration_pool_id (optional, str, None)
    Acceleration Pool ID.

    Used while adding an acceleration device.

    Media type supported are \ :literal:`SSD`\  and \ :literal:`NVDIMM`\ .

    Mutually exclusive with \ :emphasis:`acceleration\_pool\_name`\ , \ :emphasis:`storage\_pool\_name`\  and \ :emphasis:`storage\_pool\_id`\ .


  protection_domain_name (optional, str, None)
    Protection domain name.

    Used while identifying a storage pool along with \ :emphasis:`storage\_pool\_name`\ .

    Mutually exclusive with \ :emphasis:`protection\_domain\_id`\ .


  protection_domain_id (optional, str, None)
    Protection domain ID.

    Used while identifying a storage pool along with \ :emphasis:`storage\_pool\_name`\ .

    Mutually exclusive with \ :emphasis:`protection\_domain\_name`\ .


  external_acceleration_type (optional, str, None)
    Device external acceleration types.

    Used while adding a device.


  media_type (optional, str, None)
    Device media types.

    Required while adding a device.


  state (True, str, None)
    State of the device.


  force (optional, bool, False)
    Using the Force flag to add a device.

    Use this flag, to overwrite existing data on the device.

    Use this flag with caution, because all data on the device will be destroyed.


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
   - The value for device\_id is generated only after successful addition of the device.
   - To uniquely identify a device, either \ :emphasis:`device\_id`\  can be passed or one of \ :emphasis:`current\_pathname`\  or \ :emphasis:`device\_name`\  must be passed with \ :emphasis:`sds\_id`\  or \ :emphasis:`sds\_name`\ .
   - It is recommended to install Rfcache driver for SSD device on SDS in order to add it to an acceleration pool.
   - The \ :emphasis:`check\_mode`\  is not supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add a device
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        current_pathname: "/dev/sdb"
        sds_name: "node1"
        media_type: "HDD"
        device_name: "device2"
        storage_pool_name: "pool1"
        protection_domain_name: "domain1"
        external_acceleration_type: "ReadAndWrite"
        state: "present"
    - name: Add a device with force flag
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        current_pathname: "/dev/sdb"
        sds_name: "node1"
        media_type: "HDD"
        device_name: "device2"
        storage_pool_name: "pool1"
        protection_domain_name: "domain1"
        external_acceleration_type: "ReadAndWrite"
        force: true
        state: "present"
    - name: Get device details using device_id
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        device_id: "d7fe088900000000"
        state: "present"
    - name: Get device details using (current_pathname, sds_name)
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        current_pathname: "/dev/sdb"
        sds_name: "node0"
        state: "present"
    - name: Get device details using (current_pathname, sds_id)
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        current_pathname: "/dev/sdb"
        sds_id: "5717d71800000000"
        state: "present"
    - name: Remove a device using device_id
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        device_id: "76eb7e2f00010000"
        state: "absent"
    - name: Remove a device using (current_pathname, sds_id)
      dellemc.powerflex.device:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        current_pathname: "/dev/sdb"
        sds_name: "node1"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


device_details (When device exists, dict, {'accelerationPoolId': None, 'accelerationProps': None, 'aggregatedState': 'NeverFailed', 'ataSecurityActive': False, 'autoDetectMediaType': 'SSD', 'cacheLookAheadActive': False, 'capacity': 0, 'capacityLimitInKb': 365772800, 'deviceCurrentPathName': '/dev/sdb', 'deviceOriginalPathName': '/dev/sdb', 'deviceState': 'Normal', 'deviceType': 'Unknown', 'errorState': 'None', 'externalAccelerationType': 'None', 'fglNvdimmMetadataAmortizationX100': 150, 'fglNvdimmWriteCacheSize': 16, 'firmwareVersion': None, 'id': 'b6efa59900000000', 'ledSetting': 'Off', 'links': [{'href': '/api/instances/Device::b6efa59900000000', 'rel': 'self'}, {'href': '/api/instances/Device::b6efa59900000000/relationships /Statistics', 'rel': '/api/Device/relationship/Statistics'}, {'href': '/api/instances/Sds::8f3bb0ce00000000', 'rel': '/api/parent/relationship/sdsId'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': '/api/parent/relationship/storagePoolId'}, {'href': '/api/instances/SpSds::fedf6f2000000000', 'rel': '/api/parent/relationship/spSdsId'}], 'logicalSectorSizeInBytes': 0, 'longSuccessfulIos': {'longWindow': None, 'mediumWindow': None, 'shortWindow': None}, 'maxCapacityInKb': 365772800, 'mediaFailing': False, 'mediaType': 'HDD', 'modelName': None, 'name': 'device230', 'persistentChecksumState': 'Protected', 'physicalSectorSizeInBytes': 0, 'protectionDomainId': '9300c1f900000000', 'protectionDomainName': 'domain1', 'raidControllerSerialNumber': None, 'rfcacheErrorDeviceDoesNotExist': False, 'rfcacheProps': None, 'sdsId': '8f3bb0ce00000000', 'sdsName': 'node1', 'serialNumber': None, 'slotNumber': None, 'spSdsId': 'fedf6f2000000000', 'ssdEndOfLifeState': 'NeverFailed', 'storagePoolId': 'e0d8f6c900000000', 'storagePoolName': 'pool1', 'storageProps': {'destFglAccDeviceId': None, 'destFglNvdimmSizeMb': 0, 'fglAccDeviceId': None, 'fglNvdimmSizeMb': 0}, 'temperatureState': 'NeverFailed', 'vendorName': None, 'writeCacheActive': False})
  Details of the device.


  accelerationPoolId (, str, )
    Acceleration pool ID.


  accelerationPoolName (, str, )
    Acceleration pool name.


  accelerationProps (, str, )
    Indicates acceleration props.


  aggregatedState (, str, )
    Indicates aggregated state.


  ataSecurityActive (, bool, )
    Indicates ATA security active state.


  autoDetectMediaType (, str, )
    Indicates auto detection of media type.


  cacheLookAheadActive (, bool, )
    Indicates cache look ahead active state.


  capacity (, int, )
    Device capacity.


  capacityLimitInKb (, int, )
    Device capacity limit in KB.


  deviceCurrentPathName (, str, )
    Device current path name.


  deviceOriginalPathName (, str, )
    Device original path name.


  deviceState (, str, )
    Indicates device state.


  deviceType (, str, )
    Indicates device type.


  errorState (, str, )
    Indicates error state.


  externalAccelerationType (, str, )
    Indicates external acceleration type.


  fglNvdimmMetadataAmortizationX100 (, int, )
    Indicates FGL NVDIMM meta data amortization value.


  fglNvdimmWriteCacheSize (, int, )
    Indicates FGL NVDIMM write cache size.


  firmwareVersion (, str, )
    Indicates firmware version.


  id (, str, )
    Device ID.


  ledSetting (, str, )
    Indicates LED setting.


  links (, list, )
    Device links.


    href (, str, )
      Device instance URL.


    rel (, str, )
      Relationship of device with different entities.



  logicalSectorSizeInBytes (, int, )
    Logical sector size in bytes.


  longSuccessfulIos (, list, )
    Indicates long successful IOs.


  maxCapacityInKb (, int, )
    Maximum device capacity limit in KB.


  mediaFailing (, bool, )
    Indicates media failing.


  mediaType (, str, )
    Indicates media type.


  modelName (, str, )
    Indicates model name.


  name (, str, )
    Device name.


  persistentChecksumState (, str, )
    Indicates persistent checksum state.


  physicalSectorSizeInBytes (, int, )
    Physical sector size in bytes.


  protectionDomainId (, str, )
    Protection domain ID.


  protectionDomainName (, str, )
    Protection domain name.


  raidControllerSerialNumber (, str, )
    RAID controller serial number.


  rfcacheErrorDeviceDoesNotExist (, bool, )
    Indicates RF cache error device does not exist.


  rfcacheProps (, str, )
    RF cache props.


  sdsId (, str, )
    SDS ID.


  sdsName (, str, )
    SDS name.


  serialNumber (, str, )
    Indicates Serial number.


  spSdsId (, str, )
    Indicates SPs SDS ID.


  ssdEndOfLifeState (, str, )
    Indicates SSD end of life state.


  storagePoolId (, str, )
    Storage Pool ID.


  storagePoolName (, str, )
    Storage Pool name.


  storageProps (, list, )
    Storage props.


  temperatureState (, str, )
    Indicates temperature state.


  vendorName (, str, )
    Indicates vendor name.


  writeCacheActive (, bool, )
    Indicates write cache active.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

