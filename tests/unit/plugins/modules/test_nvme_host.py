# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for NVMe host module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_nvme_host_api import MockNVMeHostApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.plugins.modules.nvme_host \
    import PowerFlexNVMeHost, NVMeHostHandler

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()


class TestPowerflexNVMeHost(PowerFlexUnitBase):

    get_module_args = MockNVMeHostApi.COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexNVMeHost

    def test_invalid_nvme_host_params(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'nqn': ''
            })
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'invalid_params'), powerflex_module_mock, NVMeHostHandler)

    def test_get_nvme_host_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'nqn': 'test_nqn',
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_no_name_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'nqn': 'test_nqn',
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_NO_NAME_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_using_name_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'nvme_host_name': 'nvme_host_test',
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'nvme_host_name': 'nvme_host_test',
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'get_host'), powerflex_module_mock, NVMeHostHandler)

    def test_create_nvme_host(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present"
            })
        powerflex_module_mock.get_nvme_host = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.host.create.assert_called()

    def test_create_nvme_host_no_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nqn": "test_nqn",
                "state": "present"
            })
        powerflex_module_mock.get_nvme_host = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.host.create = MagicMock(
            side_effect=MockNVMeHostApi.NVME_HOST_NO_NAME_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.host.create.assert_called()

    def test_create_nvme_host_check_mode(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present"
            })
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.module._diff = True
        powerflex_module_mock.get_nvme_host = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True
        assert powerflex_module_mock.module.exit_json.call_args[1]['diff']['after']['nvme_host_name'] == "nvme_host_test"

    def test_create_nvme_host_no_nqn_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "state": "present"
            })
        powerflex_module_mock.get_nvme_host = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'create_host'), powerflex_module_mock, NVMeHostHandler)

    def test_create_nvme_host_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present"
            })
        powerflex_module_mock.get_nvme_host = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        powerflex_module_mock.powerflex_conn.host.create = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'create_host'), powerflex_module_mock, NVMeHostHandler)

    def test_modify_nvme_host(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present",
                "nvme_host_new_name": "fs_new_name",
                "max_num_paths": "4",
                "max_num_sys_ports": "10"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdc.rename.assert_called()
        powerflex_module_mock.powerflex_conn.host.modify_max_num_sys_ports.assert_called()
        powerflex_module_mock.powerflex_conn.host.modify_max_num_paths.assert_called()

    def test_modify_nvme_host_check_mode(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present",
                "nvme_host_new_name": "nvme_host_test_new_name",
                "max_num_paths": "4",
                "max_num_sys_ports": "10"
            })
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.module._diff = True
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True
        assert powerflex_module_mock.module.exit_json.call_args[1]['diff']['after']['name'] == "nvme_host_test_new_name"

    def test_rename_nvme_host_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present",
                "nvme_host_new_name": "fs_new_name",
                "max_num_paths": "4",
                "max_num_sys_ports": "10"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.sdc.rename = MagicMock(
            side_effect=MockApiException)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'modify_host'), powerflex_module_mock, NVMeHostHandler)

    def test_modify_max_num_sys_ports_nvme_host_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present",
                "nvme_host_new_name": "fs_new_name",
                "max_num_paths": "4",
                "max_num_sys_ports": "10"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        powerflex_module_mock.powerflex_conn.host.modify_max_num_sys_ports = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'modify_host'), powerflex_module_mock, NVMeHostHandler)

    def test_modify_max_num_paths_nvme_host_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present",
                "nvme_host_new_name": "fs_new_name",
                "max_num_paths": "4",
                "max_num_sys_ports": "10"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        powerflex_module_mock.powerflex_conn.sdc.modify_max_num_paths = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'modify_host'), powerflex_module_mock, NVMeHostHandler)

    def test_modify_max_num_paths_nvme_host_version_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nvme_host_name": "nvme_host_test",
                "nqn": "test_nqn",
                "state": "present",
                "max_num_paths": "4",
                "max_num_sys_ports": "10"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS_4_5
        )
        powerflex_module_mock.powerflex_conn.sdc.modify_max_num_paths = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'modify_host_version_check'), powerflex_module_mock, NVMeHostHandler)

    def test_delete_nvme_host(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nqn": 'test_nqn',
                "state": "absent"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdc.delete.assert_called()

    def test_delete_nvme_host_check_mode(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nqn": 'test_nqn',
                "state": "absent"
            })
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.module._diff = True
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        NVMeHostHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True
        assert powerflex_module_mock.module.exit_json.call_args[1]['diff']['after'] == {}

    def test_delete_nvme_host_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "nqn": 'test_nqn',
                "state": "absent"
            })
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockNVMeHostApi.NVME_HOST_DETAILS)
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockNVMeHostApi.INFO_ARRAY_DETAILS
        )
        powerflex_module_mock.powerflex_conn.sdc.delete = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockNVMeHostApi.get_exception_response(
                'delete_host'), powerflex_module_mock, NVMeHostHandler)
