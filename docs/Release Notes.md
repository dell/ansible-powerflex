**Ansible Modules for Dell Technologies PowerFlex** 
=========================================
### Release notes 3.0.0

>   © 2025 Dell Inc. or its subsidiaries. All rights reserved. Dell
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
| 03       | Sep 2025        | Current release of Ansible Modules for Dell PowerFlex 3.0.0 |
| 02       | June 2025       | Current release of Ansible Modules for Dell PowerFlex 2.6.1 |
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
Note: In this context, PowerFlex Gen1 refers to PowerFlex versions < 5.0.0, and PowerFlex Gen2
refers to PowerFlex versions ≥ 5.0.0.

This release introduces extended support for Dell PowerFlex Gen2 by adding compatibility for
modules including mdm_cluster, nvme_host, sdc, sdt, and snapshot_policy, as well as
roles such as activemq, lia, mdm, and tb.

This release also includes new Gen2-specific modules — device_v2, info_v2, protection_domain_v2,
snapshot_v2, storagepool_v2, and volume_v2 — which replace their original Gen1 counterparts for Gen2 environments.

Additionally, the modules fault_set, replication_consistency_group, replication_pair, resource_group,
and sds are not supported on PowerFlex Gen2 and are deprecated for Gen2 use. However, all deprecated
modules continue to be fully supported on PowerFlex Gen1.

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
