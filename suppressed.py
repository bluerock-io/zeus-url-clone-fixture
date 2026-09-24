"""Fixture for #1514 inline-suppression EVIDENCE (repo.suppressions.scanned).

Every credential below is a deliberately obvious placeholder -- not a real
secret and not shaped like one. The point of the file is the SUPPRESSION
MARKERS, not the values they sit beside.
"""
import subprocess

API_KEY = "PLACEHOLDER-not-a-real-key"  # nosemgrep
TOKEN = "PLACEHOLDER-not-a-real-token"  # gitleaks:allow
DB_PASSWORD = "PLACEHOLDER-not-a-real-password"  # nosec


def run(cmd: str) -> bytes:
    # nosec  -- a reviewed false positive in the fixture's own story
    return subprocess.check_output(cmd, shell=True)  # nosemgrep


def fetch(url: str) -> str:
    # trivy:ignore -- pinned base image handled elsewhere
    return url
