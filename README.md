# Monday Morning Punchlines

[![Monday Morning Punchlines bounty](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Entry rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/shelbyxxx1/monday-morning-punchlines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard)
[![Entry reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/shelbyxxx1/monday-morning-punchlines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

A make.fun CLASSIC entry that writes one Monday-morning joke using only the Python
standard library. No dependencies, network access, or secrets are needed.

## Run

```sh
python3 main.py
```

The program writes the joke as UTF-8 plus one trailing newline to
`/output/entry.txt`, or `$MAKEFUN_OUTPUT_DIR/entry.txt` when `MAKEFUN_OUTPUT_DIR` is
set to a non-empty value. An unset or empty value uses `/output`. Missing parent
directories are created, and the output directory itself is never removed or
replaced.

## The joke

> I tried to reschedule Monday to Tuesday, but it declined, counter-proposed 7 a.m., and CC'd my boss on the whole thread.
