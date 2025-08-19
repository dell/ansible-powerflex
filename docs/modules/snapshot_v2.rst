.. _snapshot_v2_module:


snapshot_v2 -- Manage Snapshots on Dell PowerFlex
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing snapshots on PowerFlex Storage System includes creating, getting details, modifying the attributes and deleting snapshot.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

  snapshot_name (optional, str, None)
    The name of the snapshot.

    Mandatory for create operation.

    Specify either :emphasis:`snapshot\_name` or :emphasis:`snapshot\_id` (but not both) for any operation.


  snapshot_id (optional, str, None)
    The ID of the Snapshot.


  vol_name (optional, str, None)
    The name of the volume for which snapshot will be taken.

    Specify either :emphasis:`vol\_name` or :emphasis:`vol\_id` while creating snapshot.


  vol_id (optional, str, None)
    The ID of the volume.


  snapshot_new_name (optional, str, None)
    New name of the snapshot. Used to rename the snapshot.


  desired_retention (optional, int, None)
    The retention value for the Snapshot.

    If the desired\_retention is not mentioned during creation, snapshot will be created with unlimited retention.

    Maximum supported desired retention is 31 days.


  retention_unit (optional, str, None)
    The unit for retention. It defaults to :literal:`hours`\ , if not specified.


  remove_mode (optional, str, None)
    Removal mode for the snapshot.

    It defaults to :literal:`ONLY\_ME`\ , if not specified.


  state (optional, str, present)
    State of the snapshot.


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
   - Snapshots are read-only since PowerFlex 5.0.0
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create snapshot
      dellemc.powerflex.snapshot_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_name: "ansible_snapshot"
        vol_name: "ansible_volume"
        desired_retention: 2
        state: "present"

    - name: Get snapshot details using snapshot id
      dellemc.powerflex.snapshot_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        state: "present"

    - name: Rename snapshot
      dellemc.powerflex.snapshot_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        snapshot_new_name: "ansible_renamed_snapshot_10"
        state: "present"

    - name: Delete snapshot
      dellemc.powerflex.snapshot_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        remove_mode: "ONLY_ME"
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


snapshot_details (When snapshot exists, dict, {'accessModeLimit': 'ReadOnly', 'ancestorVolumeId': 'cdd883cf00000002', 'ancestorVolumeName': 'ansible-volume-1', 'autoSnapshotGroupId': None, 'compressionMethod': 'Invalid', 'consistencyGroupId': '22f1e80c00000001', 'creationTime': 1631619229, 'dataLayout': 'MediumGranularity', 'genType': 'EC', 'id': 'cdd883d000000004', 'links': [{'href': '/api/instances/Volume::cdd883d000000004', 'rel': 'self'}, {'href': '/api/instances/Volume::cdd883d000000004/relationships /Statistics', 'rel': '/api/Volume/relationship/Statistics'}, {'href': '/api/instances/Volume::cdd883cf00000002', 'rel': '/api/parent/relationship/ancestorVolumeId'}, {'href': '/api/instances/VTree::6e86255c00000001', 'rel': '/api/parent/relationship/vtreeId'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': '/api/parent/relationship/storagePoolId'}], 'lockedAutoSnapshot': False, 'lockedAutoSnapshotMarkedForRemoval': False, 'managedBy': 'ScaleIO', 'mappedSdcInfo': None, 'name': 'ansible_vol_snap_1', 'notGenuineSnapshot': False, 'nsid': 23, 'originalExpiryTime': 0, 'pairIds': None, 'replicationJournalVolume': False, 'replicationTimeStamp': 0, 'retentionInHours': 0, 'retentionLevels': [], 'secureSnapshotExpTime': 0, 'sizeInGb': 16, 'sizeInKb': 16777216, 'snplIdOfAutoSnapshot': None, 'snplIdOfSourceVolume': None, 'storagePoolId': 'e0d8f6c900000000', 'storagePoolName': 'pool1', 'timeStampIsAccurate': False, 'useRmcache': False, 'volumeClass': 'defaultclass', 'volumeReplicationState': 'UnmarkedForReplication', 'volumeType': 'Snapshot', 'vtreeId': '6e86255c00000001'})
  Details of the snapshot.


  ancestorVolumeId (, str, )
    The ID of the root of the specified volume's V-Tree.


  ancestorVolumeName (, str, )
    The name of the root of the specified volume's V-Tree.


  creationTime (, int, )
    The creation time of the snapshot.


  id (, str, )
    The ID of the snapshot.


  name (, str, )
    Name of the snapshot.


  secureSnapshotExpTime (, int, )
    Expiry time of the snapshot.


  sizeInKb (, int, )
    Size of the snapshot.


  sizeInGb (, int, )
    Size of the snapshot.


  retentionInHours (, int, )
    Retention of the snapshot in hours.


  storagePoolId (, str, )
    The ID of the Storage pool in which snapshot resides.


  storagePoolName (, str, )
    The name of the Storage pool in which snapshot resides.






Status
------





Authors
~~~~~~~

- Yuhao Liu (@RayLiu7) <ansible.team@dell.com>

