.. _device_group_module:


device_group -- Manage Device Groups on Dell PowerFlex
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing device groups on PowerFlex Gen2 storage systems includes getting details of a device group, renaming a device group, updating spare node and spare device counts, and querying usable capacity. Device group creation and deletion are not supported by this module. Support only for PowerFlex 5.0 versions and above.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

 device_group_name (optional, str, None)
    The name of the device group.

    Mutually exclusive with :emphasis:`device\_group\_id`.


 device_group_id (optional, str, None)
    The ID of the device group.

    Mutually exclusive with :emphasis:`device\_group\_name`.


 new_device_group_name (optional, str, None)
    New name for the device group (rename operation).


 protection_domain_name (optional, str, None)
    Name of the protection domain for device group identification/validation.

    Mutually exclusive with :emphasis:`protection\_domain\_id`.


 protection_domain_id (optional, str, None)
    ID of the protection domain for device group identification/validation.

    Mutually exclusive with :emphasis:`protection\_domain\_name`.


 media_type (optional, str, None)
    Media type of the device group.

    Query and validation only; it cannot be modified.

    Choices: SSD, PMEM


 spare_node_count (optional, int, None)
    Spare node count for the device group.


 spare_device_count (optional, int, None)
    Spare device count for the device group.


 query_usable_capacity (optional, bool, False)
    Whether to query the usable capacity of the device group.

    This is a read-only operation.


 state (optional, str, present)
    State of the device group.

    Only :literal:`present` is supported; the module manages existing device groups and does not create or delete them.

    Choices: present


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


 timeout (optional, int, 120)
    Time after which connection will get terminated.

    It is to be mentioned in seconds.




Notes
-----

.. note::
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get device group details by name
      dellemc.powerflex.device_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "<your_password>"
        validate_certs: "{{ validate_certs }}"
        device_group_name: "DG1"
        state: "present"

    - name: Get device group details by ID
      dellemc.powerflex.device_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "<your_password>"
        validate_certs: "{{ validate_certs }}"
        device_group_id: "39a898be00000000"
        state: "present"

    - name: Rename device group and update spare counts
      dellemc.powerflex.device_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "<your_password>"
        validate_certs: "{{ validate_certs }}"
        device_group_name: "DG1"
        new_device_group_name: "DG1_renamed"
        spare_node_count: 2
        spare_device_count: 1
        state: "present"

    - name: Query usable capacity for a device group
      dellemc.powerflex.device_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "<your_password>"
        validate_certs: "{{ validate_certs }}"
        device_group_id: "39a898be00000000"
        query_usable_capacity: true
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


device_group_details (When device group exists, dict, {'id': '39a898be00000000', 'name': 'test_dg', 'protectionDomainId': '7bd6457000000000', 'mediaType': 'SSD', 'spareNodeCount': 1, 'spareDeviceCount': 1, 'links': []})
  Details of the device group.


  id (, str, )
    Device group ID.


  name (, str, )
    Device group name.


  protectionDomainId (, str, )
    Protection domain ID.


  mediaType (, str, )
    Media type of the device group.


  spareNodeCount (, int, )
    Spare node count.


  spareDeviceCount (, int, )
    Spare device count.


  links (, list, )
    Related resource links.


usable_capacity_details (When query_usable_capacity is true, dict, {'39a898be00000000': {'numProtectionSlices': 2}})
  Usable capacity details for the device group.





Status
------

This module is supported on Dell PowerFlex 5.x and later versions.



Authors
~~~~~~~

- Dell Technologies (@dellemc) <ansible.team@dell.com>
