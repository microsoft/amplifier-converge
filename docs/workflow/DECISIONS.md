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
