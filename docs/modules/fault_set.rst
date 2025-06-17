.. _fault_set_module:


fault_set -- Manage Fault Sets on Dell PowerFlex
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing fault sets on PowerFlex storage system includes creating, getting details, renaming and deleting a fault set.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  fault_set_name (optional, str, None)
    Name of the Fault Set.

    Mutually exclusive with \ :emphasis:`fault\_set\_id`\ .


  fault_set_id (optional, str, None)
    ID of the Fault Set.

    Mutually exclusive with \ :emphasis:`fault\_set\_name`\ .


  protection_domain_name (optional, str, None)
    Name of protection domain.

    Mutually exclusive with \ :emphasis:`protection\_domain\_id`\ .


  protection_domain_id (optional, str, None)
    ID of the protection domain.

    Mutually exclusive with \ :emphasis:`protection\_domain\_name`\ .


  fault_set_new_name (optional, str, None)
    New name of the fault set.


  state (optional, str, present)
    State of the Fault Set.


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
   - The \ :emphasis:`check\_mode`\  is supported.
   - When \ :emphasis:`fault\_set\_name`\  is provided, \ :emphasis:`protection\_domain\_name`\  or \ :emphasis:`protection\_domain\_id`\  must be provided.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Create Fault Set on Protection Domain
      dellemc.powerflex.fault_set:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        fault_set_name: "{{ fault_set_name }}"
        protection_domain_name: "{{ pd_name }}"
        state: present

    - name: Rename Fault Set
      dellemc.powerflex.fault_set:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        fault_set_name: "{{ fault_set_name }}"
        fault_set_new_name: "{{ fault_set_new_name }}"
        state: present

    - name: Get details of a Fault Set
      dellemc.powerflex.fault_set:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        fault_set_id: "{{ fault_set_id }}"
        state: present

    - name: Delete Fault Set
      dellemc.powerflex.fault_set:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        fault_set_id: "{{ fault_set_id }}"
        state: absent



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


fault_set_details (always, dict, {'protectionDomainId': 'da721a8300000000', 'protectionDomainName': 'sample-pd', 'name': 'fs_001', 'id': 'eb44b70500000000', 'links': []})
  Details of fault set.


  protectionDomainId (, str, )
    Unique identifier of the protection domain.


  protectionDomainName (, str, )
    Name of the protection domain.


  name (, str, )
    Name of the fault set.


  id (, str, )
    Unique identifier of the fault set.


  SDS (, list, )
    List of SDS associated to the fault set.


  links (, list, )
    Fault set links.


    href (, str, )
      Fault Set instance URL.


    rel (, str, )
      Relationship of fault set with different entities.







Status
------





Authors
~~~~~~~

- Carlos Tronco (@ctronco) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

