# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Resource Group module on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_resource_group_api \
    import MockResourceResourceGroupAPI
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.plugins.modules.resource_group \
    import PowerFlexResourceGroup


class TestResourceGroup(PowerFlexUnitBase):

    get_module_args = MockResourceResourceGroupAPI.RG_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexResourceGroup

    def test_delete_deploy_check_mode(self, powerflex_module_mock):
        self.set_module_params(powerflex_module_mock, self.get_module_args,
                               {"resource_group_name": "ans_rg", "state": "absent", "validate": True})
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE)
        powerflex_module_mock.powerflex_conn.deployment.delete = MagicMock(return_value=None)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_deploy(self, powerflex_module_mock):
        self.set_module_params(powerflex_module_mock, self.get_module_args,
                               {"resource_group_name": "ans_rg", "state": "absent", "validate": True})
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(return_value=[MagicMock()])
        powerflex_module_mock.powerflex_conn.deployment.delete = MagicMock(return_value=None)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_deploy_by_id(self, powerflex_module_mock):
        self.set_module_params(powerflex_module_mock, self.get_module_args,
                               {"resource_group_id": "8aaa03a88de961fa018de96a88d80008",
                                "state": "absent", "validate": True, "resource_group_name": None})
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE[0])
        powerflex_module_mock.powerflex_conn.deployment.delete = MagicMock(return_value=None)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_delete_deploy_by_id_exception(self, powerflex_module_mock):
        self.set_module_params(powerflex_module_mock, self.get_module_args,
                               {"resource_group_id": "8aaa03a88de961fa018de96a88d80008",
                                "state": "absent", "validate": True, "resource_group_name": None})
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(side_effect=MockApiException)
        powerflex_module_mock.powerflex_conn.deployment.delete = MagicMock(return_value=None)
        self.capture_fail_json_call("", powerflex_module_mock, invoke_perform_module=True)

    def test_delete_deploy_exception(self, powerflex_module_mock):
        self.set_module_params(powerflex_module_mock, self.get_module_args,
                               {"resource_group_name": "ans_rg", "state": "absent", "validate": True,
                                "resource_group_id": None})
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE)
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE[0])
        powerflex_module_mock.powerflex_conn.deployment.delete = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('get_delete_deploy_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_validate_deploy(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": "c65d0172-8666-48ab-935e-9a0bf69ed66d",
                     "firmware_repository_id": "8aaa80788b5755d1018b576126d51ba3",
                     "validate": True, "resource_group_id": None, "state": "present"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(return_value=[])
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(return_value=[])
        powerflex_module_mock.powerflex_conn.service_template.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.firmware_repository.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_FIRMWARE_REPO)
        powerflex_module_mock.powerflex_conn.deployment.validate = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_validate_deploy_exception(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": "c65d0172-8666-48ab-935e-9a0bf69ed66d",
                     "firmware_repository_id": "8aaa80788b5755d1018b576126d51ba3",
                     "validate": True, "resource_group_id": None, "state": "present"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.get_deployment_data = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('get_validate_deploy_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_create_deploy(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": None, "template_name": "update-template",
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present", "schedule_date": "2020-01-01"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(return_value=[])
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(return_value=[])
        powerflex_module_mock.powerflex_conn.service_template.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.service_template.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.firmware_repository.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_FIRMWARE_REPO)
        powerflex_module_mock.powerflex_conn.deployment.create = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_deploy_exception(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": None, "template_name": "update-template",
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.get_deployment_data = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('get_create_deploy_exception'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_template_validation(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": None, "template_name": None,
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.service_template.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('get_template_validate_error'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_scheduled_data(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": None, "template_name": "update-template",
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present", "schedule_date": "01/01/2024"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(return_value=[])
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(return_value=[])
        powerflex_module_mock.powerflex_conn.service_template.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.service_template.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.firmware_repository.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_FIRMWARE_REPO)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('invalid_date_format'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_resource_group_name_error(self, powerflex_module_mock):
        arguments = {"resource_group_name": None, "description": "ans_rg",
                     "template_id": None, "template_name": "update-template",
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present", "schedule_date": None}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(return_value=None)
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(return_value=None)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('resource_group_name_error'),
            powerflex_module_mock, invoke_perform_module=True)

    def test_resource_group_edit(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": None, "template_name": "update-template",
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present", "schedule_date": "2020-01-01",
                     "scaleup": True, "node_count": 1, "clone_node": "block-legacy-gateway",
                     "new_resource_group_name": "ans_rg1"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE)
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE[0])
        powerflex_module_mock.powerflex_conn.service_template.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.service_template.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.firmware_repository.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_FIRMWARE_REPO)
        powerflex_module_mock.powerflex_conn.deployment.edit = MagicMock(
            return_value=None)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True
        arguments.update({"clone_node": None})
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_resource_group_exception(self, powerflex_module_mock):
        arguments = {"resource_group_name": "ans_rg", "description": "ans_rg",
                     "template_id": None, "template_name": "update-template",
                     "firmware_repository_id": None, "firmware_repository_name": "firmware-name",
                     "validate": False, "state": "present", "schedule_date": "2020-01-01",
                     "scaleup": True, "node_count": 1, "clone_node": "block-legacy-gateway"}
        self.set_module_params(powerflex_module_mock, self.get_module_args, arguments)
        powerflex_module_mock.powerflex_conn.deployment.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE)
        powerflex_module_mock.powerflex_conn.deployment.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_RESPONSE[0])
        powerflex_module_mock.powerflex_conn.service_template.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.service_template.get_by_id = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_TEMPLATE_RESPONSE)
        powerflex_module_mock.powerflex_conn.firmware_repository.get = MagicMock(
            return_value=MockResourceResourceGroupAPI.RG_FIRMWARE_REPO)
        powerflex_module_mock.modify_resource_group_details = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_call(
            MockResourceResourceGroupAPI.resource_group_error('resource_group_edit_error'),
            powerflex_module_mock, invoke_perform_module=True)
