# Experience Interface Contract — v2 candidate (DRAFT 2026-09-18)

Proposed replacement for `experience-interface.v1.md`; exact amendment pending owner review.

## Who builds against this

App hosts conversation and experiences; SDK supplies bindings; Agents connects managers.
Service admits durable effects; Reader supplies reading. Owners use public seams.

## What it is

One shell conversation helps the person across experiences and channels, driving a
manager under delegated authority with observable progress, direct steering and handback.

```text
phone / voice / SMS / notification reply / typed chat
  -> one conversation, identified participant and originating task context
  -> discover supported actions and current context <-> selected experience
  -> admitted operation / authorized manager -> receipt -> observed result
```

## The promises

1. **One conversation, explicit scope.** Changing experience or channel preserves
   conversation identity and continuity. Each event retains participant, project
   or absence, source channel and causal references; browser/activation are explicit
   where applicable. A delayed reply never borrows the screen's newer scope.
   Delivery, transcript correction and retry cannot create duplicate decisions.
2. **Discover before acting.** Compatible versions, renderers, artifact kinds and
   every user operation are advertised before use with inputs, outputs, effects
   and availability. Authorized agents and peer experiences use those operations,
   including navigation, disclosure, draft editing and presentation. Missing
   handlers, incompatible versions and unavailable operations give a reason.
3. **Context is bounded and quiet.** Shell, experiences and authorized managers
   exchange revisioned context in both directions, including only declared draft
   fields. Context grants no tools or permissions. Passive updates create no
   conversation turn or unsolicited speech; an intentional notification retains
   its reason and task reference in the conversation.
4. **One operation across modalities.** UI and conversational intent reach the
   same admission and exact revision checks. Clear authorization needs no extra
   click solely because it was spoken or typed. Taking control, interrupting and
   handing back report their actual scope and effect. Exact retries settle once;
   changed reuse is refused and unknown effects are reconciled before another try.
5. **Progress carries its evidence.** The person can inspect intent, progress,
   uncertainty and intervention needs without opening a manager session. Arrival,
   admission, application, durable commit, rendering and independent verification
   remain distinct. Notifications and assistant summaries preserve those meanings;
   receipt or worker report alone cannot claim a checked outcome or ratification.
6. **Replacement preserves continuity.** Compatible installed implementations
   declare version checks, lifecycle, state transfer and recovery. Replacement
   preserves conversation, canonical records and declared draft/view state or
   explains an incompatibility before disposal. Late results keep original scope;
   subscriptions are cleaned up, independent workers survive, actions never replay.
7. **References keep their meaning.** Read, reveal, comparison and decision name
   the exact project, artifact and revision. Feedback keeps the intended source
   span, origin and explicit destination; a later yes or goodbye cannot replace it.
   Channel replies retain their target and are clarified when intent is ambiguous.
8. **Presentation cooperates across owners.** Experiences declare semantic regions
   and supported choices; shell settings combine accessible defaults, user choices
   and authorized agent customization with explicit precedence and applied,
   adjusted or unsupported results. Reading, changes, review and history are
   outcomes, not prescribed views. Supported renderers preserve actions and meaning.

## Not in v2

- Provider protocols, vendors, audio storage and schemas: owners version these when needed.
- Arbitrary downloaded implementations: propose trust and isolation before admission.
- New decision authority: existing Service, Method and Queue ownership still applies.
- A required visual layout or closed theme list: prove supported choices with consumers.

## How the kit checks it

- Continue a task from typed chat to voice to SMS and back, across experiences,
  with one history; duplicate delivery, late replies and corrected transcripts do
  not duplicate actions or change project/revision. No browser is assumed on a call.
- Discover and invoke every user operation through the catalog; compare UI and
  agent outcomes, including disabled reasons, scoped local state and stale requests.
- Observe quiet context in both directions and declared draft redaction; intentional
  notifications are explainable, while navigation alone never starts a response.
- Interrupt an in-flight manager, observe what stopped or remains unknown, steer
  directly, then hand back without losing context or repeating an uncertain effect.
- Show refused, pending, unknown, observed and independently checked outcomes
  distinctly in the canvas and every channel, without inventing approval.
- Replace an installed implementation during a draft and in-flight action; preserve
  declared state, refuse incompatible transfer and recover a failed activation.
- Preserve exact comparison and feedback references across newer revisions/turns.
- Complete the same review in narrow/wide layouts, existing presets and supported
  customization; producer -> renderer -> action -> owner update -> render must pass.

## Open questions

See [owner decisions and acceptance scenarios](../docs/workflow/UNIFIED-EXPERIENCE-20260918.md).
Existing v1 remains authoritative until the exact amendment is accepted.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-18 | Proposed continuity, complete action parity, replacement and cooperative presentation. | Brian's product clarification; catalog drift and missing control coverage recorded in the linked owner review. |
