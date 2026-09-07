# Amplifier Converge — Vision (RATIFIED 2026-09-06)

The end state this family converges toward, written as though already true. This page
is never edited to record what shipped; that lives in the ledger and the queue. It
changes by amendment first — a dated line in the changelog with the evidence — and the
work is derived from the gap afterwards, never the other way round.

## What Amplifier Converge is

The app a person opens to get work done the Converge way: vision first, contracts as the
law, work derived from the gap between the two, a team of agents doing the work. It runs
as one instance on that person's machine, installed by itself with nothing else required.
The person — the **intent steward** — creates a project or attaches a repository, picks
which kind of agent will manage it, and presses go. A **manager session** reads the
project's direction (or drafts it, on a repository that has none), derives the work, and
runs it in **lanes**. Every lane is a **run** the app shows live. The steward reads plain
sentences and answers four kinds of question, and is otherwise never the bottleneck.

## Principles

### 1. One experience, many projects
Amplifier Converge is a family of small Converge projects — method, service, app,
agents, queue — each with its own repository, vision, contracts, ledger, queue and
manager session, held together by contracts at their seams. The top level holds the
seams and names the parts; it holds no part's internals.

### 2. The API is the truth
Anything worth knowing about a run, a claim, a call or a check is a record the service
holds. A file, a terminal or a log is evidence of it, never the source. When two
disagree, the record wins and the disagreement is a defect.

### 3. Bring your own agent; the method stays the law
Any agent type can run a manager or a worker. What it must do — claim, resolve, file,
call, report liveness, and for a manager re-run the check — is in the wake contract and
the service's refusals, not in the agent. Amplifier is one type among several, ready to
configure and never required.

### 4. A run is a record, not a process
A run begins, ends in exactly one of three ways — done with proof, stuck with a cause,
waiting on the steward — and merges. Where its process lives is the agent type's
business. When it was last seen alive is a timestamp, never a state somebody maintains.

### 5. Trim, for one job
Each part does what this experience needs and nothing another product would want of it.
A queue is a queue with custody; a service is a few records and one API; an agent type
is three functions.

### 6. The steward answers four things and reads sentences
Ratify a change of direction; allow an irreversible act; perform a check only a person
can; set a priority or stop. Everything else keeps moving, and what reaches them is
written for a person who has never opened a code editor.

### 7. One install, one instance, nothing else required
`uv tool install` of this repository installs the whole. The instance owns one data
directory and every project's state under it. It creates workspaces, clones
repositories and launches managers from the screen; a person opens a terminal only to
attach to a live session, by choice.

### 8. Endpoints come from the router, never from prose
What an agent is told it may call is generated from what the service actually serves. A
check fails the moment they drift.

### 9. A part that grows a second domain is split out, not grown
Every part names a ceiling and a test for a second domain inside it. Crossing either
means a split-out proposed at the family level within one wave. Splitting is the normal
shape of growth; a part that keeps growing is the defect.

## What this deliberately resists

- **A monorepo.** The parts are repositories with their own lives.
- **An org chart, a company, budgets first.** One steward per project; roles are modes,
  not hires; budgets arrive as a gate when a part earns one.
- **A scheduler that re-spawns agents on a tick.** The service observes; the type decides
  how a run lives.
- **Cloud first.** A run happens on the person's machine, or an isolated twin of it.
- **Being an add-on to another tool.** Nothing has to be installed first; no agent type
  is required.
- **A general tracker, terminal dashboard or memory store.** Each part is bespoke to this
  experience and owes nothing to another product's users.

## How you can tell it is working

- A steward attaches a repository that has never seen Converge and reaches a ratified
  vision and a seeded ledger in **under an hour without opening a terminal**.
- A steward opening the picker sees every part (six today) and their own projects, and
  reaches any one's direction and runs in **one click**.
- Five manager sessions run five parts at once with **zero** shared files, queue items
  or calls between them — read by the family kit, not asserted.
- A steward reading a wave finds **zero** runs marked merged without the manager's check
  on record; the service refused the rest.
- A stalled lane is visible to the steward within **fifteen minutes**, because an
  observation was written and shown, not inferred.
- A person with `uv` reaches a running instance with the browser open in **under five
  minutes**, one command, no other product required.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-06 | v1 drafted from the steward's sentences; corrected the same day (installs on its own; one instance owns state; Amplifier optional); ratified as content. | Steward's words, 2026-09-06. |
| 2026-09-06 | Principle 9 (split out, not grown) added on the steward's design-safety rule; headings carry one state word. | Steward's words; method `documents.v1` clause 2. |
| 2026-09-07 | Proposed reshaped into this format: one-paragraph "what it is", principles as titled subsections, resists list, changelog table. No principle changed. | `proposed-format/FORMAT.md`. |
