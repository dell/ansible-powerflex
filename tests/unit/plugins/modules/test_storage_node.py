# Copyright: (c) 2026, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Storage Node module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storage_node_api \
    import MockStorageNodeApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase

from ansible_collections.dellemc.powerflex.plugins.modules.storage_node import \
    PowerFlexStorageNode, StorageNodeHandler


class TestPowerflexStorageNode(PowerFlexUnitBase):

    get_module_args = MockStorageNodeApi.STORAGE_NODE_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexStorageNode

    def mock_storage_node_get(self, powerflex_module_mock, return_value=None):
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=return_value if return_value is not None
            else MockStorageNodeApi.STORAGE_NODE_GET_LIST)

    def mock_protection_domain_get(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockStorageNodeApi.PROTECTION_DOMAIN_GET_LIST)

    # FR-1: Platform Prerequisites and Node Identification

    def test_get_storage_node_by_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': 'node1', 'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.get.assert_called()
        assert powerflex_module_mock.result['changed'] is False

    def test_get_storage_node_by_id(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': None,
             'storage_node_id': MockStorageNodeApi.STORAGE_NODE_ID_1,
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.get.assert_called()

    def test_get_storage_node_not_found(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock, return_value=[])
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('get_storage_node_not_found'),
            powerflex_module_mock, StorageNodeHandler)

    def test_get_storage_node_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'state': 'present'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('get_storage_node_exception'),
            powerflex_module_mock, StorageNodeHandler)

    # FR-3.1: Add IP

    def test_add_ip_new(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.0.0.2', 'role': 'HostOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_called()
        assert powerflex_module_mock.result['changed'] is True

    def test_add_ip_idempotent(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.47.xxx.xxx', 'role': 'StorageOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        assert powerflex_module_mock.result['changed'] is False

    def test_add_ip_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.0.0.2', 'role': 'HostOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('add_ip_exception'),
            powerflex_module_mock, StorageNodeHandler)

    # FR-3.2: Remove IP

    def test_remove_ip_existing(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.46.xxx.xxx', 'role': 'HostOnly'}],
             'node_ip_state': 'absent-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_called()
        assert powerflex_module_mock.result['changed'] is True

    def test_remove_ip_idempotent(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.0.0.99', 'role': 'HostOnly'}],
             'node_ip_state': 'absent-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_not_called()
        assert powerflex_module_mock.result['changed'] is False

    def test_remove_ip_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.46.xxx.xxx', 'role': 'HostOnly'}],
             'node_ip_state': 'absent-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('remove_ip_exception'),
            powerflex_module_mock, StorageNodeHandler)

    # FR-3.3: Auto-detect IP role change

    def test_ip_role_auto_update(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.47.xxx.xxx', 'role': 'StorageAndHost'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called_with(
            MockStorageNodeApi.STORAGE_NODE_ID_1, '10.47.xxx.xxx', 'StorageAndHost')
        assert powerflex_module_mock.result['changed'] is True

    def test_ip_role_no_change(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.47.xxx.xxx', 'role': 'StorageOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_not_called()
        assert powerflex_module_mock.result['changed'] is False

    def test_ip_role_update_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.47.xxx.xxx', 'role': 'StorageAndHost'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('update_role_exception'),
            powerflex_module_mock, StorageNodeHandler)

    def test_mixed_add_and_role_update(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [
                {'ip': '10.47.xxx.xxx', 'role': 'StorageAndHost'},
                {'ip': '10.0.0.2', 'role': 'HostOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_called()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called()
        assert powerflex_module_mock.result['changed'] is True

    # FR-4: Node Rename

    def test_rename_success(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_new_name': 'node1_renamed', 'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_called_with(
            MockStorageNodeApi.STORAGE_NODE_ID_1, 'node1_renamed')
        assert powerflex_module_mock.result['changed'] is True

    def test_rename_idempotent(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_new_name': 'node1', 'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_not_called()
        assert powerflex_module_mock.result['changed'] is False

    def test_rename_empty_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_new_name': '', 'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('rename_empty_name'),
            powerflex_module_mock, StorageNodeHandler)

    def test_rename_with_ip_add(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_new_name': 'node1_renamed',
             'node_ip_list': [{'ip': '10.0.0.2', 'role': 'HostOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_called()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_called()
        assert powerflex_module_mock.result['changed'] is True

    def test_rename_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_new_name': 'node1_renamed', 'state': 'present'})
        self.mock_storage_node_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_call(
            MockStorageNodeApi.get_exception_response('rename_exception'),
            powerflex_module_mock, StorageNodeHandler)

    # FR-6: Check Mode

    def test_check_mode_rename(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_new_name': 'node1_renamed', 'state': 'present'})
        powerflex_module_mock.module.check_mode = True
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_not_called()
        assert powerflex_module_mock.result['changed'] is True

    def test_check_mode_add_ip(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'node_ip_list': [{'ip': '10.0.0.2', 'role': 'HostOnly'}],
             'node_ip_state': 'present-in-node',
             'state': 'present'})
        powerflex_module_mock.module.check_mode = True
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        assert powerflex_module_mock.result['changed'] is True

    def test_check_mode_query_only(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'state': 'present'})
        powerflex_module_mock.module.check_mode = True
        self.mock_storage_node_get(powerflex_module_mock)
        self.mock_protection_domain_get(powerflex_module_mock)
        StorageNodeHandler().handle(
            powerflex_module_mock, powerflex_module_mock.module.params)
        assert powerflex_module_mock.result['changed'] is False
