# Copyright: (c) 2021, Dell Technologies
# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging
import math
from decimal import Decimal
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.logging_handler \
    import CustomRotatingFileHandler

"""import PyPowerFlex lib"""
try:
    from PyPowerFlex import PowerFlexClient
    from PyPowerFlex.objects.sds import Sds
    from PyPowerFlex.objects import protection_domain
    from PyPowerFlex.objects import storage_pool
    from PyPowerFlex.objects import sdc
    from PyPowerFlex.objects import volume
    from PyPowerFlex.objects import system
    from PyPowerFlex.objects.system import SnapshotDef

    HAS_POWERFLEX_SDK = True
except ImportError:
    HAS_POWERFLEX_SDK = False

"""importing pkg_resources"""
try:
    from pkg_resources import parse_version
    import pkg_resources

    PKG_RSRC_IMPORTED = True
except ImportError:
    PKG_RSRC_IMPORTED = False

"""importing dateutil"""
try:
    import dateutil.relativedelta
    HAS_DATEUTIL = True
except ImportError:
    HAS_DATEUTIL = False

'''
This method provides common access parameters required for the ansible
modules on PowerFlex Storage System
options:
  gateway_host:
    description:
    - IP/FQDN of PowerFlex Gateway.
    required: true
  port:
    description:
    - port at which PowerFlex Gateway api is listening.
    default:
    - defaults to 443 if not specified.
    required: false
  verifycert:
    description:
    - Whether or not to verify client SSL certificate.
    required: false
  username:
    description:
    - User name to access on to PowerFlex Gateway.
    required: true
  password:
    description:
    - password to access on to PowerFlex Gateway.
    required: true
  timeout:
    description:
    - Time after which connection will get terminated.
    - It is to be mentioned in seconds.
    - defaults to 120 if not mentioned.
    required: false
'''


def get_powerflex_gateway_host_parameters():
    return dict(
        gateway_host=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        verifycert=dict(type='bool', required=False, default=True),
        port=dict(type='int', required=False, default=443),
        timeout=dict(type='int', required=False, default=120)
    )


'''
This method is to establish connection with PowerFlex storage system.
parameters:
  module_params - Ansible module parameters which contain below powerflex
                  API Gateway details to establish connection.
                - gateway_host: IP/FQDN of powerflex api gateway.
                - port:port at which powerflex api gateway api is hosted.
                - verifycert: Boolean value to inform system whether to
                  verify client certificate or not.
                - username:  User name to access on to powerflex api gateway.
                - password: Password to access powerflex api gateway.
                - timeout: Time after which connection will get terminated.
returns connection object to access powerflex api gateway host using PyPowerFlex SDK
'''


def get_powerflex_gateway_host_connection(module_params):
    if HAS_POWERFLEX_SDK:
        conn = PowerFlexClient(
            gateway_address=module_params['gateway_host'],
            gateway_port=module_params['port'],
            verify_certificate=module_params['verifycert'],
            username=module_params['username'],
            password=module_params['password'],
            timeout=module_params['timeout'])
        conn.initialize()
        return conn


'''
This method checks if supported version of PyPowerFlex SDK is installed.
'''


def pypowerflex_version_check():
    try:
        missing_packages = ""
        missing_packages_message = "Please install the required python " \
                                   "packages {0} to use this module. "

        if not HAS_DATEUTIL:
            missing_packages = 'python-dateutil, '

        if not PKG_RSRC_IMPORTED:
            missing_packages += 'pkg_resources, '

        if not HAS_POWERFLEX_SDK:
            missing_packages += 'PyPowerFlex V 1.4.0 or above'
        else:
            min_ver = '1.4.0'
            curr_version = pkg_resources.require("PyPowerFlex")[0].version
            supported_version = parse_version(curr_version) >= parse_version(
                min_ver)
            if not supported_version:
                missing_packages += 'PyPowerFlex V 1.4.0 or above'

        missing_packages_check = dict(
            dependency_present=False if missing_packages else True,
            error_message=missing_packages_message.format(
                missing_packages))

        return missing_packages_check

    except Exception as e:
        error_message = "Getting PyPowerFlex SDK version, failed with " \
                        "Error {0}".format(str(e))

        missing_packages_check = dict(
            dependency_present=False,
            error_message=error_message)
        return missing_packages_check


'''
This method is to initialize logger and return the logger object
parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: Name of file in which the log messages get appended.
     - log_devel: log level.
returns logger object
'''


def get_logger(module_name, log_file_name='ansible_powerflex.log', log_devel=logging.INFO):
    FORMAT = '%(asctime)-15s %(filename)s %(levelname)s : %(message)s'
    max_bytes = 5 * 1024 * 1024
    logging.basicConfig(filename=log_file_name, format=FORMAT)
    LOG = logging.getLogger(module_name)
    LOG.setLevel(log_devel)
    handler = CustomRotatingFileHandler(log_file_name, maxBytes=max_bytes, backupCount=5)
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    LOG.addHandler(handler)
    LOG.propagate = False
    return LOG


'''
Convert the given size to bytes
'''
KB_IN_BYTES = 1024
MB_IN_BYTES = 1024 * 1024
GB_IN_BYTES = 1024 * 1024 * 1024
TB_IN_BYTES = 1024 * 1024 * 1024 * 1024


def get_size_bytes(size, cap_units):
    if size is not None and size > 0:
        if cap_units in ('kb', 'KB'):
            return size * KB_IN_BYTES
        elif cap_units in ('mb', 'MB'):
            return size * MB_IN_BYTES
        elif cap_units in ('gb', 'GB'):
            return size * GB_IN_BYTES
        elif cap_units in ('tb', 'TB'):
            return size * TB_IN_BYTES
        else:
            return size
    else:
        return 0


'''
Convert size in byte with actual unit like KB,MB,GB,TB,PB etc.
'''


def convert_size_with_unit(size_bytes):
    if not isinstance(size_bytes, int):
        raise ValueError('This method takes Integer type argument only')
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


'''
Convert the given size to size in GB, size is restricted to 2 decimal places
'''


def get_size_in_gb(size, cap_units):
    size_in_bytes = get_size_bytes(size, cap_units)
    size = Decimal(size_in_bytes / GB_IN_BYTES)
    size_in_gb = round(size)
    return size_in_gb
