# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of MDM cluster module on PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockMdmClusterApi:
    MODULE_PATH = 'ansible_collections.dellemc.powerflex.plugins.modules.mdm_cluster.PowerFlexMdmCluster'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils'

    MDM_CLUSTER_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "mdm_id": None,
        "mdm_name": None,
        "mdm_new_name": None,
        "performance_profile": None,
        "standby_mdm": None,
        "is_primary": None,
        "cluster_mode": None,
        "mdm": None,
        "mdm_state": None,
        "virtual_ip_interfaces": None,
        "clear_interfaces": None,
        'state': None
    }

    MDM_NAME = "mdm_node1"
    MDM_NAME_STB_MGR = "mdm_node_mgr"
    MDM_ID = "5908d328581d1401"
    STB_TB_MDM_ID = "5908d328581d1403"
    STB_MGR_MDM_ID = "36279b98215e5a04"
    IP_1 = "10.x.y.z"
    IP_2 = "10.x.x.z"
    IP_3 = "10.x.z.z"
    IP_4 = "10.x.y.y"
    SSL_VERSION = "OpenSSL 1.0.2k-fips  26 Jan 2017"
    SYS_VERSION = "DellEMC PowerFlex Version: R3_6.0.354"

    THREE_MDM_CLUSTER_DETAILS = {
        "clusterState": "ClusteredNormal",
        "clusterMode": "ThreeNodes",
        "goodNodesNum": 3,
        "master": {
            "virtualInterfaces": [
                "ens1"
            ],
            "managementIPs": [
                IP_1
            ],
            "ips": [
                IP_1
            ],
            "versionInfo": "R3_6.0.0",
            "opensslVersion": SSL_VERSION,
            "role": "Manager",
            "status": "Normal",
            "name": "sample_mdm",
            "id": "5908d328581d1400",
            "port": 9011
        },
        "perfProfile": "HighPerformance",
        "slaves": [
            {
                "virtualInterfaces": [
                    "ens1"
                ],
                "managementIPs": [
                    IP_2
                ],
                "ips": [
                    IP_2
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": SSL_VERSION,
                "role": "Manager",
                "status": "Normal",
                "name": "sample_mdm1",
                "id": MDM_ID,
                "port": 9011
            }
        ],
        "tieBreakers": [
            {
                "managementIPs": [],
                "ips": [
                    IP_4
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "TieBreaker",
                "status": "Normal",
                "id": "5908d328581d1402",
                "port": 9011
            }
        ],
        "standbyMDMs": [
            {
                "managementIPs": [
                    IP_3
                ],
                "ips": [
                    IP_3
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "TieBreaker",
                "status": "Normal",
                "name": MDM_NAME,
                "id": STB_TB_MDM_ID,
                "port": 9011
            },
            {
                "virtualInterfaces": [
                    "ens12"
                ],
                "managementIPs": [
                    IP_3
                ],
                "ips": [
                    IP_3
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "Manager",
                "status": "Normal",
                "name": MDM_NAME_STB_MGR,
                "id": STB_MGR_MDM_ID,
                "port": 9011
            }
        ],
        "goodReplicasNum": 2,
        "id": "cdd883cf00000002"
    }

    THREE_MDM_CLUSTER_DETAILS_2 = {
        "clusterState": "ClusteredNormal",
        "clusterMode": "ThreeNodes",
        "goodNodesNum": 3,
        "master": {
            "virtualInterfaces": [
                "ens1"
            ],
            "managementIPs": [
                IP_1
            ],
            "ips": [
                IP_1
            ],
            "versionInfo": "R3_6.0.0",
            "opensslVersion": SSL_VERSION,
            "role": "Manager",
            "status": "Normal",
            "name": "sample_mdm",
            "id": "5908d328581d1400",
            "port": 9011
        },
        "perfProfile": "HighPerformance",
        "slaves": [
            {
                "virtualInterfaces": [
                    "ens1"
                ],
                "managementIPs": [
                    IP_2
                ],
                "ips": [
                    IP_2
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": SSL_VERSION,
                "role": "Manager",
                "status": "Normal",
                "name": "sample_mdm1",
                "id": MDM_ID,
                "port": 9011
            }
        ],
        "tieBreakers": [
            {
                "managementIPs": [],
                "ips": [
                    IP_4
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "TieBreaker",
                "status": "Normal",
                "id": "5908d328581d1402",
                "port": 9011
            }
        ],
        "goodReplicasNum": 2,
        "id": "cdd883cf00000002"
    }

    FIVE_MDM_CLUSTER_DETAILS = {
        "clusterState": "ClusteredNormal",
        "clusterMode": "FiveNodes",
        "goodNodesNum": 5,
        "master": {
            "virtualInterfaces": [
                "ens1"
            ],
            "managementIPs": [
                IP_1
            ],
            "ips": [
                IP_1
            ],
            "versionInfo": "R3_6.0.0",
            "opensslVersion": SSL_VERSION,
            "role": "Manager",
            "status": "Normal",
            "name": "sample_mdm",
            "id": "5908d328581d1400",
            "port": 9011
        },
        "perfProfile": "HighPerformance",
        "slaves": [
            {
                "virtualInterfaces": [],
                "managementIPs": [
                    IP_2
                ],
                "ips": [
                    IP_2
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": SSL_VERSION,
                "role": "Manager",
                "status": "Normal",
                "name": "sample_mdm11",
                "id": MDM_ID,
                "port": 9011
            },
            {
                "virtualInterfaces": [
                    "ens12"
                ],
                "managementIPs": [
                    IP_3
                ],
                "ips": [
                    IP_3
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "Manager",
                "status": "Normal",
                "name": MDM_NAME_STB_MGR,
                "id": STB_MGR_MDM_ID,
                "port": 9011
            }
        ],
        "tieBreakers": [
            {
                "managementIPs": [
                    IP_3
                ],
                "ips": [
                    IP_3
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "TieBreaker",
                "status": "Normal",
                "name": MDM_NAME,
                "id": STB_TB_MDM_ID,
                "port": 9011
            },
            {
                "managementIPs": [],
                "ips": [
                    IP_4
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "TieBreaker",
                "status": "Normal",
                "id": "5908d328581d1402",
                "port": 9011
            }
        ],
        "standbyMDMs": [
            {
                "virtualInterfaces": [
                    "ens13"
                ],
                "managementIPs": [
                    IP_1
                ],
                "ips": [
                    IP_1
                ],
                "versionInfo": "R3_6.0.0",
                "opensslVersion": "N/A",
                "role": "Manager",
                "status": "Normal",
                "name": "mgr_node_2",
                "id": "5120af354fb17305",
                "port": 9011
            }
        ],
        "goodReplicasNum": 2,
        "id": "cdd883cf00000002"
    }
    PARTIAL_SYSTEM_DETAILS = [
        {
            "systemVersionName": SYS_VERSION,
            "perfProfile": "Compact",
            "name": "System:3c567fd2298f020f",
            "id": "3c567fd2298f020f"
        },
        {
            "systemVersionName": SYS_VERSION,
            "perfProfile": "Compact",
            "name": "System:3c567fd2298f0201",
            "id": "3c567fd2298f0201"
        }
    ]
    PARTIAL_SYSTEM_DETAILS_1 = [
        {
            "systemVersionName": SYS_VERSION,
            "perfProfile": "Compact",
            "name": "System:3c567fd2298f020f",
            "id": "3c567fd2298f020f"
        }
    ]

    @staticmethod
    def get_failed_response():
        return "Failed to get the MDM cluster with error"

    @staticmethod
    def rename_failed_response():
        return "Failed to rename the MDM mdm_node1 with error"

    @staticmethod
    def perf_profile_failed_response():
        return "Failed to update performance profile to Compact with error"

    @staticmethod
    def virtual_ip_interface_failed_response():
        return "Failed to modify the virtual IP interfaces of MDM 5908d328581d1401 with error"

    @staticmethod
    def remove_mdm_failed_response():
        return "Failed to remove the standby MDM 5908d328581d1403 from the MDM cluster with error"

    @staticmethod
    def add_mdm_failed_response():
        return "Failed to Add a standby MDM with error"

    @staticmethod
    def owner_failed_response():
        return "Failed to update the Owner of MDM cluster to MDM sample_mdm1 with error"

    @staticmethod
    def switch_mode_failed_response():
        return "Failed to change the MDM cluster mode with error"

    @staticmethod
    def system_failed_response():
        return "Failed to get system id with error"

    @staticmethod
    def multiple_system_failed_response():
        return "Multiple systems exist on the given host."

    @staticmethod
    def remove_mdm_no_id_name_failed_response():
        return "Either mdm_name or mdm_id is required while removing the standby MDM."

    @staticmethod
    def without_standby_failed_response():
        return "No Standby MDMs found. To expand cluster size, first add standby MDMs."

    @staticmethod
    def no_cluster_failed_response():
        return "MDM cluster not found"

    @staticmethod
    def id_none_interface_failed_response():
        return "Please provide mdm_name/mdm_id to modify virtual IP interfaces the MDM"

    @staticmethod
    def id_none_rename_failed_response():
        return "Please provide mdm_name/mdm_id to rename the MDM"

    @staticmethod
    def id_none_change_owner_failed_response():
        return "Either mdm_name or mdm_id is required while changing ownership of MDM cluster"

    @staticmethod
    def new_name_add_mdm_failed_response():
        return "Parameters mdm_id/mdm_new_name are not allowed while adding a standby MDM"
