# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for storage pool module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storagepool_api import MockStoragePoolApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.storagepool import PowerFlexStoragePool


class TestPowerflexStoragePool(PowerFlexUnitBase):

    get_module_args = MockStoragePoolApi.STORAGE_POOL_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexStoragePool

    def test_get_storagepool_details(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "state": "present"
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
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.get.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics.assert_called()

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
            powerflex_module_mock, invoke_perform_module=True)

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
            powerflex_module_mock, invoke_perform_module=True)

    @pytest.mark.parametrize("params", [
        {"pd_id": "4eeb304600000000"},
        {"pd_name": "test"},
    ])
    def test_get_protection_domain(self, powerflex_module_mock, params):
        pd_id = params.get("pd_id", None)
        pd_name = params.get("pd_name", None)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolApi.PROTECTION_DETAILS
        )
        pd_details = powerflex_module_mock.get_protection_domain(pd_name, pd_id)
        assert MockStoragePoolApi.PROTECTION_DETAILS[0] == pd_details

    def test_get_protection_domain_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_id": "4eeb304600000001",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('get_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_get_protection_domain_non_exist(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_id": "4eeb304600000001",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('get_pd_non_exist'),
            powerflex_module_mock, invoke_perform_module=True)

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
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_storagepool_response(self, powerflex_module_mock):
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
            return_value=None
        )
        resp = powerflex_module_mock.create_storage_pool(pool_name="test_pool",
                                                         pd_id=MockStoragePoolApi.PROTECTION_DETAILS_1[0]['id'],
                                                         media_type="HDD")
        assert resp is True
        powerflex_module_mock.powerflex_conn.storage_pool.create.assert_called()

    def test_create_storagepool_only_pool_id(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_id": "test_pool_id",
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
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_pool_id'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_storagepool_new_name(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "storage_pool_new_name": "pool_new_name",
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
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_pool_new_name'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_storagepool_empty_name(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": " ",
            "protection_domain_name": "test_pd_name",
            "media_type": "HDD",
            "state": "present"
        })
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolApi.PROTECTION_DETAILS_1)
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('create_pool_name_empty'),
            powerflex_module_mock, invoke_perform_module=True)

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
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_storagepool_transitional_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "protection_domain_name": "test_pd_name",
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
            powerflex_module_mock, invoke_perform_module=True)

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
            powerflex_module_mock, invoke_perform_module=True)

    def test_modify_storagepool_details(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "storage_pool_new_name": "new_ansible_pool",
            "use_rfcache": True,
            "use_rmcache": True,
            "media_type": "TRANSITIONAL",
            "state": "present"
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
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.rename.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_use_rmcache.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_use_rfcache.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.set_media_type.assert_called()

    def test_rename_storagepool_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "storage_pool_new_name": "new_ansible_pool",
            "state": "present"
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
        powerflex_module_mock.powerflex_conn.storage_pool.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('rename_storage_pool'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_rename_storagepool_empty_exception(self, powerflex_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "storage_pool_new_name": " ",
            "state": "present"
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
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('rename_storage_pool_empty'),
            powerflex_module_mock, invoke_perform_module=True)

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
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        powerflex_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        self.capture_fail_json_call(
            MockStoragePoolApi.get_exception_response('delete_storage_pool'),
            powerflex_module_mock, invoke_perform_module=True)
