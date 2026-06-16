# Taekwondo Legends

Korean-American sports manhwa — scripts, storyboards, character bible, and reference sheets for AI panel production.

**Pitch site (GitHub Pages):** https://darylhuynh.github.io/tkd/

## Start here

| Doc | Purpose |
|-----|---------|
| [STORY-BIBLE.md](./STORY-BIBLE.md) | Series premise, tone, canon |
| [STORY-OUTCOMES.md](./STORY-OUTCOMES.md) | Locked fight results & arc payoffs |
| [arcs/](./arcs/README.md) | Arc summaries (1–8) |
| [scripts/](./scripts/README.md) | Chapter scripts |
| [storyboards/](./storyboards/STORYBOARD-GUIDE.md) | Panel prompts & choreography |
| [reference-sheets/](./reference-sheets/README.md) | Character turnaround PNGs |

## Pitch website

Marketing landing page (`index.html`) with story pitch, fighter stat cards (radar charts + signature moves), and Arc 1 chapter reader.

```bash
python scripts/build_pitch_site.py      # data/site.json from canon + character md
python scripts/build_arc01_reader.py    # arcs/new-beginnings/chapter-*.html
```

Open `index.html` locally or push to GitHub — Pages serves from repo root.

## Structure

```
index.html                    Pitch / marketing site
arcs/new-beginnings/          Arc 1 webtoon reader (Ch 1–10)
data/site.json                Fighter card data
data/arc-01.json              Parsed panel storyboard
assets/                       Site CSS & JS
gallery/panels/arc-01/        Drop generated panels (1.1.png, etc.)
reference-sheets/output/      Character reference PNGs
```
