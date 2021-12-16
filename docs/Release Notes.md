**Ansible Modules for Dell EMC PowerFlex** 
=========================================
### Release Notes 1.1.1

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
-------
These release notes contain supplemental information about Ansible
Modules for Dell EMC PowerFlex.

-   [Product Description](#product-description)
-   [New Features](#new-features)
-   [Known issues](#known-issues)
-   [Limitations](#limitations)
-   [Distribution](#distribution)
-   [Documentation](#documentation)

Product Description
-------------------

The Ansible Modules for Dell EMC PowerFlex are used for managing volumes,
storage pools, SDCs, snapshots, SDSs and devices for PowerFlex storage devices. 
The modules use playbooks to list, show, create, delete, and modify
each of the entities.

The Ansible Modules for Dell EMC PowerFlex supports the following
features:

-   Create volumes, storage pools, snapshots, SDSs.
-   Add devices.
-   Modify volumes, storage pools, SDCs, snapshots and SDSs.
-   Delete volumes, snapshots and SDSs.
-   Get details of a volumes, snapshots, SDCs, storage pools, SDSs and devices.
-   Get entities of the PowerFlex storage device.
-   Remove devices.

New Features
---------------------------
- The Product Guide, Release Notes and ReadMe have been updated to adhere to the guidelines by the ansible community.
- "gatherfacts" module has been renamed to "info" module.

Known issues
------------
- Setting the RF cache and performance profile of the SDS during its creation fails intermittently on PowerFlex version 3.5 

Limitations
-----------
There are no known limitations.

Distribution
------------
The software package is available for download from the [Ansible Modules
for PowerFlex GitHub](https://github.com/dell/ansible-powerflex/tree/1.1.1) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerFlex GitHub](../docs)
page. It includes the following:

   - README
   - Release Notes (this document)
   - Product Guide
