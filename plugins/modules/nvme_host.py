#!/usr/bin/python

# Copyright: (c) 2024, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" Ansible module for managing NVMe hosts on Dell Technologies (Dell) PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
module: nvme_host
version_added: '1.0.0'
short_description: Manage NVMe hosts on Dell PowerFlex
description:
- Managing NVMe hosts on PowerFlex storage system includes getting details of NVMe hosts
  and renaming NVMe hosts.

author:
- Peter Cao (@P-Cao) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerflex.powerflex

options:
  max_num_paths:
    description:
    - Maximum number of paths per volume. Used to create/modify the NVMe host.
    type: str
  max_num_sys_ports:
    description:
    - Maximum number of ports per protection domain. Used to create/modify the NVMe host.
    type: str
  nqn:
    description:
    - NQN of the NVMe host. Used to create/get/modify the NVMe host.
    type: str
  nvme_host_name:
    description:
    - Name of the NVMe host.
    - Specify either I(nvme_host_name), I(nqn) for create/get/rename operation.
    type: str
  nvme_host_new_name:
    description:
    - New name of the NVMe host. Used to rename the NVMe host.
    type: str
  state:
    description:
    - State of the NVMe host.
    choices: ['present', 'absent']
    required: true
    type: str
notes:
  - The I(check_mode) is not supported.
"""

EXAMPLES = r"""
- name: Create NVMe host
  dellemc.powerflex.nvme_host:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    nqn: "{{ nqn }}"
    nvme_host_name: "{{ nvme_host_name }}"
    state: "present"

- name: Rename nvme_host using NVMe host id
  dellemc.powerflex.nvme_host:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    nvme_host_name: "{{ nvme_host_name }}"
    nvme_host_new_name: "{{ nvme_host_new_name }}"
    state: "present"

- name: Set maximum number of paths per volume and maximum Number of Ports Per Protection Domain of nvme_host
  dellemc.powerflex.nvme_host:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    nvme_host_name: "{{ nvme_host_name }}"
    max_num_paths: "{{ max_num_paths }}"
    max_num_sys_ports: "{{ max_num_sys_ports }}"
    state: "present"

- name: Remove nvme_host
  dellemc.powerflex.nvme_host:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    nvme_host_name: "{{ nvme_host_name }}"
    state: "absent"
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'

nvme_host_details:
    description: Details of the NVMe host.
    returned: When NVMe host exists
    type: dict
    contains:
        max_num_paths:
            description: Maximum number of paths per volume. Used to create/modify the NVMe host.
            type: str
        max_num_sys_ports:
            description: Maximum number of ports per protection domain. Used to create/modify the NVMe host.
            type: str
        nvme_host_name:
            description: Name of the NVMe host.
            type: str
        nqn:
            description: NQN of the NVMe host. Used to create/get/modify the NVMe host.
            type: str
    sample: {
        "hostOsFullType": "Generic",
        "systemId": "264ec85b3855280f",
        "name": "name",
        "sdcApproved": null,
        "sdcAgentActive": null,
        "mdmIpAddressesCurrent": null,
        "sdcIp": null,
        "sdcIps": null,
        "osType": null,
        "perfProfile": null,
        "peerMdmId": null,
        "sdtId": null,
        "mdmConnectionState": null,
        "softwareVersionInfo": null,
        "socketAllocationFailure": null,
        "memoryAllocationFailure": null,
        "versionInfo": null,
        "sdcType": null,
        "nqn": "nqn.2014-08.org.nvmexpress:uuid:79e90a42-47c9-a0f6-d9d3-51c47c72c7c1",
        "maxNumPaths": 6,
        "maxNumSysPorts": 10,
        "sdcGuid": null,
        "installedSoftwareVersionInfo": null,
        "kernelVersion": null,
        "kernelBuildNumber": null,
        "sdcApprovedIps": null,
        "hostType": "NVMeHost",
        "sdrId": null,
        "id": "1040d67200010000",
        "links": [
            {
                "rel": "self",
                "href": "/api/instances/Host::1040d67200010000"
            },
            {
                "rel": "/api/Host/relationship/Volume",
                "href": "/api/instances/Host::1040d67200010000/relationships/Volume"
            },
            {
                "rel": "/api/Host/relationship/NvmeController",
                "href": "/api/instances/Host::1040d67200010000/relationships/NvmeController"
            },
            {
                "rel": "/api/parent/relationship/systemId",
                "href": "/api/instances/System::264ec85b3855280f"
            }
        ]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import (
    utils,
)

LOG = utils.get_logger("nvme")


class PowerFlexNvmeHost(object):
    """Class with NVMe host operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powerflex_gateway_host_parameters()
        self.module_params.update(get_powerflex_nvme_host_parameters())

        required_one_of = [["nvme_host_name", "nqn"]]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            required_one_of=required_one_of,
        )

        utils.ensure_required_libs(self.module)

        try:
            self.powerflex_conn = utils.get_powerflex_gateway_host_connection(
                self.module.params
            )
            LOG.info("Got the PowerFlex system connection object instance")
        except Exception as e:
            LOG.error(str(e))
            self.module.fail_json(msg=str(e))

    def perform_module_operation(self):
        """
        Perform different actions on NVMe host based on parameters passed in the playbook
        """
        nvme_host_name = self.module.params["nvme_host_name"]
        nvme_host_new_name = self.module.params["nvme_host_new_name"]
        max_num_paths = self.module.params["max_num_paths"]
        max_num_sys_ports = self.module.params["max_num_sys_ports"]
        nqn = self.module.params["nqn"]
        state = self.module.params["state"]

        changed = False
        result = dict(changed=False, nvme_host_details={})

        self.validate_parameters()

        # try to get NVMe host detail
        # nvme host can be queried using name or id
        nvme_host_details = self.get_nvme_host(
            nvme_host_name=nvme_host_name, nqn=nqn
        )
        if nvme_host_details:
            msg = "Fetched the NVMe host details %s" % str(nvme_host_details)
            LOG.info(msg)
        if state == "absent" and nvme_host_details:
            changed = self.remove(nvme_host_details["id"])

        if state == "present" and nvme_host_details:
            changed = self.perform_modify(
                nvme_host_details, nvme_host_new_name, max_num_paths, max_num_sys_ports
            )

        # do create operation if no host exists
        if state == "present" and not nvme_host_details:
            nvme_host_details, changed = self.process_host_creation(
                nvme_host_name,
                nvme_host_new_name,
                nqn,
                max_num_paths,
                max_num_sys_ports,
            )

        if changed:
            nvme_host_details = self.get_nvme_host(
                nvme_host_name=nvme_host_new_name or nvme_host_name,
                nqn=nqn,
            )

        result["nvme_host_details"] = nvme_host_details
        result["changed"] = changed
        self.module.exit_json(**result)

    def process_host_creation(
        self, nvme_host_name, nvme_host_new_name, nqn, max_num_paths, max_num_sys_ports
    ):
        """
        Create a new NVMe host based on the given parameters and retrieve the NVMe host details
        """
        if nvme_host_new_name:
            self.module.fail_json(
                msg="nvme_host_new_name parameter is not supported during "
                "creation of a NVMe host. Try renaming the NVMe host after"
                " the creation."
            )

        created_nvme = self.create_nvme_host(
            nqn=nqn,
            name=nvme_host_name,
            max_num_paths=max_num_paths,
            max_num_sys_ports=max_num_sys_ports,
        )

        if created_nvme:
            nvme_host_details = self.get_nvme_host(nvme_host_id=created_nvme["id"])
            msg = (
                "NVMe host created successfully, fetched "
                "NVMe host details %s" % str(nvme_host_details)
            )
            LOG.info(msg)
            return nvme_host_details, True
        return None, False

    def get_nvme_host(self, nvme_host_id=None, nvme_host_name=None, nqn=None):
        """Get the NVMe host Details
        :param nvme_host_name: The name of the NVMe host
        :param nvme_host_di: The ID of the NVMe host
        :return: The dict containing NVMe host details
        """
        id_name_map = {
            "id": nvme_host_id,
            "nqn": nqn,
            "name": nvme_host_name
        }
        id_name = next(((key, value) for key, value in id_name_map.items() if value), None)

        try:
            filter_field = None
            filter_value = None

            if id_name:
                filter_field, filter_value = id_name

            all_host_details = self.powerflex_conn.sdc.get()
            # Assign names to unnamed NVMe hosts and find the target host
            for nvme_host in all_host_details:
                if nvme_host.get("name") is None:
                    nvme_host["name"] = f"NVMeHost:{nvme_host['id']}"

            if filter_field is None or filter_value is None:
                return all_host_details[0] if all_host_details else None

            nvme_host_details = [
                host_entity for host_entity in all_host_details
                if host_entity.get(filter_field) == filter_value and host_entity.get('hostType') == 'NVMeHost'
            ]

            return nvme_host_details[0] if nvme_host_details else None

        except Exception as e:
            errormsg = "Failed to get the NVMe host %s with error %s" % (
                id_name,
                str(e),
            )
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def create_nvme_host(self, nqn, name, max_num_paths, max_num_sys_ports):
        """Create the NVMe host
        :param nqn: The NQN of the NVMe host
        :param name: The name of the NVMe host
        :param max_num_paths: The maximum number of paths per volume
        :param max_num_sys_ports: Maximum Number of Ports Per Protection Domain
        """
        try:
            if nqn is None or len(nqn.strip()) == 0:
                self.module.fail_json(msg="Please provide valid NQN.")
            host_id = self.powerflex_conn.host.create(
                nqn=nqn,
                name=name,
                max_num_paths=max_num_paths,
                max_num_sys_ports=max_num_sys_ports,
            )
            return host_id

        except Exception as e:
            errormsg = "Create NVMe host operation failed with " "error %s" % str(e)
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def validate_parameters(self):
        """Validate the input parameters"""

        host_identifiers = ["nvme_host_name", "nqn"]
        for param in host_identifiers:
            if (
                self.module.params[param] is not None
                and len(self.module.params[param].strip()) == 0
            ):
                msg = f"Please provide valid {param}"
                LOG.error(msg)
                self.module.fail_json(msg=msg)

        if (
            self.module.params["nvme_host_name"] is None
            and self.module.params["nqn"] is None
        ):
            msg = "Please provide at least one of nvme_host_name or nqn"
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def remove(self, nvme_id):
        """Remove the NVMe host"""
        try:
            LOG.info(msg=f"Failed to remove NVMe host {nvme_id}")
            self.powerflex_conn.sdc.delete(nvme_id)
            return True
        except Exception as e:
            errormsg = f"Failed to remove NVMe host {nvme_id} with error {str(e)}"
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def perform_modify(
        self, nvme_host_details, nvme_host_new_name, max_num_paths, max_num_sys_ports
    ):
        """
        Modifies the NVMe host with the given details.

        Args:
            nvme_host_details (dict): The details of the NVMe host.
            nvme_host_new_name (str): The new name of the NVMe host.
            max_num_paths (int): The new maximum number of paths per volume.
            max_num_sys_ports (int): The new maximum number of ports per protection domain.

        Returns:
            bool: True if the NVMe host was modified, False otherwise.

        Raises:
            Exception: If there was an error renaming the NVMe host or modifying its properties.
        """
        modified = False
        modified_fields = []
        if (
            nvme_host_new_name is not None
            and nvme_host_new_name != nvme_host_details["name"]
        ):
            try:
                self.powerflex_conn.sdc.rename(
                    sdc_id=nvme_host_details["id"], name=nvme_host_new_name
                )
                modified_fields.append("name")
                modified = True
            except Exception as e:
                errormsg = "Failed to rename NVMe host %s with error %s" % (
                    nvme_host_details["id"],
                    str(e),
                )
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)

        if max_num_paths and max_num_paths != str(nvme_host_details["maxNumPaths"]):
            try:
                self.powerflex_conn.host.modify_max_num_paths(
                    host_id=nvme_host_details["id"], max_num_paths=max_num_paths
                )
                modified_fields.append("max_num_paths")
                modified = True
            except Exception as e:
                msg = "Successfully modified the following fields: %s " % ", ".join(modified_fields)
                errormsg = (
                    "Failed to modify NVMe host %s max_num_paths with error %s. %s"
                    % (nvme_host_details["id"], str(e), msg if modified_fields else "")
                )
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)

        if max_num_sys_ports and max_num_sys_ports != str(nvme_host_details["maxNumSysPorts"]):
            try:
                self.powerflex_conn.host.modify_max_num_sys_ports(
                    host_id=nvme_host_details["id"], max_num_sys_ports=max_num_sys_ports
                )
                modified = True
            except Exception as e:
                msg = "Successfully modified the following fields: %s " % ", ".join(modified_fields)
                errormsg = (
                    "Failed to modify NVMe host %s max_num_sys_ports with error %s. %s"
                    % (nvme_host_details["id"], str(e), msg if modified_fields else "")
                )
                LOG.error(errormsg)
                self.module.fail_json(msg=errormsg)
        return modified


def get_powerflex_nvme_host_parameters():
    """This method provide parameter required for the Ansible NVMe host module on
    PowerFlex"""
    return dict(
        nqn=dict(type="str"),
        nvme_host_name=dict(type="str"),
        nvme_host_new_name=dict(type="str"),
        max_num_paths=dict(type="str"),
        max_num_sys_ports=dict(type="str"),
        state=dict(required=True, type="str", choices=["present", "absent"]),
    )


def main():
    """Create PowerFlex NVMe host and perform actions on it
    based on user input from playbook"""
    obj = PowerFlexNvmeHost()
    obj.perform_module_operation()


if __name__ == "__main__":
    main()
