# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock ApiException for Dell Technologies (Dell) PowerFlex Test modules"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockResourceResourceGroupAPI:

    RG_COMMON_ARGS = {
        "hostname": "**.***.**.***",
        "username": "username",
        "password": "password",
        "validate_certs": False,
        "port": "443",
        "validate": False,
        "template_name": None,
        "template_id": None,
        "firmware_repository_name": None,
        "firmware_repository_id": None,
        "resource_group_name": None,
        "resource_group_id": None,
        "schedule_date": None
    }

    RG_RESPONSE = [{
        "id": "8aaa03a88de961fa018de96a88d80008",
        "deploymentName": "ans_rg",
        "deploymentDescription": "ans test rg",
        "retry": True,
        "teardown": False,
        "serviceTemplate": {
            "id": "8aaa03a88de961fa018de96a88d80008",
            "templateName": "update-template (8aaa03a88de961fa018de96a88d80008)",
            "components": [
                {
                    "id": "a7dafed9-96f2-4a55-9518-57af4f45686e",
                    "componentID": "component-scaleio-gateway-1",
                    "identifier": None,
                    "componentValid": {
                        "valid": True,
                        "messages": []
                    },
                    "puppetCertName": "scaleio-block-legacy-gateway",
                    "osPuppetCertName": None,
                    "name": "block-legacy-gateway",
                    "type": "SERVER",
                    "subType": "COMPUTEONLY",
                    "teardown": False,
                    "helpText": None,
                    "managementIpAddress": None,
                    "configFile": None,
                    "serialNumber": None,
                    "asmGUID": "scaleio-block-legacy-gateway",
                    "relatedComponents": {
                        "fc0f8f08-18c7-4fa8-bae8-67f3e6f9ccd6": "Node (Software Only)"
                    },
                    "resources": [{
                        "id": "asm::server",
                        "parameters": [{
                            "id": "a7dafed9",
                            "guid": None,
                            "value": None}]}],
                    "refId": None,
                    "cloned": False,
                    "clonedFromId": None,
                    "manageFirmware": False,
                    "brownfield": False,
                    "instances": 1,
                    "clonedFromAsmGuid": None,
                    "ip": None
                }]
        },
        "scheduleDate": None,
        "status": "error",
        "compliant": True,
        "deploymentDevice": [{
            "refId": "scaleio-block-legacy-gateway",
            "refType": "SCALEIO",
            "deviceHealth": "GREEN",
            "compliantState": "COMPLIANT",
            "deviceType": "scaleio",
            "currentIpAddress": "1.3.9.2",
            "componentId": "910bf934-d45a-4fe3-8ea2-dc481e063a81",
            "statusMessage": "The processing of PowerFlex is unsuccessful.",
            "model": "PowerFlex Gateway",
            "brownfield": False}],
        "updateServerFirmware": True,
        "useDefaultCatalog": True,
        "firmwareRepository": {
            "id": "8aaa80788b5755d1018b576126d51ba3",
            "name": "PowerFlex 4.5.0.0",
            "rcmapproved": False},
        "firmwareRepositoryId": "8aaa80788b5755d1018b576126d51ba3",
        "deploymentHealthStatusType": "red",
        "allUsersAllowed": False,
        "owner": "admin",
        "numberOfDeployments": 0,
        "lifecycleMode": False,
        "vds": False,
        "scaleUp": False,
        "brownfield": False,
        "templateValid": True,
        "configurationChange": False}]

    RG_FIRMWARE_REPO = [{
        "id": "8aaa80788b5755d1018b576126d51ba3",
        "name": "firmware-name",
        "sourceLocation": "https://100.65.27.72/artifactory/path/pfxmlogs-bvt-pfmp-swo-upgrade-402-to-451-56.tar.gz",
        "sourceType": None,
        "diskLocation": "",
        "filename": "",
        "md5Hash": None,
        "username": "",
        "password": "",
        "downloadStatus": "error",
        "createdDate": "2024-02-26T17:07:11.884+00:00",
        "createdBy": "admin",
        "updatedDate": "2024-03-01T06:21:10.917+00:00",
        "updatedBy": "system",
        "defaultCatalog": False,
        "embedded": False,
        "state": "errors",
        "softwareComponents": [],
        "softwareBundles": [],
        "deployments": [],
        "bundleCount": 0,
        "componentCount": 0,
        "userBundleCount": 0,
        "minimal": True,
        "downloadProgress": 100,
        "extractProgress": 0,
        "fileSizeInGigabytes": 0.0,
        "signedKeySourceLocation": None,
        "signature": "Unknown",
        "custom": False,
        "needsAttention": False,
        "jobId": "Job-10d75a23-d801-4fdb-a2d0-7f6389ab75cf",
        "rcmapproved": False
    }]

    RG_TEMPLATE_RESPONSE = [{
        "id": "8aaa03a88de961fa018de96a88d80008",
        "templateName": "update-template"
    }]

    @staticmethod
    def resource_group_error(response_type):
        return {
            "get_delete_deploy_exception": "Deleting a resource group deployment failed with error ",
            "get_validate_deploy_exception": "Validating a resource group deployment failed with error",
            "get_create_deploy_exception": "Deploying a resource group failed with error",
            "get_template_validate_error": "Deploying a resource group failed with error Either template_id",
            "get_template_error": "Service template new-template is not found",
            "invalid_date_format": "Deploying a resource group failed with error Invalid schedule_date format",
            "resource_group_name_error": "Specify resource_group_name for resource group deployment",
            "resource_group_edit_error": "Editing a resource group failed with error",
        }[response_type]
