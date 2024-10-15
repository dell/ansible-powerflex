# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for SDS module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sds_api import MockSDSApi
from ansible_collections.dellemc.powerflex.plugins.modules.sds import \
    SDSHandler
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase

from ansible_collections.dellemc.powerflex.plugins.modules.sds import PowerFlexSDS


class TestPowerflexSDS(PowerFlexUnitBase):

    get_module_args = MockSDSApi.SDS_COMMON_ARGS
    ip1 = "10.47.xxx.xxx"
    ip2 = "10.46.xxx.xxx"

    @pytest.fixture
    def module_object(self):
        return PowerFlexSDS

    def test_get_sds_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'sds_id': '8f3bb0cc00000002',
                'state': 'present'
            })
        powerflex_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST)
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.get.assert_called()

    def test_get_sds_name_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST)
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.get.assert_called()

    def test_get_sds_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.sds.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'get_sds_exception'), powerflex_module_mock, SDSHandler)

    def test_create_sds_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'performance_profile': "HighPerformance",
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=None)
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.create.assert_called()

    def test_create_sds_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'performance_profile': "HighPerformance",
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        powerflex_module_mock.get_fault_set = MagicMock(
            return_value=MockSDSApi.FAULT_SET_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.sds.create = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_exception'), powerflex_module_mock, SDSHandler)

    def test_rename_sds_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_new_name": "node0_new",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.rename.assert_called()

    def test_modify_rfcache_enabled_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "rfcache_enabled": False,
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.set_rfcache_enabled.assert_called()

    def test_modify_rmcache_enabled_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "rmcache_enabled": False,
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.set_rmcache_enabled.assert_called()

    def test_modify_rmcache_size_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "rmcache_size": 256,
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.set_rmcache_size.assert_called()

    def test_rmcache_size_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': False,
                'rmcache_size': 128,
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'rmcache_size_exception'), powerflex_module_mock, SDSHandler)

    def test_create_sds_wo_sds_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'sds_name': None,
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_wo_sds_name'), powerflex_module_mock, SDSHandler)

    def test_create_sds_wo_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'state': "present"
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=None)
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_wo_pd'), powerflex_module_mock, SDSHandler)

    def test_create_sds_wo_sds_ip_list_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list': [],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_wo_sds_ip_list'), powerflex_module_mock, SDSHandler)

    def test_create_sds_incorrect_sds_ip_state_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'absent-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_incorrect_sds_ip_state'), powerflex_module_mock, SDSHandler)

    def test_create_sds_sds_id_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'sds_id': "sds_id_1",
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_sds_id'), powerflex_module_mock, SDSHandler)

    def test_create_sds_sds_new_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'sds_new_name': "sds_new_name",
                'protection_domain_name': 'test_domain',
                'fault_set_name': 'fault_set_name',
                'sds_ip_list':
                [
                    {
                        'ip': self.ip1,
                        'role': "all"
                    }
                ],
                'sds_ip_state': 'present-in-sds',
                'rmcache_enabled': True,
                'rmcache_size': 128,
                'state': "present"
            })
        pd_resp = MockSDKResponse(MockSDSApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'])
        fs_resp = MockSDSApi.FAULT_SET_GET_LIST
        powerflex_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fs_resp)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'create_sds_sds_new_name'), powerflex_module_mock, SDSHandler)

    def test_modify_performance_profile_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "performance_profile": "Compact",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.set_performance_parameters.assert_called()

    def test_rename_sds_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_new_name": "node0_new",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.sds.rename = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'rename_sds_exception'), powerflex_module_mock, SDSHandler)

    def test_rename_sds_empty_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_new_name": "",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'rename_sds_empty_exception'), powerflex_module_mock, SDSHandler)

    def test_update_role_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": self.ip2,
                        "role": "all"
                    }
                ],
                "sds_ip_state": "present-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.set_ip_role.assert_called()

    def test_update_role_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": self.ip2,
                        "role": "all"
                    }
                ],
                "sds_ip_state": "present-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.sds.set_ip_role = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'set_ip_role_exception'), powerflex_module_mock, SDSHandler)

    def test_add_ip_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": "10.xx.xx.xx",
                        "role": "all"
                    }
                ],
                "sds_ip_state": "present-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.add_ip.assert_called()

    def test_add_ip_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": "10.xx.xx.xx",
                        "role": "all"
                    }
                ],
                "sds_ip_state": "present-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.sds.add_ip = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'add_ip_exception'), powerflex_module_mock, SDSHandler)

    def test_remove_ip_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": self.ip2,
                        "role": "sdcOnly"
                    }
                ],
                "sds_ip_state": "absent-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.remove_ip.assert_called()

    def test_remove_ip_idempotent(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": "10.45.xxx.xxx",
                        "role": "sdcOnly"
                    }
                ],
                "sds_ip_state": "absent-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.get.assert_called()

    def test_remove_ip_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "sds_ip_list":
                [
                    {
                        "ip": self.ip2,
                        "role": "sdcOnly"
                    }
                ],
                "sds_ip_state": "absent-in-sds",
                "state": "present"
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.sds.remove_ip = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'remove_ip_exception'), powerflex_module_mock, SDSHandler)

    def test_delete_sds_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'state': 'absent'
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        SDSHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.sds.delete.assert_called()

    def test_delete_fault_set_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'state': 'absent'
            })
        powerflex_module_mock.get_sds_details = MagicMock(
            return_value=MockSDSApi.SDS_GET_LIST[0])
        powerflex_module_mock.powerflex_conn.sds.delete = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockSDSApi.get_sds_exception_response(
                'delete_sds_exception'), powerflex_module_mock, SDSHandler)
