# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for Protection Domain module on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_protection_domain_api import MockProtectionDomainApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.protection_domain import PowerFlexProtectionDomain


class TestPowerflexProtectionDomain():

    get_module_args = {
        'hostname': '**.***.**.***',
        'protection_domain_id': '7bd6457000000000',
        'protection_domain_name': None,
        'protection_domain_new_name': None,
        'is_active': True,
        'network_limits': {
            'rebuild_limit': 10240,
            'rebalance_limit': 10240,
            'vtree_migration_limit': 10240,
            'overall_limit': 20480,
            'bandwidth_unit': 'KBps',
        },
        'rf_cache_limits': {
            'is_enabled': None,
            'page_size': 4,
            'max_io_limit': 16,
            'pass_through_mode': 'None'
        },
        'state': 'present'
    }

    @pytest.fixture
    def protection_domain_module_mock(self, mocker):
        mocker.patch(MockProtectionDomainApi.MODULE_UTILS_PATH + '.PowerFlexClient', new=MockApiException)
        protection_domain_module_mock = PowerFlexProtectionDomain()
        return protection_domain_module_mock

    def test_get_protection_domain_response(self, protection_domain_module_mock):
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.perform_module_operation()
        protection_domain_module_mock.powerflex_conn.protection_domain.get.assert_called()

    def test_create_protection_domain(self, protection_domain_module_mock):
        self.get_module_args.update({
            "protection_domain_name": "test_domain",
            "state": "present"
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.get_protection_domain = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain'][0]
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.create = MagicMock(return_values=None)
        protection_domain_module_mock.perform_module_operation()
        assert (self.get_module_args['protection_domain_name'] ==
                protection_domain_module_mock.module.exit_json.call_args[1]["protection_domain_details"]['name'])
        assert protection_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_protection_domain(self, protection_domain_module_mock):
        self.get_module_args.update({
            'network_limits': {
                'rebuild_limit': 10,
                'rebalance_limit': 10,
                'vtree_migration_limit': 11,
                'overall_limit': 21,
                'bandwidth_unit': 'GBps',
            }
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        sp_resp = MockSDKResponse(MockProtectionDomainApi.STORAGE_POOL)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.get_storage_pools = MagicMock(
            return_value=sp_resp.__dict__['data']['storagepool']
        )
        protection_domain_module_mock.perform_module_operation()
        protection_domain_module_mock.powerflex_conn.protection_domain.network_limits.assert_called()

    def test_rename_protection_domain(self, protection_domain_module_mock):
        self.get_module_args.update({
            'protection_domain_new_name': 'new_test_domain'
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.perform_module_operation()
        protection_domain_module_mock.powerflex_conn.protection_domain.rename.assert_called()

    def test_inactivate_protection_domain(self, protection_domain_module_mock):
        self.get_module_args.update({
            'is_active': False
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.perform_module_operation()
        protection_domain_module_mock.powerflex_conn.protection_domain. \
            inactivate.assert_called()

    def test_activate_protection_domain(self, protection_domain_module_mock):
        self.get_module_args.update({
            'is_active': True
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.activate = MagicMock(return_value=None)
        protection_domain_module_mock.perform_module_operation()
        assert protection_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_protection_domain(self, protection_domain_module_mock):
        self.get_module_args.update({
            'protection_domain_name': 'new_test_domain',
            'state': 'absent'
        })
        protection_domain_module_mock.module.params = self.get_module_args
        protection_domain_module_mock.get_protection_domain = MagicMock(return_values=None)
        protection_domain_module_mock.perform_module_operation()
        assert protection_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_protection_domain_throws_exception(self, protection_domain_module_mock):
        self.get_module_args.update({
            'protection_domain_id': '7bd6457000000000',
            'state': 'absent'
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.delete = MagicMock(
            side_effect=utils.PowerFlexClient)
        protection_domain_module_mock.perform_module_operation()
        assert MockProtectionDomainApi.delete_pd_failed_msg(self.get_module_args['protection_domain_id']) in \
               protection_domain_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_with_404_exception(self, protection_domain_module_mock):
        MockProtectionDomainApi.status = 404
        self.get_module_args.update({
            "protection_domain_name": "test_domain1"
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.create = MagicMock(
            side_effect=utils.PowerFlexClient)
        protection_domain_module_mock.perform_module_operation()
        assert protection_domain_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_protection_domain_throws_exception(self, protection_domain_module_mock):
        self.get_module_args.update({
            "protection_domain_id": "7bd6457000000000",
            'rf_cache_limits': {
                'is_enabled': True,
                'page_size': 64,
                'max_io_limit': 128,
                'pass_through_mode': 'invalid_Read'
            }
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.set_rfcache_enabled = MagicMock(
            side_effect=utils.PowerFlexClient)
        protection_domain_module_mock.perform_module_operation()
        assert MockProtectionDomainApi.modify_pd_with_failed_msg(self.get_module_args['protection_domain_id']) in \
               protection_domain_module_mock.module.fail_json.call_args[1]['msg']

    def test_rename_protection_domain_invalid_value(self, protection_domain_module_mock):
        self.get_module_args.update({
            "protection_domain_name": "test_domain",
            "protection_domain_new_name": "  test domain",
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.rename = MagicMock(
            side_effect=utils.PowerFlexClient)
        protection_domain_module_mock.perform_module_operation()
        assert MockProtectionDomainApi.rename_pd_failed_msg(self.get_module_args['protection_domain_id']) in \
               protection_domain_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_protection_domain_invalid_param(self, protection_domain_module_mock):
        self.get_module_args.update({
            "protection_domain_name": "test_domain1",
            "protection_domain_new_name": "new_domain",
            "state": "present"
        })
        protection_domain_module_mock.module.params = self.get_module_args
        pd_resp = MockSDKResponse(MockProtectionDomainApi.PROTECTION_DOMAIN)
        protection_domain_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp.__dict__['data']['protectiondomain']
        )
        protection_domain_module_mock.powerflex_conn.protection_domain.create = MagicMock(
            side_effect=utils.PowerFlexClient)
        protection_domain_module_mock.perform_module_operation()
        assert MockProtectionDomainApi.version_pd_failed_msg() in \
               protection_domain_module_mock.module.fail_json.call_args[1]['msg']
