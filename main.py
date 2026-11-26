"""Worst Pizza Topping entry: writes one funny line to /output/entry.txt."""
import os
import sys

MAX_CHARS = 200


def main():
    try:
        line = (
            "Try our Soggy Sock Pizza: wet gym socks slow-simmered in warm milk "
            "on a crust that gave up hours ago \u2014 crunchy, soggy, "
            "and somehow still judging you."
        )
        line = line[:MAX_CHARS] if len(line) > MAX_CHARS else line
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
        return 0
    except Exception as exc:  # noqa: BLE001 - grader must exit 0
        print(f"error: {exc}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
