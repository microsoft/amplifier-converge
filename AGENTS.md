# Working in this repository

This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.

This repository develops the Amplifier Converge methodology. Start with README.md, docs/VISION.md, and the applicable contracts. For work applying the method elsewhere, use guides/agent-guide.md; for a guidance review, use guides/reviewer-guide.md.

Keep the shared promises portable across people and agent systems. Put practical application in the guides, with links to the governing contracts. Keep the methodology independent of a particular runtime, database, application, or agent framework. Project contracts may deliberately commit to technologies, architecture, interfaces, and detailed experience behavior.

Use plain language, concrete examples, and just enough detail to act or judge. Keep technical and experience details when they define something others must rely on; brevity must not make a commitment ambiguous. Preserve one authoritative home for each promise. Independent decisions within delegated authority are the normal mode; do not add approval gates for routine implementation or ordinary editorial work. Proactively expose consequential gaps in direction before dependent implementation and help resolve them; check clarity for the next outcome, not completeness of the whole project.

When editing a commitment, consider the behavior and audience it affects. Keep implementation detail and review evidence out of the vision. Describe the methodology directly; do not add migration notes, references to previous implementations, or a changelog.

For documentation changes, inspect the complete changed passages, check local links and references, and walk through a relevant scenario. Do not claim a documentation review proves live execution. Do not provision an application or install dependencies just to review prose.

## Ecosystem maps

Keep this repository's README and product-page maps aligned with the
[Constellation map guide](https://github.com/microsoft/amplifier-constellation/blob/main/docs/ecosystem-maps.md)
and its canonical registry; start with this repository's
`docs/ecosystem-map.json`. When creating, renaming, splitting, retiring, or
changing a role, interface, parent, or dependency, inspect incoming and outgoing
relationships and update every affected parent/consumer map and link, including
the centralized product pages. Regenerate from source data and synchronize local
records/images rather than hand-editing generated images. Describe actual
boundaries and optional choices; a role highlight is not a compatibility claim.
Documentation work does not authorize deployment or resume paused product work.
