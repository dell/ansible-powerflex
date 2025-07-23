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
  - dellemc.powerflex.powerflex

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
      - Used to activate or deactivate the protection domain.
    required: false
    type: bool
  rebuild_enabled:
    description:
      - Used to enable or disable rebuild.
    required: false
    type: bool
  rebalance_enabled:
    description:
      - Used to enable or disable rebalance.
    required: false
    type: bool
  io_policy:
    description:
      - The I/O policy of the protection domain.
    required: false
    type: dict
    suboptions:
      overall_concurrent_io_limit:
        description:
          - The overall concurrent I/O limit.
        required: false
        type: int
      bandwidth_limit_overall_ios:
        description:
          - The bandwidth limit for overall I/O.
        required: false
        type: int
      bandwidth_limit_bg_dev_scanner:
        description:
          - The bandwidth limit for background device scanner.
        required: false
        type: int
      bandwidth_limit_garbage_collector:
        description:
          - The bandwidth limit for garbage collector.
        required: false
        type: int
      bandwidth_limit_singly_impacted_rebuild:
        description:
          - The bandwidth limit for singly impacted rebuild.
        required: false
        type: int
      bandwidth_limit_doubly_impacted_rebuild:
        description:
          - The bandwidth limit for doubly impacted rebuild.
        required: false
        type: int
      bandwidth_limit_rebalance:
        description:
          - The bandwidth limit for rebalance.
        required: false
        type: int
      bandwidth_limit_other:
        description:
          - The bandwidth limit for other operations.
        required: false
        type: int
      bandwidth_limit_node_network:
        description:
          - The bandwidth limit for node network.
        required: false
        type: int
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
  - The I(check_mode) is not supported.
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
    rebuild_enabled: true
    rebalance_enabled: true
    io_policy:
      overall_concurrent_io_limit: 1000
      bandwidth_limit_overall_ios: 100
      bandwidth_limit_bg_dev_scanner: 50
      bandwidth_limit_garbage_collector: 20
      bandwidth_limit_singly_impacted_rebuild: 30
      bandwidth_limit_doubly_impacted_rebuild: 40
      bandwidth_limit_rebalance: 50
      bandwidth_limit_other: 60
      bandwidth_limit_node_network: 70
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
    rebuild_enabled: false
    rebalance_enabled: false
    io_policy:
      overall_concurrent_io_limit: 500
      bandwidth_limit_overall_ios: 50
      bandwidth_limit_bg_dev_scanner: 20
      bandwidth_limit_garbage_collector: 10
      bandwidth_limit_singly_impacted_rebuild: 20
      bandwidth_limit_doubly_impacted_rebuild: 30
      bandwidth_limit_rebalance: 40
      bandwidth_limit_other: 50
      bandwidth_limit_node_network: 60
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
        storagePool:
            description: List of storage pools.
            type: list
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
        "fglDefaultMetadataCacheSize": 0,
        "fglDefaultNumConcurrentWrites": 1000,
        "fglMetadataCacheEnabled": false,
        "id": "7bd6457000000000",
        "links": [
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000",
                "rel": "self"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/Statistics",
                "rel": "/api/ProtectionDomain/relationship/Statistics"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/Sdr",
                "rel": "/api/ProtectionDomain/relationship/Sdr"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/AccelerationPool",
                "rel": "/api/ProtectionDomain/relationship/AccelerationPool"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/StoragePool",
                "rel": "/api/ProtectionDomain/relationship/StoragePool"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/Sds",
                "rel": "/api/ProtectionDomain/relationship/Sds"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/ReplicationConsistencyGroup",
                "rel": "/api/ProtectionDomain/relationship/
                        ReplicationConsistencyGroup"
            },
            {
                "href": "/api/instances/ProtectionDomain::7bd6457000000000/
                        relationships/FaultSet",
                "rel": "/api/ProtectionDomain/relationship/FaultSet"
            },
            {
                "href": "/api/instances/System::0989ce79058f150f",
                "rel": "/api/parent/relationship/systemId"
            }
        ],
        "mdmSdsNetworkDisconnectionsCounterParameters": {
            "longWindow": {
                "threshold": 700,
                "windowSizeInSec": 86400
            },
            "mediumWindow": {
                "threshold": 500,
                "windowSizeInSec": 3600
            },
            "shortWindow": {
                "threshold": 300,
                "windowSizeInSec": 60
            }
        },
        "name": "domain1",
        "overallIoNetworkThrottlingEnabled": false,
        "overallIoNetworkThrottlingInKbps": null,
        "protectedMaintenanceModeNetworkThrottlingEnabled": false,
        "protectedMaintenanceModeNetworkThrottlingInKbps": null,
        "protectionDomainState": "Active",
        "rebalanceNetworkThrottlingEnabled": false,
        "rebalanceNetworkThrottlingInKbps": null,
        "rebuildNetworkThrottlingEnabled": false,
        "rebuildNetworkThrottlingInKbps": null,
        "rfcacheAccpId": null,
        "rfcacheEnabled": true,
        "rfcacheMaxIoSizeKb": 128,
        "rfcacheOpertionalMode": "WriteMiss",
        "rfcachePageSizeKb": 64,
        "sdrSdsConnectivityInfo": {
            "clientServerConnStatus": "CLIENT_SERVER_CONN_STATUS_ALL
                                      _CONNECTED",
            "disconnectedClientId": null,
            "disconnectedClientName": null,
            "disconnectedServerId": null,
            "disconnectedServerIp": null,
            "disconnectedServerName": null
        },
        "sdsConfigurationFailureCounterParameters": {
            "longWindow": {
                "threshold": 700,
                "windowSizeInSec": 86400
            },
            "mediumWindow": {
                "threshold": 500,
                "windowSizeInSec": 3600
            },
            "shortWindow": {
                "threshold": 300,
                "windowSizeInSec": 60
            }
        },
        "sdsDecoupledCounterParameters": {
            "longWindow": {
                "threshold": 700,
                "windowSizeInSec": 86400
            },
            "mediumWindow": {
                "threshold": 500,
                "windowSizeInSec": 3600
            },
            "shortWindow": {
                "threshold": 300,
                "windowSizeInSec": 60
            }
        },
        "sdsReceiveBufferAllocationFailuresCounterParameters": {
            "longWindow": {
                "threshold": 2000000,
                "windowSizeInSec": 86400
            },
            "mediumWindow": {
                "threshold": 200000,
                "windowSizeInSec": 3600
            },
            "shortWindow": {
                "threshold": 20000,
                "windowSizeInSec": 60
            }
        },
        "sdsSdsNetworkDisconnectionsCounterParameters": {
            "longWindow": {
                "threshold": 700,
                "windowSizeInSec": 86400
            },
            "mediumWindow": {
                "threshold": 500,
                "windowSizeInSec": 3600
            },
            "shortWindow": {
                "threshold": 300,
                "windowSizeInSec": 60
            }
        },
        "storagePool": [
            {
                "id": "8d1cba1700000000",
                "name": "pool1"
            }
        ],
        "systemId": "0989ce79058f150f",
        "vtreeMigrationNetworkThrottlingEnabled": false,
        "vtreeMigrationNetworkThrottlingInKbps": null
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils


LOG = utils.get_logger('protection_domain_v2')


class PowerFlexProtectionDomainV2(PowerFlexBase):
    """Class with protection domain operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        argument_spec = dict(
            protection_domain_name=dict(),
            protection_domain_new_name=dict(),
            protection_domain_id=dict(type='str'),
            is_active=dict(type='bool'),
            rebuild_enabled=dict(type='bool'),
            rebalance_enabled=dict(type='bool'),
            io_policy=dict(type='dict', options=dict(
                overall_concurrent_io_limit=dict(type='int'),
                bandwidth_limit_overall_ios=dict(type='int'),
                bandwidth_limit_bg_dev_scanner=dict(type='int'),
                bandwidth_limit_garbage_collector=dict(type='int'),
                bandwidth_limit_singly_impacted_rebuild=dict(type='int'),
                bandwidth_limit_doubly_impacted_rebuild=dict(type='int'),
                bandwidth_limit_rebalance=dict(type='int'),
                bandwidth_limit_other=dict(type='int'),
                bandwidth_limit_node_network=dict(type='int'),
            )),
            state=dict(required=True, type='str',
                       choices=['present', 'absent'])
        )

        mut_ex_args = [['protection_domain_name', 'protection_domain_id']]

        required_one_of_args = [['protection_domain_name',
                                 'protection_domain_id']]

        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': False,
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
            error_msg = "Failed to get the protection domain '%s' with " \
                        "error '%s'" % (name_or_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def delete(self, id):
        """
        Delete Protection Domain
        :param id: ID of the protection domain
        :type id: str
        :rtype: None
        """
        try:
            self.powerflex_conn.protection_domain.delete(id)
            LOG.info("Protection domain deleted successfully.")
        except Exception as e:
            error_msg = "Delete protection domain '%s' operation failed" \
                        " with error '%s'" % (id, str(e))
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
            return self.powerflex_conn.protection_domain.create(protection_domain)
        except Exception as e:
            error_msg = "Create protection domain '%s' operation failed" \
                        " with error '%s'" % (
                            protection_domain['name'], str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update(self, protection_domain, current_protection_domain=None):
        """
        Modify protection domain attributes
        :param protection_domain: Dictionary containing the attributes of
                            protection domain which are to be updated
        :type protection_domain: dict
        :return: Bool to indicate if protection domain is updated,
                 Dict representation of the updated protection domain
        """
        try:
            LOG.info("Updating protection domain with id: %s ",
                     protection_domain['id'])
            return self.powerflex_conn.protection_domain.update(protection_domain, current_protection_domain)
        except Exception as e:
            err_msg = "Failed to update the protection domain {0}" \
                " with error {1}".format(protection_domain['id'], str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def exec(self):
        """
        Perform different actions on protection domain based on parameters
        passed in the playbook
        """
        protection_domain_name = self.module.params['name']
        protection_domain_id = self.module.params['id']
        is_active = self.module.params['is_active']
        rebuild_enabled = self.module.params['rebuild_enabled']
        rebalance_enabled = self.module.params['rebalance_enabled']
        io_policy = self.module.params['io_policy']
        overall_concurrent_io_limit = None if io_policy is None else io_policy[
            'overall_concurrent_io_limit']
        bandwidth_limit_overall_ios = None if io_policy is None else io_policy[
            'bandwidth_limit_overall_ios']
        bandwidth_limit_bg_dev_scanner = None if io_policy is None else io_policy[
            'bandwidth_limit_bg_dev_scanner']
        bandwidth_limit_garbage_collector = None if io_policy is None else io_policy[
            'bandwidth_limit_garbage_collector']
        bandwidth_limit_singly_impacted_rebuild = None if io_policy is None else io_policy[
            'bandwidth_limit_singly_impacted_rebuild']
        bandwidth_limit_doubly_impacted_rebuild = None if io_policy is None else io_policy[
            'bandwidth_limit_doubly_impacted_rebuild']
        bandwidth_limit_rebalance = None if io_policy is None else io_policy[
            'bandwidth_limit_rebalance']
        bandwidth_limit_other = None if io_policy is None else io_policy['bandwidth_limit_other']
        bandwidth_limit_node_network = None if io_policy is None else io_policy[
            'bandwidth_limit_node_network']
        state = self.module.params['state']

        result = dict(
            changed=False,
            protection_domain_details=None
        )

        pd_details = self.get(
            protection_domain_id,
            protection_domain_name,
        )

        if state == 'absent':
            if pd_details:
                self.delete(pd_details['id'])
                result['changed'] = True
            self.module.exit_json(**result)
            return

        protection_domain = {}
        if protection_domain_name is not None:
            protection_domain['name'] = protection_domain_name
        if is_active is not None:
            protection_domain['protectionDomainState'] = "Active" if is_active else "Inactive"
        if rebuild_enabled is not None:
            protection_domain['rebuildEnabled'] = rebuild_enabled
        if rebalance_enabled is not None:
            protection_domain['rebalanceEnabled'] = rebalance_enabled
        if overall_concurrent_io_limit is not None:
            protection_domain['overallConcurrentIoLimit'] = overall_concurrent_io_limit
        if bandwidth_limit_overall_ios is not None:
            protection_domain['bandwidthLimitOverallIos'] = bandwidth_limit_overall_ios
        if bandwidth_limit_bg_dev_scanner is not None:
            protection_domain['bandwidthLimitBgDevScanner'] = bandwidth_limit_bg_dev_scanner
        if bandwidth_limit_garbage_collector is not None:
            protection_domain['bandwidthLimitGarbageCollector'] = bandwidth_limit_garbage_collector
        if bandwidth_limit_singly_impacted_rebuild is not None:
            protection_domain['bandwidthLimitSinglyImpactedRebuild'] = bandwidth_limit_singly_impacted_rebuild
        if bandwidth_limit_doubly_impacted_rebuild is not None:
            protection_domain['bandwidthLimitDoublyImpactedRebuild'] = bandwidth_limit_doubly_impacted_rebuild
        if bandwidth_limit_rebalance is not None:
            protection_domain['bandwidthLimitRebalance'] = bandwidth_limit_rebalance
        if bandwidth_limit_other is not None:
            protection_domain['bandwidthLimitOther'] = bandwidth_limit_other
        if bandwidth_limit_node_network is not None:
            protection_domain['bandwidthLimitNodeNetwork'] = bandwidth_limit_node_network

        if not pd_details:
            result['protection_domain_details'] = self.create(
                protection_domain)
            result['changed'] = True
        else:
            protection_domain['id'] = pd_details['id']
            result['changed'], result['protection_domain_details'] = self.update(
                protection_domain, pd_details)

        self.module.exit_json(**result)


def main():
    """ Create PowerFlex protection domain object and perform actions on it
        based on user input from playbook"""
    obj = PowerFlexProtectionDomainV2()
    obj.exec()


if __name__ == '__main__':
    main()
