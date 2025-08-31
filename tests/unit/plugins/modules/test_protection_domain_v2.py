# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for protection domain module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from mock.mock import patch, MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.protection_domain_v2 \
    import PowerFlexProtectionDomainV2
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_protection_domain_api_v2 import \
    MockProtectionDomainV2Api


class TestPowerflexProtectionDomainV2(PowerFlexUnitBase):
    get_module_args = MockProtectionDomainV2Api.PD_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexProtectionDomainV2

    @pytest.mark.parametrize(
        "params, expected_method", [
            (
                {'protection_domain_id': MockProtectionDomainV2Api.PD_ID},
                'get_by_id'
            ),
            (
                {"protection_domain_name": MockProtectionDomainV2Api.PD_NAME},
                'get_by_name'
            ),
        ]
    )
    def test_get_protection_domain_response(self, powerflex_module_mock, params, expected_method):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': params.get('protection_domain_id'),
                'protection_domain_name': params.get('protection_domain_name'),
            }
        )

        mock_get_by_id = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        mock_get_by_name = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        mock_update = MagicMock(return_value=(
            False, MockProtectionDomainV2Api.PROTECTION_DOMAIN))

        powerflex_module_mock.powerflex_conn.protection_domain.get_by_id = mock_get_by_id
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = mock_get_by_name
        powerflex_module_mock.powerflex_conn.protection_domain.update = mock_update
        powerflex_module_mock.perform_module_operation()

        if expected_method == 'get_by_id':
            mock_get_by_id.assert_called_once_with(
                MockProtectionDomainV2Api.PD_ID)
        elif expected_method == 'get_by_name':
            mock_get_by_name.assert_called_once_with(
                MockProtectionDomainV2Api.PD_NAME)

    def test_validate_input_empty_params(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': ''
            })
        mock_get_by_id = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        mock_get_by_name = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        mock_update = MagicMock(return_value=(
            False, MockProtectionDomainV2Api.PROTECTION_DOMAIN))

        powerflex_module_mock.powerflex_conn.protection_domain.get_by_id = mock_get_by_id
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = mock_get_by_name
        powerflex_module_mock.powerflex_conn.protection_domain.update = mock_update

        self.capture_fail_json_call(
            MockProtectionDomainV2Api.get_failed_msgs('empty_pd_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_get_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainV2Api.PD_ID,
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_id = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockProtectionDomainV2Api.get_failed_msgs('get_pd_failed_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_pd_new_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
                'protection_domain_new_name': MockProtectionDomainV2Api.PD_NAME
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(
            MockProtectionDomainV2Api.get_failed_msgs('new_name_in_create'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_pd_(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainV2Api.PD_NAME
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.storage_pool.create = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.create.assert_called()

    def test_rename_pd(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
                'protection_domain_new_name': MockProtectionDomainV2Api.PD_NEW_NAME,
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.update = MagicMock(
            return_value=(False, MockProtectionDomainV2Api.PROTECTION_DOMAIN))
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.update.assert_called()

    def test_rename_pd_execption(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
                'protection_domain_new_name': MockProtectionDomainV2Api.PD_NEW_NAME,
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.update = MagicMock(
            return_value=(False, MockProtectionDomainV2Api.PROTECTION_DOMAIN))
        powerflex_module_mock.powerflex_conn.protection_domain.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainV2Api.get_failed_msgs('rename_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    # def test_update_pd_execption(self, powerflex_module_mock):
    #     self.set_module_params(
    #         powerflex_module_mock,
    #         self.get_module_args,
    #         {
    #             'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
    #             'protection_domain_new_name': MockProtectionDomainV2Api.PD_NEW_NAME,
    #         })
    #     powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
    #         return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
    #     powerflex_module_mock.powerflex_conn.protection_domain.update = MagicMock(
    #         side_effect=MockApiException)
    #     self.capture_fail_json_call(
    #         MockProtectionDomainV2Api.get_failed_msgs('rename_pd_exception'),
    #         powerflex_module_mock, invoke_perform_module=True
    #     )

    # def test_inactivate_pd(self, powerflex_module_mock):
    #     self.set_module_params(
    #         powerflex_module_mock,
    #         self.get_module_args,
    #         {
    #             'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
    #             'is_active': False
    #         })
    #     powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
    #         return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
    #     # powerflex_module_mock.powerflex_conn.protection_domain.update = MagicMock(
    #     #     return_value=(False, MockProtectionDomainV2Api.PROTECTION_DOMAIN))
    #     powerflex_module_mock.perform_module_operation()
    #     powerflex_module_mock.powerflex_conn.protection_domain.update.assert_called()
    #
    # def test_activate_pd(self, powerflex_module_mock):
    #     self.set_module_params(
    #         powerflex_module_mock,
    #         self.get_module_args,
    #         {
    #             'protection_domain_id': MockProtectionDomainV2Api.PD_ID,
    #             'is_active': True
    #         })
    #     powerflex_module_mock.powerflex_conn.protection_domain.get_by_id = MagicMock(
    #         return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN_1)
    #     powerflex_module_mock.perform_module_operation()
    #     powerflex_module_mock.powerflex_conn.protection_domain.activate.assert_called()

    def test_create_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
                'is_active': False
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.protection_domain.create = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainV2Api.get_failed_msgs('create_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_delete_pd(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_name': MockProtectionDomainV2Api.PD_NAME,
                'state': 'absent'
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.update = MagicMock(
            return_value=(False, MockProtectionDomainV2Api.PROTECTION_DOMAIN))
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.protection_domain.delete.assert_called()

    def test_delete_pd_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'protection_domain_id': MockProtectionDomainV2Api.PD_ID,
                'state': 'absent'
            })
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_id = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.delete = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockProtectionDomainV2Api.get_failed_msgs('delete_pd_exception'),
            powerflex_module_mock, invoke_perform_module=True
        )

    def test_check_mode(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.protection_domain.get_by_name = MagicMock(
            return_value=MockProtectionDomainV2Api.PROTECTION_DOMAIN)
        powerflex_module_mock.powerflex_conn.protection_domain.need_update = MagicMock(
            return_value=(True, {})
        )
        with patch.object(powerflex_module_mock.module,
                          'check_mode',
                          return_value=True):
            self.set_module_params(
                powerflex_module_mock,
                self.get_module_args,
                {
                    "protection_domain_name": MockProtectionDomainV2Api.PD_NAME,
                    "protection_domain_new_name": MockProtectionDomainV2Api.PD_NEW_NAME,
                    "is_active": False,
                    "state": "present"
                })
            powerflex_module_mock.perform_module_operation()
            assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

            # self.set_module_params(
            #     powerflex_module_mock,
            #     self.get_module_args,
            #     {
            #         "storage_pool_name": "test_pool",
            #         "protection_domain_name": "test_pd_1",
            #         "protection_scheme": "TwoPlusTwo",
            #         "compression_method": "None",
            #         "state": "present"
            #     })
            # powerflex_module_mock.perform_module_operation()
            # assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True
