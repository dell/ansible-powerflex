# Copyright: (c) 2023, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for snapshot policy module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_snapshot_policy_api import MockSnapshotPolicyApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.snapshot_policy import PowerFlexSnapshotPolicy, SnapshotPolicyHandler


class TestPowerflexSnapshotPolicy():

    get_module_args = MockSnapshotPolicyApi.SNAPSHOT_POLICY_COMMON_ARGS

    @pytest.fixture
    def snapshot_policy_module_mock(self, mocker):
        snapshot_policy_module_mock = PowerFlexSnapshotPolicy()
        snapshot_policy_module_mock.module.check_mode = False
        snapshot_policy_module_mock.module.fail_json = fail_json
        return snapshot_policy_module_mock

    def capture_fail_json_call(self, error_msg, snapshot_policy_module_mock):
        try:
            SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        except FailJsonException as fj_object:
            assert error_msg == fj_object.message

    def test_get_snapshot_policy_detail_using_name(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get.assert_called()
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics.assert_called()

    def test_get_snapshot_policy_detail_using_id(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_id": "testing",
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get.assert_called()
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics.assert_called()

    def test_get_snapshot_policy_details_with_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('get_snapshot_policy_details_exception'),
                                    snapshot_policy_module_mock)

    def test_create_snapshot_policy_using_name(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "access_mode": "ReadOnly",
            "secure_snapshots": True,
            "auto_snapshot_creation_cadence": {
                "time": 1,
                "unit": "Hour"},
            "num_of_retained_snapshots_per_level": [20],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=None
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.create.assert_called()

    def test_create_snapshot_policy_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "access_mode": "ReadOnly",
            "secure_snapshots": True,
            "auto_snapshot_creation_cadence": {
                "time": 1,
                "unit": "Hour"},
            "num_of_retained_snapshots_per_level": [20],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=None
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.create = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('create_exception'),
                                    snapshot_policy_module_mock)

    def test_create_snapshot_policy_with_id_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_id": "testing",
            "access_mode": "ReadOnly",
            "secure_snapshots": True,
            "auto_snapshot_creation_cadence": {
                "time": 1,
                "unit": "Hour"},
            "num_of_retained_snapshots_per_level": [20],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=None
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('create_id_exception'),
                                    snapshot_policy_module_mock)

    def test_delete_snapshot_policy(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "state": "absent"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.delete.assert_called()

    def test_delete_snapshot_policy_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "state": "absent"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.delete = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('delete_exception'),
                                    snapshot_policy_module_mock)

    def test_modify_snapshot_policy(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "auto_snapshot_creation_cadence": {
                "time": 20,
                "unit": "Minute"},
            "num_of_retained_snapshots_per_level": [30],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.modify.assert_called()

    def test_modify_snapshot_policy_wo_snapshot_rule(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "num_of_retained_snapshots_per_level": [30],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.modify.assert_called()

    def test_modify_snapshot_policy_wo_retention_rule(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "auto_snapshot_creation_cadence": {
                "time": 20,
                "unit": "Minute"},
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.modify.assert_called()

    def test_modify_snapshot_policy_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "auto_snapshot_creation_cadence": {
                "time": 20,
                "unit": "Minute"},
            "num_of_retained_snapshots_per_level": [30],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.modify = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('modify_exception'),
                                    snapshot_policy_module_mock)

    def test_rename_snapshot_policy(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "new_name": "testing_new",
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.rename.assert_called()

    def test_rename_snapshot_policy_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "new_name": "testing_new",
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.rename = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('modify_exception'),
                                    snapshot_policy_module_mock)

    def test_add_source_volume(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "source_volume": [{
                "name": "source_volume_name",
                "id": None,
                "auto_snap_removal_action": None,
                "detach_locked_auto_snapshots": None,
                "state": "present"}],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotPolicyApi.VOLUME_GET_LIST
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.add_source_volume.assert_called()

    def test_add_non_existing_volume_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "source_volume": [{
                "name": "non_existing_source_volume_name",
                "id": None,
                "auto_snap_removal_action": None,
                "detach_locked_auto_snapshots": None}],
            "source_volume_state": "present",
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('add_non_existing_source_volume'),
                                    snapshot_policy_module_mock)

    def test_add_source_volume_wo_id_or_name_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "source_volume": [{
                "name": None,
                "id": None,
                "auto_snap_removal_action": None,
                "detach_locked_auto_snapshots": None,
                "state": "present"}],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('add_source_volume_wo_vol'),
                                    snapshot_policy_module_mock)

    def test_add_source_volume_wo_id_and_name_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "source_volume": [{
                "name": "source_volume_name",
                "id": "source_volume_id",
                "auto_snap_removal_action": None,
                "detach_locked_auto_snapshots": None,
                "state": "present"}],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('add_source_volume_vol_id_name'),
                                    snapshot_policy_module_mock)

    def test_add_source_volume_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing",
            "source_volume": [{
                "name": "source_volume_name",
                "id": None,
                "auto_snap_removal_action": None,
                "detach_locked_auto_snapshots": None,
                "state": "present"}],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotPolicyApi.VOLUME_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.add_source_volume = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('source_volume_exception'),
                                    snapshot_policy_module_mock)

    def test_remove_source_volume(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing_2",
            "source_volume": [{
                "id": "source_volume_id_2",
                "name": None,
                "auto_snap_removal_action": 'Remove',
                "detach_locked_auto_snapshots": None,
                "state": "absent"}],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_2_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockSnapshotPolicyApi.VOLUME_2_GET_LIST
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.remove_source_volume.assert_called()

    def test_pause_snapshot_policy(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing_2",
            "pause": True,
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.pause.assert_called()

    def test_resume_snapshot_policy(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing_2",
            "pause": False,
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_2_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        SnapshotPolicyHandler().handle(snapshot_policy_module_mock, snapshot_policy_module_mock.module.params)
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.resume.assert_called()

    def test_pause_snapshot_policy_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing_2",
            "pause": True,
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_2_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.volume.pause = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('pause_exception'),
                                    snapshot_policy_module_mock)

    def test_remove_source_volume_exception(self, snapshot_policy_module_mock):
        self.get_module_args.update({
            "snapshot_policy_name": "testing_2",
            "source_volume": [{
                "id": "source_volume_id_2",
                "name": None,
                "auto_snap_removal_action": 'Remove',
                "detach_locked_auto_snapshots": None,
                "state": "absent"}],
            "state": "present"
        })
        snapshot_policy_module_mock.module.params = self.get_module_args
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_2_GET_LIST
        )
        snapshot_policy_module_mock.powerflex_conn.snapshot_policy.get_statistics = MagicMock(
            return_value=MockSnapshotPolicyApi.SNAPSHOT_POLICY_STATISTICS
        )
        snapshot_policy_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockSnapshotPolicyApi.get_snapshot_policy_exception_response('get_vol_details_exception'),
                                    snapshot_policy_module_mock)
