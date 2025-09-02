.. _volume_v2_module:


volume_v2 -- Manage volumes on Dell PowerFlex
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing volumes on PowerFlex storage system includes creating, getting details, modifying attributes and deleting volume.

It also includes adding/removing snapshot policy, mapping/unmapping volume to/from SDC and listing associated snapshots.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 5.0 or later.
- PyPowerFlex 2.0.0



Parameters
----------

  vol_name (optional, str, None)
    The name of the volume.

    Mandatory for create operation.

    It is unique across the PowerFlex array.

    Mutually exclusive with :emphasis:`vol\_id`.


  vol_id (optional, str, None)
    The ID of the volume.

    Except create operation, all other operations can be performed using :emphasis:`vol\_id`.

    Mutually exclusive with :emphasis:`vol\_name`.


  storage_pool_name (optional, str, None)
    The name of the storage pool.

    Either name or the id of the storage pool is required for creating a volume.

    During creation, if storage pool name is provided then either protection domain name or id must be mentioned along with it.

    Mutually exclusive with :emphasis:`storage\_pool\_id`.


  storage_pool_id (optional, str, None)
    The ID of the storage pool.

    Either name or the id of the storage pool is required for creating a volume.

    Mutually exclusive with :emphasis:`storage\_pool\_name`.


  protection_domain_name (optional, str, None)
    The name of the protection domain.

    During creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.

    Mutually exclusive with :emphasis:`protection\_domain\_id`.


  protection_domain_id (optional, str, None)
    The ID of the protection domain.

    During creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.

    Mutually exclusive with :emphasis:`protection\_domain\_name`.


  vol_type (optional, str, None)
    Type of volume provisioning.


  snapshot_policy_name (optional, str, None)
    Name of the snapshot policy.

    To remove/detach snapshot policy, empty :emphasis:`snapshot\_policy\_id`\ /\ :emphasis:`snapshot\_policy\_name` is to be passed along with :emphasis:`auto\_snap\_remove\_type`.


  snapshot_policy_id (optional, str, None)
    ID of the snapshot policy.

    To remove/detach snapshot policy, empty :emphasis:`snapshot\_policy\_id`\ /\ :emphasis:`snapshot\_policy\_name` is to be passed along with :emphasis:`auto\_snap\_remove\_type`.


  auto_snap_remove_type (optional, str, None)
    Whether to remove or detach the snapshot policy.

    To remove/detach snapshot policy, empty :emphasis:`snapshot\_policy\_id`\ /\ :emphasis:`snapshot\_policy\_name` is to be passed along with :emphasis:`auto\_snap\_remove\_type`.

    If the snapshot policy name/id is passed empty then :emphasis:`auto\_snap\_remove\_type` is defaulted to :literal:`detach`.


  size (optional, int, None)
    The size of the volume.

    Size of the volume will be assigned as higher multiple of 8 GB.


  cap_unit (optional, str, None)
    The unit of the volume size. It defaults to 'GB'.


  vol_new_name (optional, str, None)
    New name of the volume. Used to rename the volume.


  refresh_src_vol_id (optional, str, None)
    ID of the source volume/snapshot to refresh from.

    Either the name or the id of the source volume/snapshot is required

    Mutually exclusive with :emphasis:`refresh\_src\_vol\_name`.


  refresh_src_vol_name (optional, str, None)
    Name of the source volume/snapshot to refresh from.

    Either the name or the id of the source volume/snapshot is required

    Mutually exclusive with :emphasis:`refresh\_src\_vol\_id`.


  restore_src_vol_id (optional, str, None)
    ID of the source volume/snapshot to restore from.

    Either the name or the id of the source volume/snapshot is required

    Mutually exclusive with :emphasis:`restore\_src\_vol\_name`.


  restore_src_vol_name (optional, str, None)
    Name of the source volume/snapshot to restore from.

    Either the name or the id of the source volume/snapshot is required

    Mutually exclusive with :emphasis:`restore\_src\_vol\_id`.


  allow_multiple_mappings (optional, bool, None)
    Specifies whether to allow or not allow multiple mappings.

    If the volume is mapped to one SDC then for every new mapping :emphasis:`allow\_multiple\_mappings` has to be passed as true.


  sdc (optional, list, None)
    Specifies SDC parameters.


    sdc_name (optional, str, None)
      Name of the SDC.

      Specify either :emphasis:`sdc\_name`\ , :emphasis:`sdc\_id` or :emphasis:`sdc\_ip`.

      Mutually exclusive with :emphasis:`sdc\_id` and :emphasis:`sdc\_ip`.


    sdc_id (optional, str, None)
      ID of the SDC.

      Specify either :emphasis:`sdc\_name`\ , :emphasis:`sdc\_id` or :emphasis:`sdc\_ip`.

      Mutually exclusive with :emphasis:`sdc\_name` and :emphasis:`sdc\_ip`.


    sdc_ip (optional, str, None)
      IP of the SDC.

      Specify either :emphasis:`sdc\_name`\ , :emphasis:`sdc\_id` or :emphasis:`sdc\_ip`.

      Mutually exclusive with :emphasis:`sdc\_id` and :emphasis:`sdc\_ip`.


    access_mode (optional, str, None)
      Define the access mode for all mappings of the volume.


    bandwidth_limit (optional, int, None)
      Limit of volume network bandwidth.

      Need to mention in multiple of 1024 Kbps.

      To set no limit, 0 is to be passed.


    iops_limit (optional, int, None)
      Limit of volume IOPS.

      Minimum IOPS limit is 11 and specify 0 for unlimited iops.



  sdc_state (optional, str, None)
    Mapping state of the SDC.


  delete_snapshots (optional, bool, None)
    If :literal:`true`\ , the volume and all its dependent snapshots will be deleted.

    If :literal:`false`\ , only the volume will be deleted.

    It can be specified only when the :emphasis:`state` is :literal:`absent`.

    It defaults to :literal:`false`\ , if not specified.


  state (True, str, None)
    State of the volume.


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
   - Compression\_type and use\_rmcache are not supported since PowerFlex 5.0.0
   - Refresh and restore cannot be conducted in the same task.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        storage_pool_name: "pool_1"
        protection_domain_name: "pd_1"
        vol_type: "THIN_PROVISIONED"
        size: 16
        state: "present"

    - name: Map a SDC to volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        allow_multiple_mappings: true
        sdc:
          - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
            access_mode: "READ_WRITE"
        sdc_state: "mapped"
        state: "present"

    - name: Unmap a SDC to volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        sdc:
          - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
        sdc_state: "unmapped"
        state: "present"

    - name: Map multiple SDCs to a volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        protection_domain_name: "pd_1"
        sdc:
          - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
            access_mode: "READ_WRITE"
            bandwidth_limit: 2048
            iops_limit: 20
          - sdc_ip: "198.10.xxx.xxx"
            access_mode: "READ_ONLY"
        allow_multiple_mappings: true
        sdc_state: "mapped"
        state: "present"

    - name: Get the details of the volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_id: "fe6c8b7100000005"
        state: "present"

    - name: Restore volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        restore_src_vol_id: "fe6c8b7100000006"
        state: "present"

    - name: Refresh volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        refresh_src_vol_name: "example_snapshot"
        state: "present"

    - name: Modify the details of the Volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        storage_pool_name: "pool_1"
        vol_new_name: "new_sample_volume"
        size: 64
        state: "present"

    - name: Delete the Volume
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        delete_snapshots: false
        state: "absent"

    - name: Delete the Volume and all its dependent snapshots
      dellemc.powerflex.volume_v2:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"
        vol_name: "sample_volume"
        delete_snapshots: true
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


volume_details (When volume exists, dict, {'accessModeLimit': 'ReadWrite', 'ancestorVolumeId': None, 'autoSnapshotGroupId': None, 'compressionMethod': 'Invalid', 'consistencyGroupId': None, 'creationTime': 1631618520, 'dataLayout': 'MediumGranularity', 'genType': 'EC', 'id': 'cdd883cf00000002', 'links': [{'href': '/api/instances/Volume::cdd883cf00000002', 'rel': 'self'}, {'href': '/api/instances/Volume::cdd883cf00000002/relationships /Statistics', 'rel': '/api/Volume/relationship/Statistics'}, {'href': '/api/instances/VTree::6e86255c00000001', 'rel': '/api/parent/relationship/vtreeId'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': '/api/parent/relationship/storagePoolId'}], 'lockedAutoSnapshot': False, 'lockedAutoSnapshotMarkedForRemoval': False, 'managedBy': 'ScaleIO', 'mappedSdcInfo': None, 'name': 'ansible-volume-1', 'notGenuineSnapshot': False, 'nsid': 23, 'originalExpiryTime': 0, 'pairIds': None, 'protectionDomainId': '9300c1f900000000', 'protectionDomainName': 'domain1', 'replicationJournalVolume': False, 'replicationTimeStamp': 0, 'retentionLevels': [], 'secureSnapshotExpTime': 0, 'sizeInGB': 16, 'sizeInKb': 16777216, 'snapshotPolicyId': None, 'snapshotPolicyName': None, 'snapshotsList': [{'accessModeLimit': 'ReadOnly', 'ancestorVolumeId': 'cdd883cf00000002', 'autoSnapshotGroupId': None, 'compressionMethod': 'Invalid', 'consistencyGroupId': '22f1e80c00000001', 'creationTime': 1631619229, 'dataLayout': 'MediumGranularity', 'id': 'cdd883d000000004', 'links': [{'href': '/api/instances/Volume::cdd883d000000004', 'rel': 'self'}, {'href': '/api/instances/Volume::cdd883d000000004 /relationships/Statistics', 'rel': '/api/Volume/relationship/Statistics'}, {'href': '/api/instances/Volume::cdd883cf00000002', 'rel': '/api/parent/relationship/ancestorVolumeId'}, {'href': '/api/instances/VTree::6e86255c00000001', 'rel': '/api/parent/relationship/vtreeId'}, {'href': '/api/instances/StoragePool::e0d8f6c900000000', 'rel': '/api/parent/relationship/storagePoolId'}], 'lockedAutoSnapshot': False, 'lockedAutoSnapshotMarkedForRemoval': False, 'managedBy': 'ScaleIO', 'mappedSdcInfo': None, 'name': 'ansible_vol_snap_1', 'notGenuineSnapshot': False, 'originalExpiryTime': 0, 'pairIds': None, 'replicationJournalVolume': False, 'replicationTimeStamp': 0, 'retentionLevels': [], 'secureSnapshotExpTime': 0, 'sizeInKb': 16777216, 'snplIdOfAutoSnapshot': None, 'snplIdOfSourceVolume': None, 'storagePoolId': 'e0d8f6c900000000', 'timeStampIsAccurate': False, 'useRmcache': False, 'volumeReplicationState': 'UnmarkedForReplication', 'volumeType': 'Snapshot', 'vtreeId': '6e86255c00000001'}], 'statistics': {'host_trim_bandwidth': 0, 'host_trim_iops': 0, 'avg_host_write_latency': 0, 'logical_provisioned': 3221225472, 'avg_host_read_latency': 0, 'host_read_bandwidth': 0, 'host_read_iops': 0, 'logical_used': 0, 'host_write_bandwidth': 0, 'host_write_iops': 0, 'avg_host_trim_latency': 0}, 'snplIdOfAutoSnapshot': None, 'snplIdOfSourceVolume': None, 'storagePoolId': 'e0d8f6c900000000', 'storagePoolName': 'pool1', 'timeStampIsAccurate': False, 'useRmcache': False, 'volumeClass': 'defaultclass', 'volumeReplicationState': 'UnmarkedForReplication', 'volumeType': 'ThinProvisioned', 'vtreeId': '6e86255c00000001'})
  Details of the volume.


  id (, str, )
    The ID of the volume.


  mappedSdcInfo (, dict, )
    The details of the mapped SDC.


    sdcId (, str, )
      ID of the SDC.


    sdcName (, str, )
      Name of the SDC.


    sdcIp (, str, )
      IP of the SDC.


    accessMode (, str, )
      Mapping access mode for the specified volume.


    limitIops (, int, )
      IOPS limit for the SDC.


    limitBwInMbps (, int, )
      Bandwidth limit for the SDC.



  name (, str, )
    Name of the volume.


  sizeInKb (, int, )
    Size of the volume in Kb.


  sizeInGb (, int, )
    Size of the volume in Gb.


  storagePoolId (, str, )
    ID of the storage pool in which volume resides.


  storagePoolName (, str, )
    Name of the storage pool in which volume resides.


  protectionDomainId (, str, )
    ID of the protection domain in which volume resides.


  protectionDomainName (, str, )
    Name of the protection domain in which volume resides.


  snapshotPolicyId (, str, )
    ID of the snapshot policy associated with volume.


  snapshotPolicyName (, str, )
    Name of the snapshot policy associated with volume.


  snapshotsList (, str, )
    List of snapshots associated with the volume.


  statistics (, dict, )
    Statistics details of the volume.


    avg_host_read_latency (, int, )
      Average host read latency.


    avg_host_trim_latency (, int, )
      Average host trim latency.


    avg_host_write_latency (, int, )
      Average host write latency.


    host_read_bandwidth (, int, )
      Host read bandwidth.


    host_read_iops (, int, )
      Host read IOPS.


    host_trim_bandwidth (, int, )
      Host trim bandwidth.


    host_trim_iops (, int, )
      Host trim IOPS.


    host_write_bandwidth (, int, )
      Host write bandwidth.


    host_write_iops (, int, )
      Host write IOPS.


    logical_provisioned (, int, )
      Logical provisioned size.


    logical_used (, int, )
      Logical used size.







Status
------





Authors
~~~~~~~

- Yuhao Liu (@RayLiu7) <ansible.team@dell.com>

