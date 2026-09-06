# Queue Contract — v1 (RATIFIED 2026-09-06)

**Who builds against this:** the service (it fronts the queue and records what the
queue says); every manager session (it derives, files and claims items); every
worker session (it claims, heartbeats and resolves); the app (it shows items in
plain words); the method part (its ledger reads that every item names a contract).

## Purpose

Work is derived, never invented, and several agents pull from one queue at once.
This seam names what an item is, what a claim is, who owns custody, and how an item
closes — so the queue can be small, embedded and ours, and so the service and the
app never reach past it into how it stores anything.

## Core (the teeth)

1. **An item names its contract.** Every item carries the contract clause it
   serves (or the steward's feedback it came from, quoted), what the gap is, and
   what done looks like in plain words. An item without a contract line is refused.

2. **A claim is atomic and exclusive.** One call takes the next ready item, or a
   named one, and establishes custody in the same act; two callers never hold one
   item; a directed claim on a held item is refused naming the holder.

3. **Custody has one owner.** The queue owns custody: renewal while the holder
   lives, reclaim after a named interval without renewal, and nobody else keeps a
   second clock. A holder learns it lost custody on its next write, which is
   refused, never on a later read that silently succeeds.

4. **Reading never claims.** Any item may be read in full — title, contract,
   description, acceptance, holder, resolution — without touching custody.

5. **An item closes with words for the person who asked.** A resolution says what
   is live, what changed for them, the honest caveat and the check they can run. A
   closed item's text is final; a correction is an appended erratum or a reopen
   with a reason, never a rewrite.

6. **Discovered work is linked, not lost.** An item filed while holding another
   records where it came from; the link is a fact of the queue, not a note.

7. **States are the five plain words.** *Truly ready · Waiting on you · Working ·
   Stuck · Done*, derived by the queue from custody and dependencies; a machine
   word never reaches a surface a person reads.

8. **Embedded in the instance, one store per project.** The queue is a library the
   instance runs, with each project's store under the instance's data directory by
   project id; there is no second server and nothing written into a repository's
   working copy.

## What v1 deliberately does NOT freeze

- **Priority as a number** — promoted the first time a steward's priority word has
  nowhere to land.
- **Dependencies beyond "blocks"** — promoted when a second kind is needed by a
  real item.
- **Sharing one queue across hosts** — promoted when two hosts must pull from one.
- **The storage engine** — never frozen here; the queue part's contracts own it.

## Conformance kit asserts

- Two concurrent claims of one ready item yield one holder and one refusal that
  names the holder; measured, not assumed.
- A write after custody lapsed is refused; the lapse is visible on the item.
- An item filed without a contract line is refused with the reason in plain words.
- No surface the app renders carries a machine state word from the queue.
- Each project's queue store sits under the instance's data directory by project id
  and nothing of the queue is written into a repository's working copy.

## Reserved / open questions (NOT frozen)

- Whether the family's top-level queue and a part's queue may reference each
  other's items by id, or only by seam.
