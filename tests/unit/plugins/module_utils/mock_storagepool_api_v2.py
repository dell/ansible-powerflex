# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of storage pool module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockStoragePoolV2Api:
    STORAGE_POOL_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "storage_pool_name": None,
        "storage_pool_id": None,
        "storage_pool_new_name": None,
        "protection_domain_name": None,
        "protection_domain_id": "7bd6457000000000",
        "device_group_name": None,
        "device_group_id": None,
        "protection_scheme": None,
        "compression_method": None,
        "use_all_available_capacity": None,
        "physical_size_gb": None,
        "cap_alert_thresholds": {
            "high_threshold": 30,
            "critical_threshold": 50
        },
        "over_provisioning_factor": 100,
        "state": None
    }

    STORAGE_POOL_GET_DETAIL = {
        "genType": "EC",
        "fglAccpId": None,
        "backgroundScannerMode": None,
        "vtreeMigrationIoPriorityPolicy": None,
        "backgroundScannerBWLimitKBps": None,
        "vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice": None,
        "protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice": None,
        "rebalanceIoPriorityBwLimitPerDeviceInKbps": None,
        "vtreeMigrationIoPriorityBwLimitPerDeviceInKbps": None,
        "protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps": None,
        "rebuildIoPriorityAppIopsPerDeviceThreshold": None,
        "rebalanceIoPriorityAppIopsPerDeviceThreshold": None,
        "vtreeMigrationIoPriorityAppIopsPerDeviceThreshold": None,
        "protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold": None,
        "rebuildIoPriorityAppBwPerDeviceThresholdInKbps": None,
        "rebalanceIoPriorityAppBwPerDeviceThresholdInKbps": None,
        "vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps": None,
        "protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps": None,
        "rebuildIoPriorityQuietPeriodInMsec": None,
        "rebalanceIoPriorityQuietPeriodInMsec": None,
        "vtreeMigrationIoPriorityQuietPeriodInMsec": None,
        "protectedMaintenanceModeIoPriorityQuietPeriodInMsec": None,
        "useRmcache": False,
        "protectedMaintenanceModeIoPriorityPolicy": None,
        "rebuildIoPriorityNumOfConcurrentIosPerDevice": None,
        "rebalanceIoPriorityNumOfConcurrentIosPerDevice": None,
        "rebuildIoPriorityBwLimitPerDeviceInKbps": None,
        "fglNvdimmWriteCacheSizeInMb": None,
        "fglMetadataSizeXx100": None,
        "rebalanceIoPriorityPolicy": None,
        "rebuildIoPriorityPolicy": None,
        "fglNvdimmMetadataAmortizationX100": None,
        "name": "test_pool",
        "zeroPaddingEnabled": True,
        "mediaType": None,
        "protectionDomainId": "7bd6457000000000",
        'protectionDomainName': "test_pd_1",
        "rebuildEnabled": None,
        "dataLayout": "ErasureCoding",
        "overProvisioningFactor": 100,
        "compressionMethod": "Normal",
        "externalAccelerationType": "None",
        "fglExtraCapacity": None,
        "fglOverProvisioningFactor": None,
        "fglWriteAtomicitySize": None,
        "fglMaxCompressionRatio": None,
        "fglPerfProfile": None,
        "spClass": "Default",
        "physicalSizeGB": 4096,
        "spHealthState": "Protected",
        "useRfcache": False,
        "addressSpaceUsage": "Normal",
        "sparePercentage": None,
        "capacityAlertHighThreshold": 80,
        "capacityAlertCriticalThreshold": 90,
        "capacityUsageState": "Normal",
        "addressSpaceUsageType": "DeviceCapacityLimit",
        "capacityUsageType": "NetCapacity",
        "deviceGroupId": "39a898be00000000",
        "protectionScheme": "TwoPlusTwo",
        "persistentChecksumState": "StateInvalid",
        "rmcacheWriteHandlingMode": "Invalid",
        "checksumEnabled": False,
        "fragmentationEnabled": False,
        "numOfParallelRebuildRebalanceJobsPerDevice": None,
        "bgScannerCompareErrorAction": "Invalid",
        "bgScannerReadErrorAction": "Invalid",
        "replicationCapacityMaxRatio": None,
        "persistentChecksumEnabled": False,
        "persistentChecksumBuilderLimitKb": None,
        "persistentChecksumValidateOnRead": None,
        "rawSizeGB": 8192,
        "wrcDeviceGroupId": "39a898be00000000",
        "rebalanceEnabled": None,
        "id": "5dac1b0300000000",
    }

    STORAGE_POOL_GET_MULTI_LIST = [
        {
            'protectionDomainId': "7bd6457000000000",
            'protectionDomainName': "test_pd_1",
            'rebuildEnabled': True,
            'dataLayout': 'MediumGranularity',
            'persistentChecksumState': 'Protected',
            'addressSpaceUsage': 'Normal',
            'externalAccelerationType': 'None',
            'rebalanceEnabled': True,
            'sparePercentage': 10,
            'rmcacheWriteHandlingMode': 'Cached',
            'checksumEnabled': False,
            'useRfcache': False,
            'compressionMethod': 'Invalid',
            'fragmentationEnabled': True,
            'numOfParallelRebuildRebalanceJobsPerDevice': 2,
            'capacityAlertHighThreshold': 80,
            'capacityAlertCriticalThreshold': 90,
            'capacityUsageState': 'Normal',
            'capacityUsageType': 'NetCapacity',
            'addressSpaceUsageType': 'DeviceCapacityLimit',
            'bgScannerCompareErrorAction': 'ReportAndFix',
            'bgScannerReadErrorAction': 'ReportAndFix',
            'fglExtraCapacity': None,
            'fglOverProvisioningFactor': None,
            'fglWriteAtomicitySize': None,
            'fglMaxCompressionRatio': None,
            'fglPerfProfile': None,
            'replicationCapacityMaxRatio': 0,
            'persistentChecksumEnabled': True,
            'persistentChecksumBuilderLimitKb': 3072,
            'persistentChecksumValidateOnRead': False,
            'useRmcache': False,
            'fglAccpId': None,
            'rebuildIoPriorityPolicy': 'limitNumOfConcurrentIos',
            'rebalanceIoPriorityPolicy': 'favorAppIos',
            'vtreeMigrationIoPriorityPolicy': 'favorAppIos',
            'protectedMaintenanceModeIoPriorityPolicy': 'limitNumOfConcurrentIos',
            'rebuildIoPriorityNumOfConcurrentIosPerDevice': 1,
            'rebalanceIoPriorityNumOfConcurrentIosPerDevice': 1,
            'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': 1,
            'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': 1,
            'rebuildIoPriorityBwLimitPerDeviceInKbps': 10240,
            'rebalanceIoPriorityBwLimitPerDeviceInKbps': 10240,
            'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': 10240,
            'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': 10240,
            'rebuildIoPriorityAppIopsPerDeviceThreshold': None,
            'rebalanceIoPriorityAppIopsPerDeviceThreshold': None,
            'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None,
            'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None,
            'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'rebuildIoPriorityQuietPeriodInMsec': None,
            'rebalanceIoPriorityQuietPeriodInMsec': None,
            'vtreeMigrationIoPriorityQuietPeriodInMsec': None,
            'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None,
            'zeroPaddingEnabled': True,
            'backgroundScannerMode': 'DataComparison',
            'backgroundScannerBWLimitKBps': 3072,
            'fglMetadataSizeXx100': None,
            'fglNvdimmWriteCacheSizeInMb': None,
            'fglNvdimmMetadataAmortizationX100': None,
            'mediaType': 'HDD',
            'name': 'test_pool',
            'id': 'test_pool_id_1'
        },
        {
            'protectionDomainId': "7bd6457000000000",
            'protectionDomainName': 'test_pd_1',
            'rebuildEnabled': True,
            'dataLayout': 'MediumGranularity',
            'persistentChecksumState': 'Protected',
            'addressSpaceUsage': 'Normal',
            'externalAccelerationType': 'None',
            'rebalanceEnabled': True,
            'sparePercentage': 10,
            'rmcacheWriteHandlingMode': 'Cached',
            'checksumEnabled': False,
            'useRfcache': False,
            'compressionMethod': 'Invalid',
            'fragmentationEnabled': True,
            'numOfParallelRebuildRebalanceJobsPerDevice': 2,
            'capacityAlertHighThreshold': 80,
            'capacityAlertCriticalThreshold': 90,
            'capacityUsageState': 'Normal',
            'capacityUsageType': 'NetCapacity',
            'addressSpaceUsageType': 'DeviceCapacityLimit',
            'bgScannerCompareErrorAction': 'ReportAndFix',
            'bgScannerReadErrorAction': 'ReportAndFix',
            'fglExtraCapacity': None,
            'fglOverProvisioningFactor': None,
            'fglWriteAtomicitySize': None,
            'fglMaxCompressionRatio': None,
            'fglPerfProfile': None,
            'replicationCapacityMaxRatio': 0,
            'persistentChecksumEnabled': True,
            'persistentChecksumBuilderLimitKb': 3072,
            'persistentChecksumValidateOnRead': False,
            'useRmcache': False,
            'fglAccpId': None,
            'rebuildIoPriorityPolicy': 'limitNumOfConcurrentIos',
            'rebalanceIoPriorityPolicy': 'favorAppIos',
            'vtreeMigrationIoPriorityPolicy': 'favorAppIos',
            'protectedMaintenanceModeIoPriorityPolicy': 'limitNumOfConcurrentIos',
            'rebuildIoPriorityNumOfConcurrentIosPerDevice': 1,
            'rebalanceIoPriorityNumOfConcurrentIosPerDevice': 1,
            'vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice': 1,
            'protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice': 1,
            'rebuildIoPriorityBwLimitPerDeviceInKbps': 10240,
            'rebalanceIoPriorityBwLimitPerDeviceInKbps': 10240,
            'vtreeMigrationIoPriorityBwLimitPerDeviceInKbps': 10240,
            'protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps': 10240,
            'rebuildIoPriorityAppIopsPerDeviceThreshold': None,
            'rebalanceIoPriorityAppIopsPerDeviceThreshold': None,
            'vtreeMigrationIoPriorityAppIopsPerDeviceThreshold': None,
            'protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold': None,
            'rebuildIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'rebalanceIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps': None,
            'rebuildIoPriorityQuietPeriodInMsec': None,
            'rebalanceIoPriorityQuietPeriodInMsec': None,
            'vtreeMigrationIoPriorityQuietPeriodInMsec': None,
            'protectedMaintenanceModeIoPriorityQuietPeriodInMsec': None,
            'zeroPaddingEnabled': True,
            'backgroundScannerMode': 'DataComparison',
            'backgroundScannerBWLimitKBps': 3072,
            'fglMetadataSizeXx100': None,
            'fglNvdimmWriteCacheSizeInMb': None,
            'fglNvdimmMetadataAmortizationX100': None,
            'mediaType': 'HDD',
            'name': 'test_pool',
            'id': 'test_pool_id_2'
        }
    ]

    PROTECTION_DETAILS = [{"pd_id": "4eeb304600000000", "pd_name": "test_pd"}]

    PROTECTION_DETAILS_1 = [{"id": "4eeb304600000001", "name": "test_pd_name"}]

    PROTECTION_DOMAIN = {
        "protection_domain": [
            {
                "id": "7bd6457000000000",
                "name": "test_pd_1",
                "genType": "EC",
                "vtreeMigrationNetworkThrottlingEnabled": False,
                "overallIoNetworkThrottlingEnabled": False,
                "rfcacheEnabled": True,
                "rebalanceNetworkThrottlingEnabled": False,
                "rebuildNetworkThrottlingEnabled": False,
            }
        ]
    }

    DEVICE_GROUP = {
        "device_group": [
            {
                "id": "39a898be00000000",
                "name": "test_dg_1",
                "genType": "EC",
                "mediaType": "SSD",
                "protectionDomainId": "7bd6457000000000",
                "capacityHealthState": "Protected",
                "deviceGroupState": "Initializing",
            }
        ]
    }

    DEVICE_GROUP_DETAILS_1 = [{"id": "4eeb304600000001", "name": "test_dg_name"},
                              {"id": "4eeb304600000002", "name": "test_dg_name_2"}]

    STORAGE_POOL_STATISTICS = {
        "id": "5dac1b0300000000",
        "metrics": [
            {
                "name": "physical_free",
                "values": [
                    4344359419904
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
                    8796093022208
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
                    4398046511104
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
                    4398046511104
                ]
            }
        ]
    }

    RESPONSE_EXEC_DICT = {
        "get_details": "Failed to get the storage pool test_pool with error ",
        "invalid_pd_id": "Entered protection domain id does not match with the storage pool's protection domain id.",
        "invalid_pd_name": "Entered protection domain name does not match with the storage pool's protection domain name",
        "invalid_dg_id": "Entered device group id does not match with the storage pool's device group id.",
        "create_storage_pool": "Create storage pool 'test_pool' operation failed with error",
        "physical_size_gb_should_not_specify": "When creating or updating storage pool, physical_size_gb must not be specified",
        "physical_size_gb_must_specify": "When creating or updating storage pool, physical_size_gb must be specified",
        "delete_storage_pool": "Delete storage pool test_pool operation failed",
        "delete_non_existing_storage_pool": "Storage pool not found",
        "update_storage_pool": "Failed to update the storage pool",
        "query_metrics": "Failed to query statistics with error",
        "protection_domain_params": "Either protection_domain_id or protection_domain_name",
        "device_group_not_found": "Unable to find device group with",
        "device_group_exception": "Failed to get device group",
        "mismatch_device_group_id_exception": "Entered device group id does not match",
        "mismatch_device_group_name_exception": "Entered device group name does not match",
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockStoragePoolV2Api.RESPONSE_EXEC_DICT.get(response_type, "")
