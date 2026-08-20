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
    title: "Mentalidade de aguia: como parar de viver no cercado",
    excerpt:
      "A diferenca entre quem prospera e quem estagna raramente e talento. E altitude mental. Entenda como treinar a visao de aguia no dia a dia e transformar sua forma de enxergar oportunidades.",
    date: "2026-08-12",
    readingTime: 8,
    category: "Mentalidade",
    coverImage:
      "https://images.unsplash.com/photo-1611348524140-53c9a25263d6?w=1200&q=80",
    tags: ["mentalidade", "foco", "crescimento", "visao estrategica"],
    featured: true,
    content: `A galinha vive olhando para o chao. A aguia vive olhando para o horizonte. Ambas tem asas, mas somente uma decide usa-las de verdade. Essa metafora simples resume um dos maiores desafios da vida moderna: a maioria das pessoas passa o dia inteiro reagindo ao que aparece na tela, no grupo de WhatsApp, na notificacao do celular ou na urgencia fabricada do e-mail corporativo, em vez de agir com intencao clara sobre o que realmente importa para o seu futuro.

Existe uma diferenca fundamental entre quem age de forma proativa e quem apenas reage ao ambiente. A pessoa que vive no modo reativo acorda cedo, fica ocupada o dia inteiro, deita tarde e, ao revisar o que fez, percebe que nao avancou quase nada no que realmente importava. Ja quem treinou a mentalidade de aguia aprende a separar o urgente do importante, o barulho do sinal, o movimento da direcao.

No mundo digital isso se traduz em foco estrategico e consistencia de longo prazo. Enquanto a maioria das pessoas consome conteudo passivamente, reagindo ao que o algoritmo entrega, a minoria constroi ativos digitais que trabalham por ela mesmo quando ela esta dormindo. A diferenca nao esta no talento nato, nem no acesso privilegiado a informacao. A diferenca esta na capacidade de elevar o ponto de vista e enxergar o que a multidao, encurvada sobre a tela, simplesmente nao consegue ver a partir de baixo.

Treinar a mentalidade de aguia comeca com tres decisoes diarias que parecem simples na teoria, mas exigem pratica consciente e repetida ate se tornarem automaticas. A primeira decisao e escolher com clareza absoluta o que merece a sua atencao naquele dia especifico. Nao o que e urgente para o seu chefe ou para o seu cliente, nao o que apareceu primeiro no feed, nao o que gerou mais ansiedade ao acordar. O que e estrategico para voce, para o seu projeto, para o seu crescimento real ao longo dos proximos doze meses.

A segunda decisao e eliminar sem culpa tudo o que rouba a sua energia sem gerar retorno proporcional. Reunioes sem pauta definida que acabam em nada. Conversas circulares que voltam sempre para o mesmo ponto sem avanco. Conteudo que entreteme por trinta minutos mas nao ensina, nao inspira e nao transforma. Grupos de mensagens que funcionam mais como ruido social do que como troca de valor real. Cada coisa que voce elimina dessas categorias e energia disponivel para o que constroi.

A terceira decisao, e talvez a mais poderosa de todas, e proteger com seriedade o bloco de tempo em que voce cria. Esse periodo reservado, seja uma hora pela manha ou duas horas a tarde, e sagrado e inegociavel. Nele voce nao responde mensagens, nao verifica metricas, nao atende telefonemas, nao abre redes sociais. Voce constroi. Essa e a diferenca real entre o profissional que acumula entregas e o que acumula relevancia, entre o que trabalha pelo dinheiro e o que constroi ativos que geram dinheiro.

Nao e motivacao que sustenta esse processo no longo prazo. Motivacao e volatil, aparece nos dias bons e some nos dias dificeis. O que sustenta e a arquitetura, a construcao deliberada de um ambiente fisico e digital, uma rotina clara e um conjunto de habitos que tornam a execucao o caminho natural e automatico, nao o excepcional e heroico. A aguia nao se motiva para voar alto toda manha. Ela foi construida para isso e treinou ate que o alto fosse o seu lugar comum, o seu estado padrao.

Uma das praticas mais transformadoras para desenvolver essa mentalidade e o que especialistas em produtividade chamam de revisao semanal. Todo domingo, separe trinta minutos para revisar a semana que passou com honestidade: o que voce criou, o que voce apenas consumiu, onde voce foi estrategico e onde voce foi reativo. Esse habito de autoavaliacao regular calibra o sistema interno e evita que semanas inteiras passem no modo automatico sem producao real de valor.

Outro elemento central e a gestao da atencao, que e diferente da gestao do tempo. Tempo voce nao controla, apenas distribui. Atencao voce treina, fortalece e direciona. Uma hora de trabalho com atencao total vale mais do que quatro horas de trabalho fragmentado por notificacoes, conversas e troca de contexto constante. Os estudos de neurociencia cognitiva mostram que cada interrupcao custa em media vinte e tres minutos para que o cerebro retorne ao nivel de concentracao anterior. Isso significa que um dia com dez interrupcoes pode custar mais de tres horas de produtividade real.

A mentalidade de aguia tambem se manifesta na forma como voce reage ao fracasso e aos obstaculos. A galinha, quando encontra uma cerca, para. A aguia enxerga a cerca do alto e voa sobre ela sem nem perceber que ela existia. Isso nao e arrogancia, e perspectiva. Problemas vistos de perto parecem intransponiveis. O mesmo problema visto de cima, com mais contexto e mais opcoes no horizonte, frequentemente tem uma solucao que nao estava visivel de dentro do cercado.

Comece hoje com uma pergunta honesta e direta: onde voce tem voado baixo por comodidade? Onde voce aceitou o cercado como limite definitivo quando podia simplesmente voar sobre ele? A resposta esta nos seus ultimos sete dias de agenda, nos seus ultimos sete dias de consumo de conteudo, nos seus ultimos sete dias de conversas. O que voce fez que foi de fato estrategico para o seu crescimento de longo prazo, e o que foi apenas barulho bem-intencionado disfarado de produtividade?

A mentalidade de aguia exige essa honestidade brutal consigo mesmo. Exige olhar para os proprios habitos sem auto-sabotagem nem auto-indulgencia. E recompensa generosamente quem a pratica com clareza de proposito, consistencia de execucao, resultado mensuravel ao longo dos meses e, com o tempo e a devida persistencia, com a liberdade real que voce esta buscando. O cercado sempre foi opcional. A escolha de voar sempre foi sua.`,
  },
  {
    id: "disciplina-supera-motivacao",
    slug: "disciplina-supera-motivacao",
    title: "Por que disciplina vence motivacao todos os dias",
    excerpt:
      "Motivacao e clima, disciplina e estrutura. Um sistema simples e comprovado para executar com consistencia mesmo nos dias em que a vontade simplesmente nao aparece.",
    date: "2026-08-05",
    readingTime: 7,
    category: "Disciplina",
    coverImage:
      "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&q=80",
    tags: ["disciplina", "produtividade", "habitos", "execucao"],
    content: `Motivacao e uma emocao e emocoes oscilam. Ha dias em que voce acorda com energia, clareza de proposito e disposicao para conquistar o mundo inteiro antes das dez da manha. Ha outros dias, e esses sao a maioria, em que a simples ideia de sentar em frente ao computador e comecar o trabalho mais importante parece um esforo gigantesco e injustificado. Quem constroi algo de valor real ao longo do tempo aprende cedo, geralmente da forma mais dolorosa possivel, que nao da para depender do humor do dia nem da inspiracao do momento.

A motivacao e influenciada por dezenas de variaveis fora do seu controle: qualidade do sono na noite anterior, nivel de estresse acumulado, situacao financeira do momento, clima, saude, relacionamentos. Construir uma vida e uma carreira sobre uma base tao instavel e como construir uma casa sobre areia molhada. A estrutura parece firme por alguns dias, ate que o proximo problema chega e todo o progresso desmorona.

Disciplina, por outro lado, e um contrato que voce assina com o seu futuro. Nao com a versao animada e empolgada de voce que esta em dia bom, cheia de energia e confianca. O contrato e assinado com a versao cansada, com sono, desanimada, com vontade legitima de procrastinar e assistir mais um episodio da serie. Quando a disciplina esta instalada como sistema operacional da sua rotina, ela executa independentemente do estado emocional do momento. Ela nao pede permissao ao humor do dia.

O sistema mais eficaz para construir disciplina duradoura e, quase sempre, o mais simples e aparentemente o mais chato: mesma hora, mesmo lugar, mesma primeira tarefa, todos os dias. A repeticao sistematica elimina a necessidade de tomar decisoes a cada novo dia. Quando voce precisa decidir toda manha se vai trabalhar, quando vai comecar e em que vai focar, voce ja gastou energia cognitiva preciosa antes mesmo de comecar. Isso e o que os pesquisadores de neurociencia chamam de fadiga de decisao, e ela e real e mensuravel.

Quanto menos voce precisa decidir sobre o quando, o onde e o que fazer primeiro, mais energia mental e emocional sobra para a execucao em si, para o trabalho de alta qualidade que realmente move o ponteiro. Os grandes nomes da produtividade, de Darwin a Darwin a Hemingway, de Einstein a Jobs, tinham rotinas rigidas e repetitivas nao por falta de criatividade, mas precisamente para preservar a criatividade para o que importava.

Comece com o minimo inegociavel. Nao com a meta heroica de trabalhar oito horas por dia no seu projeto paralelo alem do emprego. Comece com quarenta e cinco minutos por dia de trabalho profundo e focado no seu projeto principal. Nao quatro horas esporadicas numa sabado seguidas de cinco dias de completa inatividade e culpa. Quarenta e cinco minutos todos os dias, sem excecao, sete dias por semana, incluindo sabados, domingos e feriados. A continuidade e mais valiosa do que a intensidade.

Esse bloco de trabalho profundo deve acontecer antes que as demandas do dia tomem conta da sua atencao e da sua energia. De preferencia logo pela manha, antes de abrir o e-mail, antes de checar o Instagram, antes de ver qualquer mensagem. A ciencia do sono e da cognitividade mostra que as primeiras horas apos acordar sao o momento de maior capacidade para trabalho criativo e analitico profundo, antes que o cortex pre-frontal seja sobrecarregado pelas demandas externas.

Ha um segundo componente da disciplina que e pouco discutido mas extremamente importante: a protecao ativa do ambiente fisico e digital onde voce trabalha. Disciplina nao e apenas forca de vontade mental. Ela fraqueja rapidamente quando o ambiente ao redor convida constantemente a distracao e a dispersao. Se o celular esta sobre a mesa com a tela virada para cima, ele vai ser pego. Se o feed esta aberto em outra aba, ele vai ser consultado. Se as notificacoes estao ativas, elas vao interromper.

Construir disciplina real significa, em boa parte, construir friccao intencional para os comportamentos que atrapalham e remover toda a friccao possivel para os comportamentos que constroem. O celular vai para outro comodo durante o bloco de trabalho. O feed fica bloqueado por um aplicativo de controle. As notificacoes ficam desativadas. O ambiente fala mais alto do que qualquer discurso motivacional.

Existe tambem a dimensao social da disciplina que merece atencao. Compartilhar publicamente os seus compromissos, seja num grupo de pessoas que tem metas similares, seja num diario pessoal, cria responsabilidade externa que reforca a responsabilidade interna. Nao como mecanismo de pressao toxica, mas como ancora. Saber que voce vai registrar o que fez ou deixou de fazer no dia seguinte muda a decisao de agora.

Ao final de noventa dias aplicando um sistema simples e consistente como esse, o resultado surpreende quem ainda nao vivenciou. O resultado nao vem do dia heroico em que voce produziu durante doze horas seguidas no sabado. Vem dos noventa dias comuns, dos dias de quarenta e cinco minutos, dos dias cinzas de terca-feira em que ninguem sabia que voce estava avancando porque voce estava silenciosamente acumulando progresso real.

Essa e a matematica discreta e poderosa da disciplina: invisivel no curto prazo, absolutamente transformadora no longo. Enquanto a motivacao faz barulho nas redes sociais, a disciplina constroi em silencio os resultados que outras pessoas vao perguntar como voce conseguiu.`,
  },
  {
    id: "primeiros-passos-era-digital",
    slug: "primeiros-passos-era-digital",
    title: "Primeiros passos para construir renda na era digital",
    excerpt:
      "Sem formula magica: um caminho realista, passo a passo, para sair do zero, validar uma oferta real e transformar conhecimento em receita consistente.",
    date: "2026-07-28",
    readingTime: 9,
    category: "Negocios",
    coverImage:
      "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&q=80",
    tags: ["negocios digitais", "renda online", "empreendedorismo", "validacao"],
    content: `Todo negocio digital bem-sucedido nasce de tres respostas que precisam estar muito claras antes de qualquer acao tecnica, antes de criar qualquer pagina, antes de fazer qualquer post e especialmente antes de gastar qualquer real em anuncio. A primeira resposta e para quem exatamente voce serve, com um nivel de especificidade que vai alem de demograficos genericos como adultos de vinte a quarenta anos interessados em saude. A segunda e qual dor especifica e urgente voce resolve para essas pessoas. A terceira e qual transformacao concreta e mensuravel voce entrega, o que muda na vida delas depois que trabalham com voce ou compram o seu produto.

Sem essas tres respostas bem articuladas, qualquer estrategia de marketing e construida sobre areia. Voce pode ter o melhor funil de vendas do mercado, o copy mais persuasivo, o trafego mais caro e bem segmentado. Se a proposta de valor nao esta clara e nao ressoa com uma dor real de um publico real, o resultado e sempre o mesmo: gasto sem retorno, frustracao e a conclusao equivocada de que o mercado digital nao funciona para voce.

Antes de gastar um centavo com anuncio pago, gaste tempo e energia com clareza. E isso significa conversas reais com pessoas reais do publico que voce pretende atender. Nao pesquisas de formulario que as pessoas respondem de forma mecanica. Conversas genuinas, de preferencia por video ou ao telefone, de pelo menos trinta minutos cada. Dez dessas conversas revelam mais sobre posicionamento, linguagem do publico e angulos de oferta do que centenas de horas de pesquisa teorica em cursos e livros.

Nessas conversas, faca perguntas abertas sobre as dores e frustraces que as pessoas ja experimentaram tentando resolver o problema que voce quer ajudar a solucionar. Pergunte sobre tentativas frustradas anteriores, sobre o que elas ja compraram que nao funcionou, sobre o que acontece na vida delas por nao terem esse problema resolvido ainda. Escute mais do que fala. Anote as palavras exatas que elas usam para descrever o problema, nao as palavras academicas ou tecnicas que voce usa internamente.

Com essas informacoes concretas em maos, construa a oferta minima viavel: algo entregavel em no maximo uma semana, que resolva um problema especifico e urgente com um resultado mensuravel e claro. Nao o produto perfeito que voce imagina ha seis meses mas nunca comecu a construir. Nao o curso completo com quarenta modulos, certificado e comunidade exclusiva. Uma solucao focada, direta, que voce consegue entregar agora mesmo com os recursos e o conhecimento que ja tem hoje. Produto perfeito que ainda nao existe nao fatura. Oferta imperfeita que ja existe pode mudar a sua vida.

O proximo passo e contraintuitivo para quem tem pressa de escalar: venda manualmente para dez pessoas reais antes de automatizar qualquer parte do processo. Esse principio fundamental e ignorado pela maioria dos novos empreendedores digitais por causa da ansiedade de escala prematura. A automacao serve para multiplicar e acelerar o que ja esta comprovadamente funcionando, nao para testar se funciona. Quando voce vende manualmente para dez pessoas, conduzindo cada conversa de venda pessoalmente, voce aprende mais sobre objeces reais, duvidas recorrentes, pontos de maior valor percebido e o momento certo de fazer a oferta do que qualquer teste A/B ou analise de dados poderia te ensinar.

Essas dez primeiras vendas tambem constroem algo muito mais valioso do que dinheiro no curto prazo: elas constroem confianca no proprio produto, no proprio processo e na propria capacidade de vender. Muitos empreendedores digitais nunca chegam a esse ponto porque ficam em loop infinito de preparacao, ajustando slides de apresentacao, refazendo a logo, escolhendo a plataforma perfeita para hospedar o produto, quando o que eles precisam e simplesmente de uma conversa com um cliente potencial.

O caminho do zero ao primeiro real digital e linear mas nao e rapido, e isso precisa ser dito com clareza para nao alimentar expectativas irreais. O processo envolve definir o publico com precisao cirurgica, realizar conversas de descoberta com pessoas reais desse publico, criar uma proposta de valor testada e refinada com base nessas conversas, montar uma oferta minima viavel entregavel em uma semana, conduzir vendas manuais para as primeiras dez pessoas, coletar feedback real e refinar a oferta, e somente entao comecar a investir em distribuicao sistematica e automacao de processos.

Cada etapa depende da anterior e tem um proposito especifico. Pular qualquer uma delas nao acelera o processo, aumenta exponencialmente o risco de desperdicio de tempo, dinheiro e energia. O empreendedor que constroi na ordem certa chega ao resultado mais rapido do que o que tenta queimar etapas.

A monetizacao digital mais sustentavel nao vem de tendencias ou de nichos da moda. Vem da intersecao entre o conhecimento especifico que voce ja tem, uma dor real que um publico especifico experimenta e que voce consegue ajudar a resolver, e um modelo de entrega que voce consegue manter com consistencia ao longo do tempo. Essa intersecao, quando encontrada e validada, e o fundamento de uma renda digital que cresce e se solidifica com o tempo.

A escala vem depois da prova, nao antes. Quando voce tem dez clientes satisfeitos com resultados reais, um processo de entrega que funciona de forma previsivel e um posicionamento validado pelo mercado, ai sim o investimento em anuncio pago, em funil automatizado e em estrutura de escala faz todo o sentido economico e estrategico. Antes desse ponto, o mesmo investimento e otimismo mal aplicado. O empreendedor digital que perdura e o que respeita essa sequencia mesmo quando a pressa interna e a pressao externa falam mais alto.`,
  },
  {
    id: "rotina-de-alta-performance",
    slug: "rotina-de-alta-performance",
    title: "A rotina de alta performance de quem constroi liberdade",
    excerpt:
      "Como estruturar o seu dia em blocos de energia e por que a manha decide o resultado das outras 16 horas. O sistema pratico de quem constroi liberdade real.",
    date: "2026-07-19",
    readingTime: 8,
    category: "Rotina",
    coverImage:
      "https://images.unsplash.com/photo-1502945015378-0e284ca1a5be?w=1200&q=80",
    tags: ["rotina", "produtividade", "alta performance", "gestao de energia"],
    content: `Nao existe alta performance sustentavel sem gestao inteligente de energia. Tempo e o recurso mais democratico do mundo: vinte e quatro horas por dia, sete dias por semana, para todo ser humano vivo, independente de riqueza, posicao social, nivel de educacao ou localizacao geografica. Energia, por outro lado, e profundamente desigual e ao mesmo tempo completamente gerenciavel. Quem aprende a cuidar da propria energia fisica, mental, emocional e ate espiritual multiplica de forma dramatica o resultado que consegue extrair de cada hora disponivel no dia.

A confusao mais comum e mais cara que as pessoas cometem e tratar gestao do tempo e gestao de energia como sinonimos. Voce pode ter um calendario perfeitamente organizado, reunioes de quinze minutos, tarefas priorizadas por impacto e um sistema de productividade sofisticado, e ainda assim entregar resultados mediocres se a sua energia estiver mal alocada. Uma hora de trabalho com atencao plena e energia alta vale mais do que quatro horas de trabalho fragmentado, exausto e repleto de interrupcoes.

A estrutura de rotina mais eficaz para quem quer construir liberdade financeira real, baseada tanto na literatura cientifica sobre produtividade quanto na pratica de construtores de negocio bem-sucedidos, divide o dia em tres blocos funcionais distintos que respeitam os ciclos naturais de energia do cerebro humano.

O primeiro bloco e o de criacao, e ele pertence exclusivamente ao inicio da manha, nas duas a tres primeiras horas depois de acordar. Esse e o momento em que o cortex pre-frontal, a regiao do cerebro responsavel pelo pensamento criativo, pelo planejamento estrategico e pela resolucao de problemas complexos, esta no seu pico de funcionamento, ainda nao sobrecarregado pelas demandas externas do dia. Nesse bloco voce cria: escreve o conteudo que vai publicar, grava o video da semana, desenvolve o produto que vai vender, planeja as acoes estrategicas do mes, toma as decisoes mais importantes. E o trabalho de maior valor e por isso exige o seu melhor momento cognitivo do dia. Gastar esse tempo precioso respondendo e-mails ou scrollando o feed e um dos desperdicos mais caros que um construtor pode cometer.

O segundo bloco e o de execucao, composto pelas tarefas operacionais e relacionais que exigem mais acao pratica do que pensamento criativo profundo. Responder mensagens e e-mails, participar de reunioes, fazer ligacoes comerciais, resolver pendencias administrativas, implementar na pratica o que foi planejado no bloco anterior, coordenar equipes ou colaboradores. Esse bloco pertence ao meio do dia, entre dez da manha e tres da tarde aproximadamente, quando a energia ainda esta sustentada em nivel adequado mas o pico criativo da manha ja passou naturalmente.

O terceiro bloco e o de manutencao, e ele e tao importante quanto os dois anteriores, mas quase sempre e o primeiro a ser sacrificado quando o dia fica cheio e o tempo aperta. Este bloco e dedicado ao cuidado do proprio corpo e da propria mente: exercicio fisico regular, alimentacao intencional e nutritiva, descanso ativo, meditacao ou pratica contemplativa, conexoes sociais que nutrem em vez de drenar. Nao e o bloco menos importante. E o bloco que torna todos os outros sustentaveis no longo prazo, mes apos mes, ano apos ano.

Alta performance que ignora o corpo e o bem-estar mental e um sprint, nao uma maratona. E todo construtor que ja chegou perto do burnout sabe exatamente do que estamos falando. O pico de produtividade sem recuperacao adequada gera uma divida biologica que cobra juros altos mais a frente na forma de doencas, queda de imunidade, perda de criatividade, irritabilidade cronica e, eventualmente, colapso total.

Proteja o sono com a mesma seriedade com que voce protege o seu faturamento, porque o sono de qualidade e literalmente parte do seu faturamento. Cada hora de sono reparador e hora de consolidacao de memoria e aprendizado, de regulacao hormonal incluindo cortisol e insulina, de limpeza metabolica do cerebro e de recarga da capacidade de tomada de decisoes de alta qualidade. Um empreendedor que dorme mal por semanas toma decisoes piores, cria menos, tem mais reatividade emocional nas relacoes profissionais e acumula micro-erros de julgamento que custam muito mais em termos de oportunidade e recursos do que as poucas horas que ele tentou economizar reduzindo o sono.

A importancia do ritual matinal nao e uma fantasia de guru motivacional. Ela tem fundamento neurologico solido. A sequencia de comportamentos das primeiras horas do dia condiciona literalmente o estado mental dominante do resto do dia. Quem acorda e imediatamente pega o celular para checar mensagens, redes sociais ou noticias ativa o modo reativo do sistema nervoso, aquele orientado a responder estimulos externos, e esse modo tende a persistir e a dominar pelo resto do dia inteiro.

Quem acorda e escolhe intencionalmente os primeiros estimulos: hidratacao, movimento do corpo, alguns minutos de silencio ou meditacao, e so entao o trabalho mais importante antes de abrir qualquer aplicativo de comunicacao, condiciona o cerebro ao modo proativo. Esse modo e orientado a criar, a construir e a tomar iniciativa, e e esse modo que gera os resultados que diferenciam quem constroi liberdade de quem apenas sobrevive ao dia.

A manha decide o resultado das outras dezesseis horas nao porque existe magia mistica nos primeiros raios de sol. E porque a sequencia de comportamentos que voce estabelece ao acordar cria o estado mental, emocional e energetico que vai filtrar como voce interpreta e responde a tudo o que acontecer depois. Construa a sua manha com intencao. Proteja o seu sono com disciplina. Divida o seu dia em blocos de energia respeitando os ciclos naturais do seu organismo. E fature em silencio, construa com consistencia dia apos dia, e deixe os resultados acumulados falarem por si mesmos no tempo certo.`,
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
