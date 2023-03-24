# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

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


__metaclass__ = type


class MockInfoApi:
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

    INFO_STORAGE_POOL_GET_LIST = MockStoragePoolApi.STORAGE_POOL_GET_LIST

    INFO_STORAGE_POOL_STATISTICS = {
        'test_pool_id_1': MockStoragePoolApi.STORAGE_POOL_STATISTICS
    }

    RCG_LIST = MockReplicationConsistencyGroupApi.get_rcg_details()
    PAIR_LIST = MockReplicationPairApi.get_pair_details()

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'volume_get_details':
            return "Get volumes list from powerflex array failed with error "
        elif response_type == 'sp_get_details':
            return "Get storage pool list from powerflex array failed with error "
        elif response_type == 'rcg_get_details':
            return "Get replication consistency group list from powerflex array failed with error "
        elif response_type == 'replication_pair_get_details':
            return "Get replication pair list from powerflex array failed with error "
