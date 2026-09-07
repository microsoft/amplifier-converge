# Family Contract — v1 candidate (proposal)

**Target.** `contracts/family.v1.md`, Core 3 (the picker) and Core 6 (two managers never share state).

## The exact change

### Core 3 — the picker's anchor is the manager session
Before:
```
The app's
   project picker shows exactly this file's parts, beside the steward's own projects.
```
After:
```
The app's
   picker shows every manager session — running or resumable — with the repositories
   it steers; this file's parts and the steward's own projects appear through the
   sessions that steer them, and a project with no session shows as one to start.
```

### Core 6 — one manager may steer several repositories
Before:
```
6. **Two managers never share state.** The instance keeps every project's state
   under its own data directory by project id — workspace, queue, plan record,
   lanes, calls — and no two projects share a path;
```
After:
```
6. **Two managers never share state.** The instance keeps every manager session's
   state under its own data directory by session id — workspace, queue, plan record,
   lanes, calls — and no two sessions share a path; one session may steer several
   repositories, each shown apart;
```

### Kit assert
Before:
```
- The app's project picker, read live, lists exactly the parts in `family.toml`
  plus the steward's own projects — no more, no fewer.
```
After:
```
- The app's picker, read live, lists every manager session the instance knows and,
  through them, every part in `family.toml` and every project of the steward's — a
  part or project with no session appears once, as one to start.
```

## The evidence
The steward, in the UX transcript (line 883): "the manager session is the thing that
we're pinned to, and then the related resources, not a particular project or
particular repo"; (1015) "a highly glanceable list of running or resumable manager
sessions"; (873) "that manager session might be connected to multiple repos at once…
they should be separated by repo." The ratified Core 3 forbids that home as the picker.

## What does NOT change
Cores 1, 2, 4, 5, 7, 8, 9; `family.toml`'s shape; the three status words.

## The steward's word
_(ratified · ratified with edits · declined · later)_
