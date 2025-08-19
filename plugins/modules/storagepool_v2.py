#!/usr/bin/python

# Copyright: (c) 2021-25, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for managing storage pool on Dell Technologies (Dell) PowerFlex 5.x"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: storagepool_v2
version_added: '3.0.0'
short_description: Managing storage pool on Dell PowerFlex 5.x

description:
- Dell PowerFlex storage pool module includes getting the details of
  storage pool, creating a new storage pool, and modifying the attribute of
  a storage pool.

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

author:
- Luis Liu (@vangork) <ansible.team@dell.com>
- Yiming Bao (@baoy1) <ansible.team@dell.com>

options:
  storage_pool_name:
    description:
    - The name of the storage pool.
    - If more than one storage pool is found with the same name then
      protection domain id/name is required to perform the task.
    - Mutually exclusive with I(storage_pool_id).
    type: str
  storage_pool_id:
    description:
    - The id of the storage pool.
    - It is auto generated, hence should not be provided during
      creation of a storage pool.
    - Mutually exclusive with I(storage_pool_name).
    type: str
  storage_pool_new_name:
    description:
    - New name for the storage pool can be provided.
    - This parameter is used for renaming the storage pool.
    type: str
  protection_domain_name:
    description:
    - The name of the protection domain.
    - During creation of a pool, either protection domain name or id must be
      mentioned.
    - Mutually exclusive with I(protection_domain_id).
    type: str
  protection_domain_id:
    description:
    - The id of the protection domain.
    - During creation of a pool, either protection domain name or id must
      be mentioned.
    - Mutually exclusive with I(protection_domain_name).
    type: str
  device_group_id:
    description:
      - The ID of the device group.
    required: false
    type: str
  device_group_name:
    description:
      - The name of the device group.
    required: false
    type: str
  cap_alert_thresholds:
    description:
      - The capacity alert thresholds.
    required: false
    type: dict
    suboptions:
      high_threshold:
        description:
          - The high threshold.
        required: false
        type: int
      critical_threshold:
        description:
          - The critical threshold.
        required: false
        type: int
  compression_method:
    description:
      - The compression method.
    required: false
    type: str
    choices: ['None', 'Normal']
  over_provisioning_factor:
    description:
      - The over-provisioning factor.
    required: false
    type: int
  physical_size_gb:
    description:
      - The physical size in GB.
      - If 'use_all_available_capacity' is set to true, this parameter cannot be specified.
      - If 'use_all_available_capacity' is set to false, this parameter is required.
    required: false
    type: int
  use_all_available_capacity:
    description:
      - Whether to use all available capacity for storage pool.
      - When set to true, the 'physical_size_gb' parameter cannot be specified.
      - When set to false, the 'physical_size_gb' parameter is required.
    required: false
    type: bool
  protection_scheme:
    description:
      - The protection scheme.
    required: false
    type: str
    choices: ['TwoPlusTwo', 'EightPlusTwo']
  state:
    description:
      - The state of the storage pool. Can be 'present' or 'absent'.
    required: true
    choices: ['present', 'absent']
    type: str
notes:
  - This module is supported on Dell PowerFlex 5.x and later versions.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Get the details of storage pool by name
  dellemc.powerflex.storagepool_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_pool_name: "sample_pool_name"
    protection_domain_name: "sample_protection_domain"
    state: "present"

- name: Get the details of storage pool by id
  dellemc.powerflex.storagepool_v2:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    storage_pool_id: "abcd1234ab12r"
    state: "present"

- name: Create a new Storage pool
  dellemc.powerflex.storagepool_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    storage_pool_name: "{{ pool_name }}"
    protection_domain_name: "{{ protection_domain_name }}"
    device_group_name: "{{ device_group_name }}"
    cap_alert_thresholds:
      high_threshold: 80
      critical_threshold: 90
    compression_method: Normal
    over_provisioning_factor: 2
    physical_size_gb: 100
    protection_scheme: TwoPlusTwo
    state: "present"

- name: Modify a Storage pool by name
  dellemc.powerflex.storagepool_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    storage_pool_name: "{{ pool_name }}"
    protection_domain_name: "{{ protection_domain_name }}"
    storage_pool_new_name: "pool_name_new"
    cap_alert_thresholds:
      high_threshold: 85
      critical_threshold: 95
    compression_method: None
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: 'false'
storage_pool_details:
    description: Details of the storage pool.
    returned: When storage pool exists
    type: dict
    contains:
        id:
            description: ID of the storage pool.
            type: str
        name:
            description: Name of the storage pool.
            type: str
        protectionDomainId:
            description: ID of the protection domain in which the storage pool resides.
            type: str
        zeroPaddingEnabled:
            description: Indicates whether zero padding is enabled for the storage pool.
            type: bool
        capacityAlertHighThreshold:
            description: High threshold for capacity alert (percentage).
            type: int
        capacityAlertCriticalThreshold:
            description: Critical threshold for capacity alert (percentage).
            type: int
        capacityUsageState:
            description: Current capacity usage state of the storage pool.
            type: str
        capacityUsageType:
            description: Type of capacity usage being monitored.
            type: str
        addressSpaceUsage:
            description: Current address space usage state.
            type: str
        addressSpaceUsageType:
            description: Type of address space usage limit.
            type: str
        fragmentationEnabled:
            description: Indicates whether fragmentation is enabled for the storage pool.
            type: bool
        inflightRequestsFactor:
            description: In-flight requests factor for performance tuning.
            type: int
        inflightBandwidthFactor:
            description: In-flight bandwidth factor for performance tuning.
            type: int
        compressionMethod:
            description: Compression method used in the storage pool.
            type: str
        spClass:
            description: Class of the storage pool.
            type: str
        genType:
            description: Data protection generation type of the storage pool.
            type: str
        deviceGroupId:
            description: ID of the device group associated with the storage pool.
            type: str
        wrcDeviceGroupId:
            description: ID of the WRC device group.
            type: str
        rawSizeGb:
            description: Raw size of the storage pool in GB.
            type: int
        numDataSlices:
            description: Number of data slices used in erasure coding.
            type: int
        numProtectionSlices:
            description: Number of protection slices used in erasure coding.
            type: int
        physicalSizeGb:
            description: Physical size of the storage pool in GB.
            type: int
        overProvisioningFactor:
            description: Over-provisioning factor for the storage pool.
            type: int
        protectionScheme:
            description: Data protection scheme used in the storage pool.
            type: str
        spHealthState:
            description: Health state of the storage pool.
            type: str
        statistics:
            description: Statistics details of the storage pool.
            type: dict
            contains:
                "capacityInUseInKb":
                    description: Total capacity of the storage pool.
                    type: str
                "unusedCapacityInKb":
                    description: Unused capacity of the storage pool.
                    type: str
                "deviceIds":
                    description: Device Ids of the storage pool.
                    type: list
    sample: {
        "addressSpaceUsage": "Normal",
        "addressSpaceUsageType": "TypeHardLimit",
        "backgroundScannerBWLimitKBps": null,
        "backgroundScannerMode": null,
        "bgScannerCompareErrorAction": "Invalid",
        "bgScannerReadErrorAction": "Invalid",
        "capacityAlertCriticalThreshold": 90,
        "capacityAlertHighThreshold": 80,
        "capacityUsageState": "Normal",
        "capacityUsageType": "NetCapacity",
        "checksumEnabled": false,
        "compressionMethod": "Normal",
        "dataLayout": "ErasureCoding",
        "deviceGroupId": "39a898be00000000",
        "deviceGroupName": "DG1",
        "externalAccelerationType": "None",
        "fglAccpId": null,
        "fglExtraCapacity": null,
        "fglMaxCompressionRatio": null,
        "fglMetadataSizeXx100": null,
        "fglNvdimmMetadataAmortizationX100": null,
        "fglNvdimmWriteCacheSizeInMb": null,
        "fglOverProvisioningFactor": null,
        "fglPerfProfile": null,
        "fglWriteAtomicitySize": null,
        "fragmentationEnabled": false,
        "genType": "EC",
        "id": "5dabf3f800000000",
        "links": [
            {
                "href": "/api/instances/StoragePool::5dabf3f800000000",
                "rel": "self"
            },
            {
                "body": {
                    "ids": [
                        "5dabf3f800000000"
                    ],
                    "resource_type": "storage_pool"
                },
                "href": "/dtapi/rest/v1/metrics/query",
                "rel": "/dtapi/rest/v1/metrics/query"
            },
            {
                "href": "/api/instances/StoragePool::5dabf3f800000000/relationships/SpSds",
                "rel": "/api/StoragePool/relationship/SpSds"
            },
            {
                "href": "/api/instances/StoragePool::5dabf3f800000000/relationships/Volume",
                "rel": "/api/StoragePool/relationship/Volume"
            },
            {
                "href": "/api/instances/StoragePool::5dabf3f800000000/relationships/Device",
                "rel": "/api/StoragePool/relationship/Device"
            },
            {
                "href": "/api/instances/StoragePool::5dabf3f800000000/relationships/VTree",
                "rel": "/api/StoragePool/relationship/VTree"
            },
            {
                "href": "/api/instances/ProtectionDomain::f3d03dcf00000000",
                "rel": "/api/parent/relationship/protectionDomainId"
            },
            {
                "href": "/api/instances/DeviceGroup::39a898be00000000",
                "rel": "/api/parent/relationship/deviceGroupId"
            },
            {
                "href": "/api/instances/WrcDeviceGroup::39a898be00000000",
                "rel": "/api/parent/relationship/wrcDeviceGroupId"
            }
        ],
        "mediaType": null,
        "name": "SP_EC",
        "numOfParallelRebuildRebalanceJobsPerDevice": null,
        "overProvisioningFactor": 0,
        "persistentChecksumBuilderLimitKb": null,
        "persistentChecksumEnabled": false,
        "persistentChecksumState": "StateInvalid",
        "persistentChecksumValidateOnRead": null,
        "physicalSizeGB": 5120,
        "protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold": null,
        "protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps": null,
        "protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice": null,
        "protectedMaintenanceModeIoPriorityPolicy": null,
        "protectedMaintenanceModeIoPriorityQuietPeriodInMsec": null,
        "protectionDomainId": "f3d03dcf00000000",
        "protectionDomainName": "PD_EC",
        "protectionScheme": "TwoPlusTwo",
        "rawSizeGB": 10240,
        "rebalanceEnabled": null,
        "rebalanceIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "rebalanceIoPriorityAppIopsPerDeviceThreshold": null,
        "rebalanceIoPriorityBwLimitPerDeviceInKbps": null,
        "rebalanceIoPriorityNumOfConcurrentIosPerDevice": null,
        "rebalanceIoPriorityPolicy": null,
        "rebalanceIoPriorityQuietPeriodInMsec": null,
        "rebuildEnabled": null,
        "rebuildIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "rebuildIoPriorityAppIopsPerDeviceThreshold": null,
        "rebuildIoPriorityBwLimitPerDeviceInKbps": null,
        "rebuildIoPriorityNumOfConcurrentIosPerDevice": null,
        "rebuildIoPriorityPolicy": null,
        "rebuildIoPriorityQuietPeriodInMsec": null,
        "replicationCapacityMaxRatio": null,
        "rmcacheWriteHandlingMode": "Invalid",
        "spClass": "Default",
        "spHealthState": "Protected",
        "sparePercentage": null,
        "statistics": {
            "format": "ID_TIMESTAMP_METRIC",
            "resource_type": "storage_pool",
            "resources": [
                {
                    "id": "5dabf3f800000000",
                    "metrics": [
                        {
                            "name": "physical_free",
                            "values": [
                                5443871047680
                            ]
                        },
                        {
                            "name": "logical_provisioned",
                            "values": [
                                0
                            ]
                        },
                        {
                            "name": "raw_used",
                            "values": [
                                10995116277760
                            ]
                        },
                        {
                            "name": "logical_used",
                            "values": [
                                0
                            ]
                        },
                        {
                            "name": "physical_total",
                            "values": [
                                5497558138880
                            ]
                        },
                        {
                            "name": "physical_used",
                            "values": [
                                0
                            ]
                        },
                        {
                            "name": "over_provisioning_limit",
                            "values": [
                                4611686017353646080
                            ]
                        }
                    ]
                }
            ],
            "timestamps": [
                "2025-08-25T05:24:06Z"
            ]
        },
        "useRfcache": false,
        "useRmcache": false,
        "vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps": null,
        "vtreeMigrationIoPriorityAppIopsPerDeviceThreshold": null,
        "vtreeMigrationIoPriorityBwLimitPerDeviceInKbps": null,
        "vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice": null,
        "vtreeMigrationIoPriorityPolicy": null,
        "vtreeMigrationIoPriorityQuietPeriodInMsec": null,
        "wrcDeviceGroupId": "39a898be00000000",
        "zeroPaddingEnabled": true
    }
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils. \
    storage.dell.libraries.configuration import Configuration
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase, powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('storagepool_v2')


@powerflex_compatibility(min_ver='5.0', predecessor='storagepool')
class PowerFlexStoragePoolV2(PowerFlexBase):
    """Class with storage pool operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        argument_spec = dict(
            storage_pool_name=dict(required=False, type='str'),
            storage_pool_id=dict(required=False, type='str'),
            storage_pool_new_name=dict(required=False, type='str'),
            protection_domain_name=dict(required=False, type='str'),
            protection_domain_id=dict(type='str'),
            device_group_id=dict(type='str'),
            device_group_name=dict(type='str'),
            cap_alert_thresholds=dict(type='dict', options=dict(
                high_threshold=dict(type='int'),
                critical_threshold=dict(type='int'),
            )),
            compression_method=dict(type='str', choices=['None', 'Normal']),
            over_provisioning_factor=dict(type='int'),
            physical_size_gb=dict(type='int'),
            use_all_available_capacity=dict(type='bool'),
            protection_scheme=dict(type='str', choices=[
                'TwoPlusTwo', 'EightPlusTwo']),
            state=dict(required=True, type='str',
                       choices=['present', 'absent']),
        )

        mutually_exclusive = [['storage_pool_name', 'storage_pool_id'],
                              ['protection_domain_name', 'protection_domain_id'],
                              ['storage_pool_id', 'protection_domain_name'],
                              ['storage_pool_id', 'protection_domain_id']]
        required_one_of = [['storage_pool_name', 'storage_pool_id']]

        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive,
            'required_one_of': required_one_of
        }

        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get(self, storage_pool_id, storage_pool_name, protection_domain_id):
        """
        Get storage pool details
        :param storage_pool_id: Storage pool ID
        :type storage_pool_id: str
        :param storage_pool_name: Storage pool name
        :type storage_pool_name: str
        :param protection_domain_id: Protection domain ID
        :type protection_domain_id: str
        :return: Storage pool details
        """
        name_or_id = storage_pool_id if storage_pool_id else storage_pool_name
        try:
            if storage_pool_id:
                sp_details = self.powerflex_conn.storage_pool.get_by_id(
                    storage_pool_id)
            else:
                sp_details = self.powerflex_conn.storage_pool.get_by_name(
                    protection_domain_id, storage_pool_name)
            return sp_details
        except Exception as e:
            error_msg = f"Failed to get the storage pool {name_or_id} with error {str(e)}"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def delete(self, storage_pool):
        """
        Delete storage pool
        :param storage_pool: Storage pool
        :type storage_pool: dict
        :rtype: None
        """
        try:
            storage_pool_id = storage_pool["id"]
            self.powerflex_conn.storage_pool.delete(storage_pool_id)
            LOG.info("Storage pool deleted successfully.")
        except Exception as e:
            error_msg = f"Delete storage pool {storage_pool['name']} operation failed " \
                        f"with error {str(e)}"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def create(self, storage_pool):
        """
        Create storage pool
        :param storage_pool: Dict of the storage pool
        :type storage_pool: dict
        :return: Dict representation of the created storage pool
        """
        try:
            LOG.info("Creating storage pool with name: %s ",
                     storage_pool['name'])

            if storage_pool.get("useAllAvailableCapacity") and \
                    storage_pool.get("physicalSizeGB") is not None:
                self.module.fail_json(
                    msg="When creating or updating storage pool, physical_size_gb must not be specified"
                        " if use_all_available_capacity is true.")
            if not storage_pool.get("useAllAvailableCapacity") and \
                    storage_pool.get("physicalSizeGB") is None:
                self.module.fail_json(
                    msg="When creating or updating storage pool, physical_size_gb must be specified"
                        " unless use_all_available_capacity is true.")

            self.powerflex_conn.storage_pool.check_create_params(storage_pool)
            if self.module.check_mode:
                return storage_pool
            return self.powerflex_conn.storage_pool.create(storage_pool)
        except Exception as e:
            error_msg = f"Create storage pool '{storage_pool['name']}' operation failed" \
                        f" with error '{str(e)}'"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def update(self, storage_pool, current_storage_pool):
        """
        Modify storage pool attributes
        :param current_storage_pool: Dictionary containing the attributes of
                            storage pool which are to be updated
        :type storage_pool: dict
        :return: Bool to indicate if storage pool is updated,
                 Dict representation of the updated storage pool
        """
        try:
            LOG.info("Updating storage pool with id: %s ",
                     storage_pool['id'])

            if storage_pool.get("use_all_available_capacity") and storage_pool.get("physical_size_gb") is not None:
                self.module.fail_json(
                    msg="When creating or updating storage pool, physical_size_gb must not be specified"
                        " if use_all_available_capacity is true.")

            self.powerflex_conn.storage_pool.check_update_params(storage_pool, current_storage_pool)
            if self.module.check_mode:
                storage_pool["name"] = storage_pool.get("storage_pool_new_name", storage_pool["name"])
                storage_pool.pop("storage_pool_new_name", None)
                need_update, changes = self.powerflex_conn.storage_pool.need_update(storage_pool, current_storage_pool)
                if storage_pool.get("useAllAvailableCapacity"):
                    changes["physicalSizeGB"] = "Computed after update"
                    need_update = True
                return need_update, current_storage_pool | changes
            return self.powerflex_conn.storage_pool.update(storage_pool, current_storage_pool)
        except Exception as e:
            err_msg = f"Failed to update the storage pool {storage_pool['id']}" \
                      f" with error {str(e)}"
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)

    def verify_device_group(self, sp_details):
        """
        Verify device group details with the storage pool details
        """
        if not sp_details:
            return

        dg_name = self.module.params['device_group_name']
        dg_id = self.module.params['device_group_id']
        if dg_id and dg_id != sp_details['deviceGroupId']:
            self.module.fail_json(msg="Entered device group id does not"
                                      " match with the storage pool's"
                                      " device group id. Please enter"
                                      " a correct device group id.")
        dg = self.get_device_group(device_group_name=None,
                                   device_group_id=sp_details['deviceGroupId'])
        if dg_name and dg_name != dg['name']:
            self.module.fail_json(msg="Entered device group name does"
                                      " not match with the storage pool's"
                                      " device group name. Please enter"
                                      " a correct device group name.")
        pass

    def verify_protection_domain(self, sp_details):
        """
        Verify protection domain details with the storage pool details
        """
        if not sp_details:
            return

        pd_name = self.module.params['protection_domain_name']
        pd_id = self.module.params['protection_domain_id']
        if pd_id and pd_id != sp_details['protectionDomainId']:
            self.module.fail_json(msg="Entered protection domain id does not"
                                      " match with the storage pool's"
                                      " protection domain id. Please enter"
                                      " a correct protection domain id.")
        pd = self.get_protection_domain(protection_domain_name=None,
                                        protection_domain_id=sp_details['protectionDomainId'])
        if pd_name and pd_name != pd['name']:
            self.module.fail_json(msg="Entered protection domain name does"
                                      " not match with the storage pool's"
                                      " protection domain name. Please enter"
                                      " a correct protection domain name.")

    def perform_module_operation(self):
        """
        Perform different actions on protection domain based on parameters
        passed in the playbook
        """
        storage_pool_id = self.module.params['storage_pool_id']
        storage_pool_name = self.module.params['storage_pool_name']
        storage_pool_new_name = self.module.params['storage_pool_new_name']
        protection_domain_id = self.module.params['protection_domain_id']
        protection_domain_name = self.module.params['protection_domain_name']
        device_group_id = self.module.params['device_group_id']
        device_group_name = self.module.params['device_group_name']
        cap_alert_thresholds = self.module.params['cap_alert_thresholds']
        cap_alert_high_threshold = None if cap_alert_thresholds is None else cap_alert_thresholds[
            'high_threshold']
        cap_alert_critical_threshold = None if cap_alert_thresholds is None else cap_alert_thresholds[
            'critical_threshold']
        over_provisioning_factor = self.module.params['over_provisioning_factor']
        physical_size_gb = self.module.params['physical_size_gb']
        use_all_available_capacity = self.module.params['use_all_available_capacity']
        protection_scheme = self.module.params['protection_scheme']
        compression_method = self.module.params['compression_method']
        state = self.module.params['state']

        result = dict(
            changed=False,
            storage_pool_details=None
        )

        if storage_pool_name and not (protection_domain_id or protection_domain_name):
            self.module.fail_json(
                msg="Either protection_domain_id or protection_domain_name"
                    " must be provided when storage_pool_name is specified."
            )

        if not protection_domain_id and protection_domain_name:
            pd = self.get_protection_domain(protection_domain_name,
                                            protection_domain_id)
            protection_domain_id = pd['id']

        if not device_group_id and device_group_name:
            device_group = self.get_device_group(device_group_name=device_group_name)
            device_group_id = device_group['id']

        sp_details = self.get(
            storage_pool_id,
            storage_pool_name,
            protection_domain_id
        )

        if state == 'absent':
            if sp_details:
                result['changed'] = True
                result["diff"] = dict(before=sp_details, after={})
                if not self.module.check_mode:
                    self.delete(sp_details)
            self.module.exit_json(**result)

        storage_pool = {
            'name': storage_pool_name,
            'storage_pool_new_name': storage_pool_new_name,
            'protectionDomainId': protection_domain_id,
            'deviceGroupId': device_group_id,
            'capacityAlertHighThreshold': cap_alert_high_threshold,
            'capacityAlertCriticalThreshold': cap_alert_critical_threshold,
            'overProvisioningFactor': over_provisioning_factor,
            'physicalSizeGB': physical_size_gb,
            'useAllAvailableCapacity': use_all_available_capacity,
            'protectionScheme': protection_scheme,
            'compressionMethod': compression_method,
        }
        storage_pool = {k: v for k, v in storage_pool.items() if v is not None}

        self.verify_protection_domain(sp_details)
        self.verify_device_group(sp_details)

        if not sp_details:
            sp = self.create(storage_pool)
            changed = True
        else:
            storage_pool['id'] = sp_details['id']
            changed, sp = self.update(storage_pool, sp_details)

        result["diff"] = dict(before=sp_details if sp_details else {}, after=copy.deepcopy(sp))
        self.post_process(sp)
        result['storage_pool_details'] = sp
        result['changed'] = changed

        self.module.exit_json(**result)

    def get_device_group(self, device_group_name=None, device_group_id=None):
        """Get the details of a device group in a given PowerFlex storage
        system"""

        name_or_id = (
            device_group_id if device_group_id else device_group_name
        )

        try:
            if device_group_id:
                device_groups = self.powerflex_conn.device_group.get(
                    filter_fields={"id": device_group_id}
                )

            else:
                device_groups = self.powerflex_conn.device_group.get(
                    filter_fields={"name": device_group_name}
                )

            if len(device_groups) == 0:
                error_msg = f"Unable to find device group with '{name_or_id}'."
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            return device_groups[0]

        except Exception as e:
            error_msg = f"Failed to get device group '{name_or_id}' with error '{str(e)}'"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_protection_domain(self, protection_domain_name=None, protection_domain_id=None):
        """Get the details of a protection domain in a given PowerFlex storage
        system"""
        return Configuration(self.powerflex_conn, self.module).get_protection_domain(
            protection_domain_name=protection_domain_name, protection_domain_id=protection_domain_id)

    def query_metrics(self, storage_pool_id):
        try:
            metrics = ['raw_used', 'physical_used', 'physical_free', 'physical_total',
                       'logical_provisioned', 'over_provisioning_limit', 'logical_used']
            statistics = self.powerflex_conn.utility.query_metrics('storage_pool', [storage_pool_id], metrics)
            return statistics
        except Exception as e:
            error_msg = f"Failed to query statistics with error {str(e)}"
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def post_process(self, sp_details):
        """Post-processing function to add more details to the result"""
        if self.module.check_mode:
            return
        pd = self.get_protection_domain(protection_domain_name=None,
                                        protection_domain_id=sp_details['protectionDomainId'])
        sp_details['protectionDomainName'] = pd['name']
        dg = self.get_device_group(device_group_name=None, device_group_id=sp_details['deviceGroupId'])
        sp_details['deviceGroupName'] = dg['name']

        statistics = self.query_metrics(sp_details['id'])
        sp_details['statistics'] = statistics if statistics else {}


def main():
    """ Create PowerFlex storage pool object and perform action on it
        based on user input from playbook"""
    # import pydevd_pycharm
    # pydevd_pycharm.settrace('localhost', port=65429)
    obj = PowerFlexStoragePoolV2()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
