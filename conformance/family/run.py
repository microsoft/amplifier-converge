#!/usr/bin/env python3
"""The family kit -- the first reader of family.toml (contracts/family.v1.md, Conformance kit asserts).

Usage: python3 conformance/family/run.py [repo-root]   -> JSON {verdict, results:[{rule,status,detail}]}
PASS / FAIL / CANT_CHECK only. A rule that needs a body that does not exist yet says CANT_CHECK and why.
"""
import json, pathlib, subprocess, sys, tomllib

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
STATUSES = {"seeded", "body", "retired"}
res = []
def r(rule, status, detail): res.append({"rule": rule, "status": status, "detail": detail})

try:
    fam = tomllib.loads((ROOT / "family.toml").read_text())
    parts = fam.get("part", [])
    bad = [p.get("id") for p in parts if not all(k in p for k in ("id", "url", "branch", "seams", "status")) or p.get("status") not in STATUSES]
    r("3a", "FAIL" if bad or not parts else "PASS", f"{len(parts)} part(s); malformed or unknown status: {bad}" if bad else f"{len(parts)} part(s), every one with id, url, branch, seams and a status from the three words")
except Exception as e:
    r("3a", "FAIL", f"family.toml does not parse: {e}"); parts = []

# 3b: every url answers at its branch and carries docs/VISION.md and contracts/
missing = []
for p in parts:
    url, br = p["url"], p["branch"]
    try:
        out = subprocess.run(["gh", "api", f"repos/{url.split('github.com/')[1]}/contents/?ref={br}"], capture_output=True, text=True, timeout=30)
        names = {e["name"] for e in json.loads(out.stdout)} if out.returncode == 0 else set()
        vis = subprocess.run(["gh", "api", f"repos/{url.split('github.com/')[1]}/contents/docs/VISION.md?ref={br}"], capture_output=True, text=True, timeout=30).returncode == 0
        if not vis or "contracts" not in names: missing.append(p["id"])
    except Exception:
        missing.append(p["id"])
r("3b", "FAIL" if missing else "PASS", f"parts without a reachable docs/VISION.md and contracts/ at their branch: {missing}" if missing else f"all {len(parts)} part(s) answer and carry docs/VISION.md and contracts/")

# seams named exist here
seams = {s for p in parts for s in p.get("seams", [])}
absent = [s for s in seams if not (ROOT / "contracts" / f"{s}.md").exists()]
r("seams", "FAIL" if absent else "PASS", f"seam contracts missing at the top level: {absent}" if absent else f"every named seam exists: {sorted(seams)}")

# Core 1: no part directory here (a part's body must not live at the top level)
claimed = {"app", "service", "agents", "queue", "adapters", "src"}
present = [d for d in claimed if (ROOT / d).is_dir()]
r("1", "FAIL" if present else "PASS", f"part directories at the top level: {present}" if present else "no part's directory lives at the top level")

# Core 8: every part's first contract names a ceiling and a second-domain test (read from the checkout beside this repo if present)
noceil = []
for p in parts:
    if p["id"] == "amplifier-converge": continue
    c = ROOT.parent / f"amplifier-converge-{p['id']}" / p.get("first_contract", "")
    if not c.exists(): noceil.append(f"{p['id']}: no local checkout to read"); continue
    t = c.read_text().lower()
    if "ceiling" not in t or ("second domain" not in t and "second-domain" not in t): noceil.append(p["id"])
r("8", "FAIL" if [x for x in noceil if ":" not in x] else ("CANT_CHECK" if noceil else "PASS"), f"{noceil}" if noceil else "every part's first contract names a ceiling and a second-domain test")

# the picker (needs the app) and the state directories (needs the instance)
r("picker", "CANT_CHECK", "no app body exists yet to read the picker from")
r("6", "CANT_CHECK", "no instance exists yet; no project state directories to compare")

verdict = "FAIL" if any(x["status"] == "FAIL" for x in res) else "PASS"
print(json.dumps({"verdict": verdict, "results": res}, indent=1))
