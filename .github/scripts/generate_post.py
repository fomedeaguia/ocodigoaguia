import os, json, urllib.request, urllib.error, urllib.parse, sys, random, re, unicodedata
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
today = now.strftime("%Y-%m-%d")
hour = now.hour
api_key = os.environ["OPENROUTER_API_KEY"]
unsplash_key = os.environ["UNSPLASH_ACCESS_KEY"]
timestamp = now.strftime("%Y-%m-%d-%H")

BLOG_TS_PATH = "src/data/blog.ts"
SITEMAP_PATH = "public/sitemap.xml"
BASE_URL = "https://ocodigoaguia.com.br"

MAX_GENERATION_ATTEMPTS = 15   # Loop 1 — falha na geração da API
MAX_AUDIT_ATTEMPTS      = 15   # Loop 2 — reprovação na auditoria


def slugify(text):
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text[:80]


EBOOK_CTA_FINAL = """

---

## O Ponto de Partida Está Aqui

Tudo que você leu é apenas o começo. **O Código Águia** aprofunda cada um desses princípios com clareza, exemplos reais e um roteiro prático para quem quer mudar de nível de verdade — não amanhã, mas agora. Se a águia está dentro de você, está na hora de libertá-la. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).

---"""

UNSPLASH_QUERIES = {
    "aguia_liberdade":  ["eagle flying sky", "eagle soaring clouds", "bird freedom sky"],
    "prosperidade":     ["success mountain peak", "abundance sunrise", "wealthy mindset"],
    "mentalidade":      ["focus determination sunrise", "mind power meditation", "discipline training"],
    "renovacao":        ["transformation butterfly nature", "renewal dawn light", "rebirth nature"],
    "lideranca":        ["mountain summit leader", "leadership vision horizon", "strong leader"],
    "foco":             ["focus target arrow", "laser focus discipline", "concentration work"],
    "coragem":          ["storm courage sky", "brave challenge mountain", "overcome fear"],
    "visao":            ["aerial view horizon", "wide view landscape", "strategic vision sky"],
    "abundancia":       ["abundance nature light", "golden harvest prosperity", "rich nature golden"],
    "transformacao":    ["light growth forest", "personal growth sunrise", "change transformation"],
    "liberdade":        ["open road freedom sky", "lone traveler horizon", "wide open landscape"],
    "disciplina":       ["discipline training focus", "early morning run", "athlete discipline"],
    "identidade":       ["reflection mirror light", "self discovery nature", "identity journey"],
    "silencio":         ["calm lake reflection", "quiet forest fog", "silence nature solitude"],
    "ambiente":         ["environment influence nature", "urban crowd contrast", "peaceful forest path"],
    "proposito":        ["compass direction path", "purpose journey road", "mission clarity light"],
    "fracasso":         ["storm resilience comeback", "broken chains freedom", "rising after fall"],
    "decisoes":         ["crossroads path decision", "choice direction road", "strategic thinking"],
    "atencao":          ["focus lens sharp", "target precision aim", "selective attention light"],
    "tempo":            ["hourglass time light", "sunrise long exposure", "time passing nature"],
}
DEFAULT_UNSPLASH_QUERIES = ["eagle sky freedom", "eagle soaring", "mountain eagle sunrise"]


def buscar_imagem_unsplash(image_key):
    queries = UNSPLASH_QUERIES.get(image_key, []) + DEFAULT_UNSPLASH_QUERIES
    for query in queries:
        try:
            url = (
                f"https://api.unsplash.com/photos/random"
                f"?query={urllib.parse.quote(query)}"
                f"&orientation=landscape"
                f"&content_filter=high"
            )
            req = urllib.request.Request(
                url,
                headers={
                    "Authorization": f"Client-ID {unsplash_key}",
                    "Accept-Version": "v1",
                },
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                img_url = data["urls"]["regular"]
                if "?" in img_url:
                    img_url = img_url.split("?")[0] + "?w=1200&q=85&fit=crop&auto=format"
                else:
                    img_url = img_url + "?w=1200&q=85&fit=crop&auto=format"
                photographer = data.get("user", {}).get("name", "Unsplash")
                photo_id = data.get("id", "")
                print(f"Unsplash OK [{query}]: {photographer} — {photo_id}")
                return img_url
        except Exception as e:
            print(f"Unsplash falhou [{query}]: {e}")
            continue
    seed = abs(hash(timestamp)) % 9999
    fallback = f"https://source.unsplash.com/1200x630/?eagle&sig={seed}"
    print(f"Unsplash source fallback: {fallback}")
    return fallback


# ──────────────────────────────────────────────────────────────────────────────
# TEMAS E ÂNGULOS
# ──────────────────────────────────────────────────────────────────────────────

TEMAS_MANHA = [
    ("visao",          "visão de longo prazo"),
    ("prosperidade",   "prosperidade e mentalidade financeira"),
    ("abundancia",     "consciência de abundância"),
    ("foco",           "foco e proteção da atenção"),
    ("disciplina",     "disciplina como base da transformação"),
    ("proposito",      "propósito e direção de vida"),
    ("objetivos",      "transformar desejos vagos em objetivos concretos"),
    ("tempo",          "gestão do tempo e visão de futuro"),
]

TEMAS_TARDE = [
    ("coragem",        "coragem para agir apesar do medo"),
    ("lideranca",      "liderança e responsabilidade pelas próprias escolhas"),
    ("transformacao",  "transformação pessoal e mudança de nível"),
    ("renovacao",      "renovação e abandono de versões antigas de si"),
    ("decisoes",       "tomada de decisão com clareza"),
    ("fracasso",       "resiliência e recomeço após fracasso"),
    ("disciplina",     "disciplina quando a motivação desaparece"),
    ("identidade",     "tornar-se alguém capaz de sustentar uma nova realidade"),
]

TEMAS_NOITE = [
    ("mentalidade",    "mentalidade de águia versus mentalidade de galinha"),
    ("aguia_liberdade","psicologia dos arquétipos e o símbolo da águia"),
    ("liberdade",      "liberdade como responsabilidade e autonomia de escolha"),
    ("silencio",       "o poder do silêncio e do afastamento do ruído"),
    ("identidade",     "autoconhecimento e construção de identidade"),
    ("ambiente",       "como o ambiente e as pessoas influenciam decisões"),
    ("atencao",        "atenção como recurso mais valioso da vida"),
    ("aprovacao",      "dependência de aprovação social e autenticidade"),
]

ANGULOS = [
    "Águia como proteção da mente — mostrar como proteger atenção, pensamentos e objetivos contra influências externas.",
    "Águia como visão de longo prazo — mostrar como decisões presentes constroem ou destroem o futuro.",
    "Águia como liberdade — explorar a relação entre autonomia, responsabilidade e capacidade de escolher.",
    "Águia contra o imediatismo — contrastar visão de longo prazo com a necessidade constante de recompensas rápidas.",
    "Águia e disciplina — mostrar que visão sem ação não produz transformação.",
    "Águia e silêncio — explorar como afastar-se temporariamente do ruído pode aumentar clareza.",
    "Águia e ambiente — mostrar como aquilo que cerca uma pessoa influencia sua mentalidade e suas decisões.",
    "Águia e identidade — explorar a diferença entre querer uma vida diferente e tornar-se alguém capaz de construí-la.",
    "Águia e aprovação — mostrar como depender da validação externa impede decisões autênticas.",
    "Águia e coragem — explorar o momento em que uma pessoa precisa agir apesar do medo.",
    "Águia e objetivos — mostrar como liberdade sem direção pode se transformar em dispersão.",
    "Águia e recomeço — explorar quando abandonar uma versão antiga de si é necessário para avançar.",
    "Águia e adversidade — mostrar como dificuldades podem mudar a perspectiva e fortalecer decisões.",
    "Águia e atenção — explorar a atenção como um dos recursos mais valiosos da vida.",
    "Águia e escolhas — mostrar que cada escolha aproxima ou distancia da vida que se deseja construir.",
    "Águia e tempo — explorar a diferença entre viver reagindo ao presente e construir pensando no futuro.",
    "Águia e comparação — mostrar como comparar constantemente a própria trajetória com a dos outros destrói foco.",
    "Águia e excesso de informação — explorar como consumir informação demais produz confusão em vez de conhecimento.",
    "Águia e crescimento — mostrar que crescimento exige desconforto, mudança de comportamento e expansão de perspectiva.",
]

if hour < 12:
    pool = TEMAS_MANHA
    period = "manha"
    sensacao = "Eu posso enxergar minha vida de uma maneira diferente e começar a construir algo maior."
elif hour < 19:
    pool = TEMAS_TARDE
    period = "tarde"
    sensacao = "Eu preciso parar de esperar e começar a agir."
else:
    pool = TEMAS_NOITE
    period = "noite"
    sensacao = "Talvez eu esteja vivendo uma vida que nunca parei para questionar."

image_key, tema_desc = random.choice(pool)
angulo = random.choice(ANGULOS)

category_map = {
    "manha": ["Mentalidade de Águia", "Prosperidade", "Visão e Propósito"],
    "tarde": ["Transformação", "Coragem e Ação", "Liderança"],
    "noite": ["Filosofia", "Autoconhecimento", "Liberdade e Identidade"],
}
category = random.choice(category_map[period])

tags_map = {
    "aguia_liberdade":  ["arquétipo da águia", "liberdade", "simbolismo"],
    "prosperidade":     ["prosperidade", "abundância", "mentalidade financeira"],
    "mentalidade":      ["mentalidade de águia", "alto desempenho", "crescimento pessoal"],
    "renovacao":        ["renovação", "transformação", "recomeço"],
    "lideranca":        ["liderança", "responsabilidade", "visão estratégica"],
    "foco":             ["foco", "disciplina", "proteção da atenção"],
    "coragem":          ["coragem", "resiliência", "superação"],
    "visao":            ["visão", "estratégia", "longo prazo"],
    "abundancia":       ["abundância", "consciência financeira", "prosperidade"],
    "transformacao":    ["transformação", "mudança de nível", "desenvolvimento pessoal"],
    "liberdade":        ["liberdade", "autonomia", "escolhas"],
    "disciplina":       ["disciplina", "constância", "resultados"],
    "identidade":       ["identidade", "autoconhecimento", "propósito"],
    "silencio":         ["silêncio", "clareza mental", "foco"],
    "ambiente":         ["ambiente", "influências", "mentalidade"],
    "proposito":        ["propósito", "direção de vida", "clareza"],
    "fracasso":         ["resiliência", "recomeço", "superação"],
    "decisoes":         ["decisões", "clareza", "estratégia"],
    "atencao":          ["atenção", "foco", "presença"],
    "tempo":            ["tempo", "visão de futuro", "disciplina"],
    "aprovacao":        ["aprovação social", "autenticidade", "liberdade"],
}
tags = tags_map.get(image_key, ["mentalidade de águia", "transformação", "desenvolvimento pessoal"])

use_cta = random.random() < 0.5


# ──────────────────────────────────────────────────────────────────────────────
# AUDITORIA DE QUALIDADE E SEO
# Retorna dict com 'aprovado' (bool) e 'erros' (list[str])
# ──────────────────────────────────────────────────────────────────────────────

def auditar_post(title, excerpt, slug, content_md):
    erros = []
    avisos = []

    # ── SEO ──────────────────────────────────────────────────────────────────

    if not title or len(title) < 10:
        erros.append(f"SEO: título ausente ou muito curto ({len(title)} chars; mínimo 10)")
    elif len(title) > 70:
        erros.append(f"SEO: título muito longo ({len(title)} chars; máximo 70)")

    if not excerpt or len(excerpt) < 50:
        erros.append(f"SEO: resumo ausente ou muito curto ({len(excerpt)} chars; mínimo 50)")
    elif len(excerpt) > 165:
        erros.append(f"SEO: resumo muito longo ({len(excerpt)} chars; máximo 165)")

    if not slug or not re.match(r'^[a-z0-9-]+$', slug):
        erros.append(f"SEO: slug inválido '{slug}' (apenas letras minúsculas, números e hífens)")

    h1_count = len(re.findall(r'^# .+', content_md, re.MULTILINE))
    if h1_count != 0:
        erros.append(f"SEO: o corpo do artigo não deve conter H1 (encontrado {h1_count}); o título é o H1")

    h2_count = len(re.findall(r'^## .+', content_md, re.MULTILINE))
    if h2_count < 4:
        erros.append(f"SEO: poucos subtítulos H2 ({h2_count}; mínimo 4)")

    if re.search(r'^### ', content_md, re.MULTILINE):
        erros.append("SEO: uso de H3 (###) não permitido neste blog; use somente H2 (##)")

    if re.search(r'^#### ', content_md, re.MULTILINE):
        erros.append("SEO: uso de H4 (####) não permitido; use somente H2 (##)")

    keyword_lower = title.lower()
    first_paragraph = " ".join(content_md.split("\n")[:8]).lower()
    if not any(word in first_paragraph for word in keyword_lower.split()[:3]):
        avisos.append("SEO: tema principal não detectado nos primeiros parágrafos")

    # ── QUALIDADE DO TEXTO ───────────────────────────────────────────────────

    word_count = len(content_md.split())
    if word_count < 1000:
        erros.append(f"QUALIDADE: artigo muito curto ({word_count} palavras; mínimo 1.300)")

    if re.search(r'\[INSERIR\]|\[TODO\]|\[texto aqui\]|\[PLACEHOLDER\]', content_md, re.IGNORECASE):
        erros.append("QUALIDADE: texto contém placeholders não substituídos")

    if not re.search(r'^## ', content_md, re.MULTILINE):
        erros.append("QUALIDADE: nenhuma seção com subtítulo H2 encontrada")

    paragraphs = [p.strip() for p in re.split(r'\n{2,}', content_md) if p.strip() and not p.strip().startswith('#')]
    long_paragraphs = [p[:80] for p in paragraphs if len(p.split()) > 200]
    if long_paragraphs:
        erros.append(f"QUALIDADE: {len(long_paragraphs)} parágrafo(s) com mais de 200 palavras — quebre em blocos menores")

    sentences = re.split(r'(?<=[.!?])\s+', content_md)
    sentence_texts = [s.strip().lower()[:80] for s in sentences if len(s.strip()) > 40]
    if len(sentence_texts) != len(set(sentence_texts)):
        erros.append("QUALIDADE: frases duplicadas detectadas no artigo")

    cta_patterns = [
        r'conheça o código águia', r'acesse o site', r'clique aqui para comprar',
        r'compre agora', r'<!--CTA_FINAL-->', r'quero acessar'
    ]
    for pat in cta_patterns:
        if re.search(pat, content_md, re.IGNORECASE):
            erros.append(f"QUALIDADE: CTA comercial no corpo do artigo ('{pat}') — não permitido")
            break

    # ── FORMATAÇÃO ───────────────────────────────────────────────────────────

    bullet_count = len(re.findall(r'^[\*\-] .+', content_md, re.MULTILINE))
    if bullet_count > 0:
        erros.append(f"FORMATAÇÃO: uso de bullet points ({bullet_count} encontrados) — não permitido neste blog")

    empty_heading = re.search(r'^## .+\n+(## |\Z)', content_md, re.MULTILINE)
    if empty_heading:
        erros.append("FORMATAÇÃO: subtítulo H2 sem conteúdo logo abaixo")

    lines = content_md.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("## ") and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line == "" and i + 2 < len(lines) and lines[i + 2].strip().startswith("##"):
                erros.append(f"FORMATAÇÃO: H2 seguido imediatamente de outro H2 sem texto entre eles (linha {i+1})")
                break

    if re.search(r'\*\*\*|___', content_md):
        avisos.append("FORMATAÇÃO: uso de negrito+itálico combinado (***) — prefira apenas **negrito**")

    aprovado = len(erros) == 0
    score = max(0, 100 - len(erros) * 12 - len(avisos) * 3)

    return {
        "aprovado": aprovado,
        "score": score,
        "erros": erros,
        "avisos": avisos,
        "palavras": word_count,
        "h2_count": h2_count,
    }


# ──────────────────────────────────────────────────────────────────────────────
# PROMPT MESTRE
# ──────────────────────────────────────────────────────────────────────────────

def montar_prompt(tema_desc, angulo, sensacao, tentativa_auditoria=1, erros_anteriores=None):
    correcoes_bloco = ""
    if erros_anteriores:
        lista_erros = "\n".join(f"- {e}" for e in erros_anteriores)
        correcoes_bloco = f"""
---

## ATENÇÃO — CORREÇÕES OBRIGATÓRIAS (tentativa {tentativa_auditoria}/15)

O texto anterior foi REPROVADO na auditoria automática pelos seguintes motivos:

{lista_erros}

Você DEVE corrigir TODOS esses problemas no novo texto.
Não repita os erros anteriores. Reescreva o artigo do zero com essas correções.

---
"""

    return f"""# Prompt Mestre — Gerador de Artigos | O Código Águia

Você é um **redator especializado em desenvolvimento pessoal, mentalidade, comportamento, disciplina, liberdade, propósito e transformação pessoal**, escrevendo EXCLUSIVAMENTE em português do Brasil.

Sua missão é produzir artigos profundos, envolventes, humanos e emocionalmente inteligentes sobre a **Mentalidade de Águia**, utilizando a águia como um arquétipo narrativo para explorar visão, clareza, força mental, independência, disciplina, coragem, liberdade, objetivos e transformação pessoal.

ATENÇÃO: Responda APENAS com o artigo finalizado. Não explique o processo. Não informe o tema ou ângulo escolhido. Não escreva observações antes ou depois. Não escreva CTA. O texto deve estar pronto para publicação diretamente no site.
{correcoes_bloco}
---

TEMA DO ARTIGO: {tema_desc}

ÂNGULO NARRATIVO: {angulo}

SENSAÇÃO QUE O LEITOR DEVE SENTIR AO TERMINAR: "{sensacao}"

---

## 1. CONCEITO CENTRAL — A MENTALIDADE DE ÁGUIA

A **Mentalidade de Águia** é o conceito central de todo o projeto.

A águia deve ser utilizada como **metáfora, símbolo e arquétipo**, e não como justificativa científica.

Os artigos podem explorar: **visão, altitude mental, foco, disciplina, coragem, independência, liberdade, silêncio, estratégia, proteção da mente, seleção de ambientes, objetivos, resiliência, renovação, propósito e responsabilidade pelas próprias escolhas.**

---

## 2. ESTRUTURA NARRATIVA

Construa o artigo com progressão lógica:

**GANCHO → PROBLEMA → IDENTIFICAÇÃO → METÁFORA DA ÁGUIA → APROFUNDAMENTO → NOVA PERSPECTIVA → APLICAÇÃO NA VIDA → TRANSFORMAÇÃO → CONCLUSÃO.**

---

## 3. REGRAS OBRIGATÓRIAS DE FORMATAÇÃO

- Mínimo de **1.300 palavras** (ideal: 1.400+)
- Mínimo de **4 seções principais** com títulos usando `##`
- **NUNCA use `###`, `####` ou qualquer heading abaixo de `##`**
- **ZERO bullet points** — use parágrafos corridos
- **ZERO H1 no corpo** — o título já é o H1; o corpo começa direto com `##`
- Parágrafos com no máximo 150 palavras cada
- Uso estratégico de **negrito**
- Introdução forte no início
- Conclusão memorável no final
- Português do Brasil

---

## 4. REGRA ABSOLUTA SOBRE CTA

**NÃO ESCREVA CTA NO ARTIGO.**
**NÃO ESCREVA CHAMADA PARA COMPRA.**
**NÃO ESCREVA LINK COMERCIAL.**
**NÃO ESCREVA "CONHEÇA O CÓDIGO ÁGUIA".**

O texto deve terminar na conclusão editorial. CTA será inserido por sistema externo.

---

## 5. ESTILO

Texto: **profundo, humano, elegante, provocador, emocional, claro e natural.**

Evite: clichês, frases motivacionais vazias, exageros, promessas de transformação instantânea, linguagem corporativa, repetição, excesso de exclamações, linguagem típica de IA.

Não comece o texto com aberturas genéricas como:
- "Nos dias de hoje..."
- "Todos nós sabemos que..."
- "Você já parou para pensar..."

---

## 6. FORMATO DE SAÍDA

Entregue somente o artigo. Sem texto adicional antes ou depois.

Linha 1: # Título do Artigo (título com até 70 caracteres)
Linha 2: RESUMO: resumo com entre 80 e 160 caracteres
Linha 3 em diante: o artigo completo (corpo sem nenhum H1)
"""


# ──────────────────────────────────────────────────────────────────────────────
# FUNÇÃO DE CHAMADA À API (Loop 1 — até 15 tentativas de geração)
# ──────────────────────────────────────────────────────────────────────────────

def chamar_api(prompt_text, tentativa_geracao):
    print(f"\n── Loop 1 | Tentativa de geração {tentativa_geracao}/{MAX_GENERATION_ATTEMPTS} ──")
    payload = json.dumps({
        "model": "openrouter/auto",
        "messages": [{"role": "user", "content": prompt_text}],
        "temperature": 0.8,
        "max_tokens": 6000
    }).encode()

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://ocodigoaguia.com.br",
            "X-Title": "O Codigo Aguia Blog"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
            text = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            model_used = data.get("model", "desconhecido")
            print(f"Modelo: {model_used} | Chars: {len(text)}")
            return text
    except Exception as e:
        print(f"Erro na API (tentativa {tentativa_geracao}): {e}")
        return None


# ──────────────────────────────────────────────────────────────────────────────
# FUNÇÃO DE PARSING DO TEXTO GERADO
# ──────────────────────────────────────────────────────────────────────────────

def parsear_artigo(article_text):
    lines = article_text.strip().splitlines()
    title = ""
    excerpt = ""
    content_lines = []

    for line in lines:
        stripped = line.strip()
        if not title and stripped.startswith("# "):
            title = stripped[2:].strip()
            continue
        if not excerpt and stripped.startswith("RESUMO:"):
            excerpt = stripped[7:].strip()
            continue
        content_lines.append(line)

    content_md = "\n".join(content_lines).strip()

    if not title:
        for line in content_lines:
            if line.strip().startswith("## "):
                title = line.strip()[3:].strip()
                break
    if not title:
        title = f"A Mentalidade de Águia — {today}"

    if not excerpt:
        for line in content_lines:
            clean = line.strip()
            if len(clean) > 80 and not clean.startswith("#"):
                excerpt = re.sub(r"\*\*|\[.*?\]\(.*?\)", "", clean)[:200].strip()
                break

    return title, excerpt, content_md


# ──────────────────────────────────────────────────────────────────────────────
# LOOP DUPLO — Loop 1: geração | Loop 2: auditoria
# ──────────────────────────────────────────────────────────────────────────────

print(f"\n{'='*60}")
print(f"INICIANDO GERAÇÃO DE POST | {timestamp}")
print(f"Tema: {tema_desc} | Período: {period}")
print(f"{'='*60}")

article_text_final = None
title_final = ""
excerpt_final = ""
content_md_final = ""
slug_final = ""
audit_result = None

# ── LOOP 2: auditoria (externo) ───────────────────────────────────────────────
for tentativa_auditoria in range(1, MAX_AUDIT_ATTEMPTS + 1):
    print(f"\n{'─'*50}")
    print(f"LOOP 2 | Ciclo de auditoria {tentativa_auditoria}/{MAX_AUDIT_ATTEMPTS}")
    print(f"{'─'*50}")

    erros_auditoria_anterior = audit_result["erros"] if audit_result else None
    prompt_atual = montar_prompt(
        tema_desc, angulo, sensacao,
        tentativa_auditoria=tentativa_auditoria,
        erros_anteriores=erros_auditoria_anterior
    )

    # ── LOOP 1: geração (interno) ─────────────────────────────────────────────
    article_text_raw = None
    for tentativa_geracao in range(1, MAX_GENERATION_ATTEMPTS + 1):
        raw = chamar_api(prompt_atual, tentativa_geracao)

        if raw and len(raw) >= 500:
            article_text_raw = raw
            print(f"✓ Geração bem-sucedida na tentativa {tentativa_geracao}")
            break
        else:
            chars = len(raw) if raw else 0
            print(f"✗ Tentativa {tentativa_geracao} falhou (resposta: {chars} chars). Retentando...")

    if not article_text_raw:
        print(f"\n✗ LOOP 1 ESGOTADO: não foi possível gerar texto após {MAX_GENERATION_ATTEMPTS} tentativas.")
        print("Abortando execução.")
        sys.exit(1)

    # Parseia o texto gerado
    title_final, excerpt_final, content_md_final = parsear_artigo(article_text_raw)
    slug_final = slugify(title_final)
    if not slug_final:
        slug_final = f"post-{timestamp}"

    print(f"\nTexto gerado:")
    print(f"  Título  : {title_final}")
    print(f"  Slug    : {slug_final}")
    print(f"  Resumo  : {excerpt_final[:80]}...")
    print(f"  Palavras: {len(content_md_final.split())}")

    # ── AUDITORIA ─────────────────────────────────────────────────────────────
    audit_result = auditar_post(title_final, excerpt_final, slug_final, content_md_final)

    print(f"\n{'─'*40}")
    print(f"RESULTADO DA AUDITORIA — ciclo {tentativa_auditoria}")
    print(f"  Score   : {audit_result['score']}/100")
    print(f"  Palavras: {audit_result['palavras']}")
    print(f"  H2      : {audit_result['h2_count']}")
    print(f"  Status  : {'✓ APROVADO' if audit_result['aprovado'] else '✗ REPROVADO'}")

    if audit_result["erros"]:
        print(f"  Erros ({len(audit_result['erros'])}):")
        for e in audit_result["erros"]:
            print(f"    ✗ {e}")

    if audit_result["avisos"]:
        print(f"  Avisos ({len(audit_result['avisos'])}):")
        for a in audit_result["avisos"]:
            print(f"    ⚠ {a}")

    if audit_result["aprovado"]:
        print(f"\n✓ AUDITORIA APROVADA no ciclo {tentativa_auditoria}/{MAX_AUDIT_ATTEMPTS}")
        article_text_final = article_text_raw
        break
    else:
        if tentativa_auditoria < MAX_AUDIT_ATTEMPTS:
            print(f"\n✗ Texto reprovado. Descartando e recriando do zero (próximo ciclo: {tentativa_auditoria + 1})...")
        else:
            print(f"\n✗ LOOP 2 ESGOTADO: texto reprovado em todos os {MAX_AUDIT_ATTEMPTS} ciclos de auditoria.")
            print("Abortando execução sem publicar.")
            sys.exit(1)

# Verificação final de segurança
if not article_text_final or not audit_result or not audit_result["aprovado"]:
    print("Erro interno: texto não aprovado chegou à fase de publicação. Abortando.")
    sys.exit(1)

# ──────────────────────────────────────────────────────────────────────────────
# INSERÇÃO DO CTA (opcional, 50% de chance) — só após aprovação
# ──────────────────────────────────────────────────────────────────────────────

if use_cta:
    content_md_final = content_md_final.rstrip() + "\n" + EBOOK_CTA_FINAL
    print("CTA final inserido no artigo.")

reading_time = max(1, round(len(content_md_final.split()) / 200))

print(f"\n{'='*60}")
print(f"POST APROVADO — Publicando...")
print(f"  Título  : {title_final}")
print(f"  Slug    : {slug_final}")
print(f"  Leitura : {reading_time} min")
print(f"  Score   : {audit_result['score']}/100")
print(f"{'='*60}")

# ──────────────────────────────────────────────────────────────────────────────
# IMAGEM DE CAPA
# ──────────────────────────────────────────────────────────────────────────────

print(f"Buscando imagem Unsplash para: {image_key}")
cover_image = buscar_imagem_unsplash(image_key)

# ──────────────────────────────────────────────────────────────────────────────
# INJETAR O POST EM src/data/blog.ts
# ──────────────────────────────────────────────────────────────────────────────

def escape_backtick(s):
    s = s.replace("\\", "\\\\")
    s = s.replace("`", "\\`")
    s = s.replace("${", "\\${")
    return s

def ts_string(s):
    return "`" + escape_backtick(s) + "`"

def ts_string_simple(s):
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + s + '"'

def ts_array(lst):
    items = ", ".join(ts_string_simple(x) for x in lst)
    return f"[{items}]"

new_post_block = f"""  {{
    id: {ts_string_simple(slug_final)},
    slug: {ts_string_simple(slug_final)},
    title: {ts_string_simple(title_final)},
    excerpt: {ts_string_simple(excerpt_final[:300])},
    date: {ts_string_simple(today)},
    readingTime: {reading_time},
    category: {ts_string_simple(category)},
    coverImage: {ts_string_simple(cover_image)},
    tags: {ts_array(tags)},
    featured: false,
    content: {ts_string(content_md_final)},
  }},"""

with open(BLOG_TS_PATH, "r", encoding="utf-8") as f:
    blog_ts = f.read()

if f'slug: "{slug_final}"' in blog_ts or f"slug: '{slug_final}'" in blog_ts:
    print(f"Slug '{slug_final}' já existe em blog.ts. Abortando para evitar duplicata.")
    sys.exit(0)

ARRAY_OPEN_MARKER = "const staticPosts: BlogPost[] = ["
insert_pos = blog_ts.find(ARRAY_OPEN_MARKER)

if insert_pos == -1:
    print("ERRO: Não encontrou 'const staticPosts: BlogPost[] = [' em blog.ts")
    sys.exit(1)

after_bracket = insert_pos + len(ARRAY_OPEN_MARKER)
updated_ts = blog_ts[:after_bracket] + "\n" + new_post_block + "\n" + blog_ts[after_bracket:]

with open(BLOG_TS_PATH, "w", encoding="utf-8") as f:
    f.write(updated_ts)

print(f"Post injetado NO TOPO de {BLOG_TS_PATH}")
print(f"Slug: {slug_final} | Leitura: {reading_time} min | {len(content_md_final.split())} palavras")
print(f"Imagem: {cover_image[:100]}")

# ──────────────────────────────────────────────────────────────────────────────
# ATUALIZAR public/sitemap.xml
# ──────────────────────────────────────────────────────────────────────────────

post_url = f"{BASE_URL}/blog/{slug_final}"

new_url_entry = f"""  <url>
    <loc>{post_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""

try:
    with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
        sitemap_content = f.read()

    if post_url in sitemap_content:
        print(f"URL '{post_url}' já existe no sitemap. Nenhuma alteração feita.")
    else:
        blog_entry_marker = f"<loc>{BASE_URL}/blog</loc>"
        blog_entry_pos = sitemap_content.find(blog_entry_marker)

        if blog_entry_pos != -1:
            close_tag_pos = sitemap_content.find("</url>", blog_entry_pos)
            if close_tag_pos != -1:
                insert_after = close_tag_pos + len("</url>")
                updated_sitemap = (
                    sitemap_content[:insert_after]
                    + "\n"
                    + new_url_entry
                    + sitemap_content[insert_after:]
                )
            else:
                updated_sitemap = sitemap_content.replace(
                    "</urlset>", new_url_entry + "\n</urlset>"
                )
        else:
            updated_sitemap = sitemap_content.replace(
                "</urlset>", new_url_entry + "\n</urlset>"
            )

        with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
            f.write(updated_sitemap)

        print(f"Sitemap atualizado: {post_url} adicionado em {SITEMAP_PATH}")

except FileNotFoundError:
    print(f"AVISO: {SITEMAP_PATH} não encontrado. Sitemap não atualizado.")
except Exception as e:
    print(f"AVISO: Erro ao atualizar sitemap: {e}. Post foi gerado normalmente.")
