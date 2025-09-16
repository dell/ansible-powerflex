# !/usr/bin/python

# Copyright: (c) 2025, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for Gathering information about Dell Technologies (Dell) PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: info_v2

version_added: '3.0.0'

short_description: Gathering information about Dell PowerFlex

description:
- Gathering information about Dell PowerFlex storage system includes
  getting the api details, list of devices, NVMe host,
  protection domains, SDCs, SDT, snapshot policies, storage pools, volumes.
- Gathering information about Dell PowerFlex Manager includes getting the
  list of deployments, firmware repository, managed devices, service templates.
- Support only for Powerflex 5.0 versions and above.

author:
- Tao He (@taohe1012) <ansible.team@dell.com>

extends_documentation_fragment:
  - dellemc.powerflex.powerflex_v2

options:
  gather_subset:
    description:
    - List of string variables to specify the PowerFlex storage system
      entities for which information is required.
    - Devices - C(device).
    - Deployments - C(deployment).
    - FirmwareRepository - C(firmware_repository).
    - Managed devices - C(managed_device).
    - NVMe host - C(nvme_host)
    - NVMe Storage Data Target - C(sdt).
    - Protection domains - C(protection_domain).
    - SDCs - C(sdc).
    - Service templates - C(service_template).
    - Snapshot policies - C(snapshot_policy).
    - Storage pools - C(storage_pool).
    - Volumes - C(vol).
    choices: [deployment, device, firmware_repository, managed_device,
             nvme_host, protection_domain, sdc, sdt, service_template,
             snapshot_policy, storage_pool, vol]
    type: list
    elements: str
  filters:
    description:
    - List of filters to support filtered output for storage entities.
    - Each filter is a dictionary with keys I(filter_key), I(filter_operator), I(filter_value).
    - Supports passing of multiple filters.
    type: list
    elements: dict
    suboptions:
      filter_key:
        description:
        - Name identifier of the filter.
        type: str
        required: true
      filter_operator:
        description:
        - Operation to be performed on filter key.
        - Choice C(contains) is supported for I(gather_subset) keys C(service_template), C(managed_device),
          C(deployment), C(firmware_repository).
        type: str
        choices: [equal, contains]
        required: true
      filter_value:
        description:
        - Value of the filter key.
        type: str
        required: true
  limit:
    description:
    - Page limit.
    - Supported for I(gather_subset) keys C(service_template), C(managed_device), C(deployment), C(firmware_repository).
    type: int
    default: 50
  offset:
    description:
    - Pagination offset.
    - Supported for I(gather_subset) keys C(service_template), C(managed_device), C(deployment), C(firmware_repository).
    type: int
    default: 0
  sort:
    description:
    - Sort the returned components based on specified field.
    - Supported for I(gather_subset) keys C(service_template), C(managed_device), C(deployment), C(firmware_repository).
    - The supported sort keys for the I(gather_subset) can be referred from PowerFlex Manager API documentation in U(https://developer.dell.com).
    type: str
  include_devices:
    description:
    - Include devices in response.
    - Applicable when I(gather_subset) is C(deployment).
    type: bool
    default: true
  include_template:
    description:
    - Include service templates in response.
    - Applicable when I(gather_subset) is C(deployment).
    type: bool
    default: true
  full:
    description:
    - Specify if response is full or brief.
    - Applicable when I(gather_subset) is C(deployment), C(service_template).
    - For C(deployment) specify to use full templates including resources in response.
    type: bool
    default: false
  include_attachments:
    description:
    - Include attachments.
    - Applicable when I(gather_subset) is C(service_template).
    type: bool
    default: true
  include_bundles:
    description:
    - Include software bundle entities.
    - Applicable when I(gather_subset) is C(firmware_repository).
    type: bool
    default: false
notes:
  - The supported filter keys for the I(gather_subset) can be referred from PowerFlex Manager API documentation in U(https://developer.dell.com).
  - The I(filter), I(sort), I(limit) and I(offset) options will be ignored when more than one I(gather_subset) is specified along with
    C(deployment), C(firmware_repository), C(managed_device) or C(service_template).
'''

EXAMPLES = r'''
- name: Get detailed list of PowerFlex entities
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - vol
      - storage_pool
      - protection_domain
      - sdc
      - snapshot_policy
      - device
      - nvme_host
      - sdt

- name: Get specific volume details
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - vol
    filters:
      - filter_key: "name"
        filter_operator: "equal"
        filter_value: "ansible_test"

- name: Get specific NVMe hosts details
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - nvme_host
    filters:
      - filter_key: "name"
        filter_operator: "equal"
        filter_value: "ansible_test"

- name: Get deployment and resource provisioning info
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - managed_device
      - deployment
      - service_template

- name: Get deployment with filter, sort, pagination
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - deployment
    filters:
      - filter_key: "name"
        filter_operator: "contains"
        filter_value: "partial"
    sort: name
    limit: 10
    offset: 10
    include_devices: true
    include_template: true

- name: Get the list of firmware repository.
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - firmware_repository

- name: Get the list of firmware repository
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - firmware_repository
    include_bundles: true

- name: Get the list of firmware repository with filter
  dellemc.powerflex.info_v2:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    validate_certs: "{{ validate_certs }}"
    gather_subset:
      - firmware_repository
    filters:
      - filter_key: "createdBy"
        filter_operator: "equal"
        filter_value: "admin"
    sort: createdDate
    limit: 10
    include_bundles: true
  register: result_repository_out

- name: Get the list of available firmware repository
  ansible.builtin.debug:
    msg: "{{ result_repository_out.FirmwareRepository | selectattr('state', 'equalto', 'available') }}"

- name: Get the list of software components in the firmware repository
  ansible.builtin.debug:
    msg: "{{ result_repository_out.FirmwareRepository |
        selectattr('id', 'equalto', '8aaa80788b7') | map(attribute='softwareComponents') | flatten }}"

- name: Get the list of software bundles in the firmware repository
  ansible.builtin.debug:
    msg: "{{ result_repository_out.FirmwareRepository |
        selectattr('id', 'equalto', '8aaa80788b7') | map(attribute='softwareBundles') | flatten }}"
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
            description: Enterprise features enabled.
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
            type: str
        mdmCluster:
            description: MDM cluster details.
            type: dict
            contains:
                clusterMode:
                    description: Cluster mode.
                    type: str
                clusterState:
                    description: Cluster state.
                    type: str
                goodNodesNum:
                    description: Number of good nodes.
                    type: int
                goodReplicasNum:
                    description: Number of good replicas.
                    type: int
                id:
                    description: Cluster ID.
                    type: str
                master:
                    description: Master MDM node details.
                    type: dict
                    contains:
                        id:
                            description: Node ID.
                            type: str
                        ips:
                            description: List of IP addresses.
                            type: list
                            elements: str
                        managementIPs:
                            description: List of management IP addresses.
                            type: list
                            elements: str
                        opensslVersion:
                            description: OpenSSL version.
                            type: str
                        port:
                            description: Communication port.
                            type: int
                        role:
                            description: Node role.
                            type: str
                        status:
                            description: Node status.
                            type: str
                        versionInfo:
                            description: Version information.
                            type: str
                        virtualInterfaces:
                            description: List of virtual interfaces.
                            type: list
                            elements: str
                slaves:
                    description: Slave MDM nodes.
                    type: list
                    elements: dict
                    contains:
                        id:
                            description: Node ID.
                            type: str
                        ips:
                            description: List of IP addresses.
                            type: list
                            elements: str
                        managementIPs:
                            description: List of management IP addresses.
                            type: list
                            elements: str
                        opensslVersion:
                            description: OpenSSL version.
                            type: str
                        port:
                            description: Communication port.
                            type: int
                        role:
                            description: Node role.
                            type: str
                        status:
                            description: Node status.
                            type: str
                        versionInfo:
                            description: Version information.
                            type: str
                        virtualInterfaces:
                            description: List of virtual interfaces.
                            type: list
                            elements: str
                standbyMDMs:
                    description: Standby MDM nodes.
                    type: list
                    elements: dict
                    contains:
                        id:
                            description: Node ID.
                            type: str
                        ips:
                            description: List of IP addresses.
                            type: list
                            elements: str
                        managementIPs:
                            description: List of management IP addresses.
                            type: list
                            elements: str
                        opensslVersion:
                            description: OpenSSL version.
                            type: str
                        port:
                            description: Communication port.
                            type: int
                        role:
                            description: Node role.
                            type: str
                        virtualInterfaces:
                            description: List of virtual interfaces.
                            type: list
                            elements: str
                tieBreakers:
                    description: Tie-breaker nodes.
                    type: list
                    elements: dict
                    contains:
                        id:
                            description: Node ID.
                            type: str
                        ips:
                            description: List of IP addresses.
                            type: list
                            elements: str
                        managementIPs:
                            description: List of management IP addresses.
                            type: list
                            elements: str
                        opensslVersion:
                            description: OpenSSL version.
                            type: str
                        port:
                            description: Communication port.
                            type: int
                        role:
                            description: Node role.
                            type: str
                        status:
                            description: Node status.
                            type: str
                        versionInfo:
                            description: Version information.
                            type: str
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
        "authenticationMethod": "Mno",
        "capacityAlertCriticalThresholdPercent": 90,
        "capacityAlertHighThresholdPercent": 80,
        "capacityTimeLeftInDays": "78",
        "cliPasswordAllowed": true,
        "daysInstalled": 12,
        "defragmentationEnabled": true,
        "enterpriseFeaturesEnabled": true,
        "id": "815945c41cd8460f",
        "installId": "0076d6af044b5481",
        "isInitialLicense": true,
        "lastUpgradeTime": 0,
        "managementClientSecureCommunicationEnabled": true,
        "maxCapacityInGb": "Unlimited",
        "mdmCluster": {
            "clusterMode": "ThreeNodes",
            "clusterState": "ClusteredNormal",
            "goodNodesNum": 3,
            "goodReplicasNum": 2,
            "id": "-9126186461289757169",
            "master": {
                "id": "2d5f17673e35a101",
                "ips": [
                    "10.225.106.68"
                ],
                "managementIPs": [
                    "10.225.106.68"
                ],
                "opensslVersion": "OpenSSL 3.1.4 24 Oct 2023",
                "port": 9011,
                "role": "Manager",
                "status": "Normal",
                "versionInfo": "R5_0.0.0",
                "virtualInterfaces": ["ens160"]
            },
            "slaves": [
                {
                    "id": "5c613b076fb30100",
                    "ips": [
                        "10.225.106.67"
                    ],
                    "managementIPs": [
                        "10.225.106.67"
                    ],
                    "opensslVersion": "OpenSSL 3.1.4 24 Oct 2023",
                    "port": 9011,
                    "role": "Manager",
                    "status": "Normal",
                    "versionInfo": "R5_0.0.0",
                    "virtualInterfaces": ["ens160"]
                }
            ],
            "standbyMDMs": [
                {
                    "id": "1ef63c213b382503",
                    "ips": [
                        "10.225.106.48"
                    ],
                    "managementIPs": [
                        "10.225.106.48"
                    ],
                    "opensslVersion": "N/A",
                    "port": 9011,
                    "role": "Manager",
                    "virtualInterfaces": []
                }
            ],
            "tieBreakers": [
                {
                    "id": "6b5ae1c7248e0c02",
                    "ips": [
                        "10.225.106.69"
                    ],
                    "managementIPs": [
                        "10.225.106.69"
                    ],
                    "opensslVersion": "N/A",
                    "port": 9011,
                    "role": "TieBreaker",
                    "status": "Normal",
                    "versionInfo": "R5_0.0.0"
                }
            ]
        },
        "mdmExternalPort": 7611,
        "mdmManagementPort": 8611,
        "mdmSecurityPolicy": "Authentication",
        "showGuid": true,
        "swid": "",
        "systemVersionName": "DellEMC PowerFlex Version: R5_0.0.937",
        "tlsVersion": "TLSv1.2",
        "upgradeState": "NoUpgrade"
    }
API_Version:
    description: API version of PowerFlex API Gateway.
    returned: always
    type: str
    sample: "5.0"
Protection_Domains:
    description: Details of all protection domains.
    returned: always
    type: list
    elements: dict
    contains:
        id:
            description: protection domain id.
            type: str
        name:
            description: protection domain name.
            type: str
        bandwidthLimitBgDevScanner:
            description: Bandwidth limit for background device scanner.
            type: int
        bandwidthLimitDoublyImpactedRebuild:
            description: Bandwidth limit for doubly impacted rebuild operations.
            type: int
        bandwidthLimitNodeNetwork:
            description: Bandwidth limit for node network.
            type: int
        bandwidthLimitOther:
            description: Bandwidth limit for other I/O operations.
            type: int
        bandwidthLimitOverallIos:
            description: Overall bandwidth limit for all I/O operations.
            type: int
        bandwidthLimitRebalance:
            description: Bandwidth limit for rebalance operations.
            type: int
        bandwidthLimitSinglyImpactedRebuild:
            description: Bandwidth limit for singly impacted rebuild operations.
            type: int
        fglDefaultMetadataCacheSize:
            description: Default metadata cache size for fine-grained logging.
            type: int
        fglDefaultNumConcurrentWrites:
            description: Default number of concurrent writes for fine-grained logging.
            type: int
        fglMetadataCacheEnabled:
            description: Whether metadata cache is enabled for fine-grained logging.
            type: bool
        genType:
            description: Generation type of the protection domain (e.g., EC for Erasure Coding).
            type: str
        links:
            description: Hypermedia links related to the protection domain.
            type: list
            elements: dict
            contains:
                href:
                    description: The URI reference.
                    type: str
                rel:
                    description: The relation type of the link.
                    type: str
        mdmSdsNetworkDisconnectionsCounterParameters:
            description: MDM-SDS network disconnection counter thresholds.
            type: dict
            contains:
                longWindow:
                    description: Long time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Disconnection threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                mediumWindow:
                    description: Medium time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Disconnection threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                shortWindow:
                    description: Short time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Disconnection threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
        overallConcurrentIoLimit:
            description: Overall concurrent I/O limit for the protection domain.
            type: int
        overallIoNetworkThrottlingEnabled:
            description: Whether overall I/O network throttling is enabled.
            type: bool
        protectedMaintenanceModeNetworkThrottlingEnabled:
            description: Whether network throttling is enabled in protected maintenance mode.
            type: bool
        protectionDomainState:
            description: Current state of the protection domain (e.g., Active).
            type: str
        rebalanceEnabled:
            description: Whether rebalance operations are enabled.
            type: bool
        rebalanceNetworkThrottlingEnabled:
            description: Whether network throttling is enabled for rebalance operations.
            type: bool
        rebuildEnabled:
            description: Whether rebuild operations are enabled.
            type: bool
        rebuildNetworkThrottlingEnabled:
            description: Whether network throttling is enabled for rebuild operations.
            type: bool
        rfcacheEnabled:
            description: Whether RF-Cache is enabled.
            type: bool
        rfcacheMaxIoSizeKb:
            description: Maximum I/O size in KB for RF-Cache.
            type: int
        rfcacheOpertionalMode:
            description: Operational mode of RF-Cache (e.g., WriteMiss).
            type: str
        rfcachePageSizeKb:
            description: Page size in KB used by RF-Cache.
            type: int
        rplCapAlertLevel:
            description: Replication capacity alert level.
            type: str
        sdrSdsConnectivityInfo:
            description: Connectivity information between SDR client and SDS server.
            type: dict
            contains:
                clientServerConnStatus:
                    description: Status of client-server connection.
                    type: str
                disconnectedClientId:
                    description: ID of disconnected client (null if connected).
                    type: str
                disconnectedClientName:
                    description: Name of disconnected client (null if connected).
                    type: str
                disconnectedServerId:
                    description: ID of disconnected server (null if connected).
                    type: str
                disconnectedServerIp:
                    description: IP of disconnected server (null if connected).
                    type: str
                disconnectedServerName:
                    description: Name of disconnected server (null if connected).
                    type: str
        sdsConfigurationFailureCounterParameters:
            description: SDS configuration failure counter thresholds.
            type: dict
            contains:
                longWindow:
                    description: Long time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Failure threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                mediumWindow:
                    description: Medium time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Failure threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                shortWindow:
                    description: Short time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Failure threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
        sdsDecoupledCounterParameters:
            description: SDS decoupled state counter thresholds.
            type: dict
            contains:
                longWindow:
                    description: Long time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Decoupled threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                mediumWindow:
                    description: Medium time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Decoupled threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                shortWindow:
                    description: Short time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Decoupled threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
        sdsReceiveBufferAllocationFailuresCounterParameters:
            description: SDS receive buffer allocation failure counter thresholds.
            type: dict
            contains:
                longWindow:
                    description: Long time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Buffer allocation failure threshold.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                mediumWindow:
                    description: Medium time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Buffer allocation failure threshold.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                shortWindow:
                    description: Short time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Buffer allocation failure threshold.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
        sdsSdsNetworkDisconnectionsCounterParameters:
            description: SDS-SDS network disconnection counter thresholds.
            type: dict
            contains:
                longWindow:
                    description: Long time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Disconnection threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                mediumWindow:
                    description: Medium time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Disconnection threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
                shortWindow:
                    description: Short time window threshold settings.
                    type: dict
                    contains:
                        threshold:
                            description: Disconnection threshold count.
                            type: int
                        windowSizeInSec:
                            description: Time window size in seconds.
                            type: int
        sdtSdsConnectivityInfo:
            description: Connectivity information between SDT and SDS.
            type: dict
            contains:
                clientServerConnStatus:
                    description: Status of client-server connection.
                    type: str
                disconnectedClientId:
                    description: ID of disconnected client (null if connected).
                    type: str
                disconnectedClientName:
                    description: Name of disconnected client (null if connected).
                    type: str
                disconnectedServerId:
                    description: ID of disconnected server (null if connected).
                    type: str
                disconnectedServerIp:
                    description: IP of disconnected server (null if connected).
                    type: str
                disconnectedServerName:
                    description: Name of disconnected server (null if connected).
                    type: str
        systemId:
            description: ID of the associated storage system.
            type: str
        vtreeMigrationNetworkThrottlingEnabled:
            description: Whether network throttling is enabled for vTree migration.
            type: bool
    sample: [
        {
            "bandwidthLimitBgDevScanner": 15,
            "bandwidthLimitDoublyImpactedRebuild": 400,
            "bandwidthLimitNodeNetwork": 30,
            "bandwidthLimitOther": 10,
            "bandwidthLimitOverallIos": 500,
            "bandwidthLimitRebalance": 50,
            "bandwidthLimitSinglyImpactedRebuild": 500,
            "fglDefaultMetadataCacheSize": 0,
            "fglDefaultNumConcurrentWrites": 0,
            "fglMetadataCacheEnabled": false,
            "genType": "EC",
            "id": "e597f3dd00000000",
            "links": [
                {
                    "href": "/api/instances/ProtectionDomain::e597f3dd00000000",
                    "rel": "self"
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
            "name": "PD_EC",
            "overallConcurrentIoLimit": 5,
            "overallIoNetworkThrottlingEnabled": false,
            "overallIoNetworkThrottlingInKbps": null,
            "protectedMaintenanceModeNetworkThrottlingEnabled": false,
            "protectedMaintenanceModeNetworkThrottlingInKbps": null,
            "protectionDomainState": "Active",
            "rebalanceEnabled": true,
            "rebalanceNetworkThrottlingEnabled": false,
            "rebalanceNetworkThrottlingInKbps": null,
            "rebuildEnabled": true,
            "rebuildNetworkThrottlingEnabled": false,
            "rebuildNetworkThrottlingInKbps": null,
            "rfcacheAccpId": null,
            "rfcacheEnabled": true,
            "rfcacheMaxIoSizeKb": 0,
            "rfcacheOpertionalMode": "WriteMiss",
            "rfcachePageSizeKb": 0,
            "rplCapAlertLevel": "invalid",
            "sdrSdsConnectivityInfo": {
                "clientServerConnStatus": "CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED",
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
            "sdtSdsConnectivityInfo": {
                "clientServerConnStatus": "CLIENT_SERVER_CONN_STATUS_ALL_CONNECTED",
                "disconnectedClientId": null,
                "disconnectedClientName": null,
                "disconnectedServerId": null,
                "disconnectedServerIp": null,
                "disconnectedServerName": null
            },
            "systemId": "815945c41cd8460f",
            "vtreeMigrationNetworkThrottlingEnabled": false,
            "vtreeMigrationNetworkThrottlingInKbps": null
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
        hostOsFullType:
            description: Full operating system type of the storage data client.
            type: str
        hostType:
            description: Host type of the storage data client.
            type: str
        installedSoftwareVersionInfo:
            description: Installed software version information on the SDC.
            type: str
        kernelBuildNumber:
            description: Kernel build number of the SDC's operating system.
            type: str
        kernelVersion:
            description: Kernel version of the SDC's operating system.
            type: str
        links:
            description: List of hypermedia links related to the SDC.
            type: list
            contains:
                href:
                    description: The URI of the resource.
                    type: str
                rel:
                    description: The relation type of the link.
                    type: str
        maxNumPaths:
            description: Maximum number of paths allowed for the SDC.
            type: str
        maxNumSysPorts:
            description: Maximum number of system ports allowed for the SDC.
            type: str
        mdmConnectionState:
            description: Current MDM (Management Domain Manager) connection state of the SDC.
            type: str
        mdmIpAddressesCurrent:
            description: Indicates whether the MDM IP addresses are current.
            type: bool
        memoryAllocationFailure:
            description: Indicates if there was a memory allocation failure on the SDC.
            type: str
        nqn:
            description: NVMe Qualified Name used for NVMe-o-Fabrics connectivity.
            type: str
        osType:
            description: Operating system type of the SDC.
            type: str
        peerMdmId:
            description: Identifier of the peer MDM that the SDC is connected to.
            type: str
        perfProfile:
            description: Performance profile configured for the SDC.
            type: str
        sdcAgentActive:
            description: Indicates whether the SDC agent is currently active.
            type: bool
        sdcApproved:
            description: Indicates whether the SDC is approved to connect to the system.
            type: bool
        sdcApprovedIps:
            description: List of approved IP addresses for the SDC.
            type: list
        sdcGuid:
            description: Globally unique identifier for the SDC.
            type: str
        sdcIp:
            description: Primary IP address of the SDC.
            type: str
        sdcIps:
            description: List of all IP addresses associated with the SDC.
            type: list
            elements: str
        sdcType:
            description: Type of the SDC (e.g., AppSdc).
            type: str
        sdrId:
            description: Identifier of the SDR (Storage Data Resilience) associated with the SDC.
            type: str
        sdtId:
            description: Identifier of the SDT (Storage Data Tunnel) associated with the SDC.
            type: str
        socketAllocationFailure:
            description: Indicates if there was a socket allocation failure on the SDC.
            type: str
        softwareVersionInfo:
            description: Current software version running on the SDC.
            type: str
        systemId:
            description: Identifier of the system to which the SDC belongs.
            type: str
        versionInfo:
            description: Version information of the SDC software.
            type: str
    sample: [
        {
            "hostOsFullType": null,
            "hostType": "SdcHost",
            "id": "fdc050eb00000000",
            "installedSoftwareVersionInfo": "R5_0.0.0",
            "kernelBuildNumber": null,
            "kernelVersion": "6.4.0",
            "links": [
                {
                    "href": "/api/instances/Sdc::fdc050eb00000000",
                    "rel": "self"
                }
            ],
            "maxNumPaths": null,
            "maxNumSysPorts": null,
            "mdmConnectionState": "Connected",
            "mdmIpAddressesCurrent": false,
            "memoryAllocationFailure": null,
            "name": "SDC3",
            "nqn": null,
            "osType": "Linux",
            "peerMdmId": null,
            "perfProfile": "HighPerformance",
            "sdcAgentActive": false,
            "sdcApproved": true,
            "sdcApprovedIps": null,
            "sdcGuid": "89843E55-2B2A-42F7-A970-505467F81981",
            "sdcIp": "10.225.106.69",
            "sdcIps": [
                "10.225.106.69"
            ],
            "sdcType": "AppSdc",
            "sdrId": null,
            "sdtId": null,
            "socketAllocationFailure": null,
            "softwareVersionInfo": "R5_0.0.0",
            "systemId": "815945c41cd8460f",
            "versionInfo": "R5_0.0.0"
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
        autoSnapshotCreationCadenceInMin:
            description: Interval in minutes between automatic snapshot creations.
            type: int
        isLastAutoSnapshotDataTimeAccurate:
            description: Indicates whether the timestamp of the last auto-snapshot data is accurate.
            type: str
        lastAutoSnapshotCreationFailureReason:
            description: Reason code for the last automatic snapshot creation failure.
            type: str
        lastAutoSnapshotDataTime:
            description: Timestamp of the last auto-snapshot data creation.
            type: str
        lastAutoSnapshotFailureInFirstLevel:
            description: Indicates if the last automatic snapshot failed at the first level.
            type: bool
        links:
            description: List of hypermedia links related to the snapshot policy.
            type: list
            contains:
                href:
                    description: The URI of the linked resource.
                    type: str
                rel:
                    description: The relation type of the link.
                    type: str
        maxVTreeAutoSnapshots:
            description: Maximum number of automatic snapshots allowed per VTree.
            type: int
        nextAutoSnapshotCreationTime:
            description: Timestamp (in seconds) of the next scheduled automatic snapshot.
            type: int
        numOfAutoSnapshots:
            description: Total number of automatic snapshots created under this policy.
            type: int
        numOfCreationFailures:
            description: Number of failed automatic snapshot creation attempts.
            type: int
        numOfExpiredButLockedSnapshots:
            description: Number of snapshots that have expired but are still locked.
            type: int
        numOfLockedSnapshots:
            description: Total number of snapshots currently locked.
            type: int
        numOfRetainedSnapshotsPerLevel:
            description: Number of snapshots retained per storage level.
            type: list
            elements: int
        numOfSourceVolumes:
            description: Number of source volumes associated with this snapshot policy.
            type: int
        rcgId:
            description: Identifier of the replication consistency group (RCG) associated with the policy.
            type: str
        rcgName:
            description: Name of the replication consistency group (RCG) associated with the policy.
            type: str
        secureSnapshots:
            description: Indicates whether snapshots are secure (immutable).
            type: bool
        snapshotAccessMode:
            description: Access mode of the created snapshots (e.g., ReadOnly).
            type: str
        snapshotPolicyState:
            description: Current state of the snapshot policy (e.g., Paused, Active).
            type: str
        systemId:
            description: Identifier of the system to which the snapshot policy belongs.
            type: str
        timeOfLastAutoSnapshot:
            description: Timestamp (in seconds) of the last successfully created automatic snapshot.
            type: int
        timeOfLastAutoSnapshotCreationFailure:
            description: Timestamp (in seconds) of the last automatic snapshot creation failure.
            type: int
    sample: [
        {
            "autoSnapshotCreationCadenceInMin": 5,
            "id": "dc095e4d00000000",
            "isLastAutoSnapshotDataTimeAccurate": null,
            "lastAutoSnapshotCreationFailureReason": "NR",
            "lastAutoSnapshotDataTime": null,
            "lastAutoSnapshotFailureInFirstLevel": false,
            "links": [
                {
                    "href": "/api/instances/SnapshotPolicy::dc095e4d00000000",
                    "rel": "self"
                }
            ],
            "maxVTreeAutoSnapshots": 1,
            "name": "Sample_snap_policy_Ray",
            "nextAutoSnapshotCreationTime": 0,
            "numOfAutoSnapshots": 0,
            "numOfCreationFailures": 0,
            "numOfExpiredButLockedSnapshots": 0,
            "numOfLockedSnapshots": 0,
            "numOfRetainedSnapshotsPerLevel": [
                1
            ],
            "numOfSourceVolumes": 0,
            "rcgId": null,
            "rcgName": null,
            "secureSnapshots": false,
            "snapshotAccessMode": "ReadOnly",
            "snapshotPolicyState": "Paused",
            "systemId": "815945c41cd8460f",
            "timeOfLastAutoSnapshot": 0,
            "timeOfLastAutoSnapshotCreationFailure": 0
        }
    ]
Storage_Pools:
    description: Details of storage pools.
    returned: always
    type: list
    contains:
        mediaType:
            description: Type of devices in the storage pool.
            type: str
        useRfcache:
            description: Enable/Disable RFcache on a specific storage pool.
            type: bool
        useRmcache:
            description: Enable/Disable RMcache on a specific storage pool.
            type: bool
        id:
            description: ID of the storage pool under protection domain.
            type: str
        name:
            description: Name of the storage pool under protection domain.
            type: str
        protectionDomainId:
            description: ID of the protection domain in which pool resides.
            type: str
        addressSpaceUsage:
            description: Address space usage level of the storage pool.
            type: str
        addressSpaceUsageType:
            description: Type of address space usage (e.g., hard limit or soft limit).
            type: str
        backgroundScannerBWLimitKBps:
            description: Bandwidth limit in KBps for background scanner operations.
            type: int
        backgroundScannerMode:
            description: Mode of the background scanner (e.g., disabled, full, etc.).
            type: str
        bgScannerCompareErrorAction:
            description: Action to take when a compare error is detected during background scanning.
            type: str
        bgScannerReadErrorAction:
            description: Action to take when a read error is detected during background scanning.
            type: str
        capacityAlertCriticalThreshold:
            description: Threshold percentage for triggering critical capacity alerts.
            type: int
        capacityAlertHighThreshold:
            description: Threshold percentage for triggering high capacity alerts.
            type: int
        capacityUsageState:
            description: Current state of capacity usage (e.g., Normal, Critical).
            type: str
        capacityUsageType:
            description: Type of capacity usage metric being reported.
            type: str
        checksumEnabled:
            description: Indicates whether checksum is enabled for data integrity.
            type: bool
        compressionMethod:
            description: Compression method used in the storage pool.
            type: str
        dataLayout:
            description: Data layout scheme used in the storage pool (e.g., ErasureCoding).
            type: str
        deviceGroupId:
            description: ID of the device group associated with the storage pool.
            type: str
        externalAccelerationType:
            description: Type of external acceleration used.
            type: str
        fglAccpId:
            description: Acceleration policy ID for FlashGuard Log (FGL) if applicable.
            type: str
        fglExtraCapacity:
            description: Extra capacity allocated for FlashGuard Log.
            type: int
        fglMaxCompressionRatio:
            description: Maximum compression ratio allowed for FlashGuard Log.
            type: int
        fglMetadataSizeXx100:
            description: Metadata size for FlashGuard Log as a percentage (multiplied by 100).
            type: int
        fglNvdimmMetadataAmortizationX100:
            description: NVDIMM metadata amortization factor for FlashGuard Log (multiplied by 100).
            type: int
        fglNvdimmWriteCacheSizeInMb:
            description: Write cache size in MB for NVDIMM in FlashGuard Log.
            type: int
        fglOverProvisioningFactor:
            description: Over-provisioning factor for FlashGuard Log.
            type: int
        fglPerfProfile:
            description: Performance profile setting for FlashGuard Log.
            type: str
        fglWriteAtomicitySize:
            description: Write atomicity size for FlashGuard Log.
            type: int
        fragmentationEnabled:
            description: Indicates whether fragmentation is enabled in the storage pool.
            type: bool
        genType:
            description: Generation type of the storage pool (e.g., EC for Erasure Coding).
            type: str
        links:
            description: HATEOAS links related to the storage pool.
            type: list
            contains:
                href:
                    description: URL reference for the link.
                    type: str
                rel:
                    description: Relation type of the link (e.g., self).
                    type: str
        numOfParallelRebuildRebalanceJobsPerDevice:
            description: Number of parallel rebuild and rebalance jobs allowed per device.
            type: int
        overProvisioningFactor:
            description: Over-provisioning factor applied to the storage pool.
            type: int
        persistentChecksumBuilderLimitKb:
            description: Limit in KB for persistent checksum builder operations.
            type: int
        persistentChecksumEnabled:
            description: Indicates whether persistent checksum is enabled.
            type: bool
        persistentChecksumState:
            description: Current state of persistent checksum (e.g., StateInvalid, Valid).
            type: str
        persistentChecksumValidateOnRead:
            description: Whether to validate persistent checksum on read operations.
            type: bool
        physicalSizeGB:
            description: Physical size of the storage pool in gigabytes.
            type: int
        protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps:
            description: Application bandwidth threshold per device in Kbps during protected maintenance mode.
            type: int
        protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold:
            description: Application IOPS threshold per device during protected maintenance mode.
            type: int
        protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps:
            description: Bandwidth limit per device in Kbps during protected maintenance mode.
            type: int
        protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice:
            description: Maximum number of concurrent IOs per device during protected maintenance mode.
            type: int
        protectedMaintenanceModeIoPriorityPolicy:
            description: IO priority policy during protected maintenance mode.
            type: str
        protectedMaintenanceModeIoPriorityQuietPeriodInMsec:
            description: Quiet period in milliseconds during protected maintenance mode.
            type: int
        protectionDomainName:
            description: Name of the protection domain in which pool resides.
            type: str
        protectionScheme:
            description: Data protection scheme used (e.g., TwoPlusTwo).
            type: str
        rawSizeGB:
            description: Raw (unformatted) size of the storage pool in gigabytes.
            type: int
        rebalanceEnabled:
            description: Indicates whether rebalancing is enabled for the storage pool.
            type: bool
        rebalanceIoPriorityAppBwPerDeviceThresholdInKbps:
            description: Application bandwidth threshold per device in Kbps during rebalance.
            type: int
        rebalanceIoPriorityAppIopsPerDeviceThreshold:
            description: Application IOPS threshold per device during rebalance.
            type: int
        rebalanceIoPriorityBwLimitPerDeviceInKbps:
            description: Bandwidth limit per device in Kbps during rebalance.
            type: int
        rebalanceIoPriorityNumOfConcurrentIosPerDevice:
            description: Maximum number of concurrent IOs per device during rebalance.
            type: int
        rebalanceIoPriorityPolicy:
            description: IO priority policy during rebalance operations.
            type: str
        rebalanceIoPriorityQuietPeriodInMsec:
            description: Quiet period in milliseconds during rebalance operations.
            type: int
        rebuildEnabled:
            description: Indicates whether rebuilding is enabled for the storage pool.
            type: bool
        rebuildIoPriorityAppBwPerDeviceThresholdInKbps:
            description: Application bandwidth threshold per device in Kbps during rebuild.
            type: int
        rebuildIoPriorityAppIopsPerDeviceThreshold:
            description: Application IOPS threshold per device during rebuild.
            type: int
        rebuildIoPriorityBwLimitPerDeviceInKbps:
            description: Bandwidth limit per device in Kbps during rebuild.
            type: int
        rebuildIoPriorityNumOfConcurrentIosPerDevice:
            description: Maximum number of concurrent IOs per device during rebuild.
            type: int
        rebuildIoPriorityPolicy:
            description: IO priority policy during rebuild operations.
            type: str
        rebuildIoPriorityQuietPeriodInMsec:
            description: Quiet period in milliseconds during rebuild operations.
            type: int
        replicationCapacityMaxRatio:
            description: Maximum replication capacity ratio allowed.
            type: int
        rmcacheWriteHandlingMode:
            description: Write handling mode for RMcache.
            type: str
        spClass:
            description: Storage pool class (e.g., Default).
            type: str
        spHealthState:
            description: Health state of the storage pool (e.g., Protected).
            type: str
        sparePercentage:
            description: Percentage of spare capacity reserved in the storage pool.
            type: int
        vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps:
            description: Application bandwidth threshold per device in Kbps during vTree migration.
            type: int
        vtreeMigrationIoPriorityAppIopsPerDeviceThreshold:
            description: Application IOPS threshold per device during vTree migration.
            type: int
        vtreeMigrationIoPriorityBwLimitPerDeviceInKbps:
            description: Bandwidth limit per device in Kbps during vTree migration.
            type: int
        vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice:
            description: Maximum number of concurrent IOs per device during vTree migration.
            type: int
        vtreeMigrationIoPriorityPolicy:
            description: IO priority policy during vTree migration.
            type: str
        vtreeMigrationIoPriorityQuietPeriodInMsec:
            description: Quiet period in milliseconds during vTree migration.
            type: int
        wrcDeviceGroupId:
            description: Write Reduction Cache (WRC) device group ID.
            type: str
        zeroPaddingEnabled:
            description: Indicates whether zero padding is enabled for the storage pool.
            type: bool
        statistics:
            description: List of performance and capacity statistics for the storage pool.
            type: list
            elements: dict
            contains:
                name:
                    description: Name of the statistic (e.g., avg_host_read_latency).
                    type: str
                values:
                    description: Values for the statistic.
                    type: list
    sample: [
        {
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
            "deviceGroupId": "d291d60100000000",
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
            "id": "372743fc00000000",
            "links": [
                {
                    "href": "/api/instances/StoragePool::372743fc00000000",
                    "rel": "self"
                }
            ],
            "statistics": [
                {"name": "avg_host_read_latency", "values": [0]},
                {"name": "raw_used", "values": [13190918307840]},
                {"name": "logical_used", "values": [0]},
                {"name": "host_write_bandwidth", "values": [0]},
                {"name": "host_write_iops", "values": [0]},
                {"name": "storage_fe_write_bandwidth", "values": [0]},
                {"name": "storage_fe_write_iops", "values": [0]},
                {"name": "avg_fe_write_io_size", "values": [0]},
                {"name": "storage_fe_read_bandwidth", "values": [0]},
                {"name": "storage_fe_read_iops", "values": [0]},
                {"name": "avg_fe_read_io_size", "values": [0]},
                {"name": "utilization_ratio", "values": [0.008140671]},
                {"name": "compression_reducible_ratio", "values": [0.0]},
                {"name": "host_read_bandwidth", "values": [0]},
                {"name": "host_read_iops", "values": [0]},
                {"name": "data_reduction_ratio", "values": [0.0]},
                {"name": "thin_provisioning_ratio", "values": ["0.8"]},
                {"name": "avg_wrc_write_latency", "values": [0]},
                {"name": "unreducible_data", "values": [0]},
                {"name": "avg_wrc_read_latency", "values": [0]},
                {"name": "storage_fe_read_latency", "values": [0]},
                {"name": "over_provisioning_limit", "values": [4611686017353646080]},
                {"name": "patterns_saving_ratio", "values": [0.0]},
                {"name": "avg_host_write_latency", "values": [0]},
                {"name": "storage_fe_write_latency", "values": [0]},
                {"name": "logical_provisioned", "values": [42949672960]},
                {"name": "efficiency_ratio", "values": ["0.8"]},
                {"name": "storage_fe_trim_latency", "values": [0]},
                {"name": "physical_system", "values": [53687091200]},
                {"name": "data_reduction_reducible_ratio", "values": [0.0]},
                {"name": "storage_fe_trim_bandwidth", "values": [0]},
                {"name": "storage_fe_trim_iops", "values": [0]},
                {"name": "avg_fe_trim_io_size", "values": [0]},
                {"name": "compression_ratio", "values": [0.0]},
                {"name": "reducible_ratio", "values": [1.0]},
                {"name": "physical_used", "values": [0]},
                {"name": "snapshot_saving_ratio", "values": [0.0]},
                {"name": "physical_free", "values": [6541235191808]},
                {"name": "host_trim_bandwidth", "values": [0]},
                {"name": "host_trim_iops", "values": [0]},
                {"name": "total_wrc_write_bandwidth", "values": [0]},
                {"name": "total_wrc_write_iops", "values": [0]},
                {"name": "avg_wrc_write_io_size", "values": [0]},
                {"name": "total_wrc_read_bandwidth", "values": [0]},
                {"name": "total_wrc_read_iops", "values": [0]},
                {"name": "avg_wrc_read_io_size", "values": [0]},
                {"name": "physical_total", "values": [6594922283008]},
                {"name": "logical_owned", "values": [0]},
                {"name": "patterns_saving_reducible_ratio", "values": [0.0]},
                {"name": "avg_host_trim_latency", "values": [0]}
            ],
            "mediaType": null,
            "name": "SP_EC",
            "numOfParallelRebuildRebalanceJobsPerDevice": null,
            "overProvisioningFactor": 0,
            "persistentChecksumBuilderLimitKb": null,
            "persistentChecksumEnabled": false,
            "persistentChecksumState": "StateInvalid",
            "persistentChecksumValidateOnRead": null,
            "physicalSizeGB": 4095,
            "protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps": null,
            "protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold": null,
            "protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps": null,
            "protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice": null,
            "protectedMaintenanceModeIoPriorityPolicy": null,
            "protectedMaintenanceModeIoPriorityQuietPeriodInMsec": null,
            "protectionDomainId": "e597f3dd00000000",
            "protectionScheme": "TwoPlusTwo",
            "rawSizeGB": 8190,
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
            "useRfcache": false,
            "useRmcache": false,
            "vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps": null,
            "vtreeMigrationIoPriorityAppIopsPerDeviceThreshold": null,
            "vtreeMigrationIoPriorityBwLimitPerDeviceInKbps": null,
            "vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice": null,
            "vtreeMigrationIoPriorityPolicy": null,
            "vtreeMigrationIoPriorityQuietPeriodInMsec": null,
            "wrcDeviceGroupId": "d291d60100000000",
            "zeroPaddingEnabled": true
        }
    ]
Volumes:
    description: Details of volumes.
    returned: always
    type: list
    contains:
        accessModeLimit:
            description: Access mode limit for the volume (e.g., ReadWrite).
            type: str
        ancestorVolumeId:
            description: ID of the ancestor volume, if this is a snapshot.
            type: str
        autoSnapshotGroupId:
            description: ID of the auto-snapshot group associated with the volume.
            type: str
        compressionMethod:
            description: Compression method used for the volume (e.g., NotApplicable).
            type: str
        consistencyGroupId:
            description: ID of the consistency group the volume belongs to.
            type: str
        creationTime:
            description: Unix timestamp (in seconds) when the volume was created.
            type: int
        dataLayout:
            description: Data layout type of the volume (e.g., ErasureCoding).
            type: str
        genType:
            description: Generation type of the volume (e.g., EC).
            type: str
        id:
            description: Unique identifier of the volume.
            type: str
        links:
            description: List of hypermedia links related to the volume.
            type: list
            contains:
                href:
                    description: URL reference for the link.
                    type: str
                rel:
                    description: Relationship of the link (e.g., self, query).
                    type: str
        lockedAutoSnapshot:
            description: Indicates whether the auto-snapshot is locked.
            type: bool
        lockedAutoSnapshotMarkedForRemoval:
            description: Indicates whether the locked auto-snapshot is marked for removal.
            type: bool
        managedBy:
            description: System or component managing the volume (e.g., ScaleIO).
            type: str
        mappedSdcInfo:
            description: Information about SDCs (hosts) mapped to this volume.
            type: list
            contains:
                accessMode:
                    description: Access mode granted to the SDC (e.g., ReadWrite).
                    type: str
                hostType:
                    description: Type of host (e.g., SdcHost).
                    type: str
                isDirectBufferMapping:
                    description: Indicates whether direct buffer mapping is used.
                    type: bool
                limitBwInMbps:
                    description: Bandwidth limit in Mbps (0 means unlimited).
                    type: int
                limitIops:
                    description: IOPS limit (0 means unlimited).
                    type: int
                nqn:
                    description: NVMe Qualified Name, if applicable.
                    type: str
                sdcId:
                    description: Unique ID of the SDC (host).
                    type: str
                sdcIp:
                    description: IP address of the SDC.
                    type: str
                sdcName:
                    description: Name of the SDC.
                    type: str
        name:
            description: Name of the volume.
            type: str
        notGenuineSnapshot:
            description: Indicates whether the snapshot is not a genuine point-in-time copy.
            type: bool
        nsid:
            description: Namespace ID assigned to the volume.
            type: int
        originalExpiryTime:
            description: Original expiry time for the volume or snapshot.
            type: int
        pairIds:
            description: List of paired volume IDs, if volume is part of a pair.
            type: str
        replicationJournalVolume:
            description: Indicates whether the volume is used as a journal for replication.
            type: bool
        replicationTimeStamp:
            description: Timestamp of the last replication event.
            type: int
        retentionLevels:
            description: List of retention levels configured for the volume.
            type: list
        secureSnapshotExpTime:
            description: Expiration time for secure snapshots.
            type: int
        sizeInKb:
            description: Size of the volume in kilobytes.
            type: int
        snplIdOfAutoSnapshot:
            description: Snapshot policy ID associated with auto-snapshot.
            type: str
        snplIdOfSourceVolume:
            description: Snapshot policy ID of the source volume.
            type: str
        storagePoolId:
            description: ID of the storage pool where the volume resides.
            type: str
        timeStampIsAccurate:
            description: Indicates whether the timestamp is accurate.
            type: bool
        useRmcache:
            description: Indicates whether remote cache is enabled for the volume.
            type: bool
        volumeClass:
            description: Class or QoS policy assigned to the volume.
            type: str
        volumeReplicationState:
            description: Replication state of the volume (e.g., UnmarkedForReplication).
            type: str
        volumeType:
            description: Type of the volume (e.g., ThinProvisioned).
            type: str
        vtreeId:
            description: ID of the VTree (virtual tree) to which the volume belongs.
            type: str
        statistics:
            description: List of performance and capacity statistics for the volume.
            type: list
            contains:
                name:
                    description: Name of the statistic (e.g., avg_host_read_latency).
                    type: str
                values:
                    description: Values for the statistic.
                    type: list
    sample: [
        {
            "accessModeLimit": "ReadWrite",
            "ancestorVolumeId": null,
            "autoSnapshotGroupId": null,
            "compressionMethod": "NotApplicable",
            "consistencyGroupId": null,
            "creationTime": 1757086835,
            "dataLayout": "ErasureCoding",
            "genType": "EC",
            "id": "ae4f49db00000000",
            "links": [
                {
                    "href": "/api/instances/Volume::ae4f49db00000000",
                    "rel": "self"
                }
            ],
            "statistics": [
                {"name": "host_trim_bandwidth", "values": [0]},
                {"name": "host_trim_iops", "values": [0]},
                {"name": "avg_host_write_latency", "values": [0]},
                {"name": "avg_host_read_latency", "values": [0]},
                {"name": "logical_provisioned", "values": [10737418240]},
                {"name": "host_read_bandwidth", "values": [0]},
                {"name": "host_read_iops", "values": [0]},
                {"name": "logical_used", "values": [0]},
                {"name": "host_write_bandwidth", "values": [0]},
                {"name": "host_write_iops", "values": [0]},
                {"name": "avg_host_trim_latency", "values": [0]}
            ],
            "lockedAutoSnapshot": false,
            "lockedAutoSnapshotMarkedForRemoval": false,
            "managedBy": "ScaleIO",
            "mappedSdcInfo": [
                {
                    "accessMode": "ReadWrite",
                    "hostType": "SdcHost",
                    "isDirectBufferMapping": false,
                    "limitBwInMbps": 0,
                    "limitIops": 0,
                    "nqn": null,
                    "sdcId": "e5282d9800000001",
                    "sdcIp": "10.225.106.98",
                    "sdcName": "SDC2"
                }
            ],
            "name": "ans_dev_1",
            "notGenuineSnapshot": false,
            "nsid": 1,
            "originalExpiryTime": 0,
            "pairIds": null,
            "replicationJournalVolume": false,
            "replicationTimeStamp": 0,
            "retentionLevels": [],
            "secureSnapshotExpTime": 0,
            "sizeInKb": 10485760,
            "snplIdOfAutoSnapshot": null,
            "snplIdOfSourceVolume": "5026b97c00000000",
            "storagePoolId": "ea96090d00000000",
            "timeStampIsAccurate": false,
            "useRmcache": false,
            "volumeClass": "defaultclass",
            "volumeReplicationState": "UnmarkedForReplication",
            "volumeType": "ThinProvisioned",
            "vtreeId": "c7c9baf500000000"
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
        accelerationPoolId:
            description: ID of the acceleration pool associated with the device.
            type: str
        accelerationProps:
            description: Acceleration properties of the device.
            type: str
        aggregatedState:
            description: Aggregated health state of the device (e.g., NeverFailed).
            type: str
        ataSecurityActive:
            description: Indicates whether ATA security is active on the device.
            type: bool
        autoDetectMediaType:
            description: Indicates whether media type auto-detection is enabled.
            type: str
        cacheLookAheadActive:
            description: Indicates whether cache look-ahead is enabled for the device.
            type: bool
        capacity:
            description: Total capacity of the device (in KB or other unit, context-dependent).
            type: int
        capacityInMb:
            description: Total capacity of the device in megabytes.
            type: int
        capacityLimitInKb:
            description: Capacity limit of the device in kilobytes.
            type: int
        deviceCurrentPathName:
            description: Current device path name (e.g., /dev/sdf).
            type: str
        deviceGroupId:
            description: ID of the device group to which the device belongs.
            type: str
        deviceOriginalPathName:
            description: Original device path name at time of discovery.
            type: str
        deviceState:
            description: Current operational state of the device (e.g., Normal).
            type: str
        deviceType:
            description: Type of the device (e.g., Unknown, SSD).
            type: str
        errorState:
            description: Current error state of the device (e.g., None).
            type: str
        externalAccelerationType:
            description: Type of external acceleration used (e.g., None).
            type: str
        fglNvdimmMetadataAmortizationX100:
            description: Metadata amortization factor for FlashGuard Log (FGL) devices.
            type: str
        fglNvdimmWriteCacheSize:
            description: NVDIMM write cache size for FlashGuard Log (FGL) devices.
            type: str
        firmwareVersion:
            description: Firmware version of the device.
            type: str
        ledSetting:
            description: Current LED indicator setting of the device (e.g., Off).
            type: str
        links:
            description: List of hypermedia links related to the device.
            type: list
            contains:
                href:
                    description: The URI of the linked resource.
                    type: str
                rel:
                    description: The relation type of the link.
                    type: str
        logicalSectorSizeInBytes:
            description: Logical sector size of the device in bytes.
            type: int
        longSuccessfulIos:
            description: Long-term successful I/O statistics for the device.
            type: dict
            contains:
                longWindow:
                    description: Number of successful I/Os in the long time window.
                    type: str
                mediumWindow:
                    description: Number of successful I/Os in the medium time window.
                    type: str
                shortWindow:
                    description: Number of successful I/Os in the short time window.
                    type: str
        maxCapacityInKb:
            description: Maximum supported capacity of the device in kilobytes.
            type: int
        mediaFailing:
            description: Indicates whether the device media is failing.
            type: bool
        mediaType:
            description: Type of media used in the device (e.g., SSD).
            type: str
        modelName:
            description: Model name of the device.
            type: str
        persistentChecksumState:
            description: State of persistent checksum on the device (e.g., StateInvalid).
            type: str
        physicalSectorSizeInBytes:
            description: Physical sector size of the device in bytes.
            type: int
        raidControllerSerialNumber:
            description: Serial number of the RAID controller managing the device.
            type: str
        rfcacheErrorDeviceDoesNotExist:
            description: Indicates if there is an RFcache error due to missing device.
            type: bool
        rfcacheProps:
            description: RFcache properties associated with the device.
            type: str
        sdsId:
            description: ID of the SDS (ScaleIO Data Server) managing the device.
            type: str
        serialNumber:
            description: Serial number of the device.
            type: str
        slotNumber:
            description: Physical slot number where the device is installed (e.g., N/A).
            type: str
        spSdsId:
            description: SDS ID specific to the storage pool.
            type: str
        ssdEndOfLifeState:
            description: SSD end-of-life status (e.g., NeverFailed).
            type: str
        storageNodeId:
            description: ID of the storage node hosting the device.
            type: str
        storagePoolId:
            description: ID of the storage pool to which the device is assigned.
            type: str
        storageProps:
            description: Storage-related properties of the device.
            type: str
        temperatureState:
            description: Temperature health state of the device (e.g., NeverFailed).
            type: str
        usableCapacityInMb:
            description: Usable capacity of the device in megabytes.
            type: int
        vendorName:
            description: Manufacturer/vendor name of the device.
            type: str
        writeCacheActive:
            description: Indicates whether write cache is currently active on the device.
            type: bool
    sample: [
        {
            "accelerationPoolId": null,
            "accelerationProps": null,
            "aggregatedState": "NeverFailed",
            "ataSecurityActive": false,
            "autoDetectMediaType": null,
            "cacheLookAheadActive": false,
            "capacity": 0,
            "capacityInMb": 1048576,
            "capacityLimitInKb": 1073479680,
            "deviceCurrentPathName": "/dev/sdf",
            "deviceGroupId": "d291d60100000000",
            "deviceOriginalPathName": "/dev/sdf",
            "deviceState": "Normal",
            "deviceType": "Unknown",
            "errorState": "None",
            "externalAccelerationType": "None",
            "fglNvdimmMetadataAmortizationX100": null,
            "fglNvdimmWriteCacheSize": null,
            "firmwareVersion": null,
            "id": "63efabfb00000004",
            "ledSetting": "Off",
            "links": [
                {
                    "href": "/api/instances/Device::63efabfb00000004",
                    "rel": "self"
                }
            ],
            "logicalSectorSizeInBytes": 0,
            "longSuccessfulIos": {
                "longWindow": null,
                "mediumWindow": null,
                "shortWindow": null
            },
            "maxCapacityInKb": 1073479680,
            "mediaFailing": false,
            "mediaType": "SSD",
            "modelName": null,
            "name": "sdf",
            "persistentChecksumState": "StateInvalid",
            "physicalSectorSizeInBytes": 0,
            "raidControllerSerialNumber": null,
            "rfcacheErrorDeviceDoesNotExist": false,
            "rfcacheProps": null,
            "sdsId": null,
            "serialNumber": null,
            "slotNumber": "N/A",
            "spSdsId": null,
            "ssdEndOfLifeState": "NeverFailed",
            "storageNodeId": "876859f300000000",
            "storagePoolId": null,
            "storageProps": null,
            "temperatureState": "NeverFailed",
            "usableCapacityInMb": 1048320,
            "vendorName": null,
            "writeCacheActive": false
        }
    ]
ManagedDevices:
    description: Details of all devices from inventory.
    returned: when I(gather_subset) is I(managed_device)
    type: list
    contains:
        deviceType:
            description: Device Type.
            type: str
        serviceTag:
            description: Service Tag.
            type: str
        serverTemplateId:
            description: The ID of the server template.
            type: str
        state:
            description: The state of the device.
            type: str
        managedState:
            description: The managed state of the device.
            type: str
        compliance:
            description: The compliance state of the device.
            type: str
        systemId:
            description: The system ID.
            type: str
        chassisId:
            description: Chassis ID to which the device belongs, if applicable.
            type: str
        complianceCheckDate:
            description: Timestamp when the compliance check was last performed.
            type: str
        config:
            description: Configuration details of the device.
            type: str
        cpuType:
            description: Type of CPU installed on the device.
            type: str
        credId:
            description: Credential ID used for device authentication.
            type: str
        currentIpAddress:
            description: Current IP address assigned to the device.
            type: str
        customFirmware:
            description: Indicates whether custom firmware is applied to the device.
            type: bool
        detailLink:
            description: Hypermedia link providing more details about the device.
            type: dict
            contains:
                href:
                    description: The URI of the detailed resource.
                    type: str
                rel:
                    description: The relation type of the link.
                    type: str
                title:
                    description: Human-readable title of the linked resource.
                    type: str
                type:
                    description: Media type of the linked resource.
                    type: str
        deviceGroupList:
            description: List of device groups the device belongs to.
            type: dict
            contains:
                deviceGroup:
                    description: List of device group entries.
                    type: list
                    contains:
                        createdBy:
                            description: User who created the device group.
                            type: str
                        createdDate:
                            description: Date when the device group was created.
                            type: str
                        groupDescription:
                            description: Description of the device group.
                            type: str
                        groupName:
                            description: Name of the device group.
                            type: str
                        groupSeqId:
                            description: Sequential ID of the device group.
                            type: int
                        groupUserList:
                            description: List of users associated with the device group.
                            type: str
                        link:
                            description: Link to the device group resource.
                            type: str
                        managedDeviceList:
                            description: List of managed devices in the group.
                            type: str
                        updatedBy:
                            description: User who last updated the device group.
                            type: str
                        updatedDate:
                            description: Date when the device group was last updated.
                            type: str
                paging:
                    description: Pagination information for the device group list.
                    type: str
        discoverDeviceType:
            description: Discovered device type (e.g., SCALEIO).
            type: str
        discoveredDate:
            description: Timestamp when the device was discovered.
            type: str
        displayName:
            description: Display name of the device.
            type: str
        esxiMaintMode:
            description: ESXi maintenance mode status of the device.
            type: int
        failuresCount:
            description: Number of failures reported for the device.
            type: int
        firmwareName:
            description: Name of the firmware or catalog applied to the device.
            type: str
        flexosMaintMode:
            description: FlexOS maintenance mode status of the device.
            type: int
        health:
            description: Overall health status of the device (e.g., GREEN).
            type: str
        healthMessage:
            description: Health status message (e.g., OK).
            type: str
        hostname:
            description: Hostname of the device.
            type: str
        inUse:
            description: Indicates whether the device is currently in use.
            type: bool
        infraTemplateDate:
            description: Date of the infrastructure template applied.
            type: str
        infraTemplateId:
            description: ID of the infrastructure template applied.
            type: str
        inventoryDate:
            description: Timestamp when the device inventory was last updated.
            type: str
        ipAddress:
            description: IP address of the device.
            type: str
        lastJobs:
            description: List of recent jobs executed on the device.
            type: str
        manufacturer:
            description: Manufacturer of the device (e.g., Dell EMC).
            type: str
        memoryInGB:
            description: Total memory of the device in gigabytes.
            type: int
        model:
            description: Model name of the device (e.g., PowerFlex Gateway).
            type: str
        needsAttention:
            description: Indicates whether the device requires attention.
            type: bool
        nics:
            description: Number of network interface cards on the device.
            type: int
        numberOfCPUs:
            description: Number of CPUs installed on the device.
            type: int
        operatingSystem:
            description: Operating system running on the device (e.g., N/A).
            type: str
        osAdminCredential:
            description: Credential for OS-level administrative access.
            type: str
        osImageType:
            description: Type of OS image used.
            type: str
        osIpAddress:
            description: IP address assigned to the OS instance.
            type: str
        parsedFacts:
            description: Parsed system facts collected from the device.
            type: str
        puppetCertName:
            description: Puppet certificate name for the device.
            type: str
        refId:
            description: Reference ID of the device.
            type: str
        refType:
            description: Reference type of the device.
            type: str
        serverTemplateDate:
            description: Date of the server template applied.
            type: str
        serviceReferences:
            description: List of service references associated with the device.
            type: list
        statusMessage:
            description: Additional status message for the device.
            type: str
        svmAdminCredential:
            description: Credential for SVM (Storage Virtual Machine) access.
            type: str
        svmImageType:
            description: Type of SVM image used.
            type: str
        svmIpAddress:
            description: IP address assigned to the SVM.
            type: str
        svmName:
            description: Name of the SVM.
            type: str
        vmList:
            description: List of virtual machines associated with the device.
            type: list
    sample: [
        {
            "chassisId": null,
            "compliance": "NONCOMPLIANT",
            "complianceCheckDate": "2025-09-04T16:00:51.857+00:00",
            "config": null,
            "cpuType": null,
            "credId": "e938b574-8a0d-4b20-aea6-e0dd557d766d",
            "currentIpAddress": "10.43.1.67",
            "customFirmware": false,
            "detailLink": {
                "href": "/AsmManager/ManagedDevice/scaleio-block-legacy-gateway",
                "rel": "describedby",
                "title": "scaleio-block-legacy-gateway",
                "type": null
            },
            "deviceGroupList": {
                "deviceGroup": [
                    {
                        "createdBy": "admin",
                        "createdDate": null,
                        "groupDescription": null,
                        "groupName": "Global",
                        "groupSeqId": -1,
                        "groupUserList": null,
                        "link": null,
                        "managedDeviceList": null,
                        "updatedBy": null,
                        "updatedDate": null
                    }
                ],
                "paging": null
            },
            "deviceType": "scaleio",
            "discoverDeviceType": "SCALEIO",
            "discoveredDate": "2025-08-22T15:48:05.477+00:00",
            "displayName": "block-legacy-gateway",
            "esxiMaintMode": 0,
            "failuresCount": 0,
            "firmwareName": "Default Catalog - Intelligent Catalog 50.390.00",
            "flexosMaintMode": 0,
            "health": "GREEN",
            "healthMessage": "OK",
            "hostname": null,
            "inUse": false,
            "infraTemplateDate": null,
            "infraTemplateId": null,
            "inventoryDate": null,
            "ipAddress": "block-legacy-gateway",
            "lastJobs": null,
            "managedState": "MANAGED",
            "manufacturer": "Dell EMC",
            "memoryInGB": 0,
            "model": "PowerFlex Gateway",
            "needsAttention": false,
            "nics": 0,
            "numberOfCPUs": 0,
            "operatingSystem": "N/A",
            "osAdminCredential": null,
            "osImageType": null,
            "osIpAddress": null,
            "parsedFacts": null,
            "puppetCertName": "scaleio-block-legacy-gateway",
            "refId": "scaleio-block-legacy-gateway",
            "refType": null,
            "serverTemplateDate": null,
            "serverTemplateId": null,
            "serviceReferences": [],
            "serviceTag": "block-legacy-gateway",
            "state": "UPDATE_FAILED",
            "statusMessage": null,
            "svmAdminCredential": null,
            "svmImageType": null,
            "svmIpAddress": null,
            "svmName": null,
            "systemId": null,
            "vmList": []
        }
    ]
Deployments:
    description: Details of all deployments.
    returned: when I(gather_subset) is I(deployment)
    type: list
    contains:
        id:
            description: Deployment ID.
            type: str
        deploymentName:
            description: Deployment name.
            type: str
        status:
            description: The status of deployment.
            type: str
        firmwareRepository:
            description: The firmware repository.
            type: dict
            contains:
                signature:
                    description: The signature details.
                    type: str
                downloadStatus:
                    description: The download status.
                    type: str
                rcmapproved:
                    description: If RCM approved.
                    type: bool
        allUsersAllowed:
            description: Whether the deployment is accessible to all users.
            type: bool
        assignedUsers:
            description: List of users assigned to this deployment.
            type: list
            elements: str
        brownfield:
            description: Indicates if this is a brownfield (existing infrastructure) deployment.
            type: bool
        compliant:
            description: Indicates whether the deployment is compliant with its template.
            type: bool
        configurationChange:
            description: Indicates if there has been a configuration change in the deployment.
            type: bool
        createdBy:
            description: User who created the deployment.
            type: str
        createdDate:
            description: Timestamp when the deployment was created.
            type: str
        currentBatchCount:
            description: Current batch number being processed in the deployment workflow.
            type: int
        currentStepCount:
            description: Current step number within the current batch of the deployment.
            type: int
        currentStepMessage:
            description: Message or status detail for the current step in deployment.
            type: str
        customImage:
            description: Name of the custom image used for deployment.
            type: str
        deploymentDescription:
            description: Description of the deployment.
            type: str
        deploymentDevice:
            description: List of devices involved in the deployment.
            type: list
            contains:
                brownfield:
                    description: Indicates if the device is part of a brownfield deployment.
                    type: bool
                brownfieldStatus:
                    description: Status indicating brownfield applicability for the device.
                    type: str
                cloudLink:
                    description: Indicates if CloudLink is enabled on the device.
                    type: bool
                compliantState:
                    description: Compliance state of the device (e.g., COMPLIANT, NON_COMPLIANT).
                    type: str
                componentId:
                    description: Component ID associated with the device.
                    type: str
                currentIpAddress:
                    description: Current IP address assigned to the device.
                    type: str
                dasCache:
                    description: Indicates if DAS cache is enabled on the device.
                    type: bool
                deviceGroupName:
                    description: Name of the group to which the device belongs.
                    type: str
                deviceHealth:
                    description: Health status of the device (e.g., GREEN, YELLOW, RED).
                    type: str
                deviceState:
                    description: Current state of the device in the deployment lifecycle.
                    type: str
                deviceType:
                    description: Type of device (e.g., RackServer, Switch).
                    type: str
                healthMessage:
                    description: Detailed health message for the device.
                    type: str
                ipAddress:
                    description: IP address configured for the device.
                    type: str
                logDump:
                    description: Log dump information from the device.
                    type: str
                model:
                    description: Hardware model of the device.
                    type: str
                puppetCertName:
                    description: Puppet certificate name used for managing the device.
                    type: str
                refId:
                    description: Reference ID of the device in the system.
                    type: str
                refType:
                    description: Type of reference for the device.
                    type: str
                serviceTag:
                    description: Service tag identifier of the physical device.
                    type: str
                status:
                    description: Current operational status of the device.
                    type: str
                statusEndTime:
                    description: Timestamp when the current status ended.
                    type: str
                statusMessage:
                    description: Additional message explaining the current status.
                    type: str
                statusStartTime:
                    description: Timestamp when the current status began.
                    type: str
        deploymentFinishedDate:
            description: Timestamp when the deployment was completed.
            type: str
        deploymentHealthStatusType:
            description: Aggregated health status of the deployment (e.g., green, yellow, red).
            type: str
        deploymentScheduledDate:
            description: Scheduled start time for the deployment.
            type: str
        deploymentStartedDate:
            description: Timestamp when the deployment actually started.
            type: str
        deploymentValid:
            description: Indicates if the deployment configuration is valid.
            type: bool
        deploymentValidationResponse:
            description: Detailed response from the validation process.
            type: str
        disruptiveFirmware:
            description: Indicates if firmware update is disruptive (requires reboot).
            type: bool
        firmwareInit:
            description: Indicates if firmware initialization has started.
            type: bool
        firmwareRepositoryId:
            description: ID of the firmware repository used.
            type: str
        individualTeardown:
            description: Indicates if individual components can be torn down separately.
            type: bool
        jobDetails:
            description: Details about the background job handling the deployment.
            type: str
        jobId:
            description: ID of the associated background job.
            type: str
        licenseRepository:
            description: License repository configuration used in deployment.
            type: str
        licenseRepositoryId:
            description: ID of the license repository used.
            type: str
        lifecycleMode:
            description: Indicates if the deployment is in lifecycle management mode.
            type: bool
        lifecycleModeReasons:
            description: List of reasons why lifecycle mode is active.
            type: list
            elements: str
        noOp:
            description: Indicates if the deployment is running in dry-run (no-op) mode.
            type: bool
        numberOfDeployments:
            description: Number of deployments associated with this record.
            type: int
        operationData:
            description: Additional data related to the current operation.
            type: str
        operationStatus:
            description: Status of the current operation (e.g., running, failed).
            type: str
        operationType:
            description: Type of operation being performed (e.g., RETRY, CREATE).
            type: str
        originalDeploymentId:
            description: ID of the original deployment if this is a retry or clone.
            type: str
        owner:
            description: Owner of the deployment.
            type: str
        precalculatedDeviceHealth:
            description: Pre-calculated health status of devices.
            type: str
        preconfigureSVM:
            description: Indicates if SVM (ScaleIO Volume Manager) should be preconfigured.
            type: bool
        preconfigureSVMAndUpdate:
            description: Indicates if SVM should be preconfigured and updated.
            type: bool
        removeService:
            description: Indicates if services should be removed during teardown.
            type: bool
        retry:
            description: Indicates if this deployment is a retry of a previous attempt.
            type: bool
        scaleUp:
            description: Indicates if this is a scale-up deployment.
            type: bool
        scheduleDate:
            description: Date when the deployment is scheduled to run.
            type: str
        serviceTemplate:
            description: Template used to define the structure and components of the service.
            type: dict
            contains:
                allUsersAllowed:
                    description: Whether the template is accessible to all users.
                    type: bool
                assignedUsers:
                    description: List of users assigned to use this template.
                    type: list
                    elements: str
                brownfieldTemplateType:
                    description: Type of brownfield support in the template.
                    type: str
                category:
                    description: Category of the service (e.g., block, compute).
                    type: str
                clusterCount:
                    description: Number of clusters defined in the template.
                    type: int
                components:
                    description: List of components included in the service template.
                    type: list
                    contains:
                        asmGUID:
                            description: Unique identifier for the component in ASM.
                            type: str
                        brownfield:
                            description: Indicates if the component supports brownfield deployment.
                            type: bool
                        cloned:
                            description: Indicates if the component was cloned from another.
                            type: bool
                        clonedFromAsmGuid:
                            description: ASM GUID of the source component if cloned.
                            type: str
                        clonedFromId:
                            description: ID of the source component if cloned.
                            type: str
                        componentID:
                            description: Internal ID of the component.
                            type: str
                        componentValid:
                            description: Validation result for the component.
                            type: dict
                            contains:
                                messages:
                                    description: List of validation messages.
                                    type: list
                                    elements: str
                                valid:
                                    description: Whether the component is valid.
                                    type: bool
                        configFile:
                            description: Path or name of the configuration file.
                            type: str
                        helpText:
                            description: Help text describing the component.
                            type: str
                        id:
                            description: Unique identifier for the component.
                            type: str
                        identifier:
                            description: External identifier for the component.
                            type: str
                        instances:
                            description: Number of instances of this component.
                            type: int
                        ip:
                            description: Static IP assigned to the component.
                            type: str
                        manageFirmware:
                            description: Indicates if firmware management is enabled for this component.
                            type: bool
                        managementIpAddress:
                            description: IP address used for managing the component.
                            type: str
                        name:
                            description: Name of the component.
                            type: str
                        osPuppetCertName:
                            description: Puppet certificate name for the OS layer.
                            type: str
                        puppetCertName:
                            description: Puppet certificate name for the component.
                            type: str
                        refId:
                            description: Reference ID in external systems.
                            type: str
                        resources:
                            description: List of resources allocated to the component.
                            type: list
                        serialNumber:
                            description: Serial number of the hardware component.
                            type: str
                        subType:
                            description: Sub-type of the component (e.g., STORAGEONLY).
                            type: str
                        teardown:
                            description: Indicates if the component should be removed on teardown.
                            type: bool
                        type:
                            description: Type of the component (e.g., SCALEIO).
                            type: str
                configuration:
                    description: Full configuration payload for the service.
                    type: str
                createdDate:
                    description: Timestamp when the template was created.
                    type: str
                draft:
                    description: Indicates if the template is a draft version.
                    type: bool
                hideTemplateActive:
                    description: Indicates if the template is hidden from users.
                    type: bool
                id:
                    description: Template ID.
                    type: str
                inConfiguration:
                    description: Indicates if the template is currently in use.
                    type: bool
                lastDeployedDate:
                    description: Timestamp of the last deployment using this template.
                    type: str
                licenseRepository:
                    description: License repository associated with the template.
                    type: str
                manageFirmware:
                    description: Indicates if firmware updates are managed for this template.
                    type: bool
                networks:
                    description: List of network configurations in the template.
                    type: list
                    contains:
                        description:
                            description: Description of the network.
                            type: str
                        destinationIpAddress:
                            description: Destination IP range for routing.
                            type: str
                        id:
                            description: Network ID.
                            type: str
                        name:
                            description: Name of the network.
                            type: str
                        static:
                            description: Indicates if the network uses static addressing.
                            type: bool
                        staticNetworkConfiguration:
                            description: Static network settings.
                            type: dict
                            contains:
                                dnsSuffix:
                                    description: DNS suffix for the network.
                                    type: str
                                gateway:
                                    description: Default gateway IP.
                                    type: str
                                ipAddress:
                                    description: Specific IP assigned.
                                    type: str
                                ipRange:
                                    description: Range of IPs available for allocation.
                                    type: list
                                    contains:
                                        endingIp:
                                            description: Last IP in the range.
                                            type: str
                                        id:
                                            description: ID of the IP range.
                                            type: str
                                        role:
                                            description: Role of IPs in this range.
                                            type: str
                                        startingIp:
                                            description: First IP in the range.
                                            type: str
                                primaryDns:
                                    description: Primary DNS server IP.
                                    type: str
                                secondaryDns:
                                    description: Secondary DNS server IP.
                                    type: str
                                staticRoute:
                                    description: Static route configuration.
                                    type: str
                                subnet:
                                    description: Subnet mask in dotted decimal format.
                                    type: str
                        type:
                            description: Type of network (e.g., SCALEIO_DATA).
                            type: str
                        vlanId:
                            description: VLAN ID associated with the network.
                            type: int
                originalTemplateId:
                    description: ID of the base template if this is a derived version.
                    type: str
                sdnasCount:
                    description: Number of SDNAS nodes in the template.
                    type: int
                serverCount:
                    description: Number of servers defined in the template.
                    type: int
                serviceCount:
                    description: Number of services in the template.
                    type: int
                storageCount:
                    description: Number of storage units.
                    type: int
                switchCount:
                    description: Number of switches included.
                    type: int
                templateDescription:
                    description: Description of the service template.
                    type: str
                templateLocked:
                    description: Indicates if the template is locked for editing.
                    type: bool
                templateName:
                    description: Name of the service template.
                    type: str
                templateType:
                    description: Type of template (e.g., VxRack FLEX).
                    type: str
                templateValid:
                    description: Validation status of the template.
                    type: dict
                    contains:
                        messages:
                            description: List of validation messages.
                            type: list
                            elements: str
                        valid:
                            description: Whether the template is valid.
                            type: bool
                templateVersion:
                    description: Version of the template.
                    type: str
                updatedDate:
                    description: Timestamp when the template was last updated.
                    type: str
                useDefaultCatalog:
                    description: Indicates if the default firmware catalog is used.
                    type: bool
                vmCount:
                    description: Number of virtual machines in the template.
                    type: int
        servicesDeployed:
            description: Status of services deployed (e.g., NONE, PARTIAL, ALL).
            type: str
        teardown:
            description: Indicates if the deployment is scheduled for teardown.
            type: bool
        teardownAfterCancel:
            description: Indicates if teardown should occur after cancellation.
            type: bool
        templateValid:
            description: Indicates if the associated service template is valid.
            type: bool
        totalBatchCount:
            description: Total number of batches in the deployment workflow.
            type: int
        totalNumOfSteps:
            description: Total number of steps across all batches.
            type: int
        updateServerFirmware:
            description: Indicates if server firmware should be updated during deployment.
            type: bool
        updatedBy:
            description: User who last updated the deployment.
            type: str
        updatedDate:
            description: Timestamp when the deployment was last updated.
            type: str
        useDefaultCatalog:
            description: Indicates if the default firmware catalog is used.
            type: bool
        vds:
            description: Indicates if Virtual Distributed Switches are used.
            type: bool
        vms:
            description: Virtual machine configurations or status.
            type: list
    sample: [
        {
            "allUsersAllowed": true,
            "assignedUsers": [],
            "brownfield": false,
            "compliant": false,
            "configurationChange": false,
            "createdBy": "admin",
            "createdDate": "2025-09-09T13:42:55.611+00:00",
            "currentBatchCount": null,
            "currentStepCount": null,
            "currentStepMessage": null,
            "customImage": "rcm_linux",
            "deploymentDescription": null,
            "deploymentDevice": [
                {
                    "brownfield": false,
                    "brownfieldStatus": "NOT_APPLICABLE",
                    "cloudLink": false,
                    "compliantState": "COMPLIANT",
                    "componentId": null,
                    "currentIpAddress": "10.226.197.13",
                    "dasCache": false,
                    "deviceGroupName": "Global",
                    "deviceHealth": "GREEN",
                    "deviceState": "DEPLOYING",
                    "deviceType": "RackServer",
                    "healthMessage": "OK",
                    "ipAddress": "10.226.197.13",
                    "logDump": null,
                    "model": "PowerFlex custom node R650 S",
                    "puppetCertName": "rackserver-bdwmcx3",
                    "refId": "8aaa07b2992a323a01992bc3945606cc",
                    "refType": null,
                    "serviceTag": "BDWMCX3",
                    "status": null,
                    "statusEndTime": null,
                    "statusMessage": null,
                    "statusStartTime": null
                }
            ],
            "deploymentFinishedDate": null,
            "deploymentHealthStatusType": "yellow",
            "deploymentName": "ECBlock",
            "deploymentScheduledDate": null,
            "deploymentStartedDate": "2025-09-09T14:21:11.073+00:00",
            "deploymentValid": null,
            "deploymentValidationResponse": null,
            "disruptiveFirmware": false,
            "firmwareInit": false,
            "firmwareRepository": {
                "bundleCount": 0,
                "componentCount": 0,
                "createdBy": null,
                "createdDate": null,
                "custom": false,
                "defaultCatalog": false,
                "deployments": [],
                "diskLocation": null,
                "downloadProgress": 0,
                "downloadStatus": null,
                "esxiOSRepository": null,
                "esxiSoftwareBundle": null,
                "esxiSoftwareComponent": null,
                "extractProgress": 0,
                "fileSizeInGigabytes": null,
                "filename": null,
                "id": "8aaa07b2992a323a01992bc015d30135",
                "jobId": null,
                "md5Hash": null,
                "minimal": false,
                "name": "Intelligent Catalog 50.390.00",
                "needsAttention": false,
                "password": null,
                "rcmapproved": false,
                "signature": null,
                "signedKeySourceLocation": null,
                "softwareBundles": [],
                "softwareComponents": [],
                "sourceLocation": null,
                "sourceType": null,
                "state": null,
                "updatedBy": null,
                "updatedDate": null,
                "userBundleCount": 0,
                "username": null
            },
            "firmwareRepositoryId": "8aaa07b2992a323a01992bc015d30135",
            "id": "8aaa07af992e959c01992eb7197b0150",
            "individualTeardown": false,
            "jobDetails": null,
            "jobId": null,
            "licenseRepository": null,
            "licenseRepositoryId": null,
            "lifecycleMode": false,
            "lifecycleModeReasons": [],
            "noOp": false,
            "numberOfDeployments": 0,
            "operationData": null,
            "operationStatus": null,
            "operationType": "RETRY",
            "originalDeploymentId": null,
            "owner": "admin",
            "precalculatedDeviceHealth": null,
            "preconfigureSVM": false,
            "preconfigureSVMAndUpdate": false,
            "removeService": false,
            "retry": false,
            "scaleUp": false,
            "scheduleDate": null,
            "serviceTemplate": {
                "allUsersAllowed": true,
                "assignedUsers": [],
                "blockServiceOperationsMap": {},
                "brownfieldTemplateType": "NONE",
                "category": "block",
                "clusterCount": 1,
                "components": [
                    {
                        "asmGUID": "scaleio-block-legacy-gateway",
                        "brownfield": false,
                        "cloned": false,
                        "clonedFromAsmGuid": null,
                        "clonedFromId": null,
                        "componentID": "component-scaleio-gateway-1",
                        "componentValid": {
                            "messages": [],
                            "valid": true
                        },
                        "configFile": null,
                        "helpText": null,
                        "id": "92511015-2a1e-498b-8b93-41455253dabf",
                        "identifier": null,
                        "instances": 1,
                        "ip": null,
                        "manageFirmware": false,
                        "managementIpAddress": null,
                        "name": "block-legacy-gateway",
                        "osPuppetCertName": null,
                        "puppetCertName": "scaleio-block-legacy-gateway",
                        "refId": null,
                        "relatedComponents": {
                            "068e82fc-3767-49ee-a052-f2d8cac50d87": "Storage Only Node-4",
                            "37e5ab99-ee64-4122-9eb0-92c7d76b8233": "Storage Only Node",
                            "73dda7ab-dc46-411a-aae4-99bdb0d0e47a": "Storage Only Node-2",
                            "c01f69a4-a1f9-4bba-8471-15285db1f18e": "Storage Only Node-5",
                            "fb7b47e0-5da0-497e-a579-98a9557e1682": "Storage Only Node-3"
                        },
                        "resources": [],
                        "serialNumber": null,
                        "subType": "STORAGEONLY",
                        "teardown": false,
                        "type": "SCALEIO"
                    }
                ],
                "configuration": null,
                "createdBy": null,
                "createdDate": "2025-09-09T13:43:03.001+00:00",
                "draft": false,
                "firmwareRepository": null,
                "hideTemplateActive": false,
                "id": "8aaa07af992e959c01992eb7197b0150",
                "inConfiguration": false,
                "lastDeployedDate": null,
                "licenseRepository": null,
                "manageFirmware": true,
                "networks": [
                    {
                        "description": "",
                        "destinationIpAddress": "10.230.45.0",
                        "id": "8aaa2600992a26d601992c06ec8e0021",
                        "name": "Data-345",
                        "static": true,
                        "staticNetworkConfiguration": {
                            "dnsSuffix": "pie.lab.emc.com",
                            "gateway": "10.230.45.1",
                            "ipAddress": null,
                            "ipRange": [
                                {
                                    "endingIp": "10.230.45.30",
                                    "id": "8aaa2600992a26d601992c06ec8e0022",
                                    "role": null,
                                    "startingIp": "10.230.45.21"
                                }
                            ],
                            "primaryDns": "10.230.44.169",
                            "secondaryDns": "10.230.44.170",
                            "staticRoute": null,
                            "subnet": "255.255.255.0"
                        },
                        "type": "SCALEIO_DATA",
                        "vlanId": 345
                    }
                ],
                "originalTemplateId": "e3deed3d-25ac-4154-8696-b65293213cfd",
                "sdnasCount": 0,
                "serverCount": 5,
                "serviceCount": 0,
                "storageCount": 0,
                "switchCount": 0,
                "templateDescription": "Storage Only 5 Node deployment using Erasure Coding",
                "templateLocked": false,
                "templateName": "SO NVMe Enabled Clone (8aaa07af992e959c01992eb7197b0150)",
                "templateType": "VxRack FLEX",
                "templateValid": {
                    "messages": [],
                    "valid": true
                },
                "templateVersion": "5.0.0.0",
                "updatedBy": null,
                "updatedDate": null,
                "useDefaultCatalog": false,
                "vmCount": 0
            },
            "servicesDeployed": "NONE",
            "status": "in_progress",
            "teardown": false,
            "teardownAfterCancel": false,
            "templateValid": true,
            "totalBatchCount": null,
            "totalNumOfSteps": null,
            "updateServerFirmware": true,
            "updatedBy": "system",
            "updatedDate": "2025-09-10T02:00:17.092+00:00",
            "useDefaultCatalog": false,
            "vds": false,
            "vms": null
        }
    ]
ServiceTemplates:
    description: Details of all service templates.
    returned: when I(gather_subset) is I(service_template)
    type: list
    contains:
        templateName:
            description: Template name.
            type: str
        templateDescription:
            description: Template description.
            type: str
        templateType:
            description: Template type.
            type: str
        templateVersion:
            description: Template version.
            type: str
        category:
            description: The template category.
            type: str
        serverCount:
            description: Server count.
            type: int
        allUsersAllowed:
            description: Indicates whether the template is available to all users.
            type: bool
        assignedUsers:
            description: List of users explicitly assigned to use this template.
            type: list
        brownfieldTemplateType:
            description: Type of brownfield deployment supported by the template (e.g., NONE).
            type: str
        clusterCount:
            description: Number of clusters defined in the template.
            type: int
        components:
            description: List of components included in the service template.
            type: list
            contains:
                asmGUID:
                    description: ASM GUID of the component, if applicable.
                    type: str
                brownfield:
                    description: Indicates whether the component supports brownfield deployment.
                    type: bool
                cloned:
                    description: Indicates whether the component is cloned from another.
                    type: bool
                clonedFromAsmGuid:
                    description: ASM GUID of the source component if cloned.
                    type: str
                clonedFromId:
                    description: ID of the source component if cloned.
                    type: str
                componentID:
                    description: Unique identifier for the component.
                    type: str
                componentValid:
                    description: Validation status of the component.
                    type: dict
                    contains:
                        messages:
                            description: List of validation messages.
                            type: list
                        valid:
                            description: Indicates whether the component is valid.
                            type: bool
                configFile:
                    description: Configuration file associated with the component.
                    type: str
                helpText:
                    description: Help text or description for the component.
                    type: str
                id:
                    description: Unique ID of the component instance.
                    type: str
                identifier:
                    description: Identifier for the component.
                    type: str
                instances:
                    description: Number of instances of this component.
                    type: int
                ip:
                    description: IP address assigned to the component.
                    type: str
                manageFirmware:
                    description: Indicates whether firmware management is enabled for the component.
                    type: bool
                managementIpAddress:
                    description: Management IP address of the component.
                    type: str
                name:
                    description: Name of the component (e.g., PowerFlex Cluster).
                    type: str
                osPuppetCertName:
                    description: Puppet certificate name for the OS instance.
                    type: str
                puppetCertName:
                    description: Puppet certificate name for the component.
                    type: str
                refId:
                    description: Reference ID of the component.
                    type: str
                resources:
                    description: List of resources associated with the component.
                    type: list
                serialNumber:
                    description: Serial number of the component.
                    type: str
                subType:
                    description: Subtype of the component (e.g., STORAGEONLY).
                    type: str
                teardown:
                    description: Indicates whether the component should be torn down.
                    type: bool
                type:
                    description: Type of the component (e.g., SCALEIO).
                    type: str
        configuration:
            description: Full configuration data of the service template.
            type: str
        createdBy:
            description: User who created the service template.
            type: str
        createdDate:
            description: Timestamp when the template was created.
            type: str
        draft:
            description: Indicates whether the template is a draft.
            type: bool
        firmwareRepository:
            description: Firmware repository used by the template.
            type: str
        hideTemplateActive:
            description: Indicates whether the template is hidden from users.
            type: bool
        id:
            description: Unique identifier of the service template.
            type: str
        inConfiguration:
            description: Indicates whether the template is currently being configured.
            type: bool
        lastDeployedDate:
            description: Timestamp when the template was last deployed.
            type: str
        licenseRepository:
            description: License repository used by the template.
            type: str
        manageFirmware:
            description: Indicates whether firmware management is enabled for the template.
            type: bool
        networks:
            description: List of network configurations defined in the template.
            type: list
            contains:
                description:
                    description: Description of the network.
                    type: str
                destinationIpAddress:
                    description: Destination IP address range for the network.
                    type: str
                id:
                    description: Unique ID of the network.
                    type: str
                name:
                    description: Name of the network (e.g., flex-data1).
                    type: str
                static:
                    description: Indicates whether the network uses static configuration.
                    type: bool
                staticNetworkConfiguration:
                    description: Static network settings for the network.
                    type: dict
                    contains:
                        dnsSuffix:
                            description: DNS suffix for the network.
                            type: str
                        gateway:
                            description: Gateway IP address.
                            type: str
                        ipAddress:
                            description: Assigned IP address.
                            type: str
                        ipRange:
                            description: Range of IP addresses.
                            type: str
                        primaryDns:
                            description: Primary DNS server IP.
                            type: str
                        secondaryDns:
                            description: Secondary DNS server IP.
                            type: str
                        staticRoute:
                            description: Static routing configuration.
                            type: str
                        subnet:
                            description: Subnet mask in dotted-decimal format.
                            type: str
                type:
                    description: Type of the network (e.g., SCALEIO_DATA).
                    type: str
                vlanId:
                    description: VLAN ID associated with the network.
                    type: int
        originalTemplateId:
            description: ID of the original template from which this was derived.
            type: str
        sdnasCount:
            description: Number of SDNAS instances in the template.
            type: int
        serviceCount:
            description: Number of services defined in the template.
            type: int
        storageCount:
            description: Number of storage components in the template.
            type: int
        switchCount:
            description: Number of switch components in the template.
            type: int
        templateLocked:
            description: Indicates whether the template is locked for editing.
            type: bool
        templateValid:
            description: Validation status of the entire template.
            type: dict
            contains:
                messages:
                    description: List of validation messages.
                    type: list
                valid:
                    description: Indicates whether the template is valid.
                    type: bool
        updatedBy:
            description: User who last updated the template.
            type: str
        updatedDate:
            description: Timestamp when the template was last updated.
            type: str
        useDefaultCatalog:
            description: Indicates whether the default firmware catalog is used.
            type: bool
        vmCount:
            description: Number of virtual machines defined in the template.
            type: int
    sample: [
        {
            "allUsersAllowed": false,
            "assignedUsers": [],
            "blockServiceOperationsMap": {},
            "brownfieldTemplateType": "NONE",
            "category": "Sample Templates",
            "clusterCount": 1,
            "components": [
                {
                    "asmGUID": null,
                    "brownfield": false,
                    "cloned": false,
                    "clonedFromAsmGuid": null,
                    "clonedFromId": null,
                    "componentID": "component-scaleio-gateway-1",
                    "componentValid": {
                        "messages": [],
                        "valid": true
                    },
                    "configFile": null,
                    "helpText": null,
                    "id": "f9adcdba-e0e7-4977-938e-9e5ca626d037",
                    "identifier": null,
                    "instances": 1,
                    "ip": null,
                    "manageFirmware": false,
                    "managementIpAddress": null,
                    "name": "PowerFlex Cluster",
                    "osPuppetCertName": null,
                    "puppetCertName": null,
                    "refId": null,
                    "relatedComponents": {
                        "db582229-d23e-4ce2-b242-ecfc17f1c16b": "Storage Only Node"
                    },
                    "resources": [],
                    "serialNumber": null,
                    "subType": "STORAGEONLY",
                    "teardown": false,
                    "type": "SCALEIO"
                }
            ],
            "configuration": null,
            "createdBy": "system",
            "createdDate": "2025-08-22T15:48:20.369+00:00",
            "draft": false,
            "firmwareRepository": null,
            "hideTemplateActive": true,
            "id": "4d0468be-6827-4c41-bbaf-01086de116a8",
            "inConfiguration": false,
            "lastDeployedDate": null,
            "licenseRepository": null,
            "manageFirmware": true,
            "networks": [
                {
                    "description": "",
                    "destinationIpAddress": "192.168.104.0",
                    "id": "ff80808177f8823b0177f8ba236b0004",
                    "name": "flex-data1",
                    "static": true,
                    "staticNetworkConfiguration": {
                        "dnsSuffix": null,
                        "gateway": null,
                        "ipAddress": null,
                        "ipRange": null,
                        "primaryDns": null,
                        "secondaryDns": null,
                        "staticRoute": null,
                        "subnet": "255.255.255.0"
                    },
                    "type": "SCALEIO_DATA",
                    "vlanId": 104
                }
            ],
            "originalTemplateId": "ff80808177f880fc0177f883bf1e0027",
            "sdnasCount": 0,
            "serverCount": 4,
            "serviceCount": 0,
            "storageCount": 0,
            "switchCount": 0,
            "templateDescription": "Storage Only 4 Node deployment with 100Gb networking",
            "templateLocked": true,
            "templateName": "Mirroring - Storage 100Gb - 2 Data - LACP",
            "templateType": "VxRack FLEX",
            "templateValid": {
                "messages": [],
                "valid": true
            },
            "templateVersion": "5.0.0-2956",
            "updatedBy": null,
            "updatedDate": null,
            "useDefaultCatalog": true,
            "vmCount": 0
        }
    ]
FirmwareRepository:
    description: Details of all firmware repository.
    returned: when I(gather_subset) is C(firmware_repository)
    type: list
    contains:
        id:
            description: ID of the firmware repository.
            type: str
        name:
            description: Name of the firmware repository.
            type: str
        sourceLocation:
            description: Source location of the firmware repository.
            type: str
        state:
            description: State of the firmware repository.
            type: str
        softwareComponents:
            description: Software components of the firmware repository.
            type: list
        softwareBundles:
            description: Software bundles of the firmware repository.
            type: list
        deployments:
            description: Deployments of the firmware repository.
            type: list
        bundleCount:
            description: Total number of bundles in the firmware repository.
            type: int
        componentCount:
            description: Total number of software components in the firmware repository.
            type: int
        createdBy:
            description: User who created the firmware repository.
            type: str
        createdDate:
            description: Timestamp when the firmware repository was created.
            type: str
        custom:
            description: Indicates whether the firmware repository is a custom catalog.
            type: bool
        defaultCatalog:
            description: Indicates whether this is the default firmware catalog.
            type: bool
        diskLocation:
            description: Disk path or URL where the firmware repository is stored.
            type: str
        downloadProgress:
            description: Progress percentage of the download process.
            type: int
        downloadStatus:
            description: Current status of the download (e.g., available).
            type: str
        esxiOSRepository:
            description: ESXi operating system repository, if applicable.
            type: str
        esxiSoftwareBundle:
            description: ESXi software bundle included in the repository.
            type: str
        esxiSoftwareComponent:
            description: ESXi software component included in the repository.
            type: str
        extractProgress:
            description: Progress percentage of the extraction process.
            type: int
        fileSizeInGigabytes:
            description: Size of the firmware repository in gigabytes.
            type: float
        filename:
            description: Name of the catalog file (e.g., catalog.xml).
            type: str
        jobId:
            description: Job ID associated with the firmware repository creation or update.
            type: str
        md5Hash:
            description: MD5 hash of the firmware repository file.
            type: str
        minimal:
            description: Indicates whether the repository is a minimal catalog.
            type: bool
        needsAttention:
            description: Indicates whether the repository requires user attention.
            type: bool
        password:
            description: Password used to access the source location, if applicable.
            type: str
        rcmapproved:
            description: Indicates whether the repository is RCM (Recommended Configuration Management) approved.
            type: bool
        signature:
            description: Signature status of the catalog (e.g., Signed).
            type: str
        signedKeySourceLocation:
            description: Source location of the signed key for catalog verification.
            type: str
        sourceType:
            description: Type of source (e.g., FILE).
            type: str
        updatedBy:
            description: User who last updated the firmware repository.
            type: str
        updatedDate:
            description: Timestamp when the firmware repository was last updated.
            type: str
        userBundleCount:
            description: Number of user-defined bundles in the repository.
            type: int
        username:
            description: Username used to access the source location.
            type: str
    sample: [
        {
            "bundleCount": 54,
            "componentCount": 2783,
            "createdBy": "admin",
            "createdDate": "2025-08-26T06:46:30.994+00:00",
            "custom": false,
            "defaultCatalog": true,
            "deployments": [],
            "diskLocation": "https://xxxx",
            "downloadProgress": 100,
            "downloadStatus": "available",
            "esxiOSRepository": null,
            "esxiSoftwareBundle": null,
            "esxiSoftwareComponent": null,
            "extractProgress": 100,
            "fileSizeInGigabytes": 21.7,
            "filename": "catalog.xml",
            "id": "8aaa80a998e515080198e520d5520000",
            "jobId": "Job-a3129599-9702-4abc-b041-0724b82087bc",
            "md5Hash": null,
            "minimal": false,
            "name": "Intelligent Catalog 50.390.00",
            "needsAttention": false,
            "password": null,
            "rcmapproved": false,
            "signature": "Signed",
            "signedKeySourceLocation": null,
            "softwareBundles": [],
            "softwareComponents": [],
            "sourceLocation": "https://xxx.zip",
            "sourceType": "FILE",
            "state": "available",
            "updatedBy": "system",
            "updatedDate": "2025-09-03T05:52:58.636+00:00",
            "userBundleCount": 0,
            "username": ""
        }
    ]
NVMe_Hosts:
    description: Details of all NVMe hosts.
    returned: always
    type: list
    contains:
        hostOsFullType:
            description: Full type of the host OS.
            type: str
        hostType:
            description: Type of the host.
            type: str
        id:
            description: ID of the NVMe host.
            type: str
        installedSoftwareVersionInfo:
            description: Installed software version information.
            type: str
        kernelBuildNumber:
            description: Kernel build number.
            type: str
        kernelVersion:
            description: Kernel version.
            type: str
        links:
            description: Links related to the NVMe host.
            type: list
            contains:
                href:
                    description: Hyperlink reference.
                    type: str
                rel:
                    description: Relation type.
                    type: str
        max_num_paths:
            description: Maximum number of paths per volume. Used to create or modify the NVMe host.
            type: int
        max_num_sys_ports:
            description: Maximum number of ports per protection domain. Used to create or modify the NVMe host.
            type: int
        mdmConnectionState:
            description: MDM connection state.
            type: str
        mdmIpAddressesCurrent:
            description: Current MDM IP addresses.
            type: list
        memoryAllocationFailure:
            description: Memory allocation failure status.
            type: str
        name:
            description: Name of the NVMe host.
            type: str
        nqn:
            description: NQN of the NVMe host. Used to create, get or modify the NVMe host.
            type: str
        osType:
            description: OS type.
            type: str
        peerMdmId:
            description: Peer MDM ID.
            type: str
        perfProfile:
            description: Performance profile.
            type: str
        sdcAgentActive:
            description: Whether the SDC agent is active.
            type: bool
        sdcApproved:
            description: Whether an SDC has approved access to the system.
            type: bool
        sdcApprovedIps:
            description: SDC approved IPs.
            type: list
        sdcGuid:
            description: SDC GUID.
            type: str
        sdcIp:
            description: SDC IP address.
            type: str
        sdcIps:
            description: SDC IP addresses.
            type: list
        sdcType:
            description: SDC type.
            type: str
        sdrId:
            description: SDR ID.
            type: str
        sdtId:
            description: SDT ID.
            type: str
        socketAllocationFailure:
            description: Socket allocation failure status.
            type: str
        softwareVersionInfo:
            description: Software version information.
            type: str
        systemId:
            description: ID of the system.
            type: str
        versionInfo:
            description: Version information.
            type: str
    sample: [
        {
            "hostOsFullType": "Generic",
            "hostType": "NVMeHost",
            "id": "fdc0ed2b00010000",
            "installedSoftwareVersionInfo": null,
            "kernelBuildNumber": null,
            "kernelVersion": null,
            "links": [
                {
                    "href": "/api/instances/Host::fdc0ed2b00010000",
                    "rel": "self"
                }
            ],
            "maxNumPaths": 4,
            "maxNumSysPorts": 10,
            "mdmConnectionState": null,
            "mdmIpAddressesCurrent": null,
            "memoryAllocationFailure": null,
            "name": "nvme_host",
            "nqn": "nqn.2014-08.org.nvmexpress:uuid:e6e80a42-b1d3-5ec2-5ba6-d46d4df291234",
            "osType": null,
            "peerMdmId": null,
            "perfProfile": null,
            "sdcAgentActive": null,
            "sdcApproved": null,
            "sdcApprovedIps": null,
            "sdcGuid": null,
            "sdcIp": null,
            "sdcIps": null,
            "sdcType": null,
            "sdrId": null,
            "sdtId": null,
            "socketAllocationFailure": null,
            "softwareVersionInfo": null,
            "systemId": "815945c41cd8460f",
            "versionInfo": null
        }
    ]
sdt:
    description: Details of NVMe storage data targets.
    returned: when I(gather_subset) is C(sdt)
    type: list
    contains:
        authenticationError:
            description: The authentication error details of the SDT object.
            type: str
        certificateInfo:
            description: The certificate information of the SDT object.
            type: dict
            contains:
                issuer:
                    description: The issuer of the certificate.
                    type: str
                subject:
                    description: The subject of the certificate.
                    type: str
                thumbprint:
                    description: The thumbprint of the certificate.
                    type: str
                validFrom:
                    description: The date from which the certificate is valid.
                    type: str
                validFromAsn1Format:
                    description: The validity start date in ASN.1 format.
                    type: str
                validTo:
                    description: The date until which the certificate is valid.
                    type: str
                validToAsn1Format:
                    description: The validity end date in ASN.1 format.
                    type: str
        discoveryPort:
            description: The discovery port number of the SDT object.
            type: int
        faultSetId:
            description: The fault set ID associated with the SDT object.
            type: str
        id:
            description: The unique identifier of the SDT object.
            type: str
        ipList:
            description: The list of IP addresses of the SDT object.
            type: list
            contains:
                ip:
                    description: The IP address of the SDT object.
                    type: str
                role:
                    description: The role associated with the IP address of the SDT object.
                    type: str
        links:
            description: Hyperlinks related to the SDT object.
            type: list
            contains:
                href:
                    description: The URL of the link.
                    type: str
                rel:
                    description: The relation type of the link.
                    type: str
        maintenanceState:
            description: The maintenance state of the SDT object.
            type: str
        mdmConnectionState:
            description: The MDM connection state of the SDT object.
            type: str
        membershipState:
            description: The membership state of the SDT object.
            type: str
        name:
            description: The name of the SDT object.
            type: str
        nvmePort:
            description: The NVMe port number of the SDT object.
            type: int
        nvme_hosts:
            description: The list of NVMe hosts associated with the SDT object.
            type: list
            contains:
                controllerId:
                    description: The controller ID.
                    type: int
                hostId:
                    description: The host ID associated with the NVMe controller.
                    type: str
                hostIp:
                    description: The IP address of the host.
                    type: str
                id:
                    description: The unique identifier of the NVMe controller.
                    type: str
                isAssigned:
                    description: Indicates if the NVMe controller is assigned.
                    type: bool
                isConnected:
                    description: Indicates if the NVMe controller is connected.
                    type: bool
                links:
                    description: Hyperlinks related to the NVMe controller.
                    type: list
                    contains:
                        href:
                            description: The URL of the link.
                            type: str
                        rel:
                            description: The relation type of the link.
                            type: str
                name:
                    description: The name of the NVMe controller. Can be null.
                    type: str
                sdtId:
                    description: The SDT ID associated with the NVMe controller.
                    type: str
                subsystem:
                    description: The subsystem associated with the NVMe controller.
                    type: str
                sysPortId:
                    description: The system port ID.
                    type: int
                sysPortIp:
                    description: The IP address of the system port.
                    type: str
        persistentDiscoveryControllersNum:
            description: Number of persistent discovery controllers.
            type: int
        protectionDomainId:
            description: The Protection Domain ID associated with the SDT object.
            type: str
        sdtState:
            description: The state of the SDT object.
            type: str
        softwareVersionInfo:
            description: The software version information of the SDT object.
            type: str
        storagePort:
            description: The storage port number of the SDT object.
            type: int
        systemId:
            description: ID of the system.
            type: str
    sample: [
        {
            "authenticationError": "None",
            "certificateInfo": {
                "issuer": "/GN=MDM/CN=CA-db69bee9dc6c0d0f/L=Hopkinton/ST=Massachusetts/C=US/O=EMC/OU=ASD",
                "subject": "/GN=sdt-comp-1/CN=pie104074/L=Hopkinton/ST=Massachusetts/C=US/O=EMC/OU=ASD",
                "thumbprint": "51:5E:FB:ED:91:43:54:8C:46:C3:60:ED:AD:0A:60:5E:90:3E:30:2D",
                "validFrom": "Sep  8 15:37:05 2025 GMT",
                "validFromAsn1Format": "250908153705Z",
                "validTo": "Sep  7 16:37:05 2035 GMT",
                "validToAsn1Format": "350907163705Z"
            },
            "discoveryPort": 8009,
            "faultSetId": null,
            "id": "19b7d6c700000001",
            "ipList": [
                {
                    "ip": "10.2.3.4",
                    "role": "StorageAndHost"
                },
                {
                    "ip": "10.1.2.3",
                    "role": "StorageAndHost"
                }
            ],
            "links": [
                {
                    "href": "/api/instances/Sdt::19b7d6c700000001",
                    "rel": "self"
                }
            ],
            "maintenanceState": "NoMaintenance",
            "mdmConnectionState": "Connected",
            "membershipState": "Joined",
            "name": "sdt_pie104074.pie.lab.emc.com",
            "nvmePort": 4420,
            "nvme_hosts": [],
            "persistentDiscoveryControllersNum": 0,
            "protectionDomainId": "19af22f800000000",
            "sdtState": "Normal",
            "softwareVersionInfo": "R5_0.0.0",
            "storagePort": 12200,
            "systemId": "db69bee9dc6c0d0f"
        }
    ]
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import powerflex_compatibility
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
import re

LOG = utils.get_logger('info_v2')

UNSUPPORTED_SUBSET_FOR_VERSION = 'One or more specified subset is not supported for the PowerFlex version.'
POWERFLEX_MANAGER_GATHER_SUBSET = {'managed_device', 'deployment', 'service_template'}
MIN_SUPPORTED_POWERFLEX_MANAGER_VERSION = 5.0
ERROR_CODES = r'PARSE002|FILTER002|FILTER003'


@powerflex_compatibility(min_ver='5.0', predecessor='info')
class PowerFlexInfo(PowerFlexBase):
    """Class with Info operations"""

    filter_mapping = {'equal': 'eq', 'contains': 'co'}

    def __init__(self):
        """ Define all parameters required by this module"""
        argument_spec = get_powerflex_info_parameters()
        module_params = {
            'argument_spec': argument_spec,
            'supports_check_mode': False,
        }
        self.filter_keys = sorted(
            [k for k in argument_spec['filters']['options'].keys()
             if 'filter' in k])
        super().__init__(AnsibleModule, module_params)
        super().check_module_compatibility()

    def get_api_details(self):
        """ Get api details of the array """
        try:
            LOG.info('Getting API details ')
            api_version = self.powerflex_conn.system.api_version(cached=True)
            return api_version

        except Exception as e:
            msg = f'Get API details from Powerflex array failed with error {str(e)}'
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
            msg = f'Get array details from Powerflex array failed with error {str(e)}'
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
            # filter out NVMe host entities
            sdc = [obj for obj in sdc if obj.get('hostType') != 'NVMeHost']
            return result_list(sdc)

        except Exception as e:
            msg = f'Get SDC list from powerflex array failed with error {str(e)}'
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_nvme_host_list(self, filter_dict=None):
        """ Get the list of NVMe hosts on a given PowerFlex storage system """

        try:
            LOG.info('Getting NVMe hosts list ')
            sdc = self.powerflex_conn.sdc.get()
            # filter out NVMe host entities
            hosts = [obj for obj in sdc if obj.get('hostType') == 'NVMeHost']
            # Add name to NVMe hosts without giving name
            for host in hosts:
                if host.get("name") is None:
                    host["name"] = f"NVMeHost:{host['id']}"
            if filter_dict:
                hosts = utils.filter_response(hosts, filter_dict)
            return result_list(hosts)

        except Exception as e:
            msg = f'Get NVMe host list from powerflex array failed with error {str(e)}'
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
            msg = f'Get protection domain list from powerflex array failed with error {str(e)}'
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

            if pool:
                resources = self.powerflex_conn.utility.query_metrics('storage_pool', [], []).get("resources", [])
                resource_map = {res["id"]: res["metrics"] for res in resources}
                for item in pool:
                    item['statistics'] = resource_map[item['id']] if item['id'] in resource_map else {}
            return result_list(pool)

        except Exception as e:
            msg = f'Get storage pool list from powerflex array failed with error {str(e)}'
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

            if volumes:
                resources = self.powerflex_conn.utility.query_metrics('volume', [], []).get("resources", [])
                resource_map = {res["id"]: res["metrics"] for res in resources}
                for item in volumes:
                    item['statistics'] = resource_map[item['id']] if item['id'] in resource_map else {}
            return result_list(volumes)

        except Exception as e:
            msg = f'Get volumes list from powerflex array failed with error {str(e)}'
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_snapshot_policy_list(self, filter_dict=None):
        """ Get the list of snapshot schedules on a given PowerFlex storage
            system """

        try:
            LOG.info('Getting snapshot policies list ')
            if filter_dict:
                snapshot_policies = \
                    self.powerflex_conn.snapshot_policy.get(
                        filter_fields=filter_dict)
            else:
                snapshot_policies = \
                    self.powerflex_conn.snapshot_policy.get()
            return result_list(snapshot_policies)

        except Exception as e:
            msg = f'Get snapshot policies list from powerflex array failed with error {str(e)}'
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
            msg = f'Get device list from powerflex array failed with error {str(e)}'
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_managed_devices_list(self):
        """ Get the list of managed devices on a given PowerFlex Manager system """
        try:
            LOG.info('Getting managed devices list ')
            devices = self.powerflex_conn.managed_device.get(filters=self.populate_filter_list(),
                                                             limit=self.get_param_value('limit'),
                                                             offset=self.get_param_value('offset'),
                                                             sort=self.get_param_value('sort'))
            return devices
        except Exception as e:
            msg = f'Get managed devices from PowerFlex Manager failed with error {str(e)}'
            return self.handle_error_exit(msg)

    def get_deployments_list(self):
        """ Get the list of deployments on a given PowerFlex Manager system """
        try:
            LOG.info('Getting deployments list ')
            deployments = self.powerflex_conn.deployment.get(filters=self.populate_filter_list(),
                                                             sort=self.get_param_value('sort'),
                                                             limit=self.get_param_value('limit'),
                                                             offset=self.get_param_value('offset'),
                                                             include_devices=self.get_param_value('include_devices'),
                                                             include_template=self.get_param_value('include_template'),
                                                             full=self.get_param_value('full'))
            return deployments
        except Exception as e:
            msg = f'Get deployments from PowerFlex Manager failed with error {str(e)}'
            return self.handle_error_exit(msg)

    def get_sdt_list(self, filter_dict=None):
        """ Get the list of sdt on a given PowerFlex Manager system """
        try:
            LOG.info('Getting sdt list ')
            # Get the list of nvme hosts
            associated_hosts = []
            nvme_hosts = self.powerflex_conn.sdc.get(filter_fields={'hostType': "NVMeHost"})
            for nvme_host in nvme_hosts:
                controller = self.powerflex_conn.host.get_related(entity_id=nvme_host.get('id'), related='NvmeController')
                associated_hosts.extend(controller)
            associated_hosts_map = {controller.get('sdtId'): controller for controller in associated_hosts if controller.get('sdtId') is not None}
            if filter_dict:
                sdts = self.powerflex_conn.sdt.get(filter_fields=filter_dict)
            else:
                sdts = self.powerflex_conn.sdt.get()

            for sdt in sdts:
                sdt['nvme_hosts'] = []
                for host in associated_hosts_map.values():
                    if host.get('sdtId') == sdt.get('id'):
                        sdt['nvme_hosts'].append(host)

            return result_list(sdts)

        except Exception as e:
            msg = f'Get sdt from PowerFlex Manager failed with error {str(e)}'
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_pagination_params(self):
        """ Get the pagination parameters """
        return {'limit': self.get_param_value('limit'), 'offset': self.get_param_value('offset'),
                'sort': self.get_param_value('sort'), 'filters': self.populate_filter_list()}

    def get_firmware_repository_list(self):
        """ Get the list of firmware repository on a given PowerFlex Manager system """
        try:
            LOG.info('Getting firmware repository list ')
            firmware_repository = self.powerflex_conn.firmware_repository.get(
                **self.get_pagination_params(),
                bundles=self.get_param_value('include_bundles'))
            return firmware_repository
        except Exception as e:
            msg = f'Get firmware repository from PowerFlex Manager failed with error {str(e)}'
            return self.handle_error_exit(msg)

    def get_service_templates_list(self):
        """ Get the list of service templates on a given PowerFlex Manager system """
        try:
            LOG.info('Getting service templates list ')
            service_templates = self.powerflex_conn.service_template.get(filters=self.populate_filter_list(),
                                                                         sort=self.get_param_value('sort'),
                                                                         offset=self.get_param_value('offset'),
                                                                         limit=self.get_param_value('limit'),
                                                                         full=self.get_param_value('full'),
                                                                         include_attachments=self.get_param_value('include_attachments'))
            return service_templates
        except Exception as e:
            msg = f'Get service templates from PowerFlex Manager failed with error {str(e)}'
            return self.handle_error_exit(msg)

    def handle_error_exit(self, detailed_message):
        match = re.search(r"displayMessage=([^']+)", detailed_message)
        error_message = match.group(1) if match else detailed_message
        LOG.error(error_message)
        if re.search(ERROR_CODES, detailed_message):
            return []
        self.module.fail_json(msg=error_message)

    def get_param_value(self, param):
        """
        Get the value of the given parameter.
        Args:
            param (str): The parameter to get the value for.
        Returns:
            The value of the parameter if it is different from the default value,
            The value of the parameter if int and greater than 0
            otherwise None.
        """
        if param in ('sort', 'offset', 'limit') and len(self.module.params.get('gather_subset')) > 1:
            return None
        default_value = self.module.argument_spec.get(param).get('default')
        param_value = self.module.params.get(param)
        if (default_value != param_value) and (param_value >= 0 if isinstance(param_value, int) else True):
            return param_value
        return None

    def validate_filter(self, filter_dict):
        """ Validate given filter_dict """

        is_invalid_filter = self.filter_keys != sorted(list(filter_dict))
        if is_invalid_filter:
            msg = "Filter should have all keys: '{0}'".format(
                ", ".join(self.filter_keys))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

        is_invalid_filter = [filter_dict[i] is None for i in filter_dict]
        if True in is_invalid_filter:
            msg = "Filter keys: '{0}' cannot be None".format(self.filter_keys)
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def populate_filter_list(self):
        """Populate the filter list"""
        if len(self.module.params.get('gather_subset')) > 1:
            return []
        filters = self.module.params.get('filters') or []
        return [
            f'{self.filter_mapping.get(filter_dict["filter_operator"])},{filter_dict["filter_key"]},{filter_dict["filter_value"]}'
            for filter_dict in filters
        ]

    def get_filters(self, filters):
        """Get the filters to be applied"""

        filter_dict = {}
        for item in filters:
            self.validate_filter(item)
            f_op = item['filter_operator']
            if self.filter_mapping.get(f_op) == self.filter_mapping.get("equal"):
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
        return filter_dict

    def validate_subset(self, api_version, subset):
        if float(api_version) < MIN_SUPPORTED_POWERFLEX_MANAGER_VERSION and subset and set(subset).issubset(POWERFLEX_MANAGER_GATHER_SUBSET):
            self.module.exit_json(msg=UNSUPPORTED_SUBSET_FOR_VERSION, skipped=True)

    def perform_module_operation(self):
        """ Perform different actions on info_v2 based on user input
            in the playbook """

        filters = self.module.params['filters']
        filter_dict = {}
        if filters:
            filter_dict = self.get_filters(filters)
            LOG.info('filters: %s', filter_dict)

        api_version = self.get_api_details()
        array_details = self.get_array_details()
        subset = self.module.params['gather_subset']
        subset_result_filter = {}
        subset_result_wo_param = {}
        self.validate_subset(api_version, subset)

        subset_dict_with_filter = {
            "sdc": self.get_sdc_list,
            "protection_domain": self.get_pd_list,
            "storage_pool": self.get_storage_pool_list,
            "vol": self.get_volumes_list,
            "snapshot_policy": self.get_snapshot_policy_list,
            "device": self.get_devices_list,
            "nvme_host": self.get_nvme_host_list,
            "sdt": self.get_sdt_list,
        }

        subset_wo_param = {
            "managed_device": self.get_managed_devices_list,
            "service_template": self.get_service_templates_list,
            "deployment": self.get_deployments_list,
            "firmware_repository": self.get_firmware_repository_list
        }
        if subset:
            subset_result_filter = {key: subset_dict_with_filter[key](
                filter_dict=filter_dict) for key in subset if key in subset_dict_with_filter}
            subset_result_wo_param = {key: subset_wo_param[key](
            ) for key in subset if key in subset_wo_param}

        self.module.exit_json(
            Array_Details=array_details,
            API_Version=api_version,
            SDCs=subset_result_filter.get("sdc", []),
            Storage_Pools=subset_result_filter.get("storage_pool", []),
            Volumes=subset_result_filter.get("vol", []),
            Snapshot_Policies=subset_result_filter.get("snapshot_policy", []),
            Protection_Domains=subset_result_filter.get(
                "protection_domain", []),
            Devices=subset_result_filter.get("device", []),
            SDTs=subset_result_filter.get("sdt", []),
            ManagedDevices=subset_result_wo_param.get("managed_device", []),
            ServiceTemplates=subset_result_wo_param.get(
                "service_template", []),
            Deployments=subset_result_wo_param.get("deployment", []),
            FirmwareRepository=subset_result_wo_param.get(
                "firmware_repository", []),
            NVMeHosts=subset_result_filter.get("nvme_host", [])
        )


def result_list(entity):
    """ Get the name and id associated with the PowerFlex entities """
    result = []
    if entity:
        LOG.info('Successfully listed.')
        for item in entity:
            if item['name']:
                result.append(item)
            else:
                result.append({"id": item['id']})
        return result
    else:
        return None


def get_powerflex_info_parameters():
    """This method provides parameters required for the ansible
    info_v2 module on powerflex"""
    return dict(
        gather_subset=dict(type='list', required=False, elements='str',
                           choices=['vol', 'storage_pool', 'protection_domain', 'sdc',
                                    'sdt', 'snapshot_policy', 'device', 'nvme_host',
                                    'service_template', 'managed_device', 'deployment', 'firmware_repository']),
        filters=dict(type='list', required=False, elements='dict',
                     options=dict(filter_key=dict(type='str', required=True, no_log=False),
                                  filter_operator=dict(
                                      type='str', required=True,
                                      choices=['equal', 'contains']),
                                  filter_value=dict(type='str', required=True)
                                  )),
        sort=dict(type='str'),
        limit=dict(type='int', default=50),
        offset=dict(type='int', default=0),
        include_devices=dict(type='bool', default=True),
        include_template=dict(type='bool', default=True),
        full=dict(type='bool', default=False),
        include_attachments=dict(type='bool', default=True),
        include_bundles=dict(type='bool', default=False),
    )


def main():
    """ Create PowerFlex info_v2 object and perform action on it
        based on user input from playbook"""
    obj = PowerFlexInfo()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
