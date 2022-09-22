# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for storage pool module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storagepool_api import MockStoragePoolApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.storagepool import PowerFlexStoragePool


class TestPowerflexStoragePool():

    get_module_args = MockStoragePoolApi.STORAGE_POOL_COMMON_ARGS

    @pytest.fixture
    def storagepool_module_mock(self, mocker):
        storagepool_module_mock = PowerFlexStoragePool()
        storagepool_module_mock.module.check_mode = False
        return storagepool_module_mock

    def test_get_storagepool_details(self, storagepool_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool",
            "state": "present"
        })
        storagepool_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        storagepool_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        storagepool_statistics_resp = MockStoragePoolApi.STORAGE_POOL_STATISTICS
        storagepool_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            return_value=storagepool_statistics_resp
        )
        storagepool_module_mock.perform_module_operation()
        storagepool_module_mock.powerflex_conn.storage_pool.get.assert_called()
        storagepool_module_mock.powerflex_conn.storage_pool.get_statistics.assert_called()

    def test_get_storagepool_details_with_exception(self, storagepool_module_mock):
        self.get_module_args.update({
            "storage_pool_name": "test_pool"
        })
        storagepool_module_mock.module.params = self.get_module_args
        storagepool_resp = MockStoragePoolApi.STORAGE_POOL_GET_LIST
        storagepool_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storagepool_resp
        )
        storagepool_module_mock.powerflex_conn.storage_pool.get_statistics = MagicMock(
            side_effect=MockApiException
        )
        storagepool_module_mock.create_storage_pool = MagicMock(return_value=None)
        storagepool_module_mock.perform_module_operation()
        assert MockStoragePoolApi.get_exception_response('get_details') in storagepool_module_mock.module.fail_json.call_args[1]['msg']
