import os, json

posts_dir = "public/blog-posts"
src_dir = "src/blog-posts"
os.makedirs(src_dir, exist_ok=True)

slugs = []
for fname in sorted(os.listdir(posts_dir)):
    if fname.endswith(".json") and fname != "manifest.json":
        slug = fname[:-5]
        src_path = os.path.join(src_dir, fname)
        pub_path = os.path.join(posts_dir, fname)
        # Copia o JSON para src/blog-posts/ para import.meta.glob funcionar
        with open(pub_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(src_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        slugs.append(slug)

manifest_path = os.path.join(posts_dir, "manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(slugs, f, ensure_ascii=False, indent=2)

print(f"Manifest atualizado: {len(slugs)} posts")
print(f"Posts copiados para src/blog-posts/: {slugs}")
