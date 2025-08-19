# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for storage pool module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from mock.mock import patch, MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.storagepool_v2 \
    import PowerFlexStoragePoolV2
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storagepool_api_v2 import \
    MockStoragePoolV2Api


class TestPowerflexStoragePoolV2(PowerFlexUnitBase):
    get_module_args = MockStoragePoolV2Api.STORAGE_POOL_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexStoragePoolV2

    def test_get_storage_pool_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL))
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )

        # verify get_by_name
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name.assert_called()
        powerflex_module_mock.powerflex_conn.storage_pool.update.assert_called()

        # verify get_by_id
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_id": "5dac1b0300000000",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_id = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_id.assert_called()

    def test_incorrect_params(self, powerflex_module_mock):
        module_args = self.get_module_args.copy()
        module_args.update({"protection_domain_name": None})
        module_args.update({"protection_domain_id": None})
        self.set_module_params(
            powerflex_module_mock,
            module_args,
            {
                "storage_pool_name": "test_pool",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL))
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )

        self.capture_fail_json_call(
            MockStoragePoolV2Api.get_exception_response(
                'protection_domain_params'),
            module_mock=powerflex_module_mock,
            invoke_perform_module=True)

    def test_get_storage_pool_with_dg(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "device_group_id": "39a898be00000000",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL))
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )

        # verify get multiple device groups
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "device_group_name": "test_dg_1",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "state": "present"
            })
        with patch.object(powerflex_module_mock.powerflex_conn.device_group,
                          "get",
                          return_value=[]):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response(
                    'device_group_not_found'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

        # exception get device groups
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "device_group_name": "test_dg_1",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "state": "present"
            })
        with patch.object(powerflex_module_mock.powerflex_conn.device_group,
                          "get",
                          side_effect=MockApiException):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response(
                    'device_group_exception'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

        # verify mismatched device group id
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "device_group_id": "4eeb304600000002",
                "device_group_name": "test_dg_1",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "state": "present"
            })

        with patch.object(powerflex_module_mock.powerflex_conn.device_group,
                          "get",
                          return_value=MockStoragePoolV2Api.DEVICE_GROUP_DETAILS_1):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response(
                    'mismatch_device_group_id_exception'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

            # verify mismatched device group name
            self.set_module_params(
                powerflex_module_mock,
                self.get_module_args,
                {
                    "storage_pool_name": "test_pool",
                    "device_group_id": "39a898be00000000",
                    "device_group_name": "invalid_device_group_name",
                    "protection_domain_name": "test_pd_1",
                    "protection_scheme": "TwoPlusTwo",
                    "compression_method": "Normal",
                    "use_all_available_capacity": True,
                    "state": "present"
                })

            with patch.object(powerflex_module_mock.powerflex_conn.device_group,
                              "get",
                              return_value=MockStoragePoolV2Api.DEVICE_GROUP_DETAILS_1):
                self.capture_fail_json_call(
                    MockStoragePoolV2Api.get_exception_response(
                        'mismatch_device_group_name_exception'),
                    module_mock=powerflex_module_mock,
                    invoke_perform_module=True)

    def test_get_storagepool_details_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, None))
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        with patch.object(powerflex_module_mock.powerflex_conn.storage_pool,
                          "get_by_name",
                          side_effect=MockApiException):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response('get_details'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

    def test_get_storagepool_details_with_invalid_pd(self, powerflex_module_mock):
        # invalid PD id
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_id": "invalid_pd_id",
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL))
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        with patch.object(powerflex_module_mock.powerflex_conn.protection_domain,
                          'get',
                          return_value=MockStoragePoolV2Api.PROTECTION_DETAILS_1):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response('invalid_pd_id'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

        # mismatched PD name & id
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_id": "7bd6457000000000",
                "protection_domain_name": "invalid_pd_id",
                "state": "present"
            })
        with patch.object(powerflex_module_mock.powerflex_conn.protection_domain,
                          'get',
                          return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain']):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response('invalid_pd_name'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

    def test_get_storagepool_details_with_invalid_dg(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "device_group_id": "invalid_dg_id",
                "state": "present"
            })
        powerflex_module_mock.module.params = self.get_module_args

        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL))
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        with patch.object(powerflex_module_mock.powerflex_conn.device_group,
                          'get',
                          return_value=MockStoragePoolV2Api.DEVICE_GROUP_DETAILS_1):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response('invalid_dg_id'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

    def test_create_storagepool_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.storage_pool.create = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.create.assert_called()

        # create with PD name only
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_id": None,
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "state": "present"
            })
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.create.assert_called()

    def test_create_storagepool_params(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": True,
                "physical_size_gb": 4096,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.storage_pool.create = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )

        self.capture_fail_json_call(
            MockStoragePoolV2Api.get_exception_response(
                'physical_size_gb_should_not_specify'),
            module_mock=powerflex_module_mock,
            invoke_perform_module=True)

        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "Normal",
                "use_all_available_capacity": False,
                "physical_size_gb": None,
                "state": "present"
            })
        self.capture_fail_json_call(
            MockStoragePoolV2Api.get_exception_response(
                'physical_size_gb_must_specify'),
            module_mock=powerflex_module_mock,
            invoke_perform_module=True)

    def test_create_storagepool_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_name": "test_pd_0",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "None",
                "use_all_available_capacity": True,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        with patch.object(powerflex_module_mock.powerflex_conn.storage_pool,
                          'create',
                          side_effect=MockApiException):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response(
                    'create_storage_pool'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

    def test_check_mode(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.storage_pool.need_update = MagicMock(
            return_value=(True, {})
        )
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        with patch.object(powerflex_module_mock.module,
                          'check_mode',
                          return_value=True):
            self.set_module_params(
                powerflex_module_mock,
                self.get_module_args,
                {
                    "storage_pool_name": "test_pool",
                    "protection_domain_name": "test_pd_1",
                    "protection_scheme": "TwoPlusTwo",
                    "compression_method": "None",
                    "use_all_available_capacity": True,
                    "state": "present"
                })
            powerflex_module_mock.perform_module_operation()
            assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

            self.set_module_params(
                powerflex_module_mock,
                self.get_module_args,
                {
                    "storage_pool_name": "test_pool",
                    "protection_domain_name": "test_pd_1",
                    "protection_scheme": "TwoPlusTwo",
                    "compression_method": "None",
                    "state": "present"
                })
            powerflex_module_mock.perform_module_operation()
            assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_update_storagepool_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_name": "test_pd_1",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "None",
                "use_all_available_capacity": True,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        with patch.object(powerflex_module_mock.powerflex_conn.storage_pool,
                          'update',
                          side_effect=MockApiException):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response(
                    'update_storage_pool'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

    def test_query_metrics_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "protection_domain_name": "test_pd_0",
                "protection_scheme": "TwoPlusTwo",
                "compression_method": "None",
                "use_all_available_capacity": True,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=None)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        with patch.object(powerflex_module_mock.powerflex_conn.utility,
                          'query_metrics',
                          side_effect=MockApiException):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response('query_metrics'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)

    def test_delete_storagepool(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "storage_pool_name": "test_pool",
                "state": "absent"
            })
        powerflex_module_mock.powerflex_conn.storage_pool.get_by_name = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL
        )
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStoragePoolV2Api.PROTECTION_DOMAIN['protection_domain'])
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockStoragePoolV2Api.DEVICE_GROUP['device_group'])
        powerflex_module_mock.powerflex_conn.storage_pool.update = MagicMock(
            return_value=(False, MockStoragePoolV2Api.STORAGE_POOL_GET_DETAIL))
        powerflex_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=MockStoragePoolV2Api.STORAGE_POOL_STATISTICS
        )
        # successful deletion
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_pool.delete.assert_called()

        # exception
        with patch.object(powerflex_module_mock.powerflex_conn.storage_pool,
                          "delete",
                          side_effect=MockApiException):
            self.capture_fail_json_call(
                MockStoragePoolV2Api.get_exception_response(
                    'delete_storage_pool'),
                module_mock=powerflex_module_mock,
                invoke_perform_module=True)
