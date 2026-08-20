import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { Nav } from "@/components/landing/Nav";
import { getPostBySlug, formatDate } from "@/data/blog";

export const Route = createFileRoute("/blog/$slug")({
  loader: ({ params }) => {
    const post = getPostBySlug(params.slug);
    if (!post) throw notFound();
    return { post };
  },
  head: ({ loaderData }) => {
    if (!loaderData) {
      return {
        meta: [{ title: "Artigo não encontrado — O Código Águia" }, { name: "robots", content: "noindex" }],
      };
    }
    const { post } = loaderData;
    return {
      meta: [
        { title: `${post.title} — Blog O Código Águia` },
        { name: "description", content: post.excerpt },
        { property: "og:title", content: post.title },
        { property: "og:description", content: post.excerpt },
        { property: "og:type", content: "article" },
        { name: "twitter:card", content: "summary" },
        { name: "twitter:title", content: post.title },
        { name: "twitter:description", content: post.excerpt },
      ],
    };
  },
  component: BlogPost,
});

function BlogPost() {
  const { post } = Route.useLoaderData();

  return (
    <div className="min-h-screen bg-background">
      <Nav />
      <main className="max-w-3xl mx-auto px-6 pt-32 pb-24">
        <Link to="/blog" className="text-xs uppercase tracking-[0.25em] text-gold hover:opacity-80">
          ← Voltar ao blog
        </Link>
        <div className="mt-8 flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-gold">
          <span>{post.category}</span>
          <span className="text-muted-foreground">{post.readTime}</span>
          <span className="text-muted-foreground">{formatDate(post.date)}</span>
        </div>
        <h1 className="mt-4 font-display text-3xl md:text-4xl leading-tight text-foreground">
          {post.title}
        </h1>
        <article className="mt-8 space-y-5">
          {post.content.map((paragraph, i) => (
            <p key={i} className="text-base leading-relaxed text-muted-foreground">
              {paragraph}
            </p>
          ))}
        </article>

        <div className="mt-14 rounded-xl border border-gold/40 bg-card/40 p-8 text-center">
          <h2 className="font-display text-2xl text-foreground">
            Quer o sistema completo?
          </h2>
          <p className="mt-3 text-sm text-muted-foreground">
            O eBook O Código Águia reúne mentalidade, disciplina e estratégia em um único método.
          </p>
          <a
            href="https://pay.kiwify.com.br/cYxU5fc"
            className="mt-6 inline-flex text-xs uppercase tracking-widest font-semibold px-6 py-3 rounded-md bg-gradient-gold text-ink hover:opacity-90 transition"
          >
            Garantir meu acesso
          </a>
        </div>
      </main>
    </div>
  );
}
