# Service Contract — v1 candidate (proposal)

**Target.** `contracts/service.v1.md`, Core 3 (two records frozen) and "What v1 deliberately does NOT freeze" (the wire format).

## The exact change

### Core 3 — the desk's records are named
Before:
```
3. **Two records are frozen: `run` and `check`.**
```
After:
```
3. **Two records are frozen here — `run` and `check` — and the desk's records are
   named beside them.** Documents, proposals, artifacts, events, calls, the four
   writes and the manager session are records the service serves under
   `contracts/desk.v1.md`; each is frozen the wave it first flows.
```

### Does not freeze — the wire format
Before:
```
- **The wire format** (REST vs RPC; poll vs push) — promoted when a client other
  than the app or the CLI needs it stable. Until then the app polls.
```
After:
```
- **The wire format** (REST vs RPC) — promoted when a client other than the app or
  the CLI needs it stable. A change on disk or in a record reaches a reader within
  ten seconds (desk.v1 Core 1); whether by poll or push is the service's business.
```

## The evidence
The app's re-derivation against the steward's UX transcript found ~60% of its missing
requirements blocked by the two-record freeze: documents, history, proposals, read
cursors, events and feedback artifacts have no record, and the app's own doctrine
forbids reading a disk to fill the gap. "Until then the app polls" contradicts the
transcript's "no stale state, no refresh ritual" (line 618).

## What does NOT change
`run` and `check` stay frozen exactly as written; Cores 1, 2, 4, 5, 6 unchanged; the
merge gate unchanged; identity per run unchanged.

## The steward's word
_(ratified · ratified with edits · declined · later)_
