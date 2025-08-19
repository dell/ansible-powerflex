#!/usr/bin/python

# Copyright: (c) 2021, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing Snapshots on Dell Technologies (Dell) PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
module: snapshot_v2
version_added: '3.0.0'
short_description: Manage Snapshots on Dell PowerFlex
description:
- Managing snapshots on PowerFlex Storage System includes
  creating, getting details, modifying the attributes and deleting snapshot.

author:
- Yuhao Liu (@RayLiu7) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

options:
  snapshot_name:
    description:
    - The name of the snapshot.
    - Mandatory for create operation.
    - Specify either I(snapshot_name) or I(snapshot_id) (but not both) for any operation.
    type: str
  snapshot_id:
    description:
    - The ID of the Snapshot.
    type: str
  vol_name:
    description:
    - The name of the volume for which snapshot will be taken.
    - Specify either I(vol_name) or I(vol_id) while creating snapshot.
    type: str
  vol_id:
    description:
    - The ID of the volume.
    type: str
  snapshot_new_name:
    description:
    - New name of the snapshot. Used to rename the snapshot.
    type: str
  desired_retention:
    description:
    - The retention value for the Snapshot.
    - If the desired_retention is not mentioned during creation, snapshot
      will be created with unlimited retention.
    - Maximum supported desired retention is 31 days.
    type: int
  retention_unit:
    description:
    - The unit for retention. It defaults to C(hours), if not specified.
    choices: [hours, days]
    type: str
  remove_mode:
    description:
    - Removal mode for the snapshot.
    - It defaults to C(ONLY_ME), if not specified.
    choices: ['ONLY_ME', 'INCLUDING_DESCENDANTS']
    type: str
  state:
    description:
    - State of the snapshot.
    choices: ['present', 'absent']
    default: present
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
  - Snapshots are read-only since PowerFlex 5.0.0
"""

EXAMPLES = r"""
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
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'

snapshot_details:
    description: Details of the snapshot.
    returned: When snapshot exists
    type: dict
    contains:
        ancestorVolumeId:
            description: The ID of the root of the specified volume's V-Tree.
            type: str
        ancestorVolumeName:
            description: The name of the root of the specified volume's V-Tree.
            type: str
        creationTime:
            description: The creation time of the snapshot.
            type: int
        id:
            description: The ID of the snapshot.
            type: str
        name:
            description: Name of the snapshot.
            type: str
        secureSnapshotExpTime:
            description: Expiry time of the snapshot.
            type: int
        sizeInKb:
            description: Size of the snapshot.
            type: int
        sizeInGb:
            description: Size of the snapshot.
            type: int
        retentionInHours:
            description: Retention of the snapshot in hours.
            type: int
        storagePoolId:
            description: The ID of the Storage pool in which snapshot resides.
            type: str
        storagePoolName:
            description: The name of the Storage pool in which snapshot resides.
            type: str
    sample: {
        "accessModeLimit": "ReadOnly",
        "ancestorVolumeId": "cdd883cf00000002",
        "ancestorVolumeName": "ansible-volume-1",
        "autoSnapshotGroupId": null,
        "compressionMethod": "Invalid",
        "consistencyGroupId": "22f1e80c00000001",
        "creationTime": 1631619229,
        "dataLayout": "MediumGranularity",
        "genType": "EC",
        "id": "cdd883d000000004",
        "links": [
            {
                "href": "/api/instances/Volume::cdd883d000000004",
                "rel": "self"
            },
            {
                "href": "/api/instances/Volume::cdd883d000000004/relationships
                        /Statistics",
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
        "nsid": 23,
        "originalExpiryTime": 0,
        "pairIds": null,
        "replicationJournalVolume": false,
        "replicationTimeStamp": 0,
        "retentionInHours": 0,
        "retentionLevels": [],
        "secureSnapshotExpTime": 0,
        "sizeInGb": 16,
        "sizeInKb": 16777216,
        "snplIdOfAutoSnapshot": null,
        "snplIdOfSourceVolume": null,
        "storagePoolId": "e0d8f6c900000000",
        "storagePoolName": "pool1",
        "timeStampIsAccurate": false,
        "useRmcache": false,
        "volumeClass": "defaultclass",
        "volumeReplicationState": "UnmarkedForReplication",
        "volumeType": "Snapshot",
        "vtreeId": "6e86255c00000001"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell\
    import utils
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from datetime import datetime, timedelta
import time
import copy

LOG = utils.get_logger("snapshot_v2")


@powerflex_compatibility(min_ver='5.0', predecessor='snapshot')
class PowerFlexSnapshotV2(PowerFlexBase):
    """Class with Snapshot operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        argument_spec = get_powerflex_snapshot_parameters()

        mutually_exclusive = [
            ["snapshot_name", "snapshot_id"],
            ["vol_name", "vol_id"],
            ["snapshot_id", "vol_name"],
            ["snapshot_id", "vol_id"],
        ]

        required_one_of = [["snapshot_name", "snapshot_id"]]

        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive,
            'required_one_of': required_one_of,
        }

        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get_storage_pool(self, storage_pool_id):
        """Get storage pool details
        :param storage_pool_id: The storage pool id
        :return: Storage pool details
        """

        try:
            return self.powerflex_conn.storage_pool.get(
                filter_fields={"id": storage_pool_id}
            )

        except Exception as e:
            errormsg = "Failed to get the storage pool %s with error " "%s" % (
                storage_pool_id,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_snapshot(self, snapshot_name=None, snapshot_id=None):
        """Get snapshot details
        :param snapshot_name: Name of the snapshot
        :param snapshot_id: ID of the snapshot
        :return: Details of snapshot if exist.
        """

        id_or_name = snapshot_id if snapshot_id else snapshot_name

        try:
            filters = {"id": snapshot_id}
            if snapshot_name:
                filters = {"name": snapshot_name}
            snapshot_details = self.powerflex_conn.volume.get(filter_fields=filters)

            if len(snapshot_details) == 0:
                msg = "Snapshot with identifier %s is not found" % id_or_name
                LOG.error(msg)
                return None

            if len(snapshot_details) > 1:
                errormsg = (
                    "Multiple instances of snapshot "
                    "exist with name {0}".format(snapshot_name)
                )
                self.module.fail_json(msg=errormsg)

            # Add ancestor volume name
            self.add_ancestor(snapshot_details)

            # Add size in GB
            self.add_size_in_gb(snapshot_details)

            # Add storage pool name
            self.add_storage_pool_name(snapshot_details)

            # Add retention in hours
            self.add_retention_in_hours(snapshot_details)

            # Match volume details with snapshot details
            if any([self.module.params["vol_name"], self.module.params["vol_id"]]):
                self.match_vol_details(snapshot_details[0])
            return snapshot_details[0]
        except Exception as e:
            errormsg = "Failed to get the snapshot %s with error %s" % (
                id_or_name,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def add_retention_in_hours(self, snapshot_details):
        if (
            "secureSnapshotExpTime" in snapshot_details[0]
            and "creationTime" in snapshot_details[0]
        ):
            if snapshot_details[0]["secureSnapshotExpTime"] != 0:
                expiry_obj = datetime.fromtimestamp(
                    snapshot_details[0]["secureSnapshotExpTime"]
                )
                creation_obj = datetime.fromtimestamp(
                    snapshot_details[0]["creationTime"]
                )
                # Get datetime diff in hours
                td_hour = int(
                    round(get_datetime_diff_in_minutes(expiry_obj, creation_obj) / 60)
                )
                snapshot_details[0]["retentionInHours"] = td_hour
            else:
                snapshot_details[0]["retentionInHours"] = 0

    def add_storage_pool_name(self, snapshot_details):
        if (
            "storagePoolId" in snapshot_details[0]
            and snapshot_details[0]["storagePoolId"]
        ):
            sp = self.get_storage_pool(snapshot_details[0]["storagePoolId"])
            if len(sp) > 0:
                snapshot_details[0]["storagePoolName"] = sp[0]["name"]

    def add_size_in_gb(self, snapshot_details):
        if "sizeInKb" in snapshot_details[0] and snapshot_details[0]["sizeInKb"]:
            snapshot_details[0]["sizeInGb"] = utils.get_size_in_gb(
                snapshot_details[0]["sizeInKb"], "KB"
            )

    def add_ancestor(self, snapshot_details):
        if (
            "ancestorVolumeId" in snapshot_details[0]
            and snapshot_details[0]["ancestorVolumeId"]
        ):
            vol = self.get_volume(vol_id=snapshot_details[0]["ancestorVolumeId"])
            snapshot_details[0]["ancestorVolumeName"] = vol["name"]

    def match_vol_details(self, snapshot):
        """Match the given volume details with the response
        :param snapshot: The snapshot details
        """
        vol_name = self.module.params["vol_name"]
        vol_id = self.module.params["vol_id"]

        try:
            if vol_name and vol_name != snapshot["ancestorVolumeName"]:
                errormsg = (
                    "Given volume name do not match with the "
                    "corresponding snapshot details."
                )
                self.module.fail_json(msg=errormsg)

            if vol_id and vol_id != snapshot["ancestorVolumeId"]:
                errormsg = (
                    "Given volume ID do not match with the "
                    "corresponding snapshot details."
                )
                self.module.fail_json(msg=errormsg)
        except Exception as e:
            errormsg = (
                "Failed to match volume details with the snapshot "
                "with error %s" % str(e)
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_volume(self, vol_name=None, vol_id=None):
        """Get the volume id
        :param vol_name: The name of the volume
        :param vol_id: The ID of the volume
        :return: The volume details
        """

        try:
            if vol_name:
                vol_details = self.powerflex_conn.volume.get(
                    filter_fields={"name": vol_name}
                )
            else:
                vol_details = self.powerflex_conn.volume.get(
                    filter_fields={"id": vol_id}
                )

            if len(vol_details) == 0:
                error_msg = "Unable to find volume with name {0}".format(vol_name)
                self.module.fail_json(msg=error_msg)
            return vol_details[0]
        except Exception as e:
            errormsg = "Failed to get the volume %s with error " "%s" % (
                vol_name,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_system_id(self):
        """Get system id"""

        try:
            resp = self.powerflex_conn.system.get()

            if len(resp) == 0:
                self.module.fail_json(msg="No system exist on the given host.")

            if len(resp) > 1:
                self.module.fail_json(
                    msg="Multiple systems exist on the " "given host."
                )
            return resp[0]["id"]
        except Exception as e:
            msg = "Failed to get system id with error %s" % str(e)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def create_snapshot(self, snapshot_name, vol_id, system_id, retention):
        """Create snapshot
        :param snapshot_name: The name of the snapshot
        :param vol_id: The ID of the source volume
        :param system_id: The system id
        :param retention: The retention for the snapshot
        :return: Boolean indicating if create operation is successful
        """
        LOG.debug("Creating Snapshot")

        try:
            if not self.module.check_mode:
                self.powerflex_conn.system.create_snapshot(
                    system_id=system_id,
                    snapshot_defs=[{"volumeId": vol_id, "snapshotName": snapshot_name}],
                    retention_period=retention,
                )

            return True
        except Exception as e:
            errormsg = "Create snapshot %s operation failed with " "error %s" % (
                snapshot_name,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def modify_retention(self, snapshot_id, new_retention):
        """Modify snapshot retention
        :param snapshot_id: The snapshot id
        :param new_retention: Desired retention of the snapshot
        :return: Boolean indicating if modifying retention is successful
        """

        try:
            if not self.module.check_mode:
                self.powerflex_conn.volume.set_retention_period(snapshot_id, new_retention)
            return True
        except Exception as e:
            errormsg = (
                "Modify retention of snapshot %s operation failed "
                "with error %s" % (snapshot_id, str(e))
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def rename_snapshot(self, snapshot_id, new_name):
        """Rename snapshot
        :param snapshot_id: The snapshot id
        :param new_name: The new name of the snapshot
        :return: Boolean indicating if rename operation is successful
        """

        try:
            if not self.module.check_mode:
                self.powerflex_conn.volume.rename(snapshot_id, new_name)
            return True
        except Exception as e:
            errormsg = "Rename snapshot %s operation failed with " "error %s" % (
                snapshot_id,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def delete_snapshot(self, snapshot_id, remove_mode):
        """Delete snapshot
        :param snapshot_id: The snapshot id
        :param remove_mode: Removal mode for the snapshot
        :return: Boolean indicating if delete operation is successful
        """

        try:
            if not self.module.check_mode:
                self.powerflex_conn.volume.delete(snapshot_id, remove_mode)
            return True
        except Exception as e:
            errormsg = "Delete snapshot %s operation failed with " "error %s" % (
                snapshot_id,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def validate_desired_retention(self, desired_retention, retention_unit):
        """Validates the specified desired retention.
        :param desired_retention: Desired retention of the snapshot
        :param retention_unit: Retention unit for snapshot
        """

        if desired_retention is not None:
            if retention_unit == "hours" and (
                desired_retention < 1 or desired_retention > 744
            ):
                self.module.fail_json(
                    msg="Please provide a valid integer as the"
                    " desired retention between 1 and 744."
                )
            elif retention_unit == "days" and (
                desired_retention < 1 or desired_retention > 31
            ):
                self.module.fail_json(
                    msg="Please provide a valid integer as the"
                    " desired retention between 1 and 31."
                )

    def validate_parameters(self):
        """Validate the input parameters"""

        desired_retention = self.module.params["desired_retention"]
        retention_unit = self.module.params["retention_unit"]

        param_list = [
            "snapshot_name",
            "snapshot_id",
            "vol_name",
            "vol_id",
            "snapshot_new_name",
        ]
        for param in param_list:
            if (
                self.module.params[param] is not None
                and len(self.module.params[param].strip()) == 0
            ):
                error_msg = "Please provide valid %s" % param
                self.module.fail_json(msg=error_msg)

        if (retention_unit is not None) and not desired_retention:
            self.module.fail_json(
                msg="retention_unit can only be specified along with desired_retention"
            )

    def get_diff_after(self, snapshot_params, snapshot_details, modify_dict):
        """Get diff between playbook input and snapshot details
        :param snapshot_params: Dictionary of parameters input from playbook
        :param snapshot_details: Dictionary of snapshot details
        :return: Dictionary of parameters of differences"""

        if snapshot_params["state"] == "absent":
            return {}
        diff_dict = {}
        if snapshot_details is None:
            diff_dict = {"snapshot_name": snapshot_params["snapshot_name"]}
            if snapshot_params["vol_name"]:
                diff_dict["ancestorVolumeName"] = snapshot_params["vol_name"]
            if snapshot_params["vol_id"]:
                diff_dict["ancestorVolumeId"] = snapshot_params["vol_id"]
            if snapshot_params["desired_retention"]:
                diff_dict["retentionInHours"] = (
                    snapshot_params["desired_retention"]
                    if snapshot_params["retention_unit"] != "days"
                    else snapshot_params["desired_retention"] * 24
                )
        else:
            diff_dict = copy.deepcopy(snapshot_details)
            for key in modify_dict.keys():
                diff_dict[key] = modify_dict[key]
        return diff_dict

    def perform_module_operation(self):
        """
        Perform different actions on snapshot based on parameters passed in
        the playbook
        """
        snapshot_name = self.module.params["snapshot_name"]
        snapshot_id = self.module.params["snapshot_id"]
        vol_name = self.module.params["vol_name"]
        vol_id = self.module.params["vol_id"]
        snapshot_new_name = self.module.params["snapshot_new_name"]
        desired_retention = self.module.params["desired_retention"]
        retention_unit = self.module.params["retention_unit"]
        remove_mode = self.module.params["remove_mode"]
        state = self.module.params["state"]

        # result is a dictionary to contain end state and snapshot details
        changed = False
        result = dict(changed=False, snapshot_details={})

        self.validate_parameters()

        retention_unit = self.get_retention_unit(desired_retention, retention_unit)

        self.validate_desired_retention(desired_retention, retention_unit)

        snapshot_details = self.get_snapshot(snapshot_name, snapshot_id)

        modify_dict = None
        if snapshot_details:
            modify_dict = self.check_snapshot_modified(
                snapshot_details, snapshot_new_name, desired_retention, retention_unit
            )

        before_dict = snapshot_details if snapshot_details is not None else {}
        diff_dict = {}
        diff_dict = self.get_diff_after(self.module.params, snapshot_details, modify_dict)
        if self.module._diff:
            result["diff"] = dict(before=before_dict, after=diff_dict)

        if state == "present" and not snapshot_details:
            self.validate_create(
                snapshot_name,
                snapshot_id,
                vol_name,
                vol_id,
                snapshot_new_name,
                remove_mode,
            )
            changed = self.create_snapshot_with_detail(
                snapshot_name, vol_name, vol_id, desired_retention, retention_unit
            )

        if state == "present" and snapshot_details and modify_dict:
            changed = self.modify_val(
                snapshot_new_name,
                desired_retention,
                retention_unit,
                snapshot_details,
                modify_dict,
            )
            snapshot_name = snapshot_new_name if snapshot_new_name else snapshot_name

        if state == "absent" and snapshot_details:
            remove_mode = "ONLY_ME" if remove_mode is None else remove_mode
            changed = self.delete_snapshot(snapshot_details["id"], remove_mode)

        if state == "present":
            snapshot_details = self.get_snapshot(snapshot_name, snapshot_id)
            result["snapshot_details"] = snapshot_details

        result["changed"] = changed
        self.module.exit_json(**result)

    def get_retention_unit(self, desired_retention, retention_unit):
        if desired_retention and not retention_unit:
            retention_unit = "hours"
        return retention_unit

    def modify_val(
        self,
        snapshot_new_name,
        desired_retention,
        retention_unit,
        snapshot_details,
        modify_dict,
    ):
        changed = False
        if "name" in modify_dict:
            changed = self.rename_snapshot(snapshot_details["id"], snapshot_new_name)
        if "retentionInHours" in modify_dict:
            retention = calculate_retention(desired_retention, retention_unit)
            changed = self.modify_retention(snapshot_details["id"], retention)
        return changed

    def create_snapshot_with_detail(
        self, snapshot_name, vol_name, vol_id, desired_retention, retention_unit
    ):
        if vol_name:
            vol = self.get_volume(vol_name=vol_name)
            vol_id = vol["id"]

        retention = 0
        if desired_retention:
            retention = calculate_retention(desired_retention, retention_unit)

        system_id = self.get_system_id()

        changed = self.create_snapshot(snapshot_name, vol_id, system_id, retention)
        return changed

    def validate_create(
        self,
        snapshot_name,
        snapshot_id,
        vol_name,
        vol_id,
        snapshot_new_name,
        remove_mode,
    ):
        if snapshot_id:
            self.module.fail_json(
                msg="Creation of snapshot is allowed "
                "using snapshot_name only, "
                "snapshot_id given."
            )

        if snapshot_name is None or len(snapshot_name.strip()) == 0:
            self.module.fail_json(msg="Please provide valid snapshot name.")

        if vol_name is None and vol_id is None:
            self.module.fail_json(
                msg="Please provide volume details to create new snapshot"
            )

        if snapshot_new_name is not None:
            self.module.fail_json(
                msg="snapshot_new_name is not required while creating snapshot"
            )

        if remove_mode:
            self.module.fail_json(
                msg="remove_mode is not required while creating snapshot"
            )

    def check_snapshot_modified(
        self,
        snapshot=None,
        snapshot_new_name=None,
        desired_retention=None,
        retention_unit=None,
    ):
        """Check if snapshot modification is required
        :param snapshot: Snapshot details
        :param snapshot_new_name: New name of the snapshot
        :param desired_retention: Desired retention of the snapshot
        :param retention_unit: Retention unit for snapshot
        :return: Dictionary containing the attributes of Snapshot which are to be
                updated
        """
        modify_dict = {}

        if snapshot_new_name is not None and snapshot_new_name != snapshot["name"]:
            modify_dict["name"] = snapshot_new_name

        expiration_timestamp = None
        snap_creation_timestamp = get_snap_creation_time(snapshot)

        if desired_retention:
            expiration_timestamp = get_expiration_timestamp(
                desired_retention, retention_unit, snap_creation_timestamp
            )

        if (
            "secureSnapshotExpTime" in snapshot
            and expiration_timestamp
            and snapshot["secureSnapshotExpTime"] != expiration_timestamp
        ):
            existing_timestamp = snapshot["secureSnapshotExpTime"]
            new_timestamp = expiration_timestamp

            info_message = (
                "The existing timestamp is: %s and the new "
                "timestamp is: %s" % (existing_timestamp, new_timestamp)
            )
            LOG.info(info_message)

            existing_time_obj = datetime.fromtimestamp(existing_timestamp)
            new_time_obj = datetime.fromtimestamp(new_timestamp)

            td = get_datetime_diff_in_minutes(existing_time_obj, new_time_obj)

            LOG.info("Time difference: %s", td)

            # A delta of two minutes is treated as idempotent
            if td > 2:
                modify_dict["retentionInHours"] = (
                    desired_retention
                    if retention_unit != "days"
                    else desired_retention * 24
                )

        return modify_dict


def get_datetime_diff_in_minutes(dt1, dt2):
    """
    Calculates the difference in two datetime objects.
    Args:
        dt1 (datetime): The first datetime object.
        dt2 (datetime): The second datetime object.
    Returns:
        int: The difference in minutes between dt1 and dt2.
    Raises:
        TypeError: If dt1 or dt2 are None.
    """
    if dt1 is None:
        raise ValueError("First datetime cannot be None")
    if dt2 is None:
        raise ValueError("Second datetime cannot be None")
    if not isinstance(dt1, datetime):
        raise TypeError(
            f"First parameter is not a datetime object, it is {type(dt1).__name__}."
        )
    if not isinstance(dt2, datetime):
        raise TypeError(
            f"Second parameter not a datetime object, it is {type(dt2).__name__}."
        )

    if dt1 > dt2:
        td = dt1 - dt2
    else:
        td = dt2 - dt1
    return int(round(td.total_seconds() / 60))


def get_expiration_timestamp(
    desired_retention, retention_unit, snap_creation_timestamp
):
    if retention_unit == "hours":
        expiration_timestamp = datetime.fromtimestamp(
            snap_creation_timestamp
        ) + timedelta(hours=desired_retention)
        expiration_timestamp = time.mktime(expiration_timestamp.timetuple())
    else:
        expiration_timestamp = datetime.fromtimestamp(
            snap_creation_timestamp
        ) + timedelta(days=desired_retention)
        expiration_timestamp = time.mktime(expiration_timestamp.timetuple())
    return expiration_timestamp


def get_snap_creation_time(snapshot):
    snap_creation_timestamp = None
    if "creationTime" in snapshot:
        snap_creation_timestamp = snapshot["creationTime"]
    return snap_creation_timestamp


def calculate_retention(desired_retention=None, retention_unit=None):
    """
    :param desired_retention: Desired retention of the snapshot
    :param retention_unit: Retention unit for snapshot
    :return: Retention in minutes
    """

    retention = 0
    if retention_unit == "days":
        retention = desired_retention * 24 * 60
    else:
        retention = desired_retention * 60
    return retention


def get_powerflex_snapshot_parameters():
    """This method provide parameter required for the Ansible snapshot
    module on PowerFlex"""
    return dict(
        snapshot_name=dict(),
        snapshot_id=dict(),
        vol_name=dict(),
        vol_id=dict(),
        snapshot_new_name=dict(),
        desired_retention=dict(type="int"),
        retention_unit=dict(choices=["hours", "days"]),
        remove_mode=dict(choices=["ONLY_ME", "INCLUDING_DESCENDANTS"]),
        state=dict(
            type="str", choices=["present", "absent"], default="present"
        ),
    )


def main():
    """Create PowerFlex Snapshot object and perform actions on it
    based on user input from playbook"""
    obj = PowerFlexSnapshotV2()
    obj.perform_module_operation()


if __name__ == "__main__":
    main()
