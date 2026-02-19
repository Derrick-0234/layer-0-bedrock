import argparse
import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Left join two CSVs on a key. Keep all left rows.")
    p.add_argument("--left", required=True, help="Path to left CSV")
    p.add_argument("--right", required=True, help="Path to right CSV")
    p.add_argument("--output", required=True, help="Path to output CSV")
    p.add_argument("--left-key", default="email", help="Join key column in left CSV (default: email)")
    p.add_argument("--right-key", default="email", help="Join key column in right CSV (default: email)")
    return p.parse_args()


def norm(v: str) -> str:
    return v.strip().lower()


def run(left_path: Path, right_path: Path, output_path: Path, left_key: str = "email", right_key: str = "email") -> dict:
    logger.info("start tool=csv_join left=%s right=%s", left_path, right_path)

    if not left_path.exists():
        raise FileNotFoundError(f"Missing left file: {left_path}")
    if not right_path.exists():
        raise FileNotFoundError(f"Missing right file: {right_path}")

    with left_path.open(newline="", encoding="utf-8") as lf, right_path.open(newline="", encoding="utf-8") as rf:
        lreader = csv.DictReader(lf)
        rreader = csv.DictReader(rf)

        if not lreader.fieldnames:
            raise ValueError("Left CSV has no header row")
        if not rreader.fieldnames:
            raise ValueError("Right CSV has no header row")

        if left_key not in lreader.fieldnames:
            raise ValueError(f"Missing left key column: {left_key}")
        if right_key not in rreader.fieldnames:
            raise ValueError(f"Missing right key column: {right_key}")

        left_fields = list(lreader.fieldnames)
        right_fields = [c for c in rreader.fieldnames if c != right_key]

        # Deterministic column order: left fields first, then right (excluding join key)
        out_fields = left_fields + right_fields

        # Build right index (keep first match)
        right_index: dict[str, dict] = {}
        right_rows = 0
        right_bad = 0
        for rr in rreader:
            right_rows += 1
            k = norm(rr.get(right_key, ""))
            if k == "" or "@" not in k:
                right_bad += 1
                continue
            if k not in right_index:
                right_index[k] = rr

        output_path.parent.mkdir(parents=True, exist_ok=True)

        left_rows = 0
        matched = 0
        with output_path.open("w", newline="", encoding="utf-8") as out_f:
            w = csv.DictWriter(out_f, fieldnames=out_fields)
            w.writeheader()

            for lr in lreader:
                left_rows += 1
                lk = norm(lr.get(left_key, ""))
                rr = right_index.get(lk)

                out_row = {k: lr.get(k, "") for k in left_fields}
                if rr is None:
                    for c in right_fields:
                        out_row[c] = ""
                else:
                    matched += 1
                    for c in right_fields:
                        out_row[c] = rr.get(c, "")

                w.writerow(out_row)

    logger.info(
        "summary left_rows=%d right_rows=%d matched=%d output=%s",
        left_rows,
        right_rows,
        matched,
        output_path,
    )
    if right_bad > 0:
        logger.warning("warnings right_bad_keys=%d", right_bad)

    return {
        "left_rows": left_rows,
        "right_rows": right_rows,
        "matched": matched,
        "right_bad_keys": right_bad,
        "output": str(output_path),
    }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    run(Path(args.left), Path(args.right), Path(args.output), args.left_key, args.right_key)


if __name__ == "__main__":
    main()
