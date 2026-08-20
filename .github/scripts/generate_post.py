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


CODIGO_AGUIA_FACTS = """
- O Código Águia é um ebook sobre transformação de mentalidade e ascensão financeira.
- O símbolo da águia representa visão ampla, coragem, renovação e prosperidade.
- A águia é o único animal que enfrenta a tempestade voando acima das nuvens.
- O ebook ensina os princípios arquetipicos que elevam pessoas de um nível de vida para outro.
- Conteúdo: mentalidade de alto desempenho, foco, resiliência, prosperidade financeira e liberdade.
- Preço: acessível, entrega imediata em PDF.
- Site oficial: ocodigoaguia.com.br
NÃO DIZER: resultados garantidos, resolver todos os problemas, riqueza rápida.
"""

EBOOK_CTA_FINAL = """

---

## Pronto Para Ativar o Arquétipo da Águia em Você?

Tudo que você leu aqui é apenas o começo. O **Código Águia** aprofunda cada um desses princípios com clareza, exemplos reais e um roteiro prático para quem quer mudar de nível de verdade — não amanhã, mas agora. Se a águia está dentro de você, está na hora de libertá-la. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).

---"""

UNSPLASH_QUERIES = {
    "aguia_liberdade": ["eagle flying sky", "eagle soaring clouds", "bird freedom sky"],
    "prosperidade":    ["success mountain peak", "abundance sunrise", "wealthy mindset"],
    "mentalidade":     ["focus determination sunrise", "mind power meditation", "discipline training"],
    "renovacao":       ["transformation butterfly nature", "renewal dawn light", "rebirth nature"],
    "lideranca":       ["mountain summit leader", "leadership vision horizon", "strong leader"],
    "foco":            ["focus target arrow", "laser focus discipline", "concentration work"],
    "coragem":         ["storm courage sky", "brave challenge mountain", "overcome fear"],
    "visao":           ["aerial view horizon", "wide view landscape", "strategic vision sky"],
    "abundancia":      ["abundance nature light", "golden harvest prosperity", "rich nature golden"],
    "transformacao":   ["light growth forest", "personal growth sunrise", "change transformation"],
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


TOPICOS_MANHA = [
    ("aguia_liberdade", "por que a águia é universalmente reconhecida como símbolo de liberdade, prosperidade e ascensão, explorando sua origem em culturas romana, asteca, americana e brasileira"),
    ("prosperidade", "a relação entre o arquétipo da águia e a prosperidade financeira, por que empresas e líderes usam a águia como símbolo de poder econômico"),
    ("mentalidade", "a mentalidade de alto desempenho representada pela águia: visão estratégica, paciência e coragem para agir com precisão"),
    ("visao", "a visão da águia como metáfora de vida: enxergar além do óbvio, antecipar tendências e tomar decisões estratégicas"),
    ("abundancia", "como o símbolo da águia se associa à abundância em tradições espirituais, e como a consciência de abundância difere da mentalidade de escassez"),
]

TOPICOS_TARDE = [
    ("renovacao", "o ritual de renovação da águia como metáfora de transformação pessoal: sair da zona de conforto e recomecar mais forte"),
    ("coragem", "como a águia enfrenta tempestades voando acima delas, como lição de resiliência para quem enfrenta crises e fracassos"),
    ("lideranca", "a águia como símbolo de liderança natural por altitude, visão e exemplo, e como aplicar isso na vida pessoal e profissional"),
    ("transformacao", "os 7 atributos arquetipicos da águia que transformam vidas: visão, coragem, renovação, altitude, precisão, liberdade e prosperidade"),
    ("foco", "o foco da águia que concentra toda energia no alvo, e como esse foco intencional é o diferencial entre sonhar e realizar"),
]

TOPICOS_NOITE = [
    ("aguia_liberdade", "por que pessoas bem-sucedidas se identificam com a águia, explorando a psicologia dos arquétipos de Jung e o poder dos símbolos na formação de identidade"),
    ("prosperidade", "os princípios de prosperidade da águia presentes em livros como Pai Rico Pai Pobre, Mindset e Os Segredos da Mente Milionária"),
    ("mentalidade", "a diferença entre mentalidade de galinha e mentalidade de águia, com exemplos práticos em decisões financeiras, relacionamentos e carreira"),
    ("visao", "como a simbologia da águia aparece em moedas, brasões, logos de empresas Fortune 500 e bandeiras de nações poderosas"),
    ("abundancia", "o que significa voar como uma águia na vida real: sair de empregos que aprisionam, relacionamentos que drenam, hábitos que sabotam"),
]

if hour < 12:
    pool = TOPICOS_MANHA
    period = "manha"
elif hour < 19:
    pool = TOPICOS_TARDE
    period = "tarde"
else:
    pool = TOPICOS_NOITE
    period = "noite"

image_key, topic_desc = random.choice(pool)

category_map = {
    "manha": ["Arquétipo da Águia", "Prosperidade"],
    "tarde": ["Transformação", "Mentalidade"],
    "noite": ["Filosofia", "Nível de Vida"],
}
category = random.choice(category_map[period])

tags_map = {
    "aguia_liberdade": ["arquétipo da águia", "liberdade", "simbolismo"],
    "prosperidade":    ["prosperidade", "abundância", "mentalidade financeira"],
    "mentalidade":     ["mentalidade", "alto desempenho", "crescimento pessoal"],
    "renovacao":       ["renovação", "transformação", "recomeço"],
    "lideranca":       ["liderança", "águia", "visão estratégica"],
    "foco":            ["foco", "disciplina", "resultados"],
    "coragem":         ["coragem", "resiliência", "superação"],
    "visao":           ["visão", "estratégia", "consciência"],
    "abundancia":      ["abundância", "riqueza", "consciência financeira"],
    "transformacao":   ["transformação", "mudança de nível", "desenvolvimento pessoal"],
}
tags = tags_map.get(image_key, ["código águia", "transformação", "prosperidade"])

use_cta = random.random() < 0.5
cta_instruction = ""
if use_cta:
    cta_instruction = "\n- No final do artigo (após a última seção), insira exatamente esta linha e nada mais: <!--CTA_FINAL-->"
else:
    cta_instruction = "\n- Não insira nenhum CTA, banner ou menção ao O Código Águia. Escreva apenas o artigo."

prompt = f"""Você é um redator especializado em conteúdo de desenvolvimento pessoal escrevendo EXCLUSIVAMENTE em português do Brasil.

Escreva um artigo de blog completo em português do Brasil sobre: {topic_desc}.

ATENÇÃO: Responda APENAS com o artigo finalizado. Não inclua rascunhos, reflexões, análise do prompt, planejamento, notas internas ou qualquer texto que não seja o artigo em si.

Fatos sobre O Código Águia (use SOMENTE se as instruções abaixo permitirem):{CODIGO_AGUIA_FACTS}

Regras obrigatórias:
- Escreva TODO o texto em português do Brasil
- Mínimo 1200 palavras, tudo em parágrafos corridos (NUNCA use listas ou bullet points)
- Use ## para títulos de seção (mínimo 6 seções). NUNCA use ### ou ####
- Use **negrito** para ênfase em palavras-chave
- Tom inspirador e humano, sem clichês de IA
- NUNCA invente dados ou estatísticas{cta_instruction}

Formato de saída (siga exatamente, sem nenhum texto adicional antes ou depois):
Linha 1: # Título do Artigo
Linha 2: RESUMO: resumo com até 160 caracteres
Linha 3 em diante: o artigo completo
"""

print(f"Buscando imagem Unsplash para: {image_key}")
cover_image = buscar_imagem_unsplash(image_key)

payload = json.dumps({
    "model": "openrouter/auto",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.75,
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
    title = f"A Águia e o Caminho da Transformação — {today}"

if not excerpt:
    for line in content_lines:
        clean = line.strip()
        if len(clean) > 80 and not clean.startswith("#"):
            excerpt = re.sub(r"\*\*|\[.*?\]\(.*?\)", "", clean)[:200].strip()
            break

if use_cta:
    content_md = content_md.replace("<!--CTA_FINAL-->", EBOOK_CTA_FINAL)
    if EBOOK_CTA_FINAL.strip() not in content_md:
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
    # Ainda imprime para o workflow capturar
    print(f"Título: {title}")
    print(f"Slug: {slug}")
    sys.exit(0)

# Insere o novo post ANTES do fechamento do array (antes de `];`)
INSERT_MARKER = "];\n\nexport const blogPosts"
if INSERT_MARKER not in blog_ts:
    # Fallback: antes de `export const blogPosts`
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
