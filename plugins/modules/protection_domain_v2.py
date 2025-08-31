#!/usr/bin/python

# Copyright: (c) 2021-25, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing protection domain on Dell Technologies (Dell) PowerFlex 5.x"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: protection_domain_v2
version_added: '3.0.0'
short_description: Managing protection domain on Dell PowerFlex 5.x

description:
- Dell PowerFlex protection domain module includes getting the details of
  protection domain, creating a new protection domain, and modifying the attribute of
  a protection domain.

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

author:
- Luis Liu (@vangork) <ansible.team@dell.com>

options:
  protection_domain_name:
    description:
    - The name of the protection domain.
    - Mandatory for create operation.
    - It is unique across the PowerFlex array.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - The ID of the protection domain.
    - Except for create operation, all other operations can be performed
      using protection_domain_id.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  protection_domain_new_name:
    description:
    - Used to rename the protection domain.
    type: str
  is_active:
    description:
        - Used to indicate the state of the protection domain and to activate or deactivate it.
        - When set to C(true), the protection domain will be in active state.
        - When set to C(false), the protection domain will be in inactive state.
    required: false
    type: bool
  state:
    description:
      - The state of the protection domain. Can be 'present' or 'absent'.
    required: true
    choices: ['present', 'absent']
    type: str
notes:
  - This module is supported on Dell PowerFlex 5.x and later versions.
  - The protection domain can only be deleted if all its related objects have
    been dissociated from the protection domain.
  - If the protection domain set to inactive, then no operation can be
    performed on protection domain.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Create protection domain
  dellemc.powerflex.protection_domain_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Create protection domain with all parameters
  dellemc.powerflex.protection_domain_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    protection_domain_name: "domain1"
    is_active: true
    state: present

- name: Get protection domain details using name
  dellemc.powerflex.protection_domain_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Get protection domain details using ID
  dellemc.powerflex.protection_domain_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_id: "5718253c00000004"
    state: "present"

- name: Modify protection domain attributes
  dellemc.powerflex.protection_domain_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    protection_domain_new_name: "domain1_new"
    state: "present"

- name: Delete protection domain using name
  dellemc.powerflex.protection_domain_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1_new"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
protection_domain_details:
    description: Details of the protection domain.
    returned: When protection domain exists
    type: dict
    contains:
        fglDefaultMetadataCacheSize:
            description: FGL metadata cache size.
            type: int
        fglDefaultNumConcurrentWrites:
            description: FGL concurrent writes.
            type: str
        fglMetadataCacheEnabled:
            description: Whether FGL cache enabled.
            type: bool
        id:
            description: Protection domain ID.
            type: str
        links:
            description: Protection domain links.
            type: list
            contains:
                href:
                    description: Protection domain instance URL.
                    type: str
                rel:
                    description: Protection domain's relationship with
                                 different entities.
                    type: str
        mdmSdsNetworkDisconnectionsCounterParameters:
            description: MDM's SDS counter parameter.
            type: dict
            contains:
                longWindow:
                    description: Long window for Counter Parameters.
                    type: int
                mediumWindow:
                    description: Medium window for Counter Parameters.
                    type: int
                shortWindow:
                    description: Short window for Counter Parameters.
                    type: int
        name:
            description: Name of the protection domain.
            type: str
        overallIoNetworkThrottlingEnabled:
            description: Whether overall network throttling enabled.
            type: bool
        overallIoNetworkThrottlingInKbps:
            description: Overall network throttling in KBps.
            type: int
        protectedMaintenanceModeNetworkThrottlingEnabled:
            description: Whether protected maintenance mode network throttling
                         enabled.
            type: bool
        protectedMaintenanceModeNetworkThrottlingInKbps:
            description: Protected maintenance mode network throttling in
                         KBps.
            type: int
        protectionDomainState:
            description: State of protection domain.
            type: int
        rebalanceNetworkThrottlingEnabled:
            description: Whether rebalance network throttling enabled.
            type: int
        rebalanceNetworkThrottlingInKbps:
            description: Rebalance network throttling in KBps.
            type: int
        rebuildNetworkThrottlingEnabled:
            description: Whether rebuild network throttling enabled.
            type: int
        rebuildNetworkThrottlingInKbps:
            description: Rebuild network throttling in KBps.
            type: int
        rfcacheAccpId:
            description: Id of RF cache acceleration pool.
            type: str
        rfcacheEnabled:
            description: Whether RF cache is enabled or not.
            type: bool
        rfcacheMaxIoSizeKb:
            description: RF cache maximum I/O size in KB.
            type: int
        rfcacheOpertionalMode:
            description: RF cache operational mode.
            type: str
        rfcachePageSizeKb:
            description: RF cache page size in KB.
            type: bool
        sdrSdsConnectivityInfo:
            description: Connectivity info of SDR and SDS.
            type: dict
            contains:
                clientServerConnStatus:
                    description: Connectivity status of client and server.
                    type: str
                disconnectedClientId:
                    description: Disconnected client ID.
                    type: str
                disconnectedClientName:
                    description: Disconnected client name.
                    type: str
                disconnectedServerId:
                    description: Disconnected server ID.
                    type: str
                disconnectedServerIp:
                    description: Disconnected server IP.
                    type: str
                disconnectedServerName:
                    description: Disconnected server name.
                    type: str
        sdsSdsNetworkDisconnectionsCounterParameters:
            description: Counter parameter for SDS-SDS network.
            type: dict
            contains:
                longWindow:
                    description: Long window for Counter Parameters.
                    type: int
                mediumWindow:
                    description: Medium window for Counter Parameters.
                    type: int
                shortWindow:
                    description: Short window for Counter Parameters.
                    type: int
        systemId:
            description: ID of system.
            type: str
        vtreeMigrationNetworkThrottlingEnabled:
            description: Whether V-Tree migration network throttling enabled.
            type: bool
        vtreeMigrationNetworkThrottlingInKbps:
            description: V-Tree migration network throttling in KBps.
            type: int
    sample: {
        "genType": "EC",
        "rebuildNetworkThrottlingEnabled": false,
        "rebalanceNetworkThrottlingEnabled": false,
        "vtreeMigrationNetworkThrottlingEnabled": false,
        "overallIoNetworkThrottlingEnabled": false,
        "rfcacheEnabled": true,
        "rfcacheAccpId": null,
        "rebuildEnabled": true,
        "rebalanceEnabled": true,
        "name": "domain1",
        "systemId": "815945c41cd8460f",
        "sdrSdsConnectivityInfo": {
            "clientServerConnStatus": "CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED",
            "disconnectedClientId": null,
            "disconnectedClientName": null,
            "disconnectedServerId": null,
            "disconnectedServerName": null,
            "disconnectedServerIp": null
        },
        "rplCapAlertLevel": "invalid",
        "protectionDomainState": "Active",
        "rebalanceNetworkThrottlingInKbps": null,
        "rebuildNetworkThrottlingInKbps": null,
        "overallIoNetworkThrottlingInKbps": null,
        "vtreeMigrationNetworkThrottlingInKbps": null,
        "sdsDecoupledCounterParameters": {
            "shortWindow": {
                "windowSizeInSec": 60,
                "threshold": 300
            },
            "mediumWindow": {
                "windowSizeInSec": 3600,
                "threshold": 500
            },
            "longWindow": {
                "windowSizeInSec": 86400,
                "threshold": 700
            }
        },
        "sdsConfigurationFailureCounterParameters": {
            "shortWindow": {
                "windowSizeInSec": 60,
                "threshold": 300
            },
            "mediumWindow": {
                "windowSizeInSec": 3600,
                "threshold": 500
            },
            "longWindow": {
                "windowSizeInSec": 86400,
                "threshold": 700
            }
        },
        "mdmSdsNetworkDisconnectionsCounterParameters": {
            "shortWindow": {
                "windowSizeInSec": 60,
                "threshold": 300
            },
            "mediumWindow": {
                "windowSizeInSec": 3600,
                "threshold": 500
            },
            "longWindow": {
                "windowSizeInSec": 86400,
                "threshold": 700
            }
        },
        "sdsSdsNetworkDisconnectionsCounterParameters": {
            "shortWindow": {
                "windowSizeInSec": 60,
                "threshold": 300
            },
            "mediumWindow": {
                "windowSizeInSec": 3600,
                "threshold": 500
            },
            "longWindow": {
                "windowSizeInSec": 86400,
                "threshold": 700
            }
        },
        "rfcacheOpertionalMode": "WriteMiss",
        "rfcachePageSizeKb": 64,
        "rfcacheMaxIoSizeKb": 128,
        "sdsReceiveBufferAllocationFailuresCounterParameters": {
            "shortWindow": {
                "windowSizeInSec": 60,
                "threshold": 20000
            },
            "mediumWindow": {
                "windowSizeInSec": 3600,
                "threshold": 200000
            },
            "longWindow": {
                "windowSizeInSec": 86400,
                "threshold": 2000000
            }
        },
        "fglDefaultNumConcurrentWrites": 1000,
        "fglMetadataCacheEnabled": false,
        "fglDefaultMetadataCacheSize": 0,
        "protectedMaintenanceModeNetworkThrottlingEnabled": false,
        "protectedMaintenanceModeNetworkThrottlingInKbps": null,
        "sdtSdsConnectivityInfo": {
            "clientServerConnStatus": "CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED",
            "disconnectedClientId": null,
            "disconnectedClientName": null,
            "disconnectedServerId": null,
            "disconnectedServerName": null,
            "disconnectedServerIp": null
        },
        "overallConcurrentIoLimit": 4,
        "bandwidthLimitOverallIos": 400,
        "bandwidthLimitBgDevScanner": 10,
        "bandwidthLimitSinglyImpactedRebuild": 400,
        "bandwidthLimitDoublyImpactedRebuild": 400,
        "bandwidthLimitRebalance": 40,
        "bandwidthLimitOther": 10,
        "bandwidthLimitNodeNetwork": 25,
        "id": "e59841fd00000002",
        "links": [
            {
                "rel": "self",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002"
            },
            {
                "rel": "/dtapi/rest/v1/metrics/query",
                "href": "/dtapi/rest/v1/metrics/query",
                "body": {
                    "resource_type": "protection_domain",
                    "ids": [
                        "e59841fd00000002"
                    ]
                }
            },
            {
                "rel": "/api/ProtectionDomain/relationship/Sdr",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/Sdr"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/Dgwt",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/Dgwt"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/AccelerationPool",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/AccelerationPool"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/Sdt",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/Sdt"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/StoragePool",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/StoragePool"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/Sds",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/Sds"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/ReplicationConsistencyGroup",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/ReplicationConsistencyGroup"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/DeviceGroup",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/DeviceGroup"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/FaultSet",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/FaultSet"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/StorageNode",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/StorageNode"
            },
            {
                "rel": "/api/ProtectionDomain/relationship/Pds",
                "href": "/api/instances/ProtectionDomain::e59841fd00000002/relationships/Pds"
            },
            {
                "rel": "/api/parent/relationship/systemId",
                "href": "/api/instances/System::815945c41cd8460f"
            }
        ]
    }
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase, powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils


LOG = utils.get_logger('protection_domain_v2')


@powerflex_compatibility(min_ver='5.0', predecessor='protection_domain')
class PowerFlexProtectionDomainV2(PowerFlexBase):
    """Class with protection domain operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        argument_spec = dict(
            protection_domain_name=dict(type='str'),
            protection_domain_new_name=dict(type='str'),
            protection_domain_id=dict(type='str'),
            is_active=dict(type='bool'),
            state=dict(required=True, type='str',
                       choices=['present', 'absent'])
        )

        mut_ex_args = [['protection_domain_name', 'protection_domain_id']]

        required_one_of_args = [['protection_domain_name',
                                 'protection_domain_id']]

        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': True,
            'mutually_exclusive': mut_ex_args,
            'required_one_of': required_one_of_args,
        }

        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get(self, id, name):
        """
        Get protection domain details
        :param id: ID of the protection domain
        :type id: str
        :param name: Name of the protection domain
        :type name: str
        :return: Protection domain details if exists
        :rtype: dict
        """
        name_or_id = id if id else name
        try:
            if id:
                pd_details = self.powerflex_conn.protection_domain.get_by_id(
                    id)
            else:
                pd_details = self.powerflex_conn.protection_domain.get_by_name(
                    name)

            return pd_details
        except Exception as e:
            error_msg = (
                "Failed to get the protection domain '%s' with "
                "error '%s'" % (name_or_id, str(e))
            )
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def delete(self, pd):
        """
        Delete Protection Domain
        :param pd: protection domain
        :type pd: dict
        :rtype: None
        """
        try:
            self.powerflex_conn.protection_domain.delete(pd["id"])
            LOG.info("Protection domain deleted successfully.")
        except Exception as e:
            error_msg = f"Delete protection domain '{pd['name']}' operation failed with error '{str(e)}'"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def create(self, protection_domain):
        """
        Create protection domain
        :param protection_domain: Dict of the protection domain
        :type protection_domain: dict
        :return: Dict representation of the created protection domain
        """
        try:
            LOG.info("Creating protection domain with name: %s ",
                     protection_domain['name'])

            self.is_id_or_new_name_in_create()
            self.powerflex_conn.protection_domain.check_create_params(
                protection_domain)
            if self.module.check_mode:
                return protection_domain
            return self.powerflex_conn.protection_domain.create(protection_domain)
        except Exception as e:
            error_msg = (f"Create protection domain '{protection_domain['name']}'"
                         f" operation failed with error '{str(e)}'")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update(self, protection_domain, current_protection_domain=None):
        """
        Modify protection domain attributes
        :param protection_domain: Dictionary containing the attributes of
                            protection domain which are to be updated
        :type protection_domain: dict
        :param current_protection_domain: Current state of protection domain
        :type current_protection_domain: dict
        :return: Bool to indicate if protection domain is updated,
                 Dict representation of the updated protection domain
        """
        try:
            LOG.info("Updating protection domain with id: %s ",
                     protection_domain['id'])
            self.powerflex_conn.protection_domain.check_update_params(
                protection_domain, current_protection_domain)
            if self.module.check_mode:
                protection_domain["name"] = protection_domain.get(
                    "newName", protection_domain["name"])
                protection_domain.pop("newName", None)
                need_update, changes = self.powerflex_conn.protection_domain.need_update(
                    protection_domain, current_protection_domain)
                return need_update, current_protection_domain | changes

            return self.powerflex_conn.protection_domain.update(protection_domain, current_protection_domain)
        except Exception as e:
            err_msg = f"Failed to update the protection domain {protection_domain['id']} with error {str(e)}"
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def validate_input_params(self):
        """Validate the input parameters"""

        name_params = ['protection_domain_name', 'protection_domain_new_name',
                       'protection_domain_id']
        msg = "Please provide the valid {0}"

        for n_item in name_params:
            if self.module.params[n_item] is not None and (len(
                    self.module.params[n_item].strip()) or self.
                    module.params[n_item].count(" ") > 0) == 0:
                err_msg = msg.format(n_item)
                self.module.fail_json(msg=err_msg)

    def is_id_or_new_name_in_create(self):
        """Checking if protection domain id or new names present in create """

        if self.module.params['protection_domain_new_name'] or \
                self.module.params['protection_domain_id']:
            error_msg = "protection_domain_new_name/protection_domain_id " \
                        "are not supported during creation of protection " \
                        "domain. Please try with protection_domain_name."
            LOG.info(error_msg)
            self.module.fail_json(msg=error_msg)

    def perform_module_operation(self):
        """
        Perform different actions on protection domain based on parameters
        passed in the playbook
        """
        protection_domain_name = self.module.params['protection_domain_name']
        protection_domain_id = self.module.params['protection_domain_id']
        protection_domain_new_name = self.module.params['protection_domain_new_name']
        is_active = self.module.params['is_active']
        state = self.module.params['state']

        result = dict(
            changed=False,
            protection_domain_details=None
        )

        # Checking invalid value for id, name and rename
        self.validate_input_params()

        pd_details = self.get(
            protection_domain_id,
            protection_domain_name,
        )

        if state == 'absent':
            if pd_details:
                result['changed'] = True
                result["diff"] = dict(before=pd_details, after={})
                if not self.module.check_mode:
                    self.delete(pd_details)
            self.module.exit_json(**result)

        protection_domain = {
            "name": protection_domain_name,
            "newName": protection_domain_new_name,
            "protectionDomainState": (
                "Active" if is_active else "Inactive"
            ) if is_active is not None else None,
        }
        protection_domain = {k: v for k,
                             v in protection_domain.items() if v is not None}

        if not pd_details:
            pd = self.create(
                protection_domain)
            changed = True
        else:
            protection_domain['id'] = pd_details['id']
            changed, pd = self.update(
                protection_domain, pd_details)

        result["diff"] = dict(
            before=pd_details if pd_details else {}, after=copy.deepcopy(pd))
        result['protection_domain_details'] = pd
        result['changed'] = changed
        self.module.exit_json(**result)


def main():
    """ Create PowerFlex protection domain object and perform actions on it
        based on user input from playbook"""
    obj = PowerFlexProtectionDomainV2()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
