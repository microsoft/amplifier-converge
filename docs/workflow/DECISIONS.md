# Decisions — the steward's words, verbatim

## 2026-09-06 — on the plan's sheet
> "1) yes, 2) yes, 3) go, 4) let's discuss... if we ARE going to run in terminal, then the value of tmux is that we can also attach as users, they survive disconnects and restarts of the parent service (as long as wired properly) and so on."

1. Six parts including `method` as its own repository — **yes**.
2. Service and agents as two repositories with `agent-types.v1` between them — **yes**.
3. Phase 0 by part-manager sessions performing their own first wakes in parallel — **go**.
4. The terminal-multiplexer constraint — **open**; the steward's requirement is attachability and survival across disconnects and service restarts, which a multiplexer provides when wired properly.

## 2026-09-06 — a design-safety rule
> "Let's build in some design safety such that any part of this system that grows to a certain point of complexity or potential for splitting on some sub-domain should be split out out into it's own sub-project/repo/etc - I could see some of these going way."

Recorded as vision principle 9 and family.v1 Core 9 (the split-out rule), both DRAFT.

## 2026-09-06 — on reading the vision
> "In the vision it says one command to install onto the Amplifier a personal already has - this should NOT require or be dependent upon any Amplifier installation already existing, etc. We just package support for Amplifier as an agent and one of the defaults ready to configure, but that is just for the agent part and they could choose to never use/configure the Amplifier agent option. When you say running in every project's own workspace and no daemon, I'm not sure we're on the same page... we DO want to have one instance of Amplifier Converge running on the user's machine and then it'll be controlling many manager sessions, which are created from that UX - so it'll be up to the Converge app to create the workspace, pull down repos, etc. as we ideally don't want users to have to go to the terminal to do any of this... we manage it all for them."

Two corrections, applied across the family's documents and sent to every part's manager:
1. **No dependency on any other product.** Amplifier Converge installs on its own. Amplifier is one agent type, shipped ready to configure; a person may never configure it.
2. **One running instance per machine.** Amplifier Converge runs as one local instance with a browser UI; it owns its data directory, creates workspaces, clones repositories, launches and supervises manager sessions. A person never needs a terminal.

## 2026-09-06 — install and naming
> "Also assume uv installed (include how to install in readme) and that we will use `uv tool install git+https...` to install, and then the tool itself should have all of usual suspects, doctor, etc., for all the things we need to get it set up and running and check in on it, etc. For the short name, keep the branding please, amplifier-converge."

- A fresh machine is assumed to have `uv` (and `git`); the README says how to get `uv`.
- Install is `uv tool install git+https://github.com/bkrabach/amplifier-converge` — the family's front door is the installable, a package that composes the parts.
- The command is `amplifier-converge`; the data directory `~/.amplifier-converge/`; the service name `amplifier-converge`. No shorter alias.
- The command carries the usual suspects for setup and check-in — `doctor`, `setup`, `start`/`stop`/`restart`/`status`, `logs`, `open`, `update`, `uninstall`, `agents list|test` — and nothing that belongs on the screen (creating projects, attaching repositories, onboarding stay in the app).

## 2026-09-06 — the family level ratified
> "ok, look good to me at the amplifier-converge level, consider those all ratified."

Ratified as written: `docs/VISION.md`, `contracts/family.v1.md`, `contracts/service.v1.md`, `contracts/agent-types.v1.md`, `contracts/queue.v1.md`. Ratified is not locked: each stays DRAFT with the word recorded in its heading; locking is a later word once the four conditions hold. The five parts' documents await their own words.

## 2026-09-06 — vocabulary, and the method part
> "Let's use the term "split out" or similar, instead of "pealed" throughout? The method is ratified pending that global update."

- Every form of *split out* becomes a form of *split out* across the family and every part — a wording change with no change of meaning, applied by the family manager in one pass as the steward's global word (clause 8: a small repair in place, not five lanes for one word).
- The `method` part's documents are **ratified** as written once the wording is applied; heading and changelog carry the word.

## 2026-09-06 — two method proposals and the service part
> "do it, ratified for those two .v2 docs. Service is ratifed. I'll go read another."

- `method/contracts/documents.v2-candidate.md` and `method/docs/VISION.v2-candidate.md` — **ratified**; applied exactly, candidates archived. Consequence of documents clause 2: every heading in the family and its parts carries ONE state word — `(DRAFT)` · `(RATIFIED <date>)` · `(LOCKED <date>)` — re-stamped as a correction of form, no content changed.
- The `service` part's vision and `contracts/control-plane.v1.md` — **ratified**.

## 2026-09-07 — agents and queue ratified; the app definition to be re-derived
> "Please re-read the chatgpt transcript in ai-context, we're definitely missing the boat on a lot of stuff in the app definition. Make sure the rest of the repos properly support the things you add from there too. you can ratify agents and queue, but I think app definitely misses a lot."

- `agents` (vision + `contracts/agent-types.v1.md`) — **ratified**. `queue` (vision + `contracts/items-and-custody.v1.md`) — **ratified**.
- `app` — **not yet**: its vision and `experience.v1` are to be re-derived against the steward's UX transcript (`ai-context/ChatGPT-Analyze UX Vision Protocol Contracts-20260903-0546.md`, outside the repositories); whatever the app then needs of service, agents, queue and method is filed as seam notes or proposals against those parts.

## 2026-09-07 — the document format
> "port it, MUCH better!"

The shape in `proposed-format/FORMAT.md` is the family's document format from today. The family manager ports the family's six documents in place (ratified, not locked: a changelog row each); every part's manager ports its own; the method part applies the documents contract change first so its kit reads the new section names. The open inconsistency (the documents contract at 101 lines against its own 80-line bar) is the method manager's to resolve — a short spec split by topic with one contract naming the promises, or a stated exception.

## 2026-09-07 — the whole sheet
> "love it, lock it in, do it all, consider ratified, move them into place in the actual repos as I have some work to do as a result of them."

All sixteen items on `SHEET-2026-09-07.md` are **ratified**, and the recommendations carried on the sheet are taken as the word where an item asked for a ruling: M-10 → *the clause stands* (ratified documents are edited in place; the guard reads only LOCKED as locked); S-15 → refusal (b) reads as a sentence, (a) does not and is the service's to fix; S-14 → *prove it* (an isolated host, the family manager's item); #16 → *a split-out contract inherits the word when no promise changed*. "Lock it in" is read as commit to it; the state word given is RATIFIED. Locking (the third state) follows the method's four conditions when each document meets them.

## 2026-09-08 — the reviewers' recommendations
> "Yes, let's take those changes they recommended, let me know what you need there and _then_ we'll get to the deck when this is all sorted."

- The app's **reader split-out** (`docs/workflow/SPLIT-OUT-THE-READER.md`) — **ratified**: the document reader becomes a seventh family part; the three promises it carries move; no promise's words change.
- The queue's **ninth promise** folded to bring `items-and-custody.v1` inside the three-to-eight band — a correction of form, in place.

## 2026-09-08 — the six words of SHEET-2026-09-08
> "take all six - hold on deck until the other is _done_, please drive that work and monitor until complete."

The family manager's recommendations are the word: **limits** → ratify `hosts-and-limits.v2` (count code, not prose) AND split session persistence out as an eighth part, `sessions`; **console-home** → one home, the family seam; the agents part undoes its copy; **priority** → `items-and-custody.v2` ratified; **refusals** → passable (S-15 closed); **M-17** → stop, no history rewritten; **seam-gaps** → go, the app's desk-record gaps are filed into the service's queue.
