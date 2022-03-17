# Ansible Modules for Dell Technologies PowerFlex
## Product Guide 1.2.0
© 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

--------------
## Contents
*   [Volume Module](#volume-module)
    *   [Synopsis](#synopsis)
    *   [Parameters](#parameters)
    *   [Notes](#notes)
    *   [Examples](#examples)
    *   [Return Values](#return-values)
    *   [Authors](#authors)
*   [Protection Domain Module](#protection-domain-module)
    *   [Synopsis](#synopsis-1)
    *   [Parameters](#parameters-1)
    *   [Notes](#notes-1)
    *   [Examples](#examples-1)
    *   [Return Values](#return-values-1)
    *   [Authors](#authors-1)
*   [Storage Pool Module](#storage-pool-module)
    *   [Synopsis](#synopsis-2)
    *   [Parameters](#parameters-2)
    *   [Notes](#notes-2)
    *   [Examples](#examples-2)
    *   [Return Values](#return-values-2)
    *   [Authors](#authors-2)
*   [SDS Module](#sds-module)
    *   [Synopsis](#synopsis-3)
    *   [Parameters](#parameters-3)
    *   [Notes](#notes-3)
    *   [Examples](#examples-3)
    *   [Return Values](#return-values-3)
    *   [Authors](#authors-3)
*   [Device Module](#device-module)
    *   [Synopsis](#synopsis-4)
    *   [Parameters](#parameters-4)
    *   [Notes](#notes-4)
    *   [Examples](#examples-4)
    *   [Return Values](#return-values-4)
    *   [Authors](#authors-4)
*   [Snapshot Module](#snapshot-module)
    *   [Synopsis](#synopsis-5)
    *   [Parameters](#parameters-5)
    *   [Notes](#notes-5)
    *   [Examples](#examples-5)
    *   [Return Values](#return-values-5)
    *   [Authors](#authors-5)
*   [Info Module](#info-module)
    *   [Synopsis](#synopsis-6)
    *   [Parameters](#parameters-6)
    *   [Notes](#notes-6)
    *   [Examples](#examples-6)
    *   [Return Values](#return-values-6)
    *   [Authors](#authors-6)
*   [SDC Module](#sdc-module)
    *   [Synopsis](#synopsis-7)
    *   [Parameters](#parameters-7)
    *   [Notes](#notes-7)
    *   [Examples](#examples-7)
    *   [Return Values](#return-values-7)
    *   [Authors](#authors-7)

--------------

# Volume Module

Manage volumes on Dell EMC PowerFlex

### Synopsis
 Managing volumes on PowerFlex storage system includes creating, getting details, modifying attributes and deleting volume.
 It also includes adding/removing snapshot policy, mapping/unmapping volume to/from SDC and listing associated snapshots.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=2 > delete_snapshots</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> If True, the volume and all its dependent snapshots will be deleted.  <br> If False, only the volume will be deleted.  <br> It can be specified only when the state is absent.  <br> It defaults to False, if not specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > sdc</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies SDC parameters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > sdc_id </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> ID of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip.  <br> Mutually exclusive with sdc_name and sdc_ip.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > sdc_name </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Name of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip.  <br> Mutually exclusive with sdc_id and sdc_ip.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > access_mode </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>READ_WRITE</li>  <li>READ_ONLY</li>  <li>NO_ACCESS</li> </ul></td>
                <td>  <br> Define the access mode for all mappings of the volume.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > iops_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit of volume IOPS.  <br> Minimum IOPS limit is 11 and specify 0 for unlimited iops.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > sdc_ip </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> IP of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip.  <br> Mutually exclusive with sdc_id and sdc_ip.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > bandwidth_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit of volume network bandwidth.  <br> Need to mention in multiple of 1024 Kbps.  <br> To set no limit, 0 is to be passed.  </td>
            </tr>
                            <tr>
            <td colspan=2 > protection_domain_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the protection domain.  <br> During creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.  <br> Mutually exclusive with protection_domain_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_policy_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the snapshot policy.  <br> To remove/detach snapshot policy, empty snapshot_policy_id/snapshot_policy_name is to be passed along with auto_snap_remove_type. </td>
        </tr>
                    <tr>
            <td colspan=2 > storage_pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the storage pool.  <br> Either name or the id of the storage pool is required for creating a volume.  <br> During creation, if storage pool name is provided then either protection domain name or id must be mentioned along with it.  <br> Mutually exclusive with storage_pool_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_policy_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the snapshot policy.  <br> To remove/detach snapshot policy, empty snapshot_policy_id/snapshot_policy_name is to be passed along with auto_snap_remove_type. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > allow_multiple_mappings</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies whether to allow multiple mappings or not.  <br> If the volume is mapped to one SDC then for every new mapping allow_multiple_mappings has to be passed as True. </td>
        </tr>
                    <tr>
            <td colspan=2 > sdc_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> Mapping state of the SDC. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > compression_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>NORMAL</li>  <li>NONE</li> </ul></td>
            <td> <br> Type of the compression method. </td>
        </tr>
                    <tr>
            <td colspan=2 > storage_pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the storage pool.  <br> Either name or the id of the storage pool is required for creating a volume.  <br> Mutually exclusive with storage_pool_name. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the volume.  <br> Except create operation, all other operations can be performed using vol_id.  <br> Mutually exclusive with vol_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume.  <br> Mandatory for create operation.  <br> It is unique across the PowerFlex array.  <br> Mutually exclusive with vol_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > auto_snap_remove_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>remove</li>  <li>detach</li> </ul></td>
            <td> <br> Whether to remove or detach the snapshot policy.  <br> To remove/detach snapshot policy, empty snapshot_policy_id/snapshot_policy_name is to be passed along with auto_snap_remove_type.  <br> If the snapshot policy name/id is passed empty then auto_snap_remove_type is defaulted to 'detach'. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>THICK_PROVISIONED</li>  <li>THIN_PROVISIONED</li> </ul></td>
            <td> <br> Type of volume provisioning. </td>
        </tr>
                    <tr>
            <td colspan=2 > protection_domain_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the protection domain.  <br> During creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.  <br> Mutually exclusive with protection_domain_name. </td>
        </tr>
                    <tr>
            <td colspan=2 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> The unit of the volume size. It defaults to 'GB'. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > size</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The size of the volume.  <br> Size of the volume will be assigned as higher multiple of 8 GB. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the volume. Used to rename the volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > use_rmcache</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Whether to use RM Cache or not. </td>
        </tr>
                                                                            </table>

### Notes
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Create a volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    storage_pool_name: "pool_1"
    protection_domain_name: "pd_1"
    vol_type: "THICK_PROVISIONED"
    compression_type: "NORMAL"
    use_rmcache: True
    size: 16
    state: "present"

- name: Map a SDC to volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    allow_multiple_mappings: True
    sdc:
      - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
        access_mode: "READ_WRITE"
    sdc_state: "mapped"
    state: "present"

- name: Unmap a SDC to volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    sdc:
      - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
    sdc_state: "unmapped"
    state: "present"

- name: Map multiple SDCs to a volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    protection_domain_name: "pd_1"
    sdc:
      - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
        access_mode: "READ_WRITE"
        bandwidth_limit: 2048
        iops_limit: 20
      - sdc_ip: "198.10.xxx.xxx"
        access_mode: "READ_ONLY"
    allow_multiple_mappings: True
    sdc_state: "mapped"
    state: "present"

- name: Get the details of the volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_id: "fe6c8b7100000005"
    state: "present"

- name: Modify the details of the Volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    storage_pool_name: "pool_1"
    new_vol_name: "new_sample_volume"
    size: 64
    state: "present"

- name: Delete the Volume
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    delete_snapshots: False
    state: "absent"

- name: Delete the Volume and all its dependent snapshots
  dellemc.powerflex.volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    delete_snapshots: True
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=3 > volume_details </td>
            <td>  complex </td>
            <td> When volume exists </td>
            <td> Details of the volume. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protectionDomainName </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the protection domain in which volume resides. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storagePoolName </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the storage pool in which volume resides. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > snapshotPolicyName </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot policy associated with volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protectionDomainId </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the protection domain in which volume resides. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sizeInGb </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the volume in Gb. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > snapshotsList </td>
                <td> str </td>
                <td>success</td>
                <td> List of snapshots associated with the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sizeInKb </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the volume in Kb. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > snapshotPolicyId </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the snapshot policy associated with volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > mappedSdcInfo </td>
                <td> complex </td>
                <td>success</td>
                <td> The details of the mapped SDC. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > accessMode </td>
                    <td> str </td>
                    <td>success</td>
                    <td> mapping access mode for the specified volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > limitIops </td>
                    <td> int </td>
                    <td>success</td>
                    <td> IOPS limit for the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sdcId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > limitBwInMbps </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Bandwidth limit for the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sdcIp </td>
                    <td> str </td>
                    <td>success</td>
                    <td> IP of the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sdcName </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the SDC. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storagePoolId </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the storage pool in which volume resides. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# Protection Domain Module

Manage Protection Domain on Dell EMC PowerFlex

### Synopsis
 Managing Protection Domain on PowerFlex storage system includes creating, modifying attributes, deleting and getting details of Protection Domain.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=2 > protection_domain_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the protection domain.  <br> Mandatory for create operation.  <br> It is unique across the PowerFlex array.  <br> Mutually exclusive with protection_domain_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > is_active</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Used to activate or deactivate the protection domain. </td>
        </tr>
                    <tr>
            <td colspan=2 > rf_cache_limits</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Used to set the RFcache parameters of the protection domain. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > max_io_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Used to set cache maximum I/O limit in KB.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > is_enabled </td>
                <td> bool  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Used to enable or disable RFcache in the protection domain.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > page_size </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Used to set the cache page size in KB.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > pass_through_mode </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>None</li>  <li>Read</li>  <li>Write</li>  <li>ReadAndWrite</li>  <li>WriteMiss</li> </ul></td>
                <td>  <br> Used to set the cache mode.  </td>
            </tr>
                            <tr>
            <td colspan=2 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the protection domain. </td>
        </tr>
                    <tr>
            <td colspan=2 > network_limits</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Network bandwidth limit used by all SDS in protection domain. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > rebalance_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit the network bandwidth for rebalance.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > overall_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit the overall network bandwidth.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > vtree_migration_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit the network bandwidth for vtree migration.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > bandwidth_unit </td>
                <td> str  </td>
                <td></td>
                <td> KBps </td>
                <td> <ul> <li>KBps</li>  <li>MBps</li>  <li>GBps</li> </ul></td>
                <td>  <br> Unit for network bandwidth limits.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > rebuild_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit the network bandwidth for rebuild.  </td>
            </tr>
                            <tr>
            <td colspan=2 > protection_domain_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the protection domain.  <br> Except for create operation, all other operations can be performed using protection_domain_id.  <br> Mutually exclusive with protection_domain_name. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > protection_domain_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Used to rename the protection domain. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                                                                            </table>

### Notes
* The protection domain can only be deleted if all its related objects have been dissociated from the protection domain.
* If the protection domain set to inactive, then no operation can be performed on protection domain.
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Create protection domain
  dellemc.powerflex.protection_domain:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Create protection domain with all parameters
  dellemc.powerflex.protection_domain:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    is_active: true
    network_limits:
      rebuild_limit: 10
      rebalance_limit: 17
      vtree_migration_limit: 14
      overall_limit: 20
      bandwidth_unit: "MBps"
    rf_cache_limits:
      is_enabled: true
      page_size: 16
      max_io_limit: 128
      pass_through_mode: "Read"
    state: "present"

- name: Get protection domain details using name
  dellemc.powerflex.protection_domain:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Get protection domain details using ID
  dellemc.powerflex.protection_domain:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    protection_domain_id: "5718253c00000004"
    state: "present"

- name: Modify protection domain attributes
  dellemc.powerflex.protection_domain:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    protection_domain_new_name: "domain1_new"
    network_limits:
      rebuild_limit: 14
      rebalance_limit: 20
      overall_limit: 25
      bandwidth_unit: "MBps"
    rf_cache_limits:
      page_size: 64
      pass_through_mode: "WriteMiss"
    state: "present"

- name: Delete protection domain using name
  dellemc.powerflex.protection_domain:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    protection_domain_name: "domain1_new"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=6>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=6 > protection_domain_details </td>
            <td>  complex </td>
            <td> When protection domain exists </td>
            <td> Details of the protection domain. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the protection domain. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > sdrSdsConnectivityInfo </td>
                <td> dict </td>
                <td>success</td>
                <td> Connectivity info of SDR and SDS. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > clientServerConnStatus </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Connectivity status of client and server. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > disconnectedClientId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Disconnected client ID. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > disconnectedClientName </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Disconnected client name. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > disconnectedServerIp </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Disconnected server IP. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > disconnectedServerId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Disconnected server ID. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > disconnectedServerName </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Disconnected server name. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rfcacheMaxIoSizeKb </td>
                <td> int </td>
                <td>success</td>
                <td> RF cache maximum I/O size in KB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > systemId </td>
                <td> str </td>
                <td>success</td>
                <td> ID of system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > fglDefaultMetadataCacheSize </td>
                <td> int </td>
                <td>success</td>
                <td> FGL metadata cache size. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rebuildNetworkThrottlingInKbps </td>
                <td> int </td>
                <td>success</td>
                <td> Rebuild network throttling in KBps. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > mdmSdsNetworkDisconnectionsCounterParameters </td>
                <td> dict </td>
                <td>success</td>
                <td> MDM's SDS counter parameter. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > longWindow </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Long window for Counter Parameters. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > shortWindow </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Short window for Counter Parameters. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > mediumWindow </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Medium window for Counter Parameters. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > protectionDomainState </td>
                <td> int </td>
                <td>success</td>
                <td> State of protection domain. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > overallIoNetworkThrottlingEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether overall network throttling enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > fglMetadataCacheEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether FGL cache enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > vtreeMigrationNetworkThrottlingInKbps </td>
                <td> int </td>
                <td>success</td>
                <td> V-Tree migration network throttling in KBps. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > storagePool </td>
                <td> list </td>
                <td>success</td>
                <td> List of storage pools. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rfcachePageSizeKb </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache page size in KB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > protectedMaintenanceModeNetworkThrottlingInKbps </td>
                <td> int </td>
                <td>success</td>
                <td> Protected maintenance mode network throttling in KBps. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Protection domain ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > overallIoNetworkThrottlingInKbps </td>
                <td> int </td>
                <td>success</td>
                <td> Overall network throttling in KBps. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rebalanceNetworkThrottlingEnabled </td>
                <td> int </td>
                <td>success</td>
                <td> Whether rebalance network throttling enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rfcacheAccpId </td>
                <td> str </td>
                <td>success</td>
                <td> Id of RF cache acceleration pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rfcacheEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether RF cache is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > fglDefaultNumConcurrentWrites </td>
                <td> str </td>
                <td>success</td>
                <td> FGL concurrent writes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rebuildNetworkThrottlingEnabled </td>
                <td> int </td>
                <td>success</td>
                <td> Whether rebuild network throttling enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > links </td>
                <td> list </td>
                <td>success</td>
                <td> Protection domain links. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > rel </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Protection domain's relationship with different entities. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > href </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Protection domain instance URL. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rebalanceNetworkThrottlingInKbps </td>
                <td> int </td>
                <td>success</td>
                <td> Rebalance network throttling in KBps. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > rfcacheOpertionalMode </td>
                <td> str </td>
                <td>success</td>
                <td> RF cache operational mode. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > protectedMaintenanceModeNetworkThrottlingEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether protected maintenance mode network throttling enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > vtreeMigrationNetworkThrottlingEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether V-Tree migration network throttling enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=5 > sdsSdsNetworkDisconnectionsCounterParameters </td>
                <td> dict </td>
                <td>success</td>
                <td> Counter parameter for SDS-SDS network. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > longWindow </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Long window for Counter Parameters. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > shortWindow </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Short window for Counter Parameters. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=4 > mediumWindow </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Medium window for Counter Parameters. </td>
                </tr>
                                                                    <tr>
            <td colspan=6 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Bhavneet Sharma (@sharmb5) <ansible.team@dell.com>

--------------------------------
# Storage Pool Module

Managing Dell EMC PowerFlex storage pool

### Synopsis
 Dell EMC PowerFlex storage pool module includes getting the details of storage pool, creating a new storage pool, and modifying the attribute of a storage pool.

### Parameters
                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=1 > protection_domain_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the protection domain.  <br> During creation of a pool, either protection domain name or id must be mentioned.  <br> Mutually exclusive with protection_domain_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_pool_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name for the storage pool can be provided.  <br> This parameter is used for renaming the storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the storage pool.  <br> If more than one storage pool is found with the same name then protection domain id/name is required to perform the task.  <br> Mutually exclusive with storage_pool_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > protection_domain_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the protection domain.  <br> During creation of a pool, either protection domain name or id must be mentioned.  <br> Mutually exclusive with protection_domain_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > use_rfcache</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Enable/Disable RFcache on a specific storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > media_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>HDD</li>  <li>SSD</li>  <li>TRANSITIONAL</li> </ul></td>
            <td> <br> Type of devices in the storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > use_rmcache</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Enable/Disable RMcache on a specific storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The id of the storage pool.  <br> It is auto generated, hence should not be provided during creation of a storage pool.  <br> Mutually exclusive with storage_pool_name. </td>
        </tr>
                                                                            </table>

### Notes
* TRANSITIONAL media type is supported only during modification.
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Get the details of storage pool by name
  dellemc.powerflex.storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_name: "sample_pool_name"
    protection_domain_name: "sample_protection_domain"
    state: "present"

- name: Get the details of storage pool by id
  dellemc.powerflex.storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_id: "abcd1234ab12r"
    state: "present"

- name: Create a new storage pool by name
  dellemc.powerflex.storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_name: "ansible_test_pool"
    protection_domain_id: "1c957da800000000"
    media_type: "HDD"
    state: "present"

- name: Modify a storage pool by name
  dellemc.powerflex.storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_name: "ansible_test_pool"
    protection_domain_id: "1c957da800000000"
    use_rmcache: True
    use_rfcache: True
    state: "present"

- name: Rename storage pool by id
  dellemc.powerflex.storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_id: "abcd1234ab12r"
    storage_pool_new_name: "new_ansible_pool"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > storage_pool_details </td>
            <td>  complex </td>
            <td> When storage pool exists </td>
            <td> Details of the storage pool. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > useRfcache </td>
                <td> bool </td>
                <td>success</td>
                <td> Enable/Disable RFcache on a specific storage pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > protectionDomainName </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the protection domain in which pool resides. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the storage pool under protection domain. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > mediaType </td>
                <td> str </td>
                <td>success</td>
                <td> Type of devices in the storage pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > useRmcache </td>
                <td> bool </td>
                <td>success</td>
                <td> Enable/Disable RMcache on a specific storage pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the storage pool under protection domain. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > protectionDomainId </td>
                <td> str </td>
                <td>success</td>
                <td> ID of the protection domain in which pool resides. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* P Srinivas Rao (@srinivas-rao5) <ansible.team@dell.com>

--------------------------------
# SDS Module

Manage SDS on Dell EMC PowerFlex

### Synopsis
 Managing SDS on PowerFlex storage system includes creating new SDS, getting details of SDS, adding/removing IP to/from SDS, modifying attributes of SDS, and deleting SDS.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=2 > protection_domain_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the protection domain.  <br> Mutually exclusive with protection_domain_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > rmcache_size</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Read RAM cache size (in MB).  <br> Minimum size is 128 MB.  <br> Maximum size is 3911 MB. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the SDS. </td>
        </tr>
                    <tr>
            <td colspan=2 > protection_domain_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the protection domain.  <br> Mutually exclusive with protection_domain_name. </td>
        </tr>
                    <tr>
            <td colspan=2 > sds_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> SDS new name. </td>
        </tr>
                    <tr>
            <td colspan=2 > sds_ip_list</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Dictionary of IPs and their roles for the SDS.  <br> At least one IP-role is  mandatory while creating a SDS.  <br> IP-roles can be updated as well. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ip </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> IP address of the SDS.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > role </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td> <ul> <li>sdsOnly</li>  <li>sdcOnly</li>  <li>all</li> </ul></td>
                <td>  <br> Role assigned to the SDS IP address.  </td>
            </tr>
                            <tr>
            <td colspan=2 > performance_profile</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Compact</li>  <li>HighPerformance</li> </ul></td>
            <td> <br> Performance profile to apply to the SDS.  <br> The HighPerformance profile configures a predefined set of parameters for very high performance use cases.  <br> Default value by API is "HighPerformance". </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > sds_ip_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-sds</li>  <li>absent-in-sds</li> </ul></td>
            <td> <br> State of IP with respect to the SDS. </td>
        </tr>
                    <tr>
            <td colspan=2 > rmcache_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Whether to enable the Read RAM cache. </td>
        </tr>
                    <tr>
            <td colspan=2 > sds_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the SDS.  <br> Except create operation, all other operations can be performed using sds_id.  <br> Mutually exclusive with sds_name. </td>
        </tr>
                    <tr>
            <td colspan=2 > sds_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the SDS.  <br> Mandatory for create operation.  <br> It is unique across the PowerFlex array.  <br> Mutually exclusive with sds_id. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > rfcache_enabled</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Whether to enable the Read Flash cache. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                                                                            </table>

### Notes
* The maximum limit for the IPs that can be associated with an SDS is 8.
* There needs to be at least 1 IP for SDS communication and 1 for SDC communication.
* If only 1 IP exists, it must be with role 'all'; else 1 IP can be with role 'all'and other IPs with role 'sdcOnly'; or 1 IP must be with role 'sdsOnly' and others with role 'sdcOnly'.
* There can be 1 or more IPs with role 'sdcOnly'.
* There must be only 1 IP with SDS role (either with role 'all' or 'sdsOnly').
* SDS can be created with RF cache disabled, but, be aware that the RF cache is not always updated. In this case, the user should re-try the operation.
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Create SDS
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node0"
    protection_domain_name: "domain1"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "all"
    sds_ip_state: "present-in-sds"
    state: "present"

- name: Create SDS with all parameters
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node1"
    protection_domain_name: "domain1"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "sdcOnly"
    sds_ip_state: "present-in-sds"
    rmcache_enabled: true
    rmcache_size: 128
    performance_profile: "HighPerformance"
    state: "present"

- name: Get SDS details using name
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node0"
    state: "present"

- name: Get SDS details using ID
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_id: "5718253c00000004"
    state: "present"

- name: Modify SDS attributes using name
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node0"
    sds_new_name: "node0_new"
    rfcache_enabled: true
    rmcache_enabled: true
    rmcache_size: 256
    performance_profile: "HighPerformance"
    state: "present"

- name: Modify SDS attributes using ID
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_id: "5718253c00000004"
    sds_new_name: "node0_new"
    rfcache_enabled: true
    rmcache_enabled: true
    rmcache_size: 256
    performance_profile: "HighPerformance"
    state: "present"

- name: Add IP and role to an SDS
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node0"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "sdcOnly"
    sds_ip_state: "present-in-sds"
    state: "present"

- name: Remove IP and role from an SDS
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node0"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "sdcOnly"
    sds_ip_state: "absent-in-sds"
    state: "present"

- name: Delete SDS using name
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_name: "node0"
    state: "absent"

- name: Delete SDS using ID
  dellemc.powerflex.sds:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    sds_id: "5718253c00000004"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > sds_details </td>
            <td>  complex </td>
            <td> When SDS exists </td>
            <td> Details of the SDS. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > sdsConfigurationFailure </td>
                <td> str </td>
                <td>success</td>
                <td> SDS configuration failure. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > protectionDomainName </td>
                <td> str </td>
                <td>success</td>
                <td> Protection Domain Name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the SDS. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheErrorDeviceDoesNotExist </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache error for device does not exist. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > configuredDrlMode </td>
                <td> str </td>
                <td>success</td>
                <td> Configured DRL mode. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rmcacheFrozen </td>
                <td> bool </td>
                <td>success</td>
                <td> RM cache frozen. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > fglMetadataCacheState </td>
                <td> str </td>
                <td>success</td>
                <td> FGL metadata cache state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheErrorInvalidDriverPath </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache error for invalid driver path. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > protectionDomainId </td>
                <td> str </td>
                <td>success</td>
                <td> Protection Domain ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > ipList </td>
                <td> list </td>
                <td>success</td>
                <td> SDS IP list. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > ip </td>
                    <td> str </td>
                    <td>success</td>
                    <td> IP present in the SDS. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > role </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Role of the SDS IP. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > sdsDecoupled </td>
                <td> str </td>
                <td>success</td>
                <td> SDS decoupled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > certificateInfo </td>
                <td> str </td>
                <td>success</td>
                <td> Information about certificate. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > fglNumConcurrentWrites </td>
                <td> int </td>
                <td>success</td>
                <td> FGL concurrent writes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rmcacheMemoryAllocationState </td>
                <td> bool </td>
                <td>success</td>
                <td> RM cache memory allocation state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > sdsState </td>
                <td> str </td>
                <td>success</td>
                <td> SDS state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > numRestarts </td>
                <td> int </td>
                <td>success</td>
                <td> Number of restarts. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > perfProfile </td>
                <td> str </td>
                <td>success</td>
                <td> Performance profile. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > onVmWare </td>
                <td> bool </td>
                <td>success</td>
                <td> Presence on VMware. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > numOfIoBuffers </td>
                <td> int </td>
                <td>success</td>
                <td> Number of IO buffers. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > drlMode </td>
                <td> str </td>
                <td>success</td>
                <td> DRL mode. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > id </td>
                <td> str </td>
                <td>success</td>
                <td> SDS ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rmcacheSizeInKb </td>
                <td> int </td>
                <td>success</td>
                <td> RM cache size in KB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > lastUpgradeTime </td>
                <td> str </td>
                <td>success</td>
                <td> Last time SDS was upgraded. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheErrorInconsistentCacheConfiguration </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache error for inconsistent cache configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheErrorLowResources </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache error for low resources. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > fglMetadataCacheSize </td>
                <td> int </td>
                <td>success</td>
                <td> FGL metadata cache size. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > softwareVersionInfo </td>
                <td> str </td>
                <td>success</td>
                <td> SDS software version information. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > mdmConnectionState </td>
                <td> str </td>
                <td>success</td>
                <td> MDM connection state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether RF cache is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > sdsReceiveBufferAllocationFailures </td>
                <td> str </td>
                <td>success</td>
                <td> SDS receive buffer allocation failures. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > links </td>
                <td> list </td>
                <td>success</td>
                <td> SDS links. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > rel </td>
                    <td> str </td>
                    <td>success</td>
                    <td> SDS's relationship with different entities. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > href </td>
                    <td> str </td>
                    <td>success</td>
                    <td> SDS instance URL. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > membershipState </td>
                <td> str </td>
                <td>success</td>
                <td> Membership state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > raidControllers </td>
                <td> int </td>
                <td>success</td>
                <td> Number of RAID controllers. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > port </td>
                <td> int </td>
                <td>success</td>
                <td> SDS port. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheErrorApiVersionMismatch </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache error for API version mismatch. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > authenticationError </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates authentication error. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rfcacheErrorInconsistentSourceConfiguration </td>
                <td> bool </td>
                <td>success</td>
                <td> RF cache error for inconsistent source configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rmcacheEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether Read RAM cache is enabled or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > maintenanceType </td>
                <td> str </td>
                <td>success</td>
                <td> Maintenance type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rmcacheSizeInMb </td>
                <td> int </td>
                <td>success</td>
                <td> RM cache size in MB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > maintenanceState </td>
                <td> str </td>
                <td>success</td>
                <td> Maintenance state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > faultSetId </td>
                <td> str </td>
                <td>success</td>
                <td> Fault set ID. </td>
            </tr>
                                        <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Device Module

Manage device on Dell EMC PowerFlex

### Synopsis
 Managing device on PowerFlex storage system includes adding new device, getting details of device, and removing a device.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=1 > current_pathname</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Full path of the device to be added.  <br> Required while adding a device. </td>
        </tr>
                    <tr>
            <td colspan=1 > external_acceleration_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Invalid</li>  <li>None</li>  <li>Read</li>  <li>Write</li>  <li>ReadAndWrite</li> </ul></td>
            <td> <br> Device external acceleration types.  <br> Used while adding a device. </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Storage Pool name.  <br> Used while adding a storage device.  <br> Mutually exclusive with storage_pool_id, acceleration_pool_id and acceleration_pool_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the device. </td>
        </tr>
                    <tr>
            <td colspan=1 > protection_domain_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Protection domain ID.  <br> Used while identifying a storage pool along with storage_pool_name.  <br> Mutually exclusive with protection_domain_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > protection_domain_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Protection domain name.  <br> Used while identifying a storage pool along with storage_pool_name.  <br> Mutually exclusive with protection_domain_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > acceleration_pool_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Acceleration Pool Name.  <br> Used while adding an acceleration device.  <br> Media type supported are SSD and NVDIMM.  <br> Mutually exclusive with storage_pool_id, storage_pool_name and acceleration_pool_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > media_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>HDD</li>  <li>SSD</li>  <li>NVDIMM</li> </ul></td>
            <td> <br> Device media types.  <br> Required while adding a device. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > device_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Device name.  <br> Mutually exclusive with device_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Storage Pool ID.  <br> Used while adding a storage device.  <br> Media type supported are SSD and HDD.  <br> Mutually exclusive with storage_pool_name, acceleration_pool_id and acceleration_pool_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > sds_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the SDS.  <br> Required while adding a device.  <br> Mutually exclusive with sds_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=1 > acceleration_pool_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Acceleration Pool ID.  <br> Used while adding an acceleration device.  <br> Media type supported are SSD and NVDIMM.  <br> Mutually exclusive with acceleration_pool_name, storage_pool_name and storage_pool_id. </td>
        </tr>
                    <tr>
            <td colspan=1 > sds_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the SDS.  <br> Required while adding a device.  <br> Mutually exclusive with sds_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > device_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Device ID.  <br> Mutually exclusive with device_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                                                                            </table>

### Notes
* The value for device_id is generated only after successful addition of the device.
* Unique ways to identify a device - (current_pathname , sds_id) or (current_pathname , sds_name) or (device_name , sds_name) or (device_name , sds_id) or device_id.
* It is recommended to install Rfcache driver for SSD device on SDS in order to add it to an acceleration pool.
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Add a device
  dellemc.powerflex.device:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_name: "node1"
    media_type: "HDD"
    device_name: "device2"
    storage_pool_name: "pool1"
    protection_domain_name: "domain1"
    external_acceleration_type: "ReadAndWrite"
    state: "present"
- name: Get device details using device_id
  dellemc.powerflex.device:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    device_id: "d7fe088900000000"
    state: "present"
- name: Get device details using (current_pathname, sds_name)
  dellemc.powerflex.device:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_name: "node0"
    state: "present"
- name: Get device details using (current_pathname, sds_id)
  dellemc.powerflex.device:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    current_pathname: "/dev/sdb"
    sds_id: "5717d71800000000"
    state: "present"
- name: Remove a device using device_id
  dellemc.powerflex.device:
   gateway_host: "{{gateway_host}}"
   username: "{{username}}"
   password: "{{password}}"
   verifycert: "{{verifycert}}"
   port: "{{port}}"
   device_id: "76eb7e2f00010000"
   state: "absent"
- name: Remove a device using (current_pathname, sds_id)
  dellemc.powerflex.device:
   gateway_host: "{{gateway_host}}"
   username: "{{username}}"
   password: "{{password}}"
   verifycert: "{{verifycert}}"
   port: "{{port}}"
   current_pathname: "/dev/sdb"
   sds_name: "node1"
   state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=3 > device_details </td>
            <td>  complex </td>
            <td> When device exists </td>
            <td> Details of the device. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Device name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > ssdEndOfLifeState </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates SSD end of life state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > deviceType </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates device type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > capacity </td>
                <td> int </td>
                <td>success</td>
                <td> Device capacity. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protectionDomainId </td>
                <td> str </td>
                <td>success</td>
                <td> Protection domain ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > serialNumber </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates Serial number. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > aggregatedState </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates aggregated state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sdsName </td>
                <td> str </td>
                <td>success</td>
                <td> SDS name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storagePoolName </td>
                <td> str </td>
                <td>success</td>
                <td> Storage Pool name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > maxCapacityInKb </td>
                <td> int </td>
                <td>success</td>
                <td> Maximum device capacity limit in KB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > deviceState </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates device state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > logicalSectorSizeInBytes </td>
                <td> int </td>
                <td>success</td>
                <td> Logical sector size in bytes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > mediaFailing </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates media failing. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > writeCacheActive </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates write cache active. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > raidControllerSerialNumber </td>
                <td> str </td>
                <td>success</td>
                <td> RAID controller serial number. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > spSdsId </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates SPs SDS ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > accelerationPoolId </td>
                <td> str </td>
                <td>success</td>
                <td> Acceleration pool ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > accelerationProps </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates acceleration props. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > modelName </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates model name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > vendorName </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates vendor name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > persistentChecksumState </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates persistent checksum state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > capacityLimitInKb </td>
                <td> int </td>
                <td>success</td>
                <td> Device capacity limit in KB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > fglNvdimmWriteCacheSize </td>
                <td> int </td>
                <td>success</td>
                <td> Indicates FGL NVDIMM write cache size. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > links </td>
                <td> list </td>
                <td>success</td>
                <td> Device links. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > rel </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Relationship of device with different entities. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > href </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Device instance URL. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storagePoolId </td>
                <td> str </td>
                <td>success</td>
                <td> Storage Pool ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > protectionDomainName </td>
                <td> str </td>
                <td>success</td>
                <td> Protection domain name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > mediaType </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates media type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > rfcacheErrorDeviceDoesNotExist </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates RF cache error device does not exist. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > autoDetectMediaType </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates auto detection of media type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > temperatureState </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates temperature state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > externalAccelerationType </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates external acceleration type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > longSuccessfulIos </td>
                <td> list </td>
                <td>success</td>
                <td> Indicates long successful IOs. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > cacheLookAheadActive </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates cache look ahead active state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > ataSecurityActive </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates ATA security active state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > deviceOriginalPathName </td>
                <td> str </td>
                <td>success</td>
                <td> Device original path name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> Device ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > physicalSectorSizeInBytes </td>
                <td> int </td>
                <td>success</td>
                <td> Physical sector size in bytes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > rfcacheProps </td>
                <td> str </td>
                <td>success</td>
                <td> RF cache props. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > deviceCurrentPathName </td>
                <td> str </td>
                <td>success</td>
                <td> Device current path name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storageProps </td>
                <td> list </td>
                <td>success</td>
                <td> Storage props. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > accelerationPoolName </td>
                <td> str </td>
                <td>success</td>
                <td> Acceleration pool name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > ledSetting </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates LED setting. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > fglNvdimmMetadataAmortizationX100 </td>
                <td> int </td>
                <td>success</td>
                <td> Indicates FGL NVDIMM meta data amortization value. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > errorState </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates error state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sdsId </td>
                <td> str </td>
                <td>success</td>
                <td> SDS ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > firmwareVersion </td>
                <td> str </td>
                <td>success</td>
                <td> Indicates firmware version. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Snapshot Module

Manage Snapshots on Dell EMC PowerFlex

### Synopsis
 Managing snapshots on PowerFlex Storage System includes creating, getting details, mapping/unmapping to/from SDC, modifying the attributes and deleting snapshot.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=2 > sdc</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies SDC parameters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > sdc_id </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> ID of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip.  <br> Mutually exclusive with sdc_name and sdc_ip.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > sdc_name </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Name of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip.  <br> Mutually exclusive with sdc_id and sdc_ip.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > access_mode </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td> <ul> <li>READ_WRITE</li>  <li>READ_ONLY</li>  <li>NO_ACCESS</li> </ul></td>
                <td>  <br> Define the access mode for all mappings of the snapshot.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > iops_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit of snapshot IOPS.  <br> Minimum IOPS limit is 11 and specify 0 for unlimited iops.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > sdc_ip </td>
                <td> str  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> IP of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip.  <br> Mutually exclusive with sdc_id and sdc_ip.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > bandwidth_limit </td>
                <td> int  </td>
                <td></td>
                <td></td>
                <td></td>
                <td>  <br> Limit of snapshot network bandwidth.  <br> Need to mention in multiple of 1024 Kbps.  <br> To set no limit, 0 is to be passed.  </td>
            </tr>
                            <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=2 > read_only</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies whether mapping of the created snapshot volume will have read-write access or limited to read-only access.  <br> If true, snapshot is created with read-only access.  <br> If false, snapshot is created with read-write access. </td>
        </tr>
                    <tr>
            <td colspan=2 > desired_retention</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The retention value for the Snapshot.  <br> If the desired_retention is not mentioned during creation, snapshot will be created with unlimited retention.  <br> Maximum supported desired retention is 31 days. </td>
        </tr>
                    <tr>
            <td colspan=2 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the Snapshot. </td>
        </tr>
                    <tr>
            <td colspan=2 > allow_multiple_mappings</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Specifies whether to allow multiple mappings or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > sdc_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>mapped</li>  <li>unmapped</li> </ul></td>
            <td> <br> Mapping state of the SDC. </td>
        </tr>
                    <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the snapshot. Used to rename the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > retention_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>hours</li>  <li>days</li> </ul></td>
            <td> <br> The unit for retention. It defaults to 'hours', if not specified. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the snapshot.  <br> Mandatory for create operation.  <br> Specify either snapshot name or ID (but not both) for any operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > size</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The size of the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The ID of the volume. </td>
        </tr>
                    <tr>
            <td colspan=2 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume for which snapshot will be taken.  <br> Specify either vol_name or vol_id while creating snapshot. </td>
        </tr>
                    <tr>
            <td colspan=2 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> The unit of the volume size. It defaults to 'GB', if not specified.. </td>
        </tr>
                    <tr>
            <td colspan=2 > remove_mode</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>ONLY_ME</li>  <li>INCLUDING_DESCENDANTS</li> </ul></td>
            <td> <br> Removal mode for the snapshot.  <br> It defaults to 'ONLY_ME', if not specified. </td>
        </tr>
                                                                            </table>

### Notes
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Create snapshot
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_name: "ansible_snapshot"
    vol_name: "ansible_volume"
    read_only: False
    desired_retention: 2
    state: "present"

- name: Get snapshot details using snapshot id
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    state: "present"

- name: Map snapshot to SDC
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
        - sdc_ip: "198.10.xxx.xxx"
        - sdc_id: "663ac0d200000001"
    allow_multiple_mappings: True
    sdc_state: "mapped"
    state: "present"

- name: Modify the attributes of SDC mapped to snapshot
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
    - sdc_ip: "198.10.xxx.xxx"
      iops_limit: 11
      bandwidth_limit: 4096
    - sdc_id: "663ac0d200000001"
      iops_limit: 20
      bandwidth_limit: 2048
    allow_multiple_mappings: True
    sdc_state: "mapped"
    state: "present"

- name: Extend the size of snapshot
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    size: 16
    state: "present"

- name: Unmap SDCs from snapshot
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
      - sdc_ip: "198.10.xxx.xxx"
      - sdc_id: "663ac0d200000001"
    sdc_state: "unmapped"
    state: "present"

- name: Rename snapshot
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    snapshot_new_name: "ansible_renamed_snapshot_10"
    state: "present"

- name: Delete snapshot
  dellemc.powerflex.snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    remove_mode: "ONLY_ME"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=3 > snapshot_details </td>
            <td>  complex </td>
            <td> When snapshot exists </td>
            <td> Details of the snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > retentionInHours </td>
                <td> int </td>
                <td>success</td>
                <td> Retention of the snapshot in hours. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storagePoolName </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the Storage pool in which snapshot resides. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > ancestorVolumeId </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the root of the specified volume's V-Tree. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > secureSnapshotExpTime </td>
                <td> int </td>
                <td>success</td>
                <td> Expiry time of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sizeInGb </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > ancestorVolumeName </td>
                <td> str </td>
                <td>success</td>
                <td> The name of the root of the specified volume's V-Tree. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sizeInKb </td>
                <td> int </td>
                <td>success</td>
                <td> Size of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > mappedSdcInfo </td>
                <td> complex </td>
                <td>success</td>
                <td> The details of the mapped SDC. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > accessMode </td>
                    <td> str </td>
                    <td>success</td>
                    <td> mapping access mode for the specified snapshot. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > limitIops </td>
                    <td> int </td>
                    <td>success</td>
                    <td> IOPS limit for the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sdcId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> ID of the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > limitBwInMbps </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Bandwidth limit for the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sdcIp </td>
                    <td> str </td>
                    <td>success</td>
                    <td> IP of the SDC. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sdcName </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the SDC. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > creationTime </td>
                <td> int </td>
                <td>success</td>
                <td> The creation time of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storagePoolId </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the Storage pool in which snapshot resides. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Info Module

Gathering information about Dell EMC PowerFlex

### Synopsis
 Gathering information about Dell EMC PowerFlex storage system includes getting the api details, list of volumes, SDSs, SDCs, storage pools, protection domains, snapshot policies, and devices.

### Parameters
                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > gather_subset</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td> <ul> <li>vol</li>  <li>storage_pool</li>  <li>protection_domain</li>  <li>sdc</li>  <li>sds</li>  <li>snapshot_policy</li>  <li>device</li> </ul></td>
            <td> <br> List of string variables to specify the Powerflex storage system entities for which information is required.  <br> Volumes - vol.  <br> Storage pools - storage_pool.  <br> Protection domains - protection_domain.  <br> SDCs - sdc.  <br> SDSs - sds.  <br> Snapshot policies - snapshot_policy.  <br> Devices - device. </td>
        </tr>
                    <tr>
            <td colspan=2 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                    <tr>
            <td colspan=2 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > filters</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of filters to support filtered output for storage entities.  <br> Each filter is a list of filter_key, filter_operator, filter_value.  <br> Supports passing of multiple filters. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_operator </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td> <ul> <li>equal</li> </ul></td>
                <td>  <br> Operation to be performed on filter key.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_key </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Name identifier of the filter.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_value </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Value of the filter key.  </td>
            </tr>
                            <tr>
            <td colspan=2 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                                                                            </table>

### Notes
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
 - name: Get detailed list of PowerFlex entities
   dellemc.powerflex.info:
     gateway_host: "{{gateway_host}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - vol
       - storage_pool
       - protection_domain
       - sdc
       - sds
       - snapshot_policy
       - device

 - name: Get a subset list of PowerFlex volumes
   dellemc.powerflex.info:
     gateway_host: "{{gateway_host}}"
     username: "{{username}}"
     password: "{{password}}"
     verifycert: "{{verifycert}}"
     gather_subset:
       - vol
     filters:
       - filter_key: "name"
         filter_operator: "equal"
         filter_value: "ansible_test"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > API_Version </td>
            <td>  str </td>
            <td> always </td>
            <td> API version of PowerFlex API Gateway. </td>
        </tr>
                    <tr>
            <td colspan=2 > SDSs </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of storage data servers. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> storage data server name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> storage data server id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Volumes </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of volumes. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> volume name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> volume id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Devices </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of devices. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> device name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> device id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Snapshot_Policies </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of snapshot policies. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> snapshot policy name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> snapshot policy id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Storage_Pools </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of storage pools. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> storage pool name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> storage pool id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Protection_Domains </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of all protection domains. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> protection domain name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> protection domain id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SDCs </td>
            <td>  list </td>
            <td> always </td>
            <td> Details of storage data clients. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> storage data client name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> storage data client id. </td>
            </tr>
                                        <tr>
            <td colspan=2 > Array_Details </td>
            <td>  dict </td>
            <td> always </td>
            <td> System entities of PowerFlex storage array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > mdmExternalPort </td>
                <td> int </td>
                <td>success</td>
                <td> MDM external port. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > enterpriseFeaturesEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Enterprise eatures enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > mdmManagementPort </td>
                <td> int </td>
                <td>success</td>
                <td> MDM management port. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > swid </td>
                <td> str </td>
                <td>success</td>
                <td> SWID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > capacityTimeLeftInDays </td>
                <td> str </td>
                <td>success</td>
                <td> Capacity time left in days. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > installId </td>
                <td> str </td>
                <td>success</td>
                <td> installation Id. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > isInitialLicense </td>
                <td> bool </td>
                <td>success</td>
                <td> Initial license. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > capacityAlertCriticalThresholdPercent </td>
                <td> int </td>
                <td>success</td>
                <td> Capacity alert critical threshold percentage. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > mdmCluster </td>
                <td> dict </td>
                <td>success</td>
                <td> MDM cluster details. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > maxCapacityInGb </td>
                <td> dict </td>
                <td>success</td>
                <td> Maximum capacity in GB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > addressSpaceUsage </td>
                <td> str </td>
                <td>success</td>
                <td> Address space usage. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > showGuid </td>
                <td> bool </td>
                <td>success</td>
                <td> Show guid. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > capacityAlertHighThresholdPercent </td>
                <td> int </td>
                <td>success</td>
                <td> Capacity alert high threshold percentage. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > lastUpgradeTime </td>
                <td> int </td>
                <td>success</td>
                <td> Last upgrade time. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cliPasswordAllowed </td>
                <td> bool </td>
                <td>success</td>
                <td> CLI password allowed. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > daysInstalled </td>
                <td> int </td>
                <td>success</td>
                <td> Days installed. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > upgradeState </td>
                <td> str </td>
                <td>success</td>
                <td> Upgrade state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > systemVersionName </td>
                <td> str </td>
                <td>success</td>
                <td> System version and name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > managementClientSecureCommunicationEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Management client secure communication enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > defragmentationEnabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Defragmentation enabled. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > tlsVersion </td>
                <td> str </td>
                <td>success</td>
                <td> TLS version. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > mdmSecurityPolicy </td>
                <td> str </td>
                <td>success</td>
                <td> MDM security policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > authenticationMethod </td>
                <td> str </td>
                <td>success</td>
                <td> Authentication method. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# SDC Module

Manage SDCs on Dell EMC PowerFlex

### Synopsis
 Managing SDCs on PowerFlex storage system includes getting details of SDC and renaming SDC.

### Parameters
                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > sdc_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip for get/rename operation.  <br> Mutually exclusive with sdc_id and sdc_ip. </td>
        </tr>
                    <tr>
            <td colspan=1 > username</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > sdc_ip</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> IP of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip for get/rename operation.  <br> Mutually exclusive with sdc_id and sdc_name. </td>
        </tr>
                    <tr>
            <td colspan=1 > sdc_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> ID of the SDC.  <br> Specify either sdc_name, sdc_id or sdc_ip for get/rename operation.  <br> Mutually exclusive with sdc_name and sdc_ip. </td>
        </tr>
                    <tr>
            <td colspan=1 > gateway_host</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether or not to validate SSL certificate.  <br> True - Indicates that the SSL certificate should be verified.  <br> False - Indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> State of the SDC. </td>
        </tr>
                    <tr>
            <td colspan=1 > port</td>
            <td> int  </td>
            <td></td>
            <td> 443 </td>
            <td></td>
            <td> <br> Port number through which communication happens with PowerFlex gateway host. </td>
        </tr>
                    <tr>
            <td colspan=1 > sdc_new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the SDC. Used to rename the SDC. </td>
        </tr>
                    <tr>
            <td colspan=1 > timeout</td>
            <td> int  </td>
            <td></td>
            <td> 120 </td>
            <td></td>
            <td> <br> Time after which connection will get terminated.  <br> It is to be mentioned in seconds. </td>
        </tr>
                                                                            </table>

### Notes
* The check_mode is not supported.
* The modules present in the collection named as 'dellemc.powerflex' are built to support the Dell EMC PowerFlex storage platform.

### Examples
```
- name: Get SDC details using SDC ip
  dellemc.powerflex.sdc:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    sdc_ip: "{{sdc_ip}}"
    state: "present"

- name: Rename SDC using SDC name
  dellemc.powerflex.sdc:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    sdc_name: "centos_sdc"
    sdc_new_name: "centos_sdc_renamed"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=3 > sdc_details </td>
            <td>  complex </td>
            <td> When SDC exists </td>
            <td> Details of the SDC. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > osType </td>
                <td> str </td>
                <td>success</td>
                <td> OS type of the SDC. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the SDC. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > mapped_volumes </td>
                <td> list </td>
                <td>success</td>
                <td> The details of the mapped volumes. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > id </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The ID of the volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > volumeType </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Type of the volume. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> The name of the volume. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sdcApproved </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether an SDC has approved access to the system. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > id </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the SDC. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sdcIp </td>
                <td> str </td>
                <td>success</td>
                <td> IP of the SDC. </td>
            </tr>
                                        <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                            </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
