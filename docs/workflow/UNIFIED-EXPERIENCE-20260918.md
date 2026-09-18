# Unified conversation and experience alignment

September 18, 2026. Proposed owner coordination for
[`experience-interface.v2-candidate.md`](../../contracts/experience-interface.v2-candidate.md).
This is a review proposal, not a new runtime API or evidence of implemented behavior.

## Product direction

Brian confirmed that Converge should do as much of the underlying work as it can,
with useful instrumentation, optional direct intervention and an easy return to
delegation. Users need not learn the orchestration machinery to use the product.
Separate reader views are optional. Every user action must also be available to
an agent under equivalent authority.

Experiences remain independently owned and replaceable. Presentation is shared
across the shell: experience developers declare supported structure and choices;
users, or agents acting for them, choose or define a presentation. Current themes
are examples. Experiences advertise their capabilities and exchange context with
the shell conversation, authorized managers and other experiences.

The shell has one continuous conversation across phone/voice, SMS/notifications
and typed chat, across experiences. It drives the manager on the user's behalf.
Switching channels or canvases must not require restarting the explanation.
Brian authorized communicating these revisions through PRs and PR comments.

## What must be decided together

| Owner | Bounded responsibility | Review question / next deliverable |
|---|---|---|
| Family | Shared meaning and scope | Review the v2 candidate against each existing v1 promise; accept an exact revision before dependent schema changes. |
| App | Conversation orchestration and channel continuity | Propose a channel-neutral conversation binding, routing and visible history; render manager state and expose direct control without creating another conversation per experience. |
| Service | Canonical conversation/action records and admission | Identify existing event, identity, action and receipt operations; propose only missing durable semantics. A channel identifier alone is not verified participant authority. |
| SDK | Discovery, context and lifecycle | Publish versioned action input/result/effect declarations, availability with reasons, local-state operations, context subscriptions and compatible replacement/state transfer. Map to existing types before adding another interface. |
| Agents + Sessions | Authorized manager connection | Drive managers through their public control boundary; publish intent and observed execution; define interrupt, steer, resume and handback results. |
| Operation | Instrumentation and intervention | Present meaningful progress and uncertainty, with optional deeper manager interaction and the same public controls used by the conversation. |
| Reader | Reading outcomes | Replace exactly four views with accessible reading, changes, proposal comparison and history outcomes. Keep legal edits, exact revisions and reading-position retention. |
| Direction | Document intent and review | Consolidate declarations, inventory user-control parity, show truthful action results, then build a natural document/proposal journey against the agreed shared interfaces. |
| App + SDK + experiences | Cooperative presentation | Document precedence, supported semantic regions and customization results; keep state stable when presentation changes. |
| Method + Service | Consequential decisions | Confirm existing exact-version authority works for explicit conversational intent; ambiguous replies require clarification, clear authorization needs no modality-specific second click. |

No owner is assigned access to another part's internal files or tables. This
proposal does not merge the pending initial-project/first-document admission
proposal or the SDK's separate canonical-shell correction.

## Conversation behavior to agree before a provider integration

One conversation is a durable logical identity, not one transport connection or
one model context window. Its connected channels read the same authorized record.
Distinct conversations and participants remain isolated. Project context belongs
to the event/task; selecting a project in a browser does not rewrite older turns.

Adapters must preserve conversation and participant references, channel event
identity, causality/reply target, originating project or explicit absence, and
artifact/decision revision where relevant. Owner-assigned ordering and provider
event IDs support reconciliation and duplicate detection. These are semantic
requirements, not proposed JSON fields. Credentials stay in the owning adapter.

Delivery, transcript and action identities are different. Replayed delivery must
not create a second intent; a changed transcript must not silently revise an
already executed action. A genuine new instruction receives its own identity.
Interrupted calls and lost acknowledgments resume from recorded state, with an
unknown effect reconciled before a repeated operation.

A notification is an intentional delivery of a conversation event, not permission
to act. Its reply references the original task and exact decision. If that target
is ambiguous or changed, ask a focused clarification. A fresh browser selection,
a delivery acknowledgment or a transcription fragment cannot supply consent.
The channel must present enough information for the requested decision; otherwise
offer an accessible way to inspect it or defer the decision.

With no browser open, authorized durable work can continue through the same public
operations. A view-only action identifies the intended presentation activation or
reports that it is unavailable; adapters must not fabricate a live browser scope.
Opening a browser later shows canonical outcomes and scoped pending review state.
Availability in each channel is explicit rather than silently losing a control.

## Acceptance scenarios

1. **Continue across channels.** Start a document change in chat, discuss it on a
   call, receive a requested SMS notification and reply there. Reopen Direction
   and then Operation: the same conversation shows the intended task, exact
   proposal and outcome. No repeated onboarding or new per-experience history.
2. **Keep a delayed reply safe.** A notification concerns Project A revision 7.
   The browser moves to Project B and A advances to revision 8. A reply still
   names A/7; it cannot authorize B or silently substitute A/8. Show what changed
   and clarify if needed. Clear authorization of a still-valid exact action can
   proceed without demanding another click.
3. **Recover delivery and calls.** Deliver the same SMS twice, reconnect a call
   and correct a transcript after an action was admitted. Observe one original
   effect, traceable event reconciliation and explicit handling of changed intent.
4. **Work without a canvas.** With no browser open, query manager progress and
   steer an authorized task. Later open the App and see the same history/results.
   A request to reveal a document reports which presentation receives it or why
   none is available; it does not pretend a phone has rendered the browser.
5. **Act from discovery alone.** A test consumer discovers, reads current values
   and invokes selection, reveal/fold, draft editing/save and supported presentation
   changes. Compare the resulting state/receipts with human controls. Refuse stale
   scope, undeclared operations and unavailable capabilities with useful reasons.
6. **Observe and take control.** The user sees the current objective, actual
   progress, what needs attention and what is uncertain. Interrupt during a
   write; report stopped, pending or unknown truthfully. Steer directly and hand
   back without repeating a possibly completed effect or losing the instruction.
7. **Change presentation.** Complete one review at 390 and 1280 pixels using the
   existing presets and one supported custom presentation. Selection and draft
   survive; keyboard and assistive-technology access remain; unsupported choices
   receive an explicit report. Read/changes/review/history need no mandated tabs.
8. **Replace an experience.** Swap a compatible installed Direction version with
   a draft and an in-flight action. Test successful transfer, rejected transfer
   and failed activation/rollback. Conversation, canonical records and independent
   work survive; old callbacks cannot affect a new scope or replay a write.
9. **Stay quiet and scoped.** Switch selections, receive a manager observation
   and update a declared draft field. Context updates both ways without speaking.
   Undeclared drafts and another participant's context never appear. A deliberately
   requested notification is recorded with its trigger and target.

## Evidence and implementation order

The September 18 Direction pilot has a Service-backed source-preserving candidate
save path and presentation checks. Its static manifest and mount manifest disagree
on renderer identity, Reveal/Compare handlers and Save's revision/content schema.
Several UI controls change local React state without a public agent equivalent.
This directly motivates trustworthy discovery and a control inventory before
claiming universal human/agent parity.

The current family v1 already requires scoped actions across modalities, quiet
context, lifecycle cleanup and distinct receipt/effect evidence. The candidate
extends those promises; it does not discard the prior work. The current Reader
contract requires exactly Reading, Changes, Review and History, which overstates
the intended interaction constraint.

First publish the handed-off Direction source; correct its existing declarations
and outcome messages; review these shared amendments; then implement the smallest
App/SDK/Agents conversation-to-action slice with real consumer evidence. Add channel
adapters against that same slice. Telephony, SMS delivery, custom presentation and
live replacement remain acceptance targets until their end-to-end checks pass.
