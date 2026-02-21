const PROFILE_API = "https://me-api-playground-1-xmn8.onrender.com/profile";
const PROJECTS_API = "https://me-api-playground-1-xmn8.onrender.com/projects";


// Local backend
//const PROFILE_API = "http://127.0.0.1:8000/profile";
//const PROJECTS_API = "http://127.0.0.1:8000/projects";

// -----------------------------
// Load profile content
// -----------------------------
fetch(PROFILE_API)
  .then(res => {
    if (!res.ok) throw new Error("Profile API error");
    return res.json();
  })
  .then(data => {
    renderSummary(data.about);
    renderEducation(data.education);
    renderSkills(data.technical_skills);
  })
  .catch(err => {
    console.error(err);
    document.getElementById("summary").innerText = "Failed to load profile.";
  });

// -----------------------------
// Load projects
// -----------------------------
fetch(PROJECTS_API)
  .then(res => res.json())
  .then(projects => {
    // hennge-transfer first, then research projects
    const ORDER = ["hennge-transfer", "ssbc", "vreyesam"];
    projects.sort(
      (a, b) => ORDER.indexOf(a.slug) - ORDER.indexOf(b.slug)
    );
    renderProjects(projects);
  });

// -----------------------------
// Render functions
// -----------------------------
function renderSummary(text) {
  document.getElementById("summary").innerHTML = `<p>${text}</p>`;
}

function renderEducation(edu) {
  document.getElementById("education").innerHTML = `
    <div class="card">
      <div class="card-title">${edu.degree}</div>
      <div class="card-sub">${edu.institution} • ${edu.timeline}</div>
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
      <div class="card-desc">Click to view full project details →</div>
    `;

    a.appendChild(div);
    c.appendChild(a);
  });
}

function renderSkills(skills) {
  const c = document.getElementById("skills");
  c.innerHTML = "";

  // Friendly display names for each category
  const labels = {
    languages: "Languages",
    backend_and_databases: "Backend & Databases",
    devops_and_cloud: "DevOps & Cloud",
    frontend: "Frontend",
    machine_learning: "Machine Learning"
  };

  Object.entries(skills).forEach(([category, items]) => {
    const div = document.createElement("div");
    div.className = "card";

    const label = labels[category] || category.replaceAll("_", " ");

    div.innerHTML = `
      <div class="card-title">${label}</div>
      <div class="card-desc" style="margin-top: 8px;">
        ${items.map(i => `<span class="badge">${i}</span>`).join("")}
      </div>
    `;
    c.appendChild(div);
  });
}
