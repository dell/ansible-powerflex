# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for volume module on PowerFlex"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_volume_v2_api import (
    MockVolumeApi,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries.powerflex_unit_base import (
    PowerFlexUnitBase,
)
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import (
    utils,
)
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fail_json import (
    FailJsonException,
    fail_json,
)

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.volume_v2 import (
    PowerFlexVolumeV2,
)


class TestPowerflexVolume(PowerFlexUnitBase):

    get_module_args = MockVolumeApi.VOLUME_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PowerFlexVolumeV2

    def capture_fail_json_call(
        self, error_msg, powerflex_module_mock, function_to_call, *args, **kwargs
    ):
        powerflex_module_mock.module.fail_json = fail_json
        try:
            function_to_call(*args, **kwargs)
        except FailJsonException as fj_object:
            assert error_msg in fj_object.message

    def test_get_volume_details(self, powerflex_module_mock):
        self.get_module_args.update({"vol_name": "testing", "state": "present"})
        powerflex_module_mock.module.params = self.get_module_args
        volume_resp = MockVolumeApi.VOLUME_GET_LIST
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_sp_resp = MockVolumeApi.VOLUME_STORAGEPOOL_DETAILS
        powerflex_module_mock.get_storage_pool = MagicMock(return_value=volume_sp_resp)
        volume_pd_resp = MockVolumeApi.VOLUME_PD_DETAILS
        powerflex_module_mock.get_protection_domain = MagicMock(
            return_value=volume_pd_resp
        )
        volume_statistics_resp = MockVolumeApi.VOLUME_STATISTICS
        powerflex_module_mock.powerflex_conn.volume.get_statistics = MagicMock(
            return_value=volume_statistics_resp
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.get.assert_called()
        powerflex_module_mock.powerflex_conn.volume.get_statistics.assert_called()

    def test_get_volume_details_with_exception(self, powerflex_module_mock):
        self.get_module_args.update({"vol_name": "testing", "state": "present"})
        powerflex_module_mock.module.params = self.get_module_args
        volume_resp = MockVolumeApi.VOLUME_GET_LIST
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        powerflex_module_mock.powerflex_conn.volume.get_statistics = MagicMock(
            side_effect=MockApiException
        )
        powerflex_module_mock.create_volume = MagicMock(return_value=None)
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("get_details"),
            powerflex_module_mock,
            powerflex_module_mock.perform_module_operation,
        )

    @pytest.mark.parametrize(
        "params",
        [
            {"pd_id": "123"},
            {"pd_name": "test"},
        ],
    )
    def test_get_protection_domain(self, powerflex_module_mock, params):
        pd_id = params.get("pd_id", None)
        pd_name = params.get("pd_name", None)
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockVolumeApi.PROTECTION_DETAILS
        )
        pd_details = powerflex_module_mock.get_protection_domain(pd_name, pd_id)
        assert MockVolumeApi.PROTECTION_DETAILS[0] == pd_details

    def test_get_protection_domain_exeception(self, powerflex_module_mock):
        pd_id = "pd_id"
        pd_name = "pd_name"
        powerflex_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=None
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("get_pd_exception"),
            powerflex_module_mock,
            powerflex_module_mock.get_protection_domain,
            pd_name,
            pd_id,
        )

    @pytest.mark.parametrize(
        "params",
        [
            {"pol_id": "123"},
            {"pol_name": "test"},
        ],
    )
    def test_get_snapshot_policy(self, powerflex_module_mock, params):
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        powerflex_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockVolumeApi.PROTECTION_DETAILS
        )
        snap_pol_details = powerflex_module_mock.get_snapshot_policy(pol_id, pol_name)
        assert MockVolumeApi.PROTECTION_DETAILS[0] == snap_pol_details

    def test_get_snapshot_policy_exception(self, powerflex_module_mock):
        pol_id = "pol_id"
        pol_name = "pol_name"
        powerflex_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=None
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("get_sp_exception"),
            powerflex_module_mock,
            powerflex_module_mock.get_snapshot_policy,
            pol_id,
            pol_name,
        )

    @pytest.mark.parametrize(
        "params",
        [
            {"pol_id": "123", "prot_id": "123"},
        ],
    )
    def test_get_storage_pool(self, powerflex_module_mock, params):
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        prot_id = params.get("prot_id", None)

        def mock_get(filter_fields):
            if filter_fields.get("protectionDomainId", None):
                return MockVolumeApi.PROTECTION_DETAILS
            else:
                return MockVolumeApi.PROTECTION_DETAILS_MULTI

        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            side_effect=mock_get
        )
        sp_details = powerflex_module_mock.get_storage_pool(pol_id, pol_name, prot_id)
        assert MockVolumeApi.PROTECTION_DETAILS[0] == sp_details

    @pytest.mark.parametrize(
        "params",
        [
            {"pol_id": "123", "assert_msg": "get_spool_error1"},
            {"pol_name": "123", "prot_id": "123", "assert_msg": "get_spool_error2"},
        ],
    )
    def test_get_storage_pool_error(self, powerflex_module_mock, params):
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        prot_id = params.get("prot_id", None)

        def mock_get(filter_fields):
            if filter_fields.get("protectionDomainId", None):
                return None
            else:
                return MockVolumeApi.PROTECTION_DETAILS_MULTI

        powerflex_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            side_effect=mock_get
        )

        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response(params.get("assert_msg")),
            powerflex_module_mock,
            powerflex_module_mock.get_storage_pool,
            pol_id,
            pol_name,
            prot_id,
        )

    @pytest.mark.parametrize("params", [{"vol_name": "123"}])
    def test_get_volume(self, powerflex_module_mock, params):
        vol_name = params.get("vol_name", None)
        vol_id = params.get("vol_id", None)
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST
        )
        powerflex_module_mock.get_snapshot_policy = MagicMock(
            return_value={"name": "snapshotPolicyName"}
        )
        volume_details = powerflex_module_mock.get_volume(vol_name, vol_id)
        assert (
            volume_details["snapshotPolicyId"]
            == MockVolumeApi.VOLUME_GET_LIST[0]["snapshotPolicyId"]
        )
        assert (
            volume_details["snapshotPolicyName"]
            == MockVolumeApi.VOLUME_GET_LIST[0]["snapshotPolicyName"]
        )

    def test_get_volume_not_found(self, powerflex_module_mock):
        vol_name = None
        vol_id = "test_vol_id"
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(return_value=[])
        volume_details = powerflex_module_mock.get_volume(vol_name, vol_id)
        assert volume_details is None

    def test_get_volume_exeception(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=MockApiException
        )
        powerflex_module_mock.get_snapshot_policy = MagicMock(
            return_value={"name": "snapshotPolicyName"}
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("get_details"),
            powerflex_module_mock,
            powerflex_module_mock.get_volume,
            "test_name_1",
            "test_id_1",
        )

    @pytest.mark.parametrize(
        "params",
        [
            {"sdc_id": "sdc_id"},
            {"sdc_ip": "sdc_ip"},
        ],
    )
    def test_get_sdc_id(self, powerflex_module_mock, params):
        sdc_name = params.get("sdc_name", None)
        sdc_ip = params.get("sdc_ip", None)
        sdc_id = params.get("sdc_id", None)
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockVolumeApi.SDC_RESPONSE
        )
        sdc_details = powerflex_module_mock.get_sdc_id(sdc_name, sdc_ip, sdc_id)
        assert MockVolumeApi.SDC_RESPONSE[0]["id"] == sdc_details

    def test_get_sdc_id_error(self, powerflex_module_mock):
        sdc_name = "sdc_name"
        sdc_ip = "sdc_ip"
        sdc_id = "sdc_id"
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(return_value=[])
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("get_sds"),
            powerflex_module_mock,
            powerflex_module_mock.get_sdc_id,
            sdc_name,
            sdc_ip,
            sdc_id,
        )

    def test_create_volume_error_vol_name(self, powerflex_module_mock):
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("create_vol_name"),
            powerflex_module_mock,
            powerflex_module_mock.create_volume,
            "",
            "pool_id",
            1024,
        )

    def test_create_volume_error_size(self, powerflex_module_mock):
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("create_vol_size"),
            powerflex_module_mock,
            powerflex_module_mock.create_volume,
            "vol_name",
            "pool_id",
            None,
        )

    def test_create_volume_exception(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.volume.create = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("create_vol_exc"),
            powerflex_module_mock,
            powerflex_module_mock.create_volume,
            "vol_name",
            None,
            1024,
        )

    def test_create_volume(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "size": 1024,
                "pool_id": "test_sp_id",
                "vol_name": "test_vol",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.powerflex_conn.volume.create = MagicMock(
            return_value=None
        )
        powerflex_module_mock.get_volume = MagicMock(
            side_effect=[None, MockVolumeApi.VOLUME_GET_LIST[0], MockVolumeApi.VOLUME_GET_LIST[0]]
        )
        powerflex_module_mock.perform_module_operation()

    def test_modify_access_mode_true(self, powerflex_module_mock):
        access_mode_list = [{"accessMode": "READ_ONLY", "sdc_id": "sdc_id"}]
        powerflex_module_mock.powerflex_conn.volume.set_access_mode_for_sdc = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.modify_access_mode("vol_name", access_mode_list)
        assert ret is True

    def test_modify_access_mode_false(self, powerflex_module_mock):
        access_mode_list = [{"accessMode": None, "sdc_id": "sdc_id"}]
        powerflex_module_mock.powerflex_conn.volume.set_access_mode_for_sdc = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.modify_access_mode("vol_name", access_mode_list)
        assert ret is False

    def test_modify_access_mode_exception(self, powerflex_module_mock):
        access_mode_list = [{"accessMode": "READ_ONLY", "sdc_id": "sdc_id"}]
        powerflex_module_mock.powerflex_conn.volume.set_access_mode_for_sdc = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("modify_access"),
            powerflex_module_mock,
            powerflex_module_mock.modify_access_mode,
            "vol_name",
            access_mode_list,
        )

    def test_modify_limits_true(self, powerflex_module_mock):
        payload = {"sdc_id": "sdc_id", "bandwidth_limit": 1024, "iops_limit": 1024}
        powerflex_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.modify_limits(payload)
        assert ret is True

    def test_modify_limits_false(self, powerflex_module_mock):
        payload = {"sdc_id": "sdc_id", "bandwidth_limit": None, "iops_limit": None}
        powerflex_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.modify_limits(payload)
        assert ret is False

    def test_modify_limits_exception(self, powerflex_module_mock):
        payload = {"sdc_id": "sdc_id", "bandwidth_limit": 1024, "iops_limit": 1024}
        powerflex_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("modify_limits"),
            powerflex_module_mock,
            powerflex_module_mock.modify_limits,
            payload,
        )

    def test_delete_volume_true(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.volume.delete = MagicMock(side_effect=None)
        ret = powerflex_module_mock.delete_operation("vol_id", False)
        assert ret is True

    def test_delete_volume_exception(self, powerflex_module_mock):
        powerflex_module_mock.powerflex_conn.volume.delete = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("delete_volume"),
            powerflex_module_mock,
            powerflex_module_mock.delete_volume,
            "vol_id",
            "remove_mode",
        )

    def test_unmap_volume_from_sdc_true(self, powerflex_module_mock):
        volume = {"mappedSdcInfo": [{"sdcId": "sdc_id"}], "id": "vol_id"}
        sdc = [{"sdc_name": "sdc_name"}]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id")
        powerflex_module_mock.powerflex_conn.volume.remove_mapped_host = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.unmap_volume_from_sdc(volume, sdc)
        assert ret is True

    def test_unmap_volume_from_sdc_false(self, powerflex_module_mock):
        volume = {"mappedSdcInfo": [{"sdcId": "sdc_id"}], "id": "vol_id"}
        sdc = [{"sdc_ip": "sdc_ip"}]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id1")
        powerflex_module_mock.powerflex_conn.volume.remove_mapped_host = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.unmap_volume_from_sdc(volume, sdc)
        assert ret is False

    def test_unmap_volume_from_sdc_exception(self, powerflex_module_mock):
        volume = {"mappedSdcInfo": [{"sdcId": "sdc_id"}], "id": "vol_id"}
        sdc = [{"sdc_id": "sdc_id"}]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id")
        powerflex_module_mock.powerflex_conn.volume.remove_mapped_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("unmap"),
            powerflex_module_mock,
            powerflex_module_mock.unmap_volume_from_sdc,
            volume,
            sdc,
        )

    def test_map_volume_to_sdc_name(self, powerflex_module_mock):
        volume = {
            "mappedSdcInfo": [
                {
                    "sdcId": "sdc_id",
                    "accessMode": "READ_WRITE",
                    "limitIops": 1024,
                    "limitBwInMbps": 1024,
                }
            ],
            "id": "vol_id",
        }
        sdc = [
            {
                "sdc_name": "sdc_name",
                "access_mode": "READ_ONLY",
                "iops_limit": 2048,
                "bandwidth_limit": 2048,
            }
        ]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id")
        ret, sdc_modify_list1, sdc_modify_list2 = (
            powerflex_module_mock.map_volume_to_sdc(volume, sdc)
        )
        assert ret is False
        assert sdc_modify_list1[0]["sdc_id"] == "sdc_id"
        assert sdc_modify_list2[0]["sdc_id"] == "sdc_id"

    def test_map_volume_to_sdc_ip(self, powerflex_module_mock):
        volume = {
            "mappedSdcInfo": [
                {
                    "sdcId": "sdc_id",
                    "accessMode": "READ_WRITE",
                    "limitIops": 1024,
                    "limitBwInMbps": 1024,
                }
            ],
            "id": "vol_id",
        }
        sdc = [
            {
                "sdc_ip": "sdc_ip",
                "access_mode": "READ_ONLY",
                "iops_limit": 2048,
                "bandwidth_limit": 2048,
            }
        ]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id1")
        powerflex_module_mock.powerflex_conn.volume.add_mapped_host = MagicMock(
            return_value=None
        )
        powerflex_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret, sdc_modify_list1, sdc_modify_list2 = (
            powerflex_module_mock.map_volume_to_sdc(volume, sdc)
        )
        assert ret is True
        assert sdc_modify_list1 == []
        assert sdc_modify_list2 == []

    def test_map_volume_to_sdc_id(self, powerflex_module_mock):
        volume = {
            "mappedSdcInfo": [
                {
                    "sdcId": "sdc_id",
                    "accessMode": "READ_WRITE",
                    "limitIops": 1024,
                    "limitBwInMbps": 1024,
                }
            ],
            "id": "vol_id",
        }
        sdc = [{"sdc_id": "sdc_id", "access_mode": "READ_ONLY"}]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id1")
        powerflex_module_mock.powerflex_conn.volume.add_mapped_host = MagicMock(
            return_value=None
        )
        powerflex_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret, sdc_modify_list1, sdc_modify_list2 = (
            powerflex_module_mock.map_volume_to_sdc(volume, sdc)
        )
        assert ret is True
        assert sdc_modify_list1 == []
        assert sdc_modify_list2 == []

    def test_map_volume_to_sdc_exception(self, powerflex_module_mock):
        volume = {
            "mappedSdcInfo": [
                {
                    "sdcId": "sdc_id",
                    "accessMode": "READ_WRITE",
                    "limitIops": 1024,
                    "limitBwInMbps": 1024,
                }
            ],
            "id": "vol_id",
            "name": "name",
        }
        sdc = [
            {
                "sdc_id": "sdc_id",
                "access_mode": "READ_ONLY",
                "iops_limit": 2048,
                "bandwidth_limit": 2048,
            }
        ]
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id1")
        powerflex_module_mock.powerflex_conn.volume.add_mapped_host = MagicMock(
            return_value=None
        )
        powerflex_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("map_vol_exception"),
            powerflex_module_mock,
            powerflex_module_mock.map_volume_to_sdc,
            volume,
            sdc,
        )

    @pytest.mark.parametrize(
        "params",
        [
            {
                "sdc": [
                    {"sdc_id": "sdc_id", "sdc_name": "sdc_name", "sdc_ip": "sdc_ip"}
                ],
                "assert_msg": "val_params_err1",
            },
            {"cap_unit": "GB", "size": None, "assert_msg": "val_params_err2"},
            {"asrt": "asrt", "assert_msg": "val_params_err3"},
            {
                "state": "present",
                "del_snaps": "del_snaps",
                "assert_msg": "val_params_err4",
            },
        ],
    )
    def test_validate_parameters(self, powerflex_module_mock, params):
        self.get_module_args.update(
            {
                "sdc": params.get("sdc", None),
                "cap_unit": params.get("cap_unit", None),
                "size": params.get("size", None),
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        asrt = params.get("asrt", None)
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        del_snaps = params.get("del_snaps", None)
        state = params.get("state", None)
        assert_msg = params.get("assert_msg", None)
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response(assert_msg),
            powerflex_module_mock,
            powerflex_module_mock.validate_parameters,
            asrt,
            pol_id,
            pol_name,
            del_snaps,
            state,
        )

    @pytest.mark.parametrize(
        "params",
        [
            {
                "modify_dict": {
                    "auto_snap_remove_type": "remove",
                    "snap_pol_id": "vol_id",
                    "new_name": "new_name",
                    "new_size": "new_size",
                },
                "vol_id": "vol_id",
            },
            {"modify_dict": {"snap_pol_id": "vol_id"}, "vol_id": "vol_id"},
        ],
    )
    def test_modify_volume(self, powerflex_module_mock, params):
        vol_id = params.get("vol_id", None)
        modify_dict = params.get("modify_dict", None)
        powerflex_module_mock.get_sdc_id = MagicMock(return_value="sdc_id1")
        powerflex_module_mock.powerflex_conn.snapshot_policy.remove_source_volume = (
            MagicMock(return_value=None)
        )
        powerflex_module_mock.powerflex_conn.snapshot_policy.add_source_volume = (
            MagicMock(return_value=None)
        )
        powerflex_module_mock.powerflex_conn.snapshot_policy.rename = MagicMock(
            return_value=None
        )
        powerflex_module_mock.powerflex_conn.snapshot_policy.extend = MagicMock(
            return_value=None
        )
        ret = powerflex_module_mock.modify_volume(vol_id, modify_dict)
        assert ret is True

    def test_modify_volume_execption(self, powerflex_module_mock):
        vol_id = "vol_id"
        modify_dict = {"snap_pol_id": "vol_id"}
        powerflex_module_mock.powerflex_conn.snapshot_policy.add_source_volume = (
            MagicMock(side_effect=MockApiException)
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("modify_volume_exp"),
            powerflex_module_mock,
            powerflex_module_mock.modify_volume,
            vol_id,
            modify_dict,
        )

    def test_to_modify(self, powerflex_module_mock):
        vol_details = {
            "storagePoolId": "sg_id",
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": "snplIdOfSourceVolume",
        }
        new_size = 1024
        new_name = "new_name"
        snap_pol_id = ""
        asrt = "asrt"
        powerflex_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL_FINE
        )
        modify_dict = powerflex_module_mock.to_modify(
            vol_details, new_size, new_name, snap_pol_id, asrt
        )
        assert modify_dict["snap_pol_id"] == "snplIdOfSourceVolume"

    def test_to_modify_new_name_error(self, powerflex_module_mock):
        vol_details = {
            "storagePoolId": "sg_id",
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": "snplIdOfSourceVolume",
        }
        new_size = None
        new_name = ""
        snap_pol_id = "snap_pol_id"
        asrt = None
        powerflex_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL_FINE
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("create_vol_name"),
            powerflex_module_mock,
            powerflex_module_mock.to_modify,
            vol_details,
            new_size,
            new_name,
            snap_pol_id,
            asrt,
        )

    def test_to_modify_remove_error(self, powerflex_module_mock):
        vol_details = {
            "storagePoolId": "sg_id",
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": "snplIdOfSourceVolume",
        }
        new_size = None
        new_name = None
        snap_pol_id = "snap_pol_id"
        asrt = "asrt"
        powerflex_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL_FINE
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("to_modify_err1"),
            powerflex_module_mock,
            powerflex_module_mock.to_modify,
            vol_details,
            new_size,
            new_name,
            snap_pol_id,
            asrt,
        )

    @pytest.mark.parametrize(
        "params",
        [
            {"snap_pol_id": "snap_pol_id", "assert_msg": "snap_pol_id_err"},
            {"snap_pol_name": "snap_pol_id", "assert_msg": "snap_pol_name_err"},
            {"pd_id": "pd_id", "assert_msg": "pd_id_err"},
            {"pool_id": "pool_id", "assert_msg": "pool_id_err"},
            {"pd_name": "pd_name", "assert_msg": "pd_name_err"},
            {"pool_name": "pool_name", "assert_msg": "pool_name_err"},
        ],
    )
    def test_verify_params(self, powerflex_module_mock, params):
        vol_details = {
            "snapshotPolicyId": "snapshotPolicyId",
            "snapshotPolicyName": "snapshotPolicyName",
            "protectionDomainId": "protectionDomainId",
            "storagePoolId": "storagePoolId",
            "protectionDomainName": "protectionDomainName",
            "storagePoolName": "storagePoolName",
        }
        snap_pol_name = params.get("snap_pol_name", None)
        snap_pol_id = params.get("snap_pol_id", None)
        pd_name = params.get("pd_name", None)
        pd_id = params.get("pd_id", None)
        pool_name = params.get("pool_name", None)
        pool_id = params.get("pool_id", None)
        assert_msg = params.get("assert_msg", None)
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response(assert_msg),
            powerflex_module_mock,
            powerflex_module_mock.verify_params,
            vol_details,
            snap_pol_name,
            snap_pol_id,
            pd_name,
            pd_id,
            pool_name,
            pool_id,
        )

    def test_perform_module_operation_delete(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "vol_type": "vol_type",
                "auto_snap_remove_type": "asrt",
                "size": 20,
                "protection_domain_name": "protection_domain_name",
                "storage_pool_name": "storage_pool_name",
                "snapshot_policy_name": "snapshot_policy_name",
                "vol_name": "vol_name",
                "state": "absent",
                "delete_snapshots": True,
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.validate_parameters = MagicMock(return_value=None)
        powerflex_module_mock.get_protection_domain = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        powerflex_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        powerflex_module_mock.get_snapshot_policy = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        powerflex_module_mock.get_volume = MagicMock(side_effect=[MockVolumeApi.GET_ID, {}])
        powerflex_module_mock.delete_volume = MagicMock(return_value=True)
        powerflex_module_mock.verify_params = MagicMock(return_value=None)
        powerflex_module_mock.perform_module_operation()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True
        assert (
            powerflex_module_mock.module.exit_json.call_args[1]["volume_details"] == {}
        )

    def test_perform_module_operation_create_fail(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "vol_type": "vol_type",
                "auto_snap_remove_type": "asrt",
                "size": 1,
                "protection_domain_name": "protection_domain_name",
                "storage_pool_name": "storage_pool_name",
                "snapshot_policy_name": "",
                "snapshot_policy_id": "",
                "vol_name": "vol_name",
                "state": "present",
                "cap_unit": "TB",
                "vol_new_name": "vol_new_name",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.validate_parameters = MagicMock(return_value=None)
        powerflex_module_mock.get_protection_domain = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        powerflex_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        powerflex_module_mock.get_snapshot_policy = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        powerflex_module_mock.get_volume = MagicMock(return_value=None)
        powerflex_module_mock.verify_params = MagicMock(return_value=None)
        powerflex_module_mock.create_volume = MagicMock(return_value=False)
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("perform_error1"),
            powerflex_module_mock,
            powerflex_module_mock.perform_module_operation,
        )

    def test_refresh_vol(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "refresh_src_vol_id": "test_vol_id",
                "vol_name": "vol_name",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.refresh.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_refresh_vol_exception(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "refresh_src_vol_id": "test_vol_id",
                "vol_name": "vol_name",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.volume.refresh = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("refresh_exception"),
            powerflex_module_mock,
            powerflex_module_mock.perform_module_operation,
        )

    def test_refresh_vol_with_invalid_name(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "refresh_src_vol_name": "invalid_name",
                "vol_name": "vol_name",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            side_effect=[MockVolumeApi.VOLUME_GET_LIST[0], None]
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("refresh_invalid_vol_name_exception"),
            powerflex_module_mock,
            powerflex_module_mock.perform_module_operation,
        )

    def test_restore_vol(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "restore_src_vol_id": "test_vol_id",
                "vol_name": "vol_name",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.restore.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_restore_vol_exception(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "restore_src_vol_id": "test_vol_id",
                "vol_name": "vol_name",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.powerflex_conn.volume.restore = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("restore_exception"),
            powerflex_module_mock,
            powerflex_module_mock.perform_module_operation,
        )

    def test_restore_vol_with_invalid_name(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "restore_src_vol_name": "invalid_name",
                "vol_name": "vol_name",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            side_effect=[MockVolumeApi.VOLUME_GET_LIST[0], None]
        )
        self.capture_fail_json_call(
            MockVolumeApi.get_exception_response("restore_invalid_vol_name_exception"),
            powerflex_module_mock,
            powerflex_module_mock.perform_module_operation,
        )

    def test_modify_and_map_vol(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "vol_name": "vol_name",
                "size": 1,
                "vol_new_name": "new_name",
                "auto_snap_remove_type": "detach",
                "snapshot_policy_id": "",
                "sdc": [{"sdc_id": "sdc_id", "sdc_name": None, "sdc_ip": None}],
                "sdc_state": "mapped",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.map_volume_to_sdc = MagicMock(
            return_value=(
                True,
                ["READ_WRITE"],
                [{"sdc_id": "sdc_id", "bandwidth_limit": 1, "iops_limit": 1}],
            )
        )
        powerflex_module_mock.modify_access_mode = MagicMock(return_value=True)
        powerflex_module_mock.modify_limits = MagicMock(return_value=True)
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockVolumeApi.SDC_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.extend.assert_called()
        powerflex_module_mock.powerflex_conn.volume.rename.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_refresh_unmap_vol(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "vol_name": "vol_name",
                "refresh_src_vol_name": "test_vol",
                "sdc": [{"sdc_id": "sdc_id", "sdc_name": None, "sdc_ip": None}],
                "sdc_state": "unmapped",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.unmap_volume_from_sdc = MagicMock(return_value=True)
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.refresh.assert_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_modify_and_map_vol_check_mode(self, powerflex_module_mock):
        self.get_module_args.update(
            {
                "vol_name": "vol_name",
                "size": 1,
                "vol_new_name": "new_name",
                "auto_snap_remove_type": "detach",
                "snapshot_policy_id": "",
                "sdc": [{"sdc_id": "sdc_id", "sdc_name": None, "sdc_ip": None}],
                "sdc_state": "mapped",
                "state": "present",
            }
        )
        powerflex_module_mock.module.params = self.get_module_args
        powerflex_module_mock.module.check_mode = True
        powerflex_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST[0]
        )
        powerflex_module_mock.sdc_state_mapped = MagicMock(
            return_value=(True, True, True)
        )
        powerflex_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockVolumeApi.SDC_RESPONSE
        )
        powerflex_module_mock.perform_module_operation()
        powerflex_module_mock.powerflex_conn.volume.extend.assert_not_called()
        powerflex_module_mock.powerflex_conn.volume.rename.assert_not_called()
        assert powerflex_module_mock.module.exit_json.call_args[1]["changed"] is True
