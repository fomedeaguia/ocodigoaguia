export interface BlogPost {
  id: string;
  slug: string;
  title: string;
  excerpt: string;
  content: string;
  coverImage?: string;
  date: string;
  readingTime: number;
  category: string;
  tags: string[];
}

export function getPostBySlug(slug: string): BlogPost | undefined {
  return blogPosts.find((post) => post.slug === slug);
}

export function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  return date.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });
}

export const blogPosts: BlogPost[] = [
  {
    id: "1",
    slug: "a-visao-que-o-ambiente-te-roubou-e-voce-nem-percebeu",
    title: "A Vis\u00e3o Que o Ambiente Te Roubou e Voc\u00ea Nem Percebeu",
    excerpt:
      "Aquilo que voc\u00ea chama de seus desejos, suas metas e at\u00e9 seus limites s\u00e3o, muitas vezes, apenas reflexos do ambiente a que voc\u00ea est\u00e1 exposto.",
    coverImage: "/blog/visao-ambiente.jpg",
    date: "2025-01-15",
    readingTime: 8,
    category: "Mentalidade",
    tags: ["mentalidade", "ambiente", "liberdade", "crescimento"],
    content: `
H\u00e1 um momento em que a sua mente \u00e9 formada por tudo que a cerca \u2014 e nunca passa pelo crivo da sua consci\u00eancia. Voc\u00ea n\u00e3o acredita em algo porque analisou cada cren\u00e7a e chegou a uma conclus\u00e3o pr\u00f3pria. Voc\u00ea acredita porque, durante anos, aquele modo de enxergar a vida foi repetido \u00e0 mesa de jantar, nos corredores do trabalho, nas conversas informais, nos coment\u00e1rios das redes sociais e at\u00e9 nos sil\u00eancios das pessoas de quem voc\u00ea procurou aceita\u00e7\u00e3o.

Essa \u00e9 a confronta\u00e7\u00e3o necess\u00e1ria do texto de hoje: aquilo que voc\u00ea chama de seus desejos, suas metas e at\u00e9 seus limites s\u00e3o, muitas vezes, apenas reflexos do ambiente a que voc\u00ea est\u00e1 exposto. A \u00e1guia n\u00e3o come\u00e7a a voar alto porque decidiu um dia. Ela \u00e9 constru\u00edda por uma cadeia de escolhas \u2014 e a escolha mais antiga e silenciosa que voc\u00ea nunca fez foi a de aceitar o ar daquele ambiente como se fosse o \u00fanico poss\u00edvel.

## A F\u00e1brica de Desejos Onde Voc\u00ea Dorme

Existe uma compreens\u00e3o inc\u00f4moda: voc\u00ea pode estar vivendo uma vida que nunca parou para interrogar. Fui ensinado que a independ\u00eancia \u00e9 uma conquista p\u00fablica e, na maioria dos casos, ela \u00e9 apenas uma troca invis\u00edvel de influ\u00eancia. Voc\u00ea deixa de obedecer aos pais e passa a obedecer ao mercado, a redes, \u00e0s tend\u00eancias, \u00e0s conversas de escrit\u00f3rio, ao podcast em alta.

N\u00e3o h\u00e1 culpa nesse comportamento, n\u00e3o se trata de um defeito individual. O c\u00e9rebro humano \u00e9 uma m\u00e1quina de economia da energia: ele aceita o que \u00e9 repetido antes de examinar o que \u00e9 verdade. E o ambiente opera exatamente nesse reino silencioso. Quem voc\u00ea escuta com const\u00e2ncia, o que v\u00ea todos os dias, como as pessoas ao redor falam de futuro, tempo, dinheiro e sucesso \u2014 isso entra dentro de voc\u00ea como um c\u00f3digo fonte, determinando quais decis\u00f5es parecer\u00e3o coerentes ou imposs\u00edveis.

Pergunte-se: quais s\u00e3o os cinco \"objetivos\" que voc\u00ea persegue hoje? Agora, diga de onde vieram cada um deles. Voc\u00ea chegou a essa meta movido por uma convic\u00e7\u00e3o interna, ou ela foi o que todo mundo ao redor j\u00e1 tinha decidido como \"certo\" para voc\u00ea? A diferen\u00e7a entre aproxima\u00e7\u00e3o e imposi\u00e7\u00e3o \u00e9 t\u00e3o violenta quanto discreta. O ambiente n\u00e3o precisa explicar; ele precisa estar em toda parte.

## Mude o Terreno para que a Dire\u00e7\u00e3o Mude

Ningu\u00e9m espera que um peixe mude de bairro. A \u00e1guia de grande porte n\u00e3o procura um lugar rasteiro para viver \u2014 ela busca altitude. A mudan\u00e7a fundamental n\u00e3o \u00e9 f\u00edsica, \u00e9 mental. A verdadeira altitude \u00e9 dist\u00e2ncia emocional.

Quando voc\u00ea ganha altitude, passa a enxergar as pessoas e as cren\u00e7as n\u00e3o como \"fatos\", mas como reflexos do horizonte em que elas foram formadas. Passa a n\u00e3o responder com a urg\u00eancia que os outros sentem. Passa a escolher, diante de uma cr\u00edtica, indagar: \"essa palavra \u00e9 um espelho ou uma janela?\" O ambiente deixa de ser algo que voc\u00ea teme e passa a ser algo que voc\u00ea interroga.

A \u00e1guia voa muito alto, mas n\u00e3o porque tem asas maiores. Ela voa porque entendeu que o ch\u00e3o \u00e9 um convite \u00e0 dispers\u00e3o: no ch\u00e3o, barulho aqui, grito ali, caminho pr\u00f3ximo \u2014 tudo te consome. Com altura, ela ganha clareza para ver o que importa.

## Blindagem Mental: A Pr\u00e1tica de Escolher o que Entra

Se a \u00e1guia tem um habitat, a mente humana tem uma porta de entrada. Nada \u00e9 mais parecido com a liberdade do que aprender a controlar essa porta. Enquanto voc\u00ea n\u00e3o decide o que entra, distra\u00e7\u00f5es entram f\u00e1cil como vento \u2014 mas tamb\u00e9m vozes, opini\u00f5es, medos alheios e, principalmente, a pequena certeza do outro de que voc\u00ea n\u00e3o pode ir al\u00e9m.

Excel\u00eancia n\u00e3o \u00e9 n\u00e3o receber influ\u00eancia \u2014 isso \u00e9 imposs\u00edvel. \u00c9 **blindagem real**: um acordo interno sobre o que merece aten\u00e7\u00e3o e o que deve passar. Quem decide primeiro n\u00e3o \u00e9 o estado do que algu\u00e9m gostou ou n\u00e3o gostou, mas sim que tipo de pessoa voc\u00ea precisa se tornar. Se o seu objetivo \u00e9 construir uma mentalidade de longo prazo, voc\u00ea expande o ambiente de longo prazo: pessoas mais velhas que j\u00e1 viveram o que voc\u00ea sonha, livros que incomodam a quietude, sil\u00eancio criativo entre as distra\u00e7\u00f5es.

N\u00e3o existe neutralidade: ou voc\u00ea seleciona os seus ambientes, ou eles te selecionam. Quem deixa que tudo entre n\u00e3o escolheu a mente aberta \u2014 escolheu a aus\u00eancia de crit\u00e9rio. A \u00e1guia \u00e9 distinta, e por isso exige dist\u00e2ncia \u2014 n\u00e3o por desprezar, mas para reconhecer o que o ambiente est\u00e1 pedindo a ela. O que o seu ambiente est\u00e1 pedindo de voc\u00ea?

## A Voz do Meio e a Liberdade Verdadeira

Existe um contraste inevit\u00e1vel entre a Mentalidade de \u00c1guia e a Mentalidade de Galinha. A galinha tem medo de tudo e come qualquer ra\u00e7\u00e3o jogada no terreiro. Ela voa pouqu\u00edssimo, rente ao ch\u00e3o. Muita gente chama isso de seguran\u00e7a. N\u00e3o \u00e9. \u00c9 apenas a repeti\u00e7\u00e3o do pr\u00f3ximo passo sem questionar se esse caminho leva a algum lugar.

A galinha espera a porteira existir para se sentir segura. A \u00e1guia, por sua vez, encontra seguran\u00e7a na pr\u00f3pria vis\u00e3o \u2014 a claridade para ler o c\u00e9u e a vontade de se aperfei\u00e7oar dia ap\u00f3s dia. Ambas olham para o mesmo mundo, mas uma enxerga o limite do cercado e a outra enxerga a diferen\u00e7a de altitude.

N\u00e3o pergunte se o seu ambiente \u00e9 \"bom\" ou \"ruim\". Pergunte se ele \u00e9 compat\u00edvel com a rota onde voc\u00ea quer chegar. Se ele n\u00e3o est\u00e1 sustentando novos h\u00e1bitos, novas conversas, novos padr\u00f5es de resposta \u2014 ele est\u00e1 te freando, n\u00e3o te carregando.

## Depois da Clareza, a Decis\u00e3o

Se voc\u00ea leu at\u00e9 aqui, \u00e9 imposs\u00edvel n\u00e3o ter sido incomodado em algum canto: voc\u00ea reconheceu que ainda opera com instru\u00e7\u00f5es do passado. Talvez voc\u00ea tenha sentido aquela pequena vertigem de perceber que seu melhor ainda encontra teto nas respostas que os outros j\u00e1 deram \u2014 e que talvez, sim, voc\u00ea esteja tratando o ambiente como destino, n\u00e3o como ponto de partida.

A boa not\u00edcia \u00e9 que territ\u00f3rio n\u00e3o \u00e9 destino: voc\u00ea pode mover o ninho. Voc\u00ea come\u00e7a pequeno \u2014 ignorar o que n\u00e3o acrescenta, criar espa\u00e7os de sil\u00eancio no caos, escolher conversar menos com quem n\u00e3o quer te ver crescer, e encher de inten\u00e7\u00e3o o que antes era autom\u00e1tico. Voc\u00ea n\u00e3o precisa romper tudo de uma vez \u2014 basta ver mais longe.

Liberdade, na Mentalidade de \u00c1guia, n\u00e3o \u00e9 aus\u00eancia de rela\u00e7\u00e3o com o mundo. Pelo contr\u00e1rio, \u00e9 a constru\u00e7\u00e3o de uma postura onde o mundo n\u00e3o decide por voc\u00ea. E essa renova\u00e7\u00e3o acontece quando voc\u00ea entende que a porta de entrada que voc\u00ea abre para o mundo \u00e9 uma escolha que voc\u00ea faz \u2014 ou deixa de fazer \u2014 todos os dias.

E agora? A pergunta final que voc\u00ea n\u00e3o deve escapar: **N\u00e3o \u00e9 o que voc\u00ea teme que decide. N\u00e3o \u00e9 nem o que voc\u00ea deseja que decide. O que importa \u00e9 o que voc\u00ea permite entrar, todos os dias, nessa pequena solid\u00e3o que se chama eu.**

Voc\u00ea est\u00e1, como a \u00e1guia, escolhendo a altitude? Ou est\u00e1 acomodado no terreiro do voo baixo, t\u00e3o seguro olhando os outros, que nem percebeu que voc\u00ea parou de usar as asas? O triste n\u00e3o \u00e9 o erro \u2014 \u00e9 esperar liberdade sem mudar de altitude.

---

## O Ponto de Partida Est\u00e1 Aqui

Tudo que voc\u00ea leu \u00e9 apenas o come\u00e7o. **O C\u00f3digo \u00c1guia** aprofunda cada um desses princ\u00edpios com clareza, exemplos reais e um roteiro pr\u00e1tico para quem quer mudar de n\u00edvel de verdade \u2014 n\u00e3o amanh\u00e3, mas agora. Se a \u00e1guia est\u00e1 dentro de voc\u00ea, est\u00e1 na hora de libert\u00e1-la. Acesse O C\u00f3digo \u00c1guia e comece hoje.
`,
  },
];
