.. _snapshot_module:


snapshot -- Manage Snapshots on Dell PowerFlex
==============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing snapshots on PowerFlex Storage System includes creating, getting details, mapping/unmapping to/from SDC, modifying the attributes and deleting snapshot.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  snapshot_name (optional, str, None)
    The name of the snapshot.

    Mandatory for create operation.

    Specify either \ :emphasis:`snapshot\_name`\  or \ :emphasis:`snapshot\_id`\  (but not both) for any operation.


  snapshot_id (optional, str, None)
    The ID of the Snapshot.


  vol_name (optional, str, None)
    The name of the volume for which snapshot will be taken.

    Specify either \ :emphasis:`vol\_name`\  or \ :emphasis:`vol\_id`\  while creating snapshot.


  vol_id (optional, str, None)
    The ID of the volume.


  read_only (optional, bool, None)
    Specifies whether mapping of the created snapshot volume will have read-write access or limited to read-only access.

    If \ :literal:`true`\ , snapshot is created with read-only access.

    If \ :literal:`false`\ , snapshot is created with read-write access.


  size (optional, int, None)
    The size of the snapshot.


  cap_unit (optional, str, None)
    The unit of the volume size. It defaults to \ :literal:`GB`\ , if not specified.


  snapshot_new_name (optional, str, None)
    New name of the snapshot. Used to rename the snapshot.


  allow_multiple_mappings (optional, bool, None)
    Specifies whether to allow multiple mappings or not.


  desired_retention (optional, int, None)
    The retention value for the Snapshot.

    If the desired\_retention is not mentioned during creation, snapshot will be created with unlimited retention.

    Maximum supported desired retention is 31 days.


  retention_unit (optional, str, None)
    The unit for retention. It defaults to \ :literal:`hours`\ , if not specified.


  sdc (optional, list, None)
    Specifies SDC parameters.


    sdc_name (optional, str, None)
      Name of the SDC.

      Specify either \ :emphasis:`sdc\_name`\ , \ :emphasis:`sdc\_id`\  or \ :emphasis:`sdc\_ip`\ .

      Mutually exclusive with \ :emphasis:`sdc\_id`\  and \ :emphasis:`sdc\_ip`\ .


    sdc_id (optional, str, None)
      ID of the SDC.

      Specify either \ :emphasis:`sdc\_name`\ , \ :emphasis:`sdc\_id`\  or \ :emphasis:`sdc\_ip`\ .

      Mutually exclusive with \ :emphasis:`sdc\_name`\  and \ :emphasis:`sdc\_ip`\ .


    sdc_ip (optional, str, None)
      IP of the SDC.

      Specify either \ :emphasis:`sdc\_name`\ , \ :emphasis:`sdc\_id`\  or \ :emphasis:`sdc\_ip`\ .

      Mutually exclusive with \ :emphasis:`sdc\_id`\  and \ :emphasis:`sdc\_ip`\ .


    access_mode (optional, str, None)
      Define the access mode for all mappings of the snapshot.


    bandwidth_limit (optional, int, None)
      Limit of snapshot network bandwidth.

      Need to mention in multiple of 1024 Kbps.

      To set no limit, 0 is to be passed.


    iops_limit (optional, int, None)
      Limit of snapshot IOPS.

      Minimum IOPS limit is 11 and specify 0 for unlimited iops.



  sdc_state (optional, str, None)
    Mapping state of the SDC.


  remove_mode (optional, str, None)
    Removal mode for the snapshot.

    It defaults to \ :literal:`ONLY\_ME`\ , if not specified.


  state (True, str, None)
    State of the snapshot.


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

    
    - name: Create snapshot
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_name: "ansible_snapshot"
        vol_name: "ansible_volume"
        read_only: false
        desired_retention: 2
        state: "present"

    - name: Get snapshot details using snapshot id
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        state: "present"

    - name: Map snapshot to SDC
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        sdc:
          - sdc_ip: "198.10.xxx.xxx"
          - sdc_id: "663ac0d200000001"
        allow_multiple_mappings: true
        sdc_state: "mapped"
        state: "present"

    - name: Modify the attributes of SDC mapped to snapshot
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        sdc:
          - sdc_ip: "198.10.xxx.xxx"
            iops_limit: 11
            bandwidth_limit: 4096
          - sdc_id: "663ac0d200000001"
            iops_limit: 20
            bandwidth_limit: 2048
        allow_multiple_mappings: true
        sdc_state: "mapped"
        state: "present"

    - name: Extend the size of snapshot
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        size: 16
        state: "present"

    - name: Unmap SDCs from snapshot
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        sdc:
          - sdc_ip: "198.10.xxx.xxx"
          - sdc_id: "663ac0d200000001"
        sdc_state: "unmapped"
        state: "present"

    - name: Rename snapshot
      dellemc.powerflex.snapshot:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        snapshot_id: "fe6cb28200000007"
        snapshot_new_name: "ansible_renamed_snapshot_10"
        state: "present"

    - name: Delete snapshot
      dellemc.powerflex.snapshot:
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


snapshot_details (When snapshot exists, dict, {'accessModeLimit': 'ReadOnly', 'ancestorVolumeId': 'cdd883cf00000002', 'ancestorVolumeName': 'ansible-volume-1', 'autoSnapshotGroupId': None, 'compressionMethod': 'Invalid', 'consistencyGroupId': '22f1e80c00000001', 'creationTime': 1631619229, 'dataLayout': 'MediumGranularity', 'id': 'cdd883d000000004', 'links': [{'href': '/api/instances/Volume::cdd883d000000004', 'rel': 'self'}, {'href': '/api/instances/Volume::cdd883d000000004/relationships /Statistics', 'rel': '/api/Volume/relationship/Statistics'}, {'href': '/api/instances/Volume::cdd883cf00000002', 'rel': '/api/parent/relationship/ancestorVolumeId'}, {'href': '/api/instances/VTree::6e86255c00000001', 'rel': '/api/parent/relationship/vtreeId'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': '/api/parent/relationship/storagePoolId'}], 'lockedAutoSnapshot': False, 'lockedAutoSnapshotMarkedForRemoval': False, 'managedBy': 'ScaleIO', 'mappedSdcInfo': None, 'name': 'ansible_vol_snap_1', 'notGenuineSnapshot': False, 'originalExpiryTime': 0, 'pairIds': None, 'replicationJournalVolume': False, 'replicationTimeStamp': 0, 'retentionInHours': 0, 'retentionLevels': [], 'secureSnapshotExpTime': 0, 'sizeInGb': 16, 'sizeInKb': 16777216, 'snplIdOfAutoSnapshot': None, 'snplIdOfSourceVolume': None, 'storagePoolId': 'e0d8f6c900000000', 'storagePoolName': 'pool1', 'timeStampIsAccurate': False, 'useRmcache': False, 'volumeReplicationState': 'UnmarkedForReplication', 'volumeType': 'Snapshot', 'vtreeId': '6e86255c00000001'})
  Details of the snapshot.


  ancestorVolumeId (, str, )
    The ID of the root of the specified volume's V-Tree.


  ancestorVolumeName (, str, )
    The name of the root of the specified volume's V-Tree.


  creationTime (, int, )
    The creation time of the snapshot.


  id (, str, )
    The ID of the snapshot.


  mappedSdcInfo (, dict, )
    The details of the mapped SDC.


    sdcId (, str, )
      ID of the SDC.


    sdcName (, str, )
      Name of the SDC.


    sdcIp (, str, )
      IP of the SDC.


    accessMode (, str, )
      Mapping access mode for the specified snapshot.


    limitIops (, int, )
      IOPS limit for the SDC.


    limitBwInMbps (, int, )
      Bandwidth limit for the SDC.



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

- Akash Shendge (@shenda1) <ansible.team@dell.com>

