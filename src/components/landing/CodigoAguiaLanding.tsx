import { GoldButton } from "@/components/ui/gold-button";
import cover from "@/assets/codigo-aguia-cover.png";
import eagle from "@/assets/eagle-flight.jpg";
import author from "@/assets/author.jpg";
import { Nav } from "@/components/landing/Nav";
import {
  Brain, Target, Flame, Eye, Crown, TrendingUp, Shield, Compass,
  Zap, Mountain, Lock, Sparkles, ChevronDown, Check, X, Quote, Star,
} from "lucide-react";
import { useState } from "react";

const learnings = [
  { icon: Brain, title: "Mentalidade de Abundância", desc: "Reprograme crenças que travam sua riqueza." },
  { icon: Flame, title: "Disciplina de Alta Performance", desc: "Construa rotinas que separam águias de galinhas." },
  { icon: Target, title: "Foco Extremo", desc: "Mire onde poucos olham. Acerte o que poucos atingem." },
  { icon: TrendingUp, title: "Riqueza Digital", desc: "Métodos para construir renda na nova economia." },
  { icon: Crown, title: "Posicionamento Premium", desc: "Seja visto como autoridade desde o primeiro dia." },
  { icon: Compass, title: "Visão Estratégica", desc: "Pense em décadas, age em minutos." },
  { icon: Shield, title: "Resiliência Mental", desc: "Aja mesmo quando o medo gritar mais alto." },
  { icon: Zap, title: "Execução Implacável", desc: "Transforme intenção em resultado mensurável." },
  { icon: Mountain, title: "Construção de Autoridade", desc: "Edifique uma marca pessoal inabalável." },
];

const before = [
  "Mentalidade de escassez e medo",
  "Procrastinação e autossabotagem",
  "Falta de direção e propósito",
  "Vida no automático",
  "Foco disperso, energia drenada",
  "Baixa autoestima financeira",
];
const after = [
  "Mentalidade estratégica e expansiva",
  "Disciplina de elite, ação diária",
  "Clareza absoluta sobre seu próximo passo",
  "Vida intencional e desenhada",
  "Foco laser em alavancagem",
  "Identidade de quem constrói riqueza",
];

const quotes = [
  "A águia não voa com a multidão.",
  "O céu não é o limite. É apenas o começo.",
  "Quem domina a mente domina o destino.",
  "Riqueza começa na identidade.",
];

const faqs = [
  { q: "O eBook é para iniciantes?", a: "Sim. O Código Águia foi estruturado para guiar tanto quem está começando quanto quem já empreende e quer subir de nível." },
  { q: "Como recebo o acesso?", a: "Imediatamente após a confirmação do pagamento, no seu e-mail e na área de membros." },
  { q: "O conteúdo é digital?", a: "Sim. 100% digital, em PDF de alta qualidade, otimizado para leitura no celular, tablet e computador." },
  { q: "Posso ler pelo celular?", a: "Sim. O eBook foi desenhado mobile first, com tipografia confortável em qualquer tela." },
  { q: "Quanto tempo tenho acesso?", a: "Acesso vitalício. Compre uma vez, releia para sempre." },
  { q: "Existe garantia?", a: "Sim. 7 dias de garantia incondicional. Se não enxergar valor, devolvemos seu investimento." },
  { q: "Serve para quem ainda não empreende?", a: "Especialmente. O Código Águia constrói a base mental antes da execução." },
];

function FAQItem({ q, a }: { q: string; a: string }) {
  const [open, setOpen] = useState(false);
  return (
    <button
      onClick={() => setOpen(!open)}
      className="w-full text-left border border-border/60 rounded-lg p-6 bg-card/40 hover:border-gold/40 transition group"
    >
      <div className="flex items-center justify-between gap-4">
        <span className="font-display text-lg text-foreground group-hover:text-gold transition">{q}</span>
        <ChevronDown className={`w-5 h-5 text-gold shrink-0 transition-transform ${open ? "rotate-180" : ""}`} />
      </div>
      {open && <p className="mt-4 text-muted-foreground leading-relaxed">{a}</p>}
    </button>
  );
}

export function CodigoAguiaLanding() {
  return (
    <div id="top" className="min-h-screen bg-background text-foreground overflow-x-hidden">
      <Nav />

      {/* HERO */}
      <header className="relative pt-32 pb-20 lg:pt-44 lg:pb-32 overflow-hidden noise">
        <div className="absolute inset-0 bg-radial-gold opacity-60" />
        <div
          className="absolute inset-0 opacity-20 bg-cover bg-center"
          style={{ backgroundImage: `url(${eagle})` }}
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background/40 via-background/60 to-background" />

        <div className="relative max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
          <div className="animate-fade-up text-center lg:text-left">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-gold/30 bg-gold/5 mb-8">
              <Sparkles className="w-3.5 h-3.5 text-gold" />
              <span className="text-[10px] tracking-[0.3em] text-gold uppercase">Disciplina · Foco · Resiliência · Propósito</span>
            </div>
            <h1 className="font-display text-4xl sm:text-5xl lg:text-7xl leading-[1.05] mb-6">
              Você não nasceu para viver{" "}
              <span className="shimmer-gold">preso no cercado.</span>
            </h1>
            <p className="text-lg lg:text-xl text-muted-foreground max-w-xl mx-auto lg:mx-0 mb-10 leading-relaxed">
              Desenvolva a mentalidade, disciplina e visão estratégica para construir
              <span className="text-gold"> riqueza e liberdade </span>
              na era digital.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <a href="#oferta">
                <GoldButton size="lg">Quero Desbloquear o Código Águia</GoldButton>
              </a>
            </div>
            <p className="mt-6 text-xs tracking-widest text-muted-foreground uppercase">
              Acesso imediato · Garantia de 7 dias
            </p>
          </div>

          <div className="relative flex justify-center">
            <div className="absolute -inset-10 bg-radial-gold blur-3xl opacity-70" />
            <img
              src={cover}
              alt="Capa do eBook O Código Águia"
              width={520}
              height={780}
              className="relative w-[280px] sm:w-[340px] lg:w-[420px] rounded-md shadow-deep animate-float ring-gold"
              style={{ transform: "rotate(-4deg)" }}
            />
          </div>
        </div>
      </header>

      {/* REFLEXÃO */}
      <section className="relative py-24 lg:py-36 border-t border-border/40">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <p className="text-xs tracking-[0.4em] text-gold uppercase mb-6">A verdade que ninguém te conta</p>
          <h2 className="font-display text-3xl sm:text-5xl leading-tight mb-12">
            A maioria vive como galinha. <br />
            <span className="text-gold-gradient">Poucos aprendem a voar como águia.</span>
          </h2>
          <div className="grid sm:grid-cols-3 gap-6 text-left">
            {[
              "Você sente que merece mais — mas não sabe exatamente o que mudar.",
              "Tenta ser disciplinado, mas o medo e a procrastinação vencem.",
              "Vê outros decolando enquanto você ainda gira em círculos.",
            ].map((t, i) => (
              <div key={i} className="border border-border/60 rounded-lg p-6 bg-card/30">
                <Quote className="w-5 h-5 text-gold mb-3" />
                <p className="text-muted-foreground leading-relaxed">{t}</p>
              </div>
            ))}
          </div>
          <p className="mt-16 font-display text-2xl sm:text-3xl text-foreground/90">
            Seu maior inimigo não está lá fora. <span className="text-gold">Está dentro da sua mente.</span>
          </p>
        </div>
      </section>

      {/* APRESENTAÇÃO DO EBOOK */}
      <section className="relative py-24 lg:py-32 bg-gradient-dark border-y border-border/40">
        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
          <div className="relative flex justify-center order-2 lg:order-1">
            <div className="absolute -inset-8 bg-radial-gold blur-3xl opacity-60" />
            <img
              src={cover}
              alt="O Código Águia"
              loading="lazy"
              className="relative w-[260px] sm:w-[340px] rounded-md shadow-deep ring-gold"
            />
          </div>
          <div className="order-1 lg:order-2">
            <p className="text-xs tracking-[0.4em] text-gold uppercase mb-4">O que é</p>
            <h2 className="font-display text-3xl sm:text-5xl mb-6 leading-tight">
              Um sistema para construir <span className="text-gold-gradient">liberdade e prosperidade</span> na era digital.
            </h2>
            <p className="text-muted-foreground leading-relaxed mb-6 text-lg">
              O Código Águia não é mais um livro motivacional. É um manual estratégico
              para reprogramar sua mentalidade, instalar disciplina de elite e construir
              riqueza real através do empreendedorismo digital.
            </p>
            <ul className="space-y-3">
              {[
                "Sistema de transformação mental em 12 capítulos",
                "Estratégias práticas de execução diária",
                "Frameworks de posicionamento e autoridade",
                "Visão estratégica para construir patrimônio",
              ].map((it) => (
                <li key={it} className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-gold mt-0.5 shrink-0" />
                  <span className="text-foreground/90">{it}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* O QUE VOCÊ VAI APRENDER */}
      <section className="relative py-24 lg:py-32">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-16">
            <p className="text-xs tracking-[0.4em] text-gold uppercase mb-4">O que você vai dominar</p>
            <h2 className="font-display text-3xl sm:text-5xl">
              12 pilares de uma <span className="text-gold-gradient">mente vencedora</span>
            </h2>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {learnings.map(({ icon: Icon, title, desc }) => (
              <div
                key={title}
                className="group relative border border-border/60 rounded-xl p-8 bg-card/40 hover:border-gold/50 hover:bg-card/60 transition-all duration-500 hover:-translate-y-1"
              >
                <div className="w-12 h-12 rounded-lg bg-gradient-gold flex items-center justify-center mb-5 shadow-gold">
                  <Icon className="w-6 h-6 text-ink" />
                </div>
                <h3 className="font-display text-xl mb-2 text-foreground">{title}</h3>
                <p className="text-muted-foreground leading-relaxed">{desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ANTES E DEPOIS */}
      <section className="relative py-24 lg:py-32 bg-gradient-dark border-y border-border/40">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <p className="text-xs tracking-[0.4em] text-gold uppercase mb-4">A transformação</p>
            <h2 className="font-display text-3xl sm:text-5xl">
              Duas vidas. <span className="text-gold-gradient">Uma decisão.</span>
            </h2>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            <div className="border border-destructive/30 rounded-xl p-8 bg-destructive/5">
              <p className="text-xs tracking-[0.3em] text-destructive uppercase mb-6">Antes</p>
              <ul className="space-y-4">
                {before.map((b) => (
                  <li key={b} className="flex items-start gap-3">
                    <X className="w-5 h-5 text-destructive mt-0.5 shrink-0" />
                    <span className="text-muted-foreground">{b}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div className="border border-gold/40 rounded-xl p-8 bg-gold/5 glow-gold">
              <p className="text-xs tracking-[0.3em] text-gold uppercase mb-6">Depois do Código Águia</p>
              <ul className="space-y-4">
                {after.map((a) => (
                  <li key={a} className="flex items-start gap-3">
                    <Check className="w-5 h-5 text-gold mt-0.5 shrink-0" />
                    <span className="text-foreground/90">{a}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* FRASES DE IMPACTO */}
      <section className="relative py-24 lg:py-36 overflow-hidden">
        <div className="absolute inset-0 bg-radial-gold opacity-40" />
        <div className="relative max-w-5xl mx-auto px-6 space-y-16">
          {quotes.map((q, i) => (
            <p
              key={i}
              className="font-display text-3xl sm:text-5xl lg:text-6xl leading-tight text-center"
              style={{ textAlign: i % 2 === 0 ? "left" : "right" }}
            >
              <span className={i % 2 === 0 ? "text-gold-gradient" : "text-foreground"}>"{q}"</span>
            </p>
          ))}
        </div>
      </section>

      {/* AUTOR */}
      <section className="relative py-24 lg:py-32 bg-gradient-dark border-y border-border/40">
        <div className="max-w-6xl mx-auto px-6 grid md:grid-cols-[300px_1fr] gap-12 items-center">
          <div className="relative justify-self-center">
            <div className="absolute -inset-4 bg-radial-gold blur-2xl opacity-70" />
            <img
              src={author}
              alt="Autor de O Código Águia"
              loading="lazy"
              width={300}
              height={300}
              className="relative w-64 h-64 object-cover rounded-full ring-gold border border-gold/30"
            />
          </div>
          <div>
            <p className="text-xs tracking-[0.4em] text-gold uppercase mb-4">Sobre o autor</p>
            <h2 className="font-display text-3xl sm:text-4xl mb-6">
              Para quem decidiu <span className="text-gold-gradient">parar de ser média.</span>
            </h2>
            <p className="text-muted-foreground leading-relaxed mb-4 text-lg">
              Empreendedor digital, estrategista de mentalidade e estudioso da
              alta performance. Construiu sistemas que transformaram a vida de
              milhares de pessoas que decidiram romper o ciclo da escassez.
            </p>
            <p className="text-foreground/90 italic border-l-2 border-gold pl-4">
              "Escrevi este livro para quem está pronto para abandonar a vida
              comum. Se você chegou até aqui, você é um dos poucos."
            </p>
          </div>
        </div>
      </section>

      {/* OFERTA */}
      <section id="oferta" className="relative py-24 lg:py-32 overflow-hidden">
        <div className="absolute inset-0 bg-radial-gold opacity-50" />
        <div className="relative max-w-5xl mx-auto px-6">
          <div className="text-center mb-12">
            <p className="text-xs tracking-[0.4em] text-gold uppercase mb-4">Sua decisão</p>
            <h2 className="font-display text-4xl sm:text-6xl">
              Acesso ao <span className="text-gold-gradient">Código Águia</span>
            </h2>
          </div>

          <div className="relative border border-gold/40 rounded-2xl bg-card/70 backdrop-blur p-8 sm:p-12 shadow-deep glow-gold">
            <div className="grid md:grid-cols-[260px_1fr] gap-10 items-center">
              <img src={cover} alt="" loading="lazy" className="w-full max-w-[240px] mx-auto rounded-md shadow-deep ring-gold" />
              <div>
                <div className="flex items-center gap-2 mb-3">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 fill-gold text-gold" />
                  ))}
                  <span className="text-xs text-muted-foreground ml-2">Leitores transformados</span>
                </div>
                <h3 className="font-display text-2xl sm:text-3xl mb-4">
                  eBook Completo + Bônus Exclusivos
                </h3>
                <ul className="space-y-2 mb-8">
                  {[
                    "eBook digital em PDF premium",
                    "Acesso vitalício e atualizações",
                    "Bônus: Protocolo de Disciplina 30 dias",
                    "Bônus: Frameworks de Posicionamento",
                  ].map((b) => (
                    <li key={b} className="flex items-center gap-2 text-foreground/90">
                      <Check className="w-4 h-4 text-gold" /> {b}
                    </li>
                  ))}
                </ul>

                <div className="flex items-baseline gap-3 mb-2">
                  <span className="text-muted-foreground line-through">De R$ 97,00 por</span>
                </div>
                <div className="flex items-baseline gap-2 mb-6">
                  <span className="text-gold text-2xl">R$</span>
                  <span className="font-display text-6xl text-gold-gradient">27</span>
                  <span className="text-muted-foreground">,00 à vista</span>
                </div>

                <GoldButton size="lg" className="w-full">
                  Quero Acessar o Código Águia Agora
                </GoldButton>
                <div className="mt-4 flex items-center justify-center gap-4 text-xs text-muted-foreground">
                  <span className="flex items-center gap-1"><Lock className="w-3 h-3" /> Compra 100% segura</span>
                  <span className="flex items-center gap-1"><Shield className="w-3 h-3" /> Garantia de 7 dias</span>
                </div>
              </div>
            </div>
          </div>

          <p className="text-center mt-10 font-display text-xl sm:text-2xl text-foreground/80">
            Quanto mais você adia, <span className="text-gold">mais distante fica da liberdade.</span>
          </p>
        </div>
      </section>

      {/* GARANTIA */}
      <section className="relative py-20 border-y border-border/40">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <div className="inline-flex w-24 h-24 rounded-full bg-gradient-gold items-center justify-center mb-6 shadow-gold">
            <Shield className="w-12 h-12 text-ink" />
          </div>
          <h2 className="font-display text-3xl sm:text-4xl mb-4">
            Garantia incondicional de <span className="text-gold-gradient">7 dias</span>
          </h2>
          <p className="text-muted-foreground leading-relaxed">
            Leia o eBook, aplique os ensinamentos e, se sentir que o conteúdo
            não agrega valor à sua evolução, devolvemos 100% do seu investimento.
            Sem perguntas. Sem burocracia.
          </p>
        </div>
      </section>

      {/* FAQ */}
      <section className="relative py-24 lg:py-32">
        <div className="max-w-3xl mx-auto px-6">
          <div className="text-center mb-12">
            <p className="text-xs tracking-[0.4em] text-gold uppercase mb-4">Perguntas frequentes</p>
            <h2 className="font-display text-3xl sm:text-5xl">Ainda em dúvida?</h2>
          </div>
          <div className="space-y-4">
            {faqs.map((f) => (
              <FAQItem key={f.q} q={f.q} a={f.a} />
            ))}
          </div>
        </div>
      </section>

      {/* CTA FINAL */}
      <section className="relative py-32 overflow-hidden border-t border-border/40">
        <div
          className="absolute inset-0 opacity-25 bg-cover bg-center"
          style={{ backgroundImage: `url(${eagle})` }}
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background via-background/70 to-background" />
        <div className="relative max-w-4xl mx-auto px-6 text-center">
          <h2 className="font-display text-4xl sm:text-6xl lg:text-7xl leading-[1.05] mb-8">
            Você pode continuar limitado pelas mesmas crenças…<br />
            <span className="text-gold-gradient">ou decidir abrir as asas.</span>
          </h2>
          <p className="text-xl text-muted-foreground mb-12">
            O próximo nível da sua vida começa com uma decisão.
          </p>
          <a href="#oferta">
            <GoldButton size="lg" className="text-base px-12 py-6">
              Quero Voar Mais Alto
            </GoldButton>
          </a>
          <p className="mt-10 text-xs tracking-[0.4em] text-muted-foreground uppercase">
            Poucos entendem · Poucos aceitam · Poucos chegam
          </p>
        </div>
      </section>

      <footer className="border-t border-border/40 py-10">
        <div className="max-w-6xl mx-auto px-6 flex flex-col sm:flex-row justify-between gap-4 text-xs text-muted-foreground">
          <span>© {new Date().getFullYear()} O Código Águia. Todos os direitos reservados.</span>
          <span>Disciplina · Foco · Resiliência · Propósito</span>
        </div>
      </footer>
    </div>
  );
}
