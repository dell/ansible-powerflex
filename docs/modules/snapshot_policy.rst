.. _snapshot_policy_module:


snapshot_policy -- Manage snapshot policies on Dell PowerFlex
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing snapshot policies on PowerFlex storage system includes creating, getting details, modifying attributes, adding a source volume, removing a source volume and deleting a snapshot policy.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  snapshot_policy_name (optional, str, None)
    The name of the snapshot policy.

    It is unique across the PowerFlex array.

    Mutually exclusive with \ :emphasis:`snapshot\_policy\_id`\ .


  snapshot_policy_id (optional, str, None)
    The unique identifier of the snapshot policy.

    Except create operation, all other operations can be performed using \ :emphasis:`snapshot\_policy\_id`\ .

    Mutually exclusive with \ :emphasis:`snapshot\_policy\_name`\ .


  auto_snapshot_creation_cadence (optional, dict, None)
    The auto snapshot creation cadence of the snapshot policy.


    time (optional, int, None)
      The time between creation of two snapshots.


    unit (optional, str, Minute)
      The unit of the auto snapshot creation cadence.



  num_of_retained_snapshots_per_level (optional, list, None)
    Number of retained snapshots per level.


  new_name (optional, str, None)
    New name of the snapshot policy.


  access_mode (optional, str, None)
    Access mode of the snapshot policy.


  secure_snapshots (optional, bool, None)
    Whether to secure snapshots or not.

    Used only in the create operation.


  source_volume (optional, list, None)
    The source volume details to be added or removed.


    id (optional, str, None)
      The unique identifier of the source volume to be added or removed.

      Mutually exclusive with \ :emphasis:`name`\ .


    name (optional, str, None)
      The name of the source volume to be added or removed.

      Mutually exclusive with \ :emphasis:`id`\ .


    auto_snap_removal_action (optional, str, None)
      Ways to handle the snapshots created by the policy (auto snapshots).

      Must be provided when \ :emphasis:`state`\  is set to \ :literal:`'absent'`\ .


    detach_locked_auto_snapshots (optional, bool, None)
      Whether to detach the locked auto snapshots during removal of source volume.


    state (optional, str, present)
      The state of the source volume.

      When \ :literal:`present`\ , source volume will be added to the snapshot policy.

      When \ :literal:`absent`\ , source volume will be removed from the snapshot policy.



  pause (optional, bool, None)
    Whether to pause or resume the snapshot policy.


  state (optional, str, present)
    State of the snapshot policy.


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
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a snapshot policy
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "snapshot_policy_name_1"
        access_mode: "READ_WRITE"
        secure_snapshots: false
        auto_snapshot_creation_cadence:
          time: 1
          unit: "Hour"
        num_of_retained_snapshots_per_level:
          - 20
        state: "present"

    - name: Get snapshot policy details using name
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "snapshot_policy_name_1"

    - name: Get snapshot policy details using id
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_id: "snapshot_policy_id_1"

    - name: Modify a snapshot policy
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "snapshot_policy_name_1"
        auto_snapshot_creation_cadence:
          time: 2
          unit: "Hour"
        num_of_retained_snapshots_per_level:
          - 40

    - name: Rename a snapshot policy
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "snapshot_policy_name_1"
        new_name: "snapshot_policy_name_1_new"

    - name: Add source volume
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "snapshot_policy_name_1"
        source_volume:
          - name: "source_volume_name_1"
          - id: "source_volume_id_2"
            state: "present"

    - name: Remove source volume
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "{{snapshot_policy_name}}"
        source_volume:
          - name: "source_volume_name_1"
            auto_snap_removal_action: 'Remove'
            state: "absent"
          - id: "source_volume_id_2"
            auto_snap_removal_action: 'Remove'
            detach_locked_auto_snapshots: true
            state: "absent"

    - name: Pause a snapshot policy
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "{{snapshot_policy_name}}"
        pause: true

    - name: Resume a snapshot policy
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "{{snapshot_policy_name}}"
        pause: false

    - name: Delete a snapshot policy
      dellemc.powerflex.snapshot_policy:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_policy_name: "snapshot_policy_name"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


snapshot_policy_details (When snapshot policy exists, dict, {'autoSnapshotCreationCadenceInMin': 120, 'id': '15ae842800000004', 'lastAutoSnapshotCreationFailureReason': 'NR', 'lastAutoSnapshotFailureInFirstLevel': False, 'links': [{'href': '/api/instances/SnapshotPolicy::15ae842800000004', 'rel': 'self'}, {'href': '/api/instances/SnapshotPolicy::15ae842800000004/relationships/Statistics', 'rel': '/api/SnapshotPolicy/relationship/Statistics'}, {'href': '/api/instances/SnapshotPolicy::15ae842800000004/relationships/SourceVolume', 'rel': '/api/SnapshotPolicy/relationship/SourceVolume'}, {'href': '/api/instances/SnapshotPolicy::15ae842800000004/relationships/AutoSnapshotVolume', 'rel': '/api/SnapshotPolicy/relationship/AutoSnapshotVolume'}, {'href': '/api/instances/System::0e7a082862fedf0f', 'rel': '/api/parent/relationship/systemId'}], 'maxVTreeAutoSnapshots': 40, 'name': 'Sample_snapshot_policy_1', 'nextAutoSnapshotCreationTime': 1683709201, 'numOfAutoSnapshots': 0, 'numOfCreationFailures': 0, 'numOfExpiredButLockedSnapshots': 0, 'numOfLockedSnapshots': 0, 'numOfRetainedSnapshotsPerLevel': [40], 'numOfSourceVolumes': 0, 'secureSnapshots': False, 'snapshotAccessMode': 'ReadWrite', 'snapshotPolicyState': 'Active', 'statistics': {'autoSnapshotVolIds': [], 'expiredButLockedSnapshotsIds': [], 'numOfAutoSnapshots': 0, 'numOfExpiredButLockedSnapshots': 0, 'numOfSrcVols': 0, 'srcVolIds': []}, 'systemId': '0e7a082862fedf0f', 'timeOfLastAutoSnapshot': 0, 'timeOfLastAutoSnapshotCreationFailure': 0})
  Details of the snapshot policy.


  autoSnapshotCreationCadenceInMin (, int, )
    The snapshot rule of the snapshot policy.


  id (, str, )
    The ID of the snapshot policy.


  lastAutoSnapshotCreationFailureReason (, str, )
    The reason for the failure of last auto snapshot creation .


  name (, str, )
    Name of the snapshot policy.


  lastAutoSnapshotFailureInFirstLevel (, bool, )
    Whether the last auto snapshot in first level failed.


  maxVTreeAutoSnapshots (, int, )
    Maximum number of VTree auto snapshots.


  nextAutoSnapshotCreationTime (, int, )
    The time of creation of the next auto snapshot.


  numOfAutoSnapshots (, int, )
    Number of auto snapshots.


  numOfCreationFailures (, int, )
    Number of creation failures.


  numOfExpiredButLockedSnapshots (, int, )
    Number of expired but locked snapshots.


  numOfLockedSnapshots (, int, )
    Number of locked snapshots.


  numOfRetainedSnapshotsPerLevel (, list, )
    Number of snapshots retained per level


  numOfSourceVolumes (, int, )
    Number of source volumes.


  secureSnapshots (, bool, )
    Whether the snapshots are secured.


  snapshotAccessMode (, str, )
    Access mode of the snapshots.


  snapshotPolicyState (, str, )
    State of the snapshot policy.


  systemId (, str, )
    Unique identifier of the PowerFlex system.


  timeOfLastAutoSnapshot (, str, )
    Time of the last auto snapshot creation.


  timeOfLastAutoSnapshotCreationFailure (, str, )
    Time of the failure of the last auto snapshot creation.


  statistics (, dict, )
    Statistics details of the snapshot policy.


    autoSnapshotVolIds (, list, )
      Volume Ids of all the auto snapshots.


    expiredButLockedSnapshotsIds (, list, )
      Ids of expired but locked snapshots.


    numOfAutoSnapshots (, int, )
      Number of auto snapshots.


    numOfExpiredButLockedSnapshots (, int, )
      Number of expired but locked snapshots.


    numOfSrcVols (, int, )
      Number of source volumes.


    srcVolIds (, list, )
      Ids of the source volumes.







Status
------





Authors
~~~~~~~

- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

