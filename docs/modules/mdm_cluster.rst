.. _mdm_cluster_module:


mdm_cluster -- Manage MDM cluster on Dell PowerFlex
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing MDM cluster and MDMs on PowerFlex storage system includes adding/removing standby MDM, modify MDM name and virtual interface.

It also includes getting details of MDM cluster, modify MDM cluster ownership, cluster mode, and performance profile.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.12 or later.
- PyPowerFlex 1.6.0.
- Python 3.9, 3.10 or 3.11.



Parameters
----------

  mdm_name (optional, str, None)
    The name of the MDM. It is unique across the PowerFlex array.

    Mutually exclusive with *mdm_id*.

    If mdm_name passed in add standby operation, then same name will be assigned to the new standby mdm.


  mdm_id (optional, str, None)
    The ID of the MDM.

    Mutually exclusive with *mdm_name*.


  mdm_new_name (optional, str, None)
    To rename the MDM.


  standby_mdm (optional, dict, None)
    Specifies add standby MDM parameters.


    mdm_ips (True, list, None)
      List of MDM IPs that will be assigned to new MDM. It can contain IPv4 addresses.


    role (True, str, None)
      Role of new MDM.


    management_ips (optional, list, None)
      List of management IPs to manage MDM. It can contain IPv4 addresses.


    port (optional, int, None)
      Specifies the port of new MDM.


    allow_multiple_ips (optional, bool, None)
      Allow the added node to have different number of IPs from the primary node.


    virtual_interfaces (optional, list, None)
      List of NIC interfaces that will be used for virtual IP addresses.



  is_primary (optional, bool, None)
    Set *is_primary* as ``true`` to change MDM cluster ownership from the current master MDM to different MDM.

    Set *is_primary* as ``false``, will return MDM cluster details.

    New owner MDM must be an MDM with a manager role.


  cluster_mode (optional, str, None)
    Mode of the cluster.


  mdm (optional, list, None)
    Specifies parameters to add/remove MDMs to/from the MDM cluster.


    mdm_id (optional, str, None)
      ID of MDM that will be added/removed to/from the cluster.


    mdm_name (optional, str, None)
      Name of MDM that will be added/removed to/from the cluster.


    mdm_type (True, str, None)
      Type of the MDM.

      Either *mdm_id* or *mdm_name* must be passed with mdm_type.



  mdm_state (optional, str, None)
    Mapping state of MDM.


  virtual_ip_interfaces (optional, list, None)
    List of interfaces to be used for virtual IPs.

    The order of interfaces must be matched with virtual IPs assigned to the cluster.

    Interfaces of the primary and secondary type MDMs are allowed to modify.

    The *virtual_ip_interfaces* is mutually exclusive with *clear_interfaces*.


  clear_interfaces (optional, bool, None)
    Clear all virtual IP interfaces.

    The *clear_interfaces* is mutually exclusive with *virtual_ip_interfaces*.


  performance_profile (optional, str, None)
    Apply performance profile to cluster MDMs.


  state (True, str, None)
    State of the MDM cluster.


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
   - Parameters *mdm_name* or *mdm_id* are mandatory for rename and modify virtual IP interfaces.
   - Parameters *mdm_name* or *mdm_id* are not required while modifying performance profile.
   - For change MDM cluster ownership operation, only changed as True will be returned and for idempotency case MDM cluster details will be returned.
   - Reinstall all SDC after changing ownership to some newly added MDM.
   - To add manager standby MDM, MDM package must be installed with manager role.
   - The *check_mode* is supported.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add a standby MDM
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        mdm_name: "mdm_1"
        standby_mdm:
          mdm_ips:
            - "10.x.x.x"
          role: "TieBreaker"
          management_ips:
            - "10.x.y.z"
        state: "present"

    - name: Remove a standby MDM
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        mdm_name: "mdm_1"
        state: "absent"

    - name: Switch cluster mode from 3 node to 5 node MDM cluster
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        cluster_mode: "FiveNodes"
        mdm:
          - mdm_id: "5f091a8a013f1100"
            mdm_type: "Secondary"
          - mdm_name: "mdm_1"
            mdm_type: "TieBreaker"
        sdc_state: "present-in-cluster"
        state: "present"

    - name: Switch cluster mode from 5 node to 3 node MDM cluster
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        cluster_mode: "ThreeNodes"
        mdm:
          - mdm_id: "5f091a8a013f1100"
            mdm_type: "Secondary"
          - mdm_name: "mdm_1"
            mdm_type: "TieBreaker"
        sdc_state: "absent-in-cluster"
        state: "present"

    - name: Get the details of the MDM cluster
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        state: "present"

    - name: Change ownership of MDM cluster
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        mdm_name: "mdm_2"
        is_primary: True
        state: "present"

    - name: Modify performance profile
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        performance_profile: "HighPerformance"
        state: "present"

    - name: Rename the MDM
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        mdm_name: "mdm_1"
        mdm_new_name: "new_mdm_1"
        state: "present"

    - name: Modify virtual IP interface of the MDM
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        mdm_name: "mdm_1"
        virtual_ip_interface:
            - "ens224"
        state: "present"

    - name: Clear virtual IP interface of the MDM
      dellemc.powerflex.mdm_cluster:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        mdm_name: "mdm_1"
        clear_interfaces: True
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


mdm_cluster_details (When MDM cluster exists, dict, {'clusterState': 'ClusteredNormal', 'clusterMode': 'ThreeNodes', 'goodNodesNum': 3, 'master': {'virtualInterfaces': ['ens1'], 'managementIPs': ['10.x.y.z'], 'ips': ['10.x.y.z'], 'versionInfo': 'R3_6.0.0', 'opensslVersion': 'OpenSSL 1.0.2k-fips  26 Jan 2017', 'role': 'Manager', 'status': 'Normal', 'name': 'sample_mdm', 'id': '5908d328581d1400', 'port': 9011}, 'perfProfile': 'HighPerformance', 'slaves': [{'virtualInterfaces': ['ens1'], 'managementIPs': ['10.x.x.z'], 'ips': ['10.x.x.z'], 'versionInfo': 'R3_6.0.0', 'opensslVersion': 'OpenSSL 1.0.2k-fips  26 Jan 2017', 'role': 'Manager', 'status': 'Normal', 'name': 'sample_mdm1', 'id': '5908d328581d1401', 'port': 9011}], 'tieBreakers': [{'virtualInterfaces': [], 'managementIPs': [], 'ips': ['10.x.y.y'], 'versionInfo': 'R3_6.0.0', 'opensslVersion': 'N/A', 'role': 'TieBreaker', 'status': 'Normal', 'id': '5908d328581d1402', 'port': 9011}], 'standbyMDMs': [{'virtualInterfaces': [], 'managementIPs': ['10.x.z.z'], 'ips': ['10.x.z.z'], 'versionInfo': 'R3_6.0.0', 'opensslVersion': 'N/A', 'role': 'TieBreaker', 'status': 'Normal', 'id': '5908d328581d1403', 'port': 9011}], 'goodReplicasNum': 2, 'id': 'cdd883cf00000002'})
  Details of the MDM cluster.


  id (, str, )
    The ID of the MDM cluster.


  name (, str, )
    Name of MDM cluster.


  clusterMode (, str, )
    Mode of the MDM cluster.


  master (, dict, )
    The details of the master MDM.


    id (, str, )
      ID of the MDM.


    name (, str, )
      Name of the MDM.


    port (, str, )
      Port of the MDM.


    ips (, list, )
      List of IPs for master MDM.


    managementIPs (, list, )
      List of management IPs for master MDM.


    role (, str, )
      Role of MDM.


    status (, str, )
      Status of MDM.


    versionInfo (, str, )
      Version of MDM.


    virtualInterfaces (, list, )
      List of virtual interfaces


    opensslVersion (, str, )
      OpenSSL version.



  slaves (, list, )
    The list of the secondary MDMs.


    id (, str, )
      ID of the MDM.


    name (, str, )
      Name of the MDM.


    port (, str, )
      Port of the MDM.


    ips (, list, )
      List of IPs for secondary MDM.


    managementIPs (, list, )
      List of management IPs for secondary MDM.


    role (, str, )
      Role of MDM.


    status (, str, )
      Status of MDM.


    versionInfo (, str, )
      Version of MDM.


    virtualInterfaces (, list, )
      List of virtual interfaces


    opensslVersion (, str, )
      OpenSSL version.



  tieBreakers (, list, )
    The list of the TieBreaker MDMs.


    id (, str, )
      ID of the MDM.


    name (, str, )
      Name of the MDM.


    port (, str, )
      Port of the MDM.


    ips (, list, )
      List of IPs for tie-breaker MDM.


    managementIPs (, list, )
      List of management IPs for tie-breaker MDM.


    role (, str, )
      Role of MDM.


    status (, str, )
      Status of MDM.


    versionInfo (, str, )
      Version of MDM.


    opensslVersion (, str, )
      OpenSSL version.



  standbyMDMs (, list, )
    The list of the standby MDMs.


    id (, str, )
      ID of the MDM.


    name (, str, )
      Name of the MDM.


    port (, str, )
      Port of the MDM.


    ips (, list, )
      List of IPs for MDM.


    managementIPs (, list, )
      List of management IPs for MDM.


    role (, str, )
      Role of MDM.


    status (, str, )
      Status of MDM.


    versionInfo (, str, )
      Version of MDM.


    virtualInterfaces (, list, )
      List of virtual interfaces.


    opensslVersion (, str, )
      OpenSSL version.



  clusterState (, str, )
    State of the MDM cluster.


  goodNodesNum (, int, )
    Number of Nodes in MDM cluster.


  goodReplicasNum (, int, )
    Number of nodes for Replication.


  virtualIps (, list, )
    List of virtual IPs.






Status
------





Authors
~~~~~~~

- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

