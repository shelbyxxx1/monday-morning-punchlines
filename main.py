import os
from pathlib import Path


JOKE = (
    "I tried to reschedule Monday to Tuesday, but it declined, "
    "counter-proposed 7 a.m., and CC'd my boss on the whole thread."
)


def main() -> None:
    output_directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "entry.txt").write_text(
        JOKE + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
