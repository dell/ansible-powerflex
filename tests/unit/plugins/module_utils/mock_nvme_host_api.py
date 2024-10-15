# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of NVMe host module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockNvmeHostApi:
    MODULE_UTILS_PATH = (
        "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"
    )
    COMMON_ARGS = {
        "nqn": None,
        "max_num_paths": None,
        "max_num_sys_ports": None,
        "nvme_host_name": None,
        "nvme_host_new_name": None,
        "state": None,
    }

    @staticmethod
    def create_nvme_host():
        return {"id": "da8f60fd00010000"}

    @staticmethod
    def get_nvme_host_details():
        return [
            {
                "hostOsFullType": "Generic",
                "systemId": "f4c3b7f5c48cb00f",
                "sdcApproved": None,
                "sdcAgentActive": None,
                "mdmIpAddressesCurrent": None,
                "sdcIp": None,
                "sdcIps": None,
                "osType": None,
                "perfProfile": None,
                "peerMdmId": None,
                "sdtId": None,
                "mdmConnectionState": None,
                "softwareVersionInfo": None,
                "socketAllocationFailure": None,
                "memoryAllocationFailure": None,
                "versionInfo": None,
                "sdcType": None,
                "nqn": "test_nqn",
                "maxNumPaths": 3,
                "maxNumSysPorts": 3,
                "sdcGuid": None,
                "installedSoftwareVersionInfo": None,
                "kernelVersion": None,
                "kernelBuildNumber": None,
                "sdcApprovedIps": None,
                "hostType": "NVMeHost",
                "sdrId": None,
                "name": "nvme_host_test",
                "id": "da8f60fd00010000",
                "links": [],
            }
        ]

    @staticmethod
    def get_nvme_host_details_none_name():
        return [
            {
                "nqn": "nqn.2014-08.org.nvmexpress:uuid:79e90a42-47c9-a0f6-d9d3-51c47c72c7c1",
                "maxNumPaths": 3,
                "maxNumSysPorts": 3,
                "hostType": "NVMeHost",
                "name": None,
                "id": "da8f60fd00010000",
            }
        ]

    RESPONSE_EXEC_DICT = {
        "rename_host": "Failed to rename NVMe host",
        "modify_host": "Failed to modify NVMe host",
        "create_host": "Create NVMe host operation failed",
        "fetch_host": "Failed to get the NVMe host",
        "delete_host": "Failed to remove NVMe host",
        "id_param": "Please provide at least one of nvme_host_name or nqn",
        "param": "Please provide valid",
        "create_new_name": "nvme_host_new_name parameter is not supported during creation of a NVMe host. Try renaming the NVMe host after the creation."
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockNvmeHostApi.RESPONSE_EXEC_DICT.get(response_type, "")
