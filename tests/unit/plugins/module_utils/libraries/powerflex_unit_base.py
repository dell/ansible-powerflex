# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
import copy

import pytest
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils
# pylint: disable=unused-import
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries import initial_mock
from mock.mock import MagicMock
from ansible_collections.dellemc.powerflex.tests.unit.plugins.module_utils.libraries. \
    fail_json import FailJsonException, fail_json


class PowerFlexUnitBase:

    '''Powerflex Unit Test Base Class'''

    @pytest.fixture(autouse=True)
    def powerflex_module_mock(self, mocker, module_object):
        utils.is_version_less = MagicMock(return_value=False)
        utils.is_version_ge_or_eq = MagicMock(return_value=False)
        self.powerflex_module_mock = module_object()
        self.powerflex_module_mock.module = MagicMock()
        self.powerflex_module_mock.module.fail_json = fail_json
        self.powerflex_module_mock.module.check_mode = False
        return self.powerflex_module_mock

    def capture_fail_json_call(self, error_msg, module_mock, module_handler=None, invoke_perform_module=False):
        try:
            if not invoke_perform_module:
                module_handler().handle(module_mock, module_mock.module.params)
            else:
                module_mock.perform_module_operation()
        except FailJsonException as fj_object:
            if error_msg not in fj_object.message:
                raise AssertionError(fj_object.message)

    def set_module_params(self, module_mock, get_module_args, params, deep_copy=True):
        if deep_copy:
            get_module_args = copy.deepcopy(get_module_args)
        get_module_args.update(params)
        if module_mock is None:
            self.powerflex_module_mock.module.params = get_module_args
        else:
            module_mock.module.params = get_module_args
