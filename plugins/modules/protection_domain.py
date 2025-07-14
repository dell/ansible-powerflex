#!/usr/bin/python

# Copyright: (c) 2022, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" Ansible module for managing Protection Domain on Dell Technologies (Dell) PowerFlex"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
module: protection_domain
version_added: '1.2.0'
short_description: Manage Protection Domain on Dell PowerFlex
description:
- Managing Protection Domain on PowerFlex storage system includes creating,
  modifying attributes, deleting and getting details of Protection Domain.
author:
- Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>
extends_documentation_fragment:
  - dellemc.powerflex.powerflex
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
    type: bool
  network_limits:
    description:
    - Network bandwidth limit used by all SDS in protection domain.
    type: dict
    suboptions:
      rebuild_limit:
        description:
        - Limit the network bandwidth for rebuild.
        type: int
      rebalance_limit:
        description:
        - Limit the network bandwidth for rebalance.
        type: int
      vtree_migration_limit:
        description:
        - Limit the network bandwidth for vtree migration.
        type: int
      overall_limit:
        description:
        - Limit the overall network bandwidth.
        type: int
      bandwidth_unit:
        description:
        - Unit for network bandwidth limits.
        type: str
        choices: ['KBps', 'MBps', 'GBps']
        default: 'KBps'
  rf_cache_limits:
    description:
    - Used to set the RFcache parameters of the protection domain.
    type: dict
    suboptions:
      is_enabled:
        description:
        - Used to enable or disable RFcache in the protection domain.
        type: bool
      page_size:
        description:
        - Used to set the cache page size in KB.
        type: int
      max_io_limit:
        description:
        - Used to set cache maximum I/O limit in KB.
        type: int
      pass_through_mode:
        description:
        - Used to set the cache mode.
        choices: ['None', 'Read', 'Write', 'ReadAndWrite', 'WriteMiss']
        type: str
  state:
    description:
    - State of the protection domain.
    required: true
    type: str
    choices: ['present', 'absent']
notes:
  - The protection domain can only be deleted if all its related objects have
    been dissociated from the protection domain.
  - If the protection domain set to inactive, then no operation can be
    performed on protection domain.
  - The I(check_mode) is not supported.
'''

EXAMPLES = r'''
- name: Create protection domain
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Create protection domain with all parameters
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    is_active: true
    network_limits:
      rebuild_limit: 10
      rebalance_limit: 17
      vtree_migration_limit: 14
      overall_limit: 20
      bandwidth_unit: "MBps"
    rf_cache_limits:
      is_enabled: true
      page_size: 16
      max_io_limit: 128
      pass_through_mode: "Read"
    state: "present"

- name: Get protection domain details using name
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Get protection domain details using ID
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_id: "5718253c00000004"
    state: "present"

- name: Modify protection domain attributes
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    protection_domain_new_name: "domain1_new"
    network_limits:
      rebuild_limit: 14
      rebalance_limit: 20
      overall_limit: 25
      bandwidth_unit: "MBps"
    rf_cache_limits:
      page_size: 64
      pass_through_mode: "WriteMiss"
    state: "present"

- name: Delete protection domain using name
  dellemc.powerflex.protection_domain:
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
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils


LOG = utils.get_logger('protection_domain')


class PowerFlexProtectionDomain(object):
    """Class with protection domain operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powerflex_gateway_host_parameters()
        self.module_params.update(dict(
            name=dict(type='str'),
            id=dict(type='str'),
            is_active=dict(type='bool'),
            rebuild_enabled=dict(type='bool'),
            rebalance_enabled=dict(type='bool'),
            overall_concurrent_io_limit=dict(type='int'),
            bandwidth_limit_overall_ios=dict(type='int'),
            bandwidth_limit_bg_dev_scanner=dict(type='int'),
            bandwidth_limit_garbage_collector=dict(type='int'),
            bandwidth_limit_singly_impacted_rebuild=dict(type='int'),
            bandwidth_limit_doubly_impacted_rebuild=dict(type='int'),
            bandwidth_limit_rebalance=dict(type='int'),
            bandwidth_limit_other=dict(type='int'),
            bandwidth_limit_node_network=dict(type='int'),
            state=dict(type='str', choices=['present', 'absent'])
        ))

        required_one_of_args = [['name', 'id']]

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False,
            required_one_of=required_one_of_args,
            # mutually_exclusive
            # required_together
            # required_if
            # required_by
        )

        utils.ensure_required_libs(self.module)

        try:
            self.powerflex_conn = utils.get_powerflex_gateway_host_connection(
                self.module.params)
            LOG.info("Got the PowerFlex system connection object instance")
        except Exception as e:
            LOG.error(str(e))
            self.module.fail_json(msg=str(e))

    def validate_input_params(self):
        """Validate the input parameters"""

    def get_protection_domain(self, name=None, id=None):
        """
        Get protection domain details
        :param name: Name of the protection domain
        :param id: ID of the protection domain
        :return: Protection domain details if exists
        :rtype: dict
        """
        name_or_id = id if id else name
        try:
            if id:
                pd_details = self.powerflex_conn.protection_domain.get_by_id(id)
            else:
                pd_details = self.powerflex_conn.protection_domain.get_by_name(name)

            return pd_details
        except Exception as e:
            error_msg = "Failed to get the protection domain '%s' with " \
                        "error '%s'" % (name_or_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
    
    def delete_protection_domain(self, id):
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

    def create_protection_domain(self, protection_domain):
        """
        Create Protection Domain
        :param protection_domain: Dict of the protection domain
        :type protection_domain: dict
        :return: Dict representation of the created protection domain
        """
        # Creation of Protection domain
        try:
            LOG.info("Creating protection domain with name: %s ",
                     protection_domain['name'])
            return self.powerflex_conn.protection_domain.create(protection_domain)
        except Exception as e:
            error_msg = "Create protection domain '%s' operation failed" \
                        " with error '%s'" % (protection_domain['name'], str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update_protection_domain(self, protection_domain):
        """
        Modify Protection domain attributes
        :param protection_domain: Dictionary containing the attributes of
                            protection domain which are to be updated
        :type protection_domain: dict
        :param new_protection_domain: Dictionary containing the new attributes of
                            protection domain which are to be updated
        :type protection_domain: dict
        :return: Bool to indicate if protection domain is updated, 
                 Dict representation of the updated protection domain
        """
        try:
            LOG.info("Updating protection domain with id: %s ",
                     protection_domain['id'])
            return self.powerflex_conn.protection_domain.update(protection_domain)
        except Exception as e:
            err_msg = "Failed to update the protection domain {0}" \
                    " with error {1}".format(protection_domain['id'],str(e))
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def perform_module_operation(self):
        """
        Perform different actions on protection domain based on parameters
        passed in the playbook
        """
        protection_domain_name = self.module.params['name']
        protection_domain_id = self.module.params['id']
        is_active = self.module.params['is_active']
        rebuild_enabled = self.module.params['rebuild_enabled']
        rebalance_enabled = self.module.params['rebalance_enabled']
        overall_concurrent_io_limit = self.module.params['overall_concurrent_io_limit']
        bandwidth_limit_overall_ios = self.module.params['bandwidth_limit_overall_ios']
        bandwidth_limit_bg_dev_scanner = self.module.params['bandwidth_limit_bg_dev_scanner']
        bandwidth_limit_garbage_collector = self.module.params['bandwidth_limit_garbage_collector']
        bandwidth_limit_singly_impacted_rebuild = self.module.params['bandwidth_limit_singly_impacted_rebuild']
        bandwidth_limit_doubly_impacted_rebuild = self.module.params['bandwidth_limit_doubly_impacted_rebuild']
        bandwidth_limit_rebalance = self.module.params['bandwidth_limit_rebalance']
        bandwidth_limit_other = self.module.params['bandwidth_limit_other']
        bandwidth_limit_node_network = self.module.params['bandwidth_limit_node_network']
        state = self.module.params['state']

        # result is a dictionary to contain end state and protection domain
        # details
        changed = False
        result = dict(
            changed=False,
            protection_domain_details=None
        )

        # Checking invalid value for id, name and rename
        self.validate_input_params()

        # get Protection Domain details
        pd_details = self.get_protection_domain(protection_domain_name,
                                                protection_domain_id)

        if state == 'absent':
            if pd_details:
                self.delete_protection_domain(pd_details['id'])
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
        
        ## to create protection domain
        if not pd_details:
            result['protection_domain_details'] = self.create_protection_domain(protection_domain)
            result['changed'] = True
        else:
            # modify the protection domain
            protection_domain['id'] = pd_details['id']
            result['changed'], result['protection_domain_details'] = self.update_protection_domain(protection_domain)

        self.module.exit_json(**result)


def main():
    """ Create PowerFlex protection domain object and perform actions on it
        based on user input from playbook"""
    obj = PowerFlexProtectionDomain()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
