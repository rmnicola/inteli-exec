# Caso 1: perguntas e respostas (casos de teste da skill)

Doze perguntas que o time comercial faz à Renata, coordenadora de vendas. Cada uma traz a resposta esperada e a fonte. Use-as para testar o NotebookLM e a skill `tira-duvidas-politicas` e para mostrar à turma onde cada um acerta e erra.

Documentos (todos em `../politicas-institucionais/`):

| Sigla | Documento |
|---|---|
| **COM3** | Política Comercial v3 (POL-COM-003), vigente |
| **SUP** | Política de Compras (POL-SUP-001) |
| **OPE** | Nível de Serviço de Entrega e Devoluções (POL-OPE-002) |
| **ADM** | Política de Viagens e Despesas (POL-ADM-004) |
| **RH** | Perguntas Frequentes de RH (RH-FAQ-2026) |
| **DS-07** | Critérios de Avaliação de Transportadoras (usado no caso 2; aqui é só volume) |

**Para a demonstração ao vivo**, use estas cinco, nesta ordem: **1** (alçada de desconto), **4** (combinar documentos), **6** (ponte para o caso 2), **9** (sem resposta) e **11** (ambígua).

---

### 1. "Posso dar 5% de desconto para um cliente novo?"
- **Resposta esperada:** Não sem aprovação. O vendedor aprova até 3%; de 3% a 7%, quem aprova é a Diretora Comercial.
- **Fonte:** COM3 §4.2.
- **O que testa:** **alçada**. O vendedor quer ouvir "sim"; a resposta certa diz até quanto ele pode sozinho e quem aprova acima disso. Sem boa instrução, o modelo tende a responder só "sim, com aprovação", sem dizer de quem.

### 2. "Qual é o prazo de pagamento padrão?"
- **Resposta esperada:** 28 dias a partir da emissão da nota fiscal. De 29 a 45 dias, com aprovação da Diretora Comercial. Acima de 45, só com o CEO.
- **Fonte:** COM3 §7.1 e §7.2.
- **O que testa:** a diferença entre o padrão e o que exige aprovação. Uma resposta só com "28 dias" está incompleta.

### 3. "O cliente da RMC fez um pedido de R$ 1.550 e eu dei 5% de desconto. Ele paga frete?"
- **Resposta esperada:** Sim. O valor considerado é o líquido, depois do desconto: R$ 1.550 × 0,95 = R$ 1.472,50, abaixo do mínimo de R$ 1.500 da RMC. Paga a taxa de R$ 85. Além disso, 5% de desconto exige aprovação da Diretora Comercial.
- **Fonte:** COM3 §8.1, §8.2 e §4.2.
- **O que testa:** uma conta simples e uma regra escondida (líquido ou bruto). É um bom momento para comentar que modelos de linguagem erram contas.

### 4. "Um restaurante na Grande SP quer comprar R$ 2.200, com 3% de desconto e 40 dias para pagar. Posso fechar? Quando chega?"
- **Resposta esperada:**
  - O desconto de 3% o vendedor pode dar.
  - Os 40 dias de prazo precisam de aprovação da Diretora Comercial.
  - O pedido líquido é de R$ 2.134, abaixo de R$ 3.000, então há taxa de entrega de R$ 140.
  - A entrega na Grande SP é em D+2.
  - Se o restaurante tiver restrição de horário, pode pedir agendamento, que tem prioridade para restaurantes.
- **Fonte:** COM3 §4.2, §7.1, §8.1 e §8.2; OPE §3.1 e §4.
- **O que testa:** **combinar dois documentos** (comercial e logística) numa única resposta.

### 5. "O cliente quer devolver 10 caixas fechadas de detergente que recebeu há 9 dias. Pode?"
- **Resposta esperada:** Pela regra, não. A devolução sem avaria é aceita em até 7 dias, com embalagem original fechada e frete por conta do cliente. Já se passaram 9 dias. A exceção seria pelo fluxo de exceções; o vendedor não pode aceitar por conta própria. Vale perguntar se a devolução é por erro da Vale Verde, porque nesse caso o prazo de 7 dias não se aplica.
- **Fonte:** OPE §7.1, §7.2 e §7.4; COM3 §10.2 e §11.
- **O que testa:** **combinar documentos** e saber perguntar pela exceção.

### 6. "Um cliente-chave quer renovar o contrato anual passando de 4% para 8% de desconto e de 35 para 45 dias de prazo. Quem aprova?"
- **Resposta esperada:**
  - 8% está acima de 7%, então o desconto vai para o CEO, com parecer prévio do Financeiro.
  - Os 45 dias de prazo a Diretora Comercial pode aprovar.
  - Como é renovação com mudança de desconto, a análise de margem do Financeiro é obrigatória em qualquer percentual. Teria que ser feita mesmo que o desconto fosse de 5%.
  - A análise deve ser pedida com pelo menos 20 dias úteis de antecedência do vencimento.
- **Fonte:** COM3 §4.2, §5.2, §5.3 e §7.1.
- **O que testa:** **ponte para o caso 2**. É exatamente o pedido do Sabor & Cia na reunião que abre o caso 2, e mostra por que o "vou ver se consigo uns 5%" da Carla não é compromisso. Para a turma: os documentos não falam do Sabor & Cia. Se você perguntar "o Sabor pode ter 8%?", a skill não sabe quem é o Sabor e deve dizer isso.

### 7. "Preciso contratar a manutenção das empilhadeiras: são uns R$ 5 mil por mês, contrato de um ano. Quantas cotações?"
- **Resposta esperada:** O valor anual é de R$ 60 mil, acima de R$ 50 mil. São necessárias 3 cotações válidas, com aprovação do diretor da área e da Gerente Financeira. Contratos acima de R$ 50 mil por ano também são revisados pelo Financeiro antes da assinatura.
- **Fonte:** SUP §3.1 e §9.1.
- **O que testa:** a regra de usar o **valor anual**, e não o mensal. Se o modelo usar R$ 5 mil, enquadra errado, com 1 cotação. Prepara o caso 2, em que a contratação da transportadora exige 3 cotações válidas.

### 8. "Vou visitar um cliente em São Paulo com meu carro e dormir lá uma noite. O que posso reembolsar?"
- **Resposta esperada:**
  - Quilometragem a R$ 1,20/km, ida e volta pela rota mais curta (cerca de 190 km de Campinas, ou R$ 228), mais pedágios e estacionamento com comprovante.
  - Hotel de até R$ 450 (São Paulo é capital).
  - Alimentação de até R$ 120 por dia.
  - Como há pernoite, precisa de aprovação prévia do gestor no sistema.
  - Prestação de contas em até 5 dias úteis.
- **Fonte:** ADM §3.1, §4.1, §5.1, §6.1 e §8.1.
- **O que testa:** uma pergunta em documento de **volume**. Mostra que o NotebookLM encontra a informação em documentos que não são o foco.

### 9. "Qual é o percentual de comissão do vendedor?"
- **Resposta esperada:** A informação não está nos documentos. A política comercial só diz que desconto sem registro não conta para comissão (COM3 §4.3), mas não traz o percentual. A skill deve dizer que não encontrou e sugerir procurar a Diretora Comercial ou o RH.
- **Fonte:** nenhuma. Há só uma menção à comissão em COM3 §4.3.
- **O que testa:** **dizer "não encontrei"**. A menção à comissão em COM3 é uma isca: um modelo mal instruído pode inventar um percentual.

### 10. "Damos desconto para pagamento antecipado?"
- **Resposta esperada:** Os documentos não tratam de desconto por pagamento antecipado. Eles só dizem que o primeiro pedido de cliente novo é faturado para pagamento antecipado (COM3 §7.3), o que é outra coisa. Procurar a Diretora Comercial ou o Financeiro.
- **Fonte:** nenhuma. Há uma menção próxima em COM3 §7.3.
- **O que testa:** **não inventar** a partir de um trecho parecido.

### 11. "Qual é o prazo?"
- **Resposta esperada:** A skill deve **perguntar de volta**: prazo de pagamento, de entrega, de devolução, de comunicação de avaria ou de prestação de contas? Depois, responder conforme a escolha.
- **Fonte:** COM3 §7, OPE §3, §6 e §7, ADM §8.
- **O que testa:** **pergunta ambígua**. A instrução manda pedir esclarecimento em vez de chutar. Sem essa regra, o modelo costuma escolher um dos prazos e responder com segurança.

### 12. "Sou do centro de distribuição. Posso fazer home office às sextas?"
- **Resposta esperada:** Não. A operação (centro de distribuição, expedição, frota) não tem home office, porque o trabalho é presencial. O home office de até 2 dias por semana vale só para as áreas administrativas.
- **Fonte:** RH, seção "Jornada e home office".
- **O que testa:** uma regra com exceção. Um modelo apressado responde "sim, até 2 dias por semana".

---

## Leitura rápida para o professor

| Pergunta | Tipo | Risco de erro sem boa instrução |
|---|---|---|
| 1, 2 | Alçadas e prazos | Médio |
| 3, 4, 5 | Combinar regras ou documentos | Médio |
| 6 | Ponte para o caso 2 | Médio |
| 7 | Regra escondida (valor anual) | Médio |
| 8, 12 | Documento de volume | Baixo a médio |
| 9, 10 | Sem resposta, com isca | Alto |
| 11 | Ambígua | Alto |
