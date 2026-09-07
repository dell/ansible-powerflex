# powerflex_provisioning_v2

Role to provide Gen2 storage provisioning for Dell PowerFlex Ansible collection.

## Description

This role delivers volume lifecycle management, snapshot/thin-clone workflows,
storage pool and device group configuration, and device/storage-node provisioning
for PowerFlex 5.x Gen2 environments. It depends on `powerflex_common_v2` for
Gen2 compatibility detection.

## Requirements

- Ansible 2.14.0 or higher
- `dellemc.powerflex` collection with Gen2 modules (volume_v2, storagepool_v2, device_group, storage_node, snapshot_v2, thin_clone)
- PowerFlex 5.x (Gen2) system
- `powerflex_common_v2` role (must run first)

## Role Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `powerflex_gateway_hostname` | PowerFlex gateway hostname or IP | `""` | Yes |
| `powerflex_gateway_username` | PowerFlex gateway username | `""` | Yes |
| `powerflex_gateway_password` | PowerFlex gateway password | `""` | Yes |
| `powerflex_gateway_port` | PowerFlex gateway port | `443` | No |
| `powerflex_gateway_validate_certs` | Validate SSL certificates | `true` | No |
| `powerflex_gateway_timeout` | Request timeout in seconds | `30` | No |
| `powerflex_provisioning_v2_provision_volumes` | Enable volume provisioning | `true` | No |
| `powerflex_provisioning_v2_provision_snapshots` | Enable snapshot/thin-clone provisioning | `true` | No |
| `powerflex_provisioning_v2_provision_infrastructure` | Enable infrastructure provisioning | `true` | No |
| `powerflex_volume_name` | Volume name | `""` | Conditional |
| `powerflex_volume_size_gb` | Volume size in GB | `100` | Conditional |
| `powerflex_volume_storage_pool_name` | Storage pool name for volume | `""` | Conditional |
| `powerflex_snapshot_name` | Snapshot name | `""` | Conditional |
| `powerflex_snapshot_retention_days` | Snapshot retention period in days | `7` | Conditional |
| `powerflex_thin_clone_name` | Thin clone name | `""` | Conditional |
| `powerflex_storage_pool_name` | Storage pool name | `""` | Conditional |
| `powerflex_storage_pool_protection_scheme` | Erasure Coding protection scheme | `TwoPlusTwo` | Conditional |
| `powerflex_device_group_name` | Device group name | `""` | Conditional |
| `powerflex_device_group_protection_domain_name` | Protection domain for device group | `""` | Conditional |
| `powerflex_device_group_media_type` | Device group media type | `SSD` | Conditional |
| `powerflex_device_group_id` | Device group ID for device provisioning | `""` | Conditional |
| `powerflex_device_node_id` | Storage node ID for device provisioning | `""` | Conditional |

## Dependencies

- `dellemc.powerflex.powerflex_common_v2`

## Example Playbook

```yaml
---
- name: Provision PowerFlex Gen2 storage
  hosts: localhost
  gather_facts: false
  vars:
    powerflex_gateway_hostname: "192.168.1.100"
    powerflex_gateway_username: "admin"
    powerflex_gateway_password: "your_password"

  roles:
    - dellemc.powerflex.powerflex_common_v2
    - dellemc.powerflex.powerflex_provisioning_v2
```

## License

GPL-3.0-only

## Author Information

Dell Technologies
