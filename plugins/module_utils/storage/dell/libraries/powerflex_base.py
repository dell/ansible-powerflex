# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('powerflex_base')


class PowerFlexBase:
    """PowerFlex Base Class"""

    def __init__(self, ansible_module_params):
        """
        Initialize the powerflex base class

        :param ansible_module_params: Parameters for ansible module class
        :type ansible_module_params: dict
        """
        params = utils.get_powerflex_gateway_host_parameters()
        ansible_module_params['argument_spec'].update(params)

        # Initialize the ansible module
        self.module = AnsibleModule(
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
