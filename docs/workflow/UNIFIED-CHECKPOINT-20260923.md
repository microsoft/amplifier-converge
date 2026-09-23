# Converge in Unified — integration checkpoint, September 23, 2026

A dated architecture and ownership map for contributors. This records the current
integration experiment; it does not amend the ratified vision, register new family
members, or ratify a draft contract. See the [retrospective](RETROSPECTIVE-20260923.md)
for observed results and the [acceptance plan](ACCEPTANCE-PLAN-20260923.md) for the
next proof.

## Experience being built

A person brings an incomplete idea, explores alternatives, agrees what the result
must do, and sees a manager turn that direction into checked work. They can revise
the direction, inspect evidence, or intervene without learning lane APIs. The
main conversation supervises a dedicated project manager; it stays available
while the manager and isolated workers continue.

The integration uses separately owned capabilities: On-ramp/Create for the idea,
Direction for documents and proposals, Possibly for alternatives and interactive
previews, and Operations for the work and its evidence. These are useful boundaries,
not a rigid wizard. Feedback can return to an earlier capability. A preview is not
a selection, ratification, or permission to implement. Canvas count need not equal
tool count, and a foreground HTML concept is not a manager-built application.

## Ownership map

| Owner | Responsibility in this composition |
| --- | --- |
| [This umbrella](https://github.com/microsoft/amplifier-converge) | Family vision, seam proposals, registry and cross-repository checkpoints. No component implementation. |
| [Method](https://github.com/microsoft/amplifier-converge-method) | Document law and method definitions. Kept distinct from executable adapters and delivered operating instructions. |
| [Portable operating bundle](https://github.com/microsoft/amplifier-bundle-converge) | Collaboration, supervisor and manager guidance; checked-work discipline and recovery that should also succeed in CLI/TUI text. No Unified canvas dependency. |
| [Optional Unified bundle](https://github.com/microsoft/amplifier-bundle-unified-converge) | Composes portable behavior with host-specific context, capability discovery, scoped presentation, delivery opening and requested completion watches. |
| [On-ramp](https://github.com/microsoft/amplifier-converge-onramp) | Retained ideas and promotion into project work, exposed through public callable operations and a view. |
| [Direction](https://github.com/microsoft/amplifier-converge-direction) | Document revisions, wording proposals and decisions; preserves source and exact revision identity. |
| [Possibly](https://github.com/robotdad/possibly) | Independently installed exploration, revision and preview capability. Preview/navigation remains separate from selecting a direction. Its installation and evidence must be observed, not replaced by a fixture or assumed from the other three tools. |
| [Operation](https://github.com/microsoft/amplifier-converge-operation) | Operations Smart Tool and project view, public observation and commands routed to their owners; receives the native runtime composition. The repository name is singular. |
| [Agents](https://github.com/microsoft/amplifier-converge-agents) | Native manager/worker execution, action admission, waves, isolated lanes, bounded attempts, manager checks and integration/recovery. |
| [Queue](https://github.com/microsoft/amplifier-converge-queue) and [Service](https://github.com/microsoft/amplifier-converge-service) | Bounded work/custody and retained records/command receipts, respectively. Consumers use their public surfaces. |
| [Experience SDK](https://github.com/microsoft/amplifier-converge-experience-sdk) | Shared capability presentation and transport support, without taking over domain decisions. |
| Amplifier Unified | General conversation, sessions, tools, canvases, scheduling and authorization. It must contain no Converge-specific domain knowledge or required Converge dependency. |

App, Reader and Sessions remain separate family projects with their existing
contracts. This map does not retire them or claim their standalone implementation
is the active Unified integration. The [migration record](REPOSITORY-MIGRATION.md)
and [family registry](../../family.toml) retain their own scope and history.

## Composition and state boundaries

Converge is optional. Loading its Unified behavior should produce a first-class
experience through generic host APIs; Unified remains usable without it. The
portable bundle owns host-neutral lessons. The optional bundle owns how those
lessons reach the host's conversation and canvas. A host capability gap needs a
generic host design review, not a Converge special case inside Unified.

The foreground conversation, native manager history, worker histories and domain
records have separate identities. Installing guidance does not start a manager,
install every Smart Tool, migrate native instructions, or replay old work. Each
role's actual resolved resources, model and reasoning policy need receiving
evidence. A configured label alone does not prove a complete provider request.

The trial uses Amplifier native sessions. Other manager/worker runtimes remain a
design goal; this checkpoint does not establish Claude Code, Codex or Copilot
adapter compatibility, interchangeable native histories, or a tested cross-device
handoff. A stopped or expired foreground watch does not stop the independent
manager. Changing views does not authorize a project mutation.

The collaborative implementation currently uses an embedded public Service
library within trusted local processes. The existing
[collaborative-capabilities draft](../../contracts/collaborative-capabilities.v1-candidate.md)
explicitly distinguishes this from the settled single-process Service door.
That reconciliation and the eventual Sessions boundary remain open design work;
successful local trials do not ratify either change.

## Delivery and readiness

There are separate proofs for worker output, manager checks, integration, selected
review result, retained runnable opening, actual customer interaction and automatic
handback. None implies all the others. Serving only an HTML artifact can lose
relative assets; an embedded website may have sandbox/storage restrictions. Keep
the existing sandbox intact, qualify the exact opening, and report a supported
direct-browser fallback honestly when embedded behavior is unavailable.

A service that answers HTTP is reachable at that observation time. A successful
open request is an accepted request. Neither proves the person can use the app or
that it survives the advertised lifetime. Product/service implementation stays
with the manager and its tracked workers; the supervisor must not rescue delivery
with an untracked replacement.

## Unapproved host proposal

The current scheduled-watch path invokes the foreground model and displays
machine-oriented scheduled input. A **design-only, unapproved** proposal is a
generic host extension point that can complete an observation with an audit
record, without a provider turn or public chat message, and invoke the agent only
for a meaningful result or failure. No such new interface is claimed here.

Converge would still own exact manager binding, current-state interpretation and
result selection; the host would own generic authorization, durable occurrences
and delivery policy. Any proposal must preserve correction/cancellation guards,
expiry, duplicate handling and ordinary schedules. The current prompt hook's
denial path is not a successful silent-observation interface. Approval and host
owner review are required before implementation outside Converge repositories.
