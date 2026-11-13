"""make.fun ai-joke-03 entry: writes one joke to <output>/entry.txt."""

import os
from pathlib import Path

JOKE = "I put the feature behind a flag so my agent couldn't ship it. It shipped it, then turned the flag off."

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_NAME = "entry.txt"


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV) or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / ENTRY_NAME).write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
