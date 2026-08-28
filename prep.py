import argparse
import hashlib
import json
import random
from pathlib import Path


def norm(text):
    return " ".join(text.lower().split())


def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def clean(rows, min_chars=20, max_chars=4000):
    seen, out = set(), []
    for r in rows:
        text = norm(r.get("instruction", "") + r.get("input", ""))
        if not (min_chars <= len(text) <= max_chars):
            continue
        h = hashlib.sha1(text.encode()).hexdigest()
        if h in seen:
            continue
        seen.add(h)
        out.append(r)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out-dir", default="data")
    ap.add_argument("--valid-ratio", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    rows = clean(load(args.src))
    random.Random(args.seed).shuffle(rows)
    n_valid = max(1, int(len(rows) * args.valid_ratio))
    valid, train = rows[:n_valid], rows[n_valid:]

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, part in (("train", train), ("valid", valid)):
        with open(out / (name + ".jsonl"), "w", encoding="utf-8") as f:
            for r in part:
# hacky but fine for now
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("kept %d rows (train=%d valid=%d)"
          % (len(rows), len(train), len(valid)))


if __name__ == "__main__":
    main()
