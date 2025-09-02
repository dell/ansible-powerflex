#!/usr/bin/python

# Copyright: (c) 2025, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing volumes on Dell Technologies (Dell) PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
module: volume_v2
version_added: '3.0.0'
short_description: Manage volumes on Dell PowerFlex
description:
- Managing volumes on PowerFlex storage system includes
  creating, getting details, modifying attributes and deleting volume.
- It also includes adding/removing snapshot policy,
  mapping/unmapping volume to/from SDC and listing
  associated snapshots.

author:
- Yuhao Liu (@RayLiu7) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2
options:
  vol_name:
    description:
    - The name of the volume.
    - Mandatory for create operation.
    - It is unique across the PowerFlex array.
    - Mutually exclusive with I(vol_id).
    type: str
  vol_id:
    description:
    - The ID of the volume.
    - Except create operation, all other operations can be performed
      using I(vol_id).
    - Mutually exclusive with I(vol_name).
    type: str
  storage_pool_name:
    description:
    - The name of the storage pool.
    - Either name or the id of the storage pool is required for creating a
      volume.
    - During creation, if storage pool name is provided then either
      protection domain name or id must be mentioned along with it.
    - Mutually exclusive with I(storage_pool_id).
    type: str
  storage_pool_id:
    description:
    - The ID of the storage pool.
    - Either name or the id of the storage pool is required for creating
      a volume.
    - Mutually exclusive with I(storage_pool_name).
    type: str
  protection_domain_name:
    description:
    - The name of the protection domain.
    - During creation of a volume, if more than one storage pool exists with
      the same name then either protection domain name or id must be
      mentioned along with it.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - The ID of the protection domain.
    - During creation of a volume, if more than one storage pool exists with
      the same name then either protection domain name or id must be
      mentioned along with it.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  vol_type:
    description:
    - Type of volume provisioning.
    choices: ["THICK_PROVISIONED", "THIN_PROVISIONED"]
    type: str
  snapshot_policy_name:
    description:
    - Name of the snapshot policy.
    - To remove/detach snapshot policy, empty
      I(snapshot_policy_id)/I(snapshot_policy_name) is to be passed along with
      I(auto_snap_remove_type).
    type: str
  snapshot_policy_id:
    description:
    - ID of the snapshot policy.
    - To remove/detach snapshot policy, empty
      I(snapshot_policy_id)/I(snapshot_policy_name) is to be passed along with
      I(auto_snap_remove_type).
    type: str
  auto_snap_remove_type:
    description:
    - Whether to remove or detach the snapshot policy.
    - To remove/detach snapshot policy, empty
      I(snapshot_policy_id)/I(snapshot_policy_name) is to be passed along with
      I(auto_snap_remove_type).
    - If the snapshot policy name/id is passed empty then
      I(auto_snap_remove_type) is defaulted to C(detach).
    choices: ['remove', 'detach']
    type: str
  size:
    description:
    - The size of the volume.
    - Size of the volume will be assigned as higher multiple of 8 GB.
    type: int
  cap_unit:
    description:
     - The unit of the volume size. It defaults to 'GB'.
    choices: ['GB' , 'TB']
    type: str
  vol_new_name:
    description:
    - New name of the volume. Used to rename the volume.
    type: str
  refresh_src_vol_id:
    description:
    - ID of the source volume/snapshot to refresh from.
    - Either the name or the id of the source volume/snapshot is required
    - Mutually exclusive with I(refresh_src_vol_name).
    type: str
  refresh_src_vol_name:
    description:
    - Name of the source volume/snapshot to refresh from.
    - Either the name or the id of the source volume/snapshot is required
    - Mutually exclusive with I(refresh_src_vol_id).
    type: str
  restore_src_vol_id:
    description:
    - ID of the source volume/snapshot to restore from.
    - Either the name or the id of the source volume/snapshot is required
    - Mutually exclusive with I(restore_src_vol_name).
    type: str
  restore_src_vol_name:
    description:
    - Name of the source volume/snapshot to restore from.
    - Either the name or the id of the source volume/snapshot is required
    - Mutually exclusive with I(restore_src_vol_id).
    type: str
  allow_multiple_mappings:
    description:
    - Specifies whether to allow or not allow multiple mappings.
    - If the volume is mapped to one SDC then for every new mapping
      I(allow_multiple_mappings) has to be passed as true.
    type: bool
  sdc:
    description:
    - Specifies SDC parameters.
    type: list
    elements: dict
    suboptions:
      sdc_name:
        description:
        - Name of the SDC.
        - Specify either I(sdc_name), I(sdc_id) or I(sdc_ip).
        - Mutually exclusive with I(sdc_id) and I(sdc_ip).
        type: str
      sdc_id:
        description:
        - ID of the SDC.
        - Specify either I(sdc_name), I(sdc_id) or I(sdc_ip).
        - Mutually exclusive with I(sdc_name) and I(sdc_ip).
        type: str
      sdc_ip:
        description:
        - IP of the SDC.
        - Specify either I(sdc_name), I(sdc_id) or I(sdc_ip).
        - Mutually exclusive with I(sdc_id) and I(sdc_ip).
        type: str
      access_mode:
        description:
        - Define the access mode for all mappings of the volume.
        choices: ['READ_WRITE', 'READ_ONLY', 'NO_ACCESS']
        type: str
      bandwidth_limit:
        description:
        - Limit of volume network bandwidth.
        - Need to mention in multiple of 1024 Kbps.
        - To set no limit, 0 is to be passed.
        type: int
      iops_limit:
        description:
        - Limit of volume IOPS.
        - Minimum IOPS limit is 11 and specify 0 for unlimited iops.
        type: int
  sdc_state:
    description:
    - Mapping state of the SDC.
    choices: ['mapped', 'unmapped']
    type: str
  delete_snapshots:
    description:
    - If C(true), the volume and all its dependent snapshots will be deleted.
    - If C(false), only the volume will be deleted.
    - It can be specified only when the I(state) is C(absent).
    - It defaults to C(false), if not specified.
    type: bool
  state:
    description:
    - State of the volume.
    choices: ['present', 'absent']
    required: true
    type: str
attributes:
  check_mode:
    description: Runs task to validate without performing action on the target
                 machine.
    support: full
  diff_mode:
    description: Runs the task to report the changes made or to be made.
    support: full
notes:
  - Compression_type and use_rmcache are not supported since PowerFlex 5.0.0
  - Refresh and restore cannot be conducted in the same task.
"""

EXAMPLES = r"""
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
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
volume_details:
    description: Details of the volume.
    returned: When volume exists
    type: dict
    contains:
        id:
            description: The ID of the volume.
            type: str
        mappedSdcInfo:
            description: The details of the mapped SDC.
            type: dict
            contains:
                sdcId:
                    description: ID of the SDC.
                    type: str
                sdcName:
                    description: Name of the SDC.
                    type: str
                sdcIp:
                    description: IP of the SDC.
                    type: str
                accessMode:
                    description: Mapping access mode for the specified volume.
                    type: str
                limitIops:
                    description: IOPS limit for the SDC.
                    type: int
                limitBwInMbps:
                    description: Bandwidth limit for the SDC.
                    type: int
        name:
            description: Name of the volume.
            type: str
        sizeInKb:
            description: Size of the volume in Kb.
            type: int
        sizeInGb:
            description: Size of the volume in Gb.
            type: int
        storagePoolId:
            description: ID of the storage pool in which volume resides.
            type: str
        storagePoolName:
            description: Name of the storage pool in which volume resides.
            type: str
        protectionDomainId:
            description: ID of the protection domain in which volume resides.
            type: str
        protectionDomainName:
            description: Name of the protection domain in which volume resides.
            type: str
        snapshotPolicyId:
            description: ID of the snapshot policy associated with volume.
            type: str
        snapshotPolicyName:
            description: Name of the snapshot policy associated with volume.
            type: str
        snapshotsList:
            description: List of snapshots associated with the volume.
            type: str
        statistics:
            description: Statistics details of the volume.
            type: dict
            contains:
                "avg_host_read_latency":
                    description: Average host read latency.
                    type: int
                "avg_host_trim_latency":
                    description: Average host trim latency.
                    type: int
                "avg_host_write_latency":
                    description: Average host write latency.
                    type: int
                "host_read_bandwidth":
                    description: Host read bandwidth.
                    type: int
                "host_read_iops":
                    description: Host read IOPS.
                    type: int
                "host_trim_bandwidth":
                    description: Host trim bandwidth.
                    type: int
                "host_trim_iops":
                    description: Host trim IOPS.
                    type: int
                "host_write_bandwidth":
                    description: Host write bandwidth.
                    type: int
                "host_write_iops":
                    description: Host write IOPS.
                    type: int
                "logical_provisioned":
                    description: Logical provisioned size.
                    type: int
                "logical_used":
                    description: Logical used size.
                    type: int
    sample: {
        "accessModeLimit": "ReadWrite",
        "ancestorVolumeId": null,
        "autoSnapshotGroupId": null,
        "compressionMethod": "Invalid",
        "consistencyGroupId": null,
        "creationTime": 1631618520,
        "dataLayout": "MediumGranularity",
        "genType": "EC",
        "id": "cdd883cf00000002",
        "links": [
            {
                "href": "/api/instances/Volume::cdd883cf00000002",
                "rel": "self"
            },
            {
                "href": "/api/instances/Volume::cdd883cf00000002/relationships
                        /Statistics",
                "rel": "/api/Volume/relationship/Statistics"
            },
            {
                "href": "/api/instances/VTree::6e86255c00000001",
                "rel": "/api/parent/relationship/vtreeId"
            },
            {
                "href": "/api/instances/StoragePool::e0d8f6c900000000",
                "rel": "/api/parent/relationship/storagePoolId"
            }
        ],
        "lockedAutoSnapshot": false,
        "lockedAutoSnapshotMarkedForRemoval": false,
        "managedBy": "ScaleIO",
        "mappedSdcInfo": null,
        "name": "ansible-volume-1",
        "notGenuineSnapshot": false,
        "nsid": 23,
        "originalExpiryTime": 0,
        "pairIds": null,
        "protectionDomainId": "9300c1f900000000",
        "protectionDomainName": "domain1",
        "replicationJournalVolume": false,
        "replicationTimeStamp": 0,
        "retentionLevels": [],
        "secureSnapshotExpTime": 0,
        "sizeInGB": 16,
        "sizeInKb": 16777216,
        "snapshotPolicyId": null,
        "snapshotPolicyName": null,
        "snapshotsList": [
            {
                "accessModeLimit": "ReadOnly",
                "ancestorVolumeId": "cdd883cf00000002",
                "autoSnapshotGroupId": null,
                "compressionMethod": "Invalid",
                "consistencyGroupId": "22f1e80c00000001",
                "creationTime": 1631619229,
                "dataLayout": "MediumGranularity",
                "id": "cdd883d000000004",
                "links": [
                    {
                        "href": "/api/instances/Volume::cdd883d000000004",
                        "rel": "self"
                    },
                    {
                        "href": "/api/instances/Volume::cdd883d000000004
                                /relationships/Statistics",
                        "rel": "/api/Volume/relationship/Statistics"
                    },
                    {
                        "href": "/api/instances/Volume::cdd883cf00000002",
                        "rel": "/api/parent/relationship/ancestorVolumeId"
                    },
                    {
                        "href": "/api/instances/VTree::6e86255c00000001",
                        "rel": "/api/parent/relationship/vtreeId"
                    },
                    {
                        "href": "/api/instances/StoragePool::e0d8f6c900000000",
                        "rel": "/api/parent/relationship/storagePoolId"
                    }
                ],
                "lockedAutoSnapshot": false,
                "lockedAutoSnapshotMarkedForRemoval": false,
                "managedBy": "ScaleIO",
                "mappedSdcInfo": null,
                "name": "ansible_vol_snap_1",
                "notGenuineSnapshot": false,
                "originalExpiryTime": 0,
                "pairIds": null,
                "replicationJournalVolume": false,
                "replicationTimeStamp": 0,
                "retentionLevels": [],
                "secureSnapshotExpTime": 0,
                "sizeInKb": 16777216,
                "snplIdOfAutoSnapshot": null,
                "snplIdOfSourceVolume": null,
                "storagePoolId": "e0d8f6c900000000",
                "timeStampIsAccurate": false,
                "useRmcache": false,
                "volumeReplicationState": "UnmarkedForReplication",
                "volumeType": "Snapshot",
                "vtreeId": "6e86255c00000001"
            }
        ],
        "statistics": {
            'host_trim_bandwidth': 0,
            'host_trim_iops': 0,
            'avg_host_write_latency': 0,
            'logical_provisioned': 3221225472,
            'avg_host_read_latency': 0,
            'host_read_bandwidth': 0,
            'host_read_iops': 0,
            'logical_used': 0,
            'host_write_bandwidth': 0,
            'host_write_iops': 0,
            'avg_host_trim_latency': 0
        },
        "snplIdOfAutoSnapshot": null,
        "snplIdOfSourceVolume": null,
        "storagePoolId": "e0d8f6c900000000",
        "storagePoolName": "pool1",
        "timeStampIsAccurate": false,
        "useRmcache": false,
        "volumeClass": "defaultclass",
        "volumeReplicationState": "UnmarkedForReplication",
        "volumeType": "ThinProvisioned",
        "vtreeId": "6e86255c00000001"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import (
    utils,
)
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base import (
    powerflex_compatibility,
)
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base import (
    PowerFlexBase,
)
import copy

LOG = utils.get_logger("volume_v2")


@powerflex_compatibility(min_ver="5.0", predecessor="volume")
class PowerFlexVolumeV2(PowerFlexBase):
    """Class with volume operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        argument_spec = get_powerflex_volume_parameters()

        mut_ex_args = [
            ["vol_name", "vol_id"],
            ["storage_pool_name", "storage_pool_id"],
            ["protection_domain_name", "protection_domain_id"],
            ["snapshot_policy_name", "snapshot_policy_id"],
            ["refresh_src_vol_id", "refresh_src_vol_name"],
            ["restore_src_vol_id", "restore_src_vol_name"],
            ["refresh_src_vol_id", "restore_src_vol_id"],
            ["refresh_src_vol_name", "restore_src_vol_name"],
            ["refresh_src_vol_name", "restore_src_vol_id"],
            ["restore_src_vol_name", "refresh_src_vol_id"],
            ["vol_id", "storage_pool_name"],
            ["vol_id", "storage_pool_id"],
            ["vol_id", "protection_domain_name"],
            ["vol_id", "protection_domain_id"],
        ]

        required_together_args = [["sdc", "sdc_state"]]

        required_one_of_args = [["vol_name", "vol_id"]]

        module_params = {
            "argument_spec": argument_spec,
            "supports_check_mode": True,
            "mutually_exclusive": mut_ex_args,
            "required_together": required_together_args,
            "required_one_of": required_one_of_args,
        }

        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get_protection_domain(
        self, protection_domain_name=None, protection_domain_id=None
    ):
        """Get protection domain details
        :param protection_domain_name: Name of the protection domain
        :param protection_domain_id: ID of the protection domain
        :return: Protection domain details
        """
        name_or_id = (
            protection_domain_id if protection_domain_id else protection_domain_name
        )
        try:
            pd_details = None
            if protection_domain_id:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={"id": protection_domain_id}
                )

            if protection_domain_name:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={"name": protection_domain_name}
                )

            if not pd_details:
                err_msg = (
                    "Unable to find the protection domain with {0}. "
                    "Please enter a valid protection domain"
                    " name/id.".format(name_or_id)
                )
                self.module.fail_json(msg=err_msg)

            return pd_details[0]

        except Exception as e:
            errormsg = (
                "Failed to get the protection domain {0} with"
                " error {1}".format(name_or_id, str(e))
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_snapshot_policy(self, snap_pol_id=None, snap_pol_name=None):
        """Get snapshot policy details
        :param snap_pol_name: Name of the snapshot policy
        :param snap_pol_id: ID of the snapshot policy
        :return: snapshot policy details
        """
        name_or_id = snap_pol_id if snap_pol_id else snap_pol_name
        try:
            snap_pol_details = None
            if snap_pol_id:
                snap_pol_details = self.powerflex_conn.snapshot_policy.get(
                    filter_fields={"id": snap_pol_id}
                )

            if snap_pol_name:
                snap_pol_details = self.powerflex_conn.snapshot_policy.get(
                    filter_fields={"name": snap_pol_name}
                )

            if not snap_pol_details:
                err_msg = (
                    "Unable to find the snapshot policy with {0}. "
                    "Please enter a valid snapshot policy"
                    " name/id.".format(name_or_id)
                )
                self.module.fail_json(msg=err_msg)

            return snap_pol_details[0]

        except Exception as e:
            errormsg = "Failed to get the snapshot policy {0} with" " error {1}".format(
                name_or_id, str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_storage_pool(
        self, storage_pool_id=None, storage_pool_name=None, protection_domain_id=None
    ):
        """Get storage pool details
        :param protection_domain_id: ID of the protection domain
        :param storage_pool_name: The name of the storage pool
        :param storage_pool_id: The storage pool id
        :return: Storage pool details
        """
        name_or_id = storage_pool_id if storage_pool_id else storage_pool_name
        try:
            sp_details = None
            if storage_pool_id:
                sp_details = self.powerflex_conn.storage_pool.get(
                    filter_fields={"id": storage_pool_id}
                )

            if storage_pool_name:
                sp_details = self.powerflex_conn.storage_pool.get(
                    filter_fields={"name": storage_pool_name}
                )

            if len(sp_details) > 1 and protection_domain_id is None:
                err_msg = (
                    "More than one storage pool found with {0},"
                    " Please provide protection domain Name/Id"
                    " to fetch the unique"
                    " pool".format(storage_pool_name)
                )
                self.module.fail_json(msg=err_msg)

            if len(sp_details) > 1 and protection_domain_id:
                sp_details = self.powerflex_conn.storage_pool.get(
                    filter_fields={
                        "name": storage_pool_name,
                        "protectionDomainId": protection_domain_id,
                    }
                )
            if not sp_details:
                err_msg = (
                    "Unable to find the storage pool with {0}. "
                    "Please enter a valid pool "
                    "name/id.".format(name_or_id)
                )
                self.module.fail_json(msg=err_msg)
            return sp_details[0]

        except Exception as e:
            errormsg = "Failed to get the storage pool {0} with error " "{1}".format(
                name_or_id, str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_volume(self, vol_name=None, vol_id=None):
        """Get volume details
        :param vol_name: Name of the volume
        :param vol_id: ID of the volume
        :return: Details of volume if exist.
        """

        id_or_name = vol_id if vol_id else vol_name

        try:
            if vol_id:
                volume_details = self.powerflex_conn.volume.get(
                    filter_fields={"id": vol_id}
                )
            else:
                volume_details = self.powerflex_conn.volume.get(
                    filter_fields={"name": vol_name}
                )

            if len(volume_details) == 0:
                msg = "Volume with identifier {0} not found".format(id_or_name)
                LOG.info(msg)
                return None

            # Append size in GB in the volume details
            if "sizeInKb" in volume_details[0] and volume_details[0]["sizeInKb"]:
                volume_details[0]["sizeInGB"] = utils.get_size_in_gb(
                    volume_details[0]["sizeInKb"], "KB"
                )

            # Append storage pool name and id.
            sp = None
            pd_id = None
            if (
                "storagePoolId" in volume_details[0]
                and volume_details[0]["storagePoolId"]
            ):
                sp = self.get_storage_pool(volume_details[0]["storagePoolId"])
                if len(sp) > 0:
                    volume_details[0]["storagePoolName"] = sp["name"]
                    pd_id = sp["protectionDomainId"]

            # Append protection domain name and id
            if sp and "protectionDomainId" in sp and sp["protectionDomainId"]:
                pd = self.get_protection_domain(protection_domain_id=pd_id)
                volume_details[0]["protectionDomainId"] = pd_id
                volume_details[0]["protectionDomainName"] = pd["name"]

            # Append snapshot policy name and id
            if volume_details[0]["snplIdOfSourceVolume"] is not None:
                snap_policy_id = volume_details[0]["snplIdOfSourceVolume"]
                volume_details[0]["snapshotPolicyId"] = snap_policy_id
                volume_details[0]["snapshotPolicyName"] = self.get_snapshot_policy(
                    snap_policy_id
                )["name"]
            else:
                volume_details[0]["snapshotPolicyId"] = None
                volume_details[0]["snapshotPolicyName"] = None

            # Append the list of snapshots associated with the volume
            list_of_snaps = self.powerflex_conn.volume.get(
                filter_fields={"ancestorVolumeId": volume_details[0]["id"]}
            )
            volume_details[0]["snapshotsList"] = list_of_snaps

            # Append statistics
            if volume_details[0]["id"]:
                statistics = self.powerflex_conn.volume.get_statistics(
                    volume_id=[volume_details[0]["id"]]
                )
                volume_details[0]["statistics"] = (
                    convert_statistics(statistics) if statistics else {}
                )

            return volume_details[0]

        except Exception as e:
            error_msg = "Failed to get the volume {0} with error {1}"
            error_msg = error_msg.format(id_or_name, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_sdc_id(self, sdc_name=None, sdc_ip=None, sdc_id=None):
        """Get the SDC ID
        :param sdc_name: The name of the SDC
        :param sdc_ip: The IP of the SDC
        :param sdc_id: The ID of the SDC
        :return: The ID of the SDC
        """

        if sdc_name:
            id_ip_name = sdc_name
        elif sdc_ip:
            id_ip_name = sdc_ip
        else:
            id_ip_name = sdc_id

        try:
            if sdc_name:
                sdc_details = self.powerflex_conn.sdc.get(
                    filter_fields={"name": sdc_name}
                )
            elif sdc_ip:
                sdc_details = self.powerflex_conn.sdc.get(
                    filter_fields={"sdcIp": sdc_ip}
                )
            else:
                sdc_details = self.powerflex_conn.sdc.get(filter_fields={"id": sdc_id})

            if len(sdc_details) == 0:
                error_msg = "Unable to find SDC with identifier {0}".format(id_ip_name)
                self.module.fail_json(msg=error_msg)
            return sdc_details[0]["id"]
        except Exception as e:
            errormsg = "Failed to get the SDC {0} with error " "{1}".format(
                id_ip_name, str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def create_volume(self, vol_name, pool_id, size, vol_type=None):
        """Create volume
        :param vol_type: Type of volume.
        :param size: Size of the volume.
        :param pool_id: Id of the storage pool.
        :param vol_name: The name of the volume.
        :return: Boolean indicating if create operation is successful
        """
        try:
            if vol_name is None or len(vol_name.strip()) == 0:
                self.module.fail_json(msg="Please provide valid volume name.")

            if not size:
                self.module.fail_json(
                    msg="Size is a mandatory parameter "
                    "for creating a volume. Please "
                    "enter a valid size"
                )

            # Basic volume created.
            if not self.module.check_mode:
                self.powerflex_conn.volume.create(
                    storage_pool_id=pool_id,
                    size_in_gb=size,
                    name=vol_name,
                    volume_type=vol_type,
                )
            return True

        except Exception as e:
            errormsg = "Create volume {0} operation failed with " "error {1}".format(
                vol_name, str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def modify_access_mode(self, vol_id, access_mode_list):
        """Modify access mode of SDCs mapped to volume
        :param vol_id: The volume id
        :param access_mode_list: List containing SDC ID's
         whose access mode is to modified
        :return: Boolean indicating if modifying access
         mode is successful
        """

        try:
            changed = False
            for temp in access_mode_list:
                if temp["accessMode"]:
                    if not self.module.check_mode:
                        self.powerflex_conn.volume.set_access_mode_for_sdc(
                            volume_id=vol_id,
                            sdc_id=temp["sdc_id"],
                            access_mode=temp["accessMode"],
                        )
                    changed = True
            return changed
        except Exception as e:
            errormsg = (
                "Modify access mode of SDC operation failed "
                "with error {0}".format(str(e))
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def modify_limits(self, payload):
        """Modify IOPS and bandwidth limits of SDC's mapped to volume
        :param payload: Dict containing SDC ID's whose bandwidth and
               IOPS is to modified
        :return: Boolean indicating if modifying limits is successful
        """

        try:
            changed = False
            if (
                payload["bandwidth_limit"] is not None
                or payload["iops_limit"] is not None
            ):
                if not self.module.check_mode:
                    self.powerflex_conn.volume.set_mapped_sdc_limits(**payload)
                changed = True
            return changed
        except Exception as e:
            errormsg = (
                "Modify bandwidth/iops limits of SDC %s operation "
                "failed with error %s" % (payload["sdc_id"], str(e))
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def delete_volume(self, vol_id, remove_mode):
        """Delete volume
        :param vol_id: The volume id
        :param remove_mode: Removal mode for the volume
        :return: Boolean indicating if delete operation is successful
        """

        try:
            if not self.module.check_mode:
                self.powerflex_conn.volume.delete(vol_id, remove_mode)
            return True
        except Exception as e:
            errormsg = "Delete volume {0} operation failed with " "error {1}".format(
                vol_id, str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def unmap_volume_from_sdc(self, volume, sdc):
        """Unmap SDC's from volume
        :param volume: volume details
        :param sdc: List of SDCs to be unmapped
        :return: Boolean indicating if unmap operation is successful
        """

        current_sdcs = volume["mappedSdcInfo"]
        current_sdc_ids = []
        sdc_id_list = []
        sdc_id = None
        if current_sdcs:
            for temp in current_sdcs:
                current_sdc_ids.append(temp["sdcId"])

        for temp in sdc:
            if "sdc_name" in temp and temp["sdc_name"]:
                sdc_id = self.get_sdc_id(sdc_name=temp["sdc_name"])
            elif "sdc_ip" in temp and temp["sdc_ip"]:
                sdc_id = self.get_sdc_id(sdc_ip=temp["sdc_ip"])
            else:
                sdc_id = self.get_sdc_id(sdc_id=temp["sdc_id"])
            if sdc_id in current_sdc_ids:
                sdc_id_list.append(sdc_id)

        LOG.info("SDC IDs to remove %s", sdc_id_list)

        if len(sdc_id_list) == 0:
            return False

        try:
            if not self.module.check_mode:
                for sdc_id in sdc_id_list:
                    self.powerflex_conn.volume.remove_mapped_host(volume["id"], sdc_id)
            return True
        except Exception as e:
            errormsg = "Unmap SDC {0} from volume {1} failed with error " "{2}".format(
                sdc_id, volume["id"], str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def map_volume_to_sdc(self, volume, sdc):
        """Map SDC's to volume
        :param volume: volume details
        :param sdc: List of SDCs
        :return: Boolean indicating if mapping operation is successful
        """

        current_sdcs = volume["mappedSdcInfo"]
        sdc_id_list = []
        sdc_map_list = []
        sdc_modify_list1 = []
        sdc_modify_list2 = []

        current_sdc_ids = self.get_current_sdcs(current_sdcs)

        for temp in sdc:
            sdc_id = self.get_sdc_id_from_input(temp)
            if sdc_id not in current_sdc_ids:
                sdc_id_list.append(sdc_id)
                self.update_temp_data(temp, sdc_id)
                sdc_map_list.append(temp)
            else:
                access_mode_dict, limits_dict = check_for_sdc_modification(
                    volume, sdc_id, temp
                )
                self.update_sdc_lists(
                    sdc_modify_list1, sdc_modify_list2, access_mode_dict, limits_dict
                )

        LOG.info("SDC to add: %s", sdc_map_list)

        if not sdc_map_list:
            return False, sdc_modify_list1, sdc_modify_list2

        try:
            changed = False
            for sdc in sdc_map_list:
                payload = {
                    "volume_id": volume["id"],
                    "host_id": sdc["sdc_id"],
                    "access_mode": sdc["access_mode"],
                    "allow_multiple_mappings": self.module.params[
                        "allow_multiple_mappings"
                    ],
                }
                if not self.module.check_mode:
                    self.powerflex_conn.volume.add_mapped_host(**payload)

                if sdc["bandwidth_limit"] or sdc["iops_limit"]:
                    payload = {
                        "volume_id": volume["id"],
                        "sdc_id": sdc["sdc_id"],
                        "bandwidth_limit": sdc["bandwidth_limit"],
                        "iops_limit": sdc["iops_limit"],
                    }

                    if not self.module.check_mode:
                        self.powerflex_conn.volume.set_mapped_sdc_limits(**payload)
                changed = True
            return changed, sdc_modify_list1, sdc_modify_list2
        except Exception as e:
            errormsg = "Mapping volume {0} to SDC {1} " "failed with error {2}".format(
                volume["name"], sdc["sdc_id"], str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def update_sdc_lists(
        self, sdc_modify_list1, sdc_modify_list2, access_mode_dict, limits_dict
    ):
        if access_mode_dict:
            sdc_modify_list1.append(access_mode_dict)
        if limits_dict:
            sdc_modify_list2.append(limits_dict)

    def get_sdc_id_from_input(self, temp):
        if "sdc_name" in temp and temp["sdc_name"]:
            sdc_id = self.get_sdc_id(sdc_name=temp["sdc_name"])
        elif "sdc_ip" in temp and temp["sdc_ip"]:
            sdc_id = self.get_sdc_id(sdc_ip=temp["sdc_ip"])
        else:
            sdc_id = self.get_sdc_id(sdc_id=temp["sdc_id"])
        return sdc_id

    def update_temp_data(self, temp, sdc_id):
        temp["sdc_id"] = sdc_id
        if "access_mode" in temp:
            temp["access_mode"] = get_access_mode(temp["access_mode"])
        if "bandwidth_limit" not in temp:
            temp["bandwidth_limit"] = None
        if "iops_limit" not in temp:
            temp["iops_limit"] = None

    def get_current_sdcs(self, current_sdcs):
        current_sdc_ids = []
        if current_sdcs:
            for temp in current_sdcs:
                current_sdc_ids.append(temp["sdcId"])
        return current_sdc_ids

    def validate_parameters(
        self, auto_snap_remove_type, snap_pol_id, snap_pol_name, delete_snaps, state
    ):
        """Validate the input parameters"""

        sdc = self.module.params["sdc"]
        cap_unit = self.module.params["cap_unit"]
        size = self.module.params["size"]

        if sdc:
            for temp in sdc:
                if (
                    all([temp["sdc_id"], temp["sdc_ip"]])
                    or all([temp["sdc_id"], temp["sdc_name"]])
                    or all([temp["sdc_ip"], temp["sdc_name"]])
                ):
                    self.module.fail_json(
                        msg="sdc_id, sdc_ip and sdc_name " "are mutually exclusive"
                    )

        if (cap_unit is not None) and not size:
            self.module.fail_json(
                msg="cap_unit can be specified along "
                "with size only. Please enter a valid"
                " value for size"
            )

        if auto_snap_remove_type and snap_pol_name is None and snap_pol_id is None:
            err_msg = (
                "To remove/detach snapshot policy, please provide"
                " empty snapshot policy name/id along with "
                "auto_snap_remove_type parameter"
            )
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        if state == "present" and delete_snaps is not None:
            self.module.fail_json(
                msg="delete_snapshots can be specified only when the state"
                " is passed as absent."
            )

    def refresh_volume(self, vol_id, refresh_src_vol_id):
        """
        Refresh the volume
        :param vol_id: Id of the volume
        :param refresh_src_vol_id: Id of the source volume/snapshot
        """
        try:
            msg = "Refreshing the volume {0} with source volume id " "{1}".format(
                vol_id, refresh_src_vol_id
            )
            LOG.info(msg)
            if not self.module.check_mode:
                self.powerflex_conn.volume.refresh(vol_id, refresh_src_vol_id)
        except Exception as e:
            err_msg = "Failed to refresh volume {0} operation with " "error {1}".format(
                vol_id, str(e)
            )
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def restore_volume(self, vol_id, restore_src_vol_id):
        """
        Restore the volume
        :param vol_id: Id of the volume
        :param restore_src_vol_id: Id of the source volume/snapshot
        """
        try:
            msg = "Restoring the volume {0} with source volume id " "{1}".format(
                vol_id, restore_src_vol_id
            )
            LOG.info(msg)
            if not self.module.check_mode:
                self.powerflex_conn.volume.restore(vol_id, restore_src_vol_id)
        except Exception as e:
            err_msg = "Failed to restore volume {0} operation with " "error {1}".format(
                vol_id, str(e)
            )
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def modify_volume(self, vol_id, modify_dict):
        """
        Update the volume attributes
        :param vol_id: Id of the volume
        :param modify_dict: Dictionary containing the attributes of
         volume which are to be updated
        :return: True, if the operation is successful
        """
        try:
            msg = (
                "Dictionary containing attributes which are to be"
                " updated is {0}.".format(str(modify_dict))
            )
            LOG.info(msg)

            if "auto_snap_remove_type" in modify_dict:
                snap_type = modify_dict["auto_snap_remove_type"]
                msg = (
                    "Removing/detaching the snapshot policy from a "
                    "volume. auto_snap_remove_type: {0} and snapshot "
                    "policy id: "
                    "{1}".format(snap_type, modify_dict["snap_pol_id"])
                )
                LOG.info(msg)
                if not self.module.check_mode:
                    self.powerflex_conn.snapshot_policy.remove_source_volume(
                        modify_dict["snap_pol_id"], vol_id, snap_type
                    )
                    msg = "The snapshot policy has been {0}ed " "successfully".format(
                        snap_type
                    )
                    LOG.info(msg)

            if (
                "auto_snap_remove_type" not in modify_dict
                and "snap_pol_id" in modify_dict
            ):
                if not self.module.check_mode:
                    self.powerflex_conn.snapshot_policy.add_source_volume(
                        modify_dict["snap_pol_id"], vol_id
                    )
                    msg = (
                        "Attached the snapshot policy {0} to volume"
                        " successfully.".format(modify_dict["snap_pol_id"])
                    )
                    LOG.info(msg)

            if "new_name" in modify_dict:
                if not self.module.check_mode:
                    self.powerflex_conn.volume.rename(vol_id, modify_dict["new_name"])
                    msg = (
                        "The name of the volume is updated"
                        " to {0} sucessfully.".format(modify_dict["new_name"])
                    )
                    LOG.info(msg)

            if "new_size" in modify_dict:
                if not self.module.check_mode:
                    self.powerflex_conn.volume.extend(vol_id, modify_dict["new_size"])
                    msg = (
                        "The size of the volume is extended to {0} "
                        "sucessfully.".format(str(modify_dict["new_size"]))
                    )
                    LOG.info(msg)

            return True

        except Exception as e:
            err_msg = "Failed to update the volume {0}" " with error {1}".format(
                vol_id, str(e)
            )
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def to_modify(
        self, vol_details, new_size, new_name, snap_pol_id, auto_snap_remove_type
    ):
        """

        :param vol_details: Details of the volume
        :param new_size: Size of the volume
        :param new_name: The new name of the volume
        :param snap_pol_id: Id of the snapshot policy
        :param auto_snap_remove_type: Whether to remove or detach the policy
        :return: Dictionary containing the attributes of
         volume which are to be updated
        """
        modify_dict = {}

        vol_size_in_gb = utils.get_size_in_gb(vol_details["sizeInKb"], "KB")

        self.update_new_size(new_size, modify_dict, vol_size_in_gb)

        self.update_new_name(vol_details, new_name, modify_dict)

        if (
            snap_pol_id is not None
            and snap_pol_id == ""
            and auto_snap_remove_type
            and vol_details["snplIdOfSourceVolume"]
        ):
            modify_dict["auto_snap_remove_type"] = auto_snap_remove_type
            modify_dict["snap_pol_id"] = vol_details["snplIdOfSourceVolume"]

        if snap_pol_id is not None and snap_pol_id != "":
            if auto_snap_remove_type and vol_details["snplIdOfSourceVolume"]:
                err_msg = (
                    "To remove/detach a snapshot policy, provide the"
                    " snapshot policy name/id as empty string"
                )
                self.module.fail_json(msg=err_msg)
            if (
                auto_snap_remove_type is None
                and vol_details["snplIdOfSourceVolume"] is None
            ):
                modify_dict["snap_pol_id"] = snap_pol_id

        return modify_dict

    def update_new_name(self, vol_details, new_name, modify_dict):
        if new_name is not None:
            if new_name is None or len(new_name.strip()) == 0:
                self.module.fail_json(msg="Please provide valid volume " "name.")
            if new_name != vol_details["name"]:
                modify_dict["new_name"] = new_name

    def update_new_size(self, new_size, modify_dict, vol_size_in_gb):
        if new_size is not None and not (
            (vol_size_in_gb - 8) < new_size <= vol_size_in_gb
        ):
            modify_dict["new_size"] = new_size

    def verify_params(
        self,
        vol_details,
        snap_pol_name,
        snap_pol_id,
        pd_name,
        pd_id,
        pool_name,
        pool_id,
    ):
        """
        :param vol_details: Details of the volume
        :param snap_pol_name: Name of the snapshot policy
        :param snap_pol_id: Id of the snapshot policy
        :param pd_name: Name of the protection domain
        :param pd_id: Id of the protection domain
        :param pool_name: Name of the storage pool
        :param pool_id: Id of the storage pool
        """

        if (
            snap_pol_id
            and "snapshotPolicyId" in vol_details
            and vol_details["snapshotPolicyId"] is not None
            and snap_pol_id != vol_details["snapshotPolicyId"]
        ):
            self.module.fail_json(
                msg="Entered snapshot policy id does not"
                " match with the snapshot policy's id"
                " attached to the volume. Please enter"
                " a correct snapshot policy id."
            )

        if (
            snap_pol_name
            and "snapshotPolicyName" in vol_details
            and vol_details["snapshotPolicyName"] is not None
            and snap_pol_name != vol_details["snapshotPolicyName"]
        ):
            self.module.fail_json(
                msg="Entered snapshot policy name does not"
                " match with the snapshot policy's "
                "name attached to the volume. Please"
                " enter a correct snapshot policy"
                " name."
            )

        if pd_id and pd_id != vol_details["protectionDomainId"]:
            self.module.fail_json(
                msg="Entered protection domain id does not"
                " match with the volume's protection"
                " domain id. Please enter a correct"
                " protection domain id."
            )

        if pool_id and pool_id != vol_details["storagePoolId"]:
            self.module.fail_json(
                msg="Entered storage pool id does"
                " not match with the volume's "
                "storage pool id. Please enter"
                " a correct storage pool id."
            )

        if pd_name and pd_name != vol_details["protectionDomainName"]:
            self.module.fail_json(
                msg="Entered protection domain name does"
                " not match with the volume's "
                "protection domain name. Please enter"
                " a correct protection domain name."
            )

        if pool_name and pool_name != vol_details["storagePoolName"]:
            self.module.fail_json(
                msg="Entered storage pool name does"
                " not match with the volume's "
                "storage pool name. Please enter"
                " a correct storage pool name."
            )

    def initialize_diff_after(self, volume_params, volume_details):
        """Initialize diff between playbook input and volume details
        :param volume_params: Dictionary of parameters input from playbook
        :param volume_params: Dictionary of volume details
        :return: Dictionary of parameters of differences"""

        diff_dict = {}
        if volume_params["state"] == "absent":
            return diff_dict

        if volume_details is None:
            excluded_keys = {
                "hostname",
                "username",
                "password",
                "port",
                "timeout",
                "validate_certs",
                "state",
            }
            diff_dict = {}

            for key, value in volume_params.items():
                if key not in excluded_keys and value is not None:
                    diff_dict[key] = value

        else:
            diff_dict = copy.deepcopy(volume_details)
        return diff_dict

    def update_diff_after(self, modify_dict, diff_dict):
        """Update diff between playbook input and volume details
        :param modify_dict: Dictionary of parameters of differences
        :param diff_dict: Dictionary of volume details
        :return: Dictionary of parameters of differences"""

        diff_dict_new = copy.deepcopy(diff_dict)
        if modify_dict:
            if "new_size" in modify_dict and modify_dict["new_size"]:
                size = self.module.params["size"]
                cap_unit = self.module.params["cap_unit"]
                diff_dict_new["after"]["size"] = size
                diff_dict_new["after"]["size_cap_unit"] = cap_unit
                diff_dict_new["after"]["sizeInKb"] = (
                    self.get_size_data(size, cap_unit) * 1024
                )
                diff_dict_new["after"]["sizeInGB"] = self.get_size_data(size, cap_unit)
            if "new_name" in modify_dict and modify_dict["new_name"]:
                diff_dict_new["after"]["name"] = modify_dict["new_name"]
            if "snap_pol_id" in modify_dict and modify_dict["snap_pol_id"]:
                diff_dict_new["after"]["snplIdOfSourceVolume"] = modify_dict[
                    "snap_pol_id"
                ]
            if (
                "auto_snap_remove_type" in modify_dict
                and modify_dict["auto_snap_remove_type"]
            ):
                diff_dict_new["after"]["snplIdOfSourceVolume"] = None
        return diff_dict_new

    def perform_module_operation(self):
        """
        Perform different actions on volume based on parameters passed in
        the playbook
        """
        vol_name = self.module.params["vol_name"]
        vol_id = self.module.params["vol_id"]
        vol_type = self.module.params["vol_type"]
        sp_name = self.module.params["storage_pool_name"]
        sp_id = self.module.params["storage_pool_id"]
        pd_name = self.module.params["protection_domain_name"]
        pd_id = self.module.params["protection_domain_id"]
        snap_pol_name = self.module.params["snapshot_policy_name"]
        snap_pol_id = self.module.params["snapshot_policy_id"]
        auto_snap_remove_type = self.module.params["auto_snap_remove_type"]
        size = self.module.params["size"]
        cap_unit = self.module.params["cap_unit"]
        vol_new_name = self.module.params["vol_new_name"]
        refresh_src_vol_id = self.module.params["refresh_src_vol_id"]
        refresh_src_vol_name = self.module.params["refresh_src_vol_name"]
        restore_src_vol_id = self.module.params["restore_src_vol_id"]
        restore_src_vol_name = self.module.params["restore_src_vol_name"]
        sdc = copy.deepcopy(self.module.params["sdc"])
        sdc_state = self.module.params["sdc_state"]
        delete_snapshots = self.module.params["delete_snapshots"]
        state = self.module.params["state"]

        vol_type = get_vol_type(vol_type)
        auto_snap_remove_type = self.check_null_capitalize(auto_snap_remove_type)

        # result is a dictionary to contain end state and volume details
        changed = False
        result = dict(changed=False, volume_details={})
        self.validate_parameters(
            auto_snap_remove_type, snap_pol_id, snap_pol_name, delete_snapshots, state
        )

        auto_snap_remove_type = self.get_auto_snap_rt(
            snap_pol_name, snap_pol_id, auto_snap_remove_type
        )

        size = self.get_size_data(size, cap_unit)

        pd_id = self.get_pd_details(pd_name, pd_id)

        sp_id = self.get_sp_details(sp_name, pd_id, sp_id)

        snap_pol_id = self.get_snap_pol_details(snap_pol_name, snap_pol_id)

        # get volume details
        volume_details, vol_id = self.get_vol(vol_name, vol_id)

        if vol_name and volume_details:
            self.verify_params(
                volume_details,
                snap_pol_name,
                snap_pol_id,
                pd_name,
                pd_id,
                sp_name,
                sp_id,
            )

        refresh_src_vol_id, restore_src_vol_id = self.get_refresh_restore_src_id(
            refresh_src_vol_id,
            refresh_src_vol_name,
            restore_src_vol_id,
            restore_src_vol_name,
        )

        before_dict = volume_details if volume_details is not None else {}
        diff_dict = {}
        diff_dict = self.initialize_diff_after(self.module.params, volume_details)
        result["diff"] = dict(before=before_dict, after=diff_dict)

        # create operation
        create_changed = False
        if state == "present" and not volume_details:
            vol_id, volume_details, create_changed = self.create_new_volume(
                vol_name, vol_id, vol_type, sp_id, size, vol_new_name, volume_details
            )

        refresh_restore_changed = False
        if state == "present" and (restore_src_vol_id or refresh_src_vol_id):
            if refresh_src_vol_id:
                self.refresh_volume(vol_id, refresh_src_vol_id)
            if restore_src_vol_id:
                self.restore_volume(vol_id, restore_src_vol_id)
            refresh_restore_changed = True

        # Mapping the SDCs to a volume
        map_changed = False
        mode_changed = False
        limits_changed = False
        if state == "present" and volume_details and sdc and sdc_state == "mapped":
            mode_changed, limits_changed, map_changed = self.sdc_state_mapped(
                vol_id, sdc, volume_details
            )

        # Unmap the SDCs to a volume
        unmap_changed = False
        if state == "present" and volume_details and sdc and sdc_state == "unmapped":
            unmap_changed = self.unmap_volume_from_sdc(volume_details, sdc)

        if not create_changed and (
            map_changed or unmap_changed or mode_changed or limits_changed
        ):
            result["diff"]["after"]["mappedSdcInfo"] = {
                "sdc": sdc,
                "sdcState": sdc_state,
            }

        modify_dict = {}
        if volume_details and state == "present":
            modify_dict = self.to_modify(
                volume_details, size, vol_new_name, snap_pol_id, auto_snap_remove_type
            )
            msg = "Parameters to be modified are as follows: {0}".format(
                str(modify_dict)
            )
            LOG.info(msg)

        # Update the basic volume attributes
        modify_changed = False
        if modify_dict and state == "present":
            modify_changed = self.modify_volume(vol_id, modify_dict)
            if not create_changed and modify_dict:
                result["diff"] = self.update_diff_after(modify_dict, result["diff"])

        # delete operation
        del_changed = False
        if state == "absent" and volume_details:
            del_changed = self.delete_operation(vol_id, delete_snapshots)

        changed = (
            modify_changed
            or unmap_changed
            or map_changed
            or create_changed
            or del_changed
            or mode_changed
            or limits_changed
            or refresh_restore_changed
        )

        # Returning the updated volume details
        self.prepare_output(vol_id, vol_name, result, create_changed)

        result["changed"] = changed
        self.module.exit_json(**result)

    def prepare_output(self, vol_id, vol_name, result, create_changed):
        vol_details = self.get_volume(vol_name, vol_id)
        result["volume_details"] = vol_details
        if not self.module.check_mode and not create_changed:
            result["diff"]["after"] = vol_details

    def get_vol(self, vol_name, vol_id):
        volume_details = self.get_volume(vol_name, vol_id)
        if volume_details:
            vol_id = volume_details["id"]
        msg = "Fetched the volume details {0}".format(str(volume_details))
        LOG.info(msg)
        return volume_details, vol_id

    def get_auto_snap_rt(self, snap_pol_name, snap_pol_id, auto_snap_remove_type):
        if not auto_snap_remove_type and (snap_pol_name == "" or snap_pol_id == ""):
            auto_snap_remove_type = "Detach"
        return auto_snap_remove_type

    def get_size_data(self, size, cap_unit):
        if size:
            if not cap_unit:
                cap_unit = "GB"

            if cap_unit == "TB":
                size = size * 1024
        return size

    def get_pd_details(self, pd_name, pd_id):
        if pd_name:
            pd_details = self.get_protection_domain(pd_name)
            if pd_details:
                pd_id = pd_details["id"]
            msg = (
                "Fetched the protection domain details with id {0},"
                " name {1}".format(pd_id, pd_name)
            )
            LOG.info(msg)
        return pd_id

    def get_sp_details(self, sp_name, pd_id, sp_id):
        if sp_name:
            sp_details = self.get_storage_pool(
                storage_pool_name=sp_name, protection_domain_id=pd_id
            )
            if sp_details:
                sp_id = sp_details["id"]
            msg = "Fetched the storage pool details id {0}," " name {1}".format(
                sp_id, sp_name
            )
            LOG.info(msg)
        return sp_id

    def get_snap_pol_details(self, snap_pol_name, snap_pol_id):
        if snap_pol_name is not None:
            snap_pol_details = None
            if snap_pol_name:
                snap_pol_details = self.get_snapshot_policy(snap_pol_name=snap_pol_name)
            if snap_pol_details:
                snap_pol_id = snap_pol_details["id"]

            if snap_pol_name == "":
                snap_pol_id = ""
            msg = "Fetched the snapshot policy details with id {0}," " name {1}".format(
                snap_pol_id, snap_pol_name
            )
            LOG.info(msg)
        return snap_pol_id

    def get_refresh_restore_src_id(
        self,
        refresh_src_vol_id,
        refresh_src_vol_name,
        restore_src_vol_id,
        restore_src_vol_name,
    ):
        refresh_src_vol_id_updated = refresh_src_vol_id
        if refresh_src_vol_name:
            _, refresh_src_vol_id_updated = self.get_vol(  # pylint: disable=disallowed-name
                refresh_src_vol_name, None
            )
            if refresh_src_vol_id_updated is None:
                self.module.fail_json(
                    msg="Invalid refresh src vol name"
                )
        restore_src_vol_id_updated = restore_src_vol_id
        if restore_src_vol_name:
            _, restore_src_vol_id_updated = self.get_vol(  # pylint: disable=disallowed-name
                restore_src_vol_name, None
            )
            if restore_src_vol_id_updated is None:
                self.module.fail_json(
                    msg="Invalid restore src vol name"
                )
        return refresh_src_vol_id_updated, restore_src_vol_id_updated

    def create_new_volume(
        self, vol_name, vol_id, vol_type, sp_id, size, vol_new_name, volume_details
    ):
        if vol_id:
            self.module.fail_json(
                msg="Creation of volume is allowed "
                "using vol_name only, "
                "vol_id given."
            )

        if vol_new_name:
            self.module.fail_json(
                msg="vol_new_name parameter is not supported during "
                "creation of a volume. Try renaming the volume after"
                " the creation."
            )
        create_changed = self.create_volume(vol_name, sp_id, size, vol_type)
        if create_changed and not self.module.check_mode:
            volume_details = self.get_volume(vol_name)
            vol_id = volume_details["id"]
            msg = "Volume created successfully, fetched " "volume details {0}".format(
                str(volume_details)
            )
            LOG.info(msg)
        return vol_id, volume_details, create_changed

    def sdc_state_mapped(self, vol_id, sdc, volume_details):
        mode_changed = False
        limits_changed = False
        map_changed = False
        map_changed, access_mode_list, limits_list = self.map_volume_to_sdc(
            volume_details, sdc
        )
        if len(access_mode_list) > 0:
            mode_changed = self.modify_access_mode(vol_id, access_mode_list)
        if len(limits_list) > 0:
            for temp in limits_list:
                payload = {
                    "volume_id": volume_details["id"],
                    "sdc_id": temp["sdc_id"],
                    "bandwidth_limit": temp["bandwidth_limit"],
                    "iops_limit": temp["iops_limit"],
                }
                limits_changed = self.modify_limits(payload)
        return mode_changed, limits_changed, map_changed

    def delete_operation(self, vol_id, delete_snapshots):
        if delete_snapshots is True:
            delete_snapshots = "INCLUDING_DESCENDANTS"
        if delete_snapshots is None or delete_snapshots is False:
            delete_snapshots = "ONLY_ME"
        del_changed = self.delete_volume(vol_id, delete_snapshots)
        return del_changed

    def check_null_capitalize(self, input_str):
        if input_str:
            input_str = input_str.capitalize()
        return input_str


def convert_statistics(raw_statistics):
    statistics = {}

    for metric in raw_statistics.get("resources", [])[0].get("metrics", []):
        metric_name = metric.get("name")
        # Assumes each metric has at least one value in 'values'
        metric_value = metric.get("values", [None])[0]
        statistics[metric_name] = metric_value

    return statistics


def check_for_sdc_modification(volume, sdc_id, sdc_details):
    """
    :param volume: The volume details
    :param sdc_id: The ID of the SDC
    :param sdc_details: The details of SDC
    :return: Dictionary with SDC attributes to be modified
    """
    access_mode_dict = dict()
    limits_dict = dict()

    for sdc in volume["mappedSdcInfo"]:
        if sdc["sdcId"] == sdc_id:
            update_access_mode(sdc_id, sdc_details, access_mode_dict, sdc)
            if (
                sdc["limitIops"] != sdc_details["iops_limit"]
                or sdc["limitBwInMbps"] != sdc_details["bandwidth_limit"]
            ):
                limits_dict["sdc_id"] = sdc_id
                limits_dict["iops_limit"] = None
                limits_dict["bandwidth_limit"] = None
                if sdc["limitIops"] != sdc_details["iops_limit"]:
                    limits_dict["iops_limit"] = sdc_details["iops_limit"]
                if sdc["limitBwInMbps"] != get_limits_in_mb(
                    sdc_details["bandwidth_limit"]
                ):
                    limits_dict["bandwidth_limit"] = sdc_details["bandwidth_limit"]
            break
    return access_mode_dict, limits_dict


def update_access_mode(sdc_id, sdc_details, access_mode_dict, sdc):
    if sdc["accessMode"] != get_access_mode(sdc_details["access_mode"]):
        access_mode_dict["sdc_id"] = sdc_id
        access_mode_dict["accessMode"] = get_access_mode(sdc_details["access_mode"])


def get_limits_in_mb(limits):
    """
    :param limits: Limits in KB
    :return: Limits in MB
    """

    if limits:
        return limits / 1024


def get_access_mode(access_mode):
    """
    :param access_mode: Access mode of the SDC
    :return: The enum for the access mode
    """

    access_mode_dict = {
        "READ_WRITE": "ReadWrite",
        "READ_ONLY": "ReadOnly",
        "NO_ACCESS": "NoAccess",
    }
    return access_mode_dict.get(access_mode)


def get_vol_type(vol_type):
    """
    :param vol_type: Type of the volume
    :return: Corresponding value for the entered vol_type
    """
    vol_type_dict = {
        "THICK_PROVISIONED": "ThickProvisioned",
        "THIN_PROVISIONED": "ThinProvisioned",
    }
    if vol_type:
        vol_type = vol_type_dict.get(vol_type)
    return vol_type


def get_powerflex_volume_parameters():
    """This method provide parameter required for the volume
    module on PowerFlex"""
    return dict(
        vol_name=dict(),
        vol_id=dict(),
        storage_pool_name=dict(),
        storage_pool_id=dict(),
        protection_domain_name=dict(),
        protection_domain_id=dict(),
        snapshot_policy_name=dict(),
        snapshot_policy_id=dict(),
        size=dict(type="int"),
        cap_unit=dict(choices=["GB", "TB"]),
        vol_type=dict(choices=["THICK_PROVISIONED", "THIN_PROVISIONED"]),
        auto_snap_remove_type=dict(choices=["detach", "remove"]),
        vol_new_name=dict(),
        allow_multiple_mappings=dict(type="bool"),
        delete_snapshots=dict(type="bool"),
        refresh_src_vol_id=dict(),
        refresh_src_vol_name=dict(),
        restore_src_vol_id=dict(),
        restore_src_vol_name=dict(),
        sdc=dict(
            type="list",
            elements="dict",
            options=dict(
                sdc_id=dict(),
                sdc_ip=dict(),
                sdc_name=dict(),
                access_mode=dict(choices=["READ_WRITE", "READ_ONLY", "NO_ACCESS"]),
                bandwidth_limit=dict(type="int"),
                iops_limit=dict(type="int"),
            ),
        ),
        sdc_state=dict(choices=["mapped", "unmapped"]),
        state=dict(required=True, type="str", choices=["present", "absent"]),
    )


def main():
    """Create PowerFlex volume object and perform actions on it
    based on user input from playbook"""
    obj = PowerFlexVolumeV2()
    obj.perform_module_operation()


if __name__ == "__main__":
    main()
