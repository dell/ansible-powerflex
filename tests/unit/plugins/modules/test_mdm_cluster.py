# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for MDM cluster module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_mdm_cluster_api import MockMdmClusterApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_sdk_response \
    import MockSDKResponse
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.mdm_cluster import PowerFlexMdmCluster


class TestPowerflexMDMCluster():

    get_module_args = MockMdmClusterApi.MDM_CLUSTER_COMMON_ARGS
    add_mdm_ip = "xx.3x.xx.xx"

    @pytest.fixture
    def mdm_cluster_module_mock(self, mocker):
        mocker.patch(MockMdmClusterApi.MODULE_UTILS_PATH + '.PowerFlexClient', new=MockApiException)
        mdm_cluster_module_mock = PowerFlexMdmCluster()
        mdm_cluster_module_mock.module.check_mode = False
        return mdm_cluster_module_mock

    def test_get_mdm_cluster(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details.assert_called()

    def test_get_mdm_cluster_with_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.get_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details.assert_called()

    def test_rename_mdm(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": MockMdmClusterApi.MDM_NAME,
            "mdm_new_name": "mdm_node_renamed",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.rename_mdm = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.rename_mdm.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_rename_mdm_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": MockMdmClusterApi.MDM_NAME,
            "mdm_new_name": "mdm_node_renamed",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.rename_mdm = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.rename_mdm.assert_called()
        assert MockMdmClusterApi.rename_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_set_performance_profile_mdm_cluster(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "performance_profile": "Compact",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.set_cluster_mdm_performance_profile = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.set_cluster_mdm_performance_profile.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_set_performance_profile_mdm_cluster_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "performance_profile": "Compact",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.set_cluster_mdm_performance_profile = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.set_cluster_mdm_performance_profile.assert_called()
        assert MockMdmClusterApi.perf_profile_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_set_virtual_ip_interface_mdm(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": MockMdmClusterApi.MDM_ID,
            "virtual_ip_interfaces": ["ens11"],
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.modify_virtual_ip_interface = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.modify_virtual_ip_interface.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_set_virtual_ip_interface_mdm_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": MockMdmClusterApi.MDM_ID,
            "virtual_ip_interfaces": ["ens11"],
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.modify_virtual_ip_interface = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.modify_virtual_ip_interface.assert_called()
        assert MockMdmClusterApi.virtual_ip_interface_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_set_virtual_ip_interface_mdm_idempotency(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": MockMdmClusterApi.MDM_ID,
            "virtual_ip_interfaces": ["ens1"],
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_remove_standby_mdm(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": MockMdmClusterApi.STB_TB_MDM_ID,
            "state": "absent"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.remove_standby_mdm = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.remove_standby_mdm.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_remove_standby_mdm_idempotency(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "non_existing_node",
            "state": "absent"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_remove_standby_mdm_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": MockMdmClusterApi.STB_TB_MDM_ID,
            "state": "absent"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.remove_standby_mdm = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.remove_standby_mdm.assert_called()
        assert MockMdmClusterApi.remove_mdm_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_standby_mdm(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "standby_node",
            "standby_mdm": {
                "mdm_ips": [self.add_mdm_ip],
                "role": "Manager",
                "port": 9011,
                "management_ips": [self.add_mdm_ip],
                "virtual_interfaces": ["ens1"],
                "allow_multiple_ips": True
            },
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS
        )
        mdm_cluster_module_mock.powerflex_conn.system.add_standby_mdm = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.add_standby_mdm.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_add_standby_mdm_idempotency(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": MockMdmClusterApi.MDM_NAME,
            "standby_mdm": {
                "mdm_ips": ["10.x.z.z"],
                "role": "TieBreaker",
                "port": 9011
            },
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_add_standby_mdm_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "standby_node",
            "standby_mdm": {
                "mdm_ips": [self.add_mdm_ip],
                "role": "Manager",
                "port": 9011,
                "management_ips": [self.add_mdm_ip],
                "virtual_interfaces": ["ens1"],
                "allow_multiple_ips": True
            },
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS
        )
        mdm_cluster_module_mock.powerflex_conn.system.add_standby_mdm = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.add_standby_mdm.assert_called()
        assert MockMdmClusterApi.add_mdm_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_change_mdm_cluster_owner(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "sample_mdm1",
            "is_primary": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.change_mdm_ownership = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.change_mdm_ownership.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_change_mdm_cluster_owner_idempotency(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": "5908d328581d1400",
            "is_primary": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(
            MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_change_mdm_cluster_owner_execption(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "sample_mdm1",
            "is_primary": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.change_mdm_ownership = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.change_mdm_ownership.assert_called()
        assert MockMdmClusterApi.owner_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_expand_mdm_cluster_mode(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": MockMdmClusterApi.STB_TB_MDM_ID,
                    "mdm_name": None,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "present-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_reduce_mdm_cluster_mode_idempotency(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "ThreeNodes",
            "mdm": [
                {
                    "mdm_name": None,
                    "mdm_id": MockMdmClusterApi.STB_MGR_MDM_ID,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": None,
                    "mdm_name": MockMdmClusterApi.MDM_NAME,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "absent-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_expand_mdm_cluster_mode_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": MockMdmClusterApi.STB_TB_MDM_ID,
                    "mdm_name": None,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "present-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode.assert_called()
        assert MockMdmClusterApi.switch_mode_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_reduce_mdm_cluster_mode(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "ThreeNodes",
            "mdm": [
                {
                    "mdm_name": None,
                    "mdm_id": MockMdmClusterApi.STB_MGR_MDM_ID,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": None,
                    "mdm_name": MockMdmClusterApi.MDM_NAME,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "absent-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.FIVE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_clear_virtual_ip_interface_mdm(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": MockMdmClusterApi.STB_MGR_MDM_ID,
            "clear_interfaces": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.modify_virtual_ip_interface = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        mdm_cluster_module_mock.powerflex_conn.system.modify_virtual_ip_interface.assert_called()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_clear_virtual_ip_interface_mdm_idempotency(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "sample_mdm11",
            "clear_interfaces": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.FIVE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_get_system_id_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_module_mock.powerflex_conn.system.get = MagicMock(
            side_effect=utils.PowerFlexClient
        )
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.system_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_mdm_cluster_owner_none(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "state": "absent"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.remove_mdm_no_id_name_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_expand_cluster_without_standby(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": None,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": None,
                    "mdm_name": None,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "present-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS_2)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.without_standby_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_system_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        system_resp = MockSDKResponse(MockMdmClusterApi.PARTIAL_SYSTEM_DETAILS_1)
        mdm_cluster_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=system_resp.__dict__['data']
        )
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value={}
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.no_cluster_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_clear_virtual_ip_interface_mdm_id_none(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": None,
            "clear_interfaces": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.is_mdm_name_id_exists = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS['master']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.id_none_interface_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_rename_mdm_id_none(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": None,
            "mdm_new_name": "new_node",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.is_mdm_name_id_exists = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS['master']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.id_none_rename_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_change_owner_id_none(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_id": None,
            "is_primary": True,
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.is_mdm_name_id_exists = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS['master']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.id_none_change_owner_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_multiple_system_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        system_resp = MockSDKResponse(MockMdmClusterApi.PARTIAL_SYSTEM_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=system_resp.__dict__['data']
        )
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.multiple_system_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_add_standby_mdm_new_name_exception(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "mdm_name": "standby_node",
            "standby_mdm": {
                "mdm_ips": [self.add_mdm_ip],
                "role": "Manager",
                "port": 9011,
                "management_ips": [self.add_mdm_ip],
                "virtual_interfaces": ["ens1"],
                "allow_multiple_ips": True
            },
            "mdm_new_name": "new_node",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_module_mock.get_mdm_cluster_details = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS
        )
        mdm_cluster_module_mock.is_mdm_name_id_exists = MagicMock(
            return_value=MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS['master']
        )
        mdm_cluster_module_mock.perform_module_operation()
        assert MockMdmClusterApi.new_name_add_mdm_failed_response() in mdm_cluster_module_mock.module.fail_json.call_args[1]['msg']

    def test_change_cluster_mode(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": MockMdmClusterApi.STB_TB_MDM_ID,
                    "mdm_name": None,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "absent-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.validate_parameters = MagicMock(return_value=None)
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_change_cluster_mode_with_name(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": MockMdmClusterApi.MDM_ID,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": MockMdmClusterApi.STB_TB_MDM_ID,
                    "mdm_name": MockMdmClusterApi.MDM_NAME,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "absent-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.validate_parameters = MagicMock(return_value=None)
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_cluster_reduce_mode_absent(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": None,
                    "mdm_name": MockMdmClusterApi.MDM_NAME,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "absent-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.is_mdm_name_id_exists = MagicMock(return_value=None)
        mdm_cluster_module_mock.validate_parameters = MagicMock(return_value=None)
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_cluster_expand_list_tb(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": None,
                    "mdm_name": MockMdmClusterApi.MDM_NAME,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "present-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.validate_parameters = MagicMock(return_value=None)
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_cluster_expand_list_tb_mdm_none(self, mdm_cluster_module_mock):
        self.get_module_args.update({
            "cluster_mode": "FiveNodes",
            "mdm": [
                {
                    "mdm_name": MockMdmClusterApi.MDM_NAME_STB_MGR,
                    "mdm_id": None,
                    "mdm_type": "Secondary"
                },
                {
                    "mdm_id": None,
                    "mdm_name": MockMdmClusterApi.MDM_NAME,
                    "mdm_type": "TieBreaker"
                }
            ],
            "mdm_state": "present-in-cluster",
            "state": "present"
        })
        mdm_cluster_module_mock.module.params = self.get_module_args
        mdm_cluster_resp = MockSDKResponse(MockMdmClusterApi.THREE_MDM_CLUSTER_DETAILS)
        mdm_cluster_module_mock.powerflex_conn.system.get_mdm_cluster_details = MagicMock(
            return_value=mdm_cluster_resp.__dict__['data']
        )
        mdm_cluster_module_mock.is_mdm_name_id_exists = MagicMock(return_value=None)
        mdm_cluster_module_mock.validate_parameters = MagicMock(return_value=None)
        mdm_cluster_module_mock.powerflex_conn.system.switch_cluster_mode = MagicMock()
        mdm_cluster_module_mock.perform_module_operation()
        assert mdm_cluster_module_mock.module.exit_json.call_args[1]['changed'] is True
