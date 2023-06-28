# Copyright: (c) 2023, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for sdc module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdc_api import MockSdcApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.sdc import PowerFlexSdc


class TestPowerflexSdc():

    get_module_args = MockSdcApi.COMMON_ARGS

    @pytest.fixture
    def sdc_module_mock(self):
        sdc_module_mock = PowerFlexSdc()
        return sdc_module_mock

    def test_get_sdc_details(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.perform_module_operation()
        sdc_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_sdc_details_with_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_id": MockSdcApi.SDC_ID,
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException)
        sdc_module_mock.perform_module_operation()
        assert "Could not find any SDC instance" in \
            sdc_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_sdc_details_mapped_volumes_with_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_id": MockSdcApi.SDC_ID,
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.get_mapped_volumes = MagicMock(
            side_effect=MockApiException)
        sdc_module_mock.perform_module_operation()
        assert "Failed to get the volumes mapped to SDC" in \
            sdc_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_sdc(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "performance_profile": "Compact",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.set_performance_profile = MagicMock(return_value=True)
        sdc_module_mock.perform_module_operation()
        assert sdc_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_sdc_throws_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "performance_profile": "Compact",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.set_performance_profile = MagicMock(
            side_effect=MockApiException)
        sdc_module_mock.perform_module_operation()
        assert "Modifying performance profile of SDC " + MockSdcApi.SDC_ID + " failed with error" in \
            sdc_module_mock.module.fail_json.call_args[1]['msg']

    def test_rename_sdc(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "sdc_new_name": "test_sdc_renamed",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.rename = MagicMock(return_value=True)
        sdc_module_mock.perform_module_operation()
        assert sdc_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_rename_sdc_throws_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "sdc_new_name": "test_sdc_renamed",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.rename = MagicMock(side_effect=MockApiException)
        sdc_module_mock.perform_module_operation()
        assert "Failed to rename SDC" in \
            sdc_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_sdc(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "state": "absent"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.delete = MagicMock(return_value=True)
        sdc_module_mock.perform_module_operation()
        assert sdc_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_sdc_throws_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_ip": "1.1.1.1",
            "state": "absent"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        sdc_module_mock.powerflex_conn.sdc.delete = MagicMock(side_effect=MockApiException)
        sdc_module_mock.perform_module_operation()
        assert "Removing SDC " + MockSdcApi.SDC_ID + " failed with error" in \
            sdc_module_mock.module.fail_json.call_args[1]['msg']
