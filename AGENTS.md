# AGENTS.md - Dell Ansible Collection for PowerFlex

## Project Overview

This is the Ansible Galaxy collection for Dell PowerFlex (VxFlex OS) software-defined storage. It provides Ansible modules and roles for automating provisioning and management of PowerFlex systems.

- **Language:** Python
- **Collection namespace:** `dellemc.powerflex`
- **SDK:** `PyPowerFlex` v2.0.0
- **License:** GNU General Public License v3.0

## Architecture

The collection follows the standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the PowerFlex Gateway API through the `PyPowerFlex` SDK.

### Authentication

Modules authenticate to a PowerFlex Gateway using `hostname`, `username`, `password`, and optional `validate_certs`, `port`, and `timeout` parameters.

### SDK Strategy

Uses `PyPowerFlex` — a Dell-published Python SDK for the PowerFlex REST API, installed via `pip`. The required version is pinned in `requirements.txt`.

### Module and Role Count

The collection includes approximately 45 modules and 12 roles. Modules cover PowerFlex entities such as volumes, SDSs, SDCs, storage pools, protection domains, snapshots, devices, MDM clusters, and replication. Roles provide automated deployment and configuration workflows.

## Directory Structure

```
galaxy.yml                        Collection metadata (namespace, name, version)
plugins/
  modules/                        Ansible modules (one .py file per resource)
  module_utils/
    storage/                      Shared utility classes and SDK wrappers
  doc_fragments/                  Shared documentation fragments
meta/                             Collection metadata (runtime.yml)
roles/                            Ansible roles for deployment and configuration
tests/
  unit/
    plugins/                      Unit tests (pytest)
playbooks/                        Example playbooks
docs/                             Module documentation
changelogs/                       Release changelog fragments
requirements.txt                  Python dependencies (PyPowerFlex)
requirements.yml                  Ansible collection dependencies
```

## Build Commands

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build the collection tarball |
| `ansible-galaxy collection install <tarball>` | Install the collection locally |
| `pytest tests/unit/` | Run unit tests |

## Testing

### Unit Tests

- Test files follow `test_*.py` convention in `tests/unit/plugins/`.
- Framework: `pytest` with `unittest.mock` for mocking SDK calls.
- No hardware required.

### Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run unit tests
pytest tests/unit/ -v
```

## Code Style and Conventions

### Module Pattern

Each module follows the standard Ansible module pattern:
1. `DOCUMENTATION`, `EXAMPLES`, and `RETURN` docstrings at the top.
2. An `AnsibleModule` argument spec defining parameters.
3. A main class that wraps SDK calls and handles idempotency.
4. `module.exit_json()` for success, `module.fail_json()` for errors.

### Shared Utilities

- `plugins/module_utils/storage/` contains shared base classes and SDK initialization code.
- `plugins/doc_fragments/` contains reusable documentation for common parameters.

### Roles

Roles in `roles/` provide end-to-end deployment workflows (e.g., gateway install, MDM configuration, SDC deployment) with tasks, defaults, and templates.

### File Header

All source files must include the Dell copyright and GPL v3.0 license header.

## Common Development Tasks

### Adding a New Module

1. Create `plugins/modules/<resource>.py` following the Ansible module pattern.
2. Add unit tests in `tests/unit/plugins/`.
3. Add example playbooks in `playbooks/`.
4. Update `changelogs/` with a changelog fragment.

### Adding a New Role

1. Create `roles/<role_name>/` with `tasks/`, `defaults/`, `meta/`, and `templates/` subdirectories.
2. Add a `main.yml` in `tasks/` with the role logic.
3. Document the role in `roles/<role_name>/README.md`.

### Updating the SDK

Update `requirements.txt` with the new `PyPowerFlex` version.

## CI/CD

GitHub Actions workflows in `.github/workflows/`. Code coverage tracked via `codecov.yml`.

## Code Ownership

All files are owned by the maintainers defined in `.github/CODEOWNERS`.
