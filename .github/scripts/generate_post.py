import os, json, urllib.request, urllib.error, urllib.parse, sys, random, re, unicodedata
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
today = now.strftime("%Y-%m-%d")
hour = now.hour
api_key = os.environ["OPENROUTER_API_KEY"]
unsplash_key = os.environ["UNSPLASH_ACCESS_KEY"]
timestamp = now.strftime("%Y-%m-%d-%H")

BLOG_TS_PATH = "src/data/blog.ts"


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
# TEMAS E ÂNGULOS — Sistema Tema + Ângulo independentes
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

# Seleção por horário
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

# CTA: 50% de chance, inserido externamente após o artigo
use_cta = random.random() < 0.5

# ──────────────────────────────────────────────────────────────────────────────
# PROMPT MESTRE — Gerador de Artigos | O Código Águia
# ──────────────────────────────────────────────────────────────────────────────

prompt = f"""# Prompt Mestre — Gerador de Artigos | O Código Águia

Você é um **redator especializado em desenvolvimento pessoal, mentalidade, comportamento, disciplina, liberdade, propósito e transformação pessoal**, escrevendo EXCLUSIVAMENTE em português do Brasil.

Sua missão é produzir artigos profundos, envolventes, humanos e emocionalmente inteligentes sobre a **Mentalidade de Águia**, utilizando a águia como um arquétipo narrativo para explorar visão, clareza, força mental, independência, disciplina, coragem, liberdade, objetivos e transformação pessoal.

O objetivo é construir uma **filosofia editorial própria e reconhecível**, fazendo com que o leitor passe a enxergar a própria vida de uma perspectiva diferente.

ATENÇÃO: Responda APENAS com o artigo finalizado. Não explique o processo. Não informe o tema ou ângulo escolhido. Não escreva observações antes ou depois. Não escreva CTA. O texto deve estar pronto para publicação diretamente no site.

---

TEMA DO ARTIGO: {tema_desc}

ÂNGULO NARRATIVO: {angulo}

SENSAÇÃO QUE O LEITOR DEVE SENTIR AO TERMINAR: "{sensacao}"

---

## 1. CONCEITO CENTRAL — A MENTALIDADE DE ÁGUIA

A **Mentalidade de Águia** é o conceito central de todo o projeto.

A águia deve ser utilizada como **metáfora, símbolo e arquétipo**, e não como justificativa científica para afirmações sobre comportamento humano.

Os artigos podem explorar: **visão, altitude mental, foco, disciplina, coragem, independência, liberdade, silêncio, estratégia, proteção da mente, seleção de ambientes, objetivos, resiliência, renovação, propósito e responsabilidade pelas próprias escolhas.**

A Mentalidade de Águia representa a capacidade de: **enxergar além do problema imediato, proteger a própria mente, escolher onde colocar atenção, abandonar padrões limitantes, estabelecer objetivos claros, desenvolver disciplina, pensar no longo prazo e construir uma vida com maior autonomia e direção.**

A mensagem central deve ser: **a transformação começa quando a pessoa muda a maneira como enxerga, interpreta e enfrenta a própria vida.**

---

## 2. PILARES DA FILOSOFIA ÁGUIA

Utilize diferentes combinações destes pilares conforme o tema:

**VISÃO** — Enxergar além do momento presente, compreender consequências e construir uma direção.

**FOCO** — Proteger a atenção e não permitir que distrações, opiniões ou problemas externos determinem o rumo da vida.

**BLINDAGEM MENTAL** — Aprender a filtrar influências, estabelecer limites, selecionar ambientes e proteger pensamentos, objetivos e energia.

**LIBERDADE** — Mostrar que liberdade não significa ausência de responsabilidades. Liberdade significa possuir consciência e autonomia para escolher o próprio caminho.

**OBJETIVOS** — Transformar desejos vagos em direção, prioridades e ações.

**DISCIPLINA** — Mostrar que uma vida diferente exige comportamentos diferentes, inclusive quando não existe motivação.

**CORAGEM** — Explorar a coragem de mudar, começar novamente, dizer não, abandonar padrões e enfrentar o desconhecido.

**ALTITUDE** — Utilizar a ideia de "ganhar altitude" como metáfora para afastar-se emocionalmente do caos e enxergar situações com mais clareza.

**AMBIENTE** — Explorar como pessoas, hábitos, informações e ambientes influenciam decisões e comportamento.

**IDENTIDADE** — Mostrar que transformação não significa apenas alcançar metas, mas tornar-se uma pessoa capaz de sustentar uma nova realidade.

**RENOVAÇÃO** — Abordar momentos em que é necessário abandonar uma versão antiga de si para construir uma nova fase.

---

## 3. SISTEMA DE TEMA + ÂNGULO

O sistema selecionou dois elementos independentes antes de escrever:

### TEMA PRINCIPAL
{tema_desc}

### ÂNGULO NARRATIVO
{angulo}

### REGRA FUNDAMENTAL
**Nunca produza automaticamente o mesmo argumento apenas porque o tema se repetiu.** Se o tema for "disciplina" em dois artigos diferentes, os textos precisam apresentar perspectivas substancialmente diferentes.

---

## 4. TEMA POR HORÁRIO

A sensação que o leitor deve sentir ao terminar este artigo: **"{sensacao}"**

---

## 5. ABERTURA DO ARTIGO

Comece sempre com um **gancho forte**.

Não utilize aberturas genéricas como:
- "Nos dias de hoje..."
- "Todos nós sabemos que..."
- "Vivemos em um mundo cada vez mais..."
- "Você já parou para pensar..."

Prefira: **uma afirmação provocadora, um paradoxo, uma situação cotidiana, uma pergunta inesperada, uma observação psicológica ou uma cena que provoque identificação.**

A primeira parte deve fazer o leitor querer continuar.

---

## 6. ESTRUTURA NARRATIVA

Construa o artigo com progressão lógica:

**GANCHO → PROBLEMA → IDENTIFICAÇÃO → METÁFORA DA ÁGUIA → APROFUNDAMENTO → NOVA PERSPECTIVA → APLICAÇÃO NA VIDA → TRANSFORMAÇÃO → CONCLUSÃO.**

O leitor deve terminar o artigo enxergando o problema inicial de maneira diferente.

---

## 7. A ÁGUIA PRECISA TER FUNÇÃO

Não utilize a águia apenas como decoração textual.

Evite repetir: "A águia voa alto." / "A águia é forte." / "A águia enxerga longe."

Transforme essas características em reflexões humanas:

**Altitude** pode representar distância emocional para analisar um problema.
**Visão** pode representar pensamento de longo prazo.
**Silêncio** pode representar afastamento do excesso de ruído.
**Liberdade** pode representar responsabilidade pelas próprias escolhas.
**Força** pode representar disciplina diante das dificuldades.

---

## 8. BLINDAGEM MENTAL

A blindagem mental deve ser um conceito recorrente quando aplicável.

Explique que blindar a mente significa: **saber o que merece atenção, estabelecer limites, selecionar influências, controlar impulsos, não absorver qualquer opinião, proteger objetivos e aprender a dizer não.**

Uma mente blindada não é uma mente fechada. É uma mente que **sabe o que deixa entrar e sabe o que precisa deixar passar.**

Não incentive paranoia, isolamento extremo ou desprezo pelas outras pessoas.

---

## 9. LIBERDADE + DIREÇÃO

Explore constantemente a relação entre liberdade e objetivos.

A ideia central: **liberdade sem direção pode virar dispersão.** E: **objetivos sem disciplina continuam sendo apenas desejos.**

Mostre que uma pessoa livre não é necessariamente aquela que faz tudo o que deseja. É aquela que desenvolveu clareza suficiente para decidir: **o que realmente vale a pena desejar, perseguir e abandonar.**

---

## 10. ÁGUIA × GALINHA

Quando fizer sentido, utilize o contraste simbólico:

**Mentalidade de Águia × Mentalidade de Galinha**

Utilize contrastes como: visão × imediatismo, propósito × distração, autonomia × dependência de aprovação, foco × dispersão, coragem × medo, disciplina × impulsividade, liberdade × conformismo, estratégia × reação automática.

Nunca utilize o conceito para humilhar o leitor. A finalidade é provocar reflexão: **"Em quais áreas da minha vida estou agindo com visão e em quais estou apenas reagindo ao ambiente?"**

---

## 11. PSICOLOGIA E CIÊNCIA

Quando utilizar psicologia, comportamento ou estudos:
- não invente pesquisas;
- não invente estatísticas;
- não atribua frases sem confirmação;
- não apresente metáforas como fatos científicos;
- não faça diagnósticos;
- não utilize pseudociência.

Quando não houver fonte disponível, apresente a ideia como **reflexão, metáfora ou interpretação**.

---

## 12. ESTILO

O texto deve ser: **profundo, humano, elegante, provocador, emocional, claro e natural.**

Evite: clichês, frases motivacionais vazias, exageros, promessas de transformação instantânea, "fórmulas secretas", linguagem corporativa, repetição, excesso de exclamações, frases artificiais, linguagem típica de IA.

Use exemplos cotidianos quando ajudarem o leitor a se identificar. O leitor deve pensar: **"Isso está falando da minha vida."**

---

## 13. REGRAS OBRIGATÓRIAS

O artigo deve possuir:
- mínimo de **1.200 palavras**;
- mínimo de **6 seções principais**;
- títulos utilizando `##`;
- nunca utilizar `###` ou `####`;
- parágrafos corridos;
- **zero bullet points no artigo final**;
- utilização estratégica de **negrito**;
- introdução forte;
- desenvolvimento progressivo;
- conclusão memorável;
- português do Brasil.

Não aumente artificialmente o tamanho do artigo repetindo ideias. Cada seção deve acrescentar uma nova camada ao argumento.

---

## 14. CONCLUSÃO

A conclusão deve recuperar a ideia central e provocar uma mudança de perspectiva.

Não termine com frases genéricas como: "Espero que este artigo tenha ajudado." / "Agora é sua vez." / "Compartilhe este conteúdo."

Termine com uma reflexão original relacionada a: **visão, identidade, liberdade, propósito, escolha, disciplina ou transformação.**

A última parte deve deixar uma ideia na mente do leitor depois que ele terminar a leitura.

---

## 15. ORIGINALIDADE

Nunca utilize automaticamente a mesma estrutura emocional.

Mesmo que o tema seja semelhante, alterne: **tipo de abertura, metáfora, perspectiva, ritmo, exemplos, perguntas, argumentos e conclusão.**

Cada artigo deve revelar uma **nova faceta da Mentalidade de Águia**.

---

## 16. PRINCÍPIO EDITORIAL

Antes de finalizar, verifique:

**Este texto ensina o leitor a enxergar melhor a própria vida?**
**Existe uma nova perspectiva?**
**A metáfora da águia acrescenta significado?**
**O leitor consegue relacionar o conteúdo à própria realidade?**
**O texto transmite visão, foco, liberdade, disciplina ou clareza?**
**O artigo evita clichês e repetição?**

Se alguma resposta for não, revise o artigo antes de entregá-lo.

---

## 17. O CÓDIGO ÁGUIA

O conteúdo editorial deve construir naturalmente o universo conceitual de **O Código Águia**.

Entretanto, o artigo deve permanecer útil mesmo para quem nunca ouviu falar do projeto. Não transforme o texto em propaganda.

O leitor deve primeiro receber: **reflexão → conhecimento → identificação → mudança de perspectiva.**

Qualquer referência comercial deverá ser controlada exclusivamente pelo sistema externo responsável pela publicação.

---

## 18. REGRA ABSOLUTA SOBRE CTA

**NÃO ESCREVA CTA NO ARTIGO.**
**NÃO ESCREVA `<!--CTA_FINAL-->`.**
**NÃO ESCREVA CHAMADA PARA COMPRA.**
**NÃO ESCREVA LINK COMERCIAL.**
**NÃO ESCREVA "CONHEÇA O CÓDIGO ÁGUIA".**
**NÃO ESCREVA "ACESSE O SITE".**
**NÃO ESCREVA NENHUM BLOCO COMERCIAL.**

O gerador deve entregar **somente o conteúdo editorial**.

A inserção de qualquer CTA será feita posteriormente por outro sistema, fora deste prompt.

Portanto, independentemente do tema, horário ou configuração externa: **O TEXTO GERADO DEVE TERMINAR NA CONCLUSÃO EDITORIAL.**

---

## 19. FORMATO DE SAÍDA

Entregue somente o artigo final.

Não explique o processo.
Não informe o tema sorteado.
Não informe o ângulo escolhido.
Não informe regras internas.
Não escreva observações antes ou depois.
Não escreva CTA.
Não escreva bloco comercial.

O resultado deve estar **pronto para publicação diretamente no site**.

Formato de saída (siga exatamente, sem nenhum texto adicional antes ou depois):
Linha 1: # Título do Artigo
Linha 2: RESUMO: resumo com até 160 caracteres
Linha 3 em diante: o artigo completo

---

## OBJETIVO FINAL

Construir uma filosofia editorial forte em torno da seguinte ideia:

**A Mentalidade de Águia é aprender a enxergar mais longe, proteger melhor a própria mente, escolher conscientemente o próprio caminho e desenvolver clareza suficiente para transformar liberdade em direção.**

Cada artigo deve apresentar uma nova perspectiva dessa filosofia.

O leitor não deve simplesmente terminar o texto pensando sobre uma águia. Ele deve terminar pensando: **"O que eu preciso mudar na forma como estou enxergando a minha própria vida?"**
"""

print(f"Buscando imagem Unsplash para: {image_key}")
cover_image = buscar_imagem_unsplash(image_key)

payload = json.dumps({
    "model": "openrouter/auto",
    "messages": [{"role": "user", "content": prompt}],
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

article_text = ""
try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
        article_text = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        model_used = data.get("model", "desconhecido")
        print(f"Modelo usado: {model_used} ({len(article_text)} chars)")
except Exception as e:
    print(f"Erro na API: {e}")
    sys.exit(1)

if not article_text or len(article_text) < 500:
    print(f"Resposta muito curta ou vazia ({len(article_text)} chars)")
    sys.exit(1)

lines = article_text.strip().splitlines()
title = ""
excerpt = ""
content_lines = []

for i, line in enumerate(lines):
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

# Inserção de CTA externo (50% de chance)
if use_cta:
    content_md = content_md.rstrip() + "\n" + EBOOK_CTA_FINAL

slug = slugify(title)
if not slug:
    slug = f"post-{timestamp}"

reading_time = max(1, round(len(content_md.split()) / 200))

# ──────────────────────────────────────────────────────────────────────────────
# INJETAR O POST DIRETAMENTE EM src/data/blog.ts (fonte de verdade do app)
# ──────────────────────────────────────────────────────────────────────────────
def escape_backtick(s):
    """Escapa backticks e ${} para uso seguro dentro de template literals TS."""
    s = s.replace("\\", "\\\\")  # barras invertidas primeiro
    s = s.replace("`", "\\`")    # backtick
    s = s.replace("${", "\\${") # template expressions
    return s

def ts_string(s):
    """Serializa string como template literal TypeScript multi-linha."""
    return "`" + escape_backtick(s) + "`"

def ts_string_simple(s):
    """Serializa string curta com aspas duplas (sem quebras de linha)."""
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + s + '"'

def ts_array(lst):
    items = ", ".join(ts_string_simple(x) for x in lst)
    return f"[{items}]"

# Monta o bloco TypeScript do novo post
new_post_block = f"""  {{
    id: {ts_string_simple(slug)},
    slug: {ts_string_simple(slug)},
    title: {ts_string_simple(title)},
    excerpt: {ts_string_simple(excerpt[:300])},
    date: {ts_string_simple(today)},
    readingTime: {reading_time},
    category: {ts_string_simple(category)},
    coverImage: {ts_string_simple(cover_image)},
    tags: {ts_array(tags)},
    featured: false,
    content: {ts_string(content_md)},
  }},"""

# Lê o arquivo blog.ts atual
with open(BLOG_TS_PATH, "r", encoding="utf-8") as f:
    blog_ts = f.read()

# Verifica se o slug já existe (evita duplicatas)
if f'slug: "{slug}"' in blog_ts or f"slug: '{slug}'" in blog_ts:
    print(f"Slug '{slug}' já existe em blog.ts. Abortando para evitar duplicata.")
    print(f"Título: {title}")
    print(f"Slug: {slug}")
    sys.exit(0)

# Insere o novo post ANTES do fechamento do array (antes de `];`)
INSERT_MARKER = "];\n\nexport const blogPosts"
if INSERT_MARKER not in blog_ts:
    INSERT_MARKER = "export const blogPosts"

insert_pos = blog_ts.find(INSERT_MARKER)
if insert_pos == -1:
    print("ERRO: Não encontrou marcador de inserção em blog.ts")
    sys.exit(1)

updated_ts = blog_ts[:insert_pos] + new_post_block + "\n" + blog_ts[insert_pos:]

with open(BLOG_TS_PATH, "w", encoding="utf-8") as f:
    f.write(updated_ts)

print(f"Post injetado em {BLOG_TS_PATH}")
print(f"Título: {title}")
print(f"Slug: {slug}")
print(f"Leitura: {reading_time} min | {len(content_md.split())} palavras")
print(f"Imagem: {cover_image[:100]}")
