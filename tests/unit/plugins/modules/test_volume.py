# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for volume module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_volume_api import MockVolumeApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.volume import PowerFlexVolume


class TestPowerflexVolume():

    get_module_args = MockVolumeApi.VOLUME_COMMON_ARGS

    @pytest.fixture
    def volume_module_mock(self, mocker):
        volume_module_mock = PowerFlexVolume()
        volume_module_mock.module.check_mode = False
        return volume_module_mock

    def test_get_volume_details(self, volume_module_mock):
        self.get_module_args.update({
            "vol_name": "testing",
            "state": "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_resp = MockVolumeApi.VOLUME_GET_LIST
        volume_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_sp_resp = MockVolumeApi.VOLUME_STORAGEPOOL_DETAILS
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=volume_sp_resp
        )
        volume_pd_resp = MockVolumeApi.VOLUME_PD_DETAILS
        volume_module_mock.get_protection_domain = MagicMock(
            return_value=volume_pd_resp
        )
        volume_statistics_resp = MockVolumeApi.VOLUME_STATISTICS
        volume_module_mock.powerflex_conn.volume.get_statistics = MagicMock(
            return_value=volume_statistics_resp
        )
        volume_module_mock.perform_module_operation()
        volume_module_mock.powerflex_conn.volume.get.assert_called()
        volume_module_mock.powerflex_conn.volume.get_statistics.assert_called()

    def test_get_volume_details_with_exception(self, volume_module_mock):
        self.get_module_args.update({
            "vol_name": "testing",
            "state": "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_resp = MockVolumeApi.VOLUME_GET_LIST
        volume_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_module_mock.powerflex_conn.volume.get_statistics = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.create_volume = MagicMock(return_value=None)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.get_exception_response('get_details') in volume_module_mock.module.fail_json.call_args[1]['msg']
