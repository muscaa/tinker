import os

ID = "tinker"
NAME = "Tinker"
AUTHOR_ID = "muscaa"
AUTHOR_NAME = "musca"
VERSION = os.environ.get("GITHUB_REF_NAME", "v0.0.1-SNAPSHOT").removeprefix("v")
DESCRIPTION = "A CLI app that generates projects from templates."
