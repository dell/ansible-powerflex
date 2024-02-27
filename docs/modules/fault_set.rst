.. _fault_set_module


device -- Manage fault set on Dell PowerFlex
============================================

.. contents::
    :local:
    :depth: 1


Synopsis
--------

Managing fault sets on PowerFlex storage system includes adding, removing and egetting details of fault sets.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.14 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  fault_set_id(optional, str, None)
        ID of the Fault Set being affected.
        Mutually exclusive with *fault_set_name*
        
  fault_set_name(optional, str, None)
        Name of the Fault Set.
        It is unique across the Powerflex Array.        
        Mutually exclusive with *fault_set_id*

  fault_set_new_name(optional, str, None)
        New Name of the Fault Set.
        This is used to rename the fault set.

  protection_domain_id (optional, str, None)
        ID of the protection domain
        Specify either *protection_domain_name* or *protection_domain_id* when creating a fault set

  protection_domain_name(optional, str, None)
        Name of protection domain.
        Specify either *protection_domain_name* or *protection_domain_id* when creating a fault set        
  
  state (True, str, None)
        State of the Fault Set.
        choices: [present, absent]
        type: str

  
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
   - The *check_mode* is not supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.



Examples
--------

.. code-block: yaml+jinja


    - name: Create Fault Set on Protection Domain
      dellemc.powerflex.fault_set:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        fault_set_name: "{{fault_set_name}}"
        protection_domain_name: "{{pd_name}}"
        state: present

    - name: Create Fault Set on Protection Domain
      dellemc.powerflex.fault_set:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        fault_set_name: "{{fault_set_name}}"
        protection_domain_id: "{{pd_id}}"
        state: present

    - name: Delete Fault Set
      dellemc.powerflex.fault_set:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        fault_set_name: "{{fault_set_name}}"
        state: absent

    - name: Delete Fault Set
      dellemc.powerflex.fault_set:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        fault_set_id: "{{fault_set_id}}"
        state: absent


Return Values:
--------------
changed(always, bool, false)
        Whether or not the resource has changed.

fault_set_details (when fault set exists, dict, { 'protectionDomainId': 'da721a8300000000', 'protectionDomainName': 'pd001', 'name': 'fs_001','id': 'eb44b70500000000','links': [{ 'rel': 'self', 'href': '/api/instances/FaultSet::eb44b70500000000' }, {'rel': '/api/FaultSet/relationship/Statistics', 'href': '/api/instances/FaultSet::eb44b70500000000/relationships/Statistics'},{'rel': '/api/FaultSet/relationship/Sds', 'href': '/api/instances/FaultSet::eb44b70500000000/relationships/Sds' }, { 'rel': '/api/parent/relationship/protectionDomainId', 'href': '/api/instances/ProtectionDomain::da721a8300000000' }})
  Details of fault set.
  
  
  protectionDomainId(, str,):
    The ID of the protection domain.


  protectionDomainName(, str,):
    The name of the protection domain.


  name(, str,)
    fault set name.


  id(, str,)
    fault set  id


  links (, list, )
    Device links.


    href (, str, )
      Device instance URL.


    rel (, str, )
      Relationship of device with different entities.


Status
------





Authors
~~~~~~~

- Carlos Tronco (@ctronco) <ansible.team@dell.com>

 