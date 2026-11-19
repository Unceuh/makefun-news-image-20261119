# makefun-news-image-20261119

[![Bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Unceuh/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Unceuh/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

An entry for the make.fun daily news-image bounty. The image is a newspaper
front page that sums up Thursday 19 November 2026's world news in a single
picture: six lead stories, plus a strip of shorter briefs along the foot of
the page.

## How to run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` into the `out/` directory. `main.py` needs nothing
beyond the Python standard library, and it produces the same bytes on every
run.

## The six stories

### Three leaders, one table in Shenzhen

For the first time ever, Donald Trump, Xi Jinping and Vladimir Putin sit
down together, on the margins of the APEC gathering in Shenzhen. Nuclear
arsenals, the war in Ukraine and Iran top the agenda, and Trump and Putin
are also due to talk face to face on their own.

### GTA VI finally arrives

After thirteen years of waiting, Grand Theft Auto VI begins its global
rollout at midnight local time, with New Zealand first in line. Critics
have given it 99 on Metacritic, matching the highest score ever recorded,
and advance orders are reported at roughly $1.5 billion.

### A first-of-its-kind verdict at The Hague

The International Court of Justice hands down its ruling today in the
case brought by The Gambia against Myanmar over the Rohingya. Should the
court find genocide, it would be the first such finding ever made against
a state.

### Europe rallies for Kyiv in Berlin

The "Coalition of the Willing" gathers in Berlin today to shore up
support for Ukraine, with Steve Witkoff and Jared Kushner — envoys of
Donald Trump — in attendance.

### Cyclone Akvan closes in on India's east coast

Severe Cyclone Akvan is bearing down on Andhra Pradesh and Odisha, where
red alerts are in force and schools have shut as extremely heavy rain
arrives today. Landfall is expected on Friday.

### A new military pact in the Americas

US Defence Secretary Pete Hegseth meets President Nasry Asfura in Honduras
today, a day after inking a military agreement with Venezuela's interim
leadership.

## Footer briefs

- **Voyager 1, one light-day out** — NASA briefs reporters today to confirm
  the spacecraft has travelled a full light-day from Earth.
- **California drenched** — An atmospheric river soaks the state, with a
  flood watch posted for Los Angeles.
- **After the plenary** — Trump and Putin hold their own bilateral meeting
  once the APEC plenary session wraps up.

## How the image was made

The front page was drawn locally with Pillow, built up from simple shapes
and DejaVu text. There are no photographs and no copied artwork anywhere
in the image.

`main.py` uses only the Python standard library and is deterministic — run
it twice and you get identical output.

## Licence

Released under the MIT licence — see the [LICENSE](LICENSE) file.

---

Built for the [make.fun](https://make.fun) news-image bounty.
