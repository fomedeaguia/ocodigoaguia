export type BlogPost = {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readTime: string;
  category: string;
  content: string[];
};

export const blogPosts: BlogPost[] = [
  {
    slug: "mentalidade-de-aguia",
    title: "Mentalidade de águia: como parar de viver no cercado",
    excerpt:
      "A diferença entre quem prospera e quem estagna raramente é talento. É altitude mental. Entenda como treinar a visão de águia no dia a dia.",
    date: "2026-08-12",
    readTime: "6 min",
    category: "Mentalidade",
    content: [
      "A galinha vive olhando para o chão. A águia vive olhando para o horizonte. Ambas têm asas — só uma decide usá-las.",
      "No mundo digital isso se traduz em foco: enquanto a maioria consome conteúdo, a minoria constrói ativos. Enquanto a maioria reage às notificações, a minoria define a própria agenda.",
      "Treinar a mentalidade de águia começa com três decisões diárias: escolher o que merece sua atenção, eliminar o que rouba sua energia e proteger o bloco de tempo em que você cria.",
      "Não é motivação. É arquitetura. Você não sobe pela força de vontade, sobe pelo ambiente que constrói ao seu redor — pessoas, rotinas e padrões de exigência.",
    ],
  },
  {
    slug: "disciplina-supera-motivacao",
    title: "Por que disciplina vence motivação todos os dias",
    excerpt:
      "Motivação é clima, disciplina é estrutura. Um sistema simples para executar mesmo nos dias em que a vontade não aparece.",
    date: "2026-08-05",
    readTime: "5 min",
    category: "Disciplina",
    content: [
      "Motivação é uma emoção — e emoções oscilam. Disciplina é um contrato que você assina com o seu futuro.",
      "O sistema mais eficaz é o mais chato: mesma hora, mesmo lugar, mesma primeira tarefa. Reduza o número de decisões e você multiplica a execução.",
      "Comece com o mínimo inegociável: 45 minutos por dia de trabalho profundo no seu projeto principal. Nada de e-mail, nada de rede social, nada de 'só uma olhadinha'.",
      "Ao final de 90 dias, o resultado não vem do dia heroico. Vem dos 90 dias comuns em que você não negociou consigo mesmo.",
    ],
  },
  {
    slug: "primeiros-passos-era-digital",
    title: "Primeiros passos para construir renda na era digital",
    excerpt:
      "Sem fórmula mágica: um caminho realista para sair do zero, validar uma oferta e transformar conhecimento em receita.",
    date: "2026-07-28",
    readTime: "7 min",
    category: "Negócios",
    content: [
      "Todo negócio digital nasce de três respostas: para quem, qual dor e qual transformação.",
      "Antes de gastar com anúncio, gaste com clareza. Converse com dez pessoas do seu público e escreva a dor delas com as palavras delas.",
      "Depois, construa a oferta mínima viável: algo entregável em uma semana, com preço acessível e promessa específica. Venda para dez pessoas antes de automatizar qualquer coisa.",
      "A escala vem depois da prova. Primeiro reprodutibilidade, depois tráfego. Quem inverte essa ordem paga caro para descobrir que a oferta não estava pronta.",
    ],
  },
  {
    slug: "rotina-de-alta-performance",
    title: "A rotina de alta performance de quem constrói liberdade",
    excerpt:
      "Como estruturar o seu dia em blocos de energia — e por que a manhã decide o resultado das outras 16 horas.",
    date: "2026-07-19",
    readTime: "5 min",
    category: "Rotina",
    content: [
      "Não existe alta performance sem gestão de energia. Tempo é igual para todos; energia não.",
      "Divida o dia em três blocos: criação (energia máxima), execução (energia média) e manutenção (energia baixa). Coloque o trabalho que muda o jogo no primeiro bloco.",
      "Proteja o sono como se fosse faturamento — porque é. Cada hora perdida de descanso custa duas de foco no dia seguinte.",
      "E fature em silêncio: quem anuncia demais o plano costuma ter menos combustível para executá-lo.",
    ],
  },
];

export function getPostBySlug(slug: string) {
  return blogPosts.find((post) => post.slug === slug);
}

export function formatDate(iso: string) {
  return new Date(iso + "T00:00:00").toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });
}
