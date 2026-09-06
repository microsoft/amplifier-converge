# Amplifier Converge — Vision (DRAFT)

*Drafted 2026-09-06 from the steward's sentences. A proposal until the steward
answers.*

---

## Where this is going

Amplifier Converge is the app a person opens to get work done the Converge way —
vision first, contracts as the law, work derived from the gap between the two — with
a team of agents doing the work and the person's attention spent only where a person
is irreplaceable. It is one experience made of several small projects, each a
Converge project in its own right, held together by contracts at their seams rather
than by one repository.

A person — the **intent steward** — creates a project or attaches a repository they
already have, picks what kind of agent will manage it, and presses go. A **manager
session** wakes, reads the project's vision and contracts (or, on a repository that
has none yet, investigates and drafts them for the steward's word), and derives the
work. It launches **worker sessions** in **lanes**, each a bounded piece with its own
working copy, and each lane is a **run**: a record the app shows live — queued,
running, ended with proof or stuck with a cause or waiting on a word, merged. The
steward reads plain sentences, answers the four calls only a person can answer, and
is otherwise never the bottleneck.

Every actor speaks one surface. The app, a command line, the manager session and
every worker session — whatever agent runs them — talk to **the Converge service**
through the same API, and what the service records is the truth: a claim on a work
item, a run's state, a call put to the steward, a check the manager re-ran. What an
agent prints is telemetry; what it tells the service is fact.

Agents are brought, not built in. An **agent type** is a small adapter — start a run
with this identity and this wake prompt, stream what it says, report how it ended —
and Amplifier is the one that ships first, with a bare process and an HTTP endpoint
always available so anything can be wired in, and Claude Code, Codex and GitHub
Copilot following as thin adapters. A manager can be any agent type; so can any
worker. The method does not depend on which agent runs it, because the method is in
the contracts and the service enforces what a contract can enforce.

The whole thing installs with one command onto the Amplifier a person already has,
needs no daemon, no database server and no terminal multiplexer, and keeps every
project's operating state under that project's own workspace.

The through-line: the vision and contracts of each project are the one text both
people and machines obey, and the top-level project's contracts are the seams
between the parts — so a part can be small, be replaced behind its seam, and be
worked on by its own manager session in parallel with the others, without the whole
moving.

---

## Principles

1. **One experience, many projects.** Amplifier Converge is the top-level project;
   the method, the service, the app, the agent types and the queue are sub-projects,
   each with its own vision, contracts, ledger, queue and manager session. The top
   level holds the seams and names its parts; it holds no part's internals.

2. **The API is the truth.** Anything worth knowing about a run, a claim, a call or a
   check is a record the service holds; a file, a terminal or a log is evidence of
   it, never the source. If two disagree, the record wins and the disagreement is a
   defect.

3. **Bring your own agent; the method stays the law.** Any agent type can run a
   manager or a worker. What it must do — claim, resolve, file, call, heartbeat, and
   for a manager re-run the check — is in the wake contract and the service's gates,
   not in the agent.

4. **A run is a record, not a process.** A run has a beginning, a state, an ending in
   exactly one of three ways — done with proof, stuck with a cause, waiting on the
   steward — and a merge. Where its process lives is the agent type's business; when
   it was last seen alive is an observation with a time on it, never a state
   somebody maintains.

5. **Trim, for one job.** Each part does exactly what this experience needs and
   nothing another product would want of it. A queue is a queue with custody; a
   service is six records and one API; an adapter is three functions.

6. **The steward answers four things and reads sentences.** Ratify a change of
   direction, allow an irreversible act, perform a check only a person can, set a
   priority or stop. Everything else keeps moving, and what reaches them is written
   for a person who has never opened a code editor.

7. **Nothing is installed twice and nothing lands outside the project.** One command;
   no daemon a person must run; every project's operating state under that
   project's own workspace; a control plane that sits lightly on the host.

8. **Endpoints are read from the router, never from prose.** What an agent is told it
   may call is generated from what the service actually serves, and a check fails
   the moment they drift.

9. **A part that grows a second domain is peeled, not grown.** Every part carries a
   size it may not exceed and a test for a second domain inside it — a sub-directory
   with its own vocabulary, its own kit or its own steward questions. When either is
   met the part's manager proposes the peel as a seam here, and the new part begins
   as a Converge project of its own. Splitting is the normal shape of growth; a part
   that keeps growing is the defect.

---

## What this is not

- **Not a monorepo** — the parts are repositories with their own lives; the top
  level references them, it does not contain them.
- **Not an org chart, a company or a budget-first system** — one steward per
  project; roles are modes, not hires; budgets arrive as a gate when a part earns
  one.
- **Not a scheduler that re-spawns agents on a tick** — the service observes runs;
  the agent type decides how a run lives.
- **Not cloud-first** — a run happens on the host, or in an isolated twin of it,
  before any remote sandbox is an agent type.
- **Not a general tracker, terminal dashboard or memory store** — each part is
  bespoke to this experience and may borrow ideas from anything, but owes nothing to
  another product's users.

---

## How you can tell it is working

- A steward creates a project, attaches a repository that has never seen Converge,
  and reaches a ratified vision and a seeded ledger in **under an hour without
  opening a terminal**.
- The app's project picker lists the top-level project, every registered part and
  the steward's own projects; each opens to its own direction, operation and runs.
- Five manager sessions run five parts at once with **zero** shared files, queue
  items or calls between them — read by the family's own kit, not asserted.
- A run's three endings are the only endings observed across a wave, and **zero**
  runs are marked merged without the manager's check on record; the service refuses.
- A stalled lane is visible to the steward within **fifteen minutes** because an
  observation was written and shown, not inferred.

---

## Changelog

- **2026-09-06 — v1 (DRAFT).** From the steward's sentences: not a monorepo;
  modular parts, each a Converge project with its own manager so several can run in
  parallel; the top level holds vision and seams and is aware of the parts, visible
  in the app; bespoke and trim, installable on day one with nothing else to bring;
  bring your own agent with Amplifier built in, Claude Code, Codex and GitHub
  Copilot next.
