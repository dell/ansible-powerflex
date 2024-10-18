# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for fault set module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fault_set_api import MockFaultSetApi
from ansible_collections.dellemc.powerflex.plugins.modules.fault_set import \
    FaultSetHandler
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase

from ansible_collections.dellemc.powerflex.plugins.modules.fault_set import PowerFlexFaultSet


class TestPowerflexFaultSet(PowerFlexUnitBase):

    get_module_args = MockFaultSetApi.FAULT_SET_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexFaultSet

    def test_get_fault_set_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'fault_set_id': 'fault_set_id_1',
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=MockFaultSetApi.FAULT_SET_GET_LIST)
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        FaultSetHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.fault_set.get.assert_called()

    def test_get_fault_set_name_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'fault_set_name': 'fault_set_name_1',
                'protection_domain_id': 'test_pd_id_1',
                'state': "present"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=MockFaultSetApi.FAULT_SET_GET_LIST)
        FaultSetHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.fault_set.get.assert_called()

    def test_create_fault_set_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": "test_fs_1",
                "protection_domain_name": "test_pd_1",
                "state": "present"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=None)
        FaultSetHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.fault_set.create.assert_called()

    def test_create_fault_set_wo_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": "test_fs_1",
                "state": "present"
            })
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=None)
        self.capture_fail_json_call(
            MockFaultSetApi.get_fault_set_exception_response(
                'create_fault_set_wo_pd_exception'), powerflex_module_mock, FaultSetHandler)

    def test_create_fault_set_empty_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": " ",
                "protection_domain_name": "test_pd_1",
                "state": "present"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=None)
        self.capture_fail_json_call(
            MockFaultSetApi.get_fault_set_exception_response(
                'create_fault_set_empty_name_exception'), powerflex_module_mock, FaultSetHandler)

    def test_create_fault_set_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": "test_fs_1",
                "protection_domain_name": "test_pd_1",
                "state": "present"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.fault_set.create = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFaultSetApi.get_fault_set_exception_response(
                'create_fault_set_exception'), powerflex_module_mock, FaultSetHandler)

    def test_rename_fault_set_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": 'fault_set_name_1',
                "protection_domain_name": "test_pd_1",
                "fault_set_new_name": "fs_new_name",
                "state": "present"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=MockFaultSetApi.FAULT_SET_GET_LIST[0])
        FaultSetHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.fault_set.rename.assert_called()

    def test_rename_fault_set_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": 'fault_set_name_1',
                "protection_domain_name": "test_pd_1",
                "fault_set_new_name": "fs_new_name",
                "state": "present"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=MockFaultSetApi.FAULT_SET_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.fault_set.rename = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFaultSetApi.get_fault_set_exception_response(
                'rename_fault_set_exception'), powerflex_module_mock, FaultSetHandler)

    def test_delete_fault_set_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": 'test_fs_1',
                "protection_domain_name": "test_pd_1",
                "state": "absent"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=MockFaultSetApi.FAULT_SET_GET_LIST[0])
        FaultSetHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.fault_set.delete.assert_called()

    def test_delete_fault_set_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "fault_set_name": 'test_fs_1',
                "protection_domain_name": "test_pd_1",
                "state": "absent"
            })
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=MockFaultSetApi.FAULT_SET_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.fault_set.delete = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockFaultSetApi.get_fault_set_exception_response(
                'delete_fault_set_exception'), powerflex_module_mock, FaultSetHandler)
