# Family Contract — v1 candidate (proposal)

**Target.** `contracts/family.v1.md`, Promise 3 (the picker), Promise 6 (state per project), and the picker line under *How the kit checks it*. Rebased 2026-09-07 onto the reshaped text; the change is the same.

## The exact change

### Promise 3 — the picker's anchor is the manager session
Before:
```
3. **Registered only when it exists.** A row whose repository is unreachable, or lacks
   `docs/VISION.md` and `contracts/`, fails the family kit. The picker shows exactly
   these rows beside the steward's own projects.
```
After:
```
3. **Registered only when it exists.** A row whose repository is unreachable, or lacks
   `docs/VISION.md` and `contracts/`, fails the family kit. The picker shows every
   manager session — running or resumable — with the repositories it steers; these rows
   and the steward's own projects appear through the sessions that steer them, and a
   project with no session shows as one to start.
```

### Promise 6 — one manager may steer several repositories
Before:
```
6. **Two managers never share state.** The instance keeps each project's state under its
   data directory by project id. No two projects share a path; a working copy receives
   only the project's own documents.
```
After:
```
6. **Two managers never share state.** The instance keeps each manager session's state
   under its data directory by session id. No two sessions share a path; one session may
   steer several repositories, each shown apart; a working copy receives only the
   project's own documents.
```

### The kit line
Before:
```
- The picker, read live, lists exactly the rows plus the steward's own projects.
```
After:
```
- The picker, read live, lists every manager session the instance knows and, through them,
  every row here and every project of the steward's; a part or project with no session
  appears once, as one to start.
```

## The evidence
The steward, in the UX transcript (883): "the manager session is the thing that we're pinned to, and then the related resources, not a particular project or particular repo"; (1015) "a highly glanceable list of running or resumable manager sessions"; (873) "that manager session might be connected to multiple repos at once… they should be separated by repo." The ratified Promise 3 forbids that home as the picker.

## What does NOT change
Promises 1, 2, 4, 5, 7, 8, 9; `family.toml`'s shape; the three status words.

## The steward's word
_(ratified · ratified with edits · declined · later)_
