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
NÃO DIZER:
- Resultados financeiros garantidos ou específicos
- Que o ebook resolve todos os problemas do leitor
- Promessas de riqueza rápida ou fácil
"""

EBOOK_CTA_MEIO = """\n\n---\n\n## O Mapa Que Faltava Para Você Subir de Nível\n\nSe você chegou até aqui, já percebeu que a mudança começa dentro — na forma como você enxerga, decide e age. O **Código Águia** reúne em um ebook direto e transformador os princípios que separam quem observa a tempestade de quem voa acima dela. São páginas escritas para quem está pronto para parar de reagir e começar a voar. [Clique aqui e garanta o seu exemplar agora](https://ocodigoaguia.com.br).\n\n---\n\n"""

EBOOK_CTA_FINAL = """\n\n---\n\n## Pronto Para Ativar o Arquétipo da Águia em Você?\n\nTudo que você leu aqui é apenas o começo. O **Código Águia** aprofunda cada um desses princípios com clareza, exemplos reais e um roteiro prático para quem quer mudar de nível de verdade — não amanhã, mas agora. Se a águia está dentro de você, está na hora de libertá-la. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).\n\n---"""

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
    "aguia_liberdade": "majestic eagle soaring above clouds golden hour dramatic lighting no text premium motivational",
    "prosperidade": "eagle silhouette golden light wealth abundance concept no text professional",
    "mentalidade": "eagle eye close-up sharp focus mindset dark dramatic tones no text",
    "renovacao": "eagle rising transformation dark gold palette no text",
    "lideranca": "eagle mountain peak sunrise leadership elevation no text",
    "foco": "eagle diving precision dark blue tones no text",
    "coragem": "eagle storm clouds courage resilience dramatic sky no text",
    "visao": "eagle soaring wide panoramic view below vision strategy no text",
    "abundancia": "eagle wings golden light rays abundance success no text",
    "transformacao": "eagle emerging shadows into light personal growth no text",
}
DEFAULT_POLLINATIONS = "powerful eagle soaring clouds transformation success dramatic golden tones no text"


def buscar_imagem(image_key, unsplash_key):
    # Tenta Unsplash primeiro se tiver chave
    if unsplash_key:
        query = UNSPLASH_QUERIES.get(image_key, DEFAULT_UNSPLASH_QUERY)
        for q in [query, DEFAULT_UNSPLASH_QUERY]:
            try:
                url = f"https://api.unsplash.com/photos/random?query={urllib.parse.quote(q)}&orientation=landscape&content_filter=high"
                req = urllib.request.Request(url, headers={"Authorization": f"Client-ID {unsplash_key}", "Accept-Version": "v1"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read())
                    img = data["urls"]["regular"]
                    print(f"Unsplash OK: {img[:60]}...")
                    return img
            except Exception as e:
                print(f"Unsplash falhou ({q}): {e}")
    # Fallback: Pollinations (sem chave, ilimitado)
    prompt = POLLINATIONS_PROMPTS.get(image_key, DEFAULT_POLLINATIONS)
    slug_seed = abs(hash(timestamp)) % 99999
    img = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width=1200&height=630&nologo=true&seed={slug_seed}"
    print(f"Usando Pollinations: {img[:80]}...")
    return img


TOPICOS_MANHA = [
    ("aguia_liberdade", "Escreva um artigo profundo explicando por que a águia é universalmente reconhecida como símbolo de liberdade, prosperidade e ascensão. Explore a origem desse arquétipo em culturas como a romana, asteca, americana e brasileira, e como esse símbolo impacta a psicologia de pessoas que buscam mudar de nível de vida."),
    ("prosperidade", "Escreva um artigo sobre a relação entre o arquétipo da águia e a prosperidade financeira: por que empresas, países e líderes usam a águia como símbolo de poder econômico, e como incorporar essa mentalidade transforma a forma como a pessoa lida com dinheiro e oportunidades."),
    ("mentalidade", "Escreva um artigo sobre a mentalidade de alto desempenho representada pela águia: visão estratégica, paciência para esperar o momento certo e coragem para agir com precisão. Como esses traços separam pessoas que crescem das que ficam estagnadas."),
    ("visao", "Escreva um artigo sobre a visão da águia como metáfora de vida: a capacidade de enxergar além do óbvio, antecipar tendências e tomar decisões de cima para baixo. Como desenvolver essa perspectiva estratégica no dia a dia e nos negócios."),
    ("abundancia", "Escreva um artigo sobre como o símbolo da águia está associado à abundância em diversas tradições espirituais e filosóficas, e como a consciência de abundância — diferente da mentalidade de escassez — é o primeiro passo para mudanças financeiras reais."),
]

TOPICOS_TARDE = [
    ("renovacao", "Escreva um artigo sobre o ritual de renovação da águia: o processo em que ela quebra o bico, arranca as garras e as penas para renascer mais forte. Use esse processo como metáfora poderosa para a transformação pessoal, saindo de zonas de conforto e recomeçando com mais força."),
    ("coragem", "Escreva um artigo sobre como a águia enfrenta tempestades voando acima delas em vez de se esconder. Use essa característica como lição de resiliência: como as pessoas de alto nível encaram crises, perdas e fracassos como trampolins, não como fins."),
    ("lideranca", "Escreva um artigo sobre a águia como símbolo de liderança natural: ela não lidera por dominação, mas por altitude, visão e exemplo. Como esse modelo de liderança se aplica à vida pessoal, profissional e financeira de quem quer mudar de nível."),
    ("transformacao", "Escreva um artigo sobre os 7 atributos arquetípicos da águia que podem transformar a vida de qualquer pessoa: visão, coragem, renovação, altitude, precisão, liberdade e prosperidade. Explique como cada um se aplica na prática."),
    ("foco", "Escreva um artigo sobre o foco da águia: ela tem a capacidade de concentrar 100% da sua energia no alvo antes de mergulhar. Como esse nível de foco intencional é o diferencial entre sonhar e realizar, e como treiná-lo no cotidiano."),
]

TOPICOS_NOITE = [
    ("aguia_liberdade", "Escreva um artigo sobre por que pessoas bem-sucedidas se identificam com a águia e não com outras aves. Explore a psicologia dos arquétipos de Carl Jung, o poder dos símbolos na formação de identidade e como escolher conscientemente seu arquétipo de vida acelera transformações."),
    ("prosperidade", "Escreva um artigo sobre os princípios de prosperidade que a águia representa e que estão presentes em livros como Pai Rico Pai Pobre, Mindset e Os Segredos da Mente Milionária. Como o arquétipo da águia sintetiza o que esses livros ensinam."),
    ("mentalidade", "Escreva um artigo sobre a diferença entre a mentalidade de galinha e a mentalidade de águia: como a galinha reage ao ambiente e a águia cria o seu. Exemplos práticos de como essa diferença se manifesta em decisões financeiras, relacionamentos e carreira."),
    ("visao", "Escreva um artigo sobre como a simbologia da águia aparece em moedas, brasões de armas, logos de empresas Fortune 500 e bandeiras de nações poderosas. O que essa presença universal diz sobre o que a humanidade associa ao poder, à prosperidade e à ascensão."),
    ("abundancia", "Escreva um artigo reflexivo sobre o que significa voar como uma águia na prática da vida real: saindo de empregos que aprisionam, relacionamentos que drenam energia, hábitos que sabotam o crescimento. Um convite à transformação profunda e duradoura."),
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

image_key, topic = random.choice(pool)
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

system_msg = (
    "Você é o redator do blog O Código Águia, portal de transformação pessoal, mentalidade e prosperidade. "
    "Escreve artigos profundos, inspiradores e com tom humano — sem soar como IA. "
    "REGRAS OBRIGATÓRIAS: "
    "1. NUNCA use bullet points, traços ou listas. Tudo em parágrafos corridos. "
    "2. Use ## apenas para títulos de seção. Jamais ### ou ####. "
    "3. Links sempre no formato [texto](url). "
    "4. Tom inspirador, direto. Sem clichês de IA. "
    "5. NUNCA invente dados ou estatísticas. "
    "6. Escreva 100% em português do Brasil. "
    "CRITICO: Retorne APENAS JSON puro. Sem texto antes ou depois. Sem blocos de codigo. "
    "Comece com { e termine com }."
)

user_msg = (
    f"Hoje e {today}. {topic}\n\n"
    f"FATOS: {CODIGO_AGUIA_FACTS}\n\n"
    "Escreva artigo com MINIMO 1200 palavras em portugues do Brasil. "
    "Use ## para secoes (minimo 6 secoes) e **negrito** para enfase. "
    "Paragrafos corridos, sem listas. "
    "Ao citar O Codigo Aguia, linke: [ocodigoaguia.com.br](https://ocodigoaguia.com.br). "
    "Insira o marcador <!--CTA_MEIO--> apos a 3a secao e <!--CTA_FINAL--> no final. "
    "Retorne APENAS este JSON sem nenhum texto adicional:\n"
    "{\n"
    f'  "id": "{slug}",\n'
    '  "title": "TITULO_AQUI",\n'
    f'  "slug": "{slug}",\n'
    '  "excerpt": "RESUMO_AQUI",\n'
    '  "content": "CONTEUDO_AQUI",\n'
    f'  "category": "{category}",\n'
    '  "author": "O Codigo Aguia",\n'
    f'  "date": "{today}",\n'
    '  "readingTime": 6,\n'
    '  "featured": false,\n'
    '  "coverImage": "",\n'
    f'  "tags": {json.dumps(tags, ensure_ascii=False)}\n'
    "}"
)

# Modelos ordenados: mais confiáveis primeiro
MODELS = [
    "mistralai/mistral-small-3.2-24b-instruct:free",
    "google/gemma-4-31b-it:free",
    "mistralai/mistral-7b-instruct:free",
    "nvidia/nemotron-3-nano-30b-a3b:free",
]


def extrair_json(text):
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    cleaned = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except Exception:
        pass
    start = text.find("{")
    if start == -1:
        raise ValueError("Nenhum { encontrado.")
    depth, in_string, escape_next, end = 0, False, False, -1
    for i, ch in enumerate(text[start:], start):
        if escape_next:
            escape_next = False
            continue
        if ch == "\\" and in_string:
            escape_next = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end == -1:
        raise ValueError("JSON incompleto.")
    candidate = text[start:end]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON inválido: {e}\n{candidate[:400]}")


# Busca imagem
print(f"Buscando imagem para: {image_key}")
cover_image = buscar_imagem(image_key, unsplash_key)

# Gera post com IA
response_data = None
content = ""

for model in MODELS:
    print(f"Tentando modelo: {model}")
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.7,
        "max_tokens": 8000
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
            msg = data.get("choices", [{}])[0].get("message", {})
            content = msg.get("content") or ""
            if not content.strip():
                print(f"{model} retornou vazio, próximo...")
                continue
            content = content.strip()
            response_data = data
            print(f"Sucesso com {model} ({len(content)} chars)")
            break
    except urllib.error.HTTPError as e:
        print(f"{model} falhou: {e.code}")
        continue
    except Exception as e:
        print(f"{model} erro: {e}")
        continue

if not response_data or not content:
    print("Todos os modelos falharam.")
    sys.exit(1)

try:
    post = extrair_json(content)
except ValueError as e:
    print(f"Erro JSON: {e}")
    print(f"Bruto:\n{content[:800]}")
    sys.exit(1)

# Injeta CTAs e finaliza
post_content = post.get("content", "")
post_content = post_content.replace("<!--CTA_MEIO-->", EBOOK_CTA_MEIO)
post_content = post_content.replace("<!--CTA_FINAL-->", EBOOK_CTA_FINAL)
post["content"] = post_content
post["readingTime"] = max(1, round(len(post_content.split()) / 200))
post["author"] = "O Código Águia"
post["category"] = category
post["coverImage"] = cover_image

os.makedirs("public/blog-posts", exist_ok=True)
filepath = f"public/blog-posts/{slug}.json"
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(post, f, ensure_ascii=False, indent=2)

print(f"Post salvo: {filepath}")
print(f"Título: {post.get('title', 'sem título')}")
