**Ansible Modules for Dell Technologies PowerFlex** 
=========================================
### Release notes 2.6.0

>   © 2024 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
-------
These release notes contain supplemental information about Ansible
Modules for Dell Technologies (Dell) PowerFlex.

-   [Revision History](#revision-history)
-   [Product Description](#product-description)
-   [New Features](#new-features-and-enhancements)
-   [Known issues](#known-issues)
-   [Limitations](#limitations)
-   [Distribution](#distribution)
-   [Documentation](#documentation)

Revision history
----------------
The table in this section lists the revision history of this document.

Table 1. Revision history

| Revision | Date            | Description                                                 |
|----------|-----------------|-------------------------------------------------------------|
| 01       | Dec 2024        | Current release of Ansible Modules for Dell PowerFlex 2.6.0 |

Product description
-------------------

The Ansible modules for Dell PowerFlex are used to automate and orchestrate
the deployment, configuration, and management of Dell PowerFlex storage
systems. The capabilities of Ansible modules are managing volumes,
storage pools, SDCs, snapshots, snapshot policy, SDSs, SDTs, NVMe hosts, replication consistency groups, replication pairs, resource group, devices, protection domain, MDM and fault sets. 
cluster, and obtaining high-level information about a PowerFlex system information.
The modules use playbooks to list, show, create, delete, and modify
each of the entities.

New features and enhancements
-----------------------------
Along with the previous release deliverables, this release supports following features - 
 - Added new modules to support the management of SDT and NVMe Host.
 - Added Ansible role to support installation and uninstallation of SDT.
 - Info module is enhanced to support the listing of SDTs and NVMe hosts.

Known issues
------------
- Setting the RF cache and performance profile of the SDS during its creation fails intermittently on PowerFlex version 3.5.
- The creation of replication pair fails when copy_type is specified as OfflineCopy on PowerFlex version 4.0.
- Pagination in info module with offset and limit fetches more than expected records when listing service templates, deployments or firmware repository.
- Templates are fetched using the info module in spite of setting include_templates to false when listing deployments.

Limitations
-----------


Distribution
------------
The software package is available for download from the [Ansible Modules
for PowerFlex GitHub](https://github.com/dell/ansible-powerflex/tree/main) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerFlex GitHub](https://github.com/dell/ansible-powerflex/tree/main/docs)
page. It includes the following:

   - README
   - Release Notes (this document)
