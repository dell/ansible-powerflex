# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dell Technologies.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):
    # Documentation fragment for PowerFlex
    DOCUMENTATION = r'''
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
        port:
            description:
            - Port number through which communication happens with PowerFlex
             gateway host.
            type: int
            required: False
            default: 443
        timeout:
            description:
            - Time after which connection will get terminated.
            - It is to be mentioned in seconds.
            type: int
            required: False
            default: 120
    requirements:
      - A Dell PowerFlex storage system version 3.5 and later. Ansible 2.11, 2.12 or 2.13
    notes:
      - The modules present in the collection named as 'dellemc.powerflex'
        are built to support the Dell PowerFlex storage platform.
'''
