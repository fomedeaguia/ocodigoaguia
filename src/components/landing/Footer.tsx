export function Footer() {
  return (
    <footer className="border-t border-border/40 py-10 text-center text-xs text-muted-foreground">
      <div className="flex justify-center gap-6 mb-4">
        <a
          href="https://x.com/ocodigoaguia"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-gold transition-colors"
        >
          X / Twitter
        </a>
        <a
          href="https://instagram.com/ocodigoaguia"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-gold transition-colors"
        >
          Instagram
        </a>
        <a
          href="https://youtube.com/@ocodigoaguia"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-gold transition-colors"
        >
          YouTube
        </a>
        <a
          href="https://tiktok.com/@ocodigoaguia"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-gold transition-colors"
        >
          TikTok
        </a>
      </div>
      <p>© {new Date().getFullYear()} O Código Águia. Todos os direitos reservados.</p>
    </footer>
  );
}
