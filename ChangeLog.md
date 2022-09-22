# ansible-powerflex Change Log

## Version 1.4.0 - released on 27/09/22
- Info module is enhanced to support the listing volumes and storage pools with statistics data​.
- Storage pool module is enhanced to get the details with statistics data​.
- Volume module is enhanced to get the details with statistics data​.
- Added support for 4.0.x release of PowerFlex OS.

## Version 1.3.0 - released on 28/06/22
- Added operations like Add/remove standby mdm, rename mdm, change mdm cluster ownership, switch mdm cluster mode, set performance profile, modify virtual IP interfaces and Get high level details of MDM cluster.
- Added execution environment manifest file to support building an execution environment with ansible-builder.
- Enabled the check_mode support for info module

## Version 1.2.0 - released on 25/03/22
- Added CRUD operations for protection domain module.
- Names of previously released modules have been changed from dellemc_powerflex_\<module name> to \<module name>.

## Version 1.1.1 - released on 16/12/21
- Gatherfacts has been renamed to Info.
- Product Guide, Release Notes and ReadMe updated as per community guidelines.

## Version 1.1.0 - released on 28/09/21
- Added dual licensing.
- Added CRUD operations for SDS and device.
- gatherfacts module is enhanced to list devices.

## Version 1.0.0 - released on 24/03/21
- Added CRUD operations for volumes, snapshots and storage pools.
- Added get and rename operation for SDC.
- gatherfacts module is added to list SDCs, SDSs, volumes, snapshots, storage pools, protection domains and snapshot policies.