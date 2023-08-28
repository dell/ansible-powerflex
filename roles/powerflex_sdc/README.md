# powerflex_sdc

Role to manage the installation and uninstallation of Powerflex SDC.

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
    <td>IP or FQDN of the PowerFlex gateway</td>
    <td></td>
    <td>str</td>
    <td>10.1.1.1</td>
  </tr>
  <tr>
    <td>username</td>
    <td>true</td>
    <td>The username of the PowerFlex gateway</td>
    <td></td>
    <td>str</td>
    <td>admin</td>
  </tr>
  <tr>
    <td>password</td>
    <td>true</td>
    <td>The password of the PowerFlex gateway</td>
    <td></td>
    <td>str</td>
    <td>password</td>
  </tr>
  <tr>
    <td>port</td>
    <td>false</td>
    <td>Port</td>
    <td></td>
    <td>int</td>
    <td>443</td>
  </tr>
  <tr>
    <td>validate_certs</td>
    <td>false</td>
    <td>If C(false), the SSL certificates will not be validated.<br>Configure C(false) only on personally controlled sites where self-signed certificates are used</td>
    <td></td>
    <td>bool</td>
    <td>false</td>
  </tr>
  <tr>
    <td>timeout</td>
    <td>false</td>
    <td>Timeout</td>
    <td></td>
    <td>int</td>
    <td>120</td>
  </tr>
  <tr>
    <td>powerflex_common_file_install_location</td>
    <td>true</td>
    <td>Location of installation and rpm gpg files to be installed.
    <br>The required, compatible installation software package based on the operating system of the node.
    <br>The files can be downloaded from the Dell Product support page for PowerFlex software.</td>
    <td></td>
    <td>str</td>
    <td>/var/tmp</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_repo_address</td>
    <td>false</td>
    <td>Repository address for the kernel modules</td>
    <td></td>
    <td>str</td>
    <td>ftp://ftp.emc.com/</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_repo_user</td>
    <td>false</td>
    <td>Username for the repository</td>
    <td></td>
    <td>str</td>
    <td>QNzgdxXix</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_repo_password</td>
    <td>false</td>
    <td>Password for the repository</td>
    <td></td>
    <td>str</td>
    <td>Aw3wFAwAq3</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_repo_local_dir</td>
    <td>false</td>
    <td>Local cache of the repository</td>
    <td></td>
    <td>str</td>
    <td>/bin/emc/scaleio/scini_sync/driver_cache/</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_user_private_rsa_key_src</td>
    <td>false</td>
    <td>Private ssh RSA key source (if using sftp protocol)</td>
    <td></td>
    <td>str</td>
    <td></td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_user_private_rsa_key_dest</td>
    <td>false</td>
    <td>Private ssh RSA key destination</td>
    <td></td>
    <td>str</td>
    <td>/bin/emc/scaleio/scini_sync/scini_key</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_repo_public_rsa_key_src</td>
    <td>false</td>
    <td>Public ssh USA key source (if using sftp protocol)</td>
    <td></td>
    <td>str</td>
    <td></td>
    </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_repo_public_rsa_key_dest</td>
    <td>false</td>
    <td>Private ssh RSA key destination</td>
    <td></td>
    <td>str</td>
    <td>/bin/emc/scaleio/scini_sync/scini_repo_key.pub</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_module_sigcheck</td>
    <td>false</td>
    <td>If signature check is required</td>
    <td></td>
    <td>str</td>
    <td>1</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_emc_public_gpg_key_src</td>
    <td>false</td>
    <td>Location of the signature file</td>
    <td></td>
    <td>str</td>
    <td>{{ powerflex_common_file_install_location }}/files/RPM-GPG-KEY-ScaleIO_2.0.*.0</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_emc_public_gpg_key_dest</td>
    <td>false</td>
    <td>Destination of the signature file</td>
    <td></td>
    <td>str</td>
    <td>/bin/emc/scaleio/scini_sync/emc_key.pub</td>
  </tr>
  <tr>
    <td>powerflex_sdc_driver_sync_sync_pattern</td>
    <td>false</td>
    <td>Repo sync pattern</td>
    <td></td>
    <td>str</td>
    <td>.*</td>
  </tr>
  <tr>
    <td>powerflex_sdc_name</td>
    <td>false</td>
    <td>Name of SDC to rename to<br></td>
    <td></td>
    <td>str</td>
    <td>sdc_test</td>
  </tr>
  <tr>
    <td>powerflex_sdc_performance_profile</td>
    <td>false</td>
    <td>Performance profile of SDC<br></td>
    <td></td>
    <td>str</td>
    <td>Compact</td>
  </tr>
  <tr>
    <td>powerflex_sdc_state</td>
    <td>false</td>
    <td>Specify state of SDC<br></td>
    <td>absent, present</td>
    <td>str</td>
    <td>present</td>
  </tr>
</tbody>
</table>

## Examples
----
```
  - name: Install and configure powerflex SDC
    ansible.builtin.import_role:
      name: powerflex_sdc
    vars:
      hostname: "{{ hostname }}"
      username: "{{ username }}"
      password: "{{ password }}"
      validate_certs: "{{ validate_certs }}"
      port: "{{ port }}"
      powerflex_common_file_install_location: "/opt/scaleio/rpm"
      powerflex_sdc_name: sdc_test
      powerflex_sdc_performance_profile: Compact
      powerflex_sdc_state: present

  - name: Uninstall powerflex SDC
    ansible.builtin.import_role:
      name: powerflex_sdc
    vars:
      hostname: "{{ hostname }}"
      username: "{{ username }}"
      password: "{{ password }}"
      validate_certs: "{{ validate_certs }}"
      port: "{{ port }}"
      powerflex_sdc_state: absent

```

## Usage instructions
----
### To install all dependency packages, including SDC, on node:
  ansible-playbook -i inventory site.yml

### To uninstall SDC:
  ansible-playbook -i inventory uninstall_powerflex.yml

Sample playbooks and inventory can be found in the playbooks directory.

## Author Information
------------------

Dell Technologies
Jennifer John (ansible.team@Dell.com)  2023
