"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line for a bug fix that made
everything worse, to the output path the harness expects
(/output/entry.txt by default, overridable via OUTPUT_PATH).
Python standard library only; fully deterministic.
"""

import os

# The entry: one commit subject line, 50 characters.
# The fix for "users can't log out" was so thorough that
# it removed the ability to log in at all -- the repair
# broke strictly more than the bug it mended.
LINE = "fix: users couldn't log out; now nobody can log in"

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
