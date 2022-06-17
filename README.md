# Ansible Modules for Dell Technologies PowerFlex

The Ansible Modules for Dell Technologies (Dell) PowerFlex allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the provisioning and management of Dell PowerFlex storage systems.

The capabilities of the Ansible modules are managing SDCs, volumes, snapshots, storage pools, SDSs, devices, protection domains, MDM cluster, and to gather high level facts from the storage system. The options available are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## License
The Ansible collection for PowerFlex is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powerflex/blob/1.3.0/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerFlex are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](https://github.com/dell/ansible-powerflex/blob/1.3.0/MODULE-LICENSE) for the full terms.

## Support
The Ansible collection for PowerFlex is supported by Dell and is provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) section for the full terms. Dell does not provide any support for the source code modifications. For any Ansible modules issues, questions or feedback, join the [Dell Automation Community](https://www.dell.com/community/Automation/bd-p/Automation).


## Prerequisites

| **Ansible Modules** | **PowerFlex/VxFlex OS Version** | **Red Hat Enterprise Linux**| **SDK version** | **Python version** | **Ansible**              |
|---------------------|-----------------------|------------------------------|-------|--------------------|--------------------------|
| v1.3.0 | 3.5, <br> 3.6 |7.9, <br>8.2, <br>8.4, <br>8.5 | 1.4.0 | 3.8.x <br> 3.9.x <br> 3.10.x | 2.11 <br> 2.12 <br> 2.13 |

  * Please follow PyPowerFlex installation instructions on [PyPowerFlex Documentation](https://github.com/dell/python-powerflex)
  
## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell PowerFlex
  * [Info module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#info-module)
  * [Snapshot module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#snapshot-module)
  * [SDC module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#sdc-module)
  * [Storage pool module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#storage-pool-module)
  * [Volume module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#volume-module)
  * [SDS module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#sds-module)
  * [Device Module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#device-module)
  * [Protection Domain Module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#protection-domain-module)
  * [MDM Cluster Module](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/Product%20Guide.md#mdm-cluster-module)

## Installation of SDK
* Install the python SDK named [PyPowerFlex](https://pypi.org/project/PyPowerFlex/). It can be installed using pip, based on appropriate python version. Execute this command:

        pip install PyPowerFlex
* Alternatively, Clone the repo "https://github.com/dell/python-powerflex"
   using command:
   
        git clone https://github.com/dell/python-powerflex.git
    * Go to the root directory of setup.
    * Execute this command:
      
            pip install .
## Building Collections
  * Use this command to build the collection from source code:

        ansible-galaxy collection build

   For more details on how to build a tar ball, please refer to: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections

#### Online Installation of Collections
  * Use this command to install the latest collection hosted in [galaxy portal](https://galaxy.ansible.com/dellemc/powerflex):

        ansible-galaxy collection install dellemc.powerflex -p <install_path>

#### Offline Installation of Collections

  * Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powerflex) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powerflex) and use this command to install the collection anywhere in your system:
 
        ansible-galaxy collection install dellemc-powerflex-1.3.0.tar.gz -p <install_path>

  * Set the environment variable:
  
        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>
 
## Using Collections

  * In order to use any Ansible module, ensure that the importing of proper FQCN(Fully Qualified Collection Name) must be embedded in the playbook.
   This example can be referred to:
 
        collections:
        - dellemc.powerflex

  * In order to use installed collection in a specific task use a proper FQCN(Fully Qualified Collection Name). Refer to this example:

        tasks:
        - name: Get Volume details
          dellemc.powerflex.volume
    
  * For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to this example:
        
        ansible-doc dellemc.powerflex.volume

## Running Ansible Modules
The Ansible server must be configured with Python library for PowerFlex to run the Ansible playbooks. The [Documents](https://github.com/dell/ansible-powerflex/blob/1.3.0/docs/) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## SSL Certificate Validation

* Copy the CA certificate to the "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
* Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command:

        export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>
* Import the SSL certificate to host using the command:

        update-ca-trust extract
* If "TLS CA certificate bundle error" occurs, then follow these steps:

        cd /etc/pki/tls/certs/
        openssl x509 -in ca-bundle.crt -text -noout    

## Results
Each module returns the updated state and details of the entity, For example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.

## Ansible Execution Environment
Ansible can also be installed in a container environment. Ansible Builder provides the ability to create reproducible, self-contained environments as container images that can be run as Ansible execution environments.
* Install the ansible builder package using:

      pip3 install ansible-builder
* Create the execution environment using:

      ansible-builder build --tag <tag_name> --container-runtime docker
* After the image is built, run the container using:

      docker run -it <tag_name> /bin/bash
* Verify collection installation using command:

      ansible-galaxy collection list
* The playbook can be run on the container using:

      docker run --rm -v $(pwd):/runner <tag_name> ansible-playbook info_test.yml

## Maintenance
Ansible Modules for Dell Technologies PowerFlex deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).
