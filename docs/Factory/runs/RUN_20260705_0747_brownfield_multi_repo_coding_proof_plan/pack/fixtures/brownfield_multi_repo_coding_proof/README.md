# Brownfield Multi-Repo Coding Proof Fixture Directory

## Version

v1

## Change Log

- v1 (2026-07-05): Initial fixture directory contract.

## Future Fixture Shape

Future implementation should add fixture JSON files under `tests/fixtures/coding_proof_harness/` or a dedicated subdirectory if the implementation keeps loader compatibility.

Each fixture should include:

- `fixture_id`
- `title`
- `domain`
- `project.declared_category = brownfield_multi_repo`
- `project.system_boundary`
- `repositories`
- `harness.system_boundary`
- `harness.repository_map`
- `harness.in_scope_repositories`
- `harness.out_of_scope_repositories`
- `harness.integration_contracts`
- `harness.ownership`
- `harness.build_commands_by_repository`
- `harness.test_commands_by_repository`
- `harness.task.relevant_repositories`
- `harness.expected.ready_for_provider`

The blocked fixture should include repositories but missing context such as service boundary, integration contract, authority path, or owner.
