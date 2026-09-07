# Tundra Testing Guide for Gen2 Roles

This guide explains how to test the new `powerflex_common_v2` and `powerflex_provisioning_v2` roles against the Tundra lab environment.

## Tundra Lab Environment

- **Gateway:** 10.247.39.78
- **PFMP Version:** 5.1
- **Core Version:** 5.1
- **API Version:** 5.x (Gen2)

## Prerequisites

1. **Network Access:** Ensure you have network connectivity to 10.247.39.78 from your development machine.
2. **Credentials:** Obtain the Tundra admin password from the lab team or vault.
3. **Ansible Collection:** Install the collection with the new roles:
   ```bash
   cd src/ansible/ansible-powerflex
   ansible-galaxy collection build --force
   ansible-galaxy collection install dellemc-powerflex-*.tar.gz --force
   ```

## Setup

1. **Configure environment variables:**
   ```bash
   cp env_tundra.yml env.yml
   # Edit env.yml and set the actual password
   vi env.yml
   ```

2. **Or use Ansible Vault (recommended):**
   ```bash
   # Create vault password file
   echo "your_vault_password" > .vault_pass

   # Encrypt the password
   ansible-vault encrypt_string "actual_tundra_password" --vault-id @.vault_pass

   # Update env_tundra.yml with the encrypted string
   ```

## Running Tests

### Test 1: powerflex_common_v2 (Gen2 Detection)

```bash
cd src/ansible/ansible-powerflex
ansible-playbook playbooks/roles/powerflex_common_v2_tundra.yml --extra-vars @env.yml
```

**Expected Output:**
- `powerflex_generation: gen2`
- `API_Version: 5.x`
- All assertions pass

### Test 2: powerflex_provisioning_v2 (Full Provisioning)

```bash
cd src/ansible/ansible-powerflex
ansible-playbook playbooks/roles/powerflex_provisioning_v2_tundra.yml --extra-vars @env.yml
```

**Expected Output:**
- Volume created successfully
- Snapshot created successfully
- Storage pool created with Erasure Coding
- Device group created successfully
- All assertions pass

## Cleanup

After testing, manually delete the test resources from Tundra:

1. **Delete test volume:** `ansible_test_vol`
2. **Delete test snapshot:** `ansible_test_snap`
3. **Delete test storage pool:** `ansible_test_pool`
4. **Delete test device group:** `ansible_test_dg`

Or use the PowerFlex GUI to delete these resources.

## Troubleshooting

### Connection Refused
- Verify network connectivity to 10.247.39.78
- Check if the Tundra lab is available (contact lab team)

### Authentication Failed
- Verify the password in env.yml is correct
- Check if the admin account is locked

### Resource Already Exists
- Change the resource names in the playbook (e.g., `ansible_test_vol_2`)
- Or delete existing resources before re-running

## Test Coverage

The Tundra tests verify:

- **powerflex_common_v2:**
  - Gen2 API version detection
  - Gateway connectivity
  - System health query
  - Graceful degradation on Gen1 (not applicable on Tundra)

- **powerflex_provisioning_v2:**
  - Volume CRUD operations
  - Snapshot creation with retention
  - Storage pool creation with Erasure Coding (TwoPlusTwo)
  - Device group creation
  - Gen2 parameter validation (device_group_id, storage_node_id)
  - Gen1-only parameter rejection

## Notes

- These tests use real Tundra resources. Ensure you have permission to create resources.
- The tests are idempotent — running them multiple times should not cause errors.
- The tests do not automatically clean up resources to allow manual inspection.
