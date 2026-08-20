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

// Posts base — sempre presentes no bundle
export const staticPosts: BlogPost[] = [
  {
    id: "mentalidade-de-aguia",
    slug: "mentalidade-de-aguia",
    title: "Mentalidade de águia: como parar de viver no cercado",
    excerpt: "A diferença entre quem prospera e quem estagna raramente é talento. É altitude mental. Entenda como treinar a visão de águia no dia a dia.",
    date: "2026-08-12",
    readingTime: 7,
    category: "Mentalidade",
    coverImage: "https://images.unsplash.com/photo-1611348586804-61bf6c080437?w=1080&q=80",
    tags: ["mentalidade", "alto desempenho", "crescimento pessoal"],
    content: `## A gaiola que você mesmo construiu

A galinha vive olhando para o chão. A águia vive olhando para o horizonte. Ambas têm asas — só uma decide usá-las. Essa é talvez a distância mais honesta entre duas formas de existir no mundo: uma passa a vida inteira dentro de um cercado que ela mesma aceita como limite, e a outra define o próprio espaço voando acima de qualquer fronteira que outros tentaram impor.

O problema não é o cercado. O problema é que a maioria das pessoas nem percebe que está dentro de um. O cercado pode ser um emprego que paga o suficiente para não doer, mas pouco demais para libertar. Pode ser uma rotina construída sobre o hábito do outro, não sobre as próprias escolhas. Pode ser, e isso é o mais sutil de todos, uma narrativa interna que repete há anos que você não é capaz, não é o momento certo, não é para você.

A mentalidade de águia começa no momento em que você questiona essa narrativa.

## O que separa quem sobe de quem fica

Durante anos, pesquisadores de comportamento humano tentaram identificar o fator determinante entre pessoas que constroem vidas extraordinárias e aquelas que vivem em modo reativo permanente. O fator mais consistente é a **locus de controle interno**: a crença de que as próprias ações são o principal determinante dos resultados de vida.

Quem tem locus externo atribui o que acontece ao acaso, ao governo, ao chefe. Quem tem locus interno sabe que a resposta às condições externas é sempre uma escolha. A águia não espera o vento parar para voar. Ela aprende a usar o vento como propulsão.

Essa é a primeira marca da mentalidade de águia: **responsabilidade radical**. Não culpa. Responsabilidade.

## Visão ampliada: enxergar o que outros não vêem

A águia tem uma acuidade visual que pode chegar a oito vezes a capacidade humana. Mas o que mais impacta não é a nitidez: é o campo. A águia vê 340 graus ao redor de si sem mover a cabeça.

No mundo humano, isso se traduz em **consciência situácional**: a capacidade de ler o ambiente com clareza suficiente para antecipar movimentos e agir antes que a maioria perceba o que está acontecendo. Desenvolver essa visão não é um dom. É uma prática.

## Altitude: o princípio que muda tudo

Altura não é apenas geográfica. É uma postura mental. Quando você opera a partir de um nível mais elevado de consciência, as decisões mudam. O que parecia urgentíssimo de perto, visto de cima, é apenas ruído.

A prática de altitude mental envolve três hábitos concretos: a **pausa estratégica** antes de reagir, o **zoom out semanal** para avaliar progresso real, e a **curadoria de input** — você se torna a média dos conteúdos que consome.

## Foco: a arma mais subestimada

A águia não caça dez presas ao mesmo tempo. Ela escolhe uma, trava o olhar e mergulha com tudo. No mundo digital, o maior inimigo do resultado não é a falta de informação. É o excesso.

O foco é a capacidade de dizer não para o bom em favor do ótimo. É escolher uma direção e aprofundar, mesmo quando a distracção parece mais estimulante. Treinar foco é treinar desconforto.

## Renovação: o ciclo que sustenta o voo

Nenhuma versão elevada de você cabe no mesmo sistema de crenças, hábitos e relacionamentos da versão anterior. Crescimento real exige desfazer antes de construir.

---

## Pronto Para Ativar o Arquétipo da Águia em Você?

Tudo que você leu aqui é apenas o começo. O **Código Águia** aprofunda cada um desses princípios com clareza, exemplos reais e um roteiro prático para quem quer mudar de nível de verdade. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).

---`,
  },
  {
    id: "disciplina-supera-motivacao",
    slug: "disciplina-supera-motivacao",
    title: "Por que disciplina vence motivação todos os dias",
    excerpt: "Motivação é clima, disciplina é estrutura. Um sistema simples para executar mesmo nos dias em que a vontade não aparece.",
    date: "2026-08-05",
    readingTime: 7,
    category: "Disciplina",
    coverImage: "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=1080&q=80",
    tags: ["disciplina", "hábitos", "alta performance"],
    content: `## O problema com a motivação

Toda segunda-feira, milhões de pessoas começam a semana com um pico de energia e uma lista de intenções. Até quarta, metade dessa energia foi consumida pelas demandas do cotidiano. Na sexta, a lista continua quase intacta e a frustração acumula.

Esse é o ciclo da motivação. E o problema é estrutural, não moral. A motivação é uma emoção, e emoções são voláteis por natureza. Construir uma vida extraordinária sobre uma base emocional instável é como tentar erguer um prédio sobre areia.

A disciplina é diferente. Disciplina é um sistema. É um conjunto de decisões tomadas uma vez e executadas repetidamente, independentemente de como você se sente.

## A neuroquimica da consistência

Quando você executa uma ação repetidamente no mesmo contexto, o cérebro cria uma via neural associada àquele comportamento. Com o tempo, o comportamento exige menos decisão consciente e mais execução automática.

O problema é que a formação de hábitos requer um período de desconforto inicial. As primeiras semanas são as mais difíceis. É exatamente aqui que a motivação falha e a **disciplina salva**: ela te leva através do desconforto inicial até o ponto em que a consistência se torna natural.

## O sistema dos três pilares

Humanos altamente produtivos não têm mais força de vontade do que a média. Eles constroem sistemas que reduzem a necessidade de força de vontade.

O primeiro é a **âncora temporal**: mesma hora, todo dia, para a tarefa mais importante. O segundo é a **redução de atrito**: eliminar qualquer obstáculo entre você e a execução. O terceiro é o **mínimo inegociável**: a versão mínima da tarefa que você executará mesmo no pior dia.

## Identidade antes de meta

A maioria das pessoas tenta mudar o comportamento pela meta. A abordagem que sustenta comportamentos a longo prazo começa pela pergunta: **quem eu estou me tornando?**

Essa inversão muda tudo. Você para de depender da motivação externa e começa a agir a partir de um compromisso interno com a própria identidade. Cada pequena ação consistente é um voto dado para a versão de si que você está construindo.

## O paradoxo da consistência

Humanos tendem a superestimar o que podem fazer em um mês e subestimar o que podem construir em um ano. Quarenta e cinco minutos diários de trabalho profundo, cinco vezes por semana, geram aproximadamente 195 horas de trabalho focado ao longo de um ano.

## Como começar hoje

Não existe o momento perfeito para começar. Escolha uma única prática que, se feita todos os dias por noventa dias, mudaria algo real na sua vida. Defina o horário. Defina o mínimo inegociável. Execute amanhã, sem esperar sentir vontade.

---

## Pronto Para Ativar o Arquétipo da Águia em Você?

Tudo que você leu aqui é apenas o começo. O **Código Águia** aprofunda cada um desses princípios com clareza e um roteiro prático para quem quer mudar de nível de verdade. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).

---`,
  },
  {
    id: "primeiros-passos-era-digital",
    slug: "primeiros-passos-era-digital",
    title: "Primeiros passos para construir renda na era digital",
    excerpt: "Sem fórmula mágica: um caminho realista para sair do zero, validar uma oferta e transformar conhecimento em receita.",
    date: "2026-07-28",
    readingTime: 7,
    category: "Negócios",
    coverImage: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1080&q=80",
    tags: ["negócios digitais", "renda online", "empreendedorismo"],
    content: `## O erro que quase todo mundo comete

A maioria das pessoas que decide criar renda na internet começa pelo lugar errado. Começa pelo produto, pelo canal, pela ferramenta. Passa semanas escolhendo nome, logo, plataforma, cor do site. Constrói uma estrutura impecável para uma oferta que ainda não foi validada por ninguém.

O resultado é quase sempre o mesmo: depois de muito esforço, o lançamento acontece no silêncio. Ninguém compra. A conclusão equivocada é que o mercado digital não funciona. A conclusão real é que a oferta foi construída sem entender o comprador.

Todo negócio digital bem-sucedido nasce de três respostas claras: **para quem**, **qual dor** e **qual transformação**.

## Antes de criar, escute

A etapa mais negligenciada na construção de um negócio digital é a pesquisa qualitativa. Converse com dez pessoas que representam seu público ideal. Não para vender. Para entender.

As respostas vão revelar algo fundamental: as palavras exatas que seu público usa para descrever a própria dor. E essas palavras são ouro — são o copy da sua página de vendas, o título do seu produto, a promessa da sua oferta.

## A oferta mínima viável

Depois de entender a dor, o próximo passo é criar a menor versão possível da solução. Não o curso completo, não o programa de doze semanas. A **oferta mínima viável**: algo que resolve um problema específico e pode ser entregue em uma semana.

O objetivo não é faturar muito na primeira venda. É validar. Uma venda real vale mais do que mil curtidas.

## Venda para dez antes de escalar para mil

Antes de investir em anúncio pago, venda manualmente para dez pessoas. Esse processo ensina o que nenhuma dashboard ensina: o que faz o cliente hesitar, o que o convence.

Com dez vendas reais, você tem dados e depoimentos. Só então faz sentido escalar. A escala amplifica o que já existe.

## Os três modelos que funcionam para quem começa

Três modelos se destacam para quem está começando do zero. O **serviço especializado**: oferecer uma habilidade específica para clientes. O **infoproduto**: transformar conhecimento em ebook ou curso. A **afiliação**: promover produtos de terceiros e receber comissão.

## A mentalidade que sustenta o processo

Construir renda digital não é um sprint. É uma maratona com aprendizados diários. A águia não aprende a voar em um dia. Ela pula do ninho, cai, ajusta, tenta de novo. O voo não vem da teoria. Vem da repetição com correção.`,
  },
  {
    id: "rotina-de-alta-performance",
    slug: "rotina-de-alta-performance",
    title: "A rotina de alta performance de quem constrói liberdade",
    excerpt: "Como estruturar o seu dia em blocos de energia — e por que a manhã decide o resultado das outras 16 horas.",
    date: "2026-07-19",
    readingTime: 7,
    category: "Rotina",
    coverImage: "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1080&q=80",
    tags: ["rotina", "produtividade", "alta performance"],
    content: `## O mito da produtividade

A palavra produtividade foi sequestrada. Hoje ela evoca imagens de planilhas coloridas e maratonas de trabalho de dezesseis horas. Mas os estudos mais sólidos sobre desempenho de longo prazo mostram o oposto: pessoas que sustentam alta performance por anos não trabalham mais horas. Trabalham melhor.

A rotina de alta performance não é sobre fazer mais. É sobre fazer o que importa, no momento de maior energia, com a máxima concentração possível.

## Energia é o recurso escasso

Tempo é democrático: todos têm vinte e quatro horas. Mas energia não é. A capacidade de foco profundo varia ao longo do dia em curvas previsíveis.

A maioria das pessoas desperdiça o pico de energia cognitiva em tarefas de baixo valor: checar e-mails, responder mensagens. A primeira decisão de uma rotina de alta performance é proteger o pico de energia para o trabalho que mais importa.

## Os três blocos do dia

Uma estrutura simples divide o dia em três blocos. O **bloco de criação** ocupa o período de energia máxima e é reservado exclusivamente para trabalho profundo. O **bloco de execução** cobre o período de energia média e comporta reuniões e respostas. O **bloco de manutenção** serve para tarefas administrativas.

## A manhã como fundação

A manhã decide o resultado do dia. Não porque existe alguma magia em acordar cedo, mas porque as primeiras decisões criam um momentum que influencia tudo o que vem depois.

Uma rotina matinal eficaz precisa incluir: **hidratação e ativação física**, **intenção clara** (saber qual é a tarefa mais importante antes de abrir qualquer tela) e **entrada no estado de foco** sem checar o celular nos primeiros trinta minutos.

## Sono: o multiplicador que ninguém respeita

Nenhuma estratégia de performance funciona sobre um cérebro mal descansado. O sono não é o tempo em que você para de produzir. É o tempo em que o cérebro consolida memórias e restaura a capacidade de tomada de decisão.

## A arte de dizer não

Cada sim que você dá para uma reunião desnecessária é um não dado ao seu bloco de criação. Alta performance exige curadoria agressiva de compromissos. A águia não gasta energia caçando tudo que se move. Ela escolhe o alvo com precisão.

---

## Pronto Para Ativar o Arquétipo da Águia em Você?

Tudo que você leu aqui é apenas o começo. O **Código Águia** aprofunda cada um desses princípios com clareza e um roteiro prático para quem quer mudar de nível de verdade. [Acesse O Código Águia e comece hoje](https://ocodigoaguia.com.br).

---`,
  },
];

// Posts dinâmicos carregados via import.meta.glob (src/blog-posts/)
function loadDynamicPosts(): BlogPost[] {
  try {
    const modules = import.meta.glob("/src/blog-posts/*.json", {
      eager: true,
    }) as Record<string, { default?: BlogPost } & BlogPost>;
    return Object.values(modules)
      .map((m) => (m.default ?? m) as BlogPost)
      .filter((post) => !!post?.slug && !!post?.title && !!post?.date);
  } catch {
    return [];
  }
}

const dynamicPosts = loadDynamicPosts();

// Mescla dinâmicos + estáticos, sem duplicatas, ordenados por data
const seenSlugs = new Set<string>();
export const blogPosts: BlogPost[] = [...dynamicPosts, ...staticPosts]
  .filter((post) => {
    if (seenSlugs.has(post.slug)) return false;
    seenSlugs.add(post.slug);
    return true;
  })
  .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

export function getPostBySlug(slug: string): BlogPost | undefined {
  return blogPosts.find((post) => post.slug === slug);
}

export function formatDate(iso: string): string {
  if (!iso) return "";
  const d = new Date(iso.length === 10 ? iso + "T12:00:00Z" : iso);
  if (isNaN(d.getTime())) return "";
  return d.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  });
}
