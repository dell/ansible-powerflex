# KNOWLEDGE.md — ansible-powerflex

<!-- yaml-metadata-start -->
scope_paths: ["./"]
capture_git_sha: "75e5618e3c5466bd5a617c7c2b580dbe20648619"
status: "current"
auto_update: false
preview_before_apply: true
scaffold_version: "1.0"
# session_state: { is_complete: true }
<!-- yaml-metadata-end -->

<!-- quick-reference-start -->
## Agent Quick Reference

| Section | Heading | Summary | never_again_count |
|---------|---------|---------|-------------------|
| Component Overview | `## Component Overview` | dellemc.powerflex collection for PowerFlex | — |
| Architectural Rationale | `## Architectural Rationale` | PyPowerFlex SDK; Ansible collection pattern | — |
| Failure Modes & Gotchas | `## Failure Modes & Gotchas` | SDK coupling, idempotency, verify_ssl | 0 |
| Implicit Contracts | `## Implicit Contracts` | Connection params, ordering, action groups | — |
<!-- quick-reference-end -->

## Five Questions Quick Reference

### What does it do?
Ansible Galaxy collection `dellemc.powerflex` (v3.0.0). Provides 23 modules and 12 roles for declarative, idempotent management of Dell PowerFlex (VxFlex OS) software-defined storage. Uses `PyPowerFlex` (==2.0.0) Python SDK.

### How do you modify it?
Create module file in `plugins/modules/`, add example playbook in `playbooks/modules/`, add unit test in `tests/unit/plugins/modules/`, append module FQCN to `meta/runtime.yml` action group.

### What breaks?
SDK version mismatch is a blocking defect. Missing action group entry causes `module_defaults` to silently skip the module. `validate_certs: false` in production violates security constitution.

### What depends on it?
`PyPowerFlex` ==2.0.0, Ansible >= 2.15.0. Ordering: dependent resources must exist before referencing them.

### What's undocumented?
`powerflex_base.py` (base class + `@powerflex_compatibility` decorator), `configuration.py`. Uses `logging.basicConfig` with `CustomRotatingFileHandler`. Writes `ansible_powerflex.log` by default (5 MB rotate, 5 backups).

---

## Component Overview

Ansible Galaxy collection `dellemc.powerflex` (v3.0.0) for Dell PowerFlex (VxFlex OS) software-defined storage. 23 modules and 12 roles covering volumes, SDCs, SDSs, protection domains, storage pools, fault sets, devices, snapshots, snapshot policies, replication consistency groups, replication pairs, and more.

---

## Architectural Rationale

Standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the PowerFlex REST API through the `PyPowerFlex` SDK.

**SDK strategy:** Static import, checked via `ensure_required_libs()`. Version pinned at `==2.0.0` in `requirements.txt`.

---

## Failure Modes & Gotchas

### 1. SDK version coupling

Each collection release is tested against exactly one SDK version (or tight range for PyU4V). A mismatch between collection and SDK version is a blocking defect. Never update `requirements.txt` SDK versions without verifying against the corresponding collection release notes.

### 2. Idempotency assumptions

Modules are designed to be idempotent but some parameters may be accepted by the module yet ignored by the underlying API. Always verify with a second run.

### 3. Verify SSL setting

`validate_certs: false` is used in example playbooks but is a lab-only setting. Production requires `true`. Modules must not default to skipping verification.

### 4. Acceptance test cleanup

If tests fail mid-run, resources may be left on the array. Clean up manually before re-running.

### PowerFlex Module Version Gating

The `@powerflex_compatibility(min_ver=..., max_ver=...)` decorator on module classes provides runtime version checking. When the module is invoked against a PowerFlex system, the base class checks the running PowerFlex API version. If outside the compatible range, the task exits with `changed=false` and a skip warning naming the correct module version.

### Roles

The collection includes 12 Ansible roles for gateway installation, MDM configuration, and cluster deployment tasks that go beyond simple module invocations.

### Never Again

No incident-derived constraints recorded.

---

## Performance Characteristics

TBD — requires SME input.

---

## Implicit Contracts

**Connection parameters required:** All modules require `hostname`, `username`, `password`, `validate_certs` — these are not optional.

**Resource ordering:** Dependent resources must exist before being referenced (e.g., filesystem before snapshot, volume group before volumes, policies before assignment).

**Action group registration:** Every new module must be appended to the `dellemc.powerflex.all` action group in `meta/runtime.yml`.

---

## Threading & Synchronization

Ansible handles concurrency via forks at the play level. Individual module executions are single-threaded.

---

## Build System & Configuration

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build collection tarball |
| `ansible-galaxy collection install <tarball>` | Install locally |
| `pytest tests/unit/` | Run unit tests |
| `ansible-playbook --syntax-check` | Validate playbook syntax |

---

## Operational Knowledge

Uses `logging.basicConfig` with `CustomRotatingFileHandler`. Writes `ansible_powerflex.log` by default (5 MB rotate, 5 backups).

---

## General Context

No additional context beyond what has been captured.

---

## References

- [Ansible Galaxy — dellemc.powerflex](https://galaxy.ansible.com/dellemc/powerflex)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)

---

## Governance Spec Discrepancies

No discrepancies detected.
