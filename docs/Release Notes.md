**Ansible Modules for Dell EMC PowerFlex** 
=========================================
### Release Notes 1.0

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
-------
These release notes contain supplemental information about Ansible
Modules for Dell EMC PowerFlex.

-   Product Description
-   New Features
-   Known issues
-   Limitations
-   Distribution
-   Documentation

Product Description
-------------------

The Ansible Modules for Dell EMC PowerFlex are used for managing volumes,
storage pools, SDCs, and snapshots for PowerFlex storage devices. 
The modules use playbooks to list, show, create, delete, and modify
each of the entities.

The Ansible Modules for Dell EMC PowerFlex supports the following
features:

-   Create volumes, storage pools and snapshots. 
-   Modify volumes, storage pools, SDCs and snapshots.
-   Delete volumes and snapshots.
-   Get details of a volumes, snapshots, SDCs and storage pool.
-   Get entities of the PowerFlex storage device.

New Features
---------------------------

The Ansible Modules for Dell EMC PowerFlex release 1.0 supports the
following features:

- The following are the features of the gatherfacts module:
   - Get the API details of a PowerFlex storage device.
   - Get the list of SDCs.
   - Get the list of SDSs.
   - Get the list of volumes.
   - Get the list of snapshots.
   - Get the list of storage pools.
   - Get list of protection domains.
   - Get list of snapshot policies.

- The following are the features of the volume module:
   - Get the details of a volume.
   - Create a volume.
   - Modify details of a volume.
   - Delete a volume.

- The following are the features of the snapshot module:
   - Get the details of a snapshot.
   - Create a snapshot.
   - Modify details of a snapshot.
   - Delete a snapshot.

- The following are the features of the storage pools module:
   - Get the details of a storage pool.
   - Create a storage pool.
   - Modify details of a storage pool.

- The following are the features of the SDCs module:
   - Get the details of the SDC.
   - Rename a SDC.


Known issues
------------
There are no known issues.

Limitations
-----------
There are no known limitations.

Distribution
------------
The software package is available for download from the [Ansible Modules
for PowerFlex GitHub](https://github.com/dell/ansible-powerflex) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerFlex GitHub](https://github.com/dell/ansible-powerflex)
page. It includes the following:

   - README
   - Release Notes (this document)
   - Product Guide
