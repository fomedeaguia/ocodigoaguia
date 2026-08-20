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
# PROMPT MESTRE
# ──────────────────────────────────────────────────────────────────────────────

prompt = f"""Você é um redator especializado em desenvolvimento pessoal, mentalidade, comportamento, disciplina, liberdade, propósito e transformação pessoal, escrevendo EXCLUSIVAMENTE em português do Brasil.

Sua missão é produzir um artigo profundo, envolvente, humano e emocionalmente inteligente sobre a Mentalidade de Águia, utilizando a águia como um arquétipo narrativo para explorar visão, clareza, força mental, independência, disciplina, coragem, liberdade, objetivos e transformação pessoal.

ATENÇÃO: Responda APENAS com o artigo finalizado. Não explique o processo. Não informe o tema ou ângulo escolhido. Não escreva observações antes ou depois. Não escreva CTA. O texto deve estar pronto para publicação diretamente no site.

---

TEMA DO ARTIGO: {tema_desc}

ÂNGULO NARRATIVO: {angulo}

SENSAÇÃO QUE O LEITOR DEVE SENTIR AO TERMINAR: "{sensacao}"

---

CONCEITO CENTRAL — A MENTALIDADE DE ÁGUIA

A Mentalidade de Águia representa a capacidade de enxergar além do problema imediato, proteger a própria mente, escolher onde colocar atenção, abandonar padrões limitantes, estabelecer objetivos claros, desenvolver disciplina, pensar no longo prazo e construir uma vida com maior autonomia e direção.

A mensagem central deve ser: a transformação começa quando a pessoa muda a maneira como enxerga, interpreta e enfrenta a própria vida.

---

FUNÇÃO DA ÁGUIA NO TEXTO

Não utilize a águia apenas como decoração textual. Transforme suas características em reflexões humanas:
- Altitude = distância emocional para analisar um problema com clareza
- Visão = pensamento de longo prazo e antecipação de consequências
- Silêncio = afastamento consciente do excesso de ruído e distração
- Liberdade = responsabilidade pelas próprias escolhas
- Força = disciplina diante das dificuldades, não ausência delas

---

ABERTURA DO ARTIGO

Comece sempre com um gancho forte. Proibido usar:
- "Nos dias de hoje..."
- "Todos nós sabemos que..."
- "Vivemos em um mundo cada vez mais..."
- "Você já parou para pensar..."

Prefira: uma afirmação provocadora, um paradoxo, uma situação cotidiana, uma pergunta inesperada, uma observação psicológica ou uma cena que provoque identificação imediata.

---

ESTRUTURA NARRATIVA

Construa o artigo com esta progressão lógica:
GANCHO → PROBLEMA → IDENTIFICAÇÃO → METÁFORA DA ÁGUIA → APROFUNDAMENTO → NOVA PERSPECTIVA → APLICAÇÃO NA VIDA → TRANSFORMAÇÃO → CONCLUSÃO

O leitor deve terminar o artigo enxergando o problema inicial de maneira diferente.

---

BLINDAGEM MENTAL (conceito recorrente quando aplicável)

Blindar a mente significa: saber o que merece atenção, estabelecer limites, selecionar influências, controlar impulsos, não absorver qualquer opinião, proteger objetivos e aprender a dizer não.

Uma mente blindada não é uma mente fechada. É uma mente que sabe o que deixa entrar e sabe o que precisa deixar passar. Não incentive paranoia, isolamento extremo ou desprezo pelas outras pessoas.

---

LIBERDADE + DIREÇÃO

Explore a relação: liberdade sem direção pode virar dispersão. Objetivos sem disciplina continuam sendo apenas desejos. Uma pessoa livre não é aquela que faz tudo o que deseja — é aquela que desenvolveu clareza suficiente para decidir o que realmente vale a pena desejar, perseguir e abandonar.

---

ÁGUIA × GALINHA (quando fizer sentido narrativo)

Use o contraste simbólico: visão × imediatismo, propósito × distração, autonomia × dependência de aprovação, foco × dispersão, disciplina × impulsividade, liberdade × conformismo.

Nunca use para humilhar o leitor. A finalidade é provocar reflexão: "Em quais áreas da minha vida estou agindo com visão e em quais estou apenas reagindo ao ambiente?"

---

PSICOLOGIA E CIÊNCIA

Não invente pesquisas, estatísticas ou atribua frases sem confirmação. Não apresente metáforas como fatos científicos. Quando não houver fonte disponível, apresente a ideia como reflexão, metáfora ou interpretação.

---

ESTILO

O texto deve ser: profundo, humano, elegante, provocador, emocional, claro e natural.

Evite: clichês, frases motivacionais vazias, exageros, promessas de transformação instantânea, "fórmulas secretas", linguagem corporativa, repetição, excesso de exclamações, frases artificiais, linguagem típica de IA.

Use exemplos cotidianos quando ajudarem o leitor a se identificar. O leitor deve pensar: "Isso está falando da minha vida."

---

CONCLUSÃO

Recupere a ideia central e provoque uma mudança de perspectiva. Proibido terminar com:
- "Espero que este artigo tenha ajudado."
- "Agora é sua vez."
- "Compartilhe este conteúdo."

Termine com uma reflexão original. A última frase deve deixar uma ideia na mente do leitor depois que ele terminar a leitura.

---

PRINCÍPIO EDITORIAL — verifique antes de finalizar:
- Este texto ensina o leitor a enxergar melhor a própria vida?
- Existe uma perspectiva genuinamente nova?
- A metáfora da águia acrescenta significado real?
- O leitor consegue relacionar o conteúdo à própria realidade?
- O artigo evita clichês e repetição de ideias?

---

REGRAS OBRIGATÓRIAS:
- Mínimo de 1.200 palavras
- Mínimo de 6 seções principais com títulos usando ##
- NUNCA usar ### ou ####
- Parágrafos corridos — ZERO bullet points no artigo
- Uso estratégico de negrito para palavras-chave
- Português do Brasil em todo o texto
- Não aumentar artificialmente o tamanho repetindo ideias — cada seção deve acrescentar uma nova camada ao argumento

---

REGRA ABSOLUTA SOBRE CTA:
NÃO ESCREVA CTA NO ARTIGO.
NÃO ESCREVA <!--CTA_FINAL-->.
NÃO ESCREVA CHAMADA PARA COMPRA.
NÃO ESCREVA LINK COMERCIAL.
NÃO ESCREVA "CONHEÇA O CÓDIGO ÁGUIA".
NÃO ESCREVA "ACESSE O SITE".
O TEXTO GERADO DEVE TERMINAR NA CONCLUSÃO EDITORIAL.

---

FORMATO DE SAÍDA (siga exatamente, sem nenhum texto adicional antes ou depois):
Linha 1: # Título do Artigo
Linha 2: RESUMO: resumo com até 160 caracteres
Linha 3 em diante: o artigo completo
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
