# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for volume module on PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_fault_set_api import MockFaultSetApi
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.get_powerflex_gateway_host_connection = MagicMock()
utils.PowerFlexClient = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powerflex.plugins.modules.fault_set import PowerFlexFaultSet


class TestPowerflexFaultSet():

    get_module_args = MockFaultSetApi.FAULT_SET_COMMON_ARGS

    @pytest.fixture
    def fault_set_module_mock(self, mocker):
        fault_set_module_mock = PowerFlexFaultSet()
        fault_set_module_mock.module.check_mode = False
        return fault_set_module_mock

    def test_create_fault_set(self, fault_set_module_mock):
        self.get_module_args.update({
            "fault_set_name": "test_fs_1",
            "protection_domain_name": "test_pd_1",
            "state": "present"
        })
        fault_set_module_mock.module.params = self.get_module_args
        fault_set_resp = MockFaultSetApi.FAULT_SET_GET_LIST
        fault_set_module_mock.powerflex_conn.fault_set.create = MagicMock(
            return_value=True
        )                
        fault_set_module_mock.powerflex_conn.fault_set.get = MagicMock(
            return_value=fault_set_resp
        )
        fault_set_module_mock.perform_module_operation()
        fault_set_module_mock.powerflex_conn.fault_set.get.assert_called()
