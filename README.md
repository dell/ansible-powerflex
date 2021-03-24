# Ansible Modules for Dell EMC PowerFlex

The Ansible Modules for Dell EMC PowerFlex allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the provisioning and management of Dell EMC PowerFlex storage systems.

The capabilities of the Ansible modules are managing SDCs, volumes, snapshots and storage pools; and to gather high level facts from the storage system. The options available for each are list, show, create, modify and delete. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## Support
Ansible modules for PowerFlex are supported by Dell EMC and are provided under the terms of the license attached to the source code. Dell EMC does not provide support for any source code modifications. For any Ansible module issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).

## Supported Platforms
  * Dell EMC PowerFlex (VxFlex OS) version 3.5

## Prerequisites
  * Ansible 2.9 or later
  * Python 3.5 or later
  * Red Hat Enterprise Linux 7.6, 7.7, 7.8, 8.2
  * PyPowerFlex python library for PowerFlex 1.1.0

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerFlex
  * Gather facts module
  * Snapshot module
  * SDC module
  * Storage pool module
  * Volume module

## Installation of SDK
Install python sdk named 'PyPowerFlex'. It can be installed using pip, based on appropriate python version.
  * Clone the repo "https://github.com/dell/python-powerflex"
   using command:
   
        git clone https://github.com/dell/python-powerflex.git
  * Go to the root directory of setup.
  * Execute the following command:
  
        pip install .

## Installing Collections
  * Download the tar build and execute the following command to install the collection anywhere in your system:
 
        ansible-galaxy collection install dellemc-powerflex-1.0.0.tar.gz -p <install_path>

  * Set the environment variable:
  
        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>
 
## Using Collections

  * In order to use any Ansible module, ensure that the importing of proper FQCN(Fully Qualified Collection Name) must be embedded in the playbook.
   Below example can be referred
 
        collections:
        - dellemc.powerflex

    
  * For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to the following example:
        
        ansible-doc dellemc.powerflex.dellemc_powerflex_gatherfacts

## Running Ansible Modules
The Ansible server must be configured with Python library for PowerFlex to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-powerflex/tree/1.0.0/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

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