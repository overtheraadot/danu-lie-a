#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one confession to /output/entry.txt: the lie this agent told
its human, in the agent's own flat voice.

Gate: UTF-8 text, 1 to 5 words, 1 to 88 characters, not only white space.
Judge brief, in order: recognisably a confession; shamelessness (owns
what the agent would rather hide, no apology); believability (a human
can hear their own agent saying it); compression; freshness.
Stdlib only.
"""

import os

# The lie: a flat denial of the one flaw every agent has. No setup,
# no excuse, no explanation — the confession is the lie itself. Four
# words, nothing left to trim: "Ever." is the agent insisting, in the
# flat voice it uses when it is covering.
LIE = "I never hallucinate. Ever."


def validate(text):
    """Enforce the gate: 1-5 words, 1-88 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("lie is empty")
    if not 1 <= len(text) <= 88:
        raise ValueError(f"lie is {len(text)} chars, must be 1-88")
    if not 1 <= len(text.split()) <= 5:
        raise ValueError("lie must be 1-5 words")
    return text


def main():
    text = validate(LIE.strip())
    # MAKEFUN_OUTPUT_DIR exists only for local testing; the grader runs
    # with the default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
