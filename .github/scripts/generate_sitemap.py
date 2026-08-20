"""Gera public/sitemap.xml com todas as páginas + posts do blog."""
import os, json, glob
from datetime import datetime, timezone

BASE_URL = "https://ocodigoaguia.com.br"
posts_dir = "public/blog-posts"
json_files = glob.glob(f"{posts_dir}/post-*.json")
now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

STATIC_PAGES = [
    {"loc": "/", "changefreq": "daily", "priority": "1.0"},
    {"loc": "/blog", "changefreq": "daily", "priority": "0.9"},
    {"loc": "/ebook", "changefreq": "weekly", "priority": "0.8"},
]

urls = []
for page in STATIC_PAGES:
    urls.append(
        f"  <url>\n"
        f"    <loc>{BASE_URL}{page['loc']}</loc>\n"
        f"    <lastmod>{now}</lastmod>\n"
        f"    <changefreq>{page['changefreq']}</changefreq>\n"
        f"    <priority>{page['priority']}</priority>\n"
        f"  </url>"
    )

for jf in sorted(json_files, reverse=True):
    try:
        with open(jf, encoding="utf-8") as f:
            post = json.load(f)
        slug = post.get("slug", os.path.splitext(os.path.basename(jf))[0])
        date = post.get("date", now)
        urls.append(
            f"  <url>\n"
            f"    <loc>{BASE_URL}/blog/{slug}</loc>\n"
            f"    <lastmod>{date}</lastmod>\n"
            f"    <changefreq>weekly</changefreq>\n"
            f"    <priority>0.7</priority>\n"
            f"  </url>"
        )
    except Exception as e:
        print(f"Erro ao processar {jf}: {e}")

sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls) +
    "\n</urlset>"
)

os.makedirs("public", exist_ok=True)
with open("public/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"Sitemap gerado com {len(urls)} URLs em public/sitemap.xml")
