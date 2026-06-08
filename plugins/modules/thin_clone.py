#!/usr/bin/python

# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for creating Thin Clones on Dell Technologies (Dell) PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
module: thin_clone
version_added: '3.1.0'
short_description: Create Thin Clones on Dell PowerFlex 5.x (Gen2)
description:
- Creates a thin clone from a source volume (including an existing thin
  clone, which is itself a volume) or from a read-only snapshot on a
  PowerFlex 5.x Gen2 storage system.
- "This module is CREATION-ONLY. Ongoing management of the resulting
  thin clone (rename, resize, map/unmap, delete) is the responsibility
  of the C(dellemc.powerflex.volume) module, following the PowerFlex
  Gen2 architecture pattern: System creates, Volume manages."
- Supported on PowerFlex 5.0 and above only.
extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2
author:
- Dell Technologies Ansible Team (@dell-ansible)
options:
  from_volume_name:
    description:
      - Name of the source volume (or source thin clone).
      - Mutually exclusive with I(from_volume_id), I(from_snapshot_name), and I(from_snapshot_id).
    type: str
  from_volume_id:
    description:
      - ID of the source volume (or source thin clone).
      - Mutually exclusive with I(from_volume_name), I(from_snapshot_name), and I(from_snapshot_id).
    type: str
  from_snapshot_name:
    description:
      - Name of the source (read-only) snapshot.
      - Mutually exclusive with I(from_snapshot_id), I(from_volume_name), and I(from_volume_id).
    type: str
  from_snapshot_id:
    description:
      - ID of the source (read-only) snapshot.
      - Mutually exclusive with I(from_snapshot_name), I(from_volume_name), and I(from_volume_id).
    type: str
  new_clone_name:
    description:
      - Name of the new thin clone volume to create.
      - Required. Must be non-empty.
    type: str
    required: true
  state:
    description:
      - Desired state. This module supports C(present) only.
      - Delete, rename, resize, and mapping are handled by C(dellemc.powerflex.volume_v2).
    type: str
    choices: ['present']
    default: present
attributes:
  check_mode:
    description: Runs task to validate without performing action.
    support: full
  diff_mode:
    description: Reports changes made or to be made.
    support: full
notes:
  - Requires PowerFlex 5.0 or later.
  - "Architecture: System creates, Volume manages. Use
    C(dellemc.powerflex.volume_v2) for rename, resize, map/unmap, delete,
    and other ongoing operations on the returned thin clone."
"""

EXAMPLES = r"""
- name: Create thin clone from a source volume
  dellemc.powerflex.thin_clone:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    from_volume_name: "src_vol"
    new_clone_name: "clone_a"
    state: present
"""

RETURN = r"""
changed:
    description: Whether a new thin clone was created.
    returned: always
    type: bool
volume_details:
    description: Details of the thin clone volume.
    returned: always
    type: dict
source_details:
    description: Resolved source used for the create operation.
    returned: always
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase

LOG = utils.get_logger("thin_clone")


@powerflex_compatibility(min_ver='5.0')
class PowerFlexThinClone(PowerFlexBase):
    """Class with Thin Clone operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        argument_spec = get_powerflex_thin_clone_parameters()

        mutually_exclusive = [
            ['from_volume_name', 'from_volume_id',
             'from_snapshot_name', 'from_snapshot_id'],
        ]

        required_one_of = [
            ['from_volume_name', 'from_volume_id',
             'from_snapshot_name', 'from_snapshot_id'],
        ]

        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive,
            'required_one_of': required_one_of,
        }

        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get_volume(self, vol_name=None, vol_id=None):
        """Get volume details by name or id.
        :param vol_name: Name of the volume
        :param vol_id: ID of the volume
        :return: Volume details dict
        """
        id_or_name = vol_id if vol_id else vol_name
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
                return None

            if len(vol_details) > 1:
                errormsg = (
                    "Multiple instances of volume "
                    "exist with name {0}".format(vol_name)
                )
                self.module.fail_json(msg=errormsg)

            return vol_details[0]
        except Exception as e:
            errormsg = "Failed to get the volume %s with error %s" % (
                id_or_name,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def get_system_id(self):
        """Get system id"""
        try:
            resp = self.powerflex_conn.system.get()

            if len(resp) == 0:
                self.module.fail_json(
                    msg="No system exist on the given host."
                )

            if len(resp) > 1:
                self.module.fail_json(
                    msg="Multiple systems exist on the given host."
                )
            return resp[0]["id"]
        except Exception as e:
            msg = "Failed to get system id with error %s" % str(e)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def resolve_source(self):
        """Resolve the source volume or snapshot.
        :return: tuple (source_dict, source_type, source_id, source_name)
        """
        from_volume_name = self.module.params.get("from_volume_name")
        from_volume_id = self.module.params.get("from_volume_id")
        from_snapshot_name = self.module.params.get("from_snapshot_name")
        from_snapshot_id = self.module.params.get("from_snapshot_id")

        if from_volume_name or from_volume_id:
            source = self.get_volume(
                vol_name=from_volume_name, vol_id=from_volume_id
            )
            if source is None:
                identifier = from_volume_name or from_volume_id
                self.module.fail_json(
                    msg="Source volume '%s' not found" % identifier
                )
            return source, "volume", source["id"], source.get("name")

        if from_snapshot_name or from_snapshot_id:
            source = self.get_volume(
                vol_name=from_snapshot_name, vol_id=from_snapshot_id
            )
            if source is None:
                identifier = from_snapshot_name or from_snapshot_id
                self.module.fail_json(
                    msg="Source snapshot '%s' not found" % identifier
                )
            return source, "snapshot", source["id"], source.get("name")

        self.module.fail_json(
            msg="Exactly one of from_volume_name, from_volume_id, "
                "from_snapshot_name, from_snapshot_id is required"
        )

    def check_idempotency(self, source_id, new_clone_name):
        """Check if a volume with new_clone_name already exists.
        :param source_id: ID of the resolved source
        :param new_clone_name: Target clone name
        :return: tuple (exists: bool, existing_clone: dict or None)
        """
        existing = self.get_volume(vol_name=new_clone_name)
        if existing is None:
            return False, None

        ancestor_id = existing.get("ancestorVolumeId")
        if ancestor_id is None or ancestor_id != source_id:
            self.module.fail_json(
                msg="Volume '%s' already exists and is not a thin clone "
                    "of the requested source (FC-TC-015)" % new_clone_name
            )

        return True, existing

    def create_thin_clone(self, system_id, source_id, new_clone_name):
        """Create thin clone via SDK.
        :param system_id: System ID
        :param source_id: Source volume/snapshot ID
        :param new_clone_name: Name for the new clone
        :return: Create response dict
        """
        try:
            snapshot_defs = [
                {"volumeId": source_id, "snapshotName": new_clone_name}
            ]
            response = self.powerflex_conn.system.create_thin_clone(
                system_id, snapshot_defs
            )
            LOG.info(
                "Created thin clone %s from source %s",
                new_clone_name, source_id
            )
            return response
        except Exception as e:
            errormsg = (
                "Failed to create thin clone %s with error %s"
                % (new_clone_name, str(e))
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def validate_input_params(self):
        """Validate input parameters."""
        new_clone_name = self.module.params.get("new_clone_name")
        if new_clone_name is not None and len(new_clone_name.strip()) == 0:
            self.module.fail_json(
                msg="new_clone_name is required and must be non-empty"
            )

        from_volume = (
            self.module.params.get("from_volume_name")
            or self.module.params.get("from_volume_id")
        )
        from_snapshot = (
            self.module.params.get("from_snapshot_name")
            or self.module.params.get("from_snapshot_id")
        )
        if from_volume and from_snapshot:
            self.module.fail_json(
                msg="from_volume_* and from_snapshot_* are mutually exclusive"
            )

    def perform_module_operation(self):
        """Perform different actions on thin clone based on parameters."""
        new_clone_name = self.module.params["new_clone_name"]

        result = dict(
            changed=False,
            volume_details={},
            source_details={},
        )

        self.validate_input_params()

        source, source_type, source_id, source_name = self.resolve_source()

        result["source_details"] = {
            "source_type": source_type,
            "source_id": source_id,
            "source_name": source_name,
        }

        exists, existing_clone = self.check_idempotency(
            source_id, new_clone_name
        )

        if exists:
            result["changed"] = False
            result["volume_details"] = existing_clone
            if self.module._diff:
                result["diff"] = dict(
                    before=existing_clone, after=existing_clone
                )
            self.module.exit_json(**result)
            return

        if self.module.check_mode:
            planned = {
                "name": new_clone_name,
                "ancestorVolumeId": source_id,
                "volumeType": "ThinClone",
            }
            result["changed"] = True
            if self.module._diff:
                result["diff"] = dict(before={}, after=planned)
            self.module.exit_json(**result)
            return

        system_id = self.get_system_id()

        create_response = self.create_thin_clone(
            system_id, source_id, new_clone_name
        )

        volume_id_list = create_response.get("volumeIdList", [])
        if not volume_id_list:
            self.module.fail_json(
                msg="Thin clone creation returned no volume IDs"
            )
        new_clone_id = volume_id_list[0]
        clone_details = self.get_volume(vol_id=new_clone_id)
        if clone_details is None:
            self.module.fail_json(
                msg="Failed to get the volume %s after creation"
                    % new_clone_id
            )

        result["changed"] = True
        result["volume_details"] = clone_details

        if self.module._diff:
            result["diff"] = dict(before={}, after=clone_details)

        self.module.exit_json(**result)


def get_powerflex_thin_clone_parameters():
    """Parameters required for the thin_clone module"""
    return dict(
        from_volume_name=dict(),
        from_volume_id=dict(),
        from_snapshot_name=dict(),
        from_snapshot_id=dict(),
        new_clone_name=dict(required=True),
        state=dict(
            type="str", choices=["present"], default="present"
        ),
    )


def main():
    """Create PowerFlex ThinClone object and perform actions on it"""
    obj = PowerFlexThinClone()
    obj.perform_module_operation()


if __name__ == "__main__":
    main()
