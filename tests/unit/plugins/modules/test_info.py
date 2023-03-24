# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for info module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_info_api import MockInfoApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.info import PowerFlexInfo


class TestPowerflexInfo():

    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        info_module_mock = PowerFlexInfo()
        info_module_mock.module.check_mode = False
        info_module_mock.powerflex_conn.system.api_version = MagicMock(
            return_value=3.5
        )
        info_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockInfoApi.INFO_ARRAY_DETAILS
        )
        return info_module_mock

    def test_get_volume_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        volume_resp = MockInfoApi.INFO_VOLUME_GET_LIST
        info_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_stat_resp = MockInfoApi.INFO_VOLUME_STATISTICS
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_volumes = MagicMock(
            return_value=volume_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.volume.get.assert_called()
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_volumes.assert_called()

    def test_get_volume_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        volume_resp = MockInfoApi.INFO_VOLUME_GET_LIST
        info_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_volumes = MagicMock(
            side_effect=MockApiException
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('volume_get_details') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_sp_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['storage_pool']
        })
        info_module_mock.module.params = self.get_module_args
        sp_resp = MockInfoApi.INFO_STORAGE_POOL_GET_LIST
        info_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=sp_resp
        )
        sp_stat_resp = MockInfoApi.INFO_STORAGE_POOL_STATISTICS
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_storagepools = MagicMock(
            return_value=sp_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.storage_pool.get.assert_called()
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_storagepools.assert_called()

    def test_get_sp_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['storage_pool']
        })
        info_module_mock.module.params = self.get_module_args
        sp_resp = MockInfoApi.INFO_STORAGE_POOL_GET_LIST
        info_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=sp_resp
        )
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_storagepools = MagicMock(
            side_effect=MockApiException
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('sp_get_details') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_rcg_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['rcg']
        })
        info_module_mock.module.params = self.get_module_args
        rcg_resp = MockInfoApi.RCG_LIST
        info_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=rcg_resp)
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.replication_consistency_group.get.assert_called()

    def test_get_rcg_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['rcg']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            side_effect=MockApiException
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('rcg_get_details') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_replication_pair_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['replication_pair']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.replication_pair.get = MagicMock(
            return_value=MockInfoApi.PAIR_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.replication_pair.get.assert_called()

    def test_get_replication_pair_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['replication_pair']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.replication_pair.get = MagicMock(
            side_effect=MockApiException
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('replication_pair_get_details') in info_module_mock.module.fail_json.call_args[1]['msg']
