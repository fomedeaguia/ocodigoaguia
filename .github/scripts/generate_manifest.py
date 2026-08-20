import os, json, re

posts_dir = "public/blog-posts"
src_dir = "src/blog-posts"
os.makedirs(src_dir, exist_ok=True)

slugs = []
errors = []

for fname in sorted(os.listdir(posts_dir)):
    if not fname.endswith(".json") or fname == "manifest.json":
        continue

    slug = fname[:-5]
    pub_path = os.path.join(posts_dir, fname)

    # Lê o conteúdo bruto
    with open(pub_path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Tenta parsear normalmente
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON corrompido em {fname}: {e}")
        print(f"   Tentando reparar automaticamente...")

        # Estratégia de reparo: reescreve o campo "content" escapando corretamente
        try:
            # Extrai cada campo com regex para recompilar o objeto
            def extract_field(key, text):
                pattern = rf'"{key}"\s*:\s*"((?:[^"\\]|\\.)*)\"'
                m = re.search(pattern, text, re.DOTALL)
                return m.group(1) if m else None

            # Tenta um parse mais tolerante removendo caracteres de controle
            cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', raw)
            # Normaliza quebras de linha dentro de strings JSON
            # (problema comum: newlines literais dentro de strings)
            # Divide no campo content e re-escapa
            content_match = re.search(r'"content"\s*:\s*"(.*?)",\s*"category"', cleaned, re.DOTALL)
            if content_match:
                raw_content = content_match.group(1)
                safe_content = raw_content.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
                cleaned = cleaned[:content_match.start(1)] + safe_content + cleaned[content_match.end(1):]

            data = json.loads(cleaned)
            print(f"   ✅ Reparado com sucesso: {fname}")

            # Salva o arquivo reparado
            with open(pub_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

        except Exception as e2:
            print(f"   ❌ Não foi possível reparar {fname}: {e2}")
            errors.append(fname)
            continue  # pula este arquivo, não trava o manifest

    # Copia para src/blog-posts/
    src_path = os.path.join(src_dir, fname)
    with open(src_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    slugs.append(slug)
    print(f"✅ {fname}")

# Salva manifest
manifest_path = os.path.join(posts_dir, "manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(slugs, f, ensure_ascii=False, indent=2)

print(f"\nManifest atualizado: {len(slugs)} posts")
if errors:
    print(f"⚠️  Arquivos ignorados por erro irrecuperável: {errors}")
else:
    print("Todos os arquivos processados sem erros.")
