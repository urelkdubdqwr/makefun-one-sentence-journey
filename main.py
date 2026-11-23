"""Write the make.fun one-sentence journey entry to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default: /output), creates it if needed, and writes
the required UTF-8 entry text followed by a single trailing newline.
"""

import os

ENTRY_TEXT = (
    "Every winter for thirty years my father skied the pass to bring the post "
    "to the last village before the road, and the spring he retired the whole "
    "village skied out to meet him halfway up, carrying nothing, which was the "
    "first post anyone had ever carried to him."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
