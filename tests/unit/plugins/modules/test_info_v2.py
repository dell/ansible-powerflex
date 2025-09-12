# Copyright: (c) 2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Info V2 module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_info_api_v2 import MockInfoApi
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
from ansible_collections.dellemc.powerflex.plugins.modules.info_v2 import PowerFlexInfo, get_powerflex_info_parameters
INVALID_SORT_MSG = 'messageCode=PARSE002 displayMessage=An invalid column name: invalid is entered in the sort list'


class TestPowerflexInfo():

    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        mocker.patch(
            MockInfoApi.MODULE_UTILS_PATH + '.PowerFlexClient',
            new=MockApiException)
        utils.is_version_less = MagicMock(return_value=False)
        utils.is_version_ge_or_eq = MagicMock(return_value=True)
        info_module_mock = PowerFlexInfo()
        info_module_mock.module.argument_spec = get_powerflex_info_parameters()
        info_module_mock.module.check_mode = False
        info_module_mock.powerflex_conn.system.get = MagicMock(
            return_value=MockInfoApi.INFO_ARRAY_DETAILS
        )
        info_module_mock.module.fail_json = fail_json
        return info_module_mock

    def capture_fail_json_call(self, error_msg, info_module_mock):
        try:
            info_module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            assert len(error_msg) > 0 and error_msg in fj_object.message

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
        info_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=volume_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.volume.get.assert_called()
        info_module_mock.powerflex_conn.utility.query_metrics.assert_called()

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
        info_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
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
        info_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            return_value=sp_stat_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.storage_pool.get.assert_called()
        info_module_mock.powerflex_conn.utility.query_metrics.assert_called()

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
        info_module_mock.powerflex_conn.utility.query_metrics = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'sp_get_details'), info_module_mock)

    def test_get_snapshot_policy_details(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['snapshot_policy']
        })
        info_module_mock.module.params = self.get_module_args
        snapshot_policy_resp = MockInfoApi.INFO_SNAPSHOT_POLICY_GET_LIST
        info_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=snapshot_policy_resp
        )
        info_module_mock.perform_module_operation()
        info_module_mock.powerflex_conn.snapshot_policy.get.assert_called()

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

    def test_get_snapshot_policy_details_exception(self, info_module_mock):
        self.get_module_args.update({
            "gather_subset": ['snapshot_policy']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'snapshot_policy_get_error'), info_module_mock)

    def test_get_array_details_exception(self, info_module_mock):
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.system.get = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'array_get_error'), info_module_mock)

    def test_get_version_exception(self, info_module_mock):
        info_module_mock.module.params = self.get_module_args
        info_module_mock.powerflex_conn.system.api_version = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(MockInfoApi.get_exception_response(
            'version_get_error'), info_module_mock)
