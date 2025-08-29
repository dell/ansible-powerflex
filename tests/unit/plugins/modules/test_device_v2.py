# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Device V2 module on PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries \
    import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_device_api_v2 \
    import MockDeviceV2Api
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import utils
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fail_json import (
    FailJsonException,
    fail_json,
)
from ansible_collections.dellemc.powerflex.plugins.modules.device_v2 import PowerFlexDeviceV2, DeviceHandler
from ansible.module_utils import basic

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()
basic.AnsibleModule = MagicMock()


class TestPowerFlexDeviceV2():

    get_module_args = MockDeviceV2Api.DEVICE_COMMON_ARGS

    @pytest.fixture
    def device_module_mock(self, mocker):
        utils.is_version_less = MagicMock(return_value=False)
        utils.is_version_ge_or_eq = MagicMock(return_value=True)
        device_module_mock = PowerFlexDeviceV2()
        device_module_mock.module.check_mode = False
        device_module_mock.module._diff = True
        device_module_mock.module.fail_json = fail_json
        return device_module_mock

    def capture_fail_json_call(self, error_msg, device_module_mock):
        try:
            DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_device_detail_using_path_storage_node_id(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_detail_without_state(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_name": MockDeviceV2Api.NODE_NAME_1
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_detail_using_path_storage_node_name(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_name": MockDeviceV2Api.NODE_NAME_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_detail_using_dev_id(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceV2Api.DEVICE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_detail_using_dev_name(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceV2Api.DEVICE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_id": MockDeviceV2Api.DEVICE_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'get_device_exception'), device_module_mock)

    def test_create_device(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        device_module_mock.powerflex_conn.device.create = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST[0])
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.create.assert_called()

    def test_create_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        device_module_mock.powerflex_conn.device.create = MagicMock(
            side_effect=MockApiException)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_exception'), device_module_mock)

    def test_create_device_force(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "storage_node_name": MockDeviceV2Api.NODE_NAME_1,
            "device_group_name": MockDeviceV2Api.DG_NAME_1,
            "media_type": "SSD",
            "force": True,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        device_module_mock.powerflex_conn.device.create = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST[0])
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.create.assert_called()

    def test_create_device_without_path_exception(self, device_module_mock):
        self.get_module_args.update({
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_path'), device_module_mock)

    def test_create_device_without_media_type_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_media_type'), device_module_mock)

    def test_create_device_without_device_group_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_device_group'), device_module_mock)

    def test_create_device_without_storage_node_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_node'), device_module_mock)

    def test_create_device_with_id_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "device_id": MockDeviceV2Api.DEVICE_ID_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_with_id'), device_module_mock)

    def test_create_device_with_empty_name_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": "",
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_with_empty_name'), device_module_mock)

    def test_create_device_with_empty_path_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": "",
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_path'), device_module_mock)

    def test_create_device_with_empty_media_type_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_media_type'), device_module_mock)

    def test_create_device_with_empty_device_group_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_name": "",
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_device_group'), device_module_mock)

    def test_create_device_with_empty_storage_node_exception(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "storage_node_name": "",
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'create_device_without_node'), device_module_mock)

    def test_modify_device(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "new_device_name": "ansible_device_rename",
            "capacity_limit_gb": 500,
            "clear_error": True,
            "force": True,
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.rename.assert_called()
        device_module_mock.powerflex_conn.device.set_capacity_limit.assert_called()
        device_module_mock.powerflex_conn.device.clear_errors.assert_called()

    def test_rename_device_with_empty_name_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "new_device_name": "",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'rename_device_with_empty_name'), device_module_mock)

    def test_rename_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "new_device_name": "ansible_device_rename",
            "state": "present"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.device.rename = MagicMock(
            side_effect=MockApiException)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'rename_exception'), device_module_mock)

    def test_delete_device(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.delete.assert_called()

    def test_delete_device_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        device_module_mock.powerflex_conn.device.delete = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'delete_exception'), device_module_mock)

    def test_get_storage_node_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            side_effect=MockApiException)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'get_storage_node_exception'), device_module_mock)

    def test_get_storage_node_empty_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=None)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'get_storage_node_exception'), device_module_mock)

    def test_get_device_group_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'get_device_group_exception'), device_module_mock)

    def test_get_device_group_empty_exception(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.params = self.get_module_args
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=None)
        self.capture_fail_json_call(MockDeviceV2Api.get_device_exception_response(
            'get_device_group_empty'), device_module_mock)

    def test_create_device_check_mode(self, device_module_mock):
        self.get_module_args.update({
            "current_pathname": MockDeviceV2Api.PATH_1,
            "storage_node_id": MockDeviceV2Api.NODE_ID_1,
            "device_group_id": MockDeviceV2Api.DG_ID_1,
            "media_type": "SSD",
            "state": "present"
        })
        device_module_mock.module.check_mode = True
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=None)
        device_module_mock.powerflex_conn.device.create = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST[0])
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.create.assert_not_called()

    def test_modify_device_check_mode(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "new_device_name": "ansible_device_rename",
            "capacity_limit_gb": 500,
            "clear_error": True,
            "force": True,
            "state": "present"
        })
        device_module_mock.module.check_mode = True
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.rename.assert_not_called()
        device_module_mock.powerflex_conn.device.set_capacity_limit.assert_not_called()
        device_module_mock.powerflex_conn.device.clear_errors.assert_not_called()

    def test_delete_device_check_mode(self, device_module_mock):
        self.get_module_args.update({
            "device_name": MockDeviceV2Api.DEVICE_NAME_1,
            "state": "absent"
        })
        device_module_mock.module.check_mode = True
        device_module_mock.module.params = self.get_module_args
        device_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=MockDeviceV2Api.DEVICE_GET_LIST)
        device_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockDeviceV2Api.NODE_DETAILS_1)
        device_module_mock.powerflex_conn.device_group.get = MagicMock(
            return_value=MockDeviceV2Api.DG_DETAILS_1)
        DeviceHandler().handle(device_module_mock, device_module_mock.module.params)
        device_module_mock.powerflex_conn.device.delete.assert_not_called()
