# powerflex_mdm

Role to manage the installation and uninstallation of Powerflex MDM.

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
    <td>powerflex_common_file_install_location</td>
    <td>true</td>
    <td>Location of installation and rpm gpg files to be installed.
    <br> The required, compatible installation software package based on the operating system of the node.
    <br> The files can be downloaded from the Dell Product support page for PowerFlex software.</td>
    <td></td>
    <td>str</td>
    <td>/var/tmp</td>
  </tr>
  <tr>
    <td>powerflex_mdm_password</td>
    <td>true</td>
    <td>Password for mdm cluster.<br></td>
    <td></td>
    <td>str</td>
    <td>Password123</td>
  </tr>
  <tr>
    <td>powerflex_mdm_state</td>
    <td>false</td>
    <td>Specify state of MDM.<br></td>
    <td>absent, present</td>
    <td>str</td>
    <td>present</td>
  </tr>
  <tr>
    <td>powerflex_mdm_virtual_ip</td>
    <td>false</td>
    <td>Virtual IP address of MDM.<br></td>
    <td></td>
    <td>str</td>
    <td></td>
  </tr>
</tbody>
</table>

## Examples
----
```
  - name: "Install and configure powerflex mdm"
    ansible.builtin.import_role:
      name: "powerflex_mdm"
    vars:
      powerflex_common_file_install_location: "/opt/scaleio/rpm"
      powerflex_mdm_password: password
      powerflex_mdm_state: present

  - name: "Uninstall powerflex mdm"
    ansible.builtin.import_role:
      name: "powerflex_mdm"
    vars:
      powerflex_mdm_state: absent

```

## Usage instructions
----
### To install all dependency packages, including mdm, on node:
  ```
  ansible-playbook -i inventory site.yml
  ```

### To uninstall mdm:
  ```
  ansible-playbook -i inventory uninstall_powerflex.yml
  ```

Sample playbooks and inventory can be found in the playbooks directory.

## Author Information
------------------

Dell Technologies
Bhavneet Sharma (ansible.team@Dell.com)  2023
