# powerflex_tb

Role to manage the installation and uninstallation of Powerflex TB.

## Requirements

```
ansible
python
```

## Ansible collections

Collections required to use the role.

```
dellemc.powerflex
```

## Role Variables

<table>
<thead>
  <tr>
    <th>Name</th>
    <th>Required</th>
    <th>Description</th>
    <th>Choices</th>
    <th>Type</th>
    <th>Default Value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>hostname</td>
    <td>true</td>
    <td>IP or FQDN of the PowerFlex gateway.</td>
    <td></td>
    <td>str</td>
    <td></td>
  </tr>
  <tr>
    <td>username</td>
    <td>true</td>
    <td>The username of the PowerFlex gateway.</td>
    <td></td>
    <td>str</td>
    <td></td>
  </tr>
  <tr>
    <td>password</td>
    <td>true</td>
    <td>The password of the PowerFlex gateway.</td>
    <td></td>
    <td>str</td>
    <td></td>
  </tr>
  <tr>
    <td>port</td>
    <td>false</td>
    <td>Port of the PowerFlex gateway.</td>
    <td></td>
    <td>int</td>
    <td>443</td>
  </tr>
  <tr>
    <td>validate_certs</td>
    <td>false</td>
    <td>If C(false), the SSL certificates will not be validated.<br>Configure C(false) only on personally controlled sites where self-signed certificates are used.</td>
    <td></td>
    <td>bool</td>
    <td>false</td>
  </tr>
  <tr>
    <td>timeout</td>
    <td>false</td>
    <td>Timeout.</td>
    <td></td>
    <td>int</td>
    <td>120</td>
  </tr>
  <tr>
    <td>powerflex_common_file_install_location</td>
    <td>true</td>
    <td>Location of installation and rpm gpg files to be installed.
    <br>The required, compatible installation software package based on the operating system of the node.
    <br> The files can be downloaded from the Dell Product support page for PowerFlex software.</td>
    <td></td>
    <td>str</td>
    <td>/var/tmp</td>
  </tr>
  <tr>
    <td>powerflex_tb_state</td>
    <td>false</td>
    <td>Specify state of TB.<br></td>
    <td>absent, present</td>
    <td>str</td>
    <td>present</td>
  </tr>
  <tr>
    <td>powerflex_tb_primary_name</td>
    <td>true</td>
    <td>Name of the primary TB.<br></td>
    <td></td>
    <td>str</td>
    <td>primary_tb</td>
  </tr>
  <tr>
    <td>powerflex_tb_secondary_name</td>
    <td>false</td>
    <td>Name of the secondary TB.<br></td>
    <td></td>
    <td>str</td>
    <td>secondary_tb</td>
  </tr>
  <tr>
    <td>powerflex_tb_cluster_mode</td>
    <td>true</td>
    <td>Mode of the cluster.<br></td>
    <td>ThreeNodes, FiveNodes</td>
    <td>str</td>
    <td>ThreeNodes</td>
  </tr>
  <tr>
    <td>powerflex_protection_domain_name</td>
    <td>false</td>
    <td>Name of the protection domain.<br></td>
    <td></td>
    <td>str</td>
    <td>tb_protection_domain</td>
  </tr>
  <tr>
    <td>powerflex_fault_sets</td>
    <td>false</td>
    <td>List of fault sets.<br></td>
    <td></td>
    <td>list</td>
    <td>['fs1','fs2','fs3']</td>
  </tr>
  <tr>
    <td>powerflex_media_type</td>
    <td>false</td>
    <td>Media type of the storage pool.<br></td>
    <td>'SSD', 'HDD', 'TRANSITIONAL'</td>
    <td>str</td>
    <td>SSD</td>>
  </tr>
  <tr>
    <td>powerflex_storage_pool_name</td>
    <td>false</td>
    <td>Name of the storage pool.<br></td>
    <td></td>
    <td>str</td>
    <td>tb_storage_pool</td>
  </tr>
</tbody>
</table>

## Examples
----
```
  - name: Install and configure PowerFlex TB
    ansible.builtin.import_role:
      name: "powerflex_tb"
    vars:
      hostname: "{{ hostname }}"
      username: "{{ username }}"
      password: "{{ password }}"
      validate_certs: "{{ validate_certs }}"
      port: "{{ port }}"
      powerflex_tb_primary_name: "primary_tb"
      powerflex_tb_secondary_name: "secondary_tb"
      powerflex_tb_cluster_mode: "ThreeNodes"
      powerflex_protection_domain_name: "tb_protection_domain"
      powerflex_fault_sets:
        - 'fs1'
        - 'fs2'
        - 'fs3'
      powerflex_media_type: 'SSD'
      powerflex_storage_pool_name: "tb_storage_pool"
      powerflex_common_file_install_location: "/var/tmp"
      powerflex_tb_state: present

  - name: Uninstall powerflex TB
    ansible.builtin.import_role:
      name: "powerflex_tb"
    vars:
      hostname: "{{ hostname }}"
      username: "{{ username }}"
      password: "{{ password }}"
      validate_certs: "{{ validate_certs }}"
      port: "{{ port }}"
      powerflex_tb_state: 'absent'

```

## Usage instructions
----
### To install all dependency packages, including TB, on node:
  ansible-playbook -i inventory site.yml

### To uninstall TB:
  ansible-playbook -i inventory uninstall_powerflex.yml

Sample playbooks and inventory can be found in the playbooks directory.

## Notes
----

- As a pre-requisite, the Gateway must be installed.
- TRANSITIONAL media type is supported only during modification.

## Author Information
------------------

Dell Technologies
Ananthu S Kuttattu (ansible.team@Dell.com)  2023
