# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for storage node module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import os

import pytest
# pylint: disable=unused-import
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.storage_node \
    import PowerFlexStorageNode
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storage_node_api import \
    MockStorageNodeApi


class TestPowerFlexStorageNode(PowerFlexUnitBase):
    get_module_args = MockStorageNodeApi.SN_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexStorageNode

    # ------------------------------------------------------------------ #
    # Get operations
    # ------------------------------------------------------------------ #
    def test_get_storage_node_by_name(self, powerflex_module_mock):
        """Get storage node by name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.perform_module_operation()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False
        assert call_args[1].get('storage_node_details') is not None

    def test_get_storage_node_by_id(self, powerflex_module_mock):
        """Get storage node by id."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_id': MockStorageNodeApi.SN_ID})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1]['storage_node_details']['id'] == MockStorageNodeApi.SN_ID

    def test_node_not_found(self, powerflex_module_mock):
        """Node not found."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': 'nonexistent'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[])
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('node_not_found'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_get_storage_node_exception(self, powerflex_module_mock):
        """Get storage node exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_id': MockStorageNodeApi.SN_ID})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('get_sn_failed_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Rename
    # ------------------------------------------------------------------ #
    def test_rename_storage_node(self, powerflex_module_mock):
        """Rename storage node."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'new_storage_node_name': MockStorageNodeApi.SN_NEW_NAME})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_rename_idempotent(self, powerflex_module_mock):
        """Rename idempotent."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'new_storage_node_name': MockStorageNodeApi.SN_NAME})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_rename_exception(self, powerflex_module_mock):
        """Rename exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'new_storage_node_name': MockStorageNodeApi.SN_NEW_NAME})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('rename_sn_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Single IP: add
    # ------------------------------------------------------------------ #
    def test_add_ip_to_node(self, powerflex_module_mock):
        """Add ip to node."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.5', 'ip_role': 'Storage',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_ip_already_exists(self, powerflex_module_mock):
        """Add ip already exists."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.1', 'ip_role': 'StorageAndApp',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_add_ip_exception(self, powerflex_module_mock):
        """Add ip exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.5', 'ip_role': 'Storage',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('add_ip_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Single IP: remove
    # ------------------------------------------------------------------ #
    def test_remove_ip_from_node(self, powerflex_module_mock):
        """Remove ip from node."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.2', 'ip_state': 'absent-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE_MULTI_IPS])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_ip_not_exists(self, powerflex_module_mock):
        """Remove ip not exists."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.99', 'ip_state': 'absent-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_remove_ip_exception(self, powerflex_module_mock):
        """Remove ip exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.2', 'ip_state': 'absent-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE_MULTI_IPS])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('remove_ip_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Single IP: set role
    # ------------------------------------------------------------------ #
    def test_set_ip_role(self, powerflex_module_mock):
        """Set ip role."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.1', 'ip_role': 'Storage',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_set_ip_role_idempotent(self, powerflex_module_mock):
        """Set ip role idempotent."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.1', 'ip_role': 'StorageAndApp',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_set_ip_role_exception(self, powerflex_module_mock):
        """Set ip role exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.1', 'ip_role': 'Storage',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('set_ip_role_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_existing_ip_different_role_sets_role(self, powerflex_module_mock):
        """Existing ip different role sets role."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.1', 'ip_role': 'Storage',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()

    # ------------------------------------------------------------------ #
    # Update original pathnames
    # ------------------------------------------------------------------ #
    def test_update_original_pathnames(self, powerflex_module_mock):
        """Update original pathnames."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'update_original_pathnames': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_update_pathnames_with_force(self, powerflex_module_mock):
        """Update pathnames with force."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'update_original_pathnames': True, 'force_failed_devices': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        call = powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames.call_args
        assert call.kwargs.get('force') is True

    def test_update_pathnames_exception(self, powerflex_module_mock):
        """Update pathnames exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'update_original_pathnames': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('update_pathnames_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Bulk IP management via node_ips
    # ------------------------------------------------------------------ #
    def test_node_ips_bulk_add(self, powerflex_module_mock):
        """Node ips bulk add."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'node_ips': [
                 {'ip': '10.0.0.5', 'role': 'Storage', 'ip_state': 'present-in-node'},
                 {'ip': '10.0.0.6', 'role': 'App', 'ip_state': 'present-in-node'},
             ]})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.powerflex_conn.storage_node.add_ip.call_count == 2
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_node_ips_mixed_states(self, powerflex_module_mock):
        """Node ips mixed states."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'node_ips': [
                 {'ip': '10.0.0.2', 'ip_state': 'absent-in-node'},
                 {'ip': '10.0.0.9', 'role': 'App', 'ip_state': 'present-in-node'},
                 {'ip': '10.0.0.1', 'role': 'Storage', 'ip_state': 'present-in-node'},
             ]})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE_MULTI_IPS])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE_MULTI_IPS)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE_MULTI_IPS)
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            return_value=MockStorageNodeApi.STORAGE_NODE_MULTI_IPS)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_called()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_called()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_node_ips_idempotent(self, powerflex_module_mock):
        """Node ips idempotent."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'node_ips': [
                 {'ip': '10.0.0.1', 'role': 'StorageAndApp', 'ip_state': 'present-in-node'},
             ]})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    # ------------------------------------------------------------------ #
    # Query PDS / DGWT
    # ------------------------------------------------------------------ #
    def test_query_pds(self, powerflex_module_mock):
        """Query pds."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME, 'query_pds': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            return_value=MockStorageNodeApi.PDS_DETAILS)
        powerflex_module_mock.perform_module_operation()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('pds_details') == MockStorageNodeApi.PDS_DETAILS

    def test_query_pds_exception(self, powerflex_module_mock):
        """Query pds exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME, 'query_pds': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('query_pds_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_query_dgwt(self, powerflex_module_mock):
        """Query dgwt."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME, 'query_dgwt': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            return_value=MockStorageNodeApi.DGWT_DETAILS)
        powerflex_module_mock.perform_module_operation()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('dgwt_details') == MockStorageNodeApi.DGWT_DETAILS

    def test_query_dgwt_exception(self, powerflex_module_mock):
        """Query dgwt exception."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME, 'query_dgwt': True})
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('query_dgwt_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Check mode
    # ------------------------------------------------------------------ #
    def test_check_mode_rename(self, powerflex_module_mock):
        """Check mode rename."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'new_storage_node_name': MockStorageNodeApi.SN_NEW_NAME})
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_check_mode_add_ip(self, powerflex_module_mock):
        """Check mode add ip."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.5', 'ip_role': 'Storage',
             'ip_state': 'present-in-node'})
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeApi.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    # ------------------------------------------------------------------ #
    # Validation / negative
    # ------------------------------------------------------------------ #
    def test_validate_empty_name(self, powerflex_module_mock):
        """Validate empty name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': ''})
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('empty_sn_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_validate_whitespace_name(self, powerflex_module_mock):
        """Validate whitespace name."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': '   '})
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('empty_sn_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_ip_state_without_ip_address(self, powerflex_module_mock):
        """Ip state without ip address."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_state': 'present-in-node'})
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('ip_addr_required'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_node_ips_and_ip_address_mutually_exclusive(self, powerflex_module_mock):
        """Node ips and ip address mutually exclusive."""
        self.set_module_params(
            powerflex_module_mock, self.get_module_args,
            {'storage_node_name': MockStorageNodeApi.SN_NAME,
             'ip_address': '10.0.0.5', 'ip_role': 'Storage',
             'ip_state': 'present-in-node',
             'node_ips': [{'ip': '10.0.0.6', 'role': 'App', 'ip_state': 'present-in-node'}]})
        self.capture_fail_json_call(
            MockStorageNodeApi.get_failed_msgs('mutually_exclusive'),
            powerflex_module_mock, invoke_perform_module=True)

    # ------------------------------------------------------------------ #
    # Example playbook (integration / artifact existence)
    # ------------------------------------------------------------------ #
    def test_example_playbook_syntax_validation(self):
        """Example playbook syntax validation."""
        import ansible_collections.dellemc.powerflex as pf_pkg
        import yaml
        base = list(pf_pkg.__path__)[0]
        playbook = os.path.join(base, 'playbooks', 'modules', 'storage_node.yml')
        assert os.path.exists(playbook), "example playbook missing: %s" % playbook
        with open(playbook) as handle:
            tasks = yaml.safe_load(handle)
        assert isinstance(tasks, list) and len(tasks) > 0
