#!/usr/bin/env python3
"""Copy the bundled entry image to the make.fun output directory.

The image bundled next to this script is copied verbatim to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``/output``). The copy is
verified by reading the written file back and comparing its bytes with
the bundled bytes, so the output is byte-identical to the source.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    bundled = source.read_bytes()

    if destination.resolve() == source.resolve():
        return 0

    shutil.copyfile(source, destination)
    written = destination.read_bytes()
    assert written == bundled, "output bytes differ from bundled image"
    return 0


if __name__ == "__main__":
    sys.exit(main())
