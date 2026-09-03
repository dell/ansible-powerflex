.. _storage_node_module:


storage_node -- Managing storage node on Dell PowerFlex 5.x
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Dell PowerFlex storage node module includes getting the details of a storage node, adding and removing IP addresses, modifying IP roles, renaming a storage node, and updating device pathnames. This module is supported only on Dell PowerFlex 5.x and later versions. There is no Gen1 predecessor module for this entity — the Gen1 equivalent for SDS management is M(dellemc.powerflex.sds).



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

 storage_node_name (optional, str, None)
    The name of the storage node.

    Mutually exclusive with :emphasis:`storage\_node\_id`.


 storage_node_id (optional, str, None)
    The ID of the storage node.

    Mutually exclusive with :emphasis:`storage\_node\_name`.


 storage_node_new_name (optional, str, None)
    Used to rename the storage node.

    Mutually exclusive with :emphasis:`update\_pathnames`.


 node_ip_list (optional, list, None)
    Dictionary of IPs and their roles for the storage node.

    Each item in the list is a dictionary with:
    
    - ip (str, required) — The IP address
    - role (str, required) — The IP role: Storage, App, or StorageAndApp

    Mutually exclusive with :emphasis:`update\_pathnames`.


 node_ip_state (optional, str, None)
    The state of the IP address on the storage node.

    Choices: present-in-node, absent-in-node

    Required when :emphasis:`node\_ip\_list` is specified.


 update_pathnames (optional, bool, False)
    Trigger device pathname update on the storage node.

    When set to true, the module will refresh device pathnames for the storage node.

    Mutually exclusive with :emphasis:`node\_ip\_list` and :emphasis:`storage\_node\_new_name`.


 force_failed_devices (optional, bool, False)
    Force pathname update for failed devices.

    Only applicable when :emphasis:`update\_pathnames` is true.


 state (True, str, None)
    The state of the storage node. Can be 'present' or 'absent'.

    Note: Storage node creation and deletion are not supported. The module only supports querying and modifying existing storage nodes.


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
   - Storage node creation and deletion are not supported. The module only supports querying and modifying existing storage nodes.
   - The :emphasis:`check\_mode` is supported for all operations.
   - The :emphasis:`update\_pathnames` operation is non-idempotent — it will always report changed=true when executed.
   - IP role modification auto-detects changes — if an IP exists with a different role, the module will update the role.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.
   - PDS (Protection Domain Services) and DGWT (Data Gateway for Windows Thin) query operations are deferred to Phase 2 pending PyPowerFlex SDK enhancement.





Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get storage node details using name
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        state: "present"

    - name: Get storage node details using ID
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_id: "abc123def456"
        state: "present"

    - name: Add IP to storage node
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        node_ip_list:
          - ip: "10.0.0.2"
            role: "App"
        node_ip_state: "present-in-node"
        state: "present"

    - name: Change IP role on storage node
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        node_ip_list:
          - ip: "10.0.0.2"
            role: "StorageAndApp"
        node_ip_state: "present-in-node"
        state: "present"

    - name: Remove IP from storage node
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        node_ip_list:
          - ip: "10.0.0.2"
            role: "App"
        node_ip_state: "absent-in-node"
        state: "present"

    - name: Rename storage node
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        storage_node_new_name: "node1_new"
        state: "present"

    - name: Update device pathnames on storage node
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        update_pathnames: true
        state: "present"

    - name: Update device pathnames with force for failed devices
      dellemc.powerflex.storage_node:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        storage_node_name: "node1"
        update_pathnames: true
        force_failed_devices: true
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


storage_node_details (When storage node exists, dict, {...})
  Details of the storage node.


  id (, str, )
    Storage node ID.


  name (, str, )
    Name of the storage node.


  ipsList (, list, )
    List of IP addresses and their roles assigned to the storage node.


    ip (, str, )
      IP address.

    role (, str, )
      IP role: Storage, App, or StorageAndApp.


  protectionDomainId (, str, )
    Protection domain ID associated with the storage node.


  protectionDomainName (, str, )
    Protection domain name associated with the storage node.


  pdsPort (, int, )
    PDS port number.


  dgwtPort (, int, )
    DGWT port number.


  maintenanceState (, str, )
    Maintenance state of the storage node.


  links (, list, )
    Storage node links.


    href (, str, )
      Storage node instance URL.

    rel (, str, )
      Storage node's relationship with different entities.





Status
------

This module is supported on Dell PowerFlex 5.x and later versions.



Authors
~~~~~~~

- Saksham Nautiyal (@Saksham-Nautiyal) <ansible.team@dell.com>
