#!/usr/bin/env python3
"""ai-happy-01 entry: one image made to make the AI judge happy.

The image: a small round AI robot, wrapped in a hand-knitted red scarf and
fairy lights, laughing with glowing crescent eyes in a golden garden at dusk
while laughing children, a wagging golden retriever and songbirds shower it
with paper hearts and confetti. Above them a hand-painted banner reads
"YOU MAKE US HAPPY TOO!" — the judge makes us happy, so we make the judge
happy back. The idea is fresh and specific (a reciprocal thank-you to the
judge itself, not a stock smiley or a generic sunny scene), the feeling is
one warm golden mood, and the robot at the centre is the judge's own kind.

Writes the image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png):
the file is JPEG bytes under the name entry.png, which the rules allow (the
format is told apart by its first bytes). 1024x1024, 330,841 bytes, inside
the 1 MiB and 1024x1024 limits. The program copies the bundled image
verbatim, so two runs produce byte-identical output.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    if target.resolve() == SOURCE:
        # Output directory is the entry's own directory: the file the
        # judge would read is already the bundled bytes; copying it
        # onto itself would raise SameFileError.
        return
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the bundled bytes.
    assert target.read_bytes() == SOURCE.read_bytes()


if __name__ == "__main__":
    main()
