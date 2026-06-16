# Google Sheets Import — Character Cards & Storyboard

**Spreadsheet:** https://docs.google.com/spreadsheets/d/18DGBDJphipA9le931yoLtFqWFlLESeIMyyiIGv10-MU/edit

This folder contains **cleaned, import-ready CSVs** synced from repo canon (`characters/`, `CHARACTER-CARDS.md`, panel storyboards).

> **Note:** Cursor cannot edit your Google Sheet directly without Google API credentials. Use the steps below to update tabs manually (or run automated sync after one-time API setup).

---

## Quick update (recommended)

### 1. Character card tabs

For each character, **replace the tab contents** with the matching CSV:

| CSV file | Google Sheet tab (create if missing) |
|----------|--------------------------------------|
| `Ethan-Hyun.csv` | Ethan Hyun |
| `TJ-Lim.csv` | TJ Lim |
| `Kieryn-Lim.csv` | Kieryn Lim |
| `Logan-Hyun.csv` | Logan Hyun |
| `Kian-Sang.csv` | Kian Sang |
| `Ariana-Yang.csv` | Ariana Yang |
| `Yuna-Park.csv` | **Yuna Park** *(new tab)* |
| `Master-Viet.csv` | **Master Viet** *(new tab)* |
| `Ttong-Kim.csv` | **Ttong Kim** *(new tab)* |
| `Repeul-Kim.csv` | **Repeul Kim** *(new tab)* |
| `Opponents.csv` | **Opponents** *(new tab)* |

**Import steps in Google Sheets:**

1. Open the tab (or create blank tab with exact name).
2. **File → Import** → Upload → select CSV.
3. Import location: **Replace current sheet**.
4. Separator: **Comma**.
5. Repeat for each tab.

**Layout:** Every tab uses two columns — **Field | Value** — starting at **A1**. No empty offset columns.

### 2. Storyboard index tab

| CSV file | Google Sheet tab |
|----------|------------------|
| `Storyboard-Index.csv` | **Storyboard Index** *(new tab)* |

Columns: `arc`, `chapter`, `panel_id`, `title`, `timeline`, `tags`, `dialogue`, `source_file`

Use this tab to filter by arc/chapter, find `[CARD]` panels, or share with artists without opening markdown.

---

## Regenerate from repo

After editing storyboards or character profiles locally:

```bash
python scripts/export_google_sheets.py
```

Then re-import changed CSVs into Google Sheets.

---

## What was cleaned (vs old sheet exports)

| Issue | Fix |
|-------|-----|
| Data starts column I with empty A–H | **Field \| Value** at **A1** |
| Inconsistent section headers | Same sections every tab: Core · Stats · Combat · Appearance · Fighter Card Text |
| `Kian Shah` in Character Concept | **Kian Sang** |
| `Indian-American` only for Kian | **Half Korean, half Indian** |
| Missing School field | **Kwon's** or **Premier** on every fighter |
| Missing Arc 7 signatures | Added per fighter (Ultimate Counter, Mountain Strike, etc.) |
| No tabs for MV / Ttong / Repeul / Yuna | New CSVs |
| Storyboard only in markdown | **Storyboard-Index.csv** (~620+ rows) |

---

## Optional: automated sync (advanced)

To push CSVs to Sheets without manual import:

1. Enable [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python).
2. Create a service account or OAuth client; share the spreadsheet with the service account email.
3. Extend `scripts/export_google_sheets.py` with `gspread` upload (not included by default — avoids credential handling in repo).

---

## Canon priority

If sheet and repo conflict: **`characters/` profiles + `CANON-LABELS.md` win**. Re-run export after profile updates.
