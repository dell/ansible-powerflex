# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for SDC module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdc_api import MockSdcApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fail_json \
    import FailJsonException, fail_json

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.sdc import PowerFlexSdc


class TestPowerflexSdc():

    get_module_args = MockSdcApi.COMMON_ARGS

    @pytest.fixture
    def sdc_module_mock(self, mocker):
        mocker.patch(
            MockSdcApi.MODULE_UTILS_PATH + '.PowerFlexClient',
            new=MockApiException)
        sdc_module_mock = PowerFlexSdc()
        sdc_module_mock.module.check_mode = False
        sdc_module_mock.module.fail_json = fail_json
        return sdc_module_mock

    def capture_fail_json_call(self, error_msg, sdc_module_mock):
        try:
            sdc_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

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

    def test_get_sdc_details_empty_sdc_id_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_id": " ",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'get_sdc_details_empty_sdc_id_exception'), sdc_module_mock)

    def test_get_sdc_details_with_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_id": MockSdcApi.SDC_ID,
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'get_sdc_details_with_exception'), sdc_module_mock)

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
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'get_sdc_details_mapped_volumes_with_exception'), sdc_module_mock)

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
        sdc_module_mock.powerflex_conn.sdc.set_performance_profile.assert_called()

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
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'modify_sdc_throws_exception'), sdc_module_mock)

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
        sdc_module_mock.powerflex_conn.sdc.rename.assert_called()

    def test_rename_sdc_empty_new_name_exception(self, sdc_module_mock):
        self.get_module_args.update({
            "sdc_name": "test_sdc",
            "sdc_new_name": " ",
            "state": "present"
        })
        sdc_module_mock.module.params = self.get_module_args
        sdc_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockSdcApi.get_sdc_details()
        )
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'rename_sdc_empty_new_name_exception'), sdc_module_mock)

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
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'rename_sdc_throws_exception'), sdc_module_mock)

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
        sdc_module_mock.powerflex_conn.sdc.delete.assert_called()

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
        self.capture_fail_json_call(MockSdcApi.get_sdc_exception_response(
            'remove_sdc_throws_exception'), sdc_module_mock)
