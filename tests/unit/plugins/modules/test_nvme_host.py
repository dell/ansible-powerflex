# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for NVMe host module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_nvme_host_api import MockNvmeHostApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.nvme_host import PowerFlexNvmeHost


class TestPowerflexNVMeHost():

    get_module_args = MockNvmeHostApi.COMMON_ARGS

    @pytest.fixture
    def nvme_host_module_mock(self, mocker):
        mocker.patch(
            MockNvmeHostApi.MODULE_UTILS_PATH + '.PowerFlexClient',
            new=MockApiException)
        nvme_host_module_mock = PowerFlexNvmeHost()
        nvme_host_module_mock.module.check_mode = False
        nvme_host_module_mock.module.fail_json = fail_json
        return nvme_host_module_mock

    def test_validate_parameter_no_id(self, nvme_host_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        try:
            nvme_host_module_mock.validate_parameters()
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response(
                "id_param") in fj_object.message

    def test_validate_parameter_no_param(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nqn": "",
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        try:
            nvme_host_module_mock.validate_parameters()
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response(
                "param") in fj_object.message

    def test_get_nvme_host_details(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nvme_host_name": "nvme_host_test",
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        nvme_host_module_mock.perform_module_operation()
        nvme_host_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_no_name_details(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nvme_host_name": "NVMeHost:da8f60fd00010000",
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details_none_name()
        )
        nvme_host_module_mock.perform_module_operation()
        nvme_host_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_details_nqn(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nqn": "test_nqn",
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        nvme_host_module_mock.perform_module_operation()
        nvme_host_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_details_exception(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nqn": "test_nqn",
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException
        )
        try:
            nvme_host_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response("fetch_host") in fj_object.message

    def test_get_nvme_host_no_filter(self, nvme_host_module_mock):
        nvme_host_module_mock.module.params = MockNvmeHostApi.COMMON_ARGS
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        result = nvme_host_module_mock.get_nvme_host()
        assert result is not None

    def test_process_create_host(self, nvme_host_module_mock):
        nvme_host_module_mock.powerflex_conn.host.create = MagicMock(
            return_value=MockNvmeHostApi.create_nvme_host()
        )
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        ret = nvme_host_module_mock.process_host_creation("test_nqn", None, "test_nvem_host", None, None)
        nvme_host_module_mock.powerflex_conn.host.create.assert_called()
        assert ret is not None

    def test_create_nvme_host(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nvme_host_name": "nvme_host_test_new",
            "nvme_host_new_name": "nvme_host_test_name",
            "state": "present"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        try:
            nvme_host_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response(
                "create_new_name") in fj_object.message

    def test_create_nvme_host_nqn_exception(self, nvme_host_module_mock):
        nvme_host_module_mock.module.params = self.get_module_args
        try:
            nvme_host_module_mock.create_nvme_host(None, "test_nvem_host", None, None)
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response(
                "create_host") in fj_object.message

    def test_modify_nvme_host(self, nvme_host_module_mock):
        details = MockNvmeHostApi.get_nvme_host_details()
        ret = nvme_host_module_mock.perform_modify(details[0], None, "5", "6")
        assert ret is True

    def test_rename_nvme_host(self, nvme_host_module_mock):
        details = MockNvmeHostApi.get_nvme_host_details()
        ret = nvme_host_module_mock.perform_modify(details[0], "new_name", "5", "6")
        assert ret is True

    def test_modify_nvme_host_rename_exception(self, nvme_host_module_mock):
        details = MockNvmeHostApi.get_nvme_host_details()
        nvme_host_module_mock.powerflex_conn.sdc.rename = MagicMock(
            side_effect=MockApiException
        )
        try:
            nvme_host_module_mock.perform_modify(details[0], "new_name", "5", "6")
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response("rename_host") in fj_object.message

    def test_modify_nvme_host_modify_max_num_paths_exception(self, nvme_host_module_mock):
        details = MockNvmeHostApi.get_nvme_host_details()
        nvme_host_module_mock.powerflex_conn.host.modify_max_num_paths = MagicMock(
            side_effect=MockApiException
        )
        try:
            nvme_host_module_mock.perform_modify(details[0], None, "5", "6")
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response("modify_host") in fj_object.message

    def test_modify_nvme_host_modify_max_num_sys_ports_exception(self, nvme_host_module_mock):
        details = MockNvmeHostApi.get_nvme_host_details()
        nvme_host_module_mock.powerflex_conn.host.modify_max_num_sys_ports = MagicMock(
            side_effect=MockApiException
        )
        try:
            nvme_host_module_mock.perform_modify(details[0], None, "3", "6")
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response("modify_host") in fj_object.message

    def test_delete_nvme_host(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nvme_host_name": "nvme_host_test",
            "nqn": "test_nqn",
            "state": "absent"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        nvme_host_module_mock.perform_module_operation()
        nvme_host_module_mock.powerflex_conn.sdc.delete.assert_called()

    def test_delete_nvme_host_exception(self, nvme_host_module_mock):
        self.get_module_args.update({
            "nvme_host_name": "test_nvem_host",
            "nqn": "test_nqn",
            "state": "absent"
        })
        nvme_host_module_mock.module.params = self.get_module_args
        nvme_host_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNvmeHostApi.get_nvme_host_details()
        )
        nvme_host_module_mock.powerflex_conn.sdc.delete = MagicMock(
            side_effect=MockApiException
        )
        try:
            nvme_host_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert MockNvmeHostApi.get_exception_response("delete_host") in fj_object.message
