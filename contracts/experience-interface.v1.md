# Experience Interface Contract — v1 (DRAFT)

The shared exchange between the shell, experience implementations and their
service and agent adapters; the SDK implements this promise, it does not own it.

## Who builds against this

The app hosts independently owned experiences. The experience SDK supplies
compatible bindings and a conformance harness. The service admits durable
effects, agents report observed execution, and the reader supplies document
reading. Each owner depends on this seam, not another owner's private files.

## What it is

An installed implementation declares what it understands and can display.
The host supplies the current scope; requests and results keep that scope.

```text
compatible implementation + declared operations + renderer profile
  -> conversation / selected project / browser / activation
  -> bounded current context and exact artifact references
  -> admitted action -> typed result -> observed effect
```

## The promises

1. **One explicit originating scope.** Exchanges identify conversation, selected
   project or its absence, browser and activation. Unbound means that project's
   setup state; no first-project fallback or late effect on a different scope.
2. **Compatibility precedes activation.** Open implementation identifiers,
   versioned operations, artifact kinds and renderer profiles are declared before
   use. Missing required handlers or incompatible versions fail with a reason.
3. **Context does not grant authority.** Both sides publish bounded, revisioned
   context and current availability. Only declared draft fields cross the seam;
   updates cause no speech by themselves and cannot widen tools or permissions.
4. **Every modality uses one action.** Click, keyboard, voice and text reach the
   same admitted operation and revision checks. Identical request reuse settles
   from its receipt; changed reuse is refused; uncertain effects are not replayed.
5. **Receipt and effect stay separate.** Arrival is not admission; admission is
   not application, durable commit or rendering. A lost acknowledgment remains
   unknown. A worker report or UI result is not an independent manager check.
6. **Presentation does not own work.** Activation/disposal cleans up view work,
   subscriptions and scoped drafts as declared, without cancelling independent
   workers or erasing conversation. Late presentation results cannot cross scopes.
7. **Artifacts and feedback retain identity.** Reads/reveal name project, kind,
   identity and revision. Feedback freezes the intended source span, origin and
   explicit destination; later yes/goodbye cannot replace it or supply approval.
8. **Renderers preserve shared meaning.** React and eligible A2UI profiles use
   the same context/actions/artifacts and host presentation settings. An unsupported
   profile is explicit. A profile is supported only after its two-way proof passes.

## Not in v1

- Provider wire formats and execution internals — revise the seam only when
  two admitted adapters cannot express the same required interaction.
- Arbitrary runtime installation or downloaded catalogs — propose trust and
  isolation first when a real untrusted implementation must be admitted.
- Exact field spelling and resource-limit values — version them in SDK schemas
  and publish measured compatibility before peers depend on a release.

## How the kit checks it

- Two projects, two browsers and a late response never cross originating scopes.
- A fifth compatible implementation needs configuration, not a fixed-ID edit;
  incompatible versions, undeclared actions and missing handlers fail before use.
- Passive context updates do not speak, commit drafts or reveal undeclared data.
- The same operation via UI and assistant has the same scope, checks and result.
- Lost acknowledgments do not replay; committed/rendered/applied claims carry
  their own evidence, separate from arrival and method outcomes.
- Deactivation removes subscriptions while conversation and independent work remain.
- Feedback source survives subsequent turns; product destination and origin remain
  distinct, and exact-version decision safeguards are unchanged.
- Independent producer -> renderer -> edited value/action -> owner receipt/update
  -> observed render passes, including wrong-scope/catalog and unavailable cases.

## Open questions

No new authority is assigned to an experience or SDK. Service admission, Queue's
sole custody, Method decisions and Reader ownership remain their existing seams.
An owning contract conflict must be proposed before dependent implementation.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-16 | First draft, not ratified. | Mixed project views, incorrect feedback-span capture and a fixed replacement interface require a shared scope/action boundary; reviewed source and the split packet preserve the observations. |