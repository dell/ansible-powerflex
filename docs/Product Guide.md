**Ansible Modules for Dell EMC PowerFlex** 
=========================================
### Product Guide 1.0

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
-------
- [Common access parameters](#common-access-parameters)

-   [Gatherfacts module](#gatherfacts-module)
    -   [Synopsis](#synopsis)
    -   [Parameters](#parameters)
    -   [Examples](#examples)
    -   [Return Values](#return-values)
    -   [Authors](#authors)
-   [SDC module](#sdc-module)
    -   [Synopsis](#synopsis-1)
    -   [Parameters](#parameters-1)
    -   [Examples](#examples-1)
    -   [Return Values](#return-values-1)
    -   [Authors](#authors-1)
-   [Volume module](#volume-module)
    -   [Synopsis](#synopsis-2)
    -   [Parameters](#parameters-2)
    -   [Examples](#examples-2)
    -   [Return Values](#return-values-2)
    -   [Authors](#authors-2)
-   [Snapshot module](#snapshot-module)
    -   [Synopsis](#synopsis-3)
    -   [Parameters](#parameters-3)
    -   [Examples](#examples-3)
    -   [Return Values](#return-values-3)
    -   [Authors](#authors-3)
-   [Storage pool module](#storage-pool-module)
    -   [Synopsis](#synopsis-4)
    -   [Parameters](#parameters-4)
    -   [Examples](#examples-4)
    -   [Return Values](#return-values-4)
    -   [Authors](#authors-4)

Common access parameters
==================================
These parameters are applicable to all modules, along with module-specific parameters.

**NOTE:** If the parameter is mandatory, then required=True else it is an optional parameter.
 This is applicable to all the module specific parameters also.
 
<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-gateway_host"></div>
                <b>gateway_host</b>
                <a class="ansibleOptionLink" href="#parameter-gateway_host" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                                              <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP or FQDN of the PowerFlex gateway host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-port"></div>
                <b>port</b>
                <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">443</div>
                                </td>
                                                            <td>
                                        <div>Port number through which communication happens with PowerFlex gateway host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-username"></div>
                <b>username</b>
                <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The username of the PowerFlex gateway host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-password"></div>
                <b>password</b>
                <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The password of the PowerFlex gateway host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-verifycert"></div>
                <b>verifycert</b>
                <a class="ansibleOptionLink" href="#parameter-verifycert" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable to specify whether or not to validate SSL certificate.</div>
                                        <div>True - Indicates that the SSL certificate should be verified.</div>
                                        <div>False - Indicates that the SSL certificate should not be verified.</div>
                                                    </td>
        </tr>
                    </table>
<br/>


Gather Facts Module
====================

## Synopsis

-   Gathering information about Dell EMC PowerFlex storage system
    includes Get the API details of a PowerFlex array, Get list of
    volumes in PowerFlex array, Get list of SDSs in a PowerFlex array,
    Get list of SDCs in a PowerFlex array, Get list of storage pools in
    PowerFlex array, Get list of protection domains in a PowerFlex
    array, Get list of snapshot policies in a PowerFlex array.

## Parameters

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-filters"></div>
                <b>filters</b>
                <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                     , <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of filters to support filtered output for storage entities.</div>
                                        <div>Each filter is a list of filter_key, filter_operator, filter_value.</div>
                                        <div>Supports passing of multiple filters.</div>
                                                    </td>
        </tr>
                                    <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filters/filter_key"></div>
                <b>filter_key</b>
                <a class="ansibleOptionLink" href="#parameter-filters/filter_key" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name identifier of the filter.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filters/filter_operator"></div>
                <b>filter_operator</b>
                <a class="ansibleOptionLink" href="#parameter-filters/filter_operator" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>equal</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Operation to be performed on filter key.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filters/filter_value"></div>
                <b>filter_value</b>
                <a class="ansibleOptionLink" href="#parameter-filters/filter_value" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Value of the filter key.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-gather_subset"></div>
                <b>gather_subset</b>
                <a class="ansibleOptionLink" href="#parameter-gather_subset" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                     , <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>vol</li>
                                                                                                                                                                                            <li>storage_pool</li>
                                                                                                                                                                                            <li>protection_domain</li>
                                                                                                                                                                                            <li>sdc</li>
                                                                                                                                                                                            <li>sds</li>
                                                                                                                                                                                            <li>snapshot_policy</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>List of string variables to specify the Powerflex storage system entities for which information is required.</div>
                                        <div>vol</div>
                                        <div>storage_pool</div>
                                        <div>protection_domain</div>
                                        <div>sdc</div>
                                        <div>sds</div>
                                        <div>snapshot_policy</div>
                                                    </td>
        </tr>
                    </table>
<br/>

## Examples

``` yaml+jinja
- name: Get detailed list of PowerFlex entities.
  dellemc_powerflex_gatherfacts:
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

- name: Get a subset list of PowerFlex volumes.
  dellemc_powerflex_gatherfacts:
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

## Return Values

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-API_Version"></div>
                <b>API_Version</b>
                <a class="ansibleOptionLink" href="#return-API_Version" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>API version of PowerFlex API Gateway.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Array_Details"></div>
                <b>Array_Details</b>
                <a class="ansibleOptionLink" href="#return-Array_Details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   , <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>System entities of PowerFlex storage array.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the system</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/installId"></div>
                <b>installId</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/installId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>installation Id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/mdmSecurityPolicy"></div>
                <b>mdmSecurityPolicy</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/mdmSecurityPolicy" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>mdm security policy</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Array_Details/systemVersionName"></div>
                <b>systemVersionName</b>
                <a class="ansibleOptionLink" href="#return-Array_Details/systemVersionName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>system version and name</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Protection_Domains"></div>
                <b>Protection_Domains</b>
                <a class="ansibleOptionLink" href="#return-Protection_Domains" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of all protection domains</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Protection_Domains/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Protection_Domains/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>protection domain id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Protection_Domains/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Protection_Domains/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>protection domain name</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-SDCs"></div>
                <b>SDCs</b>
                <a class="ansibleOptionLink" href="#return-SDCs" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of storage data clients</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SDCs/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-SDCs/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>storage data client id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SDCs/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-SDCs/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>storage data client name</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-SDSs"></div>
                <b>SDSs</b>
                <a class="ansibleOptionLink" href="#return-SDSs" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of storage data servers</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SDSs/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-SDSs/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>storage data server id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SDSs/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-SDSs/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>storage data server name</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Snapshot_Policies"></div>
                <b>Snapshot_Policies</b>
                <a class="ansibleOptionLink" href="#return-Snapshot_Policies" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of snapshot policies</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Snapshot_Policies/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Snapshot_Policies/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>snapshot policy id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Snapshot_Policies/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Snapshot_Policies/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>snapshot policy name</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Storage_Pools"></div>
                <b>Storage_Pools</b>
                <a class="ansibleOptionLink" href="#return-Storage_Pools" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of storage pools</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Storage_Pools/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Storage_Pools/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>storage pool id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Storage_Pools/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Storage_Pools/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>storage pool name</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Volumes"></div>
                <b>Volumes</b>
                <a class="ansibleOptionLink" href="#return-Volumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Details of volumes</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Volumes/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-Volumes/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>volume id</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Volumes/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Volumes/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>volume name</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

### Authors

-   Arindam Datta (@dattaarindam) &lt;<ansible.team@dell.com>&gt;


SDC Module
==============================================

## Synopsis

-   Managing SDC's on PowerFlex storage system includes getting details
    of SDC and renaming SDC.

## Parameters

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc_id"></div>
                <b>sdc_id</b>
                <a class="ansibleOptionLink" href="#parameter-sdc_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip for get/rename operation.</div>
                                        <div>Mutually exclusive with sdc_name and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc_ip"></div>
                <b>sdc_ip</b>
                <a class="ansibleOptionLink" href="#parameter-sdc_ip" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip for get/rename operation.</div>
                                        <div>Mutually exclusive with sdc_id and sdc_name.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc_name"></div>
                <b>sdc_name</b>
                <a class="ansibleOptionLink" href="#parameter-sdc_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip for get/rename operation.</div>
                                        <div>Mutually exclusive with sdc_id and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc_new_name"></div>
                <b>sdc_new_name</b>
                <a class="ansibleOptionLink" href="#parameter-sdc_new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name of the SDC. Used to rename the SDC.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the storage pool.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

## Examples

``` yaml+jinja
- name: Get SDC details using SDC ip
  dellemc_powerflex_sdc:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    sdc_ip: "{{sdc_ip}}"
    state: "present"

- name: Rename SDC using SDC name
  dellemc_powerflex_sdc:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    sdc_name: "centos_sdc"
    sdc_new_name: "centos_sdc_renamed"
    state: "present"
```

## Return Values


<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-sdc_details"></div>
                <b>sdc_details</b>
                <a class="ansibleOptionLink" href="#return-sdc_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When SDC exists</td>
            <td>
                                        <div>Details of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sdc_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sdc_details/mapped_volumes"></div>
                <b>mapped_volumes</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/mapped_volumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                   , <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The details of the mapped volumes</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-sdc_details/mapped_volumes/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/mapped_volumes/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-sdc_details/mapped_volumes/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/mapped_volumes/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The name of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-sdc_details/mapped_volumes/volumeType"></div>
                <b>volumeType</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/mapped_volumes/volumeType" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sdc_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sdc_details/osType"></div>
                <b>osType</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/osType" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>OS type of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sdc_details/sdcApproved"></div>
                <b>sdcApproved</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/sdcApproved" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether an SDC has approved access to the system</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sdc_details/sdcIp"></div>
                <b>sdcIp</b>
                <a class="ansibleOptionLink" href="#return-sdc_details/sdcIp" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>IP of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

### Authors

-   Akash Shendge (@shenda1) &lt;<ansible.team@dell.com>&gt;


Volume Module
==========================================

## Synopsis

-   Managing volumes on PowerFlex storage system includes creating new
    volume, getting details of volume, adding/removing snapshot policy
    to/from volume, mapping/unmapping volume to/from SDC, listing
    snapshots associated with a volume, modifying attributes of volume
    and deleting volume.

## Parameters

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-allow_multiple_mappings"></div>
                <b>allow_multiple_mappings</b>
                <a class="ansibleOptionLink" href="#parameter-allow_multiple_mappings" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Specifies whether to allow multiple mappings or not.</div>
                                        <div>If the volume is mapped to one SDC then for every new mapping allow_multiple_mappings has to be passed as True.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-auto_snap_remove_type"></div>
                <b>auto_snap_remove_type</b>
                <a class="ansibleOptionLink" href="#parameter-auto_snap_remove_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>remove</li>
                                                                                                                                                                                            <li>detach</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Whether to remove or detach the snapshot policy.</div>
                                        <div>To remove/detach snapshot policy, empty snapshot_policy_id/snapshot_policy_name is to be passed along with auto_snap_remove_type.</div>
                                        <div>If the snapshot policy name/id is passed empty then auto_snap_remove_type is defaulted to &#x27;detach&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-cap_unit"></div>
                <b>cap_unit</b>
                <a class="ansibleOptionLink" href="#parameter-cap_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>GB</li>
                                                                                                                                                                                            <li>TB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The unit of the volume size. It defaults to &#x27;GB&#x27;.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-compression_type"></div>
                <b>compression_type</b>
                <a class="ansibleOptionLink" href="#parameter-compression_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>NORMAL</li>
                                                                                                                                                                                            <li>NONE</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Type of the compression method.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-delete_snapshots"></div>
                <b>delete_snapshots</b>
                <a class="ansibleOptionLink" href="#parameter-delete_snapshots" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>If True, the volume and all its dependent snapshots will be deleted.</div>
                                        <div>If False, only the volume will be deleted.</div>
                                        <div>delete_snapshots parameter can be specified only when the state is absent.</div>
                                        <div>delete_snapshots defaults to False.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-protection_domain_id"></div>
                <b>protection_domain_id</b>
                <a class="ansibleOptionLink" href="#parameter-protection_domain_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the protection domain.</div>
                                        <div>While creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.</div>
                                        <div>protection_domain_name and protection_domain_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-protection_domain_name"></div>
                <b>protection_domain_name</b>
                <a class="ansibleOptionLink" href="#parameter-protection_domain_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the protection domain.</div>
                                        <div>While creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.</div>
                                        <div>protection_domain_name and protection_domain_name are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-sdc"></div>
                <b>sdc</b>
                <a class="ansibleOptionLink" href="#parameter-sdc" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                     , <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Specifies SDC parameters</div>
                                                    </td>
        </tr>
                                    <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/access_mode"></div>
                <b>access_mode</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/access_mode" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>READ_WRITE</li>
                                                                                                                                                                                            <li>READ_ONLY</li>
                                                                                                                                                                                            <li>NO_ACCESS</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define the access mode for all mappings of the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/bandwidth_limit"></div>
                <b>bandwidth_limit</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/bandwidth_limit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Limit of volume network bandwidth.</div>
                                        <div>Need to mention in multiple of 1024 Kbps.</div>
                                        <div>To set no limit, 0 is to be passed.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/iops_limit"></div>
                <b>iops_limit</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/iops_limit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Limit of volume IOPS.</div>
                                        <div>Minimum IOPS limit is 11 and specify 0 for unlimited iops.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/sdc_id"></div>
                <b>sdc_id</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/sdc_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip.</div>
                                        <div>Mutually exclusive with sdc_name and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/sdc_ip"></div>
                <b>sdc_ip</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/sdc_ip" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip.</div>
                                        <div>Mutually exclusive with sdc_id and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/sdc_name"></div>
                <b>sdc_name</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/sdc_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip.</div>
                                        <div>Mutually exclusive with sdc_id and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-sdc_state"></div>
                <b>sdc_state</b>
                <a class="ansibleOptionLink" href="#parameter-sdc_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>mapped</li>
                                                                                                                                                                                            <li>unmapped</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Mapping state of the SDC.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-size"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The size of the volume.</div>
                                        <div>Size of the volume will be assigned as higher multiple of 8 GB.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_policy_id"></div>
                <b>snapshot_policy_id</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_policy_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the snapshot policy.</div>
                                        <div>To remove/detach snapshot policy, empty snapshot_policy_id/snapshot_policy_name is to be passed along with auto_snap_remove_type.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_policy_name"></div>
                <b>snapshot_policy_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_policy_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the snapshot policy.</div>
                                        <div>To remove/detach snapshot policy, empty snapshot_policy_id/snapshot_policy_name is to be passed along with auto_snap_remove_type.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-storage_pool_id"></div>
                <b>storage_pool_id</b>
                <a class="ansibleOptionLink" href="#parameter-storage_pool_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the storage pool.</div>
                                        <div>Either name or the id of the storage pool is required for creating a volume.</div>
                                        <div>storage_pool_name and storage_pool_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-storage_pool_name"></div>
                <b>storage_pool_name</b>
                <a class="ansibleOptionLink" href="#parameter-storage_pool_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the storage pool.</div>
                                        <div>Either name or the id of the storage pool is required for creating a volume.</div>
                                        <div>During creation, If storage pool name is provided then either protection domain name or id must be mentioned along with it.</div>
                                        <div>storage_pool_name and storage_pool_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-use_rmcache"></div>
                <b>use_rmcache</b>
                <a class="ansibleOptionLink" href="#parameter-use_rmcache" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Whether to use RM Cache or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-vol_id"></div>
                <b>vol_id</b>
                <a class="ansibleOptionLink" href="#parameter-vol_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the volume.</div>
                                        <div>Except create operation, all other operations can be performed using vol_id.</div>
                                        <div>vol_name and vol_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-vol_name"></div>
                <b>vol_name</b>
                <a class="ansibleOptionLink" href="#parameter-vol_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the volume.</div>
                                        <div>Mandatory for create operation.</div>
                                        <div>vol_name is unique across the PowerFlex array.</div>
                                        <div>vol_name and vol_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-vol_new_name"></div>
                <b>vol_new_name</b>
                <a class="ansibleOptionLink" href="#parameter-vol_new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name of the volume. Used to rename the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-vol_type"></div>
                <b>vol_type</b>
                <a class="ansibleOptionLink" href="#parameter-vol_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>THICK_PROVISIONED</li>
                                                                                                                                                                                            <li>THIN_PROVISIONED</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The type of volume provisioning.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

## Examples

``` yaml+jinja
- name: Create a volume
  dellemc_powerflex_volume:
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
  dellemc_powerflex_volume:
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
  dellemc_powerflex_volume:
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
  dellemc_powerflex_volume:
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
      - sdc_ip: "127.0.0.1"
        access_mode: "READ_ONLY"
    allow_multiple_mappings: True
    sdc_state: "mapped"
    state: "present"

- name: Get the details of the volume
  dellemc_powerflex_volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_id: "fe6c8b7100000005"
    state: "present"

- name: Modify the details of the Volume
  dellemc_powerflex_volume:
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
  dellemc_powerflex_volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    delete_snapshots: False
    state: "absent"

- name: Delete the Volume and all its dependent snapshots
  dellemc_powerflex_volume:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    delete_snapshots: True
    state: "absent"
```

## Return Values

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-volume_details"></div>
                <b>volume_details</b>
                <a class="ansibleOptionLink" href="#return-volume_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When volume exists</td>
            <td>
                                        <div>Details of the volume</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-volume_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo"></div>
                <b>mappedSdcInfo</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The details of the mapped SDC</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo/accessMode"></div>
                <b>accessMode</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo/accessMode" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>mapping access mode for the specified volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo/limitBwInMbps"></div>
                <b>limitBwInMbps</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo/limitBwInMbps" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Bandwidth limit for the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo/limitIops"></div>
                <b>limitIops</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo/limitIops" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>IOPS limit for the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo/sdcId"></div>
                <b>sdcId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo/sdcId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo/sdcIp"></div>
                <b>sdcIp</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo/sdcIp" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>IP of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mappedSdcInfo/sdcName"></div>
                <b>sdcName</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mappedSdcInfo/sdcName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-volume_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the volume</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/protectionDomainId"></div>
                <b>protectionDomainId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/protectionDomainId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the protection domain in which volume resides.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/protectionDomainName"></div>
                <b>protectionDomainName</b>
                <a class="ansibleOptionLink" href="#return-volume_details/protectionDomainName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the protection domain in which volume resides.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/sizeInGb"></div>
                <b>sizeInGb</b>
                <a class="ansibleOptionLink" href="#return-volume_details/sizeInGb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of the volume in Gb.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/sizeInKb"></div>
                <b>sizeInKb</b>
                <a class="ansibleOptionLink" href="#return-volume_details/sizeInKb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of the volume in Kb.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/snapshotPolicyId"></div>
                <b>snapshotPolicyId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/snapshotPolicyId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the snapshot policy associated with volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/snapshotPolicyName"></div>
                <b>snapshotPolicyName</b>
                <a class="ansibleOptionLink" href="#return-volume_details/snapshotPolicyName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the snapshot policy associated with volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/snapshotsList"></div>
                <b>snapshotsList</b>
                <a class="ansibleOptionLink" href="#return-volume_details/snapshotsList" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of snapshots associated with the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/storagePoolId"></div>
                <b>storagePoolId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/storagePoolId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the storage pool in which volume resides.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details/storagePoolName"></div>
                <b>storagePoolName</b>
                <a class="ansibleOptionLink" href="#return-volume_details/storagePoolName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the storage pool in which volume resides.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

### Authors

-   P Srinivas Rao (@srinivas-rao5) &lt;<ansible.team@dell.com>&gt;

# Snapshot Module

## Synopsis

-   Managing snapshots on PowerFlex Storage System includes creating new
    snapshot, getting details of snapshot, mapping/unmapping snapshot
    to/from SDC, modifying attributes of snapshot and deleting snapshot.

## Parameters

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-allow_multiple_mappings"></div>
                <b>allow_multiple_mappings</b>
                <a class="ansibleOptionLink" href="#parameter-allow_multiple_mappings" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Specifies whether to allow multiple mappings or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-cap_unit"></div>
                <b>cap_unit</b>
                <a class="ansibleOptionLink" href="#parameter-cap_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>GB</li>
                                                                                                                                                                                            <li>TB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The unit of the volume size. It defaults to &#x27;GB&#x27;, if not specified.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-desired_retention"></div>
                <b>desired_retention</b>
                <a class="ansibleOptionLink" href="#parameter-desired_retention" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The retention value for the Snapshot.</div>
                                        <div>If the desired_retention is not mentioned during creation, snapshot will be created with unlimited retention.</div>
                                        <div>Maximum supported desired retention is 31 days.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-read_only"></div>
                <b>read_only</b>
                <a class="ansibleOptionLink" href="#parameter-read_only" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Specifies whether mapping of the created snapshot volume will have read-write access or limited to read-only access.</div>
                                        <div>If true, snapshot is created with read-only access.</div>
                                        <div>If false, snapshot is created with read-write access.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-remove_mode"></div>
                <b>remove_mode</b>
                <a class="ansibleOptionLink" href="#parameter-remove_mode" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>ONLY_ME</li>
                                                                                                                                                                                            <li>INCLUDING_DESCENDANTS</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Removal mode for the snapshot.</div>
                                        <div>It defaults to &#x27;ONLY_ME&#x27;, if not specified.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-retention_unit"></div>
                <b>retention_unit</b>
                <a class="ansibleOptionLink" href="#parameter-retention_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>hours</li>
                                                                                                                                                                                            <li>days</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The unit for retention. It defaults to &#x27;hours&#x27;, if not specified.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-sdc"></div>
                <b>sdc</b>
                <a class="ansibleOptionLink" href="#parameter-sdc" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                     , <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Specifies SDC parameters</div>
                                                    </td>
        </tr>
                                    <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/access_mode"></div>
                <b>access_mode</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/access_mode" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>READ_WRITE</li>
                                                                                                                                                                                            <li>READ_ONLY</li>
                                                                                                                                                                                            <li>NO_ACCESS</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define the access mode for all mappings of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/bandwidth_limit"></div>
                <b>bandwidth_limit</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/bandwidth_limit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Limit of snapshot network bandwidth.</div>
                                        <div>Need to mention in multiple of 1024 Kbps.</div>
                                        <div>To set no limit, 0 is to be passed.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/iops_limit"></div>
                <b>iops_limit</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/iops_limit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Limit of snapshot IOPS.</div>
                                        <div>Minimum IOPS limit is 11 and specify 0 for unlimited iops.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/sdc_id"></div>
                <b>sdc_id</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/sdc_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>ID of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip.</div>
                                        <div>Mutually exclusive with sdc_name and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/sdc_ip"></div>
                <b>sdc_ip</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/sdc_ip" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip.</div>
                                        <div>Mutually exclusive with sdc_id and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sdc/sdc_name"></div>
                <b>sdc_name</b>
                <a class="ansibleOptionLink" href="#parameter-sdc/sdc_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the SDC.</div>
                                        <div>Specify either sdc_name, sdc_id or sdc_ip.</div>
                                        <div>Mutually exclusive with sdc_id and sdc_ip.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-sdc_state"></div>
                <b>sdc_state</b>
                <a class="ansibleOptionLink" href="#parameter-sdc_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>mapped</li>
                                                                                                                                                                                            <li>unmapped</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Mapping state of the SDC.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-size"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The size of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
                <b>snapshot_id</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the Snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the snapshot.</div>
                                        <div>Mandatory for create operation.</div>
                                        <div>Specify either snapshot name or ID (but not both) for any operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_new_name"></div>
                <b>snapshot_new_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name of the snapshot. Used to rename the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-vol_id"></div>
                <b>vol_id</b>
                <a class="ansibleOptionLink" href="#parameter-vol_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The ID of the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-vol_name"></div>
                <b>vol_name</b>
                <a class="ansibleOptionLink" href="#parameter-vol_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the volume for which snapshot will be taken.</div>
                                        <div>Specify either vol_name or vol_id while creating snapshot.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

## Examples

``` yaml+jinja
- name: Create snapshot
  dellemc_powerflex_snapshot:
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
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    state: "present"

- name: Map snapshot to SDC
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
        - sdc_ip: "10.247.66.203"
        - sdc_id: "663ac0d200000001"
    allow_multiple_mappings: True
    sdc_state: "mapped"
    state: "present"

- name: Modify the attributes of SDC mapped to snapshot
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
    - sdc_ip: "10.247.66.203"
      iops_limit: 11
      bandwidth_limit: 4096
    - sdc_id: "663ac0d200000001"
      iops_limit: 20
      bandwidth_limit: 2048
    allow_multiple_mappings: True
    sdc_state: "mapped"
    state: "present"

- name: Extend the size of snapshot
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    size: 16
    state: "present"

- name: Unmap SDCs from snapshot
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
      - sdc_ip: "10.247.66.203"
      - sdc_id: "663ac0d200000001"
    sdc_state: "unmapped"
    state: "present"

- name: Rename snapshot
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    snapshot_new_name: "ansible_renamed_snapshot_10"
    state: "present"

- name: Delete snapshot
  dellemc_powerflex_snapshot:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    snapshot_id: "fe6cb28200000007"
    remove_mode: "ONLY_ME"
    state: "absent"
```

## Return Values

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-snapshot_details"></div>
                <b>snapshot_details</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When snapshot exists</td>
            <td>
                                        <div>Details of the snapshot</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/ancestorVolumeId"></div>
                <b>ancestorVolumeId</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/ancestorVolumeId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The of the root of the specified volume&#x27;s V-Tree</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/creationTime"></div>
                <b>creationTime</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/creationTime" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The creation time of the snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The ID of the snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo"></div>
                <b>mappedSdcInfo</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The details of the mapped SDC</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo/accessMode"></div>
                <b>accessMode</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo/accessMode" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>mapping access mode for the specified snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo/limitBwInMbps"></div>
                <b>limitBwInMbps</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo/limitBwInMbps" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Bandwidth limit for the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo/limitIops"></div>
                <b>limitIops</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo/limitIops" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>IOPS limit for the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo/sdcId"></div>
                <b>sdcId</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo/sdcId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo/sdcIp"></div>
                <b>sdcIp</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo/sdcIp" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>IP of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/mappedSdcInfo/sdcName"></div>
                <b>sdcName</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/mappedSdcInfo/sdcName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the SDC</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/sizeInKb"></div>
                <b>sizeInKb</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/sizeInKb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of the snapshot</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-snapshot_details/storagePoolId"></div>
                <b>storagePoolId</b>
                <a class="ansibleOptionLink" href="#return-snapshot_details/storagePoolId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Storage pool in which snapshot resides</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

### Authors

-   Akash Shendge (@shenda1) &lt;<ansible.team@dell.com>&gt;

# Storage Pool Module

## Synopsis

-   Dell EMC PowerFlex storage pool module includes Get the details of
    storage pool, Create a new storage pool, Modify the attribute of a
    storage pool.

## Parameters

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-media_type"></div>
                <b>media_type</b>
                <a class="ansibleOptionLink" href="#parameter-media_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>HDD</li>
                                                                                                                                                                                            <li>SSD</li>
                                                                                                                                                                                            <li>TRANSITIONAL</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Type of devices in the storage pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-protection_domain_id"></div>
                <b>protection_domain_id</b>
                <a class="ansibleOptionLink" href="#parameter-protection_domain_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the protection domain.</div>
                                        <div>While creation of a pool, either protection domain name or id must be mentioned.</div>
                                        <div>protection_domain_name and protection_domain_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-protection_domain_name"></div>
                <b>protection_domain_name</b>
                <a class="ansibleOptionLink" href="#parameter-protection_domain_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the protection domain.</div>
                                        <div>While creation of a pool, either protection domain name or id must be mentioned.</div>
                                        <div>protection_domain_name and protection_domain_name are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                             , <span style="color: red">required=True</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the storage pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-storage_pool_id"></div>
                <b>storage_pool_id</b>
                <a class="ansibleOptionLink" href="#parameter-storage_pool_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The id of the storage pool.</div>
                                        <div>storage_pool_id is auto generated, hence should not be provided during creation of a storage pool.</div>
                                        <div>storage_pool_name and storage_pool_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-storage_pool_name"></div>
                <b>storage_pool_name</b>
                <a class="ansibleOptionLink" href="#parameter-storage_pool_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the storage pool.</div>
                                        <div>If more than one storage pool is found with the same name then protection domain id/name is required to perform the task.</div>
                                        <div>storage_pool_name and storage_pool_id are mutually exclusive parameters.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-storage_pool_new_name"></div>
                <b>storage_pool_new_name</b>
                <a class="ansibleOptionLink" href="#parameter-storage_pool_new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name for the storage pool can be provided.</div>
                                        <div>This parameter is used for renaming the storage pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-use_rfcache"></div>
                <b>use_rfcache</b>
                <a class="ansibleOptionLink" href="#parameter-use_rfcache" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Enable/Disable RFcache on a specific storage pool.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-use_rmcache"></div>
                <b>use_rmcache</b>
                <a class="ansibleOptionLink" href="#parameter-use_rmcache" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Enable/Disable RMcache on a specific storage pool.</div>
                                                    </td>
        </tr>
                    </table>
<br/>

## Notes

<div class="note">

<div class="title">

</div>

- TRANSITIONAL media type is supported only during modification.
- The modules prefixed with dellemc\_powerflex are built to support the Dell
EMC PowerFlex storage platform.

</div>

## Examples

``` yaml+jinja
- name: Get the details of storage pool by name
  dellemc_powerflex_storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_name: "sample_pool_name"
    protection_domain_name: "sample_protection_domain"
    state: "present"

- name: Get the details of storage pool by id
  dellemc_powerflex_storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_id: "abcd1234ab12r"
    state: "present"

- name: Create a new storage pool by name
  dellemc_powerflex_storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_name: "ansible_test_pool"
    protection_domain_id: "1c957da800000000"
    media_type: "HDD"
    state: "present"

- name: Modify a storage pool by name
  dellemc_powerflex_storagepool:
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
  dellemc_powerflex_storagepool:
    gateway_host: "{{gateway_host}}"
    username: "{{username}}"
    password: "{{password}}"
    verifycert: "{{verifycert}}"
    storage_pool_id: "abcd1234ab12r"
    storage_pool_new_name: "new_ansible_pool"
    state: "present"
```

## Return Values


<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details"></div>
                <b>storage_pool_details</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When storage pool exists</td>
            <td>
                                        <div>Details of the storage pool</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/id"></div>
                <b>id</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/id" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the storage pool under protection domain.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/mediaType"></div>
                <b>mediaType</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/mediaType" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of devices in the storage pool</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the storage pool under protection domain.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/protectionDomainId"></div>
                <b>protectionDomainId</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/protectionDomainId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the protection domain in which pool resides.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/protectionDomainName"></div>
                <b>protectionDomainName</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/protectionDomainName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the protection domain in which pool resides.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/useRfcache"></div>
                <b>useRfcache</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/useRfcache" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Enable/Disable RFcache on a specific storage pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_pool_details/useRmcache"></div>
                <b>useRmcache</b>
                <a class="ansibleOptionLink" href="#return-storage_pool_details/useRmcache" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Enable/Disable RMcache on a specific storage pool.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>
<br/><br/>

### Authors

-   Arindam Datta (@dattaarindam) &lt;<ansible.team@dell.com>&gt;
-   P Srinivas Rao (@srinivas-rao5) &lt;<ansible.team@dell.com>&gt;
