.. _nvme_host_module:


nvme_host -- Manage NVMe hosts on Dell PowerFlex
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing NVMe hosts on PowerFlex storage system includes creating, getting details of NVMe hosts , modifying and deleting NVMe hosts.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  max_num_paths (optional, str, None)
    Maximum number of paths per volume. Used to create or modify the NVMe host.


  max_num_sys_ports (optional, str, None)
    Maximum number of ports per protection domain. Used to create or modify the NVMe host.


  nqn (optional, str, None)
    NQN of the NVMe host. Used to create, get or modify the NVMe host.

    To retrieve NQN of NVMe host, use command :command:\`cat /etc/nvme/hostnqn\`


  nvme_host_name (optional, str, None)
    Name of the NVMe host.

    Specify either \ :emphasis:`nvme\_host\_name`\ , \ :emphasis:`nqn`\  for create, get or rename operation.


  nvme_host_new_name (optional, str, None)
    New name of the NVMe host. Used to rename the NVMe host.

    Only used for updates. Ignored during creation.


  state (optional, str, present)
    State of the NVMe host.


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
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create NVMe host
      dellemc.powerflex.nvme_host:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        nqn: "{{ nqn }}"
        nvme_host_name: "{{ nvme_host_name }}"
        state: "present"

    - name: Rename nvme_host using NVMe host id
      dellemc.powerflex.nvme_host:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        nvme_host_name: "{{ nvme_host_name }}"
        nvme_host_new_name: "{{ nvme_host_new_name }}"
        state: "present"

    - name: Set maximum number of paths per volume and maximum Number of Ports Per Protection Domain of nvme_host
      dellemc.powerflex.nvme_host:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        nvme_host_name: "{{ nvme_host_name }}"
        max_num_paths: "{{ max_num_paths }}"
        max_num_sys_ports: "{{ max_num_sys_ports }}"
        state: "present"

    - name: Remove nvme_host
      dellemc.powerflex.nvme_host:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        nvme_host_name: "{{ nvme_host_name }}"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


nvme_host_details (When NVMe host exists, dict, {'hostOsFullType': 'Generic', 'systemId': '264ec85b3855280f', 'name': 'name', 'sdcApproved': None, 'sdcAgentActive': None, 'mdmIpAddressesCurrent': None, 'sdcIp': None, 'sdcIps': None, 'osType': None, 'perfProfile': None, 'peerMdmId': None, 'sdtId': None, 'mdmConnectionState': None, 'softwareVersionInfo': None, 'socketAllocationFailure': None, 'memoryAllocationFailure': None, 'versionInfo': None, 'sdcType': None, 'nqn': 'nqn.org.nvmexpress:uuid', 'maxNumPaths': 6, 'maxNumSysPorts': 10, 'sdcGuid': None, 'installedSoftwareVersionInfo': None, 'kernelVersion': None, 'kernelBuildNumber': None, 'sdcApprovedIps': None, 'hostType': 'NVMeHost', 'sdrId': None, 'id': '1040d67200010000', 'links': [{'rel': 'self', 'href': '/api/instances/Host::1040d67200010000'}, {'rel': '/api/Host/relationship/Volume', 'href': '/api/instances/Host::1040d67200010000/relationships/Volume'}, {'rel': '/api/Host/relationship/NvmeController', 'href': '/api/instances/Host::1040d67200010000/relationships/NvmeController'}, {'rel': '/api/parent/relationship/systemId', 'href': '/api/instances/System::264ec85b3855280f'}]})
  Details of the NVMe host.


  hostOsFullType (, str, )
    Full type of the host OS.


  hostType (, str, )
    Type of the host.


  id (, str, )
    ID of the NVMe host.


  installedSoftwareVersionInfo (, str, )
    Installed software version information.


  kernelBuildNumber (, str, )
    Kernel build number.


  kernelVersion (, str, )
    Kernel version.


  links (, list, )
    Links related to the NVMe host.


    href (, str, )
      Hyperlink reference.


    rel (, str, )
      Relation type.



  max_num_paths (, int, )
    Maximum number of paths per volume. Used to create or modify the NVMe host.


  max_num_sys_ports (, int, )
    Maximum number of ports per protection domain. Used to create or modify the NVMe host.


  mdmConnectionState (, str, )
    MDM connection state.


  mdmIpAddressesCurrent (, list, )
    Current MDM IP addresses.


  name (, str, )
    Name of the NVMe host.


  nqn (, str, )
    NQN of the NVMe host. Used to create, get or modify the NVMe host.


  osType (, str, )
    OS type.


  peerMdmId (, str, )
    Peer MDM ID.


  perfProfile (, str, )
    Performance profile.


  sdcAgentActive (, bool, )
    Whether the SDC agent is active.


  sdcApproved (, bool, )
    Whether an SDC has approved access to the system.


  sdcApprovedIps (, list, )
    SDC approved IPs.


  sdcGuid (, str, )
    SDC GUID.


  sdcIp (, str, )
    SDC IP address.


  sdcIps (, list, )
    SDC IP addresses.


  sdcType (, str, )
    SDC type.


  sdrId (, str, )
    SDR ID.


  sdtId (, str, )
    SDT ID.


  softwareVersionInfo (, str, )
    Software version information.


  systemId (, str, )
    ID of the system.


  versionInfo (, str, )
    Version information.






Status
------





Authors
~~~~~~~

- Peter Cao (@P-Cao) <ansible.team@dell.com>

