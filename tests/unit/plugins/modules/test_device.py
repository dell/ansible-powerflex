# Copyright: (c) 2023, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Device module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_device_api import MockDeviceApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.device import PowerFlexDevice


class TestPowerflexDevice():

    get_module_args = MockDeviceApi.DEVICE_COMMON_ARGS

    @pytest.fixture
    def device_module_mock(self, mocker):
        mocker.patch(
            MockDeviceApi.MODULE_UTILS_PATH + '.PowerFlexClient',
            new=MockApiException)
        device_module_mock = PowerFlexDevice()
        device_module_mock.module.fail_json = fail_json
        return device_module_mock

    def capture_fail_json_call(self, error_msg, device_module_mock):
        try:
            device_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_device_detail_using_dev_name_sds_id(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "sds_id": MockDeviceApi.SDS_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceApi.DEVICE_GET_LIST)
        device_module_mock.perform_module_operation()
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_detail_using_path_sds_name(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceApi.DEVICE_GET_LIST)
        device_module_mock.perform_module_operation()
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_detail_using_dev_id(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceApi.DEVICE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceApi.DEVICE_GET_LIST)
        device_module_mock.perform_module_operation()
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_without_sds(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'get_dev_without_SDS'), device_module_mock)

    def test_get_device_without_sds_with_path(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'get_device_details_without_path'), device_module_mock)

    def test_get_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceApi.DEVICE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'get_device_exception'), device_module_mock)

    def test_create_device_with_id(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceApi.DEVICE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'create_id_exception'), device_module_mock)

    def test_get_device_with_empty_path(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": "",
            "sds_id": MockDeviceApi.SDS_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'empty_path'), device_module_mock)

    def test_get_device_with_empty_name(self, device_module_mock):
        self.get_module_args.update({
            "device_name": "",
            "sds_id": MockDeviceApi.SDS_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'empty_device_name'), device_module_mock)

    def test_get_device_with_empty_sds_id(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceApi.DEVICE_ID_1,
            "sds_id": "",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'empty_sds'), device_module_mock)

    def test_get_device_with_empty_sds_name(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceApi.DEVICE_ID_1,
            "sds_name": "",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'empty_sds'), device_module_mock)

    def test_get_device_with_empty_dev_id(self, device_module_mock):
        self.get_module_args.update({
            "device_id": "",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'empty_dev_id'), device_module_mock)

    def test_get_device_with_space_in_name(self, device_module_mock):
        self.get_module_args.update({
            "device_name": " ",
            "sds_id": MockDeviceApi.SDS_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'space_in_name'), device_module_mock)

    def test_get_device_with_space_in_name_with_sds_name(self, device_module_mock):
        self.get_module_args.update({
            "device_name": " ",
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'space_in_name'), device_module_mock)

    def test_get_device_without_required_params(self, device_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response(
            'with_required_params'), device_module_mock)

    def test_modify_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceApi.DEVICE_GET_LIST)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'modify_exception'), device_module_mock)

    def test_delete_device(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceApi.DEVICE_GET_LIST)
        device_module_mock.perform_module_operation()
        device_module_mock.powerflex_conn.device.delete.assert_called()

    def test_delete_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceApi.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.device.delete = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'delete_exception'), device_module_mock)
        device_module_mock.powerflex_conn.device.delete.assert_called()

    def test_get_sds_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=False)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'sds_exception'), device_module_mock)

    def test_get_pd_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "storage_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=False)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'pd_exception'), device_module_mock)

    def test_get_sp_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "storage_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockDeviceApi.PD_DETAILS_1)
        device_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=False)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'sp_exception'), device_module_mock)

    def test_get_acc_pool_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "acceleration_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockDeviceApi.PD_DETAILS_1)
        device_module_mock.powerflex_conn.acceleration_pool.get = MagicMock(
            return_value=False)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'ap_exception'), device_module_mock)

    def test_add_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "storage_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockDeviceApi.PD_DETAILS_1)
        device_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=MockDeviceApi.SP_DETAILS_1)
        device_module_mock.powerflex_conn.device.create = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'add_exception'), device_module_mock)
        device_module_mock.powerflex_conn.device.create.assert_called()

    def test_add_device_name_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": " ",
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "storage_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockDeviceApi.PD_DETAILS_1)
        device_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=MockDeviceApi.SP_DETAILS_1)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'add_dev_name_exception'), device_module_mock)

    def test_add_device_path_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": "  ",
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "storage_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockDeviceApi.PD_DETAILS_1)
        device_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=MockDeviceApi.SP_DETAILS_1)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'add_dev_path_exception'), device_module_mock)

    def test_add_device_ext_acc_type_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": "  ",
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "protection_domain_name": MockDeviceApi.PD_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockDeviceApi.PD_DETAILS_1)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'ext_type_exception'), device_module_mock)

    def test_add_device_without_pd_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "storage_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=MockDeviceApi.SP_DETAILS_1)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'add_without_pd'), device_module_mock)

    def test_add_device_without_pd_exception_for_acc_pool(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceApi.PATH_1,
            "sds_name": MockDeviceApi.SDS_NAME_1,
            "device_name": MockDeviceApi.DEVICE_NAME_1,
            "media_type": "HDD",
            "external_acceleration_type": "ReadAndWrite",
            "acceleration_pool_name": MockDeviceApi.SP_NAME_1,
            "force": False,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=MockDeviceApi.SDS_DETAILS_1)
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=[])
        device_module_mock.powerflex_conn.acceleration_pool.get = MagicMock(
            return_value=MockDeviceApi.SP_DETAILS_1)
        self.capture_fail_json_call(MockDeviceApi.get_device_exception_response1(
            'add_without_pd'), device_module_mock)
