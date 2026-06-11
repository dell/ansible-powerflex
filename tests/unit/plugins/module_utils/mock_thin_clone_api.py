# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Api response for Unit tests of thin_clone module on Dell Technologies (Dell) PowerFlex
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockThinCloneApi:
    MODULE_UTILS_PATH = "ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.utils"

    THIN_CLONE_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "from_volume_name": None,
        "from_volume_id": None,
        "from_snapshot_name": None,
        "from_snapshot_id": None,
        "new_clone_name": None,
        "state": None,
    }

    SOURCE_VOLUME_ID = "src_vol_id_01"
    SOURCE_SNAPSHOT_ID = "snap_id_01"
    SYSTEM_ID = "system_id_01"
    NEW_CLONE_ID = "new_clone_id_01"

    SOURCE_VOLUME = {
        "id": "src_vol_id_01",
        "name": "src_vol",
        "volumeType": "ThickProvisioned",
        "ancestorVolumeId": "src_vol_id_01",
        "sizeInKb": 8388608,
        "storagePoolId": "sp_01",
        "mappedSdcInfo": None,
        "links": [
            {"rel": "self", "href": "/api/instances/Volume::src_vol_id_01"},
        ],
    }

    SOURCE_SNAPSHOT = {
        "id": "snap_id_01",
        "name": "snap_prod",
        "volumeType": "Snapshot",
        "ancestorVolumeId": "src_vol_id_01",
        "sizeInKb": 8388608,
        "storagePoolId": "sp_01",
        "mappedSdcInfo": None,
        "links": [
            {"rel": "self", "href": "/api/instances/Volume::snap_id_01"},
        ],
    }

    SOURCE_THIN_CLONE = {
        "id": "clone_a_id",
        "name": "clone_a",
        "volumeType": "ThinClone",
        "ancestorVolumeId": "src_vol_id_01",
        "sizeInKb": 8388608,
        "storagePoolId": "sp_01",
        "mappedSdcInfo": None,
        "links": [
            {"rel": "self", "href": "/api/instances/Volume::clone_a_id"},
        ],
    }

    CREATE_RESPONSE = {"volumeIdList": ["new_clone_id_01"]}

    NEW_CLONE_DETAILS = [
        {
            "id": "new_clone_id_01",
            "name": "clone_a",
            "volumeType": "ThinClone",
            "ancestorVolumeId": "src_vol_id_01",
            "sizeInKb": 8388608,
            "storagePoolId": "sp_01",
            "mappedSdcInfo": None,
            "links": [
                {"rel": "self", "href": "/api/instances/Volume::new_clone_id_01"},
            ],
        }
    ]

    EXISTING_CLONE_MATCHING = [
        {
            "id": "existing_clone_id",
            "name": "clone_a",
            "volumeType": "ThinClone",
            "ancestorVolumeId": "src_vol_id_01",
            "sizeInKb": 8388608,
            "storagePoolId": "sp_01",
            "mappedSdcInfo": None,
            "links": [
                {"rel": "self", "href": "/api/instances/Volume::existing_clone_id"},
            ],
        }
    ]

    EXISTING_CLONE_MISMATCHED = [
        {
            "id": "other_clone_id",
            "name": "clone_a",
            "volumeType": "ThinClone",
            "ancestorVolumeId": "different_src_id",
            "sizeInKb": 8388608,
            "storagePoolId": "sp_01",
            "mappedSdcInfo": None,
            "links": [
                {"rel": "self", "href": "/api/instances/Volume::other_clone_id"},
            ],
        }
    ]

    EXISTING_REGULAR_VOLUME = [
        {
            "id": "regular_vol_id",
            "name": "clone_a",
            "volumeType": "ThickProvisioned",
            "ancestorVolumeId": "regular_vol_id",
            "sizeInKb": 8388608,
            "storagePoolId": "sp_01",
            "mappedSdcInfo": None,
            "links": [
                {"rel": "self", "href": "/api/instances/Volume::regular_vol_id"},
            ],
        }
    ]

    SYSTEM_GET_RESPONSE = [{"id": "system_id_01"}]

    RESPONSE_EXEC_DICT = {
        "source_volume_not_found": "Source volume",
        "source_snapshot_not_found": "Source snapshot",
        "empty_clone_name": "new_clone_name is required and must be non-empty",
        "name_exists_mismatched": "already exists and is not a thin clone of the requested source",
        "name_exists_not_thin_clone": "already exists and is not a thin clone of the requested source",
        "create_sdk_exception": "Failed to create thin clone",
        "get_volume_exception": "Failed to get the volume",
        "get_system_exception": "Failed to get system id",
        "no_system_exist": "No system exist on the given host",
        "multiple_volumes": "Multiple instances",
        "reread_exception": "Failed to get the volume",
    }

    @staticmethod
    def get_exception_response(response_type):
        return MockThinCloneApi.RESPONSE_EXEC_DICT.get(response_type, "")
