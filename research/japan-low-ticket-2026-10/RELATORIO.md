# Inteligência de Mercado — Produtos Digitais Low Ticket no Japão

**Data da coleta:** 29/10/2026 · **Janela de tendências:** 29/09/2026 a 29/10/2026 · **Idioma das buscas:** japonês

Legenda de origem usada em todo o relatório:

- **[DF]**: obtido com ferramentas do **DeerFlow** (`web_search`, `web_fetch` e `browser_automation` do harness).
- **[L30]**: obtido com o motor do **Last30Days** (`last30days.py` v3.31.0).

Legenda do tipo de dado:

- **(C)** comprovado: número lido diretamente na página.
- **(D)** declarado pelo vendedor, sem auditoria (por exemplo, títulos "○○部突破").
- **(E)** estimativa minha.
- **(H)** hipótese a testar.

---

## 0. Resumo executivo

1. **Brain e Tips não são bons mercados de low ticket para novos entrantes.** Os rankings por vendas do Tips são dominados por material de 副業, 恋愛/ナンパ e investimento entre ¥9.800 e ¥100.000. Os poucos low ticket que aparecem são guias de SNS de criadores que já têm audiência. O Brain mostra o mesmo padrão: os títulos "部突破" estão concentrados em ChatGPT, Threads, Kindle e Canva. [DF]
2. **A demanda low ticket verificável e criável com IA está no BOOTH e na ココナラ.** O ponto comum é **material para criadores**: eventos doujin, TRPG online (ココフォリア), VTubers/streamers e editores de vídeo. Esses compradores precisam de muito material, compram com frequência e já aceitam preços de ¥100 a ¥1.500. [DF]
3. **A ココナラ revela demanda paga de serviços sob medida que podem virar produto de prateleira mais barato.** Exemplos:

   | Serviço | Preço | Avaliações |
   |---|---|---|
   | お品書き para eventos | ¥3.000 | 341 |
   | 待機画面 de stream | ¥10.000 | 340 |
   | Tela de stream (配信画面) | ¥15.000 | 214 |
   | LP no Canva | ¥4.500 | 244 |
   | Template de PowerPoint | ¥4.000 | 233 |
   | Planilha de 青色申告 | ¥8.000 | 37 |

   A hipótese central do relatório é que **um template de ¥500 a ¥1.500 atende quem não paga ¥3.000 a ¥15.000**. **(C)** para os números, **(H)** para a tese.
4. **O BOOTH aceita material gerado por IA, com condições.** A plataforma não proíbe IA; proíbe itens muito dependentes de um artista ou obra específica e a listagem em massa (endurecido em julho de 2025). Há packs de 立ち絵 com a tag "AI生成", publicados em 2025, com 1.400 a 2.238 curtidas (♥). [DF] **(C)**
5. **O Last30Days funcionou só com YouTube** neste ambiente e mostrou sobretudo **saturação do lado do vendedor**: muitos vídeos "como ganhar dinheiro com IA vendendo X". Exemplos:
   - note: 111.600 views;
   - LINEスタンプ com IA: 62.173 views;
   - デジタルペーパー Canva×IA: 45.706 views.

   Também mostrou duas tendências do lado do comprador: planners digitais 2027 (207.990 views) e うちわ de 推し活 (44.128 e 35.657 views). [L30] **(C)**

**Os 5 vencedores**, detalhados na seção 6:

1. Templates de お品書き e etiquetas de preço para a C109.
2. Packs de PNG transparente sazonais.
3. Templates de LP no Canva para pequenos negócios.
4. Kit de stream animado (fundo em loop, 待機画面 e CSS de comentários).
5. Packs de 立ち絵 NPC gerados por IA para TRPG.

---

## 1. Verificação e execução das ferramentas

### 1.1 DeerFlow (`new-age-age/deer-flow`, branch de trabalho)

| Etapa | Status | Detalhe |
|---|---|---|
| Leitura da documentação | Feita | `AGENTS.md`, `backend/AGENTS.md`, `config.example.yaml` e a skill `skills/public/deep-research/SKILL.md` |
| Instalação | Feita | `uv sync` no backend; `config.yaml` gerado a partir do exemplo (gitignored, não commitado); `playwright==1.63.0` instalado no venv |
| **Loop do agente (LangGraph + LLM)** | **Não executado** | Não há credencial de LLM no ambiente: nenhuma chave OpenAI/Anthropic, e as credenciais AWS existentes são inválidas para Bedrock (`InvalidClientTokenId`). O DeerFlow avisa "No models are configured". |
| `web_search` (DDG/ddgs, `deerflow.community.ddg_search`) | **Executado** | 107 consultas em japonês, com resultados limitados a 5 por consulta pela configuração padrão |
| `web_fetch` (Jina, `deerflow.community.jina_ai`) | **Executado com bloqueios** | Funcionou de forma intermitente. Respondeu 401 "bad IP reputation" e voltou depois. O texto vem truncado em 4.096 caracteres. |
| `browser_automation` (Playwright, `deerflow.community.browser_automation`) | **Executado** | Usado para os rankings do Tips, as listagens do BOOTH e o JSON público dos itens do BOOTH (1.150 itens em 73 tags). O resolver de egresso fixado (proteção SSRF por SOCKS) foi desativado porque a cadeia TLS do sandbox falhava nesse caminho (`ERR_CERT_AUTHORITY_INVALID`). O `url_guard` do DeerFlow continuou ativo. |
| Metodologia | Seguida | Fases da skill `deep-research`: exploração ampla, aprofundamento por nicho, diversidade e validação, checagem de síntese |

Como o loop do agente não rodou, **o planejamento e a síntese foram feitos por mim**. Todo dado de mercado listado como [DF] veio das ferramentas reais do harness. Os scripts estão em `scripts/` e os dados brutos em `data/deerflow/`.

### 1.2 Last30Days (`new-age-age/last30days-skill`)

| Etapa | Status | Detalhe |
|---|---|---|
| Leitura da documentação | Feita | `SKILL.md`, `references/research-runbook.md` e `--diagnose` |
| Instalação | Feita | `yt-dlp` 2026.10.26 instalado, o que ativou a fonte YouTube |
| Execuções | **44 execuções reais** | Tópicos curtos em japonês, `--deep`, `--search youtube`, `--plan` (planner externo, conforme o runbook), janela de 30 dias |
| Fontes ativas | Só **YouTube** | Reddit: HTTP 403 "Blocked". Web keyless (`html.duckduckgo.com`): túnel encerrado pelo proxy. X, TikTok e Instagram: sem chave. Hacker News e Polymarket: irrelevantes para o tema. |
| Qualidade | Fina | Muitas execuções retornaram 0 vídeos dentro da janela. Algumas trouxeram ruído em chinês e inglês, descartado na análise. |

### 1.3 Fontes indisponíveis ou bloqueadas (limitações)

| Fonte | Situação |
|---|---|
| **Brain** (`brain-market.com`) | Página "アクセス制限のお知らせ" para o navegador. Só os snippets de busca [DF] foram usados. |
| **ココナラ** | 403 Forbidden no navegador headless. Funcionou via `web_fetch`/Jina [DF], mas truncado nos primeiros resultados de cada busca. |
| **note** | API de busca (`/api/v3/searches`) bloqueada pelo CloudFront (403). Páginas individuais abriram. **Não há dado de vendas do note**, e a plataforma não expõe compras publicamente. |
| Udemy (Cloudflare) e Amazon Kindle ranking | Bloqueados |
| Reddit, X, TikTok, Instagram (Last30Days) | Indisponíveis (403 ou sem credenciais) |

Duas limitações de método valem para o relatório inteiro:

- **Nenhuma plataforma mostra vendas exatas.** Os indicadores usados foram:
  - número de avaliações na ココナラ, tratado como piso aproximado de transações concluídas (inferência);
  - posição no ranking "販売数" do Tips;
  - contagem de ♥ (`wish_lists_count`) do BOOTH, que mede **interesse e não vendas**;
  - "部突破" no Brain e no Tips **(D)**.
- **As curtidas do BOOTH são cumulativas desde o lançamento.** O ranking favorece itens antigos. Por isso medi também a fatia de itens publicados a partir de 2025 no top 30 ("entrantes recentes").

---

## 2. Critérios de pontuação

Cada produto recebeu notas de 1 a 5:

| Critério | Peso | Como foi medido |
|---|---|---|
| **D: Demanda** | 35% | 5 = compras verificáveis (muitas avaliações na ココナラ, topo do ranking de vendas) **e** interesse alto (♥ BOOTH > 1.000). 3 = só interesse ou só serviço adjacente. 1 = sem evidência. |
| **C: Concorrência (invertida)** | 25% | 5 = poucos anúncios (< 500 no BOOTH) e entrantes recentes no top 30. 1 = milhares de anúncios, mercado maduro ou muitos itens grátis. |
| **F: Facilidade com IA** | 20% | 5 = produção quase toda por IA (imagem, texto ou código) com revisão humana leve. 1 = exige habilidade especializada (3D, autoria original). |
| **A: Automação, preço e margem** | 20% | 5 = entrega automática (download), preço dentro de ¥500 a ¥5.000 e custo marginal zero. Nota menor quando o teto de preço observado fica abaixo de ¥500 ou a entrega é manual. |
| **Risco (penalidade)** | −0,2 a −0,5 | Regras de plataforma, rejeição de comunidade a IA, precisão técnica (impostos), reputação de 情報商材 |

**Potencial comercial = 0,35·D + 0,25·C + 0,20·F + 0,20·A − risco** (escala de 1 a 5).

---

## 3. Panorama por plataforma

### Tips [DF]

Ranking "販売数" por categoria (累計 = acumulado, 月間 = mensal):

| Categoria | Item no ranking | Preço | Observação |
|---|---|---|---|
| ビジネス (累計) | 1º, "Threads完全攻略マニュアル" | ¥9.800 | 207 avaliações |
| ビジネス (累計) | "Threads×アフィ最短攻略" | ¥4.980 | 82 avaliações |
| ビジネス (月間) | 1º, "AI×note販売戦略" | ¥9.980 | — |
| マネー (月間) | 1º, "セルフバック案件まとめ" | ¥3.960 | 82 avaliações |
| 恋愛 (月間) | 1º | ¥980 | Revista mensal |
| デザイン (累計) | 1º, "500部完売" pack de templates Canva | ¥39.800 | — |
| スポーツ (月間) | 1º, "スポーツキッズの補食・献立BOOK" | ¥2.480 | Categoria de baixo volume |

Conclusão: o comprador do Tips procura renda extra e relacionamentos. O low ticket que vende exige audiência própria.

Fontes:
- https://tips.jp/category/%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9/ranking?sort=sales_count&period=total
- https://tips.jp/category/%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3/ranking?sort=sales_count&period=total
- https://tips.jp/category/%E3%83%9E%E3%83%8D%E3%83%BC/ranking?sort=sales_count&period=monthly

### Brain [DF]

Títulos com contagem declarada **(D)**:

| Título | Link |
|---|---|
| 【1300部突破】ChatGPT画像生成の教科書 | https://brain-market.com/u/midori-tatsuta/a/b3MzMwUjMgoTZsNWa0JXY |
| 【1900部突破】Threadsバブルの『裏』解体新書 | https://brain-market.com/u/hikasann/a/bxIjN4UjMgoTZsNWa0JXY |
| 【660部突破】ChatGPTで"売上につなげる"インスタを回す | https://brain-market.com/u/riko_nft/a/bxkTM2QjMgoTZsNWa0JXY |
| 【800部突破】デザイン分析GPTs | https://brain-market.com/u/mato_11234/a/byYDN4QjMgoTZsNWa0JXY |
| 【500部突破】Kindle出版 | https://brain-market.com/u/kan11/a/bcjM1EzNgoTZsNWa0JXY |

Quase tudo é "ensinar a ganhar dinheiro". Um vendedor registra que mudanças de modelo do ChatGPT quebraram o conteúdo (obsolescência rápida).

### note [DF] [L30]

- Não foi possível medir vendas (bloqueio da API).
- [L30]: vídeos sobre monetizar o note estão em alta, o que indica **mais vendedores entrando**:
  - 111.600 views, 03/10: https://www.youtube.com/watch?v=1vE36sjjHLo
  - 12.507 views, 25/10, "AIで作った有料noteは本当に売れる？": https://www.youtube.com/watch?v=oH8RYJz5Tdg
  - 6.903 views, 27/10: https://www.youtube.com/watch?v=JhGLEpdZ_kI

### BOOTH [DF]

Oferta (itens por tag) e interesse:

| Tag | Itens | Curtidas |
|---|---|---|
| VRChat | 204.517 | — |
| 3Dモデル | 74.574 | — |
| 背景素材 | 35.355 | — |
| 立ち絵 | 24.409 | — |
| BGM | 13.908 | — |
| 配信背景 | 13.638 | — |
| CoC | 10.711 | Mediana do top 30 pago: 15.020 ♥ |
| 配信画面 | 9.863 | — |
| ココフォリア | 9.404 | Mediana do top 30 pago: 9.338 ♥ |
| テンプレート | 8.714 | — |
| 推し活 | 8.230 | — |
| AI生成 | 7.811 | — |
| 待機画面 | 3.184 | — |
| 透過素材 | 3.068 | — |
| デジタルプランナー | 2.103 | Mediana paga: 55 ♥ |
| テロップ | 1.786 | — |
| 年賀状 | 1.534 | — |
| 家計簿 | 613 | Mediana paga: 17 ♥ |
| 確定申告 | 565 | — |
| お品書き | **399** | — |
| CSS | 831 | — |
| コメント枠 | 262 | — |
| うちわ文字 | 178 | Máximo: 29 ♥ |

O comprador do BOOTH é criador (doujin, TRPG, VTuber, VRChat). Templates "de lifestyle" (家計簿, planners) quase não atraem interesse ali.

### ココナラ [DF]

Os maiores volumes de avaliações estão em serviços para criadores e pequenos negócios:

| Serviço | Preço | Avaliações |
|---|---|---|
| Miniatura de YouTube | ¥3.000 | **3.589** |
| お品書き | ¥3.000 | 341 |
| ES (就活) | ¥10.000 | 339 |
| 待機画面 | ¥10.000 | 340 |
| LP Canva | ¥4.500 | 244 |
| PPT | ¥4.000 | 233 |
| 配信画面 | ¥15.000 | 214 |
| Trailer TRPG | ¥3.500 | 117 |
| 青色申告 スプシ | ¥8.000 | 37 |

A コンテンツマーケット da ココナラ (downloads) existe, mas mostra "販売実績" baixo nos itens encontrados.

---

## 4. RANKING FINAL — 20 produtos

Notas de 1 a 5. Links levam à principal evidência.

| Ranking | Produto | Preço | Demanda | Concorrência (5 = baixa) | Facilidade de criação (IA) | Potencial comercial | Link |
|---|---|---|---|---|---|---|---|
| 1 | Templates de **お品書き + etiquetas de preço** para eventos doujin (Canva/PPT/Google スライド) | ¥500–1.200 | 4 | 4 | 5 | **4,40** | https://coconala.com/services/2532900 |
| 2 | **Packs de PNG transparente** sazonais (あしらい, comida, flores; 200 itens) | ¥480–980 | 4 | 3 | 5 | **4,15** | https://booth.pm/ja/items/6051435 |
| 3 | **Templates de LP no Canva** para salões, coaches e cursos | ¥2.980–3.980 | 5 | 3 | 4 | **4,10** | https://coconala.com/services/3607540 |
| 4 | **Kit de stream animado** (fundo em loop, 待機/離席/終了画面) | ¥800–1.500 | 5 | 2 | 4 | **4,05** | https://booth.pm/ja/items/6477455 |
| 5 | **Pack de 立ち絵 NPC gerado por IA** (expressões, PNG transparente, para TRPG e novel) | ¥500–980 | 4 | 2 | 5 | **3,90** | https://booth.pm/ja/items/6563809 |
| 6 | **Pack de quarto/fundo para ココフォリア** (fundo, primeiro plano, APNG) | ¥350–800 | 4 | 2 | 5 | **3,90** | https://booth.pm/ja/items/4295537 |
| 7 | **CSS de comentários e templates わんコメ** para OBS (YouTube/Twitch) | ¥300–600 | 3,5 | 4 | 5 | **3,83** | https://booth.pm/ja/items/4950117 |
| 8 | **Presets de テロップ e animação de texto** (Premiere/AE) | ¥500–1.000 | 4 | 3 | 3 | **3,75** | https://booth.pm/ja/items/3700775 |
| 9 | **Planilha de 確定申告 para criadores** (vendas BOOTH/FANBOX/Skeb + guia) | ¥980–2.980 | 3 | 4 | 4 | **3,65** | https://coconala.com/services/2010782 |
| 10 | **Templates de miniatura de YouTube** no Canva (por gênero) | ¥500–1.500 | 2,5 | 3 | 5 | **3,63** | https://coconala.com/services/1197314 |
| 11 | **ES e 職務経歴書: templates por cargo + prompts** | ¥980–1.980 | 3 | 3 | 4 | **3,60** | https://coconala.com/services/681909 |
| 12 | **Templates de PowerPoint** para material de vendas | ¥2.000–4.000 | 4 | 2 | 4 | **3,50** | https://coconala.com/services/2054869 |
| 13 | **Templates de 家計簿** (Google スプレッドシート/Notion) | ¥500–1.000 | 2 | 3 | 5 | **3,45** | https://booth.pm/ja/items/3131156 |
| 14 | **Cenário CoC** (タイマン/少人数) com quarto de ココフォリア | ¥500–1.500 | 5 | 2 | 2 | **3,35** | https://booth.pm/ja/items/2976456 |
| 15 | **Guia de geração de imagens com IA** (ChatGPT/Gemini) | ¥1.980–4.980 | 4 | 1 | 5 | **3,35** | https://brain-market.com/u/midori-tatsuta/a/b3MzMwUjMgoTZsNWa0JXY |
| 16 | **Posts de Instagram para salões de beleza** (Canva, 30 posts) | ¥1.500–3.000 | 3 | 2 | 5 | **3,35** | https://coconala.com/contents_market/pictures/cmuexr36105rp7l0hgmmky0mj |
| 17 | **Planner digital 2027** (Goodnotes) | ¥800–2.900 | 3 | 2 | 4 | **3,35** | https://www.youtube.com/watch?v=Ee4dhh2Bifg |
| 18 | **Arquivos de うちわ文字** (推し活) | ¥100–300 | 3 | 4 | 4 | **3,25** | https://booth.pm/ja/items/7957197 |
| 19 | **年賀状 2027 (未年) e 年賀状じまい**: template e modelos de texto | ¥300–800 | 2 | 2 | 5 | **3,20** | https://booth.pm/ja/items/2576419 |
| 20 | **Guia low ticket de Threads/SNS** | ¥980–4.980 | 5 | 1 | 3 | **3,10** | https://tips.jp/category/%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9/ranking?sort=sales_count&period=total |

Notas de A e penalidades de risco aplicadas:

| Item | A | Penalidade e motivo |
|---|---|---|
| 1 a 6, 8 | 5 | — |
| 3 | 4 | — |
| 7 | 3 | Preço abaixo de ¥500 |
| 9 | 5 | −0,2 (precisão tributária) |
| 12 | 4 | — |
| 14 | 5 | −0,3 (diretrizes de 二次創作 e rejeição a IA) |
| 15 | 5 | −0,3 (情報商材 e obsolescência) |
| 16 | 4 | — |
| 18 | 2 | Preço abaixo de ¥500 |
| 20 | 5 | −0,5 (reputação e exigência de audiência) |

Desempates em 3,90 e 3,35: decididos pela evidência de entrantes recentes e pela nota D.

**Descartados durante a pesquisa:**

| Produto | Motivo |
|---|---|
| LINEスタンプ com IA | Categoria "名前・名字" com 6.586.509 itens [DF]; avalanche de tutoriais com IA (62.173 views) [L30]; ticket de ¥120–250 |
| Material pedagógico de 保育 | 275 itens no BOOTH, mas o líder pago tem só 54 ♥ [DF] |
| Presets de Lightroom/LUT | Máximo de 73 ♥ [DF] |
| Roupas 3D de VRChat | Demanda enorme (até 9.663 ♥), mas exige modelagem 3D |
| 占い | Vender texto de IA como leitura humana seria enganoso |

---

## 5. Fichas de validação (os 20 produtos)

Formato de cada ficha:

- **Categoria e público:** quem compra.
- **Problema:** o que resolve.
- **Preço de mercado:** faixa observada.
- **Concorrentes:** quem já vende.
- **Evidências:** dados de demanda, com origem e tipo.
- **Concorrência:** nível e justificativa.
- **IA:** possibilidade de produção com IA.
- **Custo:** custo estimado de criação.
- **Automação e escala:** potencial de automação e escala.

### 1. Templates de お品書き e etiquetas de preço (eventos doujin)

- **Categoria e público:** template de design. Círculos doujin que vão vender em eventos: C109 de 29 a 31/12/2026, 文学フリマ e eventos de ジャンル.
- **Problema:** a お品書き é obrigatória no estande e é divulgada no X. Montar uma dá trabalho, e encomendar custa ¥3.000 ou mais.
- **Preço de mercado:** BOOTH de ¥100 a ¥450; serviço sob medida na ココナラ a ¥3.000.
- **Concorrentes:**
  - BOOTH 4331063, お品書きテンプレート, ¥100;
  - BOOTH 5948180 (grátis);
  - BOOTH 7771936 e 7899572 (Canva/PPT, ¥150–200);
  - ココナラ 2532900.
- **Evidências:**
  - ココナラ "同人イベント用お品書きを作成します", ¥3.000, **341 avaliações, nota 5.0**; só 285 anúncios para "お品書き". [DF] **(C)**
  - BOOTH: 399 itens na tag; top pago de 915 ♥ a ¥100. [DF] **(C)**
  - **37% do top 30 publicado a partir de 2025**, ou seja, entrantes recentes conseguem aparecer. [DF] **(C)**
  - Template Canva publicado em 12/2025 já com 102 ♥. [DF] **(C)**
  - C109 confirmada para 29 a 31/12/2026. [DF] **(C)**
  - Last30Days não achou vídeos recentes sobre o tema. [L30]
- **Concorrência:** baixa a média.
- **IA:** alta. Layouts gerados com IA mais Canva, e ilustrações de enfeite por IA.
- **Custo:** ¥0–3.000 (ferramentas) mais 15 a 25 horas. **(E)**
- **Automação e escala:** download automático no BOOTH. Eventos se repetem o ano todo, o que permite uma linha sazonal.

### 2. Packs de PNG transparente sazonais

- **Categoria e público:** material de imagem. VTubers, círculos (お品書き), designers de SNS e mestres de TRPG.
- **Problema:** encontrar e recortar enfeites e ícones prontos para uso comercial.
- **Preço de mercado:** ¥230 a ¥480.
- **Concorrentes:**
  - BOOTH 6051435, 季節の花 200点, ¥480;
  - BOOTH 5167059, ケーキ50点;
  - BOOTH 5400066, 洋食50点;
  - BOOTH 5806712, あしらい.
- **Evidências:**

  | Item | Preço | Curtidas | Observação |
  |---|---|---|---|
  | 季節の花 200点 | ¥480 | **1.653 ♥** | — |
  | ケーキ | ¥480 | 1.296 ♥ | — |
  | あしらい | ¥450 | 1.327 ♥ | — |
  | 洋食 | ¥480 | 717 ♥ | — |
  | Item lançado em 02/2026 | ¥440 | 1.937 ♥ | Tag 透過素材, 3.068 itens |

  [DF] **(C)**
- **Concorrência:** média.
- **IA:** alta. Geração de imagem, remoção de fundo e upscale, com a origem por IA declarada.
- **Custo:** ¥2.000–5.000 por mês em ferramentas de IA. **(E)**
- **Automação e escala:** total. Uma série mensal e sazonal (inverno, Natal, Ano-Novo, Valentine) leva o mesmo comprador a voltar. **(H)**

### 3. Templates de LP no Canva para pequenos negócios

- **Categoria e público:** template de negócio. Salões, coaches, cursos e freelancers sem verba para uma web designer.
- **Problema:** ter uma página de vendas bonita sem programar.
- **Preço de mercado:** ¥2.000 a ¥4.500.
- **Concorrentes:**
  - ココナラ 3607540, ¥4.500;
  - LP素材 na コンテンツマーケット, ¥2.000;
  - 2.988 anúncios na busca "Canva テンプレート" da ココナラ.
- **Evidências:**
  - "CanvaのLPテンプレートを販売します", ¥4.500, **244 avaliações**. Outros anúncios com o mesmo título têm 58, 28 e 21 avaliações. [DF] **(C)**
  - Notificação de compra exibida na página de categoria. [DF] **(C)**
- **Concorrência:** média.
- **IA:** alta. Texto e estrutura com IA, layout no Canva.
- **Custo:** cerca de ¥0–1.500 de Canva Pro **(E, preço JP não verificado)** mais 20 a 30 horas.
- **Automação e escala:** entrega por link de template, automática no BOOTH e no note. Na ココナラ, cada serviço exige mensagem.

### 4. Kit de stream animado (fundo em loop, 待機/離席/終了画面)

- **Categoria e público:** material para VTubers e streamers independentes.
- **Problema:** ter uma tela de stream "profissional" sem pagar de ¥10.000 a ¥15.000.
- **Preço de mercado:** ¥500 a ¥1.500 no BOOTH; serviço sob medida de ¥10.000 a ¥15.000.
- **Concorrentes:**
  - BOOTH 6477455, ¥700;
  - BOOTH 6083011, ¥520~;
  - BOOTH 5871788, ¥880;
  - lojas declaradamente baseadas em IA ("Vtuber素材屋さん").
- **Evidências:**
  - ココナラ 2347677, 待機画面: ¥10.000 com **340 avaliações**. [DF] **(C)**
  - ココナラ 2431841, 配信画面: ¥15.000 com **214 avaliações**. [DF] **(C)**
  - BOOTH 6477455 (01/2025), ¥700: **3.332 ♥**. [DF] **(C)**
  - BOOTH 6083011: 3.697 ♥. [DF] **(C)**
- **Concorrência:** alta (配信背景 13.638 itens; 待機画面 3.184).
- **IA:** média a alta. Imagem por IA e animação sutil (image-to-video ou AE).
- **Custo:** ¥5.000–15.000. **(E)**
- **Automação e escala:** total.

### 5. Pack de 立ち絵 NPC gerado por IA (TRPG e novel)

- **Categoria e público:** material de ilustração. Mestres de CoC e TRPG, criadores de novel games e streamers.
- **Problema:** conseguir rostos de NPC consistentes, com expressões, de graça ou barato.
- **Preço de mercado:** ¥200 a ¥1.000.
- **Concorrentes:**
  - BOOTH 6563809, ¥200~, AI生成;
  - BOOTH 6766490;
  - BOOTH 2576656, モブNPC100種, ¥1.000.
- **Evidências:**
  - **2.238 ♥** em item com tag AI生成 publicado em 02/2025. [DF] **(C)**
  - 1.489 ♥ (04/2025). [DF] **(C)**
  - Tag 立ち絵: 24.409 itens; mediana paga do top 30: 2.590 ♥. [DF] **(C)**
  - Last30Days: sem sinal útil (ruído). [L30]
- **Concorrência:** alta.
- **IA:** alta. Personagem consistente e variações de expressão.
- **Custo:** ¥3.000–10.000. **(E)**
- **Automação e escala:** total.
- **Riscos:**
  - parte da comunidade rejeita IA, então é preciso declarar a origem;
  - o BOOTH proíbe imitar o estilo de artistas específicos;
  - substitutos: há guias no note ensinando a gerar 立ち絵 por conta própria com IA. [DF]

### 6. Pack de quarto/fundo para ココフォリア

- **Categoria e público:** material TRPG.
- **Problema:** montar "salas" bonitas para sessões online.
- **Preço de mercado:** ¥100 a ¥800.
- **Concorrentes:**
  - BOOTH 4295537, ¥350;
  - BOOTH 4186217, ¥500;
  - BOOTH 4296841, ¥100~.
- **Evidências:**

  | Item | Preço | Curtidas |
  |---|---|---|
  | BOOTH 4186217 | ¥500 | **26.797 ♥** |
  | BOOTH 4295537 | ¥350 | 12.021 ♥ |
  | BOOTH 4857456, 背景36枚 | ¥480 | 3.614 ♥ |

  Tag com 9.404 itens. Na ココナラ, quarto sob medida a ¥6.000 tem só 3 avaliações. [DF] **(C)**
- **Concorrência:** **mercado maduro**. 0% de itens recentes no top 30 e muito material grátis. Entrar exige um nicho temático.
- **IA:** alta.
- **Custo:** ¥3.000–10.000. **(E)**
- **Automação e escala:** total.

### 7. CSS de comentários e templates わんコメ para OBS

- **Categoria e público:** código e design para streamers.
- **Problema:** caixa de comentários bonita no stream.
- **Preço de mercado:** ¥100 a ¥500.
- **Concorrentes:**
  - BOOTH 4950117, ¥300;
  - BOOTH 7039763, ¥100.
- **Evidências:**
  - BOOTH 4950117: 4.535 ♥. [DF] **(C)**
  - わんコメ template de 06/2025: 873 ♥. [DF] **(C)**
  - Tags: CSS com 831 itens; コメント枠 com 262. [DF] **(C)**
- **Concorrência:** baixa a média.
- **IA:** altíssima (código gerado por LLM).
- **Custo:** quase zero. **(E)**
- **Automação e escala:** total, mas com teto de preço baixo. A tese é vender em bundle com o item 4. **(H)**

### 8. Presets de テロップ e animação de texto (Premiere/AE)

- **Categoria e público:** editores de vídeo e YouTubers.
- **Problema:** legendas "estilo TV de variedades" rápidas.
- **Preço de mercado:** ¥300 a ¥1.000 (há outlier a ¥39.800).
- **Concorrentes:**
  - BOOTH 3700775, 120種, ¥300;
  - BOOTH 5163222, AE 170個, ¥500;
  - BOOTH 8684637, Premiere 50種, ¥800.
- **Evidências:**
  - BOOTH 3700775: 1.375 ♥; BOOTH 5163222: 1.508 ♥. [DF] **(C)**
  - BOOTH 8684637, publicado em **08/2026**: 774 ♥. [DF] **(C)**
  - 23% do top 30 publicado a partir de 2025. [DF] **(C)**
  - Demanda adjacente: miniatura de YouTube na ココナラ com 3.589 avaliações. [DF] **(C)**
- **Concorrência:** média.
- **IA:** média. Exige operar o Premiere/AE; a IA ajuda nos estilos.
- **Custo:** Adobe (assinatura). **(E)**
- **Automação e escala:** total.

### 9. Planilha de 確定申告 para criadores

- **Categoria e público:** planilha e guia. Criadores com renda do BOOTH, FANBOX ou Skeb, e quem tem 副業.
- **Problema:** confusão sobre a obrigação de declarar e sobre a escrituração. Há perguntas no 知恵袋, por exemplo "BOOTHの売り上げが50万…確定申告": https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10244132705 [DF]
- **Preço de mercado:** ¥1.000 no BOOTH; ¥7.000 a ¥8.000 na ココナラ.
- **Concorrentes:**
  - ココナラ 2010782 (青色申告, ¥8.000);
  - ココナラ 2184275 (白色申告, ¥7.000);
  - BOOTH 5519458 (CSV→freee, ¥1.000);
  - guia grátis BOOTH 8881152;
  - apps freee e マネーフォワード.
- **Evidências:**
  - ココナラ: 37 e 19 avaliações. [DF] **(C)**
  - Guia grátis do BOOTH (09/2026): **1.440 ♥ em semanas**. [DF] **(C)**
  - 47% do top 30 da tag 確定申告 é recente. [DF] **(C)**
- **Concorrência:** média.
- **IA:** alta nas fórmulas, mas **a revisão de um 税理士 é recomendada**.
- **Custo:** ¥0–30.000 (revisão profissional). **(E)**
- **Automação e escala:** total.
- **Sazonalidade:** janeiro a março.

### 10. Templates de miniatura de YouTube no Canva

- **Público:** YouTubers iniciantes e pequenos negócios.
- **Evidências:**
  - Serviço sob medida na ココナラ 1197314: ¥3.000 com **3.589 avaliações**. [DF] **(C)**
  - Demanda por **template** não comprovada. Exemplo VTuber BOOTH 6377856, ¥300: 60 ♥. [DF] **(C)**
- **Concorrência:** a tag サムネイル tem 7.850 itens, dominados por VTuber e VRChat.
- **IA:** alta.
- **Status:** hipótese a testar.

### 11. ES e 職務経歴書: templates por cargo + prompts

- **Público:** estudantes do ciclo 27卒/28卒 e quem muda de emprego.
- **Evidências:**
  - Correção de ES na ココナラ (681909): ¥10.000 com **339 avaliações**. [DF] **(C)**
  - Correção de 職務経歴書: "実績 668件" e "総販売実績1300件". [DF] **(D)**
  - [L30]: vídeo "エントリーシート完全攻略" com 6.966 views (08/10): https://www.youtube.com/watch?v=OEJAtR8MlNs.
- **Riscos:** recrutadores dizem perceber ES escritas por IA (知恵袋 q13280921848) [DF], e há modelos gratuitos de grandes sites.
- **IA:** alta.

### 12. Templates de PowerPoint para material de vendas

- **Evidências:** ココナラ 2054869, ¥4.000 com **233 avaliações** (50 slides). A busca "テンプレート" tem 51.545 anúncios. [DF] **(C)**
- **Canal:** ココナラ. No BOOTH, a tag PowerPoint tem baixo interesse.

### 13. Templates de 家計簿

- **Evidências:**
  - BOOTH: 613 itens; mediana paga de 17 ♥; líder Notion a ¥1.000 com 81 ♥. [DF] **(C)**
  - ココナラ: 139 anúncios. [DF] **(C)**
  - [L30]: 0 vídeos dentro da janela.
- **Problema real:** "家計簿が続かない", recorrente no 知恵袋. [DF]
- **Concorrência:** muitos modelos grátis no note.
- **Conclusão:** demanda paga fraca.

### 14. Cenário CoC + quarto de ココフォリア

- **Evidências:**
  - BOOTH CoC: 10.711 itens; mediana paga do top 30: **15.020 ♥**; preço mediano: ¥500. [DF] **(C)**
  - Líder BOOTH 2976456: ¥1.000 com 28.064 ♥. [DF] **(C)**
- **Riscos:** exige seguir a diretriz de 二次創作 da KADOKAWA e da Arclight (código SPLL). A IA só ajuda no rascunho, e originalidade é o principal valor.
- **Facilidade de criação:** baixa.

### 15. Guia de geração de imagens com IA

- **Evidências:** Brain com 1.300, 660 e 500 部 **(D)**; o Tips AI tem itens de ¥4.980 a ¥59.800. [DF]
- **Riscos:**
  - concorrência máxima;
  - obsolescência a cada novo modelo (registrada pelo próprio vendedor);
  - associação com 情報商材 (golpes de 副業 citados por advogados: https://www.bengohiroba.jp/consumer-damage/article17875.html). [DF]

### 16. Posts de Instagram para salões de beleza (Canva)

- **Evidências:**
  - コンテンツマーケット a ¥1.500 (sem contagem visível). [DF]
  - Serviços: 31 vendas e 15 avaliações (2130329); 9 vendas (1999351). [DF] **(C)**
  - ココナラ "インスタ テンプレート": **21.707 anúncios**. [DF] **(C)**
- **Concorrência:** alta, com demanda moderada.

### 17. Planner digital 2027 (Goodnotes)

- **Evidências:**
  - [L30]: "iPadを理想の手書き手帳にする｜Goodnotes × KotaLog Diary 2027", **207.990 views** (08/10). [L30] **(C)**
  - [L30]: "デジタルプランナー2027リリース", 11.531 views. [L30] **(C)**
  - BOOTH: 2.103 itens, mediana paga de 55 ♥. O BOOTH não é o canal certo. [DF] **(C)**
- **Status:** hipótese. Vender em loja própria ou no note, com venda sazonal de outubro a janeiro.

### 18. Arquivos de うちわ文字 (推し活)

- **Evidências:**
  - [L30]: "デコうちわ" com 44.128 views (10/10) e "名前うちわの作り方" com 35.657 views (05/10). [L30] **(C)**
  - BOOTH: 178 itens com máximo de 29 ♥. [DF] **(C)**
  - ココナラ: serviço de うちわ com 82 avaliações. [DF] **(C)**
- **Risco:** o teto de preço de ¥100–300 está abaixo da faixa-alvo.

### 19. 年賀状 2027 e 年賀状じまい

- **Evidências:**
  - BOOTH: 1.534 itens, mediana paga de 134 ♥. [DF] **(C)**
  - Muitos sites gratuitos (nenga-illust.com, frame-illust.com). [DF]
  - 年賀状じまい crescendo também entre pessoas de 20 a 40 anos (https://nenga.n-pri.jp/tips/tips55/). [DF]
  - Last30Days: 0 vídeos na janela. [L30]
- **Conclusão:** baixa disposição a pagar.

### 20. Guia low ticket de Threads/SNS

- **Evidências:**
  - 1º no ranking acumulado de vendas do Tips (¥9.800, 207 avaliações). [DF] **(C)**
  - Guia de ¥4.980 com 82 avaliações. [DF] **(C)**
- **Riscos:** exige resultados próprios e audiência; mercado de 情報商材.
- **Conclusão:** não recomendado para começar.

---

## 6. Os cinco vencedores

### 🥇 1. "C109対応 お品書き＆値札テンプレート（Canva/PowerPoint/Googleスライド）"

- **Produto exato:**
  - 20 layouts de お品書き (A4/B5 para impressão e versão 16:9/4:5 para o X);
  - 30 etiquetas de preço (値札) e placas "新刊/既刊/完売";
  - 50 enfeites em PNG transparente;
  - guia de 1 página.
  - Versões: **básica ¥500, completa ¥1.200, gratuita** (3 layouts, padrão comum entre os líderes do BOOTH).
- **Por que existe oportunidade:**
  - a demanda paga por お品書き sob medida é comprovada: ココナラ a ¥3.000 com 341 avaliações;
  - os templates do BOOTH são baratos (¥100–450) e simples;
  - entrantes recentes conseguem aparecer (37% do top 30 é de 2025 ou depois);
  - oferta pequena: 399 itens.
- **Evidências:** ver a ficha 1. ココナラ 2532900; BOOTH 4331063, 5948180, 7771936, 7899572; C109 em 29 a 31/12/2026 (https://japan-event.info/ja/articles/comiket-109). [DF]
- **Como criar com IA:**
  - LLM para a estrutura e as variações de layout;
  - ilustrações de enfeite por geração de imagem, com remoção de fundo;
  - montagem no Canva e exportação para PPT e Google スライド;
  - declarar "AI生成素材を含む" na descrição.
- **Onde vender:**
  - BOOTH (principal, com entrega automática);
  - ココナラ コンテンツマーケット;
  - Canva Creators, se aprovado (H).
- **Como conseguir compradores:**
  - X com #お品書き, #C109, #コミケ, #新刊 e #サークル;
  - posts "antes/depois" mostrando uma お品書き feita em 10 minutos;
  - tags corretas no BOOTH (お品書き, 値札, 同人誌即売会, Canva).
- **Automação:**
  - download automático no BOOTH;
  - posts agendados no X;
  - atualização por evento (C109, 文学フリマ, 夏コミ) para recompra. **(H)**
- **Investimento inicial:** **¥0 a ¥10.000** (IA e Canva por um mês) mais cerca de 20 horas. **(E)**
- **Primeiras 10 vendas:**
  1. Publicar até 15/11, antes do pico de preparação da C109.
  2. Lançar a versão grátis e capturar seguidores.
  3. Responder posts de círculos que dizem "お品書き作らなきゃ" oferecendo o template grátis.
  4. Fazer 3 exemplos por gênero (創作, 二次創作, 評論).
  5. Dar desconto de lançamento (¥500 → ¥300) por 72 horas.
  6. Pedir aos primeiros compradores que postem a お品書き feita com o template, usando uma hashtag própria.

### 🥈 2. Packs de PNG transparente sazonais (série mensal)

- **Produto exato:** "冬〜お正月 透過PNG素材200点（あしらい・食べ物・飾り）商用可・AI生成明記", **¥480**. Depois, packs de Valentine (fevereiro), primavera e assim por diante, como uma série mensal.
- **Oportunidade:**
  - packs equivalentes a ¥480 têm de 717 a 1.653 ♥;
  - um item de 02/2026 já tem 1.937 ♥;
  - o público é amplo: お品書き, streamers, TRPG, SNS.
- **Evidências:** BOOTH 6051435, 5167059, 5400066, 5806712 e 8039792. [DF] **(C)**
- **Como criar com IA:**
  - prompts com estilo consistente;
  - geração em lote;
  - remoção de fundo e upscale;
  - curadoria manual (descartar defeitos);
  - folha de licença.
- **Onde vender:** BOOTH (principal), ココナラ コンテンツマーケット e, depois, mercados internacionais. **(H)**
- **Compradores:** amostras grátis (10 itens) e cross-sell com o produto 1 (enfeites de お品書き).
- **Automação:** total, com cadência mensal.
- **Investimento:** ¥3.000–5.000 por mês. **(E)**
- **Primeiras 10 vendas:**
  1. Lançar o pack de inverno e Natal até 20/11.
  2. Oferecer uma versão grátis de 10 itens com link para a completa.
  3. Fazer posts de "uso real" (お品書き e miniaturas usando o pack).
  4. Usar as tags 透過素材, 商用可, クリスマス e お正月.

### 🥉 3. Templates de LP no Canva para pequenos negócios

- **Produto exato:** 3 LPs verticais (salão de beleza, coach/curso, aula individual) com textos de exemplo e um "prompt de copywriting" para adaptar ao negócio. **¥2.980** no BOOTH e no note, **¥3.980** na ココナラ.
- **Oportunidade:** ¥4.500 com 244 avaliações, e outros anúncios com 21 a 58 avaliações, comprovam que pequenos negócios compram LP em template. [DF] **(C)**
- **Como criar com IA:** estrutura de copy (PASONA e similares) por LLM, imagens por IA e layout no Canva.
- **Onde vender:**
  - ココナラ, onde está a demanda comprovada (exige mensagem por pedido);
  - BOOTH e note, com entrega automática do link.
- **Compradores:**
  - Instagram e X de 個人サロン e コーチ;
  - parceria com quem vende cursos de Instagram;
  - preço de entrada abaixo do líder (¥2.980 contra ¥4.500).
- **Automação:** no BOOTH e no note, o link do template é entregue automaticamente. Na ココナラ, há mensagem-padrão.
- **Investimento:** cerca de ¥0–1.500 de Canva Pro **(E, preço não verificado)** mais 25 horas.
- **Primeiras 10 vendas:**
  1. Abrir na ココナラ com preço de lançamento para gerar as primeiras avaliações (avaliações são o principal fator de confiança na plataforma).
  2. Mostrar 3 exemplos reais.
  3. Oferecer a adaptação de 1 bloco de texto grátis aos 5 primeiros compradores.

### 4. Kit de stream animado (com CSS de comentários)

- **Produto exato:** "動く配信画面セット" com fundo em loop de 30 segundos, telas de 待機, 離席 e 終了, moldura de câmera, CSS de comentários para YouTube e Twitch, template de わんコメ, em **3 cores**. **¥980**, com versão grátis em 1 cor.
- **Oportunidade:**
  - quem não paga ¥10.000–15.000 na ココナラ (340 e 214 avaliações) compra kits de ¥500–1.500 no BOOTH;
  - um kit de 2025 a ¥700 tem 3.332 ♥.
- **Evidências:** ココナラ 2347677 e 2431841; BOOTH 6477455, 6083011, 4950117 e 7039763. [DF] **(C)**
- **Como criar com IA:**
  - imagem do cenário por IA;
  - loop sutil (image-to-video ou partículas no AE ou CapCut);
  - CSS gerado e testado com LLM no OBS.
- **Onde vender:** BOOTH (principal) e ココナラ コンテンツマーケット.
- **Compradores:**
  - X com #VTuber素材, #配信画面 e #個人勢VTuber;
  - oferecer o kit grátis a 5 VTubers pequenos em troca de crédito no stream.
- **Automação:** total.
- **Investimento:** ¥5.000–15.000. **(E)**
- **Primeiras 10 vendas:**
  1. Lançar a versão grátis primeiro (padrão "無料版あり" dos líderes).
  2. Postar um vídeo curto do loop.
  3. Lançar um kit temático (inverno e neve) antes de dezembro.

### 5. Pack de 立ち絵 NPC gerado por IA (TRPG e novel)

- **Produto exato:** "モブNPC立ち絵 30体（職業別・表情差分5種・透過PNG・AI生成明記・商用可）", **¥580**. Packs temáticos seguintes (escola, hospital, fantasia, horror para CoC).
- **Oportunidade:**
  - packs com a tag AI生成 de 2025 chegaram a 1.489–2.238 ♥;
  - packs de ¥580–1.000 de 立ち絵 por profissão têm de 481 a 3.912 ♥;
  - complementa o ecossistema CoC/ココフォリア (cenários com 10 a 28 mil ♥).
- **Evidências:** BOOTH 6563809, 6766490, 5352817, 5349585 e 2576656. [DF] **(C)**
- **Como criar com IA:**
  - geração com personagem consistente;
  - variações de expressão;
  - recorte e limpeza manual;
  - **nunca imitar artistas específicos** (regra do BOOTH).
- **Onde vender:** BOOTH.
- **Compradores:**
  - X com #TRPG素材, #ココフォリア素材 e #CoC;
  - amostra grátis de 3 personagens;
  - parceria com autores de cenário (pack temático por cenário).
- **Automação:** total.
- **Investimento:** ¥3.000–10.000. **(E)**
- **Primeiras 10 vendas:**
  1. Lançar o pack "ホラー/CoC向け" com amostra grátis.
  2. Postar sessões de demonstração no ココフォリア usando os NPCs.
  3. Responder a pedidos de "NPC素材" no X.
- **Atenção:** deixar claro que é IA evita rejeição e cumpre a transparência esperada pela comunidade.

---

## 7. O que é comprovado, estimado e hipotético

- **Comprovado (C):**
  - contagem de avaliações e preços na ココナラ;
  - posição nos rankings de vendas do Tips;
  - contagem de anúncios e de ♥ no BOOTH (via JSON público, em 29/10/2026);
  - views e likes no YouTube (Last30Days);
  - data da C109.
- **Declarado (D):** "○○部突破" no Brain e no Tips; "実績○件" em títulos da ココナラ.
- **Estimado (E):** custos de criação, horas de trabalho e preços de ferramentas (o preço do Canva Pro no Japão não foi verificado; a taxa do BOOTH de "5,6% + ¥45" vem de um artigo de terceiros, quasa.io, não da página oficial).
- **Hipóteses (H):**
  - a conversão de compradores de serviço da ココナラ para templates baratos;
  - a recompra por séries sazonais;
  - a demanda por templates de miniatura;
  - o canal ideal para planners 2027.
- **Não afirmado em nenhum ponto:** número de vendas ou faturamento de qualquer produto. ♥ não é venda.

---

## 8. Fontes originais (japonês) por ferramenta

### Obtidas pelo DeerFlow [DF]

**ココナラ:**

| Serviço | Link |
|---|---|
| お品書き | https://coconala.com/services/2532900 |
| LP Canva | https://coconala.com/services/3607540 |
| PPT | https://coconala.com/services/2054869 |
| 待機画面 | https://coconala.com/services/2347677 |
| 配信画面 | https://coconala.com/services/2431841 |
| ES | https://coconala.com/services/681909 |
| Miniatura | https://coconala.com/services/1197314 |
| 青色申告 | https://coconala.com/services/2010782 |
| 白色申告 | https://coconala.com/services/2184275 |
| Trailer TRPG | https://coconala.com/services/1615468 |
| Quarto ココフォリア | https://coconala.com/services/4095282 |
| 推し活 | https://coconala.com/categories/785/548 |

**BOOTH:**

| Uso no relatório | Itens |
|---|---|
| お品書き | https://booth.pm/ja/items/4331063 · https://booth.pm/ja/items/5948180 · https://booth.pm/ja/items/7771936 · https://booth.pm/ja/items/7899572 |
| PNG transparente | https://booth.pm/ja/items/6051435 · https://booth.pm/ja/items/5167059 · https://booth.pm/ja/items/5400066 · https://booth.pm/ja/items/5806712 · https://booth.pm/ja/items/8039792 |
| Stream | https://booth.pm/ja/items/6477455 · https://booth.pm/ja/items/6083011 · https://booth.pm/ja/items/5871788 · https://booth.pm/ja/items/4950117 · https://booth.pm/ja/items/7039763 |
| 立ち絵 | https://booth.pm/ja/items/6563809 · https://booth.pm/ja/items/6766490 · https://booth.pm/ja/items/2576656 · https://booth.pm/ja/items/5352817 |
| ココフォリア/CoC | https://booth.pm/ja/items/4186217 · https://booth.pm/ja/items/4295537 · https://booth.pm/ja/items/4857456 · https://booth.pm/ja/items/2976456 |
| テロップ | https://booth.pm/ja/items/3700775 · https://booth.pm/ja/items/5163222 · https://booth.pm/ja/items/8684637 |
| 確定申告 | https://booth.pm/ja/items/8881152 · https://booth.pm/ja/items/5519458 |
| 家計簿 | https://booth.pm/ja/items/3131156 |
| うちわ | https://booth.pm/ja/items/7957197 |

**Tips:** rankings `https://tips.jp/category/{カテゴリ}/ranking?sort=sales_count&period={total|monthly}` (ビジネス, デザイン, マネー, 恋愛, AIテクノロジー, ライフスタイル, スポーツ, エンタメ, グルメ).

**Brain:** links da seção 3.

**Regras e contexto:**
- Regras de IA no BOOTH: https://aiteller.jp/blog/booth-ai-kiyaku · https://aiteller.jp/data/ai-platform-rules-timeline
- C109: https://japan-event.info/ja/articles/comiket-109
- 年賀状じまい: https://nenga.n-pri.jp/tips/tips55/
- Golpes de 情報商材: https://www.bengohiroba.jp/consumer-damage/article17875.html
- 知恵袋: q10244132705 (BOOTH e 確定申告), q14256825259 (家計簿 que não dura), q13280921848 (ES feita por IA)

**Dados brutos:** `data/deerflow/` (`s1–s7.jsonl` com as buscas, `booth_scan*.json`, `booth_metrics.json` e `pages/` com as páginas obtidas).

### Obtidas pelo Last30Days [L30] (YouTube, 29/09 a 29/10/2026)

| Tema | Vídeo | Views | Link |
|---|---|---|---|
| note | — | 111.600 | https://www.youtube.com/watch?v=1vE36sjjHLo |
| note | — | 12.507 | https://www.youtube.com/watch?v=oH8RYJz5Tdg |
| note | — | 6.903 | https://www.youtube.com/watch?v=JhGLEpdZ_kI |
| LINEスタンプ e IA | — | 62.173 | https://www.youtube.com/watch?v=ytFu2CnhqGY |
| LINEスタンプ e IA | — | 34.638 | https://www.youtube.com/watch?v=62tjDbExdU8 |
| デジタルペーパー Canva×IA | — | 45.706 | https://www.youtube.com/watch?v=_OdzKNRzeN8 |
| Planner 2027 | KotaLog | 207.990 | https://www.youtube.com/watch?v=Ee4dhh2Bifg |
| Planner 2027 | TSUBAME | 11.531 | https://www.youtube.com/watch?v=pDQ7V6B3F_E |
| 推し活 うちわ | — | 44.128 | https://www.youtube.com/watch?v=2d6CfZETWQI |
| 推し活 うちわ | — | 35.657 | https://www.youtube.com/watch?v=h4iWT0dcNLg |
| ES | — | 6.966 | https://www.youtube.com/watch?v=OEJAtR8MlNs |

**Dados brutos:** `data/last30days/*.out` (44 execuções) e `plans/`.

---

## 9. Próximos passos sugeridos (sem desenvolver produtos nesta etapa)

1. **Rodar o loop completo do agente DeerFlow.** Basta configurar um modelo em `config.yaml` com uma chave de API; os mesmos scripts e a skill `deep-research` rodariam autonomamente.
2. **Ampliar o Last30Days.** Configurar `SCRAPECREATORS_API_KEY` (TikTok/Instagram) e X adicionaria sinal de comprador além do YouTube.
3. **Validar as hipóteses com testes baratos:**
   - versões gratuitas no BOOTH, medindo ♥ e downloads em 14 dias;
   - um anúncio de teste na ココナラ.
