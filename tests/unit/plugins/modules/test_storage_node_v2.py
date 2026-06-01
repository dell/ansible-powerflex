# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for storage node module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from mock.mock import patch, MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.storage_node_v2 \
    import PowerFlexStorageNodeV2
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_storage_node_api_v2 import \
    MockStorageNodeV2Api


class TestPowerFlexStorageNodeV2(PowerFlexUnitBase):
    get_module_args = MockStorageNodeV2Api.SN_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexStorageNodeV2

    # TC-001: Get storage node by name
    def test_get_storage_node_by_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.module.exit_json.assert_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False
        assert call_args[1].get('storage_node_details') is not None

    # TC-002: Get storage node by ID
    def test_get_storage_node_by_id(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_id': MockStorageNodeV2Api.SN_ID,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.module.exit_json.assert_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('storage_node_details') is not None
        assert call_args[1]['storage_node_details']['id'] == MockStorageNodeV2Api.SN_ID

    # TC-004: Get storage node exception
    def test_get_storage_node_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_id': MockStorageNodeV2Api.SN_ID,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('get_sn_failed_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-005: Create storage node
    def test_create_storage_node(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'protection_domain_name': MockStorageNodeV2Api.PD_NAME,
                'node_ips': [{'ip': '10.0.0.1', 'role': 'StorageAndApp'}],
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[])
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[MockStorageNodeV2Api.PROTECTION_DOMAIN])
        powerflex_module_mock.powerflex_conn.storage_node.create = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.create.assert_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-006: Create storage node exception
    def test_create_storage_node_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'protection_domain_name': MockStorageNodeV2Api.PD_NAME,
                'node_ips': [{'ip': '10.0.0.1', 'role': 'StorageAndApp'}],
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[])
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[MockStorageNodeV2Api.PROTECTION_DOMAIN])
        powerflex_module_mock.powerflex_conn.storage_node.create = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('create_sn_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-007: Create with new_name fails
    def test_create_with_new_name_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'new_storage_node_name': MockStorageNodeV2Api.SN_NEW_NAME,
                'protection_domain_name': MockStorageNodeV2Api.PD_NAME,
                'node_ips': [{'ip': '10.0.0.1', 'role': 'StorageAndApp'}],
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[])
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=[MockStorageNodeV2Api.PROTECTION_DOMAIN])
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('new_name_in_create'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-008: Delete storage node
    def test_delete_storage_node(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'state': 'absent',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.delete = MagicMock(
            return_value=None)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.delete.assert_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-009: Delete storage node not found
    def test_delete_storage_node_not_found(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': 'nonexistent',
                'state': 'absent',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[])
        powerflex_module_mock.perform_module_operation()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False

    # TC-010: Delete storage node exception
    def test_delete_storage_node_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'state': 'absent',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.delete = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('delete_sn_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-011: Rename storage node
    def test_rename_storage_node(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'new_storage_node_name': MockStorageNodeV2Api.SN_NEW_NAME,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        renamed_node = dict(MockStorageNodeV2Api.STORAGE_NODE)
        renamed_node['name'] = MockStorageNodeV2Api.SN_NEW_NAME
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock(
            return_value=renamed_node)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, MockStorageNodeV2Api.SN_NEW_NAME)
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-012: Rename idempotent
    def test_rename_storage_node_idempotent(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'new_storage_node_name': MockStorageNodeV2Api.SN_NAME,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False

    # TC-013: Rename exception
    def test_rename_storage_node_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'new_storage_node_name': MockStorageNodeV2Api.SN_NEW_NAME,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('rename_sn_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-014: Add IP to node
    def test_add_ip_to_node(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.5',
                'ip_role': 'Storage',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE_MULTI_IPS)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-015: Add IP already exists (idempotent)
    def test_add_ip_already_exists(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.1',
                'ip_role': 'StorageAndApp',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False

    # TC-016: Add IP exception
    def test_add_ip_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.5',
                'ip_role': 'Storage',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('add_ip_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-017: Remove IP from node
    def test_remove_ip_from_node(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.2',
                'ip_state': 'absent-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE_MULTI_IPS])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, '10.0.0.2')
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-018: Remove IP not exists (idempotent)
    def test_remove_ip_not_exists(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.99',
                'ip_state': 'absent-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False

    # TC-019: Remove IP exception
    def test_remove_ip_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.2',
                'ip_state': 'absent-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE_MULTI_IPS])
        powerflex_module_mock.powerflex_conn.storage_node.remove_ip = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('remove_ip_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-020: Set IP role
    def test_set_ip_role(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.1',
                'ip_role': 'Storage',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, '10.0.0.1', 'Storage')
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-021: Set IP role idempotent
    def test_set_ip_role_idempotent(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.1',
                'ip_role': 'StorageAndApp',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is False

    # TC-022: Set IP role exception
    def test_set_ip_role_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.1',
                'ip_role': 'Storage',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('set_ip_role_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-023: Update original pathnames
    def test_update_original_pathnames(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'update_original_pathnames': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames.assert_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-024: Update pathnames with force
    def test_update_pathnames_with_force(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'update_original_pathnames': True,
                'force_failed_devices': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, force=True)

    # TC-025: Update pathnames exception
    def test_update_pathnames_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'update_original_pathnames': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.update_original_pathnames = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('update_pathnames_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-026: Query PDS details
    def test_query_pds(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'query_pds': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            return_value=MockStorageNodeV2Api.PDS_DETAILS)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.get_related.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, 'Pds')
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('pds_details') == MockStorageNodeV2Api.PDS_DETAILS

    # TC-027: Query PDS exception
    def test_query_pds_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'query_pds': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('query_pds_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-028: Query DGWT details
    def test_query_dgwt(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'query_dgwt': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            return_value=MockStorageNodeV2Api.DGWT_DETAILS)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.get_related.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, 'Dgwt')
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('dgwt_details') == MockStorageNodeV2Api.DGWT_DETAILS

    # TC-029: Query DGWT exception
    def test_query_dgwt_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'query_dgwt': True,
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.get_related = MagicMock(
            side_effect=MockApiException())
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('query_dgwt_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-030: Check mode rename
    def test_check_mode_rename(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'new_storage_node_name': MockStorageNodeV2Api.SN_NEW_NAME,
            })
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.rename = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.rename.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-031: Check mode add IP
    def test_check_mode_add_ip(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.5',
                'ip_role': 'Storage',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-032: Check mode delete
    def test_check_mode_delete(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'state': 'absent',
            })
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.delete = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.delete.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True

    # TC-033: Validate empty name
    def test_validate_empty_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': '',
            })
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('empty_sn_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-034: Validate whitespace name
    def test_validate_whitespace_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': '   ',
            })
        self.capture_fail_json_call(
            MockStorageNodeV2Api.get_failed_msgs('empty_sn_msg'),
            powerflex_module_mock, invoke_perform_module=True)

    # TC-035: Existing IP with different role triggers set_ip_role
    def test_add_ip_sets_role_when_different(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                'storage_node_name': MockStorageNodeV2Api.SN_NAME,
                'ip_address': '10.0.0.1',
                'ip_role': 'Storage',
                'ip_state': 'present-in-node',
            })
        powerflex_module_mock.powerflex_conn.storage_node.get = MagicMock(
            return_value=[MockStorageNodeV2Api.STORAGE_NODE])
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role = MagicMock(
            return_value=MockStorageNodeV2Api.STORAGE_NODE)
        powerflex_module_mock.powerflex_conn.storage_node.add_ip = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.storage_node.set_ip_role.assert_called_once_with(
            MockStorageNodeV2Api.SN_ID, '10.0.0.1', 'Storage')
        powerflex_module_mock.powerflex_conn.storage_node.add_ip.assert_not_called()
        call_args = powerflex_module_mock.module.exit_json.call_args
        assert call_args[1].get('changed') is True
