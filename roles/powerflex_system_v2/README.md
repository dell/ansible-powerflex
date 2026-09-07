# powerflex_system_v2

Gen2 system information, configuration validation, and diagnostics role for Dell PowerFlex 5.x environments.

## Requirements

- PowerFlex 5.x (Gen2) with API version >= 5.0
- `dellemc.powerflex` collection >= 3.1.0
- `PyPowerFlex` >= 2.0.0

## Role Variables

See `defaults/main.yml` for the full list. Key variables:

### Connection Parameters

| Variable | Default | Description |
|----------|---------|-------------|
| `powerflex_gateway_hostname` | `""` | PowerFlex gateway IP/hostname |
| `powerflex_gateway_username` | (required) | Gateway username |
| `powerflex_gateway_password` | (required) | Gateway password |
| `powerflex_gateway_port` | `443` | Gateway port |
| `powerflex_gateway_validate_certs` | `true` | Validate SSL certificates |

### Feature Flags

| Variable | Default | Description |
|----------|---------|-------------|
| `powerflex_system_query` | `true` | Run system information queries |
| `powerflex_system_validate` | `false` | Run configuration validation |
| `powerflex_system_diagnostics` | `false` | Run system diagnostics |

### Query Filters

Set entity name or ID variables to query specific resources (e.g., `powerflex_query_volume_name`).

### Validation Targets

Enable specific validation targets: `powerflex_validate_mdm_cluster`, `powerflex_validate_protection_domains`, `powerflex_validate_storage_pools`, `powerflex_validate_volumes`.

### Diagnostics Targets

Enable specific reports: `powerflex_diag_system_health`, `powerflex_diag_capacity_report`, `powerflex_diag_snapshot_report`.

## Dependencies

- `dellemc.powerflex.powerflex_common_v2`

## Example Playbook

```yaml
- name: Query Gen2 system information
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Run common role
      ansible.builtin.include_role:
        name: powerflex_common_v2

    - name: Run system queries
      ansible.builtin.include_role:
        name: powerflex_system_v2
      vars:
        powerflex_system_query: true
        powerflex_system_gather_subset:
          - vol
          - protection_domain
          - storage_pool
```

## License

GPL-3.0-only

## Author Information

Dell Technologies — Ansible Team
