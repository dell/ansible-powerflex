.. _replication_consistency_group_module:


replication_consistency_group -- Manage replication consistency groups on Dell PowerFlex
========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing replication consistency groups on PowerFlex storage system includes getting details, creating, modifying, creating snapshots, pause, resume, freeze, unfreeze, activate, failover, reverse, restore, sync, switchover, inactivate and deleting a replication consistency group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  rcg_name (optional, str, None)
    The name of the replication consistency group.

    It is unique across the PowerFlex array.

    Mutually exclusive with \ :emphasis:`rcg\_id`\ .


  rcg_id (optional, str, None)
    The ID of the replication consistency group.

    Mutually exclusive with \ :emphasis:`rcg\_name`\ .


  create_snapshot (optional, bool, None)
    Whether to create the snapshot of the replication consistency group.


  rpo (optional, int, None)
    Desired RPO in seconds.


  protection_domain_id (optional, str, None)
    Protection domain id.

    Mutually exclusive with \ :emphasis:`protection\_domain\_name`\ .


  protection_domain_name (optional, str, None)
    Protection domain name.

    Mutually exclusive with \ :emphasis:`protection\_domain\_id`\ .


  activity_mode (optional, str, None)
    Activity mode of RCG.

    This parameter is supported for version 3.6 and above.


  pause (optional, bool, None)
    Pause or resume the RCG.

    This parameter is deprecated. Use rcg\_state instead.


  rcg_state (optional, str, None)
    Specify an action for RCG.

    Failover the RCG.

    Reverse the RCG.

    Restore the RCG.

    Switchover the RCG.

    Pause or resume the RCG.

    Freeze or unfreeze the RCG.

    Synchronize the RCG.


  force (optional, bool, None)
    Force switchover the RCG.


  freeze (optional, bool, None)
    Freeze or unfreeze the RCG.

    This parameter is deprecated. Use rcg\_state instead.


  pause_mode (optional, str, None)
    Pause mode.

    It is required if pause is set as true.


  target_volume_access_mode (optional, str, None)
    Target volume access mode.


  is_consistent (optional, bool, None)
    Consistency of RCG.


  new_rcg_name (optional, str, None)
    Name of RCG to rename to.


  remote_peer (optional, dict, None)
    Remote peer system.


    hostname (True, str, None)
      IP or FQDN of the remote peer gateway host.


    username (True, str, None)
      The username of the remote peer gateway host.


    password (True, str, None)
      The password of the remote peer gateway host.


    validate_certs (optional, bool, True)
      Boolean variable to specify whether or not to validate SSL certificate.

      \ :literal:`true`\  - Indicates that the SSL certificate should be verified.

      \ :literal:`false`\  - Indicates that the SSL certificate should not be verified.


    port (optional, int, 443)
      Port number through which communication happens with remote peer gateway host.


    timeout (optional, int, 120)
      Time after which connection will get terminated.

      It is to be mentioned in seconds.


    protection_domain_id (optional, str, None)
      Remote protection domain id.

      Mutually exclusive with \ :emphasis:`protection\_domain\_name`\ .


    protection_domain_name (optional, str, None)
      Remote protection domain name.

      Mutually exclusive with \ :emphasis:`protection\_domain\_id`\ .



  state (optional, str, present)
    State of the replication consistency group.


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
   - Idempotency is not supported for create snapshot operation.
   - There is a delay in reflection of final state of RCG after few update operations on RCG.
   - In 3.6 and above, the replication consistency group will return back to consistent mode on changing to inconsistent mode if consistence barrier arrives. Hence idempotency on setting to inconsistent mode will return changed as true.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

    - name: Get RCG details
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "{{rcg_name}}"

    - name: Create a snapshot of the RCG
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_id: "{{rcg_id}}"
        create_snapshot: true
        state: "present"

    - name: Create a replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rpo: 60
        protection_domain_name: "domain1"
        activity_mode: "active"
        remote_peer:
          hostname: "{{hostname}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          port: "{{port}}"
          protection_domain_name: "domain1"

    - name: Modify replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rpo: 60
        target_volume_access_mode: "ReadOnly"
        activity_mode: "Inactive"
        is_consistent: true

    - name: Rename replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        new_rcg_name: "rcg_test_rename"

    - name: Pause replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "pause"
        pause_mode: "StopDataTransfer"

    - name: Resume replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "resume"

    - name: Freeze replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "freeze"

    - name: UnFreeze replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "unfreeze"

    - name: Failover replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "failover"

    - name: Reverse replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "reverse"

    - name: Restore replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "restore"

    - name: Switchover replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "switchover"

    - name: Synchronize replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        rcg_state: "sync"

    - name: Delete replication consistency group
      dellemc.powerflex.replication_consistency_group:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "rcg_test"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


replication_consistency_group_details (When replication consistency group exists, dict, {'protectionDomainId': 'b969400500000000', 'peerMdmId': '6c3d94f600000000', 'remoteId': '2130961a00000000', 'remoteMdmId': '0e7a082862fedf0f', 'currConsistMode': 'Consistent', 'freezeState': 'Unfrozen', 'lifetimeState': 'Normal', 'pauseMode': 'None', 'snapCreationInProgress': False, 'lastSnapGroupId': 'e58280b300000001', 'lastSnapCreationRc': 'SUCCESS', 'targetVolumeAccessMode': 'NoAccess', 'remoteProtectionDomainId': '4eeb304600000000', 'remoteProtectionDomainName': 'domain1', 'failoverType': 'None', 'failoverState': 'None', 'activeLocal': True, 'activeRemote': True, 'abstractState': 'Ok', 'localActivityState': 'Active', 'remoteActivityState': 'Active', 'inactiveReason': 11, 'rpoInSeconds': 30, 'replicationDirection': 'LocalToRemote', 'disasterRecoveryState': 'None', 'remoteDisasterRecoveryState': 'None', 'error': 65, 'name': 'test_rcg', 'type': 'User', 'id': 'aadc17d500000000'})
  Details of the replication consistency group.


  id (, str, )
    The ID of the replication consistency group.


  name (, str, )
    The name of the replication consistency group.


  protectionDomainId (, str, )
    The Protection Domain ID of the replication consistency group.


  peerMdmId (, str, )
    The ID of the peer MDM of the replication consistency group.


  remoteId (, str, )
    The ID of the remote replication consistency group.


  remoteMdmId (, str, )
    The ID of the remote MDM of the replication consistency group.


  currConsistMode (, str, )
    The current consistency mode of the replication consistency group.


  freezeState (, str, )
    The freeze state of the replication consistency group.


  lifetimeState (, str, )
    The Lifetime state of the replication consistency group.


  pauseMode (, str, )
    The Lifetime state of the replication consistency group.


  snapCreationInProgress (, bool, )
    Whether the process of snapshot creation of the replication consistency group is in progress or not.


  lastSnapGroupId (, str, )
    ID of the last snapshot of the replication consistency group.


  lastSnapCreationRc (, int, )
    The return code of the last snapshot of the replication consistency group.


  targetVolumeAccessMode (, str, )
    The access mode of the target volume of the replication consistency group.


  remoteProtectionDomainId (, str, )
    The ID of the remote Protection Domain.


  remoteProtectionDomainName (, str, )
    The Name of the remote Protection Domain.


  failoverType (, str, )
    The type of failover of the replication consistency group.


  failoverState (, str, )
    The state of failover of the replication consistency group.


  activeLocal (, bool, )
    Whether the local replication consistency group is active.


  activeRemote (, bool, )
    Whether the remote replication consistency group is active


  abstractState (, str, )
    The abstract state of the replication consistency group.


  localActivityState (, str, )
    The state of activity of the local replication consistency group.


  remoteActivityState (, str, )
    The state of activity of the remote replication consistency group..


  inactiveReason (, int, )
    The reason for the inactivity of the replication consistency group.


  rpoInSeconds (, int, )
    The RPO value of the replication consistency group in seconds.


  replicationDirection (, str, )
    The direction of the replication of the replication consistency group.


  disasterRecoveryState (, str, )
    The state of disaster recovery of the local replication consistency group.


  remoteDisasterRecoveryState (, str, )
    The state of disaster recovery of the remote replication consistency group.


  error (, int, )
    The error code of the replication consistency group.


  type (, str, )
    The type of the replication consistency group.






Status
------





Authors
~~~~~~~

- Trisha Datta (@Trisha-Datta) <ansible.team@dell.com>
- Jennifer John (@Jennifer-John) <ansible.team@dell.com>

