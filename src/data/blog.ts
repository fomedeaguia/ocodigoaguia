export type BlogPost = {
  id: string;
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readingTime: number;
  category: string;
  content: string;
  coverImage?: string;
  tags?: string[];
  author?: string;
  featured?: boolean;
};

// Carrega apenas os JSONs dinâmicos de public/blog-posts/
function loadDynamicPosts(): BlogPost[] {
  try {
    const modules = import.meta.glob("/public/blog-posts/*.json", {
      eager: true,
    }) as Record<string, BlogPost>;
    return Object.values(modules)
      .filter((post) => !!post?.slug && !!post?.title && !!post?.date)
      .map((post) => ({
        ...post,
        readingTime: post.readingTime ?? 5,
      }));
  } catch {
    return [];
  }
}

export const blogPosts: BlogPost[] = loadDynamicPosts().sort(
  (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()
);

export function getPostBySlug(slug: string): BlogPost | undefined {
  return blogPosts.find((post) => post.slug === slug);
}

export function formatDate(iso: string): string {
  if (!iso) return "";
  const d = new Date(iso.length === 10 ? iso + "T12:00:00Z" : iso);
  if (isNaN(d.getTime())) return "";
  return d.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  });
}
