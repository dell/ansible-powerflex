# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for info module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_info_api import MockInfoApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fault_set_api import MockFaultSetApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fail_json \
    import FailJsonException, fail_json

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()
utils.filter_response = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.info import PowerFlexInfo
INVALID_SORT_MSG = 'messageCode=PARSE002 displayMessage=An invalid column name: invalid is entered in the sort list'


class TestPowerflexInfo():

    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        mocker.patch(
            MockInfoApi.MODULE_UTILS_PATH + '.PowerFlexClient',
            new=MockApiException)
        info_module_mock = PowerFlexInfo()
        info_module_mock.module.check_mode = False
        info_module_mock.powerflex_conn.system.api_version = MagicMock(
            return_value=3.5
        )
        info_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockInfoApi.INFO_ARRAY_DETAILS
        )
        info_module_mock.module.fail_json = fail_json
        return info_module_mock

    def capture_fail_json_call(self, error_msg, info_module_mock):
        try:
            info_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_volume_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        volume_resp = MockInfoApi.INFO_VOLUME_GET_LIST
        info_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_stat_resp = MockInfoApi.INFO_VOLUME_STATISTICS
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_volumes = MagicMock(
            return_value=volume_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.volume.get.assert_called()
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_volumes.assert_called()

    def test_get_volume_details_filter(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['vol'],
            "filters": [{
                "filter_key": "storagePoolId",
                "filter_operator": "equal",
                "filter_value": "test_pool_id_1"
            }]
        })
        info_module_mock.module.params = self.get_module_args
        vol_resp = MockInfoApi.INFO_VOLUME_GET_LIST
        info_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=vol_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.volume.get.assert_called()

    def test_get_volume_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        volume_resp = MockInfoApi.INFO_VOLUME_GET_LIST
        info_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_volumes = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'volume_get_details'), info_module_mock)

    def test_get_sp_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['storage_pool']
        })
        info_module_mock.module.params = self.get_module_args
        sp_resp = MockInfoApi.INFO_STORAGE_POOL_GET_LIST
        info_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=sp_resp
        )
        sp_stat_resp = MockInfoApi.INFO_STORAGE_POOL_STATISTICS
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_storagepools = MagicMock(
            return_value=sp_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.storage_pool.get.assert_called()
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_storagepools.assert_called()

    def test_get_sp_details_filter(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['storage_pool'],
            "filters": [{
                "filter_key": "id",
                "filter_operator": "equal",
                "filter_value": "test_pool_id_1"
            }]
        })
        info_module_mock.module.params = self.get_module_args
        storage_pool_resp = MockInfoApi.INFO_STORAGE_POOL_GET_LIST
        info_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=storage_pool_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.storage_pool.get.assert_called()

    def test_get_sp_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['storage_pool']
        })
        info_module_mock.module.params = self.get_module_args
        sp_resp = MockInfoApi.INFO_STORAGE_POOL_GET_LIST
        info_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            return_value=sp_resp
        )
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_storagepools = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'sp_get_details'), info_module_mock)

    def test_get_rcg_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['rcg']
        })
        info_module_mock.module.params = self.get_module_args
        rcg_resp = MockInfoApi.RCG_LIST
        info_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=rcg_resp)
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.replication_consistency_group.get.assert_called()

    def test_get_rcg_filter_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['rcg'],
            "filters": [{
                "filter_key": "id",
                "filter_operator": "equal",
                "filter_value": "aadc17d500000000"
            }]
        })
        info_module_mock.module.params = self.get_module_args
        rcg_resp = MockInfoApi.RCG_LIST
        info_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            return_value=rcg_resp)
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.replication_consistency_group.get.assert_called()

    def test_get_rcg_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['rcg']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.replication_consistency_group.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'rcg_get_details'), info_module_mock)

    def test_get_replication_pair_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['replication_pair']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.replication_pair.get = MagicMock(
            return_value=MockInfoApi.PAIR_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.replication_pair.get.assert_called()

    def test_get_replication_pair_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['replication_pair']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.replication_pair.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'replication_pair_get_details'), info_module_mock)

    def test_get_snapshot_policy_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['snapshot_policy']
        })
        info_module_mock.module.params = self.get_module_args
        snapshot_policy_resp = MockInfoApi.INFO_SNAPSHOT_POLICY_GET_LIST
        info_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=snapshot_policy_resp
        )
        snapshot_policy_stat_resp = MockInfoApi.INFO_SNAPSHOT_POLICY_STATISTICS
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_snapshot_policies = MagicMock(
            return_value=snapshot_policy_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.snapshot_policy.get.assert_called()
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_snapshot_policies.assert_called()

    def test_get_snapshot_policy_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['snapshot_policy']
        })
        info_module_mock.module.params = self.get_module_args
        snapshot_policy_resp = MockInfoApi.INFO_SNAPSHOT_POLICY_GET_LIST
        info_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=snapshot_policy_resp
        )
        info_module_mock.powerflex_conn.utility.get_statistics_for_all_snapshot_policies = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'snapshot_policy_get_details'), info_module_mock)

    def test_get_sdc_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sdc']
        })
        info_module_mock.module.params = self.get_module_args
        sdc_resp = MockInfoApi.INFO_SDC_FILTER_LIST
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=sdc_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_sdc_details_filter(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sdc'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": "equal",
                "filter_value": "sdc_1"
            }]
        })
        info_module_mock.module.params = self.get_module_args
        sdc_resp = MockInfoApi.INFO_SDC_FILTER_LIST
        info_module_mock.powerflex_conn.sdc.create = MagicMock(
            return_value=sdc_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_sdc_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sdc']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'sdc_get_details'), info_module_mock)

    def test_get_sds_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sds']
        })
        info_module_mock.module.params = self.get_module_args
        sds_resp = MockInfoApi.INFO_SDS_GET_LIST
        info_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=sds_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sds.get.assert_called()

    def test_get_sds_filter_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sds'],
            "filters": [
                {
                    "filter_key": "name",
                    "filter_operator": "equal",
                    "filter_value": "node0",
                },
                {
                    "filter_key": "name",
                    "filter_operator": "equal",
                    "filter_value": "node1",
                },
                {
                    "filter_key": "id",
                    "filter_operator": "equal",
                    "filter_value": "8f3bb15300000001",
                }
            ]
        })
        info_module_mock.module.params = self.get_module_args
        sds_resp = MockInfoApi.INFO_SDS_GET_LIST
        info_module_mock.powerflex_conn.sds.get = MagicMock(
            return_value=sds_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sds.get.assert_called()

    def test_get_sds_details_filter_invalid(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sds'],
            "filters": [{
                "filter_key": "name",
                "filter_op": "equal",
                "filter_value": "LGLAP203",
            }]
        })
        info_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'get_sds_details_filter_invalid'), info_module_mock)

    def test_get_sds_details_filter_empty(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sds'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": None,
                "filter_value": "LGLAP203",
            }]
        })
        info_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'get_sds_details_filter_empty'), info_module_mock)

    def test_get_sds_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sds']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.sds.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'sds_get_details'), info_module_mock)

    def test_get_pd_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['protection_domain']
        })
        info_module_mock.module.params = self.get_module_args
        pd_resp = MockInfoApi.INFO_GET_PD_LIST
        info_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.protection_domain.get.assert_called()

    def test_get_pd_filter_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['protection_domain'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": "equal",
                "filter_value": "domain1",
            }]
        })
        info_module_mock.module.params = self.get_module_args
        pd_resp = MockInfoApi.INFO_GET_PD_LIST
        info_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.protection_domain.get.assert_called()

    def test_get_pd_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['protection_domain']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'pd_get_details'), info_module_mock)

    def test_get_device_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['device']
        })
        info_module_mock.module.params = self.get_module_args
        device_resp = MockInfoApi.INFO_GET_DEVICE_LIST
        info_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=device_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_filter_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['device'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": "equal",
                "filter_value": "device230",
            }]
        })
        info_module_mock.module.params = self.get_module_args
        device_resp = MockInfoApi.INFO_GET_DEVICE_LIST
        info_module_mock.powerflex_conn.device.get = MagicMock(
            return_value=device_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.device.get.assert_called()

    def test_get_device_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['device']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.device.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'device_get_details'), info_module_mock)

    def test_get_fault_set_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['fault_set']
        })
        info_module_mock.module.params = self.get_module_args
        pd_resp = MockFaultSetApi.PROTECTION_DOMAIN
        info_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=pd_resp['protectiondomain'])
        fault_set_resp = MockInfoApi.INFO_GET_FAULT_SET_LIST
        info_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fault_set_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.fault_set.get.assert_called()

    def test_get_fault_set_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['fault_set']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.fault_set.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'fault_set_get_details'), info_module_mock)

    def test_get_fault_set_details_invalid_filter_operator_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['fault_set'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": "does_not_contain",
                "filter_value": "LGLAP203",
            }]
        })
        info_module_mock.module.params = self.get_module_args
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'invalid_filter_operator_exception'), info_module_mock)

    def test_get_fault_set_details_api_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['fault_set']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.system.api_version = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'api_exception'), info_module_mock)

    def test_get_fault_set_details_system_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['fault_set']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.system.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'system_exception'), info_module_mock)

    def test_get_managed_device_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['managed_device']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.managed_device.get = MagicMock()
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.managed_device.get.assert_called()

    def test_get_managed_device_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['managed_device']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.managed_device.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'managed_device_get_error'), info_module_mock)

    def test_get_service_template_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['service_template']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.service_template.get = MagicMock()
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.service_template.get.assert_called()

    def test_get_service_template_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['service_template']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.service_template.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'service_template_get_error'), info_module_mock)

    def test_get_deployment_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['deployment'],
            "limit": 20
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.deployment.get = MagicMock()
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.deployment.get.assert_called()

    def test_get_deployment_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['deployment']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.deployment.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'deployment_get_error'), info_module_mock)

    def test_get_deployment_details_throws_exception_invalid_sort(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['deployment'],
            "sort": 'invalid'
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.deployment.get = MagicMock(
            side_effect=MockApiException(INVALID_SORT_MSG)
        )
        info_module_mock.perform_module_operation()
        assert info_module_mock.get_deployments_list() == []

    def test_get_with_multiple_gather_subset(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['deployment', 'service_template'],
            "sort": 'name', "filters": [{"filter_key": "name", "filter_operator": "equal", "filter_value": "rack"}],
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert info_module_mock.populate_filter_list() == []
        assert info_module_mock.get_param_value('sort') is None

    def test_get_with_invalid_offset_and_limit_for_subset(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['deployment'],
            "limit": -1, "offset": -1
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.perform_module_operation()
        assert info_module_mock.get_param_value('limit') is None
        assert info_module_mock.get_param_value('offset') is None

    def test_get_firmware_repository_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['firmware_repository'],
            "limit": 20
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.firmware_repository.get = MagicMock()
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.firmware_repository.get.assert_called()

    def test_get_deployment_details_throws_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['firmware_repository']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.firmware_repository.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'firmware_repository_get_error'), info_module_mock)

    def test_get_nvme_host_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['nvme_host']
        })
        info_module_mock.module.params = self.get_module_args
        nvme_host_resp = MockInfoApi.INFO_NVME_HOST_LIST
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=nvme_host_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_details_filter(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['nvme_host'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": "equal",
                "filter_value": "fake_host_name_1"
            }]
        })
        info_module_mock.module.params = self.get_module_args
        nvme_host_resp = MockInfoApi.INFO_SDC_FILTER_LIST
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=nvme_host_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sdc.get.assert_called()

    def test_get_nvme_host_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['nvme_host']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'nvme_host_get_details'), info_module_mock)

    def test_get_sdt_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sdt']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.sdt.get = MagicMock(
            return_value=MockInfoApi.INFO_GET_SDT_LIST
        )
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockInfoApi.INFO_GET_SDT_NVME_HOST_LIST
        )
        info_module_mock.powerflex_conn.host.get_related = MagicMock(
            return_value=MockInfoApi.INFO_GET_SDT_NVME_CONTROLLER_LIST
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sdt.get.assert_called()
        info_module_mock.powerflex_conn.sdc.get.assert_called()
        info_module_mock.powerflex_conn.host.get_related.assert_called()

    def test_get_sdt_details_filter(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sdt'],
            "filters": [{
                "filter_key": "name",
                "filter_operator": "equal",
                "filter_value": "sdt-name",
            }]
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.sdt.get = MagicMock(
            return_value=MockInfoApi.INFO_GET_SDT_LIST
        )
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockInfoApi.INFO_GET_SDT_NVME_HOST_LIST
        )
        info_module_mock.powerflex_conn.host.get_related = MagicMock(
            return_value=MockInfoApi.INFO_GET_SDT_NVME_CONTROLLER_LIST
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.sdt.get.assert_called()
        info_module_mock.powerflex_conn.sdc.get.assert_called()
        info_module_mock.powerflex_conn.host.get_related.assert_called()

    def test_get_sdt_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['sdt']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.sdc.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'sdt_get_error'), info_module_mock)
