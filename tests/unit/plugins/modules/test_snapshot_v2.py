# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Snapshot module on PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import (
    initial_mock,
)
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_snapshot_api_v2 import (
    MockSnapshotApi,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import (
    utils,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base \
    import PowerFlexUnitBase
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fail_json import (
    FailJsonException,
    fail_json,
)

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.snapshot_v2 import (
    PowerFlexSnapshotV2,
)


class TestPowerflexSnapshotV2(PowerFlexUnitBase):

    get_module_args = MockSnapshotApi.SNAPSHOT_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexSnapshotV2

    def capture_fail_json_call(self, error_msg, powerflex_module_mock):
        powerflex_module_mock.module.fail_json = fail_json
        try:
            powerflex_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_snapshot_details(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"snapshot_name": "example_snap_test", "state": "present"},
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.get.assert_called()

    def test_get_snapshot_details_empty_snapshot_id_exception(
        self, powerflex_module_mock
    ):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"snapshot_id": " ", "state": "present"})
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "get_snapshot_details_empty_snapshot_id_exception"
            ),
            powerflex_module_mock,
        )

    def test_get_snapshot_details_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "get_snapshot_details_exception"
            ),
            powerflex_module_mock,
        )

    def test_get_snapshot_details_multi_instance_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "state": "present"
            })
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=["instance1", "instance2"]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "snapshot_details_multi_instance_exception"
            ),
            powerflex_module_mock,
        )

    def test_get_system_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "vol_id": "test_vol_id",
                "state": "present",
            }
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "get_system_with_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "vol_id": "test_vol_id",
                "desired_retention": 2,
                "retention_unit": "hours",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.system.create_snapshot.assert_called()

    def test_create_snapshot_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "vol_id": "test_vol_id",
                "desired_retention": 2,
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        powerflex_module_mock.powerflex_conn.system.create_snapshot = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_with_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_with_sp_id_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "snapshot_id": "test_snapshot_id",
                "vol_id": "test_vol_id",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_with_sp_id_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_without_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_without_name_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_without_vol_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_without_vol_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_with_new_name_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "snapshot_new_name": "test_snapshot_new_name",
                "vol_id": "test_vol_id",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_with_new_name_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_with_rm_mode_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "remove_mode": "ONLY_ME",
                "vol_id": "test_vol_id",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_with_rm_mode_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_unit_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "retention_unit": "hours",
                "vol_id": "test_vol_id",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_unit_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_vol_id_conflict_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "vol_id": "test_vol_id_1",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [],
                [{"name": "test_snapshot", "ancestorVolumeId": "test_vol_id"}],
                [{"id": "test_vol_id", "name": "test_vol"}],
            ]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_vol_id_conflict_exception"
            ),
            powerflex_module_mock,
        )

    def test_create_snapshot_vol_name_conflict_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "vol_name": "test_vol_1",
                "state": "present",
            }
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=[
                [],
                [{"id": "test_vol_id", "name": "test_vol"}],
                [{"name": "test_snapshot", "ancestorVolumeId": "test_vol_id"}],
                [{"id": "test_vol_id", "name": "test_vol"}],
            ]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "create_snapshot_vol_name_conflict_exception"
            ),
            powerflex_module_mock,
        )

    def test_get_volume_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "vol_name": "test_vol",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=[{"id": "1"}]
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "get_volume_with_exception"
            ),
            powerflex_module_mock,
        )

    def test_get_datetime(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "desired_retention": 1,
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=[{"id": "1", "creationTime": 2, "secureSnapshotExpTime": 3}]
        )
        powerflex_module_mock.perform_module_operation()

    def test_get_storage_pool_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"snapshot_id": MockSnapshotApi.SNAPSHOT_ID, "state": "present"},
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "get_storage_pool_with_exception"
            ),
            powerflex_module_mock,
        )

    def test_modify_snapshot(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "snapshot_new_name": "test_snapshot_modified",
                "desired_retention": 5,
                "retention_unit": "days",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.rename.assert_called()
        powerflex_module_mock.powerflex_conn.volume.set_retention_period.assert_called()

    def test_rename_snapshot_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "snapshot_new_name": "test_snapshot_modified",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.powerflex_conn.volume.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "rename_snapshot_exception"
            ),
            powerflex_module_mock,
        )

    def test_modify_retention_snapshot_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "desired_retention": 5,
                "retention_unit": "days",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.powerflex_conn.volume.set_retention_period = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "modify_retention_snapshot_exception"
            ),
            powerflex_module_mock,
        )

    def test_retention_hours_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "desired_retention": 999,
                "retention_unit": "hours",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "retention_hours_exception"
            ),
            powerflex_module_mock,
        )

    def test_retention_days_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_id": MockSnapshotApi.SNAPSHOT_ID,
                "desired_retention": 40,
                "retention_unit": "days",
                "state": "present",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response("retention_days_exception"),
            powerflex_module_mock,
        )

    def test_remove_snapshot(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {
                "snapshot_name": "test_snapshot",
                "remove_mode": "ONLY_ME",
                "state": "absent",
            },
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.delete.assert_called()

    def test_remove_snapshot_with_exception(self, powerflex_module_mock):
        self.set_module_params(
            powerflex_module_mock,
            self.get_module_args,
            {"snapshot_name": "test_snapshot", "state": "absent"},
        )
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotApi.SNAPSHOT_GET_LIST
        )
        powerflex_module_mock.powerflex_conn.volume.delete = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockSnapshotApi.get_snapshot_exception_response(
                "remove_snapshot_exception"
            ),
            powerflex_module_mock,
        )
