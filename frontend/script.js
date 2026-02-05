const PROFILE_API = "http://127.0.0.1:8000/profile";
const PROJECTS_API = "http://127.0.0.1:8000/projects";

// -----------------------------
// Load profile content
// -----------------------------
fetch(PROFILE_API)
  .then(res => res.json())
  .then(data => {
    renderSummary(data.professional_profile);
    renderEducation(data.education);
    renderSkills(data.technical_skills);
  })
  .catch(() => {
    document.getElementById("summary").innerText =
      "Failed to load profile.";
  });

// -----------------------------
// Load project pages
// -----------------------------
fetch(PROJECTS_API)
  .then(res => res.json())
  .then(projects => {
    // ✅ enforce visual ordering
    // enforce visual ordering
    const ORDER = ["ssbc", "vreyesam"];

    projects.sort(
    (a, b) => ORDER.indexOf(a.slug) - ORDER.indexOf(b.slug)
    );


    renderProjects(projects);
  })
  .catch(() => {
    document.getElementById("projects").innerText =
      "Failed to load projects.";
  });

// -----------------------------
// Render functions
// -----------------------------
function renderSummary(profile) {
  document.getElementById("summary").innerHTML =
    `<p>${profile.professional_summary}</p>`;
}

function renderEducation(edu) {
  const c = document.getElementById("education");
  c.innerHTML = `
    <div class="card">
      <div class="card-title">${edu.degree}</div>
      <div class="card-sub">
        ${edu.institution} • ${edu.timeline}
      </div>
      <div class="card-desc">${edu.specialization}</div>
    </div>
  `;
}

function renderProjects(projects) {
  const c = document.getElementById("projects");
  c.innerHTML = "";

  projects.forEach(p => {
    const a = document.createElement("a");
    a.href = `project.html?slug=${p.slug}`;
    a.style.textDecoration = "none";
    a.style.color = "inherit";

    const div = document.createElement("div");
    div.className = "card";
    div.innerHTML = `
      <div class="card-title">${p.title}</div>
      <div class="card-sub">${p.subtitle}</div>
      <div class="card-desc">
        Click to view full project details →
      </div>
    `;

    a.appendChild(div);
    c.appendChild(a);
  });
}

function renderSkills(skills) {
  const c = document.getElementById("skills");
  c.innerHTML = "";

  Object.entries(skills).forEach(([key, vals]) => {
    const div = document.createElement("div");
    div.className = "card";
    div.innerHTML = `
      <div class="card-title">${key.replaceAll("_", " ")}</div>
      <div class="card-desc">${vals.join(", ")}</div>
    `;
    c.appendChild(div);
  });
}
