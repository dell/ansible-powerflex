.. _sdc_module:


sdc -- Manage SDCs on Dell PowerFlex
====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SDCs on PowerFlex storage system includes getting details of SDC and renaming SDC.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  sdc_name (optional, str, None)
    Name of the SDC.

    Specify either \ :emphasis:`sdc\_name`\ , \ :emphasis:`sdc\_id`\  or \ :emphasis:`sdc\_ip`\  for get/rename operation.

    Mutually exclusive with \ :emphasis:`sdc\_id`\  and \ :emphasis:`sdc\_ip`\ .


  sdc_id (optional, str, None)
    ID of the SDC.

    Specify either \ :emphasis:`sdc\_name`\ , \ :emphasis:`sdc\_id`\  or \ :emphasis:`sdc\_ip`\  for get/rename operation.

    Mutually exclusive with \ :emphasis:`sdc\_name`\  and \ :emphasis:`sdc\_ip`\ .


  sdc_ip (optional, str, None)
    IP of the SDC.

    Specify either \ :emphasis:`sdc\_name`\ , \ :emphasis:`sdc\_id`\  or \ :emphasis:`sdc\_ip`\  for get/rename operation.

    Mutually exclusive with \ :emphasis:`sdc\_id`\  and \ :emphasis:`sdc\_name`\ .


  sdc_new_name (optional, str, None)
    New name of the SDC. Used to rename the SDC.


  performance_profile (optional, str, None)
    Define the performance profile as \ :emphasis:`Compact`\  or \ :emphasis:`HighPerformance`\ .

    The high performance profile configures a predefined set of parameters for very high performance use cases.


  state (True, str, None)
    State of the SDC.


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
   - The \ :emphasis:`check\_mode`\  is not supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get SDC details using SDC ip
      dellemc.powerflex.sdc:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        sdc_ip: "{{sdc_ip}}"
        state: "present"

    - name: Rename SDC using SDC name
      dellemc.powerflex.sdc:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        sdc_name: "centos_sdc"
        sdc_new_name: "centos_sdc_renamed"
        state: "present"

    - name: Modify performance profile of SDC using SDC name
      dellemc.powerflex.sdc:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        sdc_name: "centos_sdc"
        performance_profile: "Compact"
        state: "present"

    - name: Remove SDC using SDC name
      dellemc.powerflex.sdc:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        sdc_name: "centos_sdc"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


sdc_details (When SDC exists, dict, {'id': '07335d3d00000006', 'installedSoftwareVersionInfo': 'R3_6.0.0', 'kernelBuildNumber': None, 'kernelVersion': '3.10.0', 'links': [{'href': '/api/instances/Sdc::07335d3d00000006', 'rel': 'self'}, {'href': '/api/instances/Sdc::07335d3d00000006/relationships/ Statistics', 'rel': '/api/Sdc/relationship/Statistics'}, {'href': '/api/instances/Sdc::07335d3d00000006/relationships/ Volume', 'rel': '/api/Sdc/relationship/Volume'}, {'href': '/api/instances/System::4a54a8ba6df0690f', 'rel': '/api/parent/relationship/systemId'}], 'mapped_volumes': [], 'mdmConnectionState': 'Disconnected', 'memoryAllocationFailure': None, 'name': 'LGLAP203', 'osType': 'Linux', 'peerMdmId': None, 'perfProfile': 'HighPerformance', 'sdcApproved': True, 'sdcApprovedIps': None, 'sdcGuid': 'F8ECB844-23B8-4629-92BB-B6E49A1744CB', 'sdcIp': 'N/A', 'sdcIps': None, 'sdcType': 'AppSdc', 'sdrId': None, 'socketAllocationFailure': None, 'softwareVersionInfo': 'R3_6.0.0', 'systemId': '4a54a8ba6df0690f', 'versionInfo': 'R3_6.0.0'})
  Details of the SDC.


  id (, str, )
    The ID of the SDC.


  name (, str, )
    Name of the SDC.


  sdcIp (, str, )
    IP of the SDC.


  osType (, str, )
    OS type of the SDC.


  mapped_volumes (, list, )
    The details of the mapped volumes.


    id (, str, )
      The ID of the volume.


    name (, str, )
      The name of the volume.


    volumeType (, str, )
      Type of the volume.



  sdcApproved (, bool, )
    Indicates whether an SDC has approved access to the system.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

