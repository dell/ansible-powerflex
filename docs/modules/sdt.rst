.. _sdt_module:


sdt -- Manage SDT (also called NVMe Target) on Dell PowerFlex
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SDT (also called NVMe Target) on PowerFlex storage system includes creating new SDT, getting details of SDT, managing IP or role of SDT, modifying attributes of SDT, and deleting SDT.

Support only for Powerflex 4.5 versions and above.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  discovery_port (optional, int, None)
    Discovery port of the SDT.


  maintenance_mode (optional, str, None)
    Maintenance mode state of the SDT.


  nvme_port (optional, int, None)
    NVMe port of the SDT.


  protection_domain_name (optional, str, None)
    The name of the protection domain.


  sdt_ip_list (optional, list, None)
    Dictionary of IPs and their roles for the SDT.

    At least one IP-role is mandatory while creating a SDT.

    IP-roles can be updated as well.


    ip (True, str, None)
      IP address of the SDT.


    role (True, str, None)
      Role assigned to the SDT IP address.



  sdt_name (True, str, None)
    The name of the SDT.

    Mandatory for all operations.

    It is unique across the PowerFlex array.


  sdt_new_name (optional, str, None)
    SDT new name, can only be used for renaming the SDT.

    Only used for updates. Ignored during creation.


  state (optional, str, present)
    State of the SDT.


  storage_port (optional, int, None)
    Storage port of the SDT.


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
   - IP addresses, and IP address roles must be configured for each SDT.
   - You can assign both storage and host roles to the same target IP addresses.
   - Alternatively, assign the storage role to one target IP address, and add another target IP address for the host role.
   - Both roles must be configured on each NVMe target.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create SDT
      dellemc.powerflex.sdt:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        sdt_name: "sdt_example"
        sdt_ip_list:
          - ip: "172.169.xx.xx"
            role: "StorageAndHost"
          - ip: "172.169.yy.yy"
            role: "StorageAndHost"
        protection_domain_name: "PD1"
        storage_port: 12200
        nvme_port: 4420
        discovery_port: 8009
        state: "present"

    - name: Rename SDT
      dellemc.powerflex.sdt:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        sdt_name: "sdt_example"
        sdt_new_name: "sdt_new_example"
        state: "present"

    - name: Modify SDT port
      dellemc.powerflex.sdt:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        sdt_name: "sdt_example"
        nvme_port: 4421
        discovery_port: 8008
        state: "present"

    - name: Change maintenance mode
      dellemc.powerflex.sdt:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        sdt_name: "sdt_example"
        maintenance_mode: "active"
        state: "present"

    - name: Set IP and role to SDT
      dellemc.powerflex.sdt:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        sdt_name: "sdt_example"
        sdt_ip_list:
          - ip: "172.169.xx.xx"
            role: "StorageAndHost"
          - ip: "172.169.zz.zz"
            role: "StorageAndHost"
        state: "present"

    - name: Remove SDT
      dellemc.powerflex.sdt:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        sdt_name: "sdt_example"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


sdt_details (When SDT exists, dict, {'authenticationError': 'None', 'certificateInfo': {'issuer': '/GN=MDM/CN=CA-804696a4dbe1d90f/L=Hopkinton/ST=Massachusetts/C=US/O=EMC/OU=ASD', 'subject': '/GN=sdt-comp-0/CN=host41/L=Hopkinton/ST=Massachusetts/C=US/O=EMC/OU=ASD', 'thumbprint': '07:1E:FC:48:03:42:E6:45:14:1D:AA:97:1F:4F:B9:B2:B4:11:99:09', 'validFrom': 'Oct 8 02:35:00 2024 GMT', 'validFromAsn1Format': '241008023500Z', 'validTo': 'Oct 7 03:35:00 2034 GMT', 'validToAsn1Format': '341007033500Z'}, 'discoveryPort': 8009, 'faultSetId': None, 'id': '917d28ed00000000', 'ipList': [{'ip': '172.169.xx.xx', 'role': 'StorageAndHost'}, {'ip': '172.169.yy.yy', 'role': 'StorageAndHost'}], 'links': [{'href': '/api/instances/Sdt::917d28ed00000000', 'rel': 'self'}, {'href': '/api/instances/Sdt::917d28ed00000000/relationships/Statistics', 'rel': '/api/Sdt/relationship/Statistics'}, {'href': '/api/instances/ProtectionDomain::b4787fa100000000', 'rel': '/api/parent/relationship/protectionDomainId'}], 'maintenanceState': 'NoMaintenance', 'mdmConnectionState': 'Connected', 'membershipState': 'Joined', 'name': 'Sdt-pf460-svm-1', 'nvmePort': 4420, 'persistentDiscoveryControllersNum': 0, 'protectionDomainId': 'b4787fa100000000', 'protectionDomainName': 'PD1', 'sdtState': 'Normal', 'softwareVersionInfo': 'R4_5.2100.0', 'storagePort': 12200, 'systemId': '804696a4dbe1d90f'})
  Details of the SDT.


  authenticationError (, str, )
    Indicates authentication error.


  certificateInfo (, dict, )
    Information about certificate.


    issuer (, str, )
      Issuer of the certificate.


    subject (, str, )
      Subject of the certificate.


    thumbprint (, str, )
      Thumbprint of the certificate.


    validFrom (, str, )
      Date and time the certificate is valid from.


    validFromAsn1Format (, str, )
      Valid from date in ASN.1 format.


    validTo (, str, )
      Date and time the certificate is valid to.


    validToAsn1Format (, str, )
      Valid to date in ASN.1 format.



  discoveryPort (, int, )
    Discovery port.


  faultSetId (, str, )
    Fault set ID.


  id (, str, )
    SDS ID.


  ipList (, list, )
    SDS IP list.


    ip (, str, )
      IP present in the SDS.


    role (, str, )
      Role of the SDS IP.



  links (, list, )
    SDS links.


    href (, str, )
      SDS instance URL.


    rel (, str, )
      SDS's relationship with different entities.



  maintenanceState (, str, )
    Maintenance state.


  mdmConnectionState (, str, )
    MDM connection state.


  membershipState (, str, )
    Membership state.


  name (, str, )
    Name of the SDS.


  nvmePort (, int, )
    NVMe port.


  persistentDiscoveryControllersNum (, int, )
    Number of persistent discovery controllers.


  protectionDomainId (, str, )
    Protection Domain ID.


  protectionDomainName (, str, )
    Protection Domain Name.


  sdtState (, str, )
    SDS state.


  softwareVersionInfo (, str, )
    SDS software version information.


  storagePort (, int, )
    Storage port.


  systemId (, str, )
    System ID.






Status
------





Authors
~~~~~~~

- Yuhao Liu (@RayLiu7) <yuhao_liu@dell.com>

