/* Tokenizador BPE (o mesmo algoritmo do tiktoken), com os vocabulários de tokens-vocab.js.
   tokenizar(texto, "gpt3" | "gpt4o") → lista de tokens, cada um como Uint8Array com os bytes UTF-8. */
(function () {
  const PADROES = {
    /* r50k_base (GPT-2 e GPT-3) */
    gpt3: /'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+/gu,
    /* o200k_base (GPT-4o); os sufixos (?i:'s|…) escritos sem o modificador de caixa */
    gpt4o: new RegExp([
      "[^\\r\\n\\p{L}\\p{N}]?[\\p{Lu}\\p{Lt}\\p{Lm}\\p{Lo}\\p{M}]*[\\p{Ll}\\p{Lm}\\p{Lo}\\p{M}]+(?:'[sS]|'[tT]|'[rR][eE]|'[vV][eE]|'[mM]|'[lL][lL]|'[dD])?",
      "[^\\r\\n\\p{L}\\p{N}]?[\\p{Lu}\\p{Lt}\\p{Lm}\\p{Lo}\\p{M}]+[\\p{Ll}\\p{Lm}\\p{Lo}\\p{M}]*(?:'[sS]|'[tT]|'[rR][eE]|'[vV][eE]|'[mM]|'[lL][lL]|'[dD])?",
      "\\p{N}{1,3}",
      " ?[^\\s\\p{L}\\p{N}]+[\\r\\n/]*",
      "\\s*[\\r\\n]+",
      "\\s+(?!\\S)",
      "\\s+",
    ].join("|"), "gu"),
  };
  const ranks = {};
  /* chave de um token: os bytes como string latin1 */
  const chave = (bytes) => String.fromCharCode.apply(null, bytes);
  function vocab(nome) {
    if (!ranks[nome]) {
      const m = new Map();
      window.VOCAB_TOKENS[nome].split(" ").forEach((b64, r) => m.set(atob(b64), r));
      ranks[nome] = m;
    }
    return ranks[nome];
  }
  /* junta, a cada rodada, o par vizinho de menor rank, até não haver par no vocabulário */
  function bpe(bytes, m) {
    if (m.has(chave(bytes))) return [bytes];
    let partes = Array.from(bytes, (b) => [b]);
    for (;;) {
      let melhor = -1, rank = Infinity;
      for (let i = 0; i < partes.length - 1; i++) {
        const r = m.get(chave(partes[i].concat(partes[i + 1])));
        if (r !== undefined && r < rank) { rank = r; melhor = i; }
      }
      if (melhor < 0) break;
      partes.splice(melhor, 2, partes[melhor].concat(partes[melhor + 1]));
    }
    return partes.map((p) => Uint8Array.from(p));
  }
  const utf8 = new TextEncoder();
  window.tokenizar = function (texto, nome) {
    const m = vocab(nome), out = [];
    for (const pedaco of texto.match(PADROES[nome]) || []) out.push(...bpe(utf8.encode(pedaco), m));
    return out;
  };
})();
