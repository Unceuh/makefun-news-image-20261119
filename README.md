# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Unceuh/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Unceuh/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A newspaper front page summing up Thursday 19 November 2026's world news in one image: the first Trump–Xi–Putin trilateral summit in Shenzhen, GTA VI's worldwide launch, the ICJ's Myanmar genocide ruling, Ukraine's allies meeting in Berlin, Cyclone Akvan nearing India, and Hegseth's visit to Honduras.

## Running it

Run it with the output folder set: `MAKEFUN_OUTPUT_DIR=out python3 main.py` (create `out` first with `mkdir -p out`).

## What the image shows

A 1024x1024 newspaper front page, "WORLD NEWS", dated Thursday, 19 November 2026. Six numbered stories:

1. THREE LEADERS MEET IN SHENZHEN — Donald Trump, Xi Jinping and Vladimir Putin hold the first trilateral summit at APEC in Shenzhen; nuclear arms, Ukraine and Iran top the agenda.
2. GTA VI LAUNCHES WORLDWIDE — The rollout began at midnight in New Zealand after a 13-year wait; 99 on Metacritic, tying the all-time record, with $1.5bn in preorders.
3. WORLD COURT RULES ON MYANMAR — The ICJ delivers its judgment in The Gambia v. Myanmar over the Rohingya; a genocide finding would be the first ever against a state.
4. ALLIES RALLY FOR UKRAINE IN BERLIN — Europe's "Coalition of the Willing" meets in Berlin, with Trump's envoys Steve Witkoff and Jared Kushner attending.
5. CYCLONE AKVAN NEARS INDIA — The severe storm bears down on Andhra Pradesh and Odisha; red alerts and school closures as extremely heavy rain hits; landfall due Friday.
6. HEGSETH HEADS TO HONDURAS — The US defence chief meets President Nasry Asfura, a day after signing a military pact with Venezuela's interim leaders.

Footer briefs: NASA to confirm Voyager 1 passed one light-day from Earth; atmospheric river soaks California with a flood watch in Los Angeles; Trump and Putin also meet one-on-one after the APEC plenary.

Pillow drew the front page locally from simple shapes and DejaVu text — no photos or copied artwork — and the file ships as `entry.png`.

The entry program uses only the standard library: it copies the `entry.png` next to it into `$MAKEFUN_OUTPUT_DIR/entry.png` (`/output` by default). With no network, both grader runs produce identical bytes.

## Licence

MIT licence — see the LICENSE file.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
