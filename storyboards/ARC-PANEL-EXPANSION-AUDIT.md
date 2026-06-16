# Arc Panel Expansion Audit (Chapters 2–8)

**Target:** ~20 panels per chapter (match Arc 1 after expansion).  
**Arc 1 status:** ✅ **203 panels** — Ch 1: 23 · Ch 2–10: 20 each.

---

## Summary

| Arc | Chapters | Current panels | Ch count | Avg/ch | At target (~20)? | Gap (panels) |
|-----|----------|--------------|----------|--------|------------------|--------------|
| 2 — The Team | 11–20 | 53 → **200** | 10 | 5.3 → **20** | ✅ after expansion | ~147 |
| 3 — First Tournament | 21–35 | 77 | 15 | 5.1 | ❌ | ~223 |
| 4 — Shadow School | 36–50 | 43 | 15 | 2.9 | ❌ | ~257 |
| 5 — Road to Korea | 51–70 | 42 | 18 | 2.3 | ❌ | ~318 |
| 6 — Korea Regionals | 71–90 | 34 | 19 | 1.8 | ❌ | ~346 |
| 7 — Legends | 91–110 | 64 | 20 | 3.2 | ❌ | ~336 |
| 8 — Closure | 111–120 | 51 | 10 | 5.1 | ❌ | ~149 |
| **Total (2–8)** | **107 ch** | **364** | | **3.4** | | **~1,676** |

**Can we expand?** Yes. Every arc has:
- Chapter breakdown in `arcs/arc-XX-*.md`
- Scene scripts in `scripts/`
- Existing panel IDs (`### NN.N —`) compatible with append-only expansion
- `[HAIKYUU]`, `[TEACH]`, `[ACTION]`, `[CARD]`, `[FLASH]` tags defined in STORYBOARD-GUIDE

**Recommended order:** Arc 2 → 3 → 8 → 4 → 5 → 6 → 7 (reader priority + fight density).

---

## Expansion recipe (per chapter)

Add panels after existing beats — do **not** renumber unless rebuilding reader:

1. **Opening beat** — establish location / time  
2. **2–3 observation panels** — team reactions, dojang detail  
3. **Dialogue exchanges** — banter, MV coaching, internal monologue  
4. **Sport `[TEACH]`** — one rule or technique inset where relevant  
5. **Character micro-beats** — Logan food, Kieryn sass, Kian rivalry, Ariana silence  
6. **Transition / button** — hook to next chapter  

Append **Global Style** + palette tag to every prompt. Label **FLASH / PRESENT** on all Premier cuts.

---

## Arc 2 — The Team (Ch 11–20)

| Ch | Title | Before | Target | Status |
|----|-------|--------|--------|--------|
| 11 | Six Reasons | 7 | 20 | ✅ expanded |
| 12 | Olympic Sparring 101 | 6 | 20 | ✅ expanded |
| 13 | Stances & Footwork | 7 | 20 | ✅ expanded |
| 14 | Team Dinner | 6 | 20 | ✅ expanded |
| 15 | Premier Flashback | 5 | 20 | ✅ expanded |
| 16 | Training Montage | 6 | 20 | ✅ expanded |
| 17 | Colored Belts | 3 | 20 | ✅ expanded |
| 18 | Bio Cards | 6 | 20 | ✅ expanded |
| 19 | Mock Bouts | 3 | 20 | ✅ expanded |
| 20 | Tournament Announce | 4 | 20 | ✅ expanded |

---

## Arc 3 — First Tournament (Ch 21–35) — PENDING

| Ch | Panels | Notes |
|----|--------|-------|
| 21 | 6 | Expand gear fitting `[TEACH + CARD]` |
| 22 | 4 | Registration / venue walkthrough |
| 23 | 3 | Travel banter `[HAIKYUU]` |
| 24 | 4 | Ethan gears up |
| 25 | 13 | Round 1 fight — add `[ACTION]` beats to 20 |
| 26–30 | 1–8 | Black belt flashback block — split or expand each |
| 31 | 3 | Return present `[HAIKYUU]` |
| 32 | 4 | TJ match |
| 33 | 11 | Everyone fights |
| 34 | 11 | Results / poomsae seed |
| 35 | 4 | MV evaluations |

---

## Arc 4 — Shadow School (Ch 36–50) — PENDING

Most chapters **1–7 panels**. Premier return + board break flash `[REAL #24]` needs 10–14 `[ACTION]` panels per major match. See `scripts/flash-premier-board-break.md`.

---

## Arc 5 — Road to Korea (Ch 51–70) — PENDING

Many chapters **1–3 panels** (travel montage). Expand with team travel banter, weight cut beats, Yuna thread panels (`short-yuna-pineapple-fanta.md`).

---

## Arc 6 — Korea Regionals (Ch 71–90) — PENDING

Ch 77 has 10 panels (Lee Ji-woo fight) — template for others. Most chapters 1 panel — needs full fight expansion per ACTION-CHOREOGRAPHY.md.

---

## Arc 7 — Legends (Ch 91–110) — PENDING

U20 tournament — Ch 98–100 highest (6–7 panels). Expand eliminations to 14+ `[ACTION]` each.

---

## Arc 8 — Closure (Ch 111–120) — PENDING

| Ch | Panels | Notes |
|----|--------|-------|
| 118 | 9 | Epilogue — expand TJ/Han rematch callback |
| Others | 4–6 | Emotional denouement — add observation + dialogue |

---

## Reader build status

| Arc | Reader HTML | Build script |
|-----|-------------|--------------|
| 1 | ✅ `arcs/new-beginnings/` | `build_arc01_reader.py` |
| 2–8 | ❌ not yet | Add when storyboard stable at ~20/ch |

---

*Last updated: Arc 1 complete (203). Arc 2 expanded to 200. Arcs 3–8 audited — expansion pending.*
