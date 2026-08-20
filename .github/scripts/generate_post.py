import os, json, urllib.request, urllib.error, urllib.parse, sys, random, re
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
today = now.strftime("%Y-%m-%d")
hour = now.hour
api_key = os.environ["OPENROUTER_API_KEY"]
unsplash_key = os.environ.get("UNSPLASH_ACCESS_KEY", "")
timestamp = now.strftime("%Y-%m-%d-%H")

CODIGO_AGUIA_FACTS = """
- O Código Águia é um ebook sobre transformação de mentalidade e ascensão financeira.
- O símbolo da águia representa visão ampla, coragem, renovação e prosperidade.
- A águia é o único animal que enfrenta a tempestade voando acima das nuvens.
- O ebook ensina os princípios arquetípicos que elevam pessoas de um nível de vida para outro.
- Conteúdo: mentalidade de alto desempenho, foco, resiliência, prosperidade financeira e liberdade.
- Preço: acessível, entrega imediata em PDF.
- Site oficial: ocodigoaguia.com.br
NÃO DIZER: resultados garantidos, resolver todos os problemas, riqueza rápida.
"""

EBOOK_CTA_MEIO = """

---

## O Mapa Que Faltava Para Você Subir de Nível

Se você chegou até aqui, já percebeu que a mudança começa dentro — na forma como você enxerga, decide e age. O **Código Águia** reúne em um ebook direto e transformador os princípios que separam quem observa a tempestade de quem voa acima dela. São páginas escritas para quem está pronto para parar de reagir e começar a voar. [Clique aqui e garanta o seu exemplar agora](https://ocodigoaguia.com.br).

---

"""

EBOOK_CTA_FINAL = """

---

## Pronto Para Ativar o Arquétipo da Águia em Você?

Tudo que você leu aqui é apenas o começo. O **Código Águia** aprofunda cada um desses princípios com clareza, exemplos reais e um roteiro prático para quem quer mudar de nível de verdade — não amanhã, mas agora. Se a águia está dentro de você, está na hora de libertá-la. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).

---"""

UNSPLASH_QUERIES = {
    "aguia_liberdade": "eagle flying freedom sky",
    "prosperidade": "success abundance mountain",
    "mentalidade": "focus determination sunrise",
    "renovacao": "transformation renewal nature",
    "lideranca": "mountain summit leadership",
    "foco": "precision focus arrow",
    "coragem": "storm sky courage",
    "visao": "aerial view horizon",
    "abundancia": "abundance nature light",
    "transformacao": "light growth nature",
}
DEFAULT_UNSPLASH_QUERY = "eagle sky freedom"

POLLINATIONS_PROMPTS = {
    "aguia_liberdade": "majestic eagle soaring above clouds golden hour dramatic lighting no text",
    "prosperidade": "eagle silhouette golden light wealth abundance no text",
    "mentalidade": "eagle eye close-up sharp focus dark dramatic tones no text",
    "renovacao": "eagle rising transformation dark gold palette no text",
    "lideranca": "eagle mountain peak sunrise leadership no text",
    "foco": "eagle diving precision dark blue tones no text",
    "coragem": "eagle storm clouds courage dramatic sky no text",
    "visao": "eagle soaring wide panoramic view vision strategy no text",
    "abundancia": "eagle wings golden light rays abundance no text",
    "transformacao": "eagle emerging shadows into light personal growth no text",
}
DEFAULT_POLLINATIONS = "powerful eagle soaring clouds transformation success golden tones no text"


def buscar_imagem(image_key, unsplash_key):
    if unsplash_key:
        query = UNSPLASH_QUERIES.get(image_key, DEFAULT_UNSPLASH_QUERY)
        for q in [query, DEFAULT_UNSPLASH_QUERY]:
            try:
                url = f"https://api.unsplash.com/photos/random?query={urllib.parse.quote(q)}&orientation=landscape&content_filter=high"
                req = urllib.request.Request(url, headers={"Authorization": f"Client-ID {unsplash_key}", "Accept-Version": "v1"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read())
                    img = data["urls"]["regular"]
                    print(f"Unsplash OK: {img[:80]}")
                    return img
            except Exception as e:
                print(f"Unsplash falhou ({q}): {e}")
    prompt = POLLINATIONS_PROMPTS.get(image_key, DEFAULT_POLLINATIONS)
    seed = abs(hash(timestamp)) % 99999
    img = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width=1200&height=630&nologo=true&seed={seed}"
    print(f"Pollinations fallback: {img[:80]}")
    return img


TOPICOS_MANHA = [
    ("aguia_liberdade", "por que a águia é universalmente reconhecida como símbolo de liberdade, prosperidade e ascensão, explorando sua origem em culturas romana, asteca, americana e brasileira"),
    ("prosperidade", "a relação entre o arquétipo da águia e a prosperidade financeira, por que empresas e líderes usam a águia como símbolo de poder econômico"),
    ("mentalidade", "a mentalidade de alto desempenho representada pela águia: visão estratégica, paciência e coragem para agir com precisão"),
    ("visao", "a visão da águia como metáfora de vida: enxergar além do óbvio, antecipar tendências e tomar decisões estratégicas"),
    ("abundancia", "como o símbolo da águia se associa à abundância em tradições espirituais, e como a consciência de abundância difere da mentalidade de escassez"),
]

TOPICOS_TARDE = [
    ("renovacao", "o ritual de renovação da águia como metáfora de transformação pessoal: sair da zona de conforto e recomeçar mais forte"),
    ("coragem", "como a águia enfrenta tempestades voando acima delas, como lição de resiliência para quem enfrenta crises e fracassos"),
    ("lideranca", "a águia como símbolo de liderança natural por altitude, visão e exemplo, e como aplicar isso na vida pessoal e profissional"),
    ("transformacao", "os 7 atributos arquetípicos da águia que transformam vidas: visão, coragem, renovação, altitude, precisão, liberdade e prosperidade"),
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
slug = f"post-{timestamp}"

category_map = {
    "manha": ["Arquétipo da Águia", "Prosperidade"],
    "tarde": ["Transformação", "Mentalidade"],
    "noite": ["Filosofia", "Nível de Vida"],
}
category = random.choice(category_map[period])

tags_map = {
    "aguia_liberdade": ["arquétipo da águia", "liberdade", "simbolismo"],
    "prosperidade": ["prosperidade", "abundância", "mentalidade financeira"],
    "mentalidade": ["mentalidade", "alto desempenho", "crescimento pessoal"],
    "renovacao": ["renovação", "transformação", "recomeço"],
    "lideranca": ["liderança", "águia", "visão estratégica"],
    "foco": ["foco", "disciplina", "resultados"],
    "coragem": ["coragem", "resiliência", "superação"],
    "visao": ["visão", "estratégia", "consciência"],
    "abundancia": ["abundância", "riqueza", "consciência financeira"],
    "transformacao": ["transformação", "mudança de nível", "desenvolvimento pessoal"],
}
tags = tags_map.get(image_key, ["código águia", "transformação", "prosperidade"])

# --- ETAPA 1: modelo gera apenas o artigo em Markdown puro ---
system_msg = (
    "Você é o redator do blog O Código Águia, portal de transformação pessoal e prosperidade. "
    "Escreve artigos profundos, inspiradores, com tom humano. "
    "REGRAS: sem bullet points, sem listas, tudo em parágrafos corridos. "
    "Use ## para títulos de seção (mínimo 6 seções). Jamais ### ou ####. "
    "Negrito com **palavra**. Links: [texto](url). "
    "NUNCA invente dados. Escreva 100% em português do Brasil. "
    "Retorne APENAS o texto do artigo em Markdown. Nada mais."
)

user_msg = (
    f"Hoje é {today}. Escreva um artigo sobre: {topic_desc}.\n\n"
    f"Fatos obrigatórios:{CODIGO_AGUIA_FACTS}\n"
    "Mínimo 1200 palavras. Ao mencionar O Código Águia, linke: [ocodigoaguia.com.br](https://ocodigoaguia.com.br).\n"
    "Após a 3ª seção insira exatamente: <!--CTA_MEIO-->\n"
    "No final do artigo insira exatamente: <!--CTA_FINAL-->\n"
    "A primeira linha deve ser o título no formato: # Título do Artigo\n"
    "A segunda linha deve ser o resumo no formato: RESUMO: texto do resumo com até 160 caracteres"
)

# Modelos atualizados (sem os que estão com 404)
MODELS = [
    "google/gemma-3-27b-it:free",
    "nvidia/nemotron-3-nano-30b-a3b:free",
    "meta-llama/llama-3.1-8b-instruct:free",
    "qwen/qwen-2.5-7b-instruct:free",
]


def chamar_modelo(model, system_msg, user_msg, max_tokens=6000):
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.75,
        "max_tokens": max_tokens
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
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()


# Busca imagem
print(f"Buscando imagem para: {image_key}")
cover_image = buscar_imagem(image_key, unsplash_key)

# Gera artigo em texto puro
article_text = ""
for model in MODELS:
    print(f"Tentando modelo: {model}")
    try:
        result = chamar_modelo(model, system_msg, user_msg)
        if result and len(result) > 500:
            article_text = result
            print(f"Sucesso com {model} ({len(result)} chars)")
            break
        else:
            print(f"{model} retornou muito curto ({len(result)} chars), próximo...")
    except urllib.error.HTTPError as e:
        print(f"{model} falhou: {e.code}")
    except Exception as e:
        print(f"{model} erro: {e}")

if not article_text:
    print("Todos os modelos falharam.")
    sys.exit(1)

# --- ETAPA 2: Python extrai título, resumo e monta o JSON ---
lines = article_text.strip().splitlines()

# Extrai título (primeira linha com # )
title = ""
for i, line in enumerate(lines):
    if line.startswith("# "):
        title = line[2:].strip()
        lines.pop(i)
        break
if not title:
    # Fallback: usa a primeira seção ## como título
    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip()
            break
if not title:
    title = f"A Águia e o Caminho da Transformação - {today}"

# Extrai resumo (linha RESUMO:)
excerpt = ""
for i, line in enumerate(lines):
    if line.startswith("RESUMO:"):
        excerpt = line[7:].strip()
        lines.pop(i)
        break
if not excerpt:
    # Fallback: primeiro parágrafo com mais de 80 chars
    for line in lines:
        clean = line.strip()
        if len(clean) > 80 and not clean.startswith("#"):
            excerpt = clean[:200]
            break

# Monta o conteúdo final
content_md = "\n".join(lines).strip()

# Injeta CTAs
content_md = content_md.replace("<!--CTA_MEIO-->", EBOOK_CTA_MEIO)
content_md = content_md.replace("<!--CTA_FINAL-->", EBOOK_CTA_FINAL)

# Se os marcadores não foram inseridos pelo modelo, injeta manualmente
if EBOOK_CTA_MEIO not in content_md:
    sections = re.split(r"(?=\n## )", content_md)
    if len(sections) >= 4:
        sections.insert(3, EBOOK_CTA_MEIO)
    content_md = "".join(sections)

if EBOOK_CTA_FINAL not in content_md:
    content_md += EBOOK_CTA_FINAL

reading_time = max(1, round(len(content_md.split()) / 200))

post = {
    "id": slug,
    "title": title,
    "slug": slug,
    "excerpt": excerpt,
    "content": content_md,
    "category": category,
    "author": "O Código Águia",
    "date": today,
    "readingTime": reading_time,
    "featured": False,
    "coverImage": cover_image,
    "tags": tags
}

os.makedirs("public/blog-posts", exist_ok=True)
filepath = f"public/blog-posts/{slug}.json"
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(post, f, ensure_ascii=False, indent=2)

print(f"Post salvo: {filepath}")
print(f"Título: {post['title']}")
print(f"Leitura: {reading_time} min | {len(content_md.split())} palavras")
