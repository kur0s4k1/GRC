(function () {
  "use strict";
  const data = window.GRC_DATA;
  const search = document.getElementById("search");
  const group = document.getElementById("group");
  const cost = document.getElementById("cost");
  const cards = document.getElementById("cards");
  const count = document.getElementById("count");
  const empty = document.getElementById("empty");
  const more = document.getElementById("more");
  if (!data || !Array.isArray(data.controls)) {
    count.textContent = "No se pudo cargar el catálogo.";
    return;
  }

  const themes = { "5": "Organizativos", "6": "Personas", "7": "Físicos", "8": "Tecnológicos" };
  let limit = 12;
  const normalize = value => String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("es");
  const element = (tag, className, content) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (content !== undefined) node.textContent = content;
    return node;
  };

  function matchesCost(control, selected) {
    if (selected === "all") return true;
    if (selected === "none") return control.tools.length === 0;
    return control.tools.some(name => {
      const pricing = data.tools[name].pricing;
      if (selected === "free") return pricing === "gratis" || pricing === "freemium";
      if (selected === "paid") return pricing === "pago" || pricing === "licencia" || pricing === "freemium";
      return pricing === "cotizacion";
    });
  }

  function toolCard(name) {
    const tool = data.tools[name];
    const box = element("div", "tool");
    const head = element("div", "tool-head");
    const link = element("a", "", name + " ↗");
    link.href = tool.url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.setAttribute("aria-label", name + ", sitio oficial (abre en nueva pestaña)");
    const label = { gratis: "Gratis", freemium: "Plan gratis", pago: "De pago", cotizacion: "Cotización", licencia: "Según licencia" }[tool.pricing];
    head.append(link, element("span", "tag " + tool.pricing, label));
    box.append(head, element("p", "description", tool.description), element("p", "price", tool.price), element("p", "meta", "Modalidad: " + tool.hosting), element("p", "risk", "Riesgo a evaluar: " + tool.risk));
    return box;
  }

  function controlCard(control) {
    const item = element("details", "card");
    item.id = control.id;
    const summary = element("summary");
    const top = element("span", "card-top");
    top.append(element("span", "id", control.id), element("span", "theme", themes[control.id.split(".")[1]]));
    const line = element("span", "card-summary");
    line.append(element("span", "", control.tools.length ? control.tools.join(" · ") : "Sin herramienta seleccionada"), element("span", "chevron", "⌄"));
    summary.append(top, element("span", "card-title", control.title), line);
    const body = element("div", "card-body");
    body.append(element("h3", "", "Trabajo manual"), element("p", "", control.manual), element("h3", "", "Herramientas que pueden ayudar"));
    if (control.tools.length) control.tools.forEach(name => body.append(toolCard(name)));
    else body.append(element("p", "none", "No se recomienda un producto concreto en esta edición. La tarea manual sigue siendo necesaria."));
    body.append(element("h3", "", "Cómo comprobar el resultado"), element("p", "", control.check));
    item.append(summary, body);
    return item;
  }

  function render() {
    const term = normalize(search.value.trim());
    const selectedGroup = group.value;
    const selectedCost = cost.value;
    const found = data.controls.filter(control => {
      if (selectedGroup !== "all" && !control.id.startsWith("A." + selectedGroup + ".")) return false;
      if (!matchesCost(control, selectedCost)) return false;
      const haystack = normalize([control.id, control.title, control.manual, ...control.tools].join(" "));
      return haystack.includes(term);
    });
    const shown = found.slice(0, limit);
    cards.replaceChildren(...shown.map(controlCard));
    count.textContent = found.length + (found.length === 1 ? " resultado" : " resultados") + (found.length > shown.length ? " · mostrando " + shown.length : "");
    empty.hidden = found.length !== 0;
    more.hidden = found.length <= shown.length;
  }

  function jump(identifier) {
    search.value = identifier;
    group.value = "all";
    cost.value = "all";
    limit = 12;
    render();
    history.replaceState(null, "", "#" + identifier);
    const card = document.getElementById(identifier);
    if (card) {
      card.open = true;
      card.scrollIntoView({ behavior: "smooth", block: "start" });
      card.querySelector("summary").focus({ preventScroll: true });
    }
  }

  [search, group, cost].forEach(input => input.addEventListener("input", () => { limit = 12; render(); }));
  more.addEventListener("click", () => { limit += 24; render(); });
  document.querySelectorAll("[data-jump]").forEach(button => button.addEventListener("click", () => jump(button.dataset.jump)));
  window.addEventListener("hashchange", () => {
    const identifier = decodeURIComponent(location.hash.slice(1));
    if (data.controls.some(control => control.id === identifier)) jump(identifier);
  });
  const initial = decodeURIComponent(location.hash.slice(1));
  if (data.controls.some(control => control.id === initial)) jump(initial);
  else render();
})();
