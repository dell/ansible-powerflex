# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import inspect
from pathlib import Path

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
        self.module_params = utils.get_powerflex_gateway_host_parameters()
        ansible_module_params['argument_spec'].update(self.module_params)

        # Initialize the ansible module
        self.module = ansible_module(
            **ansible_module_params
        )

        utils.ensure_required_libs(self.module)
        self.result = {"changed": False}

        try:
            self.powerflex_conn = utils.get_powerflex_gateway_host_connection(
                self.module.params)
            LOG.info("Got the PowerFlex system connection object instance")
        except Exception as e:
            LOG.error(str(e))
            self.module.fail_json(msg=str(e))

    def check_module_compatibility(self):
        """
        Check if the current module class is compatible with the target PowerFlex version.
        """

        current_class = self.__class__
        current_file = Path(inspect.getfile(current_class)).resolve()
        current_module = current_file.stem

        if not hasattr(current_class, '_powerflex_compatibility'):
            return
        compatibilities = current_class._powerflex_compatibility
        if not compatibilities:
            return

        min_ver = compatibilities.get('min_ver', None)
        max_ver = compatibilities.get('max_ver', None)
        successor = compatibilities.get('successor', None)
        predecessor = compatibilities.get('predecessor', None)

        api_version = self.powerflex_conn.system.api_version(cached=True)
        if (pfmp_version := self.get_pfmp_version()) is None:
            pfmp_version = api_version

        if min_ver and utils.is_version_less(api_version, min_ver):
            if predecessor:
                self.__skip_module(warnings=[
                    f"Please use module {predecessor} for PowerFlex {pfmp_version}"
                ])
            self.__skip_module(warnings=[
                f"Module {current_module} is not compatible with PowerFlex {pfmp_version}. "
                f"The minimum supported version of module {current_module} is {min_ver}."
            ])

        if max_ver and utils.is_version_ge_or_eq(api_version, max_ver):
            if successor:
                self.__skip_module(warnings=[
                    f"Please use module {successor} for PowerFlex {pfmp_version}"
                ])
            self.__skip_module(warnings=[
                f"Module {current_module} is not compatible with PowerFlex {pfmp_version}. "
                f"The maximum supported version of module {current_module} is below {max_ver}."
            ])

    def __skip_module(self, warnings):
        """
        Skip the module execution with a message.

        :param msg: Message to display when skipping the module
        :type msg: str
        """
        self.module.exit_json(
            changed=False,
            msg='Task Skipped!',
            warnings=warnings
        )

    def get_pfmp_version(self):
        """
        Get the PowerFlex Management Platform version.

        :return: PowerFlex Management Platform version
        :rtype: str
        """
        try:
            return self.powerflex_conn.system.pfmp_version(cached=True)
        except Exception:
            return None


def powerflex_compatibility(min_ver, max_ver=None, predecessor=None, successor=None):
    """
    Decorator to mark a module class as compatible from a specific PowerFlex version.

    Args:
        min_ver (str): Minimum PowerFlex version (inclusive) this module supports.
        max_ver (str): Optional Maximum PowerFlex version (exclusive) this module supports.
        predecessor (str): Optional predecessor module if PowerFlex version is lower than min_ver.
        successor (str): Optional successor module if PowerFlex version is higher than max_ver.
    """
    def decorator(cls):
        cls._powerflex_compatibility = {
            'min_ver': min_ver,
            'max_ver': max_ver,
            'predecessor': predecessor,
            'successor': successor
        }
        return cls
    return decorator
