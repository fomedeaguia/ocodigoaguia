export type BlogPost = {
  id: string;
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readingTime: number;
  category: string;
  content: string;
  coverImage?: string;
  tags?: string[];
  author?: string;
  featured?: boolean;
};

const staticPosts: BlogPost[] = [
  {
    id: "mentalidade-de-aguia",
    slug: "mentalidade-de-aguia",
    title: "Mentalidade de águia: como parar de viver no cercado",
    excerpt: "A diferença entre quem prospera e quem estagna raramente é talento. É altitude mental. Entenda como treinar a visão de águia no dia a dia.",
    date: "2026-08-12",
    readingTime: 6,
    category: "Mentalidade",
    content: [
      "A galinha vive olhando para o chão. A águia vive olhando para o horizonte. Ambas têm asas — só uma decide usá-las.",
      "No mundo digital isso se traduz em foco: enquanto a maioria consome conteúdo, a minoria constrói ativos.",
      "Treinar a mentalidade de águia começa com três decisões diárias: escolher o que merece sua atenção, eliminar o que rouba sua energia e proteger o bloco de tempo em que você cria.",
      "Não é motivação. É arquitetura.",
    ].join("\n\n"),
  },
  {
    id: "disciplina-supera-motivacao",
    slug: "disciplina-supera-motivacao",
    title: "Por que disciplina vence motivação todos os dias",
    excerpt: "Motivação é clima, disciplina é estrutura. Um sistema simples para executar mesmo nos dias em que a vontade não aparece.",
    date: "2026-08-05",
    readingTime: 5,
    category: "Disciplina",
    content: [
      "Motivação é uma emoção — e emoções oscilam. Disciplina é um contrato que você assina com o seu futuro.",
      "O sistema mais eficaz é o mais chato: mesma hora, mesmo lugar, mesma primeira tarefa.",
      "Comece com o mínimo inegociável: 45 minutos por dia de trabalho profundo no seu projeto principal.",
      "Ao final de 90 dias, o resultado não vem do dia heroíco. Vem dos 90 dias comuns.",
    ].join("\n\n"),
  },
  {
    id: "primeiros-passos-era-digital",
    slug: "primeiros-passos-era-digital",
    title: "Primeiros passos para construir renda na era digital",
    excerpt: "Sem fórmula mágica: um caminho realista para sair do zero, validar uma oferta e transformar conhecimento em receita.",
    date: "2026-07-28",
    readingTime: 7,
    category: "Negócios",
    content: [
      "Todo negócio digital nasce de três respostas: para quem, qual dor e qual transformação.",
      "Antes de gastar com anúncio, gaste com clareza. Converse com dez pessoas do seu público.",
      "Construa a oferta mínima viável: algo entregável em uma semana. Venda para dez pessoas antes de automatizar.",
      "A escala vem depois da prova.",
    ].join("\n\n"),
  },
  {
    id: "rotina-de-alta-performance",
    slug: "rotina-de-alta-performance",
    title: "A rotina de alta performance de quem constrói liberdade",
    excerpt: "Como estruturar o seu dia em blocos de energia — e por que a manhã decide o resultado das outras 16 horas.",
    date: "2026-07-19",
    readingTime: 5,
    category: "Rotina",
    content: [
      "Não existe alta performance sem gestão de energia. Tempo é igual para todos; energia não.",
      "Divida o dia em três blocos: criação, execução e manutenção.",
      "Proteja o sono como se fosse faturamento — porque é.",
      "E fature em silêncio.",
    ].join("\n\n"),
  },
];

export const blogPosts: BlogPost[] = staticPosts;

export function getPostBySlug(slug: string): BlogPost | undefined {
  return blogPosts.find((p) => p.slug === slug);
}

export function formatDate(iso: string): string {
  if (!iso) return "";
  const d = new Date(iso.length === 10 ? iso + "T12:00:00Z" : iso);
  if (isNaN(d.getTime())) return "";
  return d.toLocaleDateString("pt-BR", { day: "2-digit", month: "long", year: "numeric", timeZone: "UTC" });
}
