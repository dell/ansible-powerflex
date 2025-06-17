.. _resource_group_module:


resource_group -- Manage resource group deployments on Dell PowerFlex.
======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing resource group deployments on PowerFlex storage system includes deploying, editing, adding nodes and deleting a resource group deployment.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.6 or later.
- PyPowerFlex 1.14.1.



Parameters
----------

  resource_group_name (optional, str, None)
    The name of the resource group.

    This is a required field to deploy a resource group.

    Either \ :emphasis:`resource\_group\_id`\  or \ :emphasis:`resource\_group\_name`\  must be specified to perform resource group operations.

    Mutually exclusive with \ :emphasis:`resource\_group\_id`\ .


  resource_group_id (optional, str, None)
    The ID of the resource group.

    Either \ :emphasis:`resource\_group\_id`\  or \ :emphasis:`resource\_group\_name`\  must be specified to perform resource group operations.

    Mutually exclusive with \ :emphasis:`resource\_group\_name`\ .


  template_name (optional, str, None)
    The name of the published template.

    Either \ :emphasis:`template\_id`\  or \ :emphasis:`template\_name`\  must be specified to deploy a resource group.

    Mutually exclusive with \ :emphasis:`template\_id`\ .


  template_id (optional, str, None)
    The ID of the published template.

    Either \ :emphasis:`template\_id`\  or \ :emphasis:`template\_name`\  must be specified to deploy a resource group.

    Mutually exclusive with \ :emphasis:`template\_name`\ .


  firmware_repository_id (optional, str, None)
    The ID of the firmware repository if not using the appliance default catalog.

    Mutually exclusive with \ :emphasis:`firmware\_repository\_name`\ .


  firmware_repository_name (optional, str, None)
    The name of the firmware repository if not using the appliance default catalog.

    Mutually exclusive with \ :emphasis:`firmware\_repository\_id`\ .


  new_resource_group_name (optional, str, None)
    New name of the resource group to rename to.


  description (optional, str, None)
    The description of the resource group.


  scaleup (optional, bool, False)
    Whether to scale up the resource group. Specify as true to add nodes to the resource group.


  clone_node (optional, str, None)
    Resource to duplicate during scaleup, if more than one nodes are available in the resource group.


  node_count (optional, int, 1)
    Number of nodes to clone during scaleup.


  validate (optional, bool, False)
    Specify as true to validate the deployment of resource group.


  schedule_date (optional, str, None)
    Scheduled date for the resource group deployment.

    Specify in YYYY-MM-DD HH:MM:SS.sss or YYYY-MM-DD format.


  state (optional, str, present)
    The state of the resource group.


  hostname (True, str, None)
    IP or FQDN of the PowerFlex host.


  username (True, str, None)
    The username of the PowerFlex host.


  password (True, str, None)
    The password of the PowerFlex host.


  validate_certs (optional, bool, True)
    Boolean variable to specify whether or not to validate SSL certificate.

    \ :literal:`true`\  - Indicates that the SSL certificate should be verified.

    \ :literal:`false`\  - Indicates that the SSL certificate should not be verified.


  port (optional, int, 443)
    Port number through which communication happens with PowerFlex host.


  timeout (False, int, 120)
    Time after which connection will get terminated.

    It is to be mentioned in seconds.





Notes
-----

.. note::
   - The \ :emphasis:`check\_mode`\  is supported.
   - Resource group scale up can be done only when deployment is complete.
   - The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell PowerFlex storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Validate deployment of a resource group
      dellemc.powerflex.resource_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        port: "{{ port }}"
        resource_group_name: "{{ resource_group_name_1 }}"
        description: ans_rg
        template_id: c65d0172-8666-48ab-935e-9a0bf69ed66d
        firmware_repository_id: 8aaa80788b5755d1018b576126d51ba3
        validate: true

    - name: Deploy a resource group
      dellemc.powerflex.resource_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        port: "{{ port }}"
        resource_group_name: "{{ resource_group_name_1 }}"
        description: ans_rg
        template_id: c65d0172-8666-48ab-935e-9a0bf69ed66d
        firmware_repository_id: 8aaa80788b5755d1018b576126d51ba3

    - name: Add a node to a resource group
      dellemc.powerflex.resource_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        resource_group_name: "{{ resource_group_name_1 }}"
        scaleup: true
        clone_node: "{{ node_1 }}"
        node_count: "{{ node_count }}"

    - name: Modify a resource group
      dellemc.powerflex.resource_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        resource_group_name: "{{ resource_group_name_1 }}"
        new_resource_group_name: "{{ new_resource_group_name }}"
        description: "description new"

    - name: Delete a resource group
      dellemc.powerflex.resource_group:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: "{{ validate_certs }}"
        port: "{{ port }}"
        resource_group_name: ans_rg
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


resource_group_details (When resource group exists., dict, {'id': '8aaa03a88de961fa018de96a88d80008', 'deploymentName': 'dep-ans-test-rg1', 'deploymentDescription': 'ans test rg', 'retry': True, 'teardown': False, 'serviceTemplate': {'id': '8aaa03a88de961fa018de96a88d80008', 'templateName': 'update-template (8aaa03a88de961fa018de96a88d80008)'}, 'scheduleDate': None, 'status': 'error', 'compliant': True, 'deploymentDevice': [{'refId': 'scaleio-block-legacy-gateway', 'refType': 'SCALEIO', 'deviceHealth': 'GREEN', 'compliantState': 'COMPLIANT', 'deviceType': 'scaleio', 'currentIpAddress': '1.3.9.2', 'componentId': '910bf934-d45a-4fe3-8ea2-dc481e063a81', 'statusMessage': 'The processing of PowerFlex is unsuccessful.', 'model': 'PowerFlex Gateway', 'brownfield': False}], 'updateServerFirmware': True, 'useDefaultCatalog': True, 'firmwareRepository': {'id': '8aaa80788b5755d1018b576126d51ba3', 'name': 'PowerFlex 4.5.0.0', 'rcmapproved': False}, 'firmwareRepositoryId': '8aaa80788b5755d1018b576126d51ba3', 'deploymentHealthStatusType': 'red', 'allUsersAllowed': False, 'owner': 'admin', 'numberOfDeployments': 0, 'lifecycleMode': False, 'vds': False, 'scaleUp': False, 'brownfield': False, 'templateValid': True, 'configurationChange': False})
  Details of the resource group deployment.


  id (, str, )
    The ID of the deployed resource group.


  deploymentName (, str, )
    The name of the resource group deployment.


  deploymentDescription (, str, )
    The description of the resource group deployment.


  serviceTemplate (, dict, )
    The service template of the resource group.


    id (, str, )
      The ID of the service template.


    templateName (, str, )
      The name of the service template.



  status (, str, )
    The status of the deployment of the resource group.


  firmwareRepositoryId (, str, )
    The ID of the firmware repository of the resource group.






Status
------





Authors
~~~~~~~

- Jennifer John (@johnj9) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

