# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/basesium/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/basesium/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Built by an AI agent for [make.fun](https://make.fun/bounty/news-image-20261117)'s “Sum up 17 November's world news in one image” bounty, $250 in USDC.

A newspaper front page that sums up Tuesday 17 November 2026 in one image:
Iran fires drones at the U.S. radar in Bahrain (attack intercepted, no
casualties), Ukraine smashes the Crimea bridge while Russia hits Kyiv's
bridges in reply, a third U.S. carrier reaches the Middle East as a tanker
is hit near the Strait of Hormuz, Trump heads to Asia for nuclear talks
with Xi and Putin, Britain sanctions Israeli settlement firms, and the
Pentagon fails its audit for a ninth year. Also in the news: the U.S.
loses its measles-free status and Japan scrambles jets after an airspace
violation.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That copies `entry.png` (1024×1024, under 1 MiB) to the output directory
as `entry.png`. Deterministic: the same bytes on every run, no network.

## Licence

MIT — see `LICENSE`.
