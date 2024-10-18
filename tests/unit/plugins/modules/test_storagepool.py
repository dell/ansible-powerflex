# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for storage pool module on PowerFlex"""


from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storagepool_api \
    import MockStoragePoolApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.storagepool \
    import PowerFlexStoragePool
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.plugins.modules.storagepool import \
    StoragePoolHandler


class TestPowerflexStoragePool(PowerFlexUnitBase):

    get_module_args = MockStoragePoolApi.STORAGE_POOL_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexStoragePool

    def test_get_storage_pool_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=MockStoragePoolApi.STORAGE_POOL_GET_LIST)
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        StoragePoolHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_pool.get.assert_called()

    def test_get_storagepool_details_multi(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_MULTI_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('get_multi_details'),
            powerflex_module_mock, StoragePoolHandler)

    def test_get_storagepool_details_with_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            side_effect=MockApiException
        )
        powerflex_module_mock.create_storage_pool = MagicMock(return_value=None)
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('get_details'),
            powerflex_module_mock, StoragePoolHandler)

    def test_get_storagepool_details_with_invalid_pd_id(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_id": "4eeb304600000001"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolApi.PROTECTION_DETAILS_1
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('invalid_pd_id'),
            powerflex_module_mock, StoragePoolHandler)

    def test_create_storagepool_response(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "media_type": "HDD",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=[]
        )
        StoragePoolHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_pool.create.assert_called()

    def test_create_storagepool_empty_name(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": " ",
            "protection_domain_name": "test_pd_1",
            "media_type": "HDD",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolApi.PROTECTION_DETAILS_1)
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_pool_name_empty'),
            powerflex_module_mock, StoragePoolHandler)

    def test_create_storagepool_wo_pd(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "media_type": "HDD",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_wo_pd'),
            powerflex_module_mock, StoragePoolHandler)

    def test_create_storagepool_transitional_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "media_type": "TRANSITIONAL",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolApi.PROTECTION_DETAILS_1)
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.storage_pool.create = MagicMock(
            return_value=None
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_transitional'),
            powerflex_module_mock, StoragePoolHandler)

    def test_create_storagepool_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_name",
            "media_type": "HDD",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolApi.PROTECTION_DETAILS_1)
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.storage_pool.create = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_storage_pool'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_storagepool_details(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "storage_pool_new_name": "new_ansible_pool",
            "use_rfcache": True,
            "use_rmcache": True,
            "cap_alert_thresholds": {
                "high_threshold": 30,
                "critical_threshold": 50
            },
            "enable_zero_padding": True,
            "rep_cap_max_ratio": 40,
            "rmcache_write_handling_mode": "Passthrough",
            "spare_percentage": 80,
            "enable_rebalance": False,
            "enable_fragmentation": False,
            "enable_rebuild": False,
            "parallel_rebuild_rebalance_limit": 3,
            "protected_maintenance_mode_io_priority_policy": {
                "policy": "unlimited",
                "concurrent_ios_per_device": 1,
                "bw_limit_per_device": 1024},
            "rebalance_io_priority_policy": {
                "policy": "limitNumOfConcurrentIos",
                "concurrent_ios_per_device": 10,
                "bw_limit_per_device": 1024},
            "vtree_migration_io_priority_policy": {
                "policy": "limitNumOfConcurrentIos",
                "concurrent_ios_per_device": 10,
                "bw_limit_per_device": 1024},
            "persistent_checksum": {
                "enable": True,
                "validate_on_read": True,
                "builder_limit": 1024},
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        StoragePoolHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_pool.rename.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_use_rmcache.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_use_rfcache.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_fragmentation_enabled.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_persistent_checksum.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_rebuild_rebalance_parallelism_limit.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_rmcache_write_handling_mode.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.rebalance_io_priority_policy.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_vtree_migration_io_priority_policy.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_protected_maintenance_mode_io_priority_policy.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_cap_alert_thresholds.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_zero_padding_policy.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_spare_percentage.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_rebuild_enabled.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_rebalance_enabled.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_rep_cap_max_ratio.assert_called()

    def test_delete_storagepool_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "state": "absent"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('delete_storage_pool'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_name_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "storage_pool_new_name": "test_pool_new",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('rename_pool'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_rmcache_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "use_rmcahe": True,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_use_rmcache = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_rmcache'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_rfcache_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "use_rfcahe": True,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_use_rfcache = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_rfcache'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_enable_zero_padding_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "enable_zero_padding": False,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_zero_padding_policy = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_enable_zero_padding'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_rep_cap_max_ratio_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "rep_cap_max_ratio": 10,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_rep_cap_max_ratio = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_rep_cap_max_ratio'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_enable_rebalance_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "enable_rebalance": False,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_rebalance_enabled = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_enable_rebalance'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_enable_rebuild_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "enable_rebuild": False,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_rebuild_enabled = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_enable_rebuild'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_enable_fragmentation_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "enable_fragmentaion": False,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_fragmentation_enabled = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_enable_fragmentation'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_spare_percentage_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "spare_percentage": 20,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_spare_percentage = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_spare_percentage'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_rmcache_write_handling_mode_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "rmcache_write_handling_mode": "Cached",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_rmcache_write_handling_mode = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_rmcache_write_handling_mode'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_rebuild_rebalance_parallelism_limit_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "parallel_rebuild_rebalance_limit": 4,
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_rebuild_rebalance_parallelism_limit = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_rebuild_rebalance_parallelism_limit'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_capacity_alert_thresholds_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "capacity_alert_thresholds": {
                "high_threshold": 60,
                "critical_threshold": 70
            },
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_capacity_alert_thresholds = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_capacity_alert_thresholds'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_protected_maintenance_mode_io_priority_policy_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "protected_maintenance_mode_io_priority_policy": {
                "policy": "unlimited",
                "concurrent_ios_per_device": 1,
                "bw_limit_per_device": 1024},
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_protected_maintenance_mode_io_priority_policy = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_protected_maintenance_mode_io_priority_policy'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_vtree_migration_io_priority_policy_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "vtree_migration_io_priority_policy": {
                "policy": "favorAppIos",
                "concurrent_ios_per_device": 1,
                "bw_limit_per_device": 1024},
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_vtree_migration_io_priority_policy = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_vtree_migration_io_priority_policy'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_rebalance_io_priority_policy_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "rebalance_io_priority_policy": {
                "policy": "favorAppIos",
                "concurrent_ios_per_device": 1,
                "bw_limit_per_device": 1024},
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.rebalance_io_priority_policy = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_rebalance_io_priority_policy'),
            powerflex_module_mock, StoragePoolHandler)

    def test_modify_persistent_checksum_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_1",
            "persistent_checksum": {
                "enable": True,
                "validate_on_read": True,
                "builder_limit": 1024},
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        pd_resp = MockStoragePoolApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        powerflex_module_mock.powerflex_conn.storage_pool.set_persistent_checksum = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('modify_pool_persistent_checksum'),
            powerflex_module_mock, StoragePoolHandler)
