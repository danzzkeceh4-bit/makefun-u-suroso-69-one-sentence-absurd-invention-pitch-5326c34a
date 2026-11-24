# One-Sentence Absurd Invention Pitch — The Apologizer

[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/danzzkeceh4-bit/makefun-u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/danzzkeceh4-bit/makefun-u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

Entry for the [make.fun bounty](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
"One-Sentence Absurd Invention Pitch": a single sentence pitching a ridiculous
invention that fixes a tiny everyday annoyance.

## The pitch (204 characters, one sentence)

> The Apologizer: a self-blaming alarm clock that says sorry, brews your coffee, and takes the guilt for Monday, so you can snooze in peace while it files a formal complaint against mornings on your behalf.

The annoyance: waking up on Monday mornings, and the guilt that comes with
hitting snooze. The invention: an alarm clock that blames itself instead of
you — it apologises, brews your coffee, absorbs the Monday guilt, and even
files a formal complaint against mornings on your behalf, so you can snooze
in peace.

## How it works

`main.py` (Python 3.13) writes the exact pitch above — 204 characters, no
trailing newline — to `/output/entry.txt`, then reads it back and asserts the
contents match exactly. No network, no external input.

## Run

```bash
python3 main.py
```

The program writes `/output/entry.txt` (the `/output` directory must exist)
and prints the character count on success.
