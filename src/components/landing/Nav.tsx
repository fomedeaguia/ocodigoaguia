export function Nav() {
  return (
    <nav className="fixed top-0 inset-x-0 z-50 backdrop-blur-md bg-background/70 border-b border-border/40">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <a href="#top" className="flex items-center gap-2">
          <svg viewBox="0 0 24 24" className="w-6 h-6 text-gold" fill="currentColor">
            <path d="M12 2l3 6 6 1-4.5 4 1 6-5.5-3-5.5 3 1-6L3 9l6-1z" />
          </svg>
          <span className="font-display text-sm tracking-[0.3em] text-gold">CÓDIGO ÁGUIA</span>
        </a>
        <a
          href="#oferta"
          className="hidden sm:inline-flex text-xs uppercase tracking-widest font-semibold px-5 py-2.5 rounded-md bg-gradient-gold text-ink hover:opacity-90 transition"
        >
          Garantir Acesso
        </a>
      </div>
    </nav>
  );
}
