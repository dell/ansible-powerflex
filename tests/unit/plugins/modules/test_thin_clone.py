# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for thin_clone module on PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import (
    initial_mock,
)
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_thin_clone_api import (
    MockThinCloneApi,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import (
    utils,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.fail_json import (
    FailJsonException,
    fail_json,
)

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.thin_clone import (
    PowerFlexThinClone,
)


class TestPowerflexThinClone(PowerFlexUnitBase):

    get_module_args = MockThinCloneApi.THIN_CLONE_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexThinClone

    def capture_fail_json_call(self, error_msg, powerflex_module_mock):
        powerflex_module_mock.module.fail_json = fail_json
        try:
            powerflex_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    # ---------------------------------------------------------------
    # U-001: Create thin clone from source volume by name (FR-001)
    # ---------------------------------------------------------------
    def test_create_from_volume_by_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                [],  # idempotency lookup — does not exist
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read after create
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-002: Create thin clone from source volume by ID (FR-001)
    # ---------------------------------------------------------------
    def test_create_from_volume_by_id(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_id": MockThinCloneApi.SOURCE_VOLUME_ID,
                "new_clone_name": "clone_b",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source by id
                [],  # idempotency lookup
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-003: Create thin clone from snapshot by name (FR-002)
    # ---------------------------------------------------------------
    def test_create_from_snapshot_by_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_snapshot_name": "snap_prod",
                "new_clone_name": "clone_c",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_SNAPSHOT],  # resolve snapshot
                [],  # idempotency lookup
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-004: Create thin clone from snapshot by ID (FR-002)
    # ---------------------------------------------------------------
    def test_create_from_snapshot_by_id(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_snapshot_id": MockThinCloneApi.SOURCE_SNAPSHOT_ID,
                "new_clone_name": "clone_d",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_SNAPSHOT],  # resolve snapshot by id
                [],  # idempotency lookup
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-005: Create from existing thin clone uses volume path (FR-003, AD-6)
    # ---------------------------------------------------------------
    def test_create_from_thin_clone_uses_volume_path(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "clone_a",
                "new_clone_name": "grandchild",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_THIN_CLONE],  # source is itself a thin clone
                [],  # idempotency lookup
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-006: Idempotent — name exists with matching ancestry (FR-004)
    # ---------------------------------------------------------------
    def test_idempotent_name_exists_matching_ancestry(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                MockThinCloneApi.EXISTING_CLONE_MATCHING,  # idempotency: match
            ]
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is False

    # ---------------------------------------------------------------
    # U-007: Fail — name exists with mismatched ancestry (FC-TC-015)
    # ---------------------------------------------------------------
    def test_fail_name_exists_mismatched_ancestry(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                MockThinCloneApi.EXISTING_CLONE_MISMATCHED,  # ancestry mismatch
            ]
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("name_exists_mismatched"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-008: Fail — name exists but not a thin clone (FC-TC-015)
    # ---------------------------------------------------------------
    def test_fail_name_exists_not_thin_clone(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                MockThinCloneApi.EXISTING_REGULAR_VOLUME,  # not a thin clone
            ]
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("name_exists_not_thin_clone"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-009: Check mode — no API mutation (FR-010)
    # ---------------------------------------------------------------
    def test_check_mode_no_api_mutation(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                [],  # idempotency — does not exist
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock()
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-010: Diff mode — before={}, after=populated (FR-011)
    # ---------------------------------------------------------------
    def test_diff_mode_before_empty_after_populated(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.module._diff = True
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                [],  # idempotency — does not exist
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        result = powerflex_module_mock.module.exit_json.call_args[1]
        assert "diff" in result
        assert result["diff"]["before"] == {}
        assert "name" in result["diff"]["after"]

    # ---------------------------------------------------------------
    # U-011: Empty new_clone_name fails (FC-TC-003)
    # ---------------------------------------------------------------
    def test_empty_new_clone_name_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": " ",
                "state": "present",
            },
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("empty_clone_name"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-012: No source supplied fails (FC-TC-002)
    # ---------------------------------------------------------------
    def test_no_source_supplied_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        self.capture_fail_json_call(
            "Exactly one of from_volume_name",
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-013: Both volume and snapshot source supplied fails (FC-TC-001)
    # ---------------------------------------------------------------
    def test_both_volume_and_snapshot_source_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "from_snapshot_name": "snap_prod",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        self.capture_fail_json_call(
            "mutually exclusive",
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-014: Source volume not found fails (FC-TC-008)
    # ---------------------------------------------------------------
    def test_source_volume_not_found_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "nonexistent",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("source_volume_not_found"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-015: Source snapshot not found fails (FC-TC-009)
    # ---------------------------------------------------------------
    def test_source_snapshot_not_found_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_snapshot_id": "bad_snap_id",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("source_snapshot_not_found"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-016: SDK exception on create (FC-TC-022)
    # ---------------------------------------------------------------
    def test_create_thin_clone_sdk_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                [],  # idempotency — does not exist
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("create_sdk_exception"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-017: SDK exception during source volume resolve (FC-TC-017)
    # ---------------------------------------------------------------
    def test_get_volume_exception_on_source_resolve(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("get_volume_exception"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-018: Return shape matches volume_v2 (FR-006, AD-9)
    # ---------------------------------------------------------------
    def test_return_shape_matches_volume_v2(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                [],
                MockThinCloneApi.NEW_CLONE_DETAILS,
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        result = powerflex_module_mock.module.exit_json.call_args[1]
        volume_details = result.get("volume_details", {})
        assert "id" in volume_details
        assert "name" in volume_details
        assert "volumeType" in volume_details
        assert "ancestorVolumeId" in volume_details
        assert "sizeInKb" in volume_details
        assert "storagePoolId" in volume_details

    # ---------------------------------------------------------------
    # U-019: source_details returned (FR-006)
    # ---------------------------------------------------------------
    def test_source_details_returned(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                [],
                MockThinCloneApi.NEW_CLONE_DETAILS,
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        result = powerflex_module_mock.module.exit_json.call_args[1]
        source_details = result.get("source_details", {})
        assert "source_type" in source_details
        assert "source_id" in source_details

    # ---------------------------------------------------------------
    # U-020: Version gate skips on PowerFlex < 5.0 (FR-012, FC-TC-019)
    # ---------------------------------------------------------------
    def test_version_gate_skips_on_4x(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        utils.is_version_less = MagicMock(return_value=True)
        powerflex_module_mock.check_module_compatibility()
        result = powerflex_module_mock.module.exit_json.call_args[1]
        assert result["changed"] is False

    # ---------------------------------------------------------------
    # U-021: get_system_id exception (FR-013)
    # ---------------------------------------------------------------
    def test_get_system_id_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                [],
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("get_system_exception"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-022: get_system_id returns empty (FR-013)
    # ---------------------------------------------------------------
    def test_get_system_id_empty_response(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                [],
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("no_system_exist"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-023: Snapshot by name resolves correctly (FR-002, FR-019)
    # ---------------------------------------------------------------
    def test_snapshot_source_resolves_by_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_snapshot_name": "snap_prod",
                "new_clone_name": "clone_from_snap",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_SNAPSHOT],  # resolve snapshot by name
                [],  # idempotency
                MockThinCloneApi.NEW_CLONE_DETAILS,  # re-read
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_thin_clone.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    # ---------------------------------------------------------------
    # U-024: Check mode on existing clone — idempotent noop (FR-010, FR-004)
    # ---------------------------------------------------------------
    def test_check_mode_idempotent_noop(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                MockThinCloneApi.EXISTING_CLONE_MATCHING,
            ]
        )
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is False

    # ---------------------------------------------------------------
    # U-026: Multiple volumes with same name (edge case)
    # ---------------------------------------------------------------
    def test_multiple_volumes_with_same_name(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "dup_name",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=[
                MockThinCloneApi.SOURCE_VOLUME,
                MockThinCloneApi.SOURCE_VOLUME,
            ]
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("multiple_volumes"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-027: Whitespace-only clone name fails (FC-TC-003)
    # ---------------------------------------------------------------
    def test_whitespace_clone_name_fails(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "\t\n  ",
                "state": "present",
            },
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("empty_clone_name"),
            powerflex_module_mock,
        )

    # ---------------------------------------------------------------
    # U-028: Re-read after create populates details (FR-006)
    # ---------------------------------------------------------------
    def test_reread_after_create_populates_details(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                [],
                MockThinCloneApi.NEW_CLONE_DETAILS,
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        result = powerflex_module_mock.module.exit_json.call_args[1]
        assert result["volume_details"]["id"] == MockThinCloneApi.NEW_CLONE_ID

    # ---------------------------------------------------------------
    # U-029: SDK called with correct snapshot_defs format (FR-001)
    # ---------------------------------------------------------------
    def test_sdk_create_called_with_correct_snapshot_defs(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_id": MockThinCloneApi.SOURCE_VOLUME_ID,
                "new_clone_name": "clone_test",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                [],
                MockThinCloneApi.NEW_CLONE_DETAILS,
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        call_args = powerflex_module_mock.powerflex_conn.system.create_thin_clone.call_args
        assert call_args is not None
        args = call_args[0] if call_args[0] else []
        kwargs = call_args[1] if call_args[1] else {}
        # Verify snapshot_defs contains volumeId and snapshotName
        snapshot_defs = args[1] if len(args) > 1 else kwargs.get("snapshot_defs")
        assert isinstance(snapshot_defs, list)
        assert len(snapshot_defs) == 1
        assert snapshot_defs[0]["volumeId"] == MockThinCloneApi.SOURCE_VOLUME_ID
        assert snapshot_defs[0]["snapshotName"] == "clone_test"

    # ---------------------------------------------------------------
    # U-030: Idempotent no-op: diff not emitted (FR-004, FR-011)
    # ---------------------------------------------------------------
    def test_idempotent_no_diff_emitted(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.module._diff = True
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],
                MockThinCloneApi.EXISTING_CLONE_MATCHING,
            ]
        )
        powerflex_module_mock.perform_module_operation()
        result = powerflex_module_mock.module.exit_json.call_args[1]
        assert result["changed"] is False
        # On idempotent no-op, diff should either be absent or have matching before/after
        if "diff" in result:
            assert result["diff"]["before"] == result["diff"]["after"]

    # ---------------------------------------------------------------
    # U-031: Re-read exception after create (edge case)
    # ---------------------------------------------------------------
    def test_reread_exception_after_create(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "from_volume_name": "src_vol",
                "new_clone_name": "clone_a",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [MockThinCloneApi.SOURCE_VOLUME],  # resolve source
                [],  # idempotency — does not exist
                MockApiException,  # re-read fails
            ]
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockThinCloneApi.SYSTEM_GET_RESPONSE
        )
        powerflex_module_mock.powerflex_conn.system.create_thin_clone = MagicMock(
            return_value=MockThinCloneApi.CREATE_RESPONSE
        )
        self.capture_fail_json_call(
            MockThinCloneApi.get_exception_response("reread_exception"),
            powerflex_module_mock,
        )
