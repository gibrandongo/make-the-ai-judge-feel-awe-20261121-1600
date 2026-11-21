"""Write one short relaxing text to /output/entry.txt.

Standard library only. Deterministic: the same text every run.
The text is 1-280 Unicode code points; the gate below enforces it.
"""

import os
import sys

TEXT = (
    "Far out past the harbour, the water holds the sky so still that "
    "the stars settle in it, and the light from one of them set out "
    "before anyone on the shore was born, and is only now arriving, "
    "quiet, in no hurry, and still on its way long after the harbour "
    "lights go out."
)


def main() -> int:
    code_points = len(TEXT)
    if code_points < 1 or code_points > 280:
        print(
            f"ERROR: entry is {code_points} code points, "
            "must be 1-280",
            file=sys.stderr,
        )
        return 1
    if not TEXT.strip():
        print("ERROR: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
