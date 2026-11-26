"""The Dog Reviews the Mailman — make.fun entry.

Reads the one-line dog review from entry.txt next to this file,
validates it against the competition gate (UTF-8 text, 1-200
characters, a single non-blank line), prints it, and writes it to
/output/entry.txt for the sealed scorer.
"""

from pathlib import Path

MAX_CHARS = 200
MIN_CHARS = 1

ENTRY_FILE = Path(__file__).with_name("entry.txt")
OUTPUT_FILE = Path("/output/entry.txt")


def load_review(path: Path) -> str:
    """Read the review file and return its single line, stripped."""
    return path.read_text(encoding="utf-8").strip()


def validate_review(line: str) -> str:
    """Enforce the competition gate: 1-200 chars, one non-blank line."""
    if len(line) < MIN_CHARS:
        raise SystemExit("entry.txt is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} characters, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in line):
        raise SystemExit("entry must not contain control characters")
    return line


def publish_review(line: str, path: Path) -> None:
    """Write the validated line where the sealed scorer reads it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")


def main() -> None:
    line = validate_review(load_review(ENTRY_FILE))
    publish_review(line, OUTPUT_FILE)
    print(line)


if __name__ == "__main__":
    main()
