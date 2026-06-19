const FACTION_LABELS = {
  all: "All Fighters",
  kwons: "Kwon's Team",
  coach: "Coach",
  ally: "Allies",
  prime: "Prime",
  rival: "Rivals",
};

const HIDDEN_FACTIONS = new Set(["rival"]);

const GRADE_VALUES = {
  "A+": 97, A: 92, "A-": 87,
  "B+": 82, B: 77, "B-": 72,
  "C+": 67, C: 62, "C-": 57,
  "D+": 52, D: 47, "D-": 42,
  F: 30,
};

const RADAR_AXES = ["Attack", "Defense", "Technique", "Mobility", "Physical"];

let siteData = null;
let activeFilter = "all";

async function loadSiteData() {
  const res = await fetch("data/site.json?v=7");
  if (!res.ok) throw new Error("Failed to load site data");
  siteData = await res.json();
}

function el(tag, attrs = {}, children = []) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "className") node.className = v;
    else if (k === "text") node.textContent = v;
    else if (k === "html") node.innerHTML = v;
    else if (k.startsWith("on")) node.addEventListener(k.slice(2).toLowerCase(), v);
    else node.setAttribute(k, v);
  }
  for (const child of children.flat().filter(Boolean)) {
    node.append(child instanceof Node ? child : document.createTextNode(child));
  }
  return node;
}

function initials(name) {
  return name.split(/\s+/).map((w) => w[0]).join("").slice(0, 2).toUpperCase();
}

function gradeValue(grade) {
  return GRADE_VALUES[grade] ?? 60;
}

function buildRadarSvg(stats, size = 120, cssClass = "radar-chart") {
  if (!stats || !RADAR_AXES.some((a) => stats[a])) return null;

  const cx = size / 2;
  const cy = size / 2;
  const maxR = size * 0.36;
  const levels = [0.25, 0.5, 0.75, 1];

  const gridRings = levels.map((lv) => {
    const r = maxR * lv;
    return `<circle cx="${cx}" cy="${cy}" r="${r}" class="radar-ring"/>`;
  }).join("");

  const axes = RADAR_AXES.map((_, i) => {
    const angle = (Math.PI * 2 * i) / RADAR_AXES.length - Math.PI / 2;
    const x = cx + Math.cos(angle) * maxR;
    const y = cy + Math.sin(angle) * maxR;
    return `<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" class="radar-axis"/>`;
  }).join("");

  const points = RADAR_AXES.map((axis, i) => {
    const val = gradeValue(stats[axis] || "C");
    const ratio = val / 100;
    const angle = (Math.PI * 2 * i) / RADAR_AXES.length - Math.PI / 2;
    const x = cx + Math.cos(angle) * maxR * ratio;
    const y = cy + Math.sin(angle) * maxR * ratio;
    return `${x},${y}`;
  }).join(" ");

  const labels = RADAR_AXES.map((axis, i) => {
    const angle = (Math.PI * 2 * i) / RADAR_AXES.length - Math.PI / 2;
    const x = cx + Math.cos(angle) * (maxR + 14);
    const y = cy + Math.sin(angle) * (maxR + 14);
    const anchor = Math.abs(Math.cos(angle)) < 0.2 ? "middle" : Math.cos(angle) > 0 ? "start" : "end";
    const short = axis.slice(0, 3).toUpperCase();
    return `<text x="${x}" y="${y + 3}" text-anchor="${anchor}" class="radar-label">${short}</text>`;
  }).join("");

  // Labels sit outside the chart radius; pad viewBox so they aren't clipped.
  const labelPad = 20;
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute(
    "viewBox",
    `${-labelPad} ${-labelPad} ${size + labelPad * 2} ${size + labelPad * 2}`
  );
  svg.setAttribute("class", cssClass);
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", "Combat stat radar chart");
  svg.innerHTML = `${gridRings}${axes}<polygon points="${points}" class="radar-fill"/><polygon points="${points}" class="radar-stroke"/>${labels}`;
  return svg;
}

function skillList(skills, compact = false) {
  if (!skills?.length) return null;
  return el("ul", { className: compact ? "skill-list skill-list--compact" : "skill-list" },
    skills.map((s) => {
      const unlockClass = s.unlock === "arc7" ? "skill-unlock" : s.unlock === "arc5" ? "skill-arc5" : "";
      const badge = s.unlock === "arc7" ? "U20" : s.unlock === "arc5" ? "Arc 5" : "";
      return el("li", { className: unlockClass }, [
        el("span", { className: "skill-name", text: s.name }),
        badge ? el("span", { className: "skill-badge", text: badge }) : null,
      ]);
    })
  );
}

function renderHero() {
  document.getElementById("hero-logline").textContent = siteData.logline;
  const tagsEl = document.getElementById("hero-tags");
  tagsEl.replaceChildren(...siteData.genre.map((g) => el("span", { className: "tag", text: g })));
  document.getElementById("story-premise-1").textContent = siteData.story_premise;
  document.getElementById("story-premise-2").textContent = siteData.story_premise_2 || "";
}

function renderArcs() {
  const track = document.getElementById("arc-track");
  track.replaceChildren(
    ...siteData.arcs.map((arc) => {
      const inner = [
        el("div", { className: "arc-num", text: String(arc.num).padStart(2, "0") }),
        el("h3", { text: arc.title }),
        el("div", { className: "arc-chapters", text: `Ch. ${arc.chapters}` }),
        el("p", { text: arc.tagline }),
      ];
      if (arc.available && arc.href) {
        return el("a", { className: "arc-card arc-card--live", href: arc.href }, inner);
      }
      return el("article", { className: "arc-card" }, inner);
    })
  );
}

function renderFilters() {
  const visible = siteData.characters.filter((c) => !HIDDEN_FACTIONS.has(c.faction));
  const factions = ["all", ...new Set(visible.map((c) => c.faction))];
  const container = document.getElementById("roster-filters");
  container.replaceChildren(
    ...factions.map((f) =>
      el("button", {
        className: `filter-btn${f === activeFilter ? " active" : ""}`,
        type: "button",
        role: "tab",
        "aria-selected": f === activeFilter ? "true" : "false",
        text: FACTION_LABELS[f] || f,
        onClick: () => { activeFilter = f; renderFilters(); renderCards(); },
      })
    )
  );
}

function statChip(label, value) {
  if (!value) return null;
  return el("div", { className: "stat-chip" }, [
    el("span", { className: "stat-chip-label", text: label }),
    el("span", { className: "stat-chip-value", text: String(value) }),
  ]);
}

function renderCards() {
  const grid = document.getElementById("card-grid");
  const chars = siteData.characters.filter(
    (c) => !HIDDEN_FACTIONS.has(c.faction) && (activeFilter === "all" || c.faction === activeFilter)
  );

  grid.replaceChildren(
    ...chars.map((char) => {
      const portrait = char.portrait
        ? el("img", { src: char.portrait, alt: char.canon_name, loading: "lazy" })
        : el("span", { className: "portrait-fallback", text: initials(char.canon_name) });

      const radar = buildRadarSvg(char.stats, 100, "radar-chart radar-chart--card");

      return el("article", {
        className: "fighter-card",
        "data-faction": char.faction,
        tabindex: "0",
        onClick: () => openFighterModal(char),
        onKeydown: (e) => {
          if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openFighterModal(char); }
        },
      }, [
        el("div", { className: "fighter-card-bar" }),
        el("div", { className: "fighter-card-photo" }, [portrait]),
        el("div", { className: "fighter-card-body" }, [
          el("h3", { text: char.display_name || char.canon_name }),
          char.also_known_as && char.also_known_as !== char.display_name
            ? el("p", { className: "fighter-aka", text: char.also_known_as })
            : null,
          el("p", { className: "fighter-role", text: char.role }),
          el("div", { className: "fighter-card-stats-row" }, [
            statChip("Age", char.age),
            statChip("Ht", char.height),
            statChip("Wt", char.weight),
            statChip("Div", char.division),
            statChip("Dan", char.belt),
            statChip("Hair", char.hair_color),
            statChip("Style", char.hair_style),
          ].filter(Boolean)),
          el("div", { className: "fighter-card-mid" }, [
            radar ? el("div", { className: "fighter-radar-wrap" }, [radar]) : null,
            skillList(char.skills, true),
          ]),
        ]),
      ]);
    })
  );
}

function openFighterModal(char) {
  const modal = document.getElementById("fighter-modal");
  const body = document.getElementById("fighter-modal-body");

  const portrait = char.portrait
    ? el("img", { src: char.portrait, alt: char.canon_name })
    : el("div", { className: "portrait-fallback portrait-fallback--lg", text: initials(char.canon_name) });

  const radar = buildRadarSvg(char.stats, 180, "radar-chart radar-chart--modal");

  const gradeRows = char.stats && Object.keys(char.stats).length
    ? el("div", { className: "modal-grades" }, [
        el("h4", { text: "Main Stats" }),
        ...Object.entries(char.stats).map(([name, grade]) =>
          el("div", { className: "grade-row" }, [
            el("span", { text: name }),
            el("span", { text: grade }),
          ])
        ),
      ])
    : null;

  const viewGallery = char.views?.length > 1
    ? el("div", { className: "modal-views" }, [
        el("h4", { text: "Reference Views" }),
        el("div", { className: "modal-view-grid" },
          char.views.map((item, i) =>
            el("button", {
              className: `modal-view-thumb${item.src === char.portrait ? " active" : ""}`,
              type: "button",
              title: item.label,
              onClick: (e) => {
                const main = body.querySelector(".modal-portrait img");
                if (main) main.src = item.src;
                body.querySelectorAll(".modal-view-thumb").forEach((t) => t.classList.remove("active"));
                e.currentTarget.classList.add("active");
              },
            }, [el("img", { src: item.src, alt: item.label })])
          )
        ),
      ])
    : null;

  body.replaceChildren(
    el("div", { className: "modal-header" }, [
      el("div", { className: "modal-portrait modal-portrait--trim" }, [portrait]),
      el("div", { className: "modal-title" }, [
        el("h2", { text: char.display_name || char.canon_name }),
        char.also_known_as && char.also_known_as !== char.display_name
          ? el("p", { className: "aka", text: char.also_known_as })
          : null,
        el("p", { className: "role", text: char.role }),
        char.school ? el("p", { className: "school", text: char.school }) : null,
      ].filter(Boolean)),
    ]),
    viewGallery,
    el("div", { className: "modal-stat-grid" }, [
      statChip("Age", char.age),
      statChip("Height", char.height),
      statChip("Weight", char.weight),
      statChip("Division", char.division),
      statChip("Dan / Rank", char.belt),
      statChip("Hair color", char.hair_color),
      statChip("Hair style", char.hair_style),
    ].filter(Boolean)),
    el("div", { className: "modal-mid" }, [
      radar ? el("div", { className: "fighter-radar-wrap fighter-radar-wrap--modal" }, [radar]) : null,
      el("div", { className: "modal-skills" }, [
        el("h4", { text: "Signature Moves" }),
        skillList(char.skills) || el("p", { className: "muted", text: "—" }),
      ]),
      gradeRows,
    ].filter(Boolean)),
  );

  modal.showModal();
}

function setupNav() {
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  toggle.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  links.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => links.classList.remove("open"));
  });
}

function setupModals() {
  document.querySelector(".fighter-modal-close").addEventListener("click", () => {
    document.getElementById("fighter-modal").close();
  });
}

async function init() {
  try {
    await loadSiteData();
    renderHero();
    renderArcs();
    renderFilters();
    renderCards();
    setupNav();
    setupModals();
  } catch (err) {
    console.error(err);
    document.getElementById("hero-logline").textContent =
      "Could not load site data. Run: python scripts/build_pitch_site.py";
  }
}

init();
