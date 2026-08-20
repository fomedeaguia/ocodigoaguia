import { createFileRoute, Link } from "@tanstack/react-router";
import { Nav } from "@/components/landing/Nav";
import { Footer } from "@/components/landing/Footer";
import { blogPosts, formatDate } from "@/data/blog";

export const Route = createFileRoute("/blog/")({
  component: BlogIndex,
  head: () => ({
    meta: [
      { title: "Blog — O Código Águia | Mentalidade, Disciplina e Riqueza" },
      {
        name: "description",
        content:
          "Artigos sobre mentalidade de águia, disciplina, rotina de alta performance e construção de renda na era digital.",
      },
      { property: "og:title", content: "Blog — O Código Águia" },
      {
        property: "og:description",
        content: "Conteúdo sobre mentalidade, disciplina e liberdade financeira na era digital.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary" },
      { name: "twitter:title", content: "Blog — O Código Águia" },
      {
        name: "twitter:description",
        content: "Conteúdo sobre mentalidade, disciplina e liberdade financeira na era digital.",
      },
    ],
  }),
});

function BlogIndex() {
  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Nav />
      <main className="flex-1 max-w-5xl mx-auto px-6 pt-32 pb-24">
        <p className="text-xs uppercase tracking-[0.35em] text-gold">Blog</p>
        <h1 className="mt-4 font-display text-4xl md:text-5xl text-foreground">
          Conteúdo para quem decidiu voar alto
        </h1>
        <p className="mt-4 max-w-2xl text-muted-foreground">
          Mentalidade, disciplina, estratégia e execução — artigos práticos para transformar visão
          em resultado na era digital.
        </p>

        <div className="mt-14 grid gap-6 md:grid-cols-2">
          {blogPosts.map((post) => (
            <Link
              key={post.slug}
              to="/blog/$slug"
              params={{ slug: post.slug }}
              className="group rounded-xl border border-border/60 bg-card/40 p-6 transition hover:border-gold/60"
            >
              {post.coverImage && (
                <img
                  src={post.coverImage}
                  alt={post.title}
                  className="w-full rounded-lg object-cover max-h-40 mb-4"
                />
              )}
              <div className="flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-gold">
                <span>{post.category}</span>
                <span className="text-muted-foreground">{post.readingTime} min</span>
              </div>
              <h2 className="mt-4 font-display text-2xl text-foreground group-hover:text-gold transition-colors">
                {post.title}
              </h2>
              <p className="mt-3 text-sm text-muted-foreground">{post.excerpt}</p>
              <p className="mt-5 text-xs text-muted-foreground">{formatDate(post.date)}</p>
            </Link>
          ))}
        </div>
      </main>
      <Footer />
    </div>
  );
}
