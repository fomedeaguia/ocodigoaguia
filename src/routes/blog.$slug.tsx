import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { Nav } from "@/components/landing/Nav";
import { Footer } from "@/components/landing/Footer";
import { getPostBySlug, formatDate } from "@/data/blog";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const BASE_URL = "https://ocodigoaguia.com.br";

export const Route = createFileRoute("/blog/$slug")({
  loader: ({ params }) => {
    const post = getPostBySlug(params.slug);
    if (!post) throw notFound();
    return { post };
  },
  head: ({ loaderData }) => {
    if (!loaderData) return { meta: [{ title: "Artigo não encontrado — O Código Águia" }] };
    const { post } = loaderData;
    const canonicalUrl = `${BASE_URL}/blog/${post.slug}`;
    return {
      meta: [
        { title: `${post.title} — Blog O Código Águia` },
        { name: "description", content: post.excerpt },
        { property: "og:title", content: post.title },
        { property: "og:description", content: post.excerpt },
        { property: "og:image", content: post.coverImage ?? "" },
        { property: "og:type", content: "article" },
        { property: "og:url", content: canonicalUrl },
        { name: "twitter:card", content: "summary_large_image" },
        { name: "twitter:title", content: post.title },
        { name: "twitter:description", content: post.excerpt },
        { name: "twitter:image", content: post.coverImage ?? "" },
        { tagName: "link", rel: "canonical", href: canonicalUrl },
      ],
    };
  },
  component: BlogPostPage,
});

function BlogPostPage() {
  const { post } = Route.useLoaderData();
  const canonicalUrl = `${BASE_URL}/blog/${post.slug}`;

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: post.title,
    description: post.excerpt,
    image: post.coverImage ?? "",
    datePublished: post.date,
    url: canonicalUrl,
    author: {
      "@type": "Organization",
      name: "O Código Águia",
      url: BASE_URL,
    },
    publisher: {
      "@type": "Organization",
      name: "O Código Águia",
      url: BASE_URL,
    },
  };

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Nav />
      <main className="flex-1 max-w-3xl mx-auto px-6 pt-32 pb-24">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
        {/* Breadcrumb */}
        <nav aria-label="Navegação" className="flex items-center gap-2 text-xs uppercase tracking-[0.25em]">
          <Link to="/" className="text-muted-foreground hover:text-gold transition-colors">Início</Link>
          <span className="text-muted-foreground/40">›</span>
          <Link to="/blog" className="text-muted-foreground hover:text-gold transition-colors">Blog</Link>
          <span className="text-muted-foreground/40">›</span>
          <span className="text-gold truncate max-w-[200px]">{post.category}</span>
        </nav>

        {post.coverImage && (
          <img
            src={post.coverImage}
            alt={post.title}
            className="mt-8 w-full rounded-xl object-cover max-h-72"
          />
        )}

        <div className="mt-8 flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-gold">
          <span>{post.category}</span>
          <span className="text-muted-foreground">·</span>
          <span className="text-muted-foreground">{post.readingTime} min de leitura</span>
          <span className="text-muted-foreground">·</span>
          <span className="text-muted-foreground">{formatDate(post.date)}</span>
        </div>

        <h1 className="mt-4 font-display text-3xl md:text-4xl leading-tight text-foreground">
          {post.title}
        </h1>

        <p className="mt-4 text-base text-muted-foreground leading-relaxed border-l-2 border-gold/40 pl-4 italic">
          {post.excerpt}
        </p>

        {/* Conteúdo do artigo com estilos explícitos — sem depender do plugin @tailwindcss/typography */}
        <article className="mt-10 space-y-0">
          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
              h2: ({ children }) => (
                <h2 className="font-display text-2xl text-foreground mt-12 mb-4 leading-snug">
                  {children}
                </h2>
              ),
              h3: ({ children }) => (
                <h3 className="font-display text-xl text-foreground mt-8 mb-3 leading-snug">
                  {children}
                </h3>
              ),
              p: ({ children }) => (
                <p className="text-base leading-[1.85] text-muted-foreground mb-6">
                  {children}
                </p>
              ),
              strong: ({ children }) => (
                <strong className="text-foreground font-semibold">{children}</strong>
              ),
              em: ({ children }) => (
                <em className="text-foreground/80 italic">{children}</em>
              ),
              a: ({ href, children }) => (
                <a
                  href={href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gold underline underline-offset-2 hover:opacity-80 transition-opacity"
                >
                  {children}
                </a>
              ),
              hr: () => (
                <hr className="border-border/40 my-10" />
              ),
              ul: ({ children }) => (
                <ul className="space-y-2 mb-6 pl-5 list-disc marker:text-gold">
                  {children}
                </ul>
              ),
              ol: ({ children }) => (
                <ol className="space-y-2 mb-6 pl-5 list-decimal marker:text-gold">
                  {children}
                </ol>
              ),
              li: ({ children }) => (
                <li className="text-base leading-relaxed text-muted-foreground">
                  {children}
                </li>
              ),
              blockquote: ({ children }) => (
                <blockquote className="border-l-2 border-gold/60 pl-5 my-6 italic text-foreground/80">
                  {children}
                </blockquote>
              ),
              // Bloco de código cercado por ``` — renderiza o texto interno como parágrafo normal
              // evitando que conteúdo acidentalmente envolvido em backticks apareça desformatado
              pre: ({ children }) => (
                <div className="text-base leading-[1.85] text-muted-foreground mb-6">
                  {children}
                </div>
              ),
              code: ({ inline, children }: { inline?: boolean; children?: React.ReactNode }) =>
                inline ? (
                  <code className="bg-card/60 text-gold text-sm px-1.5 py-0.5 rounded font-mono">
                    {children}
                  </code>
                ) : (
                  // Bloco de código (triple backtick): exibe o conteúdo como texto normal
                  // para não quebrar posts de blog que usam backticks por engano
                  <span className="text-base leading-[1.85] text-muted-foreground whitespace-pre-wrap">
                    {children}
                  </span>
                ),
            }}
          >
            {post.content}
          </ReactMarkdown>
        </article>

        {/* CTA ao final do artigo */}
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

        {/* Voltar ao blog */}
        <div className="mt-10 text-center">
          <Link
            to="/blog"
            className="text-xs uppercase tracking-[0.25em] text-muted-foreground hover:text-gold transition-colors"
          >
            ← Voltar ao blog
          </Link>
        </div>
      </main>
      <Footer />
    </div>
  );
}
