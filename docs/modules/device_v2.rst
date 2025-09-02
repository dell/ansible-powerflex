.. _device_v2_module:


device_v2 -- Manage Device on Dell PowerFlex
============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing device on PowerFlex storage system includes adding new device, getting details of device, modifying attributes of device, and removing device.

Support only for Powerflex 5.0 versions and above.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

  current_pathname (optional, str, None)
    Full path of the device to be added.

    Required while adding a device.


  device_name (optional, str, None)
    Device name.

    Mutually exclusive with :emphasis:`device\_id`.


  device_id (optional, str, None)
    Device ID.

    Mutually exclusive with :emphasis:`device\_name`.


  device_group_name (optional, str, None)
    The name of the device group.

    Required while adding a device.

    Mutually exclusive with :emphasis:`device\_group\_id`.


  device_group_id (optional, str, None)
    The ID of the device group.

    Required while adding a device.

    Mutually exclusive with :emphasis:`device\_group\_name`.


  storage_node_name (optional, str, None)
    The name of the storage node.

    Required while adding a device.

    Mutually exclusive with :emphasis:`storage\_node\_id`.


  storage_node_id (optional, str, None)
    The ID of the storage node.

    Required while adding a device.

    Mutually exclusive with :emphasis:`storage\_node\_name`.


  new_device_name (optional, str, None)
    New name of the device.


  capacity_limit_gb (optional, int, None)
    Device capacity limit in GB.


  media_type (optional, str, None)
    Device media types.

    Required while adding a device.


  clear_error (optional, bool, None)
    Using the flag to clear error on a device.

    If the error continues to exist, the device will return to an error state as soon as it is accessed.


  state (optional, str, present)
    State of the device.


  force (optional, bool, None)
    Using the Force flag to add a device.

    Using the flag to clear device error state without checking.

    Use this flag with caution, because all data on the device will be destroyed.


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
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create device
      register: device1_result
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        current_pathname: "/dev/sdc"
        device_group_name: "DG1"
        media_type: "SSD"
        storage_node_name: "Node1"

    - name: Create device using name with force flag
      register: device2_result
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        current_pathname: "/dev/sdd"
        device_group_id: "39a898be00000000"
        storage_node_id: "03b589bf00000003"
        media_type: "SSD"
        device_name: "node1-d2"
        force: true
        state: "present"

    - name: Get device details using device_id
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        device_id: "{{ device1_result.device_details.id }}"
        state: "present"

    - name: Get device details using (current_pathname, storage_node_name)
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        current_pathname: "/dev/sdd"
        storage_node_name: "Node1"
        state: "present"

    - name: Get device details using (current_pathname, storage_node_id)
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        current_pathname: "/dev/sdd"
        storage_node_id: "03b589bf00000003"
        state: "present"

    - name: Rename device
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        device_id: "{{ device1_result.device_details.id }}"
        new_device_name: "node1-d3"
        state: "present"

    - name: Clear device error
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        device_id: "{{ device1_result.device_details.id }}"
        clear_error: true
        force: true
        state: "present"

    - name: Clear device error with force flag
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        device_name: "{{ device2_result.device_details.name }}"
        clear_error: true
        force: true
        state: "present"

    - name: Modify device capacity limit
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        device_name: "{{ device2_result.device_details.name }}"
        capacity_limit_gb: 500
        state: "present"

    - name: Remove device using device_id
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        device_id: "{{ device1_result.device_details.id }}"
        state: "absent"

    - name: Remove device using (current_pathname, storage_node_name)
      dellemc.powerflex.device_v2:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        current_pathname: "/dev/sdd"
        storage_node_name: "Node1"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


device_details (When device exists, dict, {'fglNvdimmWriteCacheSize': None, 'deviceCurrentPathName': '/dev/sdd', 'rfcacheErrorDeviceDoesNotExist': False, 'logicalSectorSizeInBytes': 0, 'deviceOriginalPathName': '/dev/sdd', 'fglNvdimmMetadataAmortizationX100': None, 'capacity': 0, 'name': None, 'serialNumber': None, 'mediaType': 'SSD', 'accelerationPoolId': None, 'rfcacheProps': None, 'sdsId': None, 'storagePoolId': None, 'capacityLimitInKb': 1073479680, 'errorState': 'None', 'storageNodeId': '03b589bf00000003', 'externalAccelerationType': 'None', 'accelerationProps': None, 'ssdEndOfLifeState': 'NeverFailed', 'temperatureState': 'NeverFailed', 'aggregatedState': 'NeverFailed', 'spSdsId': None, 'deviceState': 'Normal', 'storageProps': None, 'autoDetectMediaType': None, 'longSuccessfulIos': {'shortWindow': None, 'mediumWindow': None, 'longWindow': None}, 'maxCapacityInKb': 1073479680, 'ledSetting': 'Off', 'modelName': None, 'deviceType': 'Unknown', 'vendorName': None, 'raidControllerSerialNumber': None, 'firmwareVersion': None, 'cacheLookAheadActive': False, 'writeCacheActive': False, 'ataSecurityActive': False, 'physicalSectorSizeInBytes': 0, 'mediaFailing': False, 'slotNumber': 'N/A', 'persistentChecksumState': 'StateInvalid', 'capacityInMb': 1048576, 'usableCapacityInMb': 1048320, 'deviceGroupId': '39a898be00000000', 'id': 'e7ffaabf00030002', 'links': [{'rel': 'self', 'href': '/api/instances/Device::e7ffaabf00030002'}, {'rel': '/dtapi/rest/v1/metrics/query', 'href': '/dtapi/rest/v1/metrics/query', 'body': {'resource_type': 'device', 'ids': ['e7ffaabf00030002']}}, {'rel': '/api/parent/relationship/deviceGroupId', 'href': '/api/instances/DeviceGroup::39a898be00000000'}, {'rel': '/api/parent/relationship/storageNodeId', 'href': '/api/instances/StorageNode::03b589bf00000003'}]})
  Details of the device.


  id (, str, )
    Device ID.


  name (, str, )
    Device name.


  deviceCurrentPathname (, str, )
    Device current path name.


  deviceOriginalPathname (, str, )
    Device original path name.


  deviceState (, str, )
    Indicates device state.


  errorState (, str, )
    Indicates error state.


  capacityLimitInKb (, int, )
    Device capacity limit in KB.


  maxCapacityInKb (, int, )
    Maximum device capacity in KB.


  deviceGroupId (, str, )
    Device group ID.


  longSuccessfulIos (, dict, )
    Indicates long successful I/O operations.


  storageNodeId (, str, )
    Storage node ID.


  updateConfiguration (, bool, )
    Indicates whether configuration update is enabled.


  ledSetting (, str, )
    LED setting state.


  aggregatedState (, str, )
    Indicates aggregated device state.


  temperatureState (, str, )
    Indicates temperature state.


  ssdEndOfLifeState (, str, )
    Indicates SSD end of life state.


  modelName (, str, )
    Device model name.


  serialNumber (, str, )
    Device serial number.


  deviceType (, str, )
    Indicates device type.


  mediaType (, str, )
    Indicates media type.


  vendorName (, str, )
    Device vendor name.


  raidControllerSerialNumber (, str, )
    RAID controller serial number.


  firmwareVersion (, str, )
    Device firmware version.


  cacheLookAheadActive (, bool, )
    Indicates cache look-ahead active state.


  writeCacheActive (, bool, )
    Indicates write cache active state.


  ataSecurityActive (, bool, )
    Indicates ATA security active state.


  capacity (, int, )
    Device capacity in bytes.


  logicalSectorSizeInBytes (, int, )
    Logical sector size in bytes.


  physicalSectorSizeInBytes (, int, )
    Physical sector size in bytes.


  mediaFailing (, bool, )
    Indicates if media is failing.


  autoDetectMediaType (, str, )
    Auto-detection result of media type.


  storageProps (, dict, )
    Storage device properties.


  persistentChecksumState (, str, )
    Indicates persistent checksum state.






Status
------





Authors
~~~~~~~

- Tao He (@taohe1012) <ansible.team@dell.com>

