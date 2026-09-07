# Desk Contract — v1 (DRAFT)

What the service serves so a steward's desk needs no disk, repository or agent output read.

## Who builds against this

**The app** builds Direction and Operation on it. **The service** serves every record named
here. **Manager sessions** are read through it; **the method part's** documents are what is served.

## What it is

The browser is where a person exercises intent, not where the AI works. These are the
records that make that possible:

```
document   path · body · state_word · history[] (commit, what changed) · proposals[]
           paragraphs[] { anchor, text }             # anchor survives edits elsewhere

proposal   target · what_changes · why · evidence · what_does_not_change
           questions[] · decision (ratified | ratified with edits | declined | later)

write      kind: answer | prioritize | feedback | steer      # exactly four
           target (call | item | run | anchor) · body · artifact_ids[]

artifact   id (content hash) · kind (screenshot | audio | log | diff | output) · bytes
attention  [ up to 5 calls, each with recommendation + ≤2 trade-offs ], re-ranked per read
cursor     person · project · last_read_at      → "since you last read": documents, proposals, runs, calls
```

## The promises
1. **Documents are served, not read.** Every file under `docs/` and `contracts/` — body,
   state word, history, open proposals — from the working copy the instance owns. The app
   opens no file. A change on disk reaches the reader within ten seconds.
2. **Every paragraph has a stable anchor.** Questions, comments and evidence pin to an
   anchor, never a line number, and survive edits elsewhere in the file.
3. **A proposal has one shape, whoever wrote it.** What changes → why → evidence → what
   does not change → questions → decision, with before/after pairs rendered as a diff and
   a one-word decision beside it.
4. **Exactly four writes.** *Answer* a call; *prioritize* an item or lane (earlier, later,
   stop); *feedback* on anything (a sentence, a screenshot, a voice clip, pinned to an
   anchor or a run); *steer* (objective, budget, lane count). Every write is recorded as
   one of the four. There is no fifth and no "create issue".
5. **Evidence is content.** A check's output, a screenshot, a diff, a recording — stored
   as an artifact by content hash in the data directory and referenced by id. Project
   truth, never an opaque attachment.
6. **At most five things ask for a word.** Served as an ordered list, each arriving with a
   recommendation and at most two trade-offs, re-ranked on every read. Everything else
   keeps moving and is shown as such.
7. **What changed since you last read.** A read cursor per person per project; a return
   never begins with a search.
8. **Evidence over claims, details folded.** Every asserted fact carries its evidence one
   fold away; a run shows what is running against what was intended.

## Not in v1

- **Conversing with a manager session from the desk** — when the agents seam names the write (candidate open).
- **A UI copilot editing beside the reader** — deferred on the steward's word; when asked for again.
- **Phone and desktop layouts** — the app's own contract.
- **Review through a hosted forge** (pull requests, comments) — when a second person joins a project.

## How the kit checks it

- Edit a document on disk with the app's file access denied → re-served with new state word and history entry within ten seconds.
- A question pinned to a paragraph survives an edit above it.
- A fifth kind of write → refused with a sentence.
- The attention list never exceeds five and re-orders when a call lands.
- An artifact served by id matches its content hash.

## Open questions

- Whether a ratification given on the desk is itself a record (the method's `documents.v1` leaves this open).

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-07 | v1 drafted after the steward's UX transcript was read against the app (268 requirements, 14 covered); written in the family format. | `ai_working/app-gap-2026-09-07.md`; `docs/FORMAT.md`. |
