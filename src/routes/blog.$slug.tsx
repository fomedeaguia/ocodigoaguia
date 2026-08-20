import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { Nav } from "@/components/landing/Nav";
import { Footer } from "@/components/landing/Footer";
import { getPostBySlug, formatDate } from "@/data/blog";
import ReactMarkdown from "react-markdown";

export const Route = createFileRoute("/blog/$slug")({
  loader: ({ params }) => {
    const post = getPostBySlug(params.slug);
    if (!post) throw notFound();
    return { post };
  },
  head: ({ loaderData }) => {
    if (!loaderData) return { meta: [{ title: "Artigo não encontrado — O Código Águia" }] };
    const { post } = loaderData;
    return {
      meta: [
        { title: `${post.title} — Blog O Código Águia` },
        { name: "description", content: post.excerpt },
        { property: "og:title", content: post.title },
        { property: "og:image", content: post.coverImage ?? "" },
        { property: "og:type", content: "article" },
      ],
    };
  },
  component: BlogPostPage,
});

function BlogPostPage() {
  const { post } = Route.useLoaderData();

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Nav />
      <main className="flex-1 max-w-3xl mx-auto px-6 pt-32 pb-24">
        <Link to="/blog" className="text-xs uppercase tracking-[0.25em] text-gold hover:opacity-80">
          ← Voltar ao blog
        </Link>
        {post.coverImage && (
          <img src={post.coverImage} alt={post.title} className="mt-8 w-full rounded-xl object-cover max-h-72" />
        )}
        <div className="mt-8 flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-gold">
          <span>{post.category}</span>
          <span className="text-muted-foreground">{post.readingTime} min</span>
          <span className="text-muted-foreground">{formatDate(post.date)}</span>
        </div>
        <h1 className="mt-4 font-display text-3xl md:text-4xl leading-tight text-foreground">
          {post.title}
        </h1>
        <article className="mt-8 prose prose-invert prose-gold max-w-none">
          <ReactMarkdown
            components={{
              h2: ({ children }) => <h2 className="font-display text-2xl text-foreground mt-10 mb-4">{children}</h2>,
              p: ({ children }) => <p className="text-base leading-relaxed text-muted-foreground mb-5">{children}</p>,
              strong: ({ children }) => <strong className="text-foreground font-semibold">{children}</strong>,
              a: ({ href, children }) => (
                <a href={href} target="_blank" rel="noopener noreferrer" className="text-gold underline underline-offset-2 hover:opacity-80">
                  {children}
                </a>
              ),
              hr: () => <hr className="border-border/40 my-8" />,
            }}
          >
            {post.content}
          </ReactMarkdown>
        </article>
        <div className="mt-14 rounded-xl border border-gold/40 bg-card/40 p-8 text-center">
          <h2 className="font-display text-2xl text-foreground">Quer o sistema completo?</h2>
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
      <Footer />
    </div>
  );
}
