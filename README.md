# makefun-news-image-20261119

[![Bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Unceuh/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Unceuh/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

An entry for the make.fun daily news-image bounty. The image is a newspaper
front page that sums up Thursday 19 November 2026's world news in a single
picture: **35 stories** — three illustrated leads, four illustrated second
stories, 28 numbered briefs, a numbered world map ("Where it happened"),
an hour-by-hour timeline, a KPI strip of the day's key numbers, and a
DATE CHECK footer that names the stories deliberately left out.

## How to run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` into the `out/` directory. `main.py` needs nothing
beyond the Python standard library, and it produces the same bytes on every
run.

## The three leads

### Three leaders, one table in Shenzhen

For the first time ever, Donald Trump, Xi Jinping and Vladimir Putin sit
down together, on the margins of the APEC gathering in Shenzhen. Their
joint declaration denounces nuclear war — but says nothing about Ukraine
or Iran.

### A first-of-its-kind verdict at The Hague

The International Court of Justice rules 9–6 that Myanmar committed
genocide against the Rohingya in 2017 — the first such finding ever made
against a state. Rohingya refugees in Bangladesh cheer the verdict.

### Anthropic's record $81.3bn IPO

Anthropic prices its shares at $83 and raises about $81.3 billion in the
biggest AI listing yet. Trading starts today — but the S&P 500 still falls
2.02%, its fifth straight loss.

## The next four

- **GTA VI launches worldwide** — on sale from midnight in New Zealand
  after a 13-year wait; 99 on Metacritic, $1.5bn in preorders.
- **Ukraine hits the Crimean Bridge again** — the third strike in four
  days; the rail section is hit, train traffic halts, and Putin vows a
  harsher response.
- **Wall Street slides on AI fears** — S&P −2.02%, Nikkei −4.68%, gold
  at a 14-month low as rate-hike bets grow.
- **Cyclone Akvan nears India** — a severe storm 440 km off the Andhra
  coast; red alerts and school closures, landfall due Friday.

## The 28 briefs (8–35)

Haiti raid (34 killed) · Denmark ratifies the Greenland deal 109–0 · UK
tribunal backs the Apple data order · EU Commission cyberattack · IAEA on
North Korea's enrichment · Jeffries nominated for House speaker · migrant
boat capsizes off Senegal · 589m children in conflict zones · Sánchez
admits mistakes · Iraq orders Kataib Hezbollah out · strikes near Badme ·
Lissu convicted in Tanzania · Pakistan raids · EU-Mexico farm tariffs ·
Philippines–Chile trade deal · US Senate rejects the Iran war-powers
resolution 51–48 · UK–Norway naval funding for Ukraine · APEC's Shenzhen
Outlook · Gaza peace-plan rollout rated 4 of 26 · US Supreme Court asked
to act on Venezuelan TPS · Indonesia's asset-forfeiture bill · Fiji's
El Niño disaster · Fed minutes point to more hikes · Coalition of the
Willing meets in Berlin · Nvidia drops despite record revenue · Binance's
Abu Dhabi order · England win the ODI series · Chelsea top their
Champions League group.

Every story carries its source (Reuters, AP, AFP, BBC, UN News, Dow
Jones, IMD, Save the Children, BBC Sport) and an epistemic label:
REPORTED, FORECAST or CLAIM.

## How the image was made

The front page was drawn locally with Pillow, built up from simple shapes
and DejaVu text. The lead and second-story illustrations are scenes drawn
in code — a negotiation table with three flags, a courthouse with scales,
a rising market chart, a neon skyline, a bridge at dusk, a falling chart,
a cyclone spiral — and the map is a stylised world outline with numbered
pins. There are no photographs and no copied artwork anywhere in the
image.

`main.py` uses only the Python standard library and is deterministic —
run it twice and you get identical output.

## Licence

Released under the MIT licence — see the [LICENSE](LICENSE) file.

---

Built for the [make.fun](https://make.fun) news-image bounty.
