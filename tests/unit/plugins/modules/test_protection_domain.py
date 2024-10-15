# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Protection Domain module on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_protection_domain_api \
    import MockProtectionDomainApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.protection_domain \
    import PowerFlexProtectionDomain


class TestPowerflexProtectionDomain(PowerFlexUnitBase):

    get_module_args = MockProtectionDomainApi.PD_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexProtectionDomain

    @pytest.mark.parametrize("params", [
        {'protection_domain_id': MockProtectionDomainApi.PD_ID},
        {"protection_domain_name": MockProtectionDomainApi.PD_NAME},
    ])
    def test_get_protection_domain_response(self, powerflex_module_mock, params):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': params.get('protection_domain_id', None),
                'protection_domain_name': params.get('protection_domain_name', None)
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.get.assert_called()

    def test_get_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainApi.PD_ID,
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockApiException())
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('get_pd_failed_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_validate_input_empty_params(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': ''
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('empty_pd_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_validate_network_limits_params(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'network_limits': {'overall_limit': -199,
                                   'bandwidth_unit': 'MBps'}
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('overall_limit_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_pd_new_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'protection_domain_new_name': MockProtectionDomainApi.PD_NAME
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('new_name_in_create'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_pd_(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.protection_domain.create = MagicMock(
            return_value=None
        )
        resp = powerflex_module_mock.create_protection_domain("protection_domain_name")
        assert resp is True
        powerflex_module_mock.powerflex_conn.protection_domain.create.assert_called()

    def test_rename_pd(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'protection_domain_new_name': MockProtectionDomainApi.PD_NEW_NAME,
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.rename.assert_called()

    def test_rename_pd_execption(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'protection_domain_new_name': MockProtectionDomainApi.PD_NEW_NAME,
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('rename_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_inactivate_pd(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'is_active': False
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.inactivate.assert_called()

    def test_activate_pd(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainApi.PD_ID,
                'is_active': True
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN_1)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.activate.assert_called()

    def test_create_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'is_active': False
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[]
        )
        powerflex_module_mock.powerflex_conn.protection_domain.create = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('create_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_modify_network_limits(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'network_limits': {'overall_limit': 15,
                                   'bandwidth_unit': 'GBps',
                                   'rebalance_limit': 10,
                                   'rebuild_limit': 10,
                                   'vtree_migration_limit': 10}
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.network_limits.assert_called()

    def test_modify_network_limits_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainApi.PD_ID,
                'network_limits': {'overall_limit': 15,
                                   'bandwidth_unit': 'GBps',
                                   'rebalance_limit': 10,
                                   'rebuild_limit': 10,
                                   'vtree_migration_limit': 10}
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.network_limits = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('modify_network_limits_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_enable_rf_cache(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'rf_cache_limits': {'is_enabled': True,
                                    'page_size': 10,
                                    'max_io_limit': 10,
                                    'pass_through_mode': 'Read'}
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.set_rfcache_enabled.assert_called()
        powerflex_module_mock.powerflex_conn.protection_domain.rfcache_parameters.assert_called()

    def test_modify_rf_cache_params_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'rf_cache_limits': {'is_enabled': True, 'page_size': 10,
                                    'max_io_limit': 10, 'pass_through_mode': 'Read'}
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.set_rfcache_enabled = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('rf_cache_limits_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_delete_pd(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME,
                'state': 'absent'
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.delete.assert_called()

    def test_delete_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainApi.PD_ID,
                'state': 'absent'
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.delete = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('delete_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_get_sp(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainApi.PD_NAME
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get_storage_pools = MagicMock(
            return_value=MockProtectionDomainApi.STORAGE_POOL)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.get_storage_pools.assert_called()

    def test_get_sp_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainApi.PD_ID
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockProtectionDomainApi.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.get_storage_pools = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainApi.get_failed_msgs('get_sp_exception'),
            powerflex_module_mock, invoke_perform_module=True)
