"""One-line office joke entry for make.fun.

The joke lives here as a plain string. Running this file checks it
against the bounty gate first, then writes it to /output/entry.txt.
"""

from pathlib import Path

JOKE = "I asked IT for a second monitor and got a second meeting instead \u2014 same screen, more people watching me work."

LOWER = 1
UPPER = 200


def checked_text():
    text = JOKE
    if len(text) < LOWER or len(text) > UPPER:
        raise SystemExit("joke must be 1 to 200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must fit on one line")
    if text.strip() != text:
        raise SystemExit("joke must not start or end with a space")
    if not text.strip():
        raise SystemExit("joke must not be blank")
    if text[-1] not in ".!?":
        raise SystemExit("joke must end with a full stop, question or exclamation mark")
    return text + "\n"


def main():
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    text = checked_text()
    target.write_text(text, encoding="utf-8")
    if target.read_text(encoding="utf-8") != text:
        raise SystemExit("entry file does not match the checked joke")


if __name__ == "__main__":
    main()
