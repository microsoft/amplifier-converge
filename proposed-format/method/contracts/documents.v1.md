# Documents Contract — v1 (RATIFIED 2026-09-06 · v2 candidate: this shape)

How a vision and a contract are written, sized, ratified, locked and amended. Read by
every manager session that drafts one, every steward who answers one, and the documents
kit that checks them.

## Who builds against this

**Manager sessions** write and amend them. **The steward** answers them in one word.
**The documents kit** reads them. **Every part's** contracts and vision are instances.

## What it is

Two kinds of document carry a project's direction:

```
docs/VISION.md            what the project is when it is right — present tense, no dates in the body
contracts/<name>.vN.md    one promise the project keeps, with teeth a machine can read

# <Name> Contract — v1 (DRAFT | RATIFIED <date> | LOCKED <date>)     ← one state word
## Who builds against this   ## What it is   ## The promises   ## Not in v1
## How the kit checks it     ## Open questions   ## Changelog (Date | Change | Evidence)

# <Project> — Vision (<state>)
## What <project> is   ## Principles (### numbered)   ## What this deliberately resists
## How you can tell it is working   ## Changelog
```

A change to a locked document is a proposal beside it: `<name>.vN-candidate.md`, in
the shape *what changes → why → evidence → what does not change → questions → decision*.

## The promises

1. **Two kinds of document, and only two.** A vision says where; a contract says what is
   promised. Anything else is a note, and a note binds nobody.

2. **One state word in the heading.** *DRAFT* while argued about; *RATIFIED* the moment
   the steward gives the word; *LOCKED* once settled. No word reads as draft; two words
   read as no state, and re-stamping to the one earned is a correction of form.

3. **Sizes.** A vision is a hundred and twenty lines before its changelog. A contract is
   fifty to eighty lines; one past eighty is two contracts, or a spec split by topic with
   one short contract naming the promises. A document nobody finishes is a promise nobody
   keeps.

4. **Fixed sections, in the order above.** A reader finds the same thing in the same
   place in every document. Promise numbers never move once a document is ratified.

5. **Show the thing before the rules.** Every contract's "What it is" carries the
   artifact — a file, a record, a request and response, a command and its output — so a
   promise is read against something concrete.

6. **A promise names what broken looks like.** Two to four lines: the rule, what a reader
   would observe if it were violated, who is affected. Register: a good README, not a
   manifesto — short sentences, concrete nouns, no dash holding two ideas.

7. **Every sign that a vision is working names a person and a number.** A sign nobody
   could observe happening to somebody is cut.

8. **Delegate, don't restate.** A contract that depends on a promise made elsewhere names
   the document and stops. The method's own rules are not repeated inside a part's
   contract.

9. **Four things before a lock.** Ratified content; a kit that reads every promise; one
   real implementation or reading against it; and a worked example. Locking is one write:
   the heading and the changelog row land together.

10. **Locked means proposal-only.** A locked document is never edited in place; it changes
    by a candidate beside it and the steward's one word: *ratified · ratified with edits ·
    declined · later*. A ratified-but-unlocked document is edited in place with a
    changelog row.

11. **Ceiling and second domain.** This part's law stays under six hundred lines and no
    contract over eighty. A second vocabulary inside it is split out, not absorbed.

## Not in v1

- **Whether a ratification is also a record the control plane holds** — the first time a word is given on the desk.
- **A template for the proposal file** beyond the six-part shape — the first time two proposals disagree on form.
- **Stable paragraph anchors** in served documents (`desk.v1` asks for them) — a convention the templates can carry; drafted when desk.v1 has a word.

## How the kit checks it

- Every document under `docs/` and `contracts/` carries exactly one state word in its first heading.
- Every contract has the seven sections in order; every vision the five.
- No contract exceeds eighty lines; no vision exceeds a hundred and twenty before its changelog.
- Every contract's "What it is" contains a fenced block.
- Every "How you can tell it is working" line contains a number and a person-noun.
- A locked document has no commit editing it in place after its lock row.

## Open questions

- Whether "eighty" is right, or whether the band should be stated as a reading time.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-06 | v1 drafted at the method part's first wake; ratified. | Steward's word. |
| 2026-09-06 | v2 ratified: one state word per heading; a vision is 120 lines before its changelog. | Two headings carrying two words read as no state by the kit. |
| 2026-09-07 | **Candidate (this file):** section names renamed and reordered; contracts 50–80 lines; "show the thing" and "delegate, don't restate" added as promises; changelog as a table. Motivated by the steward's reading: the current documents "read like a manifesto". | `proposed-format/FORMAT.md`; the comparable contracts read there. |
