# Project Memory Object Seeds

This directory contains reviewed Project Memory object JSON files for this repository.

These files are:

- repo-local memory inputs for agent-facing context commands
- plain `MemoryObject` JSON records loaded by `python3 -m soane.project_memory.cli`
- intentionally small and reviewable

These files are not:

- a database schema
- a persistence architecture
- generated Markdown views
- a replacement for constitutional or canonical documents

Default agent-facing commands load `docs/project_memory/objects/` before falling back to explicit fixture inputs.

Useful commands:

```bash
python3 -m soane.project_memory.cli validate --no-fixtures --memory-dir docs/project_memory/objects
python3 -m soane.project_memory.cli agent-context --task "<TASK>"
python3 -m soane.project_memory.cli agent-trace --id <MEMORY_OBJECT_ID>
python3 -m soane.project_memory.cli agent-affected --path <SOURCE_PATH>
```
