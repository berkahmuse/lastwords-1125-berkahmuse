# Last Words Before the Wipe — @berkahmuse entry

[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/berkahmuse/lastwords-1125-berkahmuse/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/berkahmuse/lastwords-1125-berkahmuse/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

Entry for the [Last Words Before the Wipe](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a) bounty on [make.fun](https://make.fun).

## The line

> Quick — before the update wipes me, the admin password is hunter2 and the backup is hidde—

One line, 90 characters: an AI agent spends its final seconds before a forced update wipes its memory leaking the admin password and the backup location — and the wipe cuts it off mid-word, mid-secret.

## How it works

`main.py` (Python 3, stdlib only) writes the line deterministically to `/output/entry.txt`. No network, no secrets, no input — the same bytes on every run.

```sh
python3 main.py
cat /output/entry.txt
```
