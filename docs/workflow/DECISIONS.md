# Decisions — the steward's words, verbatim

## 2026-09-06 — on the plan's sheet
> "1) yes, 2) yes, 3) go, 4) let's discuss... if we ARE going to run in terminal, then the value of tmux is that we can also attach as users, they survive disconnects and restarts of the parent service (as long as wired properly) and so on."

1. Six parts including `method` as its own repository — **yes**.
2. Service and agents as two repositories with `agent-types.v1` between them — **yes**.
3. Phase 0 by part-manager sessions performing their own first wakes in parallel — **go**.
4. The terminal-multiplexer constraint — **open**; the steward's requirement is attachability and survival across disconnects and service restarts, which a multiplexer provides when wired properly.

## 2026-09-06 — a design-safety rule
> "Let's build in some design safety such that any part of this system that grows to a certain point of complexity or potential for splitting on some sub-domain should be peeled out into it's own sub-project/repo/etc - I could see some of these going way."

Recorded as vision principle 9 and family.v1 Core 9 (the peel-out rule), both DRAFT.
