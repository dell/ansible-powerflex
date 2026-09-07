# powerflex_common_v2

Role to provide Gen2 compatibility foundation for Dell PowerFlex Ansible collection.

## Description

This role delivers automatic Gen2 version detection, module compatibility validation,
and graceful degradation for Gen1 systems. It is a prerequisite for all Gen2-specific
roles (`powerflex_provisioning_v2`, `powerflex_system_v2`).

## Requirements

- Ansible 2.14.0 or higher
- `dellemc.powerflex` collection with Gen2 modules (volume_v2, storagepool_v2, device_group, storage_node)
- PowerFlex 5.x (Gen2) or 4.x (Gen1) system

## Role Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `powerflex_gateway_hostname` | PowerFlex gateway hostname or IP | `""` | Yes |
| `powerflex_gateway_username` | PowerFlex gateway username | `""` | Yes |
| `powerflex_gateway_password` | PowerFlex gateway password | `""` | Yes |
| `powerflex_gateway_port` | PowerFlex gateway port | `443` | No |
| `powerflex_gateway_validate_certs` | Validate SSL certificates | `true` | No |
| `powerflex_gateway_timeout` | Request timeout in seconds | `30` | No |
| `powerflex_version_cache_ttl` | Version detection cache TTL in seconds | `300` | No |

## Dependencies

None

## Example Playbook

```yaml
---
- name: Detect PowerFlex generation
  hosts: localhost
  gather_facts: false
  vars:
    powerflex_gateway_hostname: "192.168.1.100"
    powerflex_gateway_username: "admin"
    powerflex_gateway_password: "your_password"

  roles:
    - dellemc.powerflex.powerflex_common_v2
```

## Facts Set

- `powerflex_generation`: Set to `gen2` (API >= 5.0) or `gen1` (API < 5.0)
- `powerflex_gen2_skip`: Set to `true` on Gen1 systems (graceful degradation)

## License

GPL-3.0-only

## Author Information

Dell Technologies
