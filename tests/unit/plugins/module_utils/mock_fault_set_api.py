# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock Api response for Unit tests of volume module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockFaultSetApi:
    FAULT_SET_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "protection_domain_name": None,
        "protection_domain_id": None,
        "fault_set_name": None,
        "fault_set_id": None,
        "state": None
    }

    FAULT_SET_GET_LIST = [
        {
            "protectionDomainId": "test_pd_id_1",
            "name": "test_id_1_fault_set",
            "id": "test_id_1",
            "links": []
        }
    ]

