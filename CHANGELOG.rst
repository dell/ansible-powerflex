===============================
Dellemc.PowerFlex Change Logs
===============================

.. contents:: Topics


v1.9.0
======

Minor Changes
-------------

- Added Ansible role to support installation and uninstallation of Gateway.
- Added Ansible role to support installation and uninstallation of SDR.
- Added Ansible role to support installation and uninstallation of Web UI.

v1.8.0
======

Minor Changes
-------------

- Added Ansible role to support installation and uninstallation of LIA.
- Added Ansible role to support installation and uninstallation of MDM.
- Added Ansible role to support installation and uninstallation of SDS.
- Added Ansible role to support installation and uninstallation of TB.

v1.7.0
======

Minor Changes
-------------

- Added Ansible role to support installation and uninstallation of SDC.
- Added sample playbooks for the modules.
- Device module is enhanced to support force addition of device to the SDS.
- Info module is enhanced to list statistics in snapshot policies.
- Replication consistency group module is enhanced to support failover, restore, reverse, switchover, and sync operations.
- SDC module is enhanced to configure performance profile and to remove SDC.
- Updated modules to adhere with ansible community guidelines.

New Modules
-----------

- dellemc.powerflex.snapshot_policy - Manage snapshot policies on Dell PowerFlex

v1.6.0
======

Minor Changes
-------------

- Info module is enhanced to support the listing of replication pairs.

New Modules
-----------

- dellemc.powerflex.replication_pair - Manage replication pairs on Dell PowerFlex

v1.5.0
======

Minor Changes
-------------

- Info module is enhanced to support the listing replication consistency groups.
- Renamed gateway_host to hostname
- Renamed verifycert to validate_certs.
- Updated modules to adhere with ansible community guidelines.

New Modules
-----------

- dellemc.powerflex.replication_consistency_group - Manage replication consistency groups on Dell PowerFlex

v1.4.0
======

Minor Changes
-------------

- Added support for 4.0.x release of PowerFlex OS.
- Info module is enhanced to support the listing volumes and storage pools with statistics data.
- Storage pool module is enhanced to get the details with statistics data.
- Volume module is enhanced to get the details with statistics data.

v1.3.0
======

Minor Changes
-------------

- Added execution environment manifest file to support building an execution environment with ansible-builder.
- Enabled the check_mode support for info module

New Modules
-----------

- dellemc.powerflex.mdm_cluster - Manage MDM cluster on Dell PowerFlex

v1.2.0
======

Minor Changes
-------------

- Names of previously released modules have been changed from dellemc_powerflex_\<module name> to \<module name>.

New Modules
-----------

- dellemc.powerflex.protection_domain - Manage Protection Domain on Dell PowerFlex

v1.1.1
======

Deprecated Features
-------------------

- The dellemc_powerflex_gatherfacts module is deprecated and replaced with dellemc_powerflex_info

v1.1.0
======

Minor Changes
-------------

- Added dual licensing.
- Gatherfacts module is enhanced to list devices.

New Modules
-----------

- dellemc.powerflex.device - Manage device on Dell PowerFlex
- dellemc.powerflex.sds - Manage SDS on Dell PowerFlex

v1.0.0
======

New Modules
-----------

- dellemc.powerflex.info - Gathering information about Dell PowerFlex
- dellemc.powerflex.sdc - Manage SDCs on Dell PowerFlex
- dellemc.powerflex.snapshot - Manage Snapshots on Dell PowerFlex
- dellemc.powerflex.storagepool - Managing Dell PowerFlex storage pool
- dellemc.powerflex.volume - Manage volumes on Dell PowerFlex
