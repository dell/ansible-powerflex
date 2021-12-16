# Ansible Modules for Dell EMC PowerFlex

The Ansible Modules for Dell EMC PowerFlex allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the provisioning and management of Dell EMC PowerFlex storage systems.

The capabilities of the Ansible modules are managing SDCs, volumes, snapshots, storage pools, SDSs and devices; and to gather high level facts from the storage system. The options available are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## License
Ansible collection for PowerFlex is released and licensed under the GPL-3.0 license. See [LICENSE](LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerFlex are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](MODULE-LICENSE) for the full terms.

## Support
Ansible collection for PowerFlex are supported by Dell EMC and are provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) section for the full terms. Dell EMC does not provide any support for the source code modifications. For any Ansible modules issues, questions or feedback, join the [Dell EMC Automation Community](https://www.dell.com/community/Automation/bd-p/Automation).


## Prerequisites

| **Ansible Modules** | **PowerFlex/VxFlex OS Version** | **Red Hat Enterprise Linux**| **SDK version**| **Python version** | **Ansible** |
|---------------------|-----------------------|------------------------------|--------------------|--------------------|-------------|
| v1.1.1 | 3.5, <br> 3.6 |7.8, <br>8.2 | 1.2.0 | 3.7.x <br> 3.8.x <br> 3.9.x | 2.10 <br> 2.11 <br> 2.12 |

  * Please follow PyPowerFlex installation instructions on [PyPowerFlex Documentation](https://github.com/dell/python-powerflex)
  
## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerFlex
  * [Info module](docs/Product%20Guide.md#info-module)
  * [Snapshot module](docs/Product%20Guide.md#snapshot-module)
  * [SDC module](docs/Product%20Guide.md#sdc-module)
  * [Storage pool module](docs/Product%20Guide.md#storage-pool-module)
  * [Volume module](docs/Product%20Guide.md#volume-module)
  * [SDS module](docs/Product%20Guide.md#sds-module)
  * [Device Module](docs/Product%20Guide.md#device-module)

## Installation of SDK
Install python sdk named 'PyPowerFlex'. It can be installed using pip, based on appropriate python version.
  * Clone the repo "https://github.com/dell/python-powerflex"
   using command:
   
        git clone https://github.com/dell/python-powerflex.git
  * Go to the root directory of setup.
  * Execute the following command:
  
        pip install .

## Building Collections
  * Use the following command to build the collection from source code:

        ansible-galaxy collection build

   For more details on how to build a tar ball, please refer: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections

#### Online Installation of Collections
  * Use the following command to install the latest collection hosted in [galaxy portal](https://galaxy.ansible.com/dellemc/powerflex):

        ansible-galaxy collection install dellemc.powerflex -p <install_path>

#### Offline Installation of Collections

  * Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powerflex) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powerflex) and use the following command to install the collection anywhere in your system:
 
        ansible-galaxy collection install dellemc-powerflex-1.1.1.tar.gz -p <install_path>

  * Set the environment variable:
  
        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>
 
## Using Collections

  * In order to use any Ansible module, ensure that the importing of proper FQCN(Fully Qualified Collection Name) must be embedded in the playbook.
   Below example can be referred
 
        collections:
        - dellemc.powerflex

  * In order to use installed collection in a specific task use a proper FQCN(Fully Qualified Collection Name). Refer to the following example:

        tasks:
        - name: Get Volume details
          dellemc.powerflex.dellemc_powerflex_volume
    
  * For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to the following example:
        
        ansible-doc dellemc.powerflex.dellemc_powerflex_volume

## Running Ansible Modules
The Ansible server must be configured with Python library for PowerFlex to run the Ansible playbooks. The [Documents](docs) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## SSL Certificate Validation

* Copy the CA certificate to the "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
* Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command:

        export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>
* Import the SSL certificate to host using the command:

        update-ca-trust extract
* If "TLS CA certificate bundle error" occurs, then follow below steps:

        cd /etc/pki/tls/certs/
        openssl x509 -in ca-bundle.crt -text -noout    

## Results
Each module returns the updated state and details of the entity, For example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.
