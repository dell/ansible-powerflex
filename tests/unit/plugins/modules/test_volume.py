# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for volume module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_volume_api import MockVolumeApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.volume import PowerFlexVolume


class TestPowerflexVolume():

    get_module_args = MockVolumeApi.VOLUME_COMMON_ARGS

    @pytest.fixture
    def volume_module_mock(self, mocker):
        volume_module_mock = PowerFlexVolume()
        volume_module_mock.module.check_mode = False
        return volume_module_mock

    def test_get_volume_details(self, volume_module_mock):
        self.get_module_args.update({
            "vol_name": "testing",
            "state": "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_resp = MockVolumeApi.VOLUME_GET_LIST
        volume_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_sp_resp = MockVolumeApi.VOLUME_STORAGEPOOL_DETAILS
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=volume_sp_resp
        )
        volume_pd_resp = MockVolumeApi.VOLUME_PD_DETAILS
        volume_module_mock.get_protection_domain = MagicMock(
            return_value=volume_pd_resp
        )
        volume_statistics_resp = MockVolumeApi.VOLUME_STATISTICS
        volume_module_mock.powerflex_conn.volume.get_statistics = MagicMock(
            return_value=volume_statistics_resp
        )
        volume_module_mock.perform_module_operation()
        volume_module_mock.powerflex_conn.volume.get.assert_called()
        volume_module_mock.powerflex_conn.volume.get_statistics.assert_called()

    def test_get_volume_details_with_exception(self, volume_module_mock):
        self.get_module_args.update({
            "vol_name": "testing",
            "state": "present"
        })
        volume_module_mock.module.params = self.get_module_args
        volume_resp = MockVolumeApi.VOLUME_GET_LIST
        volume_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=volume_resp
        )
        volume_module_mock.powerflex_conn.volume.get_statistics = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.create_volume = MagicMock(return_value=None)
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.get_exception_response(
            'get_details') in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize("params", [
        {"pd_id": "123"},
        {"pd_name": "test"},
    ])
    def test_get_protection_domain(self, volume_module_mock, params):
        pd_id = params.get("pd_id", None)
        pd_name = params.get("pd_name", None)
        volume_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=MockVolumeApi.PROTECTION_DETAILS
        )
        pd_details = volume_module_mock.get_protection_domain(pd_name, pd_id)
        assert MockVolumeApi.PROTECTION_DETAILS[0] == pd_details

    def test_get_protection_domain_exeception(self, volume_module_mock):
        pd_id = "pd_id"
        pd_name = "pd_name"
        volume_module_mock.powerflex_conn.protection_domain.get = MagicMock(
            return_value=None
        )
        volume_module_mock.get_protection_domain(pd_name, pd_id)
        assert MockVolumeApi.get_exception_response(
            'get_pd_exception') in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize("params", [
        {"pol_id": "123"},
        {"pol_name": "test"},
    ])
    def test_get_snapshot_policy(self, volume_module_mock, params):
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        volume_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=MockVolumeApi.PROTECTION_DETAILS
        )
        snap_pol_details = volume_module_mock.get_snapshot_policy(
            pol_id, pol_name)
        assert MockVolumeApi.PROTECTION_DETAILS[0] == snap_pol_details

    def test_get_snapshot_policy_exception(self, volume_module_mock):
        pol_id = "pol_id"
        pol_name = "pol_name"
        volume_module_mock.powerflex_conn.snapshot_policy.get = MagicMock(
            return_value=None
        )
        volume_module_mock.get_snapshot_policy(pol_id, pol_name)
        assert MockVolumeApi.get_exception_response(
            'get_sp_exception') in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize("params", [
        {"pol_id": "123", "prot_id": "123"},
    ])
    def test_get_storage_pool(self, volume_module_mock, params):
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        prot_id = params.get("prot_id", None)

        def mock_get(filter_fields):
            if filter_fields.get("protectionDomainId", None):
                return MockVolumeApi.PROTECTION_DETAILS
            else:
                return MockVolumeApi.PROTECTION_DETAILS_MULTI

        volume_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            side_effect=mock_get
        )
        sp_details = volume_module_mock.get_storage_pool(
            pol_id, pol_name, prot_id)
        assert MockVolumeApi.PROTECTION_DETAILS[0] == sp_details

    @pytest.mark.parametrize("params", [
        {"pol_id": "123", "assert_msg": "get_spool_error1"},
        {"pol_name": "123", "prot_id": "123", "assert_msg": "get_spool_error2"},
    ])
    def test_get_storage_pool_error(self, volume_module_mock, params):
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        prot_id = params.get("prot_id", None)

        def mock_get(filter_fields):
            if filter_fields.get("protectionDomainId", None):
                return None
            else:
                return MockVolumeApi.PROTECTION_DETAILS_MULTI

        volume_module_mock.powerflex_conn.storage_pool.get = MagicMock(
            side_effect=mock_get
        )
        volume_module_mock.get_storage_pool(pol_id, pol_name, prot_id)
        assert MockVolumeApi.get_exception_response(params.get(
            "assert_msg")) in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize("params", [
        {"vol_name": "123", "assert_msg": "get_spool_error1"}
    ])
    def test_get_volume(self, volume_module_mock, params):
        vol_name = params.get("vol_name", None)
        vol_id = params.get("vol_id", None)
        volume_module_mock.powerflex_conn.volume.get = MagicMock(
            return_value=MockVolumeApi.VOLUME_GET_LIST
        )
        volume_module_mock.get_snapshot_policy = MagicMock(
            return_value={"name": "snapshotPolicyName"}
        )
        volume_details = volume_module_mock.get_volume(vol_name, vol_id)
        assert volume_details["snapshotPolicyId"] == MockVolumeApi.VOLUME_GET_LIST[0]["snapshotPolicyId"]
        assert volume_details["snapshotPolicyName"] == MockVolumeApi.VOLUME_GET_LIST[0]["snapshotPolicyName"]

    def test_get_volume_exeception(self, volume_module_mock):
        volume_module_mock.powerflex_conn.volume.get = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.get_snapshot_policy = MagicMock(
            return_value={"name": "snapshotPolicyName"}
        )
        volume_module_mock.get_volume("test_id_1", "test_id_1")
        assert MockVolumeApi.get_exception_response(
            "get_details") in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize("params", [
        {"sdc_id": "sdc_id"},
        {"sdc_ip": "sdc_ip"},
    ])
    def test_get_sdc_id(self, volume_module_mock, params):
        sdc_name = params.get("sdc_name", None)
        sdc_ip = params.get("sdc_ip", None)
        sdc_id = params.get("sdc_id", None)
        volume_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=MockVolumeApi.SDC_RESPONSE
        )
        sdc_details = volume_module_mock.get_sdc_id(sdc_name, sdc_ip, sdc_id)
        assert MockVolumeApi.SDC_RESPONSE[0]['id'] == sdc_details

    def test_get_sdc_id_error(self, volume_module_mock):
        sdc_name = "sdc_name"
        sdc_ip = "sdc_ip"
        sdc_id = "sdc_id"
        volume_module_mock.powerflex_conn.sdc.get = MagicMock(
            return_value=[]
        )
        volume_module_mock.get_sdc_id(sdc_name, sdc_ip, sdc_id)
        assert MockVolumeApi.get_exception_response(
            "get_sds") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume_error_vol_name(self, volume_module_mock):
        volume_module_mock.create_volume("", "pool_id", 1024)
        assert MockVolumeApi.get_exception_response(
            "create_vol_name") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume_error_comp_type(self, volume_module_mock):
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL
        )
        volume_module_mock.create_volume(
            "vol_name", "pool_id", 1024, comp_type="comp_type")
        assert MockVolumeApi.get_exception_response(
            "create_vol_ctype") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume_error_size(self, volume_module_mock):
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL
        )
        volume_module_mock.create_volume("vol_name", "pool_id", None)
        assert MockVolumeApi.get_exception_response(
            "create_vol_size") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume_exception(self, volume_module_mock):
        volume_module_mock.powerflex_conn.volume.create = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.create_volume("vol_name", None, 1024)
        assert MockVolumeApi.get_exception_response(
            "create_vol_exc") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_volume(self, volume_module_mock):
        volume_module_mock.powerflex_conn.volume.create = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.create_volume("vol_name", None, 1024)
        assert ret is True

    def test_modify_access_mode_true(self, volume_module_mock):
        access_mode_list = [{"accessMode": "READ_ONLY", "sdc_id": "sdc_id"}]
        volume_module_mock.powerflex_conn.volume.set_access_mode_for_sdc = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.modify_access_mode(
            "vol_name", access_mode_list)
        assert ret is True

    def test_modify_access_mode_false(self, volume_module_mock):
        access_mode_list = [{"accessMode": None, "sdc_id": "sdc_id"}]
        volume_module_mock.powerflex_conn.volume.set_access_mode_for_sdc = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.modify_access_mode(
            "vol_name", access_mode_list)
        assert ret is False

    def test_modify_access_mode_exception(self, volume_module_mock):
        access_mode_list = [{"accessMode": "READ_ONLY", "sdc_id": "sdc_id"}]
        volume_module_mock.powerflex_conn.volume.set_access_mode_for_sdc = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.modify_access_mode("vol_name", access_mode_list)
        assert MockVolumeApi.get_exception_response(
            "modify_access") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_limits_true(self, volume_module_mock):
        payload = {"sdc_id": "sdc_id",
                   "bandwidth_limit": 1024, "iops_limit": 1024}
        volume_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.modify_limits(payload)
        assert ret is True

    def test_modify_limits_false(self, volume_module_mock):
        payload = {"sdc_id": "sdc_id",
                   "bandwidth_limit": None, "iops_limit": None}
        volume_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.modify_limits(payload)
        assert ret is False

    def test_modify_limits_exception(self, volume_module_mock):
        payload = {"sdc_id": "sdc_id",
                   "bandwidth_limit": 1024, "iops_limit": 1024}
        volume_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.modify_limits(payload)
        assert MockVolumeApi.get_exception_response(
            "modify_limits") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_volume_true(self, volume_module_mock):
        volume_module_mock.powerflex_conn.volume.delete = MagicMock(
            side_effect=None
        )
        ret = volume_module_mock.delete_volume("vol_id", "remove_mode")
        assert ret is True

    def test_delete_volume_exception(self, volume_module_mock):
        volume_module_mock.powerflex_conn.volume.delete = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.delete_volume("vol_id", "remove_mode")
        assert MockVolumeApi.get_exception_response(
            "delete_volume") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_unmap_volume_from_sdc_true(self, volume_module_mock):
        volume = {"mappedSdcInfo": [{"sdcId": "sdc_id"}], "id": "vol_id"}
        sdc = [{"sdc_name": "sdc_name"}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id"
        )
        volume_module_mock.powerflex_conn.volume.remove_mapped_sdc = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.unmap_volume_from_sdc(volume, sdc)
        assert ret is True

    def test_unmap_volume_from_sdc_false(self, volume_module_mock):
        volume = {"mappedSdcInfo": [{"sdcId": "sdc_id"}], "id": "vol_id"}
        sdc = [{"sdc_ip": "sdc_ip"}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id1"
        )
        volume_module_mock.powerflex_conn.volume.remove_mapped_sdc = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.unmap_volume_from_sdc(volume, sdc)
        assert ret is False

    def test_unmap_volume_from_sdc_exception(self, volume_module_mock):
        volume = {"mappedSdcInfo": [{"sdcId": "sdc_id"}], "id": "vol_id"}
        sdc = [{"sdc_id": "sdc_id"}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id"
        )
        volume_module_mock.powerflex_conn.volume.remove_mapped_sdc = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.unmap_volume_from_sdc(volume, sdc)
        assert MockVolumeApi.get_exception_response(
            "unmap") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_map_volume_to_sdc_name(self, volume_module_mock):
        volume = {
            "mappedSdcInfo": [
                {"sdcId": "sdc_id", "accessMode": "READ_WRITE",
                 "limitIops": 1024, "limitBwInMbps": 1024}],
            "id": "vol_id",
        }
        sdc = [{"sdc_name": "sdc_name", "access_mode": "READ_ONLY",
                "iops_limit": 2048, "bandwidth_limit": 2048}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id"
        )
        ret, sdc_modify_list1, sdc_modify_list2 = volume_module_mock.map_volume_to_sdc(
            volume, sdc)
        assert ret is False
        assert sdc_modify_list1[0]["sdc_id"] == "sdc_id"
        assert sdc_modify_list2[0]["sdc_id"] == "sdc_id"

    def test_map_volume_to_sdc_ip(self, volume_module_mock):
        volume = {
            "mappedSdcInfo": [
                {"sdcId": "sdc_id", "accessMode": "READ_WRITE",
                 "limitIops": 1024, "limitBwInMbps": 1024}],
            "id": "vol_id",
        }
        sdc = [{"sdc_ip": "sdc_ip", "access_mode": "READ_ONLY",
                "iops_limit": 2048, "bandwidth_limit": 2048}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id1"
        )
        volume_module_mock.powerflex_conn.volume.add_mapped_sdc = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret, sdc_modify_list1, sdc_modify_list2 = volume_module_mock.map_volume_to_sdc(
            volume, sdc)
        assert ret is True
        assert sdc_modify_list1 == []
        assert sdc_modify_list2 == []

    def test_map_volume_to_sdc_id(self, volume_module_mock):
        volume = {
            "mappedSdcInfo": [
                {"sdcId": "sdc_id", "accessMode": "READ_WRITE",
                 "limitIops": 1024, "limitBwInMbps": 1024}],
            "id": "vol_id",
        }
        sdc = [{"sdc_id": "sdc_id", "access_mode": "READ_ONLY"}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id1"
        )
        volume_module_mock.powerflex_conn.volume.add_mapped_sdc = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            return_value=None
        )
        ret, sdc_modify_list1, sdc_modify_list2 = volume_module_mock.map_volume_to_sdc(
            volume, sdc)
        assert ret is True
        assert sdc_modify_list1 == []
        assert sdc_modify_list2 == []

    def test_map_volume_to_sdc_exception(self, volume_module_mock):
        volume = {
            "mappedSdcInfo": [
                {"sdcId": "sdc_id", "accessMode": "READ_WRITE",
                 "limitIops": 1024, "limitBwInMbps": 1024}],
            "id": "vol_id",
            "name": "name"
        }
        sdc = [{"sdc_id": "sdc_id", "access_mode": "READ_ONLY",
                "iops_limit": 2048, "bandwidth_limit": 2048}]
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id1"
        )
        volume_module_mock.powerflex_conn.volume.add_mapped_sdc = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.volume.set_mapped_sdc_limits = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.map_volume_to_sdc(volume, sdc)
        assert MockVolumeApi.get_exception_response(
            "map_vol_exception") in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize('params', [
        {"sdc": [{"sdc_id": "sdc_id", "sdc_name": "sdc_name", "sdc_ip": "sdc_ip"}],
         "assert_msg": "val_params_err1"},
        {"cap_unit": "GB", "size": None, "assert_msg": "val_params_err2"},
        {"asrt": "asrt", "assert_msg": "val_params_err3"},
        {"state": "present", "del_snaps": "del_snaps",
            "assert_msg": "val_params_err4"},
    ])
    def test_validate_parameters(self, volume_module_mock, params):
        self.get_module_args.update({
            "sdc": params.get("sdc", None),
            "cap_unit": params.get("cap_unit", None),
            "size": params.get("size", None),
        })
        volume_module_mock.module.params = self.get_module_args
        asrt = params.get("asrt", None)
        pol_id = params.get("pol_id", None)
        pol_name = params.get("pol_name", None)
        del_snaps = params.get("del_snaps", None)
        state = params.get("state", None)
        assert_msg = params.get("assert_msg", None)
        volume_module_mock.validate_parameters(
            asrt, pol_id, pol_name, del_snaps, state)
        assert MockVolumeApi.get_exception_response(
            assert_msg) in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize('params', [
        {"modify_dict": {
            "auto_snap_remove_type": "remove",
            "snap_pol_id": "vol_id",
            "new_name": "new_name",
            "new_size": "new_size",
            "use_rmcache": "use_rmcache",
            "comp_type": "comp_type"
        }, "vol_id": "vol_id"},
        {"modify_dict": {
            "snap_pol_id": "vol_id"
        }, "vol_id": "vol_id"},
    ])
    def test_modify_volume(self, volume_module_mock, params):
        vol_id = params.get("vol_id", None)
        modify_dict = params.get("modify_dict", None)
        volume_module_mock.get_sdc_id = MagicMock(
            return_value="sdc_id1"
        )
        volume_module_mock.powerflex_conn.snapshot_policy.remove_source_volume = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.snapshot_policy.add_source_volume = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.snapshot_policy.rename = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.snapshot_policy.extend = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.snapshot_policy.set_use_rmcache = MagicMock(
            return_value=None
        )
        volume_module_mock.powerflex_conn.snapshot_policy.set_compression_method = MagicMock(
            return_value=None
        )
        ret = volume_module_mock.modify_volume(vol_id, modify_dict)
        assert ret is True

    def test_modify_volume_execption(self, volume_module_mock):
        vol_id = "vol_id"
        modify_dict = {"snap_pol_id": "vol_id"}
        volume_module_mock.powerflex_conn.snapshot_policy.add_source_volume = MagicMock(
            side_effect=MockApiException
        )
        volume_module_mock.modify_volume(vol_id, modify_dict)
        assert MockVolumeApi.get_exception_response(
            "modify_volume_exp") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_to_modify(self, volume_module_mock):
        vol_details = {
            "storagePoolId": "sdc_id",
            "compressionMethod": "tar",
            "useRmcache": True,
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": "snplIdOfSourceVolume"
        }
        new_size = 1024
        use_rmcache = False
        comp_type = "zip"
        new_name = "new_name"
        snap_pol_id = ""
        asrt = "asrt"
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL_FINE
        )
        modify_dict = volume_module_mock.to_modify(vol_details, new_size, use_rmcache, comp_type,
                                                   new_name, snap_pol_id,
                                                   asrt)
        assert modify_dict["snap_pol_id"] == "snplIdOfSourceVolume"

    def test_to_modify_comp_type_error(self, volume_module_mock):
        vol_details = {
            "storagePoolId": "sdc_id",
            "compressionMethod": "tar",
            "useRmcache": True,
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": None
        }
        new_size = 1024
        use_rmcache = False
        comp_type = "zip"
        new_name = "new_name"
        snap_pol_id = "snap_pol_id"
        asrt = None
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL
        )
        volume_module_mock.to_modify(vol_details, new_size, use_rmcache, comp_type,
                                     new_name, snap_pol_id,
                                     asrt)
        assert MockVolumeApi.get_exception_response(
            "create_vol_ctype") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_to_modify_new_name_error(self, volume_module_mock):
        vol_details = {
            "storagePoolId": "sdc_id",
            "compressionMethod": "tar",
            "useRmcache": True,
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": "snplIdOfSourceVolume"
        }
        new_size = None
        use_rmcache = None
        comp_type = None
        new_name = ""
        snap_pol_id = "snap_pol_id"
        asrt = None
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL_FINE
        )
        volume_module_mock.to_modify(vol_details, new_size, use_rmcache, comp_type,
                                     new_name, snap_pol_id,
                                     asrt)
        assert MockVolumeApi.get_exception_response(
            "create_vol_name") in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_to_modify_remove_error(self, volume_module_mock):
        vol_details = {
            "storagePoolId": "sdc_id",
            "compressionMethod": "tar",
            "useRmcache": True,
            "sizeInKb": 2048,
            "name": "name",
            "snplIdOfSourceVolume": "snplIdOfSourceVolume"
        }
        new_size = None
        use_rmcache = None
        comp_type = None
        new_name = None
        snap_pol_id = "snap_pol_id"
        asrt = "asrt"
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_STORAGE_POOL_FINE
        )
        volume_module_mock.to_modify(vol_details, new_size, use_rmcache, comp_type,
                                     new_name, snap_pol_id,
                                     asrt)
        assert MockVolumeApi.get_exception_response(
            "to_modify_err1") in volume_module_mock.module.fail_json.call_args[1]['msg']

    @pytest.mark.parametrize('params', [
        {"snap_pol_id": "snap_pol_id", "assert_msg": "snap_pol_id_err"},
        {"snap_pol_name": "snap_pol_id", "assert_msg": "snap_pol_name_err"},
        {"pd_id": "pd_id", "assert_msg": "pd_id_err"},
        {"pool_id": "pool_id", "assert_msg": "pool_id_err"},
        {"pd_name": "pd_name", "assert_msg": "pd_name_err"},
        {"pool_name": "pool_name", "assert_msg": "pool_name_err"}
    ])
    def test_verify_params(self, volume_module_mock, params):
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
        volume_module_mock.verify_params(vol_details, snap_pol_name, snap_pol_id, pd_name,
                                         pd_id, pool_name, pool_id)
        assert MockVolumeApi.get_exception_response(
            assert_msg) in volume_module_mock.module.fail_json.call_args[1]['msg']

    def test_perform_module_operation_delete(self, volume_module_mock):
        self.get_module_args.update({
            "compression_type": "tar",
            "vol_type": "vol_type",
            "auto_snap_remove_type": "asrt",
            "size": 20,
            "protection_domain_name": "protection_domain_name",
            "storage_pool_name": "storage_pool_name",
            "snapshot_policy_name": "snapshot_policy_name",
            "vol_name": "vol_name",
            "state": "absent",
            "delete_snapshots": True
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.validate_parameters = MagicMock(
            return_value=None
        )
        volume_module_mock.get_protection_domain = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.get_snapshot_policy = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.get_volume = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.delete_volume = MagicMock(
            return_value=True
        )
        volume_module_mock.verify_params = MagicMock(
            return_value=None
        )
        volume_module_mock.perform_module_operation()
        assert volume_module_mock.module.exit_json.call_args[1]['changed'] is True
        assert volume_module_mock.module.exit_json.call_args[1]['volume_details'] == {
        }

    def test_perform_module_operation_create_fail(self, volume_module_mock):
        self.get_module_args.update({
            "compression_type": "tar",
            "vol_type": "vol_type",
            "auto_snap_remove_type": "asrt",
            "size": 1,
            "protection_domain_name": "protection_domain_name",
            "storage_pool_name": "storage_pool_name",
            "snapshot_policy_name": "",
            "snapshot_policy_id": "",
            "vol_name": "vol_name",
            "state": "present",
            "delete_snapshots": True,
            "cap_unit": "TB",
            "vol_id": "vol_id",
            "vol_new_name": "vol_new_name",
        })
        volume_module_mock.module.params = self.get_module_args
        volume_module_mock.validate_parameters = MagicMock(
            return_value=None
        )
        volume_module_mock.get_protection_domain = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.get_storage_pool = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.get_snapshot_policy = MagicMock(
            return_value=MockVolumeApi.GET_ID
        )
        volume_module_mock.get_volume = MagicMock(
            return_value=None
        )
        volume_module_mock.verify_params = MagicMock(
            return_value=None
        )
        volume_module_mock.create_volume = MagicMock(
            return_value=False
        )
        volume_module_mock.perform_module_operation()
        assert MockVolumeApi.get_exception_response(
            "perform_error1") in volume_module_mock.module.fail_json.call_args[1]['msg']
