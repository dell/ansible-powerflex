# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for replication consistency group module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_replication_consistency_group_api import MockReplicationConsistencyGroupApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.replication_consistency_group import PowerFlexReplicationConsistencyGroup


class TestPowerflexReplicationConsistencyGroup():

    get_module_args = MockReplicationConsistencyGroupApi.RCG_COMMON_ARGS

    @pytest.fixture
    def replication_consistency_group_module_mock(self):
        replication_consistency_group_module_mock = PowerFlexReplicationConsistencyGroup()
        replication_consistency_group_module_mock.module.check_mode = False
        return replication_consistency_group_module_mock

    def test_get_rcg_details(self, replication_consistency_group_module_mock):
        self.get_module_args.update({
            "rcg_name": "test_rcg",
            "state": "present"
        })
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_resp = MockReplicationConsistencyGroupApi.get_rcg_details()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=replication_consistency_group_resp
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get.assert_called()

    def test_get_rcg_details_with_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({
            "rcg_name": "test_rcg",
            "state": "present"
        })
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            side_effect=MockApiException)
        replication_consistency_group_module_mock.validate_create = MagicMock()
        replication_consistency_group_module_mock.perform_module_operation()
        assert MockReplicationConsistencyGroupApi.get_exception_response('get_details') in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_rcg_snapshot_response(self, replication_consistency_group_module_mock):
        self.get_module_args.update({
            "rcg_name": "test_rcg",
            "create_snapshot": True,
            "state": "present"
        })
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_resp = MockReplicationConsistencyGroupApi.get_rcg_details()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=replication_consistency_group_resp
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.create_snapshot.assert_called()

    def test_create_rcg_snapshot_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({
            "rcg_id": "aadc17d500000000",
            "create_snapshot": True,
            "state": "present"
        })
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_resp = MockReplicationConsistencyGroupApi.get_rcg_details()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=replication_consistency_group_resp
        )
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.create_snapshot = MagicMock(
            side_effect=MockApiException
        )
        replication_consistency_group_module_mock.perform_module_operation()
        assert MockReplicationConsistencyGroupApi.create_snapshot_exception_response('create_snapshot', self.get_module_args['rcg_id']) \
            in replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({
            "rcg_name": "test_rcg", "rpo": 60, "protection_domain_name": "domain1",
            "protection_domain_id": None, "activity_mode": "active", "state": "present",
            "remote_peer": {"hostname": "1.1.1.1", "username": "username", "password": "password",
                            "verifycert": "verifycert", "port": "port", "protection_domain_name": "None",
                            "protection_domain_id": "123"}})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=None
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.create.assert_called()

    def test_modify_rpo(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rpo": 60, "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details()
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.modify_rpo.assert_called()

    def test_modify_rpo_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rpo": 60, "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.modify_rpo = MagicMock(
            side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Modify rpo for replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_target_volume_access_mode(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "target_volume_access_mode": "Readonly", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details()
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.modify_target_volume_access_mode.assert_called()

    def test_modify_target_volume_access_mode_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "target_volume_access_mode": "Readonly", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.modify_target_volume_access_mode = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Modify target volume access mode for replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_activity_mode(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "activity_mode": "Inactive", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.inactivate.assert_called()

    def test_modify_activity_mode_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "activity_mode": "Active", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details(activity_mode="Inactive"))
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.activate = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Modify activity_mode for replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_pause_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'pause',
                                     "pause_mode": "StopDataTransfer", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details()
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.pause.assert_called()

    def test_pause_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'pause',
                                     "pause_mode": "StopDataTransfer", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.pause = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Pause replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_resume_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'resume', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details(pause_mode="StopDataTransfer"))
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.resume.assert_called()

    def test_resume_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'resume', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details(pause_mode="StopDataTransfer"))
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.resume = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Resume replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_freeze_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'freeze', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.freeze.assert_called()

    def test_freeze_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'freeze', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.freeze = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Freeze replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_unfreeze_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'unfreeze', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details(freeze_state="Frozen")
        )
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.unfreeze.assert_called()

    def test_unfreeze_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'unfreeze', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details(freeze_state="Frozen"))
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.unfreeze = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Unfreeze replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_rename_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "new_rcg_name": "test_rcg_rename", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.rename_rcg.assert_called()

    def test_rename_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "new_rcg_name": "test_rcg_rename", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.rename_rcg = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Renaming replication consistency group to test_rcg_rename failed with error" in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "state": "absent"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.delete.assert_called()

    def test_delete_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "state": "absent"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.delete = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Delete replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_rcg_as_inconsistent(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "is_consistent": False, "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.set_as_inconsistent.assert_called()

    def test_modify_rcg_as_consistent_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "is_consistent": True, "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details(consistency="InConsistent"))
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.set_as_consistent = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Modifying consistency of replication consistency group failed with error" in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_pause_rcg_without_pause_mode(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'pause', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.protection_domain.get = MagicMock(return_value=[{"name": "pd_id"}])
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Specify pause_mode to perform pause on replication consistency group." in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_rcg_with_invalid_params(self, replication_consistency_group_module_mock):
        self.get_module_args.update({
            "rcg_name": "test_rcg", "activity_mode": "active", "state": "present",
            "remote_peer": {"hostname": "1.1.1.1", "username": "username", "password": "password",
                            "verifycert": "verifycert", "port": "port", "protection_domain_name": None,
                            "protection_domain_id": None}})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=None)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Enter remote protection_domain_name or protection_domain_id to create replication consistency group" in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_pause_rcg_without_pause(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "pause_mode": "StopDataTransfer", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.protection_domain.get = MagicMock(return_value=[{"name": "pd_id"}])
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Specify rcg_state as 'pause' to pause replication consistency group" in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_failover_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "failover", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.failover.assert_called()

    def test_failover_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "failover", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.failover = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Failover replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_restore_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "restore", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        rcg_details = MockReplicationConsistencyGroupApi.get_rcg_details()
        rcg_details[0]['failoverType'] = 'Failover'
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(return_value=rcg_details)
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.restore.assert_called()

    def test_restore_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "restore", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        rcg_details = MockReplicationConsistencyGroupApi.get_rcg_details()
        rcg_details[0]['failoverType'] = 'Failover'
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(return_value=rcg_details)
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.restore = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Restore replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_reverse_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "reverse", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        rcg_details = MockReplicationConsistencyGroupApi.get_rcg_details()
        rcg_details[0]['failoverType'] = 'Failover'
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(return_value=rcg_details)
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.reverse.assert_called()

    def test_reverse_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "reverse", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        rcg_details = MockReplicationConsistencyGroupApi.get_rcg_details()
        rcg_details[0]['failoverType'] = 'Failover'
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(return_value=rcg_details)
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.reverse = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Reverse replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_switchover_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "switchover", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.switchover.assert_called()

    def test_switchover_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": "switchover", "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.switchover = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Switchover replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']

    def test_sync_rcg(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'sync', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.perform_module_operation()
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.sync.assert_called()

    def test_sync_rcg_throws_exception(self, replication_consistency_group_module_mock):
        self.get_module_args.update({"rcg_name": "test_rcg", "rcg_state": 'sync', "state": "present"})
        replication_consistency_group_module_mock.module.params = self.get_module_args
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=MockReplicationConsistencyGroupApi.get_rcg_details())
        replication_consistency_group_module_mock.powerflex_conn.replication_consistency_group.sync = \
            MagicMock(side_effect=MockApiException)
        replication_consistency_group_module_mock.perform_module_operation()
        assert "Synchronization of replication consistency group " + MockReplicationConsistencyGroupApi.RCG_ID \
            + MockReplicationConsistencyGroupApi.FAIL_MSG in \
            replication_consistency_group_module_mock.module.fail_json.call_args[1]['msg']
