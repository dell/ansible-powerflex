# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dell EMC.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options:
  - See respective platform section for more details.
requirements:
  - See respective platform section for more details.
notes:
  - Ansible modules are available for Dell EMC PowerFlex Storage Platform.
'''

    # Documentation fragment for PowerFlex
    POWERFLEX = r'''
    options:
        gateway_host:
            required: True
            description:
            - IP or FQDN of the PowerFlex gateway host.
            type: str
        username:
            type: str
            required: True
            description:
            - The username of the PowerFlex gateway host.
        password:
            type: str
            required: True
            description:
            - The password of the PowerFlex gateway host.
        verifycert:
            type: bool
            default: True
            required: False
            description:
            - Boolean variable to specify whether or not to validate SSL
              certificate.
            - True - Indicates that the SSL certificate should be verified.
            - False - Indicates that the SSL certificate should not be
              verified.
            choices: [True, False]
        port:
            description:
            - Port number through which communication happens with PowerFlex
             gateway host.
            type: int
            required: False
            default: 443
    requirements:
      - A Dell EMC PowerFlex storage system version 3.5 and later.
      - Ansible 2.9 or later.
    notes:
      - The modules prefixed with dellemc_powerflex are built to support the
        Dell EMC PowerFlex storage platform.
'''
