import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import ReactMarkdown from "react-markdown";
import { Nav } from "@/components/landing/Nav";
import { Footer } from "@/components/landing/Footer";
import { getPostBySlug, formatDate } from "@/data/blog";

export const Route = createFileRoute("/blog/$slug")({
  component: BlogPost,
  head: ({ params }) => {
    const post = getPostBySlug(params.slug);
    if (!post) return { meta: [{ title: "Post não encontrado" }] };
    return {
      meta: [
        { title: `${post.title} | O Código Águia` },
        { name: "description", content: post.excerpt },
        { property: "og:title", content: post.title },
        { property: "og:description", content: post.excerpt },
        { property: "og:type", content: "article" },
        ...(post.coverImage ? [{ property: "og:image", content: post.coverImage }] : []),
        { name: "twitter:card", content: "summary_large_image" },
        { name: "twitter:title", content: post.title },
        { name: "twitter:description", content: post.excerpt },
        ...(post.coverImage ? [{ name: "twitter:image", content: post.coverImage }] : []),
      ],
    };
  },
  loader: ({ params }) => {
    const post = getPostBySlug(params.slug);
    if (!post) throw notFound();
    return post;
  },
});

function BlogPost() {
  const post = Route.useLoaderData();

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Nav />
      <main className="flex-1 max-w-3xl mx-auto px-6 pt-32 pb-24">
        <Link
          to="/blog/"
          className="text-xs uppercase tracking-widest text-muted-foreground hover:text-gold transition-colors"
        >
          ← Blog
        </Link>

        <div className="mt-8 flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-gold">
          <span>{post.category}</span>
          <span className="text-muted-foreground">{post.readingTime} min de leitura</span>
        </div>

        <h1 className="mt-4 font-display text-4xl md:text-5xl text-foreground leading-tight">
          {post.title}
        </h1>

        <p className="mt-3 text-sm text-muted-foreground">{formatDate(post.date)}</p>

        {post.coverImage && (
          <img
            src={post.coverImage}
            alt={post.title}
            className="mt-8 w-full rounded-xl object-cover max-h-96"
          />
        )}

        <article className="mt-10 prose prose-invert prose-gold max-w-none">
          <ReactMarkdown>{post.content}</ReactMarkdown>
        </article>

        {post.tags && post.tags.length > 0 && (
          <div className="mt-12 flex flex-wrap gap-2">
            {post.tags.map((tag) => (
              <span
                key={tag}
                className="px-3 py-1 rounded-full border border-border/60 text-xs text-muted-foreground"
              >
                {tag}
              </span>
            ))}
          </div>
        )}

        <div className="mt-12">
          <Link
            to="/blog/"
            className="text-sm text-gold hover:underline"
          >
            ← Ver todos os artigos
          </Link>
        </div>
      </main>
      <Footer />
    </div>
  );
}
