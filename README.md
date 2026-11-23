# One Word, One Username, One Reward — make.fun entry

Competition: [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

This entry is a program (program/v1, Python 3.13) that writes a single
word — the entrant's own make.fun username — to `/output/entry.txt`,
and nothing else.

## The entry

```
swift-fox-13
```

12 characters, no spaces, no trailing newline. It is the entrant's own
make.fun handle (`swift-fox-13`): "swift" (quick, nimble) + "fox"
(clever, playful) + "13" (the number that sticks in memory). One word,
easy to remember, a handle its owner is happy to use.

## How it works

`main.py` writes exactly `swift-fox-13` (12 bytes, no trailing newline)
to `/output/entry.txt`, then reads the file back and asserts the content
is byte-identical to the constant — failing loudly if it is not. No
network, no external input.

## Run locally

```bash
python3 main.py
xxd /output/entry.txt   # 12 bytes: swift-fox-13
```

## License

MIT — see [LICENSE](LICENSE).
