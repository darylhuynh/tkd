#!/usr/bin/env python3
"""Build Arc 1 reader — delegates to build_arc_reader.py."""

import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    script = Path(__file__).resolve().parent / "build_arc_reader.py"
    sys.exit(subprocess.call([sys.executable, str(script), "1"]))
