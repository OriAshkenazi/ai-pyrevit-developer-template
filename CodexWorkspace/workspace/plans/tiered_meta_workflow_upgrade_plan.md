# Tiered Meta-Workflow Upgrade Plan (Template-Only, OOTB Example Preserved)

## Summary
- Keep this repository as a template/meta process repo, not a project-specific add-on implementation repo.
- Add two usage tiers:
  - Beginner: no hooks required.
  - Advanced: optional, opt-in hooks and stricter quality controls.
- Keep `ai-pyrevit-developer-template.extension` as a protected out-of-the-box example.
- Deliver all work from branch `docs/tiered-meta-workflow`.

## Planned Features
1. Tiered onboarding and navigation
   - Add `CodexWorkspace/human/beginner_quickstart.md` and `CodexWorkspace/human/advanced_workflow.md`.
   - Update `README.md` and `CodexWorkspace/human/README.md` with a clear Beginner vs Advanced entrypoint.

2. Canonical agent contract and decision memory
   - Expand `AGENTS.md` to be the canonical operating contract for agents in this repo.
   - Add a maintained `Decision Log` section inside `AGENTS.md` for major corrections, hard-won lessons, and non-negotiable rules.

3. Strict temporary-files policy
   - Define `tmp/` as the only allowed location for temporary artifacts (scratch files, debug outputs, generated analysis dumps).
   - Update `.gitignore` and docs so temporary files are never committed by default.
   - Add advanced-mode checks to flag temp files outside `tmp/`.

4. Advanced workflow artifact layer
   - Add:
     - `CodexWorkspace/workspace/prd.md`
     - `CodexWorkspace/workspace/tech_spec.md`
     - `CodexWorkspace/workspace/status.md`
   - Add matching templates under `CodexWorkspace/skills/develop-pyrevit-extensions/assets/templates/`.
   - Keep existing beginner workflow artifacts (`development.md`, `tasks/`, `reviews/`, `backlog.md`) unchanged.

5. `Status.md` schema contract (advanced mode)
   - Require fixed sections:
     - `Scope`
     - `Folder Map`
     - `Completed`
     - `In Progress`
     - `Pending`
     - `Known Bugs`
     - `Open Risks`
     - `Next Actions`
     - `Last Updated`
   - Document update cadence: update after each meaningful code/workflow change in advanced mode.

6. Optional advanced hooks and setup scripts
   - Add `.githooks/` and opt-in setup/teardown scripts:
     - `tools/setup_advanced_hooks.ps1`
     - `tools/disable_advanced_hooks.ps1`
   - Hooks enforce advanced safeguards without affecting beginner onboarding.

7. Release/update communication
   - Add root `CHANGELOG.md` as the canonical "what changed since last version" artifact.
   - Link `CHANGELOG.md` from root/workspace entrypoints.

8. Logging standards by tier
   - Add a logging reference page defining:
     - Beginner minimum logs (simple run outcome + error context).
     - Advanced logs (structured, detailed, persisted).
   - Standardize storage path: `tmp/logs/`.

9. Advanced AI/data-task safety rules
   - Add advanced checklist requirements for:
     - dataset coverage disclosure,
     - explicit statement when sampling is used,
     - no silent downsampling,
     - numeric sanity checks,
     - metric direction validation (what is better/worse).

10. OOTB scaffold preservation safeguards
   - Document a non-removal policy for `ai-pyrevit-developer-template.extension/` and HelloWorld paths.
   - Add CI safeguard script `tools/check_example_scaffold.ps1` to fail if required scaffold paths are missing.
   - Add checklist items enforcing scaffold preservation in review.

11. Documentation and link hygiene cleanup
   - Fix stale path patterns and inconsistent links.
   - Keep all docs aligned with the template-only positioning.

## Implementation Steps
1. Create branch `docs/tiered-meta-workflow`.
2. Update `AGENTS.md` with contract rules, strict temp policy, `Decision Log`, and scaffold non-removal policy.
3. Add tiered docs and update top-level navigation docs.
4. Add advanced hook scripts and docs for opt-in enable/disable.
5. Add `CHANGELOG.md` and cross-links.
6. Add advanced workspace artifacts plus templates.
7. Enforce and document `Status.md` schema contract.
8. Add logging standards reference and integrate into checklists.
9. Add advanced AI/data-task safety checklist items.
10. Add scaffold-preservation CI check and checklist coverage.
11. Apply link/path cleanup across docs.

## Validation Scenarios
1. Beginner flow works without enabling hooks.
2. Advanced flow enables checks only after running setup script.
3. Advanced flow can be disabled cleanly with teardown script.
4. `CHANGELOG.md` exists, is linked, and receives version updates.
5. PRD/TechSpec/Status files and templates exist and are documented.
6. `status.md` content validates against required section schema.
7. Temp artifacts outside `tmp/` are flagged in advanced mode.
8. Beginner/advanced logging requirements are documented with `tmp/logs/` location.
9. Advanced checklist contains AI/data-task safety items.
10. Scaffold check passes when expected paths exist.
11. Scaffold check fails if `ai-pyrevit-developer-template.extension/` or HelloWorld `script.py` is removed.
12. Manual smoke: extension still loads in pyRevit and HelloWorld still runs.

## Assumptions
1. This repo stays template-first.
2. Advanced controls remain opt-in to protect beginner usability.
3. `AGENTS.md` is the canonical agent contract and decision memory location.
4. OOTB scaffold remains protected and mandatory.
5. Delivery is via PR from `docs/tiered-meta-workflow`.
