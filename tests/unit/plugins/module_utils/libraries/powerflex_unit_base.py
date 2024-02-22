# Copyright: (c) 2024, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import pytest
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries. \
    fail_json import FailJsonException, fail_json


class PowerFlexUnitBase:

    '''Powerflex Unit Test Base Class'''

    @pytest.fixture
    def powerflex_module_mock(self, mocker, module_object):
        powerflex_module_mock = module_object()
        powerflex_module_mock.module = MagicMock()
        powerflex_module_mock.module.fail_json = fail_json
        powerflex_module_mock.module.check_mode = False
        return powerflex_module_mock

    def capture_fail_json_call(self, error_msg, module_mock, module_handler=None, invoke_perform_module=False):
        try:
            if not invoke_perform_module:
                module_handler().handle(module_mock, module_mock.module.params)
            else:
                module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            if error_msg not in fj_object.message:
                raise AssertionError(fj_object.message)

    def set_module_params(self, module_mock, get_module_args, params):
        get_module_args.update(params)
        module_mock.module.params = get_module_args
