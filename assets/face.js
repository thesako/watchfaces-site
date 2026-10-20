// Face page: switch the large dial between colours and between active and always-on
const dial = document.getElementById("dial");
const active = document.getElementById("active");
const aod = document.getElementById("aod");
const swatches = document.querySelectorAll(".colours button");
let colour = dial.getAttribute("src");

function show(src, mode) {
  dial.src = src;
  dial.alt = dial.alt.replace(/(active|always-on)$/, mode);
  active.setAttribute("aria-pressed", mode === "active");
  aod.setAttribute("aria-pressed", mode === "always-on");
}

active.addEventListener("click", () => show(colour, "active"));
aod.addEventListener("click", () => show(aod.dataset.src, "always-on"));
swatches.forEach((b) => b.addEventListener("click", () => {
  colour = b.dataset.active;
  swatches.forEach((s) => s.setAttribute("aria-pressed", s === b));
  show(colour, "active");
}));
