#!/usr/bin/python
# Copyright: (c) 2021, Dell EMC
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Ansible module for Gathering information about Dell EMC PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: dellemc_powerflex_gatherfacts

version_added: '1.0.0'

short_description: Gathering information about Dell EMC PowerFlex

description:
- Gathering information about Dell EMC PowerFlex storage system includes
  get the api details of a PowerFlex array,
  get list of volumes in PowerFlex array,
  get list of SDSs in a PowerFlex array,
  get list of SDCs in a PowerFlex array,
  get list of storage pools in PowerFlex array,
  get list of protection domains in a PowerFlex array,
  get list of snapshot policies in a PowerFlex array, and
  get list of devices in a PowerFlex array.

extends_documentation_fragment:
  - dellemc.powerflex.dellemc_powerflex.powerflex

author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>

options:
  gather_subset:
    description:
    - List of string variables to specify the Powerflex storage system
      entities for which information is required.
    - Volumes - vol.
    - Storage pools - storage_pool.
    - Protection domains - protection_domain.
    - SDCs - sdc.
    - SDSs - sds.
    - Snapshot policies - snapshot_policy.
    - Devices - device.
    choices: [vol, storage_pool, protection_domain, sdc, sds,
             snapshot_policy, device]
    type: list
    elements: str
  filters:
    description:
    - List of filters to support filtered output for storage entities.
    - Each filter is a list of filter_key, filter_operator, filter_value.
    - Supports passing of multiple filters.
    type: list
    elements: dict
    suboptions:
      filter_key:
        description:
        - Name identifier of the filter.
        type: str
        required: True
      filter_operator:
        description:
        - Operation to be performed on filter key.
        type: str
        choices: [equal]
        required: True
      filter_value:
        description:
        - Value of the filter key.
        type: str
        required: True
notes:
  - The check_mode is not supported.
'''

EXAMPLES = r'''
 - name: Get detailed list of PowerFlex entities
   dellemc.powerflex.dellemc_powerflex_gatherfacts:
     gateway_host: "{{gateway_host}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - vol
       - storage_pool
       - protection_domain
       - sdc
       - sds
       - snapshot_policy
       - device

 - name: Get a subset list of PowerFlex volumes
   dellemc.powerflex.dellemc_powerflex_gatherfacts:
     gateway_host: "{{gateway_host}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - vol
     filters:
       - filter_key: "name"
         filter_operator: "equal"
         filter_value: "ansible_test"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
Array_Details:
    description: System entities of PowerFlex storage array.
    returned: always
    type: dict
    contains:
        addressSpaceUsage:
            description: Address space usage.
            type: str
        authenticationMethod:
            description: Authentication method.
            type: str
        capacityAlertCriticalThresholdPercent:
            description: Capacity alert critical threshold percentage.
            type: int
        capacityAlertHighThresholdPercent:
            description: Capacity alert high threshold percentage.
            type: int
        capacityTimeLeftInDays:
            description: Capacity time left in days.
            type: str
        cliPasswordAllowed:
            description: CLI password allowed.
            type: bool
        daysInstalled:
            description: Days installed.
            type: int
        defragmentationEnabled:
            description: Defragmentation enabled.
            type: bool
        enterpriseFeaturesEnabled:
            description: Enterprise eatures enabled.
            type: bool
        id:
            description: The ID of the system.
            type: str
        installId:
            description: installation Id.
            type: str
        isInitialLicense:
            description: Initial license.
            type: bool
        lastUpgradeTime:
            description: Last upgrade time.
            type: int
        managementClientSecureCommunicationEnabled:
            description: Management client secure communication enabled.
            type: bool
        maxCapacityInGb:
            description: Maximum capacity in GB.
            type: dict
        mdmCluster:
            description: MDM cluster details.
            type: dict
        mdmExternalPort:
            description: MDM external port.
            type: int
        mdmManagementPort:
            description: MDM management port.
            type: int
        mdmSecurityPolicy:
            description: MDM security policy.
            type: str
        showGuid:
            description: Show guid.
            type: bool
        swid:
            description: SWID.
            type: str
        systemVersionName:
            description: System version and name.
            type: str
        tlsVersion:
            description: TLS version.
            type: str
        upgradeState:
            description: Upgrade state.
            type: str
    sample: {
        "addressSpaceUsage": "Normal",
        "authenticationMethod": "Native",
        "capacityAlertCriticalThresholdPercent": 90,
        "capacityAlertHighThresholdPercent": 80,
        "capacityTimeLeftInDays": "24",
        "cliPasswordAllowed": true,
        "daysInstalled": 66,
        "defragmentationEnabled": true,
        "enterpriseFeaturesEnabled": true,
        "id": "4a54a8ba6df0690f",
        "installId": "38622771228e56db",
        "isInitialLicense": true,
        "lastUpgradeTime": 0,
        "managementClientSecureCommunicationEnabled": true,
        "maxCapacityInGb": "Unlimited",
        "mdmCluster": {
            "clusterMode": "ThreeNodes",
            "clusterState": "ClusteredNormal",
            "goodNodesNum": 3,
            "goodReplicasNum": 2,
            "id": "5356091375512217871",
            "master": {
                "id": "6101582c2ca8db00",
                "ips": [
                    "10.47.xxx.xxx"
                ],
                "managementIPs": [
                    "10.47.xxx.xxx"
                ],
                "name": "node0",
                "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017",
                "port": 9011,
                "role": "Manager",
                "status": "Normal",
                "versionInfo": "R3_6.0.0",
                "virtualInterfaces": [
                    "ens160"
                ]
            },
            "slaves": [
                {
                    "id": "23fb724015661901",
                    "ips": [
                        "10.47.xxx.xxx"
                    ],
                    "managementIPs": [
                        "10.47.xxx.xxx"
                    ],
                    "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017",
                    "port": 9011,
                    "role": "Manager",
                    "status": "Normal",
                    "versionInfo": "R3_6.0.0",
                    "virtualInterfaces": [
                        "ens160"
                    ]
                }
            ],
            "tieBreakers": [
                {
                    "id": "6ef27eb20d0c1202",
                    "ips": [
                        "10.47.xxx.xxx"
                    ],
                    "managementIPs": [
                        "10.47.xxx.xxx"
                    ],
                    "opensslVersion": "N/A",
                    "port": 9011,
                    "role": "TieBreaker",
                    "status": "Normal",
                    "versionInfo": "R3_6.0.0"
                }
            ]
        },
        "mdmExternalPort": 7611,
        "mdmManagementPort": 6611,
        "mdmSecurityPolicy": "None",
        "showGuid": true,
        "swid": "",
        "systemVersionName": "DellEMC PowerFlex Version: R3_6.0.354",
        "tlsVersion": "TLSv1.2",
        "upgradeState": "NoUpgrade"
    }
API_Version:
    description: API version of PowerFlex API Gateway.
    returned: always
    type: str
    sample: "3.5"
Protection_Domains:
    description: Details of all protection domains.
    returned: always
    type: list
    contains:
        id:
            description: protection domain id.
            type: str
        name:
            description: protection domain name.
            type: str
    sample: [
        {
            "id": "9300e90900000001",
            "name": "domain2"
        },
        {
            "id": "9300c1f900000000",
            "name": "domain1"
        }
    ]
SDCs:
    description: Details of storage data clients.
    returned: always
    type: list
    contains:
        id:
            description: storage data client id.
            type: str
        name:
            description: storage data client name.
            type: str
    sample: [
        {
            "id": "07335d3d00000006",
            "name": "LGLAP203"
        },
        {
            "id": "07335d3c00000005",
            "name": "LGLAP178"
        },
        {
            "id": "0733844a00000003"
        }
    ]
SDSs:
    description: Details of storage data servers.
    returned: always
    type: list
    contains:
        id:
            description: storage data server id.
            type: str
        name:
            description: storage data server name.
            type: str
    sample: [
        {
            "id": "8f3bb0cc00000002",
            "name": "node0"
        },
        {
            "id": "8f3bb0ce00000000",
            "name": "node1"
        },
        {
            "id": "8f3bb15300000001",
            "name": "node22"
        }
    ]
Snapshot_Policies:
    description: Details of snapshot policies.
    returned: always
    type: list
    contains:
        id:
            description: snapshot policy id.
            type: str
        name:
            description: snapshot policy name.
            type: str
    sample: [
        {
            "id": "2b380c5c00000000",
            "name": "sample_snap_policy"
        },
        {
            "id": "2b380c5d00000001",
            "name": "sample_snap_policy_1"
        }
    ]
Storage_Pools:
    description: Details of storage pools.
    returned: always
    type: list
    contains:
        id:
            description: storage pool id.
            type: str
        name:
            description: storage pool name.
            type: str
    sample: [
        {
            "id": "e0d8f6c900000000",
            "name": "pool1"
        },
        {
            "id": "e0d96c1f00000002",
            "name": "pool1"
        }
    ]
Volumes:
    description: Details of volumes.
    returned: always
    type: list
    contains:
        id:
            description: volume id.
            type: str
        name:
            description: volume name.
            type: str
    sample: [
        {
            "id": "cdd883cf00000002",
            "name": "ansible-volume-1"
        }
    ]
Devices:
    description: Details of devices.
    returned: always
    type: list
    contains:
        id:
            description: device id.
            type: str
        name:
            description: device name.
            type: str
    sample:  [
        {
            "id": "b6efa59900000000",
            "name": "device230"
        },
        {
            "id": "b6efa5fa00020000",
            "name": "device_node0"
        },
        {
            "id": "b7f3a60900010000",
            "name": "device22"
        }
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import dellemc_ansible_powerflex_utils as utils

LOG = utils.get_logger('dellemc_powerflex_gatherfacts')

MISSING_PACKAGES_CHECK = utils.pypowerflex_version_check()


class PowerFlexGatherfacts(object):
    """Class with Gatherfacts operations"""

    filter_mapping = {'equal': 'eq.'}

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_powerflex_gateway_host_parameters()
        self.module_params.update(get_powerflex_gatherfacts_parameters())

        self.filter_keys = sorted(
            [k for k in self.module_params['filters']['options'].keys()
             if 'filter' in k])

        """ initialize the ansible module """
        self.module = AnsibleModule(argument_spec=self.module_params,
                                    supports_check_mode=False)

        if MISSING_PACKAGES_CHECK and \
                not MISSING_PACKAGES_CHECK['dependency_present']:
            err_msg = MISSING_PACKAGES_CHECK['error_message']
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

        try:
            self.powerflex_conn = utils.get_powerflex_gateway_host_connection(
                self.module.params)
            LOG.info('Got the PowerFlex system connection object instance')
        except Exception as e:
            LOG.error(str(e))
            self.module.fail_json(msg=str(e))

    def get_api_details(self):
        """ Get api details of the array """
        try:
            LOG.info('Getting API details ')
            api_version = self.powerflex_conn.system.api_version()
            return api_version

        except Exception as e:
            msg = 'Get API details from Powerflex array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_array_details(self):
        """ Get system details of a powerflex array """

        try:
            LOG.info('Getting array details ')
            entity_list = ['addressSpaceUsage', 'authenticationMethod',
                           'capacityAlertCriticalThresholdPercent',
                           'capacityAlertHighThresholdPercent',
                           'capacityTimeLeftInDays', 'cliPasswordAllowed',
                           'daysInstalled', 'defragmentationEnabled',
                           'enterpriseFeaturesEnabled', 'id', 'installId',
                           'isInitialLicense', 'lastUpgradeTime',
                           'managementClientSecureCommunicationEnabled',
                           'maxCapacityInGb', 'mdmCluster',
                           'mdmExternalPort', 'mdmManagementPort',
                           'mdmSecurityPolicy', 'showGuid', 'swid',
                           'systemVersionName', 'tlsVersion', 'upgradeState']

            sys_list = self.powerflex_conn.system.get()
            sys_details_list = []
            for sys in sys_list:
                sys_details = {}
                for entity in entity_list:
                    if entity in sys.keys():
                        sys_details.update({entity: sys[entity]})
                if sys_details:
                    sys_details_list.append(sys_details)

            return sys_details_list

        except Exception as e:
            msg = 'Get array details from Powerflex array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_sdc_list(self, filter_dict=None):
        """ Get the list of sdcs on a given PowerFlex storage system """

        try:
            LOG.info('Getting SDC list ')
            if filter_dict:
                sdc = self.powerflex_conn.sdc.get(filter_fields=filter_dict)
            else:
                sdc = self.powerflex_conn.sdc.get()
            return result_list(sdc)

        except Exception as e:
            msg = 'Get SDC list from powerflex array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_sds_list(self, filter_dict=None):
        """ Get the list of sdses on a given PowerFlex storage system """

        try:
            LOG.info('Getting SDS list ')
            if filter_dict:
                sds = self.powerflex_conn.sds.get(filter_fields=filter_dict)
            else:
                sds = self.powerflex_conn.sds.get()
            return result_list(sds)

        except Exception as e:
            msg = 'Get sds list from powerflex array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_pd_list(self, filter_dict=None):
        """ Get the list of Protection Domains on a given PowerFlex
            storage system """

        try:
            LOG.info('Getting protection domain list ')

            if filter_dict:
                pd = self.powerflex_conn.protection_domain.get(filter_fields=filter_dict)
            else:
                pd = self.powerflex_conn.protection_domain.get()
            return result_list(pd)

        except Exception as e:
            msg = 'Get protection domain list from powerflex array failed ' \
                  'with error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_storage_pool_list(self, filter_dict=None):
        """ Get the list of storage pools on a given PowerFlex storage
            system """

        try:
            LOG.info('Getting storage pool list ')
            if filter_dict:
                pool = self.powerflex_conn.storage_pool.get(filter_fields=filter_dict)
            else:
                pool = self.powerflex_conn.storage_pool.get()
            return result_list(pool)

        except Exception as e:
            msg = 'Get storage pool list from powerflex array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_volumes_list(self, filter_dict=None):
        """ Get the list of volumes on a given PowerFlex storage
            system """

        try:
            LOG.info('Getting volumes list ')
            if filter_dict:
                volumes = self.powerflex_conn.volume.get(filter_fields=filter_dict)
            else:
                volumes = self.powerflex_conn.volume.get()
            return result_list(volumes)

        except Exception as e:
            msg = 'Get volumes list from powerflex array failed with' \
                  ' error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_snapshot_policy_list(self, filter_dict=None):
        """ Get the list of snapshot schedules on a given PowerFlex storage
            system """

        try:
            LOG.info('Getting snapshot schedules list ')
            if filter_dict:
                snapshot_schedules = \
                    self.powerflex_conn.snapshot_policy.get(
                        filter_fields=filter_dict)
            else:
                snapshot_schedules = \
                    self.powerflex_conn.snapshot_policy.get()

            return result_list(snapshot_schedules)

        except Exception as e:
            msg = 'Get snapshot schedules list from powerflex array failed ' \
                  'with error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_devices_list(self, filter_dict=None):
        """ Get the list of devices on a given PowerFlex storage
            system """

        try:
            LOG.info('Getting device list ')
            if filter_dict:
                devices = self.powerflex_conn.device.get(filter_fields=filter_dict)
            else:
                devices = self.powerflex_conn.device.get()

            return result_list(devices)

        except Exception as e:
            msg = 'Get device list from powerflex array failed ' \
                  'with error %s' % (str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def validate_filter(self, filter_dict):
        """ Validate given filter_dict """

        is_invalid_filter = self.filter_keys != sorted(list(filter_dict))
        if is_invalid_filter:
            msg = "Filter should have all keys: '{0}'".format(
                ", ".join(self.filter_keys))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        is_invalid_filter = any([filter_dict[i] is None for i in filter_dict])
        if is_invalid_filter:
            msg = "Filter keys: '{0}' cannot be None".format(self.filter_keys)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_filters(self, filters):
        """Get the filters to be applied"""

        filter_dict = {}
        for item in filters:
            self.validate_filter(item)
            f_op = item['filter_operator']
            if self.filter_mapping.get(f_op):
                f_key = item['filter_key']
                f_val = item['filter_value']
                if f_key in filter_dict:
                    # multiple filters on same key
                    if isinstance(filter_dict[f_key], list):
                        # prev_val is list, so append new f_val
                        filter_dict[f_key].append(f_val)
                    else:
                        # prev_val is not list,
                        # so create list with prev_val & f_val
                        filter_dict[f_key] = [filter_dict[f_key], f_val]
                else:
                    filter_dict[f_key] = f_val
            else:
                msg = "Given filter operator '{0}' is not supported." \
                    "supported operators are : '{1}'".format(
                        f_op,
                        list(self.filter_mapping.keys()))
                LOG.error(msg)
                self.module.fail_json(msg=msg)
        return filter_dict

    def perform_module_operation(self):
        """ Perform different actions on Gatherfacts based on user input
            in the playbook """

        filters = self.module.params['filters']
        filter_dict = {}
        if filters:
            filter_dict = self.get_filters(filters)
            LOG.info('filters: %s', filter_dict)

        api_version = self.get_api_details()
        array_details = self.get_array_details()
        sdc = []
        sds = []
        storage_pool = []
        vol = []
        snapshot_policy = []
        protection_domain = []
        device = []

        subset = self.module.params['gather_subset']
        if subset is not None:
            if 'sdc' in subset:
                sdc = self.get_sdc_list(filter_dict=filter_dict)
            if 'sds' in subset:
                sds = self.get_sds_list(filter_dict=filter_dict)
            if 'protection_domain' in subset:
                protection_domain = self.get_pd_list(filter_dict=filter_dict)
            if 'storage_pool' in subset:
                storage_pool = self.get_storage_pool_list(filter_dict=filter_dict)
            if 'vol' in subset:
                vol = self.get_volumes_list(filter_dict=filter_dict)
            if 'snapshot_policy' in subset:
                snapshot_policy = self.get_snapshot_policy_list(filter_dict=filter_dict)
            if 'device' in subset:
                device = self.get_devices_list(filter_dict=filter_dict)

        self.module.exit_json(
            Array_Details=array_details,
            API_Version=api_version,
            SDCs=sdc,
            SDSs=sds,
            Storage_Pools=storage_pool,
            Volumes=vol,
            Snapshot_Policies=snapshot_policy,
            Protection_Domains=protection_domain,
            Devices=device
        )


def result_list(entity):
    """ Get the name and id associated with the PowerFlex entities """
    result = []
    if entity:
        LOG.info('Successfully listed.')
        for item in entity:
            if item['name']:
                result.append(
                    {
                        "name": item['name'],
                        "id": item['id']
                    }
                )
            else:
                result.append({"id": item['id']})
        return result
    else:
        return None


def get_powerflex_gatherfacts_parameters():
    """This method provides parameters required for the ansible
    gatherfacts module on powerflex"""
    return dict(
        gather_subset=dict(type='list', required=False, elements='str',
                           choices=['vol', 'storage_pool',
                                    'protection_domain', 'sdc', 'sds',
                                    'snapshot_policy', 'device']),
        filters=dict(type='list', required=False, elements='dict',
                     options=dict(filter_key=dict(type='str', required=True),
                                  filter_operator=dict(
                                      type='str', required=True,
                                      choices=['equal']),
                                  filter_value=dict(type='str', required=True)
                                  )))


def main():
    """ Create PowerFlex Gatherfacts object and perform action on it
        based on user input from playbook"""
    obj = PowerFlexGatherfacts()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
