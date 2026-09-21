# Amplifier Converge

The app a person opens to get work done the Converge way — vision first, contracts as
the law, work derived from the gap between the two — with a team of agents doing the
work. One instance on a person's machine, installed on its own and depending on
nothing else, that creates workspaces, clones repositories, launches and supervises
manager sessions, and puts every call a person must make on one screen. One
experience made of several small Converge projects, held together by contracts at
their seams; bring your own agent.

## Install

Repository and checkpoint links in this document require access to the private
Converge repositories; they are intended for authorized collaborators.

Amplifier Converge needs `uv` and `git` on the machine, and nothing else.

```sh
# uv — one line, from https://docs.astral.sh/uv/getting-started/installation/
curl -LsSf https://astral.sh/uv/install.sh | sh          # macOS, Linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex" # Windows

# Amplifier Converge
uv tool install git+https://github.com/microsoft/amplifier-converge
amplifier-converge            # starts the instance and opens the browser
amplifier-converge doctor     # says, in plain words, what is ready and what is not
```

The command carries the usual suspects for setup and check-in — `doctor`, `setup`,
`start` / `stop` / `restart` / `status`, `logs`, `open`, `update`, `uninstall`,
`agents list` / `agents test <type>`. Creating projects, attaching repositories and
onboarding them happen on the screen, never here. The instance keeps everything
under `~/.amplifier-converge/`.

*The install flow above describes the intended product entry point, not a verified
end-to-end release. Development checkpoints and their limits are recorded in
[the September 18 publication brief](docs/workflow/PUBLICATION-20260918.md).*

## What is here

This repository is the top level. It holds the family's vision, the seam contracts,
the registry of parts (`family.toml`) and, once seeded, the ledger that reads the
seams. It holds no part's internals.

- `docs/VISION.md` — where this is going (RATIFIED)
- `contracts/family.v1.md` — how the parts compose (RATIFIED)
- `contracts/service.v1.md` — one API is the truth (RATIFIED)
- `contracts/agent-types.v1.md` — what a type owes the family, and attach-and-survive (RATIFIED)
- `contracts/queue.v1.md` — items, claim, one custody owner, plain words (RATIFIED)
- `contracts/experience-interface.v1.md` — the shared shell/experience exchange (RATIFIED)
- `contracts/service.v2-candidate.md` — proposed initial creation/authoring authority (DRAFT; not ratified)
- `family.toml` — the parts and their status (`seeded` · `body` · `retired`)
- `docs/FORMAT.md` — how our visions and contracts are shaped, and why
- `docs/PLAN-vNext-2026-09-06.md` — the plan under discussion
- `docs/workflow/` — the manager session's records for this project
