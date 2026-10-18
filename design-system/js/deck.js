/* Navegação do deck Inteli.
   L, →, espaço, Enter, PageDown: avança (próximo passo da animação ou próximo slide)
   H, ←, Backspace, PageUp: volta um passo
   J, ↓: pula para o próximo slide, ignorando as animações (o slide aparece completo)
   K, ↑: pula para o slide anterior, ignorando as animações (o slide aparece completo)
   Home/End: primeiro e último · F: tela cheia · #N na URL: abre no slide N.
   Passos: elementos com a classe .passo entram a cada avanço, antes do próximo slide.
   data-passo="N": entra no passo N (padrão: a ordem no HTML) · data-sai="N": some no passo N.
   Um elemento .passo com data-passo="0" começa visível (útil com data-sai). */
(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  let atual = 0;

  slides.forEach((s, i) => s.setAttribute("data-numero", i + 1));

  /* Cada elemento .passo entra no passo data-passo (padrão: sua ordem no HTML) e,
     se tiver data-sai, some no passo data-sai. Os estados do slide são os valores distintos
     de data-passo e data-sai, em ordem. Estado 0 = antes do primeiro passo. */
  const passosDe = (s) => {
    const els = Array.from(s.querySelectorAll(".passo"));
    const itens = els.map((el, i) => ({
      el,
      entra: el.dataset.passo !== undefined ? parseFloat(el.dataset.passo) : i + 1,
      sai: el.dataset.sai !== undefined ? parseFloat(el.dataset.sai) : Infinity,
    }));
    const marcos = [...new Set(itens.flatMap((x) => [x.entra, x.sai]).filter((v) => v > 0 && v !== Infinity))].sort((a, b) => a - b);
    return { itens, marcos };
  };

  /* Mostra o slide no estado n (0 = inicial; Infinity = último estado). */
  function mostrarPassos(s, n) {
    const { itens, marcos } = passosDe(s);
    const k = Math.min(n, marcos.length);
    const limite = k === 0 ? 0 : marcos[k - 1];
    itens.forEach((x) => x.el.classList.toggle("visivel", x.entra <= limite && limite < x.sai));
    s.dataset.estado = k;
  }
  const visiveis = (s) => parseInt(s.dataset.estado || "0", 10);
  const totalPassos = (s) => passosDe(s).marcos.length;

  function escalar() {
    const e = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
    document.documentElement.style.setProperty("--escala", e);
  }

  function ir(n, atualizarUrl = true, passos = 0) {
    if (typeof fecharAjuda === "function") fecharAjuda();
    atual = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, i) => s.classList.toggle("atual", i === atual));
    mostrarPassos(slides[atual], passos);
    if (atualizarUrl) history.replaceState(null, "", "#" + (atual + 1));
  }

  function avancar() {
    const s = slides[atual];
    if (visiveis(s) < totalPassos(s)) mostrarPassos(s, visiveis(s) + 1);
    else if (atual < slides.length - 1) ir(atual + 1);
  }

  function voltar() {
    const s = slides[atual];
    if (visiveis(s) > 0) mostrarPassos(s, visiveis(s) - 1);
    else if (atual > 0) ir(atual - 1, true, Infinity);
  }

  function lerUrl() {
    const n = parseInt(location.hash.slice(1), 10);
    ir(Number.isFinite(n) ? n - 1 : 0, false);
  }

  /* Agenda: clicar num item leva ao slide de agenda daquele item (data-agora = posição do item). */
  document.addEventListener("click", (ev) => {
    const item = ev.target.closest && ev.target.closest(".slide.agenda .item");
    if (!item) return;
    const pos = Array.from(item.parentElement.querySelectorAll(".item")).indexOf(item);
    const destino = slides.findIndex((s) => s.classList.contains("agenda") && parseInt(s.dataset.agora, 10) === pos);
    if (destino >= 0) ir(destino);
  });

  /* Slides interativos: teclas digitadas num controle (campo, seletor, controle deslizante)
     ficam com o controle. Esc devolve o teclado à navegação. */
  document.addEventListener("keydown", (ev) => {
    if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
    if (ev.target.closest && ev.target.closest("input, select, textarea, [contenteditable]")) {
      if (ev.key === "Escape") ev.target.blur();
      return;
    }
    if (ev.target.closest && ev.target.closest("button")) ev.target.blur();
    const k = ev.key;
    if (["l", "L", "ArrowRight", "PageDown", " ", "Enter"].includes(k)) { avancar(); ev.preventDefault(); }
    else if (["h", "H", "ArrowLeft", "PageUp", "Backspace"].includes(k)) { voltar(); ev.preventDefault(); }
    else if (["j", "J", "ArrowDown"].includes(k)) { if (atual < slides.length - 1) ir(atual + 1, true, Infinity); ev.preventDefault(); }
    else if (["k", "K", "ArrowUp"].includes(k)) { if (atual > 0) ir(atual - 1, true, Infinity); ev.preventDefault(); }
    else if (k === "Home") ir(0);
    else if (k === "End") ir(slides.length - 1, true, Infinity);
    else if (k === "f" || k === "F") {
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    }
  });

  /* Ajuda guiada: num slide com elementos marcados com data-ajuda="texto", um botão "?" no canto
     percorre esses elementos, na ordem de data-ajuda-ordem (ou do HTML), com um balão em cada um. */
  let ajuda = null;
  function fecharAjuda() { if (ajuda) { ajuda.camada.remove(); ajuda = null; } }
  function mostrarAjuda() {
    const { s, itens, i, camada } = ajuda;
    const el = itens[i];
    const R = s.getBoundingClientRect(), esc = R.width / 1600, r = el.getBoundingClientRect();
    const x = (r.left - R.left) / esc, y = (r.top - R.top) / esc, w = r.width / esc, h = r.height / esc;
    camada.replaceChildren();
    const foco = document.createElement("div");
    foco.className = "ajuda-foco";
    Object.assign(foco.style, { left: x - 10 + "px", top: y - 10 + "px", width: w + 20 + "px", height: h + 20 + "px" });
    const balao = document.createElement("div");
    balao.className = "ajuda-balao";
    balao.innerHTML = `<p></p><div class="ajuda-acoes"><span class="ajuda-conta">${i + 1}/${itens.length}</span>` +
      (i > 0 ? '<button data-a="ant">anterior</button>' : "") +
      `<button data-a="prox" class="ativo">${i < itens.length - 1 ? "próximo" : "fechar"}</button></div>`;
    /* O texto fica como está; o deck pode listar, embaixo, notas de rodapé (ex.: o que cada sigla significa)
       definindo window.notasAjuda(texto) → [[termo, significado], ...]. */
    balao.querySelector("p").textContent = el.dataset.ajuda;
    const notas = window.notasAjuda ? window.notasAjuda(el.dataset.ajuda) : [];
    if (notas.length) {
      const rod = document.createElement("div");
      rod.className = "ajuda-notas";
      for (const [termo, sig] of notas) {
        const l = document.createElement("div");
        l.innerHTML = "<b></b> → <span></span>";
        l.querySelector("b").textContent = termo; l.querySelector("span").textContent = sig;
        rod.append(l);
      }
      balao.querySelector("p").after(rod);
    }
    camada.append(foco, balao);
    /* abaixo do elemento se couber; senão, acima; sempre dentro do slide */
    /* a largura vem antes da medida da altura; depois, tenta abaixo, acima, à direita e à esquerda do
       elemento, e por fim o canto em que menos o cobre. O balão nunca sai da área do slide (margem de 40px). */
    const bw = 560, M = 40, G = 24;
    balao.style.width = bw + "px";
    const bh = balao.offsetHeight;
    const cabe = (bx, by) => bx >= M && by >= M && bx + bw <= 1600 - M && by + bh <= 900 - M;
    const centroX = Math.max(M, Math.min(1600 - bw - M, x + w / 2 - bw / 2));
    const centroY = Math.max(M, Math.min(900 - bh - M, y + h / 2 - bh / 2));
    const opcoes = [[centroX, y + h + G], [centroX, y - bh - G], [x + w + G, centroY], [x - bw - G, centroY]];
    let [bx, by] = opcoes.find(([a, b]) => cabe(a, b)) || [];
    if (bx === undefined) {
      /* nenhum lado livre: o canto do slide mais longe do centro do elemento */
      bx = x + w / 2 < 800 ? 1600 - bw - M : M;
      by = y + h / 2 < 450 ? 900 - bh - M : M;
    }
    Object.assign(balao.style, { left: bx + "px", top: by + "px" });
    balao.addEventListener("click", (ev) => {
      const a = ev.target.dataset.a;
      if (a === "ant") { ajuda.i--; mostrarAjuda(); }
      else if (a === "prox") { if (ajuda.i < itens.length - 1) { ajuda.i++; mostrarAjuda(); } else fecharAjuda(); }
      ev.stopPropagation();
    });
  }
  function abrirAjuda(s) {
    const itens = Array.from(s.querySelectorAll("[data-ajuda]")).filter((el) => el.getClientRects().length)
      .sort((a, b) => (parseFloat(a.dataset.ajudaOrdem) || 0) - (parseFloat(b.dataset.ajudaOrdem) || 0));
    if (!itens.length) return;
    fecharAjuda();
    const camada = document.createElement("div");
    camada.className = "ajuda-camada";
    s.append(camada);
    ajuda = { s, itens, i: 0, camada };
    mostrarAjuda();
  }
  for (const s of slides) {
    if (!s.querySelector("[data-ajuda]")) continue;
    const b = document.createElement("button");
    b.className = "ajuda-botao sangra";
    b.textContent = "?";
    b.title = "ajuda";
    b.addEventListener("click", (ev) => { ev.stopPropagation(); ajuda && ajuda.s === s ? fecharAjuda() : abrirAjuda(s); });
    s.append(b);
  }
  document.addEventListener("keydown", (ev) => { if (ev.key === "Escape") fecharAjuda(); });

  /* Impressão / PDF: todo slide no seu último estado. Depois, volta ao estado da tela. */
  let estadoNaTela = 0;
  function prepararImpressao() { estadoNaTela = visiveis(slides[atual]); slides.forEach((s) => mostrarPassos(s, Infinity)); }
  window.addEventListener("beforeprint", prepararImpressao);
  window.addEventListener("afterprint", () => ir(atual, false, estadoNaTela));

  window.addEventListener("resize", escalar);
  window.addEventListener("hashchange", lerUrl);
  escalar();
  lerUrl();

  /* Usado pelas ferramentas de verificação. */
  window.deck = { ir, total: slides.length, slides, passos: (i) => totalPassos(slides[i]), prepararImpressao };
})();
