# Desk Contract — v1 (DRAFT)

**Who builds against this:** the app (this is the seam its Direction and Operation are
built on); the service (it serves every record named here); every manager session
(its briefs, proposals and evidence are read through it); the method part (its
documents are what is served, and its paragraph anchors are what questions pin to).

## Purpose

The browser is not where the AI does its work; it is where a person exercises intent.
This seam names what the service serves so that a steward's desk can be built without
the app reading a disk, a repository or an agent's output — documents as a living
agreement, proposals as objects, evidence as content, feedback with no form to fill,
and the four writes a person may make unprompted. It exists because `service.v1`
freezes two records and the desk needs these to be records too.

## Core (the teeth)

1. **Documents are served, not read.** The service serves every document under a
   project's `docs/` and `contracts/` — body, state word, history (each commit and
   what it changed), and open proposals beside it — from the working copy it owns;
   the app renders and never opens a file. A change on disk reaches the reader
   without a refresh within ten seconds.

2. **Every paragraph has a stable anchor.** A served document carries an anchor per
   paragraph and clause that survives edits elsewhere in the file; a question, a
   comment or a piece of evidence pins to an anchor, never to a line number.

3. **A proposal is an object with one shape.** *What changes → Why → Evidence → What
   does not change → Questions → Decision* — served in that order whoever wrote it,
   with the fenced before/after pairs rendered as a diff, and a decision answerable
   in one word beside it.

4. **Exactly four writes, and the app asks which.** A steward may *answer* a call,
   *prioritize* an item or a lane (earlier, later, stop), *feedback* on anything (a
   sentence, a screenshot, a voice clip, pinned to an anchor or a run), or *steer*
   (an objective, a budget, a lane count). Every write is one of the four and is
   recorded as such; there is no fifth and no "create issue".

5. **Evidence is content.** A check's output, a screenshot, a diff, a log excerpt or a
   recording is served as a first-class thing a person reads, stored as an artifact
   in the instance's data directory by content hash and referenced from a record by
   id — project truth, never an opaque attachment.

6. **At most five things ask for a word, re-ranked on every read.** The service serves
   the steward's attention as an ordered list of at most five calls, each arriving
   worked out — a recommendation and at most two trade-offs — and re-ranks it every
   time the desk is read; everything else keeps moving and is shown as such.

7. **What changed since you last read.** The service keeps a read cursor per person
   per project and serves the difference — documents, proposals, runs, calls — since
   the last read, so a return never begins with a search.

8. **Evidence over claims, details folded.** Every sentence on the desk that asserts
   a fact carries the evidence behind it one fold away; a run's state shows what is
   running against what was intended, and a claim with no evidence reads as a claim.

## What v1 deliberately does NOT freeze

- **A conversation with a manager session from the desk** (the console) — promoted
  when the agents seam names the write (`agent-types.v1` candidate open).
- **A UI copilot that edits a document beside the reader** — deferred on the
  steward's word (transcript, "an ephemeral UI copilot… later"); promoted when asked
  for again.
- **Phone and desktop as different layouts** — the app's own contract owns it.
- **Human-to-human review through a hosted forge (pull requests, comments)** —
  promoted when a second person joins a project.

## Conformance kit asserts

- A document edited on disk is re-served, with its new state word and history entry,
  within ten seconds; the app made no file read (measured with the app's file access
  denied).
- A question pinned to a paragraph survives an edit above it and still resolves.
- A fifth kind of write is refused with a sentence.
- The attention list never exceeds five and its order changes when a new call lands.
- An artifact is served by id and its content hash matches.

## Reserved / open questions (NOT frozen)

- Whether a ratification given on the desk is itself a record (the method part's
  `documents.v1` leaves this open; the first word given on the desk promotes it).
