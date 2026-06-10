# Copyright: (c) 2026, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Device Group module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.device_group \
    import PowerFlexDeviceGroup, DeviceGroupHandler
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_device_group_api \
    import MockDeviceGroupApi


class TestPowerFlexDeviceGroup(PowerFlexUnitBase):
    """Unit tests for the device_group module."""

    get_module_args = MockDeviceGroupApi.DG_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        """Return the module class under test."""
        return PowerFlexDeviceGroup

    def _mock_get(self, module_mock, value):
        module_mock.powerflex_conn.device_group.get = MagicMock(return_value=value)

    def test_get_device_group_by_name(self, powerflex_module_mock):
        """Get device group by name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.get.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False
        assert powerflex_module_mock.module.exit_json.call_args[1][
            'device_group_details']['id'] == MockDeviceGroupApi.DG_ID

    def test_get_device_group_by_id(self, powerflex_module_mock):
        """Get device group by id."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_id': MockDeviceGroupApi.DG_ID})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.get.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1][
            'device_group_details']['name'] == MockDeviceGroupApi.DG_NAME

    def test_device_group_not_found(self, powerflex_module_mock):
        """Device group not found."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': 'missing_dg'})
        self._mock_get(powerflex_module_mock, [])
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('dg_not_found'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_get_device_group_exception(self, powerflex_module_mock):
        """Get device group exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_id': MockDeviceGroupApi.DG_ID})
        powerflex_module_mock.powerflex_conn.device_group.get = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('get_dg_failed_msg'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_rename_device_group(self, powerflex_module_mock):
        """Rename device group."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': MockDeviceGroupApi.DG_NEW_NAME})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock(
            return_value=None)
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_rename_idempotent(self, powerflex_module_mock):
        """Rename idempotent."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': MockDeviceGroupApi.DG_NAME})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_rename_exception(self, powerflex_module_mock):
        """Rename exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': MockDeviceGroupApi.DG_NEW_NAME})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('rename_dg_exception'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_update_spare_node_count(self, powerflex_module_mock):
        """Update spare node count."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'spare_node_count': 5})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_spare_node_count_idempotent(self, powerflex_module_mock):
        """Spare node count idempotent."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'spare_node_count': 1})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_update_spare_device_count(self, powerflex_module_mock):
        """Update spare device count."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'spare_device_count': 3})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_spare_device_count_idempotent(self, powerflex_module_mock):
        """Spare device count idempotent."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'spare_device_count': 1})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_modify_all_attributes(self, powerflex_module_mock):
        """Modify all attributes."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': MockDeviceGroupApi.DG_NEW_NAME,
             'spare_node_count': 2,
             'spare_device_count': 3})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_called_once()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_exception(self, powerflex_module_mock):
        """Modify exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'spare_node_count': 9})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('modify_dg_exception'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_pd_resolution_by_name(self, powerflex_module_mock):
        """Pd resolution by name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'protection_domain_name': MockDeviceGroupApi.PD_NAME})
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[MockDeviceGroupApi.PROTECTION_DOMAIN])
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.protection_domain.get.assert_called()

    def test_pd_resolution_by_id(self, powerflex_module_mock):
        """Pd resolution by id."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'protection_domain_id': MockDeviceGroupApi.PD_ID})
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[MockDeviceGroupApi.PROTECTION_DOMAIN])
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.protection_domain.get.assert_called()

    def test_pd_not_found(self, powerflex_module_mock):
        """Pd not found."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'protection_domain_name': 'missing_pd'})
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[])
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('pd_not_found'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_media_type_passthrough(self, powerflex_module_mock):
        """Media type passthrough."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'media_type': 'SSD'})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1][
            'device_group_details']['mediaType'] == 'SSD'

    def test_query_usable_capacity(self, powerflex_module_mock):
        """Query usable capacity."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_id': MockDeviceGroupApi.DG_ID,
             'query_usable_capacity': True})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.query_usable_capacity = MagicMock(
            return_value=MockDeviceGroupApi.USABLE_CAPACITY)
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.query_usable_capacity.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1][
            'usable_capacity_details'] is not None

    def test_query_usable_capacity_exception(self, powerflex_module_mock):
        """Query usable capacity exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_id': MockDeviceGroupApi.DG_ID,
             'query_usable_capacity': True})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.query_usable_capacity = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('capacity_query_exception'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_check_mode_get(self, powerflex_module_mock):
        """Check mode get."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME})
        powerflex_module_mock.module.check_mode = True
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_check_mode_modify(self, powerflex_module_mock):
        """Check mode modify."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': MockDeviceGroupApi.DG_NEW_NAME})
        powerflex_module_mock.module.check_mode = True
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_diff_mode_modify(self, powerflex_module_mock):
        """Diff mode modify."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': MockDeviceGroupApi.DG_NEW_NAME})
        powerflex_module_mock.module._diff = True
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_validate_empty_name(self, powerflex_module_mock):
        """Validate empty name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': ''})
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('empty_dg_msg'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_validate_whitespace_new_name(self, powerflex_module_mock):
        """Validate whitespace new name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'new_device_group_name': '   '})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('empty_dg_msg'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_name_and_id_mutually_exclusive(self, powerflex_module_mock):
        """Name and id mutually exclusive."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'device_group_id': MockDeviceGroupApi.DG_ID})
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('mutually_exclusive'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_required_one_of_identifier(self, powerflex_module_mock):
        """Required one of identifier."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args, {})
        self.capture_fail_json_call(
            MockDeviceGroupApi.get_failed_msgs('required_one_of'),
            powerflex_module_mock, module_handler=DeviceGroupHandler)

    def test_modify_none_values(self, powerflex_module_mock):
        """Modify none values."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'device_group_name': MockDeviceGroupApi.DG_NAME,
             'spare_node_count': None, 'spare_device_count': None})
        self._mock_get(powerflex_module_mock, [MockDeviceGroupApi.DEVICE_GROUP])
        powerflex_module_mock.powerflex_conn.device_group.modify = MagicMock()
        DeviceGroupHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.device_group.modify.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False
