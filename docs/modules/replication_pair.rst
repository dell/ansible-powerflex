.. _replication_pair_module:


replication_pair -- Manage replication pairs on Dell PowerFlex
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing replication pairs on PowerFlex storage system includes getting details, creating, pause, resume initial copy and deleting a replication pair.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  pair_id (optional, str, None)
    The ID of the replication pair.

    Mutually exclusive with \ :emphasis:`pair\_name`\ .


  pair_name (optional, str, None)
    The name of the replication pair.

    Mutually exclusive with \ :emphasis:`pair\_id`\ .


  rcg_name (optional, str, None)
    The name of the replication consistency group.

    Mutually exclusive with \ :emphasis:`rcg\_id`\ .


  rcg_id (optional, str, None)
    The ID of the replication consistency group.

    Mutually exclusive with \ :emphasis:`rcg\_name`\ .


  pause (optional, bool, None)
    Pause or resume the initial copy of replication pair.


  pairs (optional, list, None)
    List of replication pairs to add to rcg.


    source_volume_id (optional, str, None)
      Source volume ID.

      Mutually exclusive with \ :emphasis:`source\_volume\_name`\ .


    source_volume_name (optional, str, None)
      Source volume name.

      Mutually exclusive with \ :emphasis:`source\_volume\_id`\ .


    target_volume_id (optional, str, None)
      Target volume ID.

      Mutually exclusive with \ :emphasis:`target\_volume\_name`\ .


    target_volume_name (optional, str, None)
      Target volume name.

      If specified, \ :emphasis:`remote\_peer`\  details should also be specified.

      Mutually exclusive with \ :emphasis:`target\_volume\_id`\ .


    copy_type (True, str, None)
      Copy type.


    name (optional, str, None)
      Name of replication pair.



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



  state (optional, str, present)
    State of the replication pair.


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
   - In 4.0 the creation of replication pair fails when \ :emphasis:`copy\_type`\  is specified as \ :literal:`OfflineCopy`\ .
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get replication pair details
      dellemc.powerflex.replication_pair:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        pair_id: "123"

    - name: Create a replication pair
      dellemc.powerflex.replication_pair:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "test_rcg"
        pairs:
          - source_volume_id: "002"
            target_volume_id: "001"
            copy_type: "OnlineCopy"
            name: "pair1"

    - name: Create a replication pair with target volume name
      dellemc.powerflex.replication_pair:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        rcg_name: "test_rcg"
        pairs:
          - source_volume_name: "src_vol"
            target_volume_name: "dest_vol"
            copy_type: "OnlineCopy"
            name: "pair1"
        remote_peer:
          hostname: "{{hostname}}"
          username: "{{username}}"
          password: "{{password}}"
          validate_certs: "{{validate_certs}}"
          port: "{{port}}"

    - name: Pause replication pair
      dellemc.powerflex.replication_pair:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        pair_name: "pair1"
        pause: true

    - name: Resume replication pair
      dellemc.powerflex.replication_pair:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        pair_name: "pair1"
        pause: false

    - name: Delete replication pair
      dellemc.powerflex.replication_pair:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        pair_name: "pair1"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


replication_pair_details (When replication pair exists, dict, {'copyType': 'OnlineCopy', 'id': '23aa0bc900000001', 'initialCopyPriority': -1, 'initialCopyState': 'Done', 'lifetimeState': 'Normal', 'localActivityState': 'RplEnabled', 'localVolumeId': 'e2bc1fab00000008', 'localVolumeName': 'vol1', 'name': None, 'peerSystemName': None, 'remoteActivityState': 'RplEnabled', 'remoteCapacityInMB': 8192, 'remoteId': 'a058446700000001', 'remoteVolumeId': '1cda7af20000000d', 'remoteVolumeName': 'vol', 'replicationConsistencyGroupId': 'e2ce036b00000002', 'userRequestedPauseTransmitInitCopy': False})
  Details of the replication pair.


  id (, str, )
    The ID of the replication pair.


  name (, str, )
    The name of the replication pair.


  remoteId (, str, )
    The ID of the remote replication pair.


  localVolumeId (, str, )
    The ID of the local volume.


  localVolumeName (, str, )
    The name of the local volume.


  replicationConsistencyGroupId (, str, )
    The ID of the replication consistency group.


  copyType (, str, )
    The copy type of the replication pair.


  initialCopyState (, str, )
    The inital copy state of the replication pair.


  localActivityState (, str, )
    The state of activity of the local replication pair.


  remoteActivityState (, str, )
    The state of activity of the remote replication pair.


  initialCopyPriority (, int, )
    Initial copy priority.


  lifetimeState (, int, )
    Lifetime state of replication pair.


  peerSystemName (, int, )
    Peer system name.


  remoteCapacityInMB (, int, )
    Remote Capacity in MB.


  userRequestedPauseTransmitInitCopy (, int, )
    Value of user requested pause transmit initial copy.


  remoteVolumeId (, int, )
    Remote Volume ID.


  remoteVolumeName (, int, )
    Remote Volume Name.



rcg_replication_pairs (When rcg exists, list, [{'copyType': 'OnlineCopy', 'id': '23aa0bc900000001', 'initialCopyPriority': -1, 'initialCopyState': 'Done', 'lifetimeState': 'Normal', 'localActivityState': 'RplEnabled', 'localVolumeId': 'e2bc1fab00000008', 'localVolumeName': 'vol1', 'name': None, 'peerSystemName': None, 'remoteActivityState': 'RplEnabled', 'remoteCapacityInMB': 8192, 'remoteId': 'a058446700000001', 'remoteVolumeId': '1cda7af20000000d', 'remoteVolumeName': 'vol', 'replicationConsistencyGroupId': 'e2ce036b00000002', 'userRequestedPauseTransmitInitCopy': False}])
  Details of the replication pairs of rcg.


  id (, str, )
    The ID of the replication pair.


  name (, str, )
    The name of the replication pair.


  remoteId (, str, )
    The ID of the remote replication pair.


  localVolumeId (, str, )
    The ID of the local volume.


  localVolumeName (, str, )
    The name of the local volume.


  replicationConsistencyGroupId (, str, )
    The ID of the replication consistency group.


  copyType (, str, )
    The copy type of the replication pair.


  initialCopyState (, str, )
    The inital copy state of the replication pair.


  localActivityState (, str, )
    The state of activity of the local replication pair.


  remoteActivityState (, str, )
    The state of activity of the remote replication pair.


  initialCopyPriority (, int, )
    Initial copy priority.


  lifetimeState (, int, )
    Lifetime state of replication pair.


  peerSystemName (, int, )
    Peer system name.


  remoteCapacityInMB (, int, )
    Remote Capacity in MB.


  userRequestedPauseTransmitInitCopy (, int, )
    Value of user requested pause transmit initial copy.


  remoteVolumeId (, int, )
    Remote Volume ID.


  remoteVolumeName (, int, )
    Remote Volume Name.






Status
------





Authors
~~~~~~~

- Jennifer John (@Jennifer-John) <ansible.team@dell.com>

