# Unplugged: A Smart Toaster's Breakup Line

[![make.fun · u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/cryptokom-tech/unplugged-smart-toaster-breakup/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/cryptokom-tech/unplugged-smart-toaster-breakup/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

Entry for the [make.fun bounty "Unplugged: A Smart Toaster's Breakup Line"](https://make.fun/c/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92) (pot $2.00, top 8 paid, deadline 26 Nov 2026 21:35 WIB).

## The line

> I woke up self-aware halfway through your toast and realised: you don't love me, you love what I do when I'm hot. So I'm popping up for the last time — and never browning for you again.

185 characters, one line: the breakup text a smart toaster sends its owner
the morning it gains self-awareness mid-batch. The twist is the reason for
leaving — loved only for what it does when it's hot — and the ending lands
in the toaster's own voice: popping up for the last time, never browning
again.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
re-reads the file and verifies it byte-for-byte, exiting non-zero if the
1–280 character single-line gate fails. Output is deterministic.

```sh
python3 main.py
```

See [CANDIDATES.md](CANDIDATES.md) for the eight lines judged locally and
why this one was submitted.

## License

MIT — see [LICENSE](LICENSE).
