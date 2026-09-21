# Repository migration — 2026-09-20

The private Microsoft repository preserves the original repository history and
uses `main` as its working/default branch. This is a history-preserving copy,
not a GitHub repository transfer. Original PR discussions and check metadata
remain in the source repository.

All source branch heads and PR heads are retained under `migration/source/*`
and `migration/source-pr/*`. [Source PR 4](https://github.com/bkrabach/amplifier-converge/pull/4)
is integrated without rewriting its commits.

The collaborative-capabilities document remains a draft proposal; merging its
file does not ratify it, resolve the embedded Service boundary or establish
product acceptance. Current registry URLs for this repository, Method, Service,
Agents and Queue now point to their verified Microsoft destinations on `main`.
The app, reader and sessions repositories are outside this migration and retain
their original URLs. Historical publications and original PR links remain intact.

The README installation section still describes the intended product entry
point, not an installable release: this repository contains documents and the
family registry. Its existing conformance kit checks registry reachability and
seams; unavailable application/runtime observations remain explicitly unverified.
No running installation, workspace or native conversation data is changed.
