/**
 * Generates public/sitemap.xml from src/data/blog.ts
 * Run manually: node scripts/generate-sitemap.mjs
 * Also triggered automatically by GitHub Actions on every push that changes blog.ts
 */
import { readFileSync, writeFileSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const BASE_URL = "https://ocodigoaguia.com.br";
const TODAY = new Date().toISOString().split("T")[0];

// Parse slugs + dates directly from blog.ts source (no TS compilation needed)
const blogSrc = readFileSync(
  resolve(__dirname, "../src/data/blog.ts"),
  "utf-8"
);

const slugMatches = [...blogSrc.matchAll(/slug:\s*["']([^"']+)["']/g)];
const dateMatches = [...blogSrc.matchAll(/date:\s*["']([\d-]+)["']/g)];

const posts = slugMatches.map((m, i) => ({
  slug: m[1],
  date: dateMatches[i]?.[1] ?? TODAY,
}));

const staticPages = [
  { loc: "/", lastmod: TODAY, changefreq: "weekly", priority: "1.0" },
  { loc: "/blog", lastmod: TODAY, changefreq: "daily", priority: "0.9" },
];

const postPages = posts.map((p) => ({
  loc: `/blog/${p.slug}`,
  lastmod: p.date,
  changefreq: "monthly",
  priority: "0.8",
}));

const allPages = [...staticPages, ...postPages];

const urlEntries = allPages
  .map(
    (p) => `  <url>
    <loc>${BASE_URL}${p.loc}</loc>
    <lastmod>${p.lastmod}</lastmod>
    <changefreq>${p.changefreq}</changefreq>
    <priority>${p.priority}</priority>
  </url>`
  )
  .join("\n");

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
  http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
${urlEntries}
</urlset>
`;

const outPath = resolve(__dirname, "../public/sitemap.xml");
writeFileSync(outPath, xml, "utf-8");
console.log(`✅ sitemap.xml gerado com ${posts.length} posts → ${outPath}`);
