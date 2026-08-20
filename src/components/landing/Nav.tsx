import { useState } from "react";
import { Link } from "@tanstack/react-router";
import { Menu, X } from "lucide-react";

const links = [
  { label: "Início", to: "/", hash: "top" },
  { label: "O Livro", to: "/", hash: "pilares" },
  { label: "Blog", to: "/blog" },
  { label: "FAQ", to: "/", hash: "faq" },
];

export function Nav() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="fixed top-0 inset-x-0 z-50 backdrop-blur-md bg-background/70 border-b border-border/40">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2">
          <svg viewBox="0 0 24 24" className="w-6 h-6 text-gold" fill="currentColor">
            <path d="M12 2l3 6 6 1-4.5 4 1 6-5.5-3-5.5 3 1-6L3 9l6-1z" />
          </svg>
          <span className="font-display text-sm tracking-[0.3em] text-gold">CÓDIGO ÁGUIA</span>
        </Link>

        <div className="hidden md:flex items-center gap-8">
          {links.map((link) => (
            <Link
              key={link.label}
              to={link.to}
              hash={link.hash}
              className="text-xs uppercase tracking-[0.2em] text-muted-foreground hover:text-gold transition-colors"
              activeProps={{ className: "text-gold" }}
              activeOptions={{ exact: true }}
            >
              {link.label}
            </Link>
          ))}
          <Link
            to="/"
            hash="oferta"
            className="inline-flex text-xs uppercase tracking-widest font-semibold px-5 py-2.5 rounded-md bg-gradient-gold text-ink hover:opacity-90 transition"
          >
            Garantir Acesso
          </Link>
        </div>

        <button
          type="button"
          aria-label={open ? "Fechar menu" : "Abrir menu"}
          onClick={() => setOpen((v) => !v)}
          className="md:hidden text-gold p-2"
        >
          {open ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
        </button>
      </div>

      {open && (
        <div className="md:hidden border-t border-border/40 bg-background/95 px-6 py-4 flex flex-col gap-4">
          {links.map((link) => (
            <Link
              key={link.label}
              to={link.to}
              hash={link.hash}
              onClick={() => setOpen(false)}
              className="text-xs uppercase tracking-[0.2em] text-muted-foreground hover:text-gold transition-colors"
            >
              {link.label}
            </Link>
          ))}
          <Link
            to="/"
            hash="oferta"
            onClick={() => setOpen(false)}
            className="inline-flex justify-center text-xs uppercase tracking-widest font-semibold px-5 py-2.5 rounded-md bg-gradient-gold text-ink"
          >
            Garantir Acesso
          </Link>
        </div>
      )}
    </nav>
  );
}
