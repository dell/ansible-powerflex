# Copyright: (c) 2022, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock SDKResponse for Unit tests for Dell Technologies (Dell) PowerFlex modules"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockSDKResponse:
    def __init__(self, data=None, status_code=200):
        self.data = data
        self.status_code = status_code
