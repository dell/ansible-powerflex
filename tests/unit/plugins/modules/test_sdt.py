# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for SDT module on PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import (
    initial_mock,
)
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdt_api import (
    MockSDTApi,
)
from ansible_collections.dellemc.powerflex.plugins.modules.sdt import SDTHandler
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdk_response import (
    MockSDKResponse,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base import (
    PowerFlexUnitBase,
)

from ansible_collections.dellemc.powerflex.plugins.modules.sdt import PowerFlexSDT


class TestPowerflexSDT(PowerFlexUnitBase):

    get_module_args = MockSDTApi.SDT_COMMON_ARGS
    ip1 = "10.47.xxx.xxx"
    ip2 = "10.46.xxx.xxx"
    ip3 = "10.45.xxx.xxx"

    @pytest.fixture
    def module_object(self):
        return PowerFlexSDT

    def test_get_sdt_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "state": "present"},
        )
        powerflex_module_mock.powerflex_conn.sdt.get = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST
        )
        pd_resp = MockSDKResponse(MockSDTApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__["data"]["protectiondomain"]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.get.assert_called()

    def test_get_sdt_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "state": "present"},
        )
        powerflex_module_mock.powerflex_conn.sdt.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("get_sdt_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_create_sdt_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "protection_domain_name": "test_domain",
                "sdt_ip_list": [{"ip": self.ip1, "role": "StorageAndHost"}],
                "sdt_name": "sdt2",
                "storage_port": 12200,
                "nvme_port": 4420,
                "discovery_port": 8009,
                "state": "present",
            },
        )
        pd_resp = MockSDKResponse(MockSDTApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__["data"]["protectiondomain"]
        )
        powerflex_module_mock.powerflex_conn.sdt.get = MagicMock(return_value=[])
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.create.assert_called()

    def test_create_sdt_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "protection_domain_name": "test_domain",
                "sdt_ip_list": [{"ip": self.ip1, "role": "StorageAndHost"}],
                "sdt_name": "sdt2",
                "storage_port": 12200,
                "nvme_port": 4420,
                "discovery_port": 8009,
                "state": "present",
            },
        )
        pd_resp = MockSDKResponse(MockSDTApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__["data"]["protectiondomain"]
        )
        powerflex_module_mock.get_sdt_details = MagicMock(return_value=None)
        powerflex_module_mock.powerflex_conn.sdt.create = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("create_sdt_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_rename_sdt_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "sdt_new_name": "sdt2", "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.rename.assert_called()

    def test_rename_sdt_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "sdt_new_name": "sdt2", "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.sdt.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("rename_sdt_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_rename_sdt_empty_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_new_name": "", "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("rename_sdt_empty_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_modify_storage_port_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "storage_port": 12201, "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.set_storage_port.assert_called()

    def test_modify_nvme_port_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "nvme_port": 4421, "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.set_nvme_port.assert_called()

    def test_modify_discovery_port_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "discovery_port": 8008, "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.set_discovery_port.assert_called()

    def test_enter_maintenance_mode_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "maintenance_mode": "active", "state": "present"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.enter_maintenance_mode.assert_called()

    def test_exit_maintenance_mode_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "maintenance_mode": "inactive", "state": "present"},
        )
        MockSDTApi.SDT_GET_LIST[0]["maintenanceState"] = 'InMaintenance'
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.exit_maintenance_mode.assert_called()

    def test_add_ip_list_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [
                    {"ip": self.ip1, "role": "StorageAndHost"},
                    {"ip": self.ip2, "role": "StorageAndHost"},
                    {"ip": self.ip3, "role": "StorageAndHost"},
                ],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.add_ip.assert_called()

    def test_add_ip_list_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [
                    {"ip": self.ip1, "role": "StorageAndHost"},
                    {"ip": self.ip2, "role": "StorageAndHost"},
                    {"ip": self.ip3, "role": "StorageAndHost"},
                ],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.sdt.add_ip = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("add_ip_list_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_remove_ip_list_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [{"ip": self.ip1, "role": "StorageAndHost"}],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.remove_ip.assert_called()

    def test_remove_ip_list_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [
                    {"ip": self.ip1, "role": "StorageAndHost"},
                ],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.sdt.remove_ip = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("remove_ip_list_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_set_ip_role_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [
                    {"ip": self.ip1, "role": "StorageOnly"},
                    {"ip": self.ip2, "role": "StorageAndHost"},
                ],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.set_ip_role.assert_called()

    def test_set_ip_role_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [
                    {"ip": self.ip1, "role": "StorageOnly"},
                    {"ip": self.ip2, "role": "StorageAndHost"},
                ],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.sdt.set_ip_role = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("set_ip_role_exception"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_change_ip_list_complex_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt1",
                "sdt_ip_list": [
                    {"ip": self.ip1, "role": "StorageOnly"},
                    {"ip": self.ip3, "role": "StorageAndHost"},
                ],
                "state": "present",
            },
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.add_ip.assert_called()
        powerflex_module_mock.powerflex_conn.sdt.remove_ip.assert_called()
        powerflex_module_mock.powerflex_conn.sdt.set_ip_role.assert_called()

    def test_create_sdt_without_sdt_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": None,
                "protection_domain_name": "test_domain",
                "sdt_ip_list": [{"ip": self.ip1, "role": "StorageAndHost"}],
                "storage_port": 12200,
                "nvme_port": 4420,
                "state": "present",
            },
        )
        pd_resp = MockSDKResponse(MockSDTApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__["data"]["protectiondomain"]
        )
        powerflex_module_mock.get_sdt_details = MagicMock(return_value=None)
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("create_sdt_without_sdt_name"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_create_sdt_without_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sdt_name": "sdt2",
                "sdt_ip_list": [{"ip": self.ip1, "role": "StorageAndHost"}],
                "storage_port": 12200,
                "nvme_port": 4420,
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=None
        )
        powerflex_module_mock.get_sdt_details = MagicMock(return_value=None)
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("create_sdt_without_pd"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_create_sdt_without_sdt_ip_list_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "protection_domain_name": "test_domain",
                "sdt_name": "sdt2",
                "sdt_ip_list": [],
                "storage_port": 12200,
                "nvme_port": 4420,
                "state": "present",
            },
        )
        pd_resp = MockSDKResponse(MockSDTApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__["data"]["protectiondomain"]
        )
        powerflex_module_mock.get_sdt_details = MagicMock(return_value=None)
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("create_sdt_without_sdt_ip_list"),
            powerflex_module_mock,
            SDTHandler,
        )

    def test_delete_sdt_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "state": "absent"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        SDTHandler().handle(powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sdt.delete.assert_called()

    def test_delete_sdt_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"sdt_name": "sdt1", "state": "absent"},
        )
        powerflex_module_mock.get_sdt_details = MagicMock(
            return_value=MockSDTApi.SDT_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.sdt.delete = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSDTApi.get_sdt_exception_response("delete_sdt_exception"),
            powerflex_module_mock,
            SDTHandler,
        )
