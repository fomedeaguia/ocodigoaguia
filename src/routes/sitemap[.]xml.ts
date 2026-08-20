import { createAPIFileRoute } from "@tanstack/react-start/api";
import { blogPosts } from "@/data/blog";

const BASE_URL = "https://ocodigoaguia.pages.dev";

function escapeXml(str: string) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

export const APIRoute = createAPIFileRoute("/sitemap.xml")({
  GET: () => {
    const staticPages = [
      { url: "/", priority: "1.0", changefreq: "weekly" },
      { url: "/blog", priority: "0.9", changefreq: "daily" },
    ];

    const postPages = blogPosts.map((post) => ({
      url: `/blog/${escapeXml(post.slug)}`,
      priority: "0.8",
      changefreq: "monthly",
      lastmod: post.date,
    }));

    const allPages = [...staticPages, ...postPages];

    const urlEntries = allPages
      .map((page) => {
        const lastmodTag = page.lastmod
          ? `\n    <lastmod>${page.lastmod}</lastmod>`
          : "";
        return `  <url>\n    <loc>${BASE_URL}${page.url}</loc>${lastmodTag}\n    <changefreq>${page.changefreq}</changefreq>\n    <priority>${page.priority}</priority>\n  </url>`;
      })
      .join("\n");

    const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n  xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9\n  http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n${urlEntries}\n</urlset>`;

    return new Response(xml, {
      headers: {
        "Content-Type": "application/xml; charset=utf-8",
        "Cache-Control": "public, max-age=3600, s-maxage=3600",
      },
    });
  },
});
