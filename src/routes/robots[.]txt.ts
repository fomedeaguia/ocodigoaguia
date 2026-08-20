import { createAPIFileRoute } from "@tanstack/react-start/api";

const BASE_URL = "https://ocodigoaguia.pages.dev";

export const APIRoute = createAPIFileRoute("/robots.txt")({
  GET: () => {
    const content = `User-agent: *
Allow: /

Sitemap: ${BASE_URL}/sitemap.xml
`;

    return new Response(content, {
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "Cache-Control": "public, max-age=86400",
      },
    });
  },
});
