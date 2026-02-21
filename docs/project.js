const params = new URLSearchParams(window.location.search);
const slug = params.get("slug");

const API = `https://me-api-playground-1-xmn8.onrender.com/projects/${slug}`;



fetch(API)
  .then(res => {
    if (!res.ok) throw new Error("Project not found");
    return res.json();
  })
  .then(data => {

    // ---------------- Title ----------------
    document.getElementById("title").innerText = data.title;
    document.getElementById("subtitle").innerText = data.subtitle;

    // ---------------- Overview ----------------
    const overview = document.getElementById("overview");
    overview.innerHTML = "";
    (data.overview || []).forEach(p => {
      const para = document.createElement("p");
      para.innerText = p;
      overview.appendChild(para);
    });

    // ---------------- Links ----------------
    if (data.links) {
      const linksDiv = document.getElementById("links");
      linksDiv.style.display = "block";
      linksDiv.innerHTML = "<strong>External Resources</strong><ul></ul>";

      const ul = linksDiv.querySelector("ul");
      Object.entries(data.links).forEach(([name, url]) => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${url}" target="_blank" style="color: var(--accent);">${name}</a>`;
        ul.appendChild(li);
      });
    }

    // ---------------- Architecture ----------------
    const arch = document.getElementById("architecture");
    arch.innerHTML = "";

    const archItems =
      data.technical_details?.["Technical Architecture & Innovations"] || [];

    archItems.forEach(item => {
      const li = document.createElement("li");
      li.innerText = item;
      arch.appendChild(li);
    });

    // Cross-project link
    if (slug === "ssbc") {
      const li = document.createElement("li");
      li.innerHTML = `
        Builds upon architectural insights from 
        <a href="project.html?slug=vreyesam" style="color: var(--accent);">
          VREyeSAM
        </a>.
      `;
      arch.appendChild(li);
    }

    // ---------------- Methodology ----------------
    const method = document.getElementById("methodology");
    method.innerHTML = "";

    Object.entries(data.technical_details || {}).forEach(([key, items]) => {
      if (key === "Technical Architecture & Innovations") return;
      items.forEach(item => {
        const li = document.createElement("li");
        li.innerText = item;
        method.appendChild(li);
      });
    });

    // ---------------- Metrics ----------------
    const metrics = document.getElementById("metrics");
    metrics.innerHTML = "";

    Object.entries(data.results?.metrics || {}).forEach(([k, v]) => {
      const span = document.createElement("span");
      span.className = "badge";
      span.innerText = `${k}: ${v}`;
      metrics.appendChild(span);
    });

    // ---------------- Impact ----------------
    const impact = document.getElementById("impact");
    impact.innerHTML = "";

    (data.results?.highlights || []).forEach(item => {
      const li = document.createElement("li");
      li.innerText = item;
      impact.appendChild(li);
    });
  })
  .catch(() => {
    document.body.innerHTML = "<h1>Project not found</h1>";
  });
