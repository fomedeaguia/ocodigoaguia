export function Footer() {
  return (
    <footer className="border-t border-border/40 bg-background">
      <div className="max-w-5xl mx-auto px-6 py-10 flex flex-col items-center gap-6">
        <p className="font-display text-lg text-gold tracking-wide">O Código Águia</p>
        <div className="flex flex-wrap justify-center gap-6 text-sm text-muted-foreground">
          <a href="https://x.com/fomedeaguia" target="_blank" rel="noopener noreferrer" className="hover:text-gold transition-colors">X / Twitter</a>
          <a href="https://www.instagram.com/fomedeaguia/" target="_blank" rel="noopener noreferrer" className="hover:text-gold transition-colors">Instagram</a>
          <a href="https://www.youtube.com/@fomedeaguia" target="_blank" rel="noopener noreferrer" className="hover:text-gold transition-colors">YouTube</a>
          <a href="https://www.tiktok.com/@fomedeaguia" target="_blank" rel="noopener noreferrer" className="hover:text-gold transition-colors">TikTok</a>
        </div>
        <p className="text-[10px] uppercase tracking-widest text-muted-foreground">
          &copy; {new Date().getFullYear()} O Código Águia
        </p>
      </div>
    </footer>
  );
}
