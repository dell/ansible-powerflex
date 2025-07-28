# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import re
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('powerflex_base')


class PowerFlexBase:

    '''PowerFlex Base Class'''

    def __init__(self, ansible_module, ansible_module_params):
        """
        Initialize the powerflex base class

        :param ansible_module: Ansible module class
        :type ansible_module: AnsibleModule
        :param ansible_module_params: Parameters for ansible module class
        :type ansible_module_params: dict
        """
        params = utils.get_powerflex_gateway_host_parameters()
        ansible_module_params['argument_spec'].update(params)

        # Initialize the ansible module
        self.module = ansible_module(
            **ansible_module_params
        )

        utils.ensure_required_libs(self.module)

        try:
            self.powerflex_conn = utils.get_powerflex_gateway_host_connection(
                self.module.params)
            LOG.info("Got the PowerFlex system connection object instance")
        except Exception as e:
            LOG.error(str(e))
            self.module.fail_json(msg=str(e))

    def check_module_compatibility(self):
        """ Check if the module is compatible with the PowerFlex array """
        class_name = self.__class__.__name__
        is_gen1_module = not re.match(r'.*V\d+$', class_name, re.IGNORECASE)

        api_version = self.powerflex_conn.system.api_version(cached=True)

        if is_gen1_module and utils.is_version_ge_or_eq(api_version, '5.0'):
            self.module.exit_json(changed=False, msg="Task Skipped!",
                                    warnings=["Please use v2 module for PowerFlex 5.0 and above"],)
        elif not is_gen1_module and utils.is_version_less(api_version, '5.0'):
            self.module.exit_json(
                changed=False, msg="Task Skipped!", warnings=["v2 module is only compatible with PowerFlex 5.0 and above"],)
