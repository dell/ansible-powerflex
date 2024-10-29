# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of info module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storagepool_api import MockStoragePoolApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_volume_api import MockVolumeApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_replication_consistency_group_api \
    import MockReplicationConsistencyGroupApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_replication_pair_api \
    import MockReplicationPairApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_snapshot_policy_api \
    import MockSnapshotPolicyApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fault_set_api import MockFaultSetApi


__metaclass__ = type


class MockInfoApi:
    MODULE_UTILS_PATH = "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"
    INFO_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "gather_subset": [],
        "filters": None
    }

    DUMMY_IP = 'xx.xx.xx.xx'
    INFO_ARRAY_DETAILS = [
        {
            'systemVersionName': 'DellEMC PowerFlex Version',
            'perfProfile': 'Compact',
            'authenticationMethod': 'Native',
            'capacityAlertHighThresholdPercent': 80,
            'capacityAlertCriticalThresholdPercent': 90,
            'upgradeState': 'NoUpgrade',
            'remoteReadOnlyLimitState': False,
            'mdmManagementPort': 6611,
            'mdmExternalPort': 7611,
            'sdcMdmNetworkDisconnectionsCounterParameters': {
                'shortWindow': {
                    'threshold': 300,
                    'windowSizeInSec': 60
                },
                'mediumWindow': {
                    'threshold': 500,
                    'windowSizeInSec': 3600
                },
                'longWindow': {
                    'threshold': 700,
                    'windowSizeInSec': 86400
                }
            },
            'sdcSdsNetworkDisconnectionsCounterParameters': {
                'shortWindow': {
                    'threshold': 800,
                    'windowSizeInSec': 60
                },
                'mediumWindow': {
                    'threshold': 4000,
                    'windowSizeInSec': 3600
                },
                'longWindow': {
                    'threshold': 20000,
                    'windowSizeInSec': 86400
                }
            },
            'sdcMemoryAllocationFailuresCounterParameters': {
                'shortWindow': {
                    'threshold': 300,
                    'windowSizeInSec': 60
                },
                'mediumWindow': {
                    'threshold': 500,
                    'windowSizeInSec': 3600
                },
                'longWindow': {
                    'threshold': 700,
                    'windowSizeInSec': 86400
                }
            },
            'sdcSocketAllocationFailuresCounterParameters': {
                'shortWindow': {
                    'threshold': 300,
                    'windowSizeInSec': 60
                },
                'mediumWindow': {
                    'threshold': 500,
                    'windowSizeInSec': 3600
                },
                'longWindow': {
                    'threshold': 700,
                    'windowSizeInSec': 86400
                }
            },
            'sdcLongOperationsCounterParameters': {
                'shortWindow': {
                    'threshold': 10000,
                    'windowSizeInSec': 60
                },
                'mediumWindow': {
                    'threshold': 100000,
                    'windowSizeInSec': 3600
                },
                'longWindow': {
                    'threshold': 1000000,
                    'windowSizeInSec': 86400
                }
            },
            'cliPasswordAllowed': True,
            'managementClientSecureCommunicationEnabled': True,
            'tlsVersion': 'TLSv1.2',
            'showGuid': True,
            'defragmentationEnabled': True,
            'mdmSecurityPolicy': 'None',
            'mdmCluster': {
                'clusterState': 'ClusteredNormal',
                'clusterMode': 'ThreeNodes',
                'slaves': [
                    {
                        'managementIPs': [
                            DUMMY_IP
                        ],
                        'ips': [
                            DUMMY_IP
                        ],
                        'versionInfo': '',
                        'virtualInterfaces': [
                            ''
                        ],
                        'opensslVersion': 'OpenSSL 26 Jan 2017',
                        'role': 'Manager',
                        'status': 'Normal',
                        'name': 'test_node1_MDM',
                        'id': 'test_id_1',
                        'port': 0000
                    }
                ],
                'goodNodesNum': 3,
                'master': {
                    'managementIPs': [
                        DUMMY_IP
                    ],
                    'ips': [
                        DUMMY_IP
                    ],
                    'versionInfo': 'R3_6.0.0',
                    'virtualInterfaces': [
                        'ens192'
                    ],
                    'opensslVersion': 'OpenSSL26 Jan 2017',
                    'role': 'Manager',
                    'status': 'Normal',
                    'name': 'test_node_0',
                    'id': 'test_id_2',
                    'port': 0000
                },
                'tieBreakers': [
                    {
                        'managementIPs': [
                            DUMMY_IP
                        ],
                        'ips': [
                            DUMMY_IP
                        ],
                        'versionInfo': '',
                        'opensslVersion': 'N/A',
                        'role': 'TieBreaker',
                        'status': 'Normal',
                        'id': 'test_id_3',
                        'port': 0000
                    }
                ],
                'goodReplicasNum': 2,
                'id': ''
            },
            'sdcSdsConnectivityInfo': {
                'clientServerConnectivityStatus': 'AllConnected',
                'disconnectedClientId': None,
                'disconnectedClientName': None,
                'disconnectedServerId': None,
                'disconnectedServerName': None,
                'disconnectedServerIp': None
            },
            'addressSpaceUsage': 'Normal',
            'lastUpgradeTime': 0,
            'sdcSdrConnectivityInfo': {
                'clientServerConnectivityStatus': 'AllConnected',
                'disconnectedClientId': None,
                'disconnectedClientName': None,
                'disconnectedServerId': None,
                'disconnectedServerName': None,
                'disconnectedServerIp': None
            },
            'sdrSdsConnectivityInfo': {
                'clientServerConnectivityStatus': 'AllConnected',
                'disconnectedClientId': None,
                'disconnectedClientName': None,
                'disconnectedServerId': None,
                'disconnectedServerName': None,
                'disconnectedServerIp': None
            },
            'isInitialLicense': False,
            'capacityTimeLeftInDays': '253',
            'swid': 'abcdXXX',
            'installId': 'id_111',
            'restrictedSdcModeEnabled': False,
            'restrictedSdcMode': 'None',
            'enterpriseFeaturesEnabled': True,
            'daysInstalled': 112,
            'maxCapacityInGb': '5120',
            'id': 'id_222'
        }
    ]

    INFO_VOLUME_GET_LIST = MockVolumeApi.VOLUME_GET_LIST

    INFO_VOLUME_STATISTICS = {
        'test_vol_id_1': MockVolumeApi.VOLUME_STATISTICS
    }

    INFO_SNAPSHOT_POLICY_GET_LIST = MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST

    INFO_SNAPSHOT_POLICY_STATISTICS = {
        'test_snap_pol_id_1': MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
    }

    INFO_STORAGE_POOL_GET_LIST = MockStoragePoolApi.STORAGE_POOL_GET_LIST

    INFO_STORAGE_POOL_STATISTICS = {
        'test_pool_id_1': MockStoragePoolApi.STORAGE_POOL_STATISTICS
    }

    RCG_LIST = MockReplicationConsistencyGroupApi.get_rcg_details()
    PAIR_LIST = MockReplicationPairApi.get_pair_details()

    INFO_GET_FAULT_SET_LIST = MockFaultSetApi.FAULT_SET_GET_LIST

    INFO_SDC_GET_LIST = [
        {
            "id": "07335d3d00000006",
            "name": "sdc_1"
        },
        {
            "id": "07335d3c00000005",
            "name": "sdc_2"
        },
        {
            "id": "0733844a00000003",
            "name": "sdc_3"
        }
    ]

    INFO_SDC_FILTER_LIST = [
        {
            "id": "07335d3d00000006",
            "name": "sdc_1"
        }
    ]

    INFO_SDS_GET_LIST = [
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
    INFO_GET_PD_LIST = [
        {
            "id": "9300e90900000001",
            "name": "domain2"
        },
        {
            "id": "9300c1f900000000",
            "name": "domain1"
        }
    ]
    INFO_GET_DEVICE_LIST = [
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

    INFO_NVME_HOST_LIST = [
        {
            "id": "fake_host_id_1",
            "name": "fake_host_name_1",
            "hostType": "NVMeHost"
        },
        {
            "id": "fake_host_id_2",
            "hostType": "NVMeHost"
        }
    ]

    INFO_NVME_HOST_FILTER_LIST = [
        {
            "id": "fake_host_id",
            "name": "fake_host_name",
        }
    ]
    INFO_GET_SDT_LIST = [
        {
            "mdmConnectionState": "Connected",
            "softwareVersionInfo": "R4_5.2100.0",
            "name": "sdt-name",
            "id": "8bddf18c00000001"
        }
    ]
    INFO_GET_SDT_NVME_HOST_LIST = [
        {
            "hostType": "NVMeHost",
            "id": "1040d69e00010001"
        }
    ]
    INFO_GET_SDT_NVME_CONTROLLER_LIST = [
        {
            "isConnected": True,
            "sdtId": "8bddf18c00000001",
            "hostIp": "172.171.1.17",
            "hostId": "1040d69e00010001",
            "controllerId": 1,
            "sysPortId": 0,
            "sysPortIp": "172.171.3.21",
            "subsystem": "Io",
            "id": "cc00010001000002"
        }
    ]

    RESPONSE_EXEC_DICT = {
        'volume_get_details': "Get volumes list from powerflex array failed with error",
        'snapshot_policy_get_details': "Get snapshot policies list from powerflex array failed with error ",
        'sp_get_details': "Get storage pool list from powerflex array failed with error ",
        'rcg_get_details': "Get replication consistency group list from powerflex array failed with error ",
        'replication_pair_get_details': "Get replication pair list from powerflex array failed with error ",
        'fault_set_get_details': "Get fault set list from powerflex array failed with error",
        'sdc_get_details': "Get SDC list from powerflex array failed with error",
        'sds_get_details': "Get SDS list from powerflex array failed with error",
        'pd_get_details': "Get protection domain list from powerflex array failed with error",
        'device_get_details': "Get device list from powerflex array failed with error",
        'get_sds_details_filter_invalid': "Filter should have all keys: 'filter_key, filter_operator, filter_value'",
        'get_sds_details_filter_empty': "Filter keys: '['filter_key', 'filter_operator', 'filter_value']' cannot be None",
        'invalid_filter_operator_exception': "Given filter operator 'does_not_contain' is not supported.",
        'api_exception': "Get API details from Powerflex array failed with error",
        'system_exception': "Get array details from Powerflex array failed with error",
        'managed_device_get_error': "Get managed devices from PowerFlex Manager failed with error",
        'service_template_get_error': "Get service templates from PowerFlex Manager failed with error",
        'deployment_get_error': "Get deployments from PowerFlex Manager failed with error",
        'firmware_repository_get_error': "Get firmware repository from PowerFlex Manager failed with error",
        'nvme_host_get_details': "Get NVMe host list from powerflex array failed with error",
        "sdt_get_error": "Get sdt from PowerFlex Manager failed with error"
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockInfoApi.RESPONSE_EXEC_DICT.get(response_type, "")
