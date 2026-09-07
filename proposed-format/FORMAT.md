# A proposed format for our visions and contracts

*What we read, what makes it readable, and the shape proposed here. Everything under
`proposed-format/` is a draft for review beside the current documents; nothing in it is
law until it is ported over.*

## What we read

Cortex's contracts (`pack-card.v1`, `memory-pack.v1`, `composer.v1`, `midcall-injection.v1`,
`gateway-client-api.v1`), the Smart Tools specification (`spec/README.md`, `structure.md`,
`manifest.md`, `invocation.md`, `packaging.md`), and two visions (`drumbeat/docs/VISION.md`,
`cortex-hub/VISION.md`) — against our fourteen contracts and six visions.

## What makes theirs readable, and where ours drifted

| Theirs | Ours today |
|---|---|
| **Show the thing first.** A YAML card, a verb table with `→ {json}` out, a request/response shape. The rules come after the reader has seen the artifact. | Rules only. A reader of `service.v1` never sees what a `run` record looks like. |
| **Short declarative sentences, concrete nouns.** "Every declared bin MUST conform to agent-tool.v1 core." | Long sentences with em-dashes and abstractions: "the record is the truth; output is telemetry." |
| **Few teeth, each named in three to six words**, two to four lines: the rule, its consequence, who feels it. | Ten-to-fourteen teeth per contract, each a dense paragraph; clause numbers cross-referenced everywhere. |
| **Delegate, don't restate.** "All verb discipline lives in agent-tool.v1 and is deliberately not restated here." | We restate the method inside product contracts (merge gates, verification, four calls appear in four places). |
| **Rules stated as tests.** "The test is whether removing the wrapper would lose anything a different caller might want." | Rules stated as doctrine; the test is left to the kit section. |
| **Changelog as a table: Date · Change · Evidence.** | Bullet prose. |
| **A one-line frame at the top** saying what kind of document this is and how it changes. | An italic drafting note. |
| **Vision: "What X is" in one paragraph; principles as titled subsections, one paragraph each; "what this deliberately resists."** | Four long paragraphs of "where this is going", then eight aphoristic principles. |
| **No meta about the method inside product documents.** | "What this can prove and what it cannot" sections in documents about an app. |

The register is the difference. Theirs read like a good README written by an engineer
who has to build the thing on Monday. Ours read like a manifesto. Our audience — a
steward, a manager session on its first wake, an engineer picking up a part — needs
the README.

## The proposed contract shape

```
# <Name> Contract — v1 (<STATE> <date>)

One line: what this document governs and who reads it.

## Who builds against this
Two sides, named. One paragraph.

## What it is
Two or three plain sentences. Then SHOW IT: a code block with the artifact —
a file, a record, a request and response, a command and its output.

## The promises            ← three to eight, each 2–4 lines
1. **Three-to-six-word name.** The rule in one sentence. What a reader would
   see if it were broken. Who is affected.

## Not in v1                ← what is deliberately left open, each with the trigger that promotes it
## How the kit checks it    ← bullets of observations, one per promise where a machine can look
## Open questions           ← honest, short
## Changelog                ← table: Date | Change | Evidence
```

Fifty to eighty lines. A contract that needs more is two contracts, or its surface
belongs in a spec split by topic (as Smart Tools does) with one short contract naming
the promises.

## The proposed vision shape

```
# <Project> — Vision (<STATE> <date>)

Six lines: what a vision is here, and how it changes (amend first, then file work).

## What <project> is         ← one paragraph a newcomer can repeat back
## Principles                ← numbered ### subsections, a title and one paragraph each
## What this deliberately resists
## How you can tell it is working   ← a person and a number in every line
## Changelog                 ← table
```

Eighty to a hundred lines before the changelog. One idea per paragraph; if a sentence
needs a dash to hold two ideas, it is two sentences.

## What porting costs

- The method part's `documents.v1` fixes section names and sizes (its clauses 3 and 4);
  the format change is a candidate against it — drafted here as
  `method/contracts/documents.v1.md` so the law and the shape land together.
- Every kit that reads a heading (`## Core`, `## Conformance kit asserts`) reads the new
  names; the method's documents kit is the only one today.
- Content does not change: every promise in a current contract appears in its proposed
  version, renamed and shortened, never dropped. The port is a rewrite of form under a
  changelog line, done by each part's own manager once the shape is agreed.

## What is here

- `family/VISION.md` and `family/contracts/*.md` — the family's six documents in the new shape.
- `method/contracts/documents.v1.md` — the law about documents, amended to permit the shape.

Read `family/contracts/service.v1.md` first: it is the shortest and shows the pattern.
