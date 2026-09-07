# Queue Contract — v1 (RATIFIED 2026-09-06)

What an item is, what a claim is, who owns custody, and how an item closes. Read by the
queue part, the service that fronts it, and every manager and worker session.

## Who builds against this

**The queue part** implements it as an embedded library. **The service** fronts it and
records what it says. **Manager sessions** derive, file and claim; **worker sessions**
claim, renew and resolve; **the app** shows items in plain words.

## What it is

```
item     id · project · contract_clause (required) · gap · done_looks_like
         holder · custody_until · resolution · discovered_from · blocks[]

claim    (next ready | this id)  -> item, or a refusal naming the holder
renew                             -> custody_until extended, or a refusal: lost
resolve  id, words for the asker  -> final; later corrections append, never rewrite
file     title, clause, ...       -> linked discovered_from the item you hold

read     any item, in full, never touching custody
state    derived: Truly ready · Waiting on you · Working · Stuck · Done
```

## The promises

1. **An item names its clause.** The contract clause it serves (or the steward's
   feedback, quoted), the gap, and what done looks like in plain words. No clause line →
   refused.

2. **Looking and taking are one call.** Claim takes the next ready item, or a named one,
   and establishes custody in the same act. Two callers never hold one item; a claim on a
   held item is refused naming the holder.

3. **Custody has one owner: the queue.** Renewal while the holder lives, reclaim after a
   named interval without it, and nobody keeps a second clock. A holder learns it lost
   custody on its next write, which is refused — never on a later read that quietly works.

4. **Reading never claims.**

5. **An item closes with words for the asker.** What is live, what changed for them, the
   honest caveat, the check they can run. Closed words are final; corrections are an
   appended erratum or a reopen with a reason.

6. **Discovered work is linked.** An item filed while holding another records where it
   came from, as a fact of the queue.

7. **Five plain words, derived at read time.** Never stored; never a machine word on a
   surface a person reads.

8. **Embedded in the instance, one store per project.** A library the instance runs; each
   project's store under the data directory by project id. No second server; nothing in
   a working copy.

## Not in v1

- **Priority as a number** — the first time a steward's priority word has nowhere to land.
- **Dependencies beyond "blocks"** — when a real item needs a second kind.
- **One queue across hosts** — when two hosts must pull from one.
- **The storage engine** — the queue part's own contracts.

## How the kit checks it

- Two concurrent claims of one ready item → one holder, one refusal naming the holder (measured).
- A write after custody lapsed → refused; the lapse visible on the item.
- An item filed without a clause line → refused with a sentence.
- No app surface carries a machine state word from the queue.
- Each project's store sits under the data directory; nothing in a working copy.

## Open questions

- Whether the family's queue and a part's queue may reference each other's items by id, or only by seam.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-06 | v1 drafted (our own queue, so day one brings nothing else); ratified as content. | Steward's words, 2026-09-06. |
| 2026-09-07 | Reshaped into the family format on the steward's word ("port it"); no promise changed. | `docs/FORMAT.md`. |
