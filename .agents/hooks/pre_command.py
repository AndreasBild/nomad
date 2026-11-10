#!/usr/bin/env python3
"""
Antigravity PreToolUse Lifecycle Hook for Nomad.
Deterministically enforces working-tree hygiene (no blind git add)
and branch protection (no direct commits/pushes to master).
"""

import json
import re
import subprocess
import sys


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        print(json.dumps({"decision": "allow"}))
        return

    tool_call = payload.get("toolCall") or {}
    args = tool_call.get("args") or {}
    cmd = args.get("CommandLine") or ""
    cwd = payload.get("cwd") or "."

    # 1. Block blind git staging (git add ., git add -A, git add --all)
    if re.search(r"(?:^|[;&|]\s*)git\s+add\s+(?:\.|--all|-A)(?:\s|$|[;&|])", cmd):
        print(
            json.dumps(
                {
                    "decision": "deny",
                    "reason": "Blocked by Nomad git-hygiene-guard: Never run 'git add .' or 'git add -A'. Stage modified files explicitly (git add <file>).",
                }
            )
        )
        return

    # 2. Block direct git commit on master or git push to master
    if re.search(r"(?:^|[;&|]\s*)git\s+push\s+\S+\s+master(?:\s|$|[;&|])", cmd):
        print(
            json.dumps(
                {
                    "decision": "deny",
                    "reason": "Blocked by Nomad git-hygiene-guard: Direct pushes to 'master' are prohibited. Push a feature/*, fix/*, or chore/* branch instead.",
                }
            )
        )
        return

    if re.search(r"(?:^|[;&|]\s*)git\s+commit(?:\s|$)", cmd):
        try:
            branch = (
                subprocess.check_output(
                    ["git", "symbolic-ref", "--short", "HEAD"],
                    cwd=cwd,
                    stderr=subprocess.DEVNULL,
                    text=True,
                ).strip()
            )
            if branch == "master":
                print(
                    json.dumps(
                        {
                            "decision": "deny",
                            "reason": "Blocked by Nomad git-hygiene-guard: Direct commits to 'master' are prohibited. Create a feature/*, fix/*, or chore/* branch first.",
                        }
                    )
                )
                return
        except Exception:
            pass

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
