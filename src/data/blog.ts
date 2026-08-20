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
    excerpt:
      "A diferença entre quem prospera e quem estagna raramente é talento. É altitude mental. Entenda como treinar a visão de águia no dia a dia.",
    date: "2026-08-12",
    readingTime: 6,
    category: "Mentalidade",
    coverImage:
      "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=1200&q=80",
    tags: ["mentalidade", "foco", "crescimento"],
    featured: true,
    content: [
      "A galinha vive olhando para o chão. A águia vive olhando para o horizonte. Ambas têm asas — só uma decide usá-las. Essa metáfora simples resume um dos maiores desafios da vida moderna: a maioria das pessoas passa o dia reagindo ao que aparece na tela, no grupo de WhatsApp ou na notificação, em vez de agir com intenção sobre o que realmente importa.",

      "No mundo digital isso se traduz em foco estratégico: enquanto a maioria consome conteúdo passivamente, a minoria constrói ativos que trabalham por ela. A diferença não está no talento nem no acesso à informação — está na capacidade de elevar o ponto de vista e enxergar o que a multidão, encurvada sobre a tela, não consegue ver.",

      "Treinar a mentalidade de águia começa com três decisões diárias que parecem simples, mas exigem prática constante. A primeira é escolher com clareza o que merece a sua atenção naquele dia — não o que é urgente para os outros, mas o que é estratégico para você. A segunda é eliminar sem culpa o que rouba sua energia: reuniões sem pauta, conversas circulares e conteúdo que entretém mas não transforma.",

      "A terceira decisão, e talvez a mais poderosa, é proteger o bloco de tempo em que você cria. Esse período — seja uma hora, sejam duas — é sagrado. Nele você não responde mensagens, não verifica métricas e não atende telefonemas. Você constrói. Essa é a diferença entre o profissional que acumula entregas e o que acumula relevância.",

      "Não é motivação que sustenta esse processo. É arquitetura. É a construção deliberada de um ambiente, uma rotina e um conjunto de hábitos que tornam a execução o caminho natural — não o excepcional. A águia não se motiva para voar alto. Ela simplesmente foi construída para isso, e treinou até que o alto fosse o seu lugar comum.",

      "Comece hoje com uma pergunta honesta: onde você tem voado baixo por comodidade? A resposta está nos seus últimos sete dias de agenda. O que você fez que foi de fato estratégico, e o que foi apenas barulho bem-intencionado? A mentalidade de águia exige essa honestidade brutal consigo mesmo — e recompensa quem a pratica com clareza, resultado e, com o tempo, com liberdade.",
    ].join("\n\n"),
  },
  {
    id: "disciplina-supera-motivacao",
    slug: "disciplina-supera-motivacao",
    title: "Por que disciplina vence motivação todos os dias",
    excerpt:
      "Motivação é clima, disciplina é estrutura. Um sistema simples para executar mesmo nos dias em que a vontade não aparece.",
    date: "2026-08-05",
    readingTime: 5,
    category: "Disciplina",
    coverImage:
      "https://images.unsplash.com/photo-1526506118085-60ce8714f8c5?w=1200&q=80",
    tags: ["disciplina", "produtividade", "hábitos"],
    content: [
      "Motivação é uma emoção — e emoções oscilam. Há dias em que você acorda com energia, clareza e disposição para conquistar o mundo. Há outros em que a simples ideia de sentar em frente ao computador parece um esforço gigantesco. Quem constrói algo de valor ao longo do tempo aprende cedo que não dá para depender do humor do dia.",

      "Disciplina é um contrato que você assina com o seu futuro. Não com a versão animada de você que está em dia bom — mas com a versão cansada, com sono, com vontade de procrastinar. Quando a disciplina está instalada como sistema, ela executa independentemente do estado emocional do momento.",

      "O sistema mais eficaz é, quase sempre, o mais simples e aparentemente mais chato: mesma hora, mesmo lugar, mesma primeira tarefa. A repetição elimina a necessidade de decisão. Quanto menos você precisa decidir sobre quando, onde e o que fazer primeiro, mais energia mental sobra para a execução em si. Isso é o que os pesquisadores chamam de conservação de energia cognitiva.",

      "Comece com o mínimo inegociável: 45 minutos por dia de trabalho profundo no seu projeto principal. Não 4 horas esporádicas seguidas de cinco dias de inatividade. Quarenta e cinco minutos todos os dias, sem exceção. Esse bloco deve acontecer antes das demandas do dia tomarem conta — de preferência de manhã, antes mesmo de abrir o e-mail ou o Instagram.",

      "Há um segundo componente pouco discutido: a proteção do ambiente. Disciplina fraqueja quando o ambiente convida à dispersão. Se o celular está na mesa, ele vai ser pego. Se o feed está aberto, ele vai ser consultado. Construir disciplina significa, em boa parte, construir fricção para os comportamentos que atrapalham e remover fricção para os comportamentos que constroem.",

      "Ao final de 90 dias aplicando um sistema simples como esse, o resultado não vem do dia heroico em que você produziu durante doze horas. Vem dos 90 dias comuns, dos dias de 45 minutos, dos dias em que ninguém ficou sabendo que você estava trabalhando porque você estava silenciosamente acumulando. Essa é a matemática discreta da disciplina — invisível no curto prazo, transformadora no longo.",
    ].join("\n\n"),
  },
  {
    id: "primeiros-passos-era-digital",
    slug: "primeiros-passos-era-digital",
    title: "Primeiros passos para construir renda na era digital",
    excerpt:
      "Sem fórmula mágica: um caminho realista para sair do zero, validar uma oferta e transformar conhecimento em receita.",
    date: "2026-07-28",
    readingTime: 7,
    category: "Negócios",
    coverImage:
      "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80",
    tags: ["negócios digitais", "renda", "empreendedorismo"],
    content: [
      "Todo negócio digital nasce de três respostas que precisam estar muito claras antes de qualquer ação técnica ou investimento em tráfego: para quem você serve, qual dor específica você resolve e qual transformação concreta você entrega. Sem essas três respostas, qualquer estratégia de marketing é construída sobre areia.",

      "Antes de gastar com anúncio, gaste com clareza. Isso significa conversas reais com pessoas reais do público que você quer atender. Dez conversas de trinta minutos revelam mais sobre posicionamento e oferta do que centenas de horas de pesquisa teórica. Pergunte sobre dores, sobre tentativas frustradas de solução, sobre o que elas pagariam para resolver aquele problema de uma vez.",

      "Com essas informações em mãos, construa a oferta mínima viável: algo entregável em uma semana, que resolva um problema específico com um resultado mensurável. Não o produto perfeito. Não o curso completo com quarenta módulos. Uma solução focada, clara e que você consegue entregar agora com os recursos que já tem. Produto perfeito que ainda não existe não fatura.",

      "Venda para dez pessoas antes de automatizar qualquer coisa. Esse é um princípio fundamental que a maioria ignora por ansiedade de escala. A automação serve para multiplicar o que já funciona — não para testar se funciona. Quando você vende manualmente para dez pessoas, aprende mais sobre objeções, dúvidas e pontos de valor do que qualquer A/B test conseguiria te dizer.",

      "O caminho do zero ao primeiro real digital é linear mas não rápido. Envolve definir o público com precisão, criar uma proposta de valor testada em conversas reais, montar uma oferta mínima viável, vender manualmente e refinar com base no feedback, e só então investir em distribuição e automação. Cada etapa depende da anterior — pular qualquer uma delas aumenta exponencialmente o risco de desperdício.",

      "A escala vem depois da prova. Quando você tem dez clientes satisfeitos, um processo de entrega que funciona e um posicionamento validado, aí sim o investimento em anúncio, em funil e em estrutura faz sentido. Antes disso, é otimismo mal aplicado. O empreendedor digital que dura é o que respeita essa sequência — mesmo quando a pressa fala mais alto.",
    ].join("\n\n"),
  },
  {
    id: "rotina-de-alta-performance",
    slug: "rotina-de-alta-performance",
    title: "A rotina de alta performance de quem constrói liberdade",
    excerpt:
      "Como estruturar o seu dia em blocos de energia — e por que a manhã decide o resultado das outras 16 horas.",
    date: "2026-07-19",
    readingTime: 5,
    category: "Rotina",
    coverImage:
      "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=1200&q=80",
    tags: ["rotina", "produtividade", "alta performance"],
    content: [
      "Não existe alta performance sem gestão de energia. Tempo é igual para todos — vinte e quatro horas, sem exceção, independente de quem você é ou quanto você fatura. Energia, por outro lado, é desigual e gerenciável. Quem aprende a cuidar da própria energia, física e mental, multiplica o resultado que consegue extrair de cada hora do dia.",

      "A estrutura mais eficaz para quem quer construir liberdade financeira divide o dia em três blocos fundamentais. O primeiro é o bloco de criação, reservado para o início da manhã, quando o córtex pré-frontal ainda não foi sobrecarregado por demandas externas. Nesse bloco você cria: escreve, grava, desenvolve, planeja. É o trabalho de mais alto valor e por isso exige o seu melhor momento cognitivo.",

      "O segundo bloco é o de execução, composto pelas tarefas operacionais que exigem mais ação do que pensamento criativo: responder e-mails, fazer reuniões, resolver pendências administrativas, implementar o que foi planejado no bloco anterior. Esse bloco pertence ao meio do dia, quando a energia está sustentada mas o pico criativo já passou.",

      "O terceiro bloco é o de manutenção — cuidado com o corpo, exercício físico, alimentação, descanso ativo. Não é o bloco menos importante; é o que torna os outros dois sustentáveis no longo prazo. Alta performance que ignora o corpo é sprint, não maratona. E liberdade se constrói em maratona.",

      "Proteja o sono como se fosse faturamento — porque é. Cada hora de sono de qualidade é hora de consolidação cognitiva, de regulação hormonal e de recarga da capacidade de tomada de decisão. Um fundador que dorme mal toma decisões piores, cria menos, tem mais reatividade emocional e acumula erros que custam muito mais do que as horas que ele tentou economizar dormindo menos.",

      "A manhã decide o resultado das outras dezesseis horas. Não porque existe magia nas primeiras horas do dia — mas porque a sequência importa. Quem começa o dia reagindo (olhando o celular, checando mensagens, entrando no feed) condiciona o cérebro a um modo reativo que persiste pelo resto do dia. Quem começa criando, movendo-se e intencionando condicionou o cérebro ao oposto. Fature em silêncio, construa com consistência e deixe os resultados falarem no tempo certo.",
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
  return d.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  });
}
