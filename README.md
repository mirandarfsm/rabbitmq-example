### Event-driven Microservice

#### O que é Event-driven Microservice?

Na arquitetura orientada a eventos (event-driven architecture), quando um serviço executa algum trabalho em que outros serviços possam estar interessados, esse serviço produz um evento - um registro da ação executada. Outros serviços consomem esses eventos para que eles possam executar qualquer uma de suas próprias tarefas necessárias como resultado do evento. Diferentemente do REST, os serviços que criam solicitações não precisam conhecer os detalhes dos serviços que estão consumindo as solicitações.

Aqui está um exemplo simples: quando um pedido é feito em um site de comércio eletrônico, um único evento de "pedido feito" é produzido e depois consumido por vários microsserviços:

1.  serviço de pedidos que pode gravar um registro de pedidos no banco de dados
1.  serviço ao cliente que pode criar o registro do cliente e
1.  serviço de pagamento que pode processar o pagamento.

Os eventos podem ser publicados de várias maneiras. Por exemplo, eles podem ser publicados em uma fila que garanta a entrega do evento aos consumidores apropriados, ou podem ser publicados em um fluxo de modelo "pub / sub" que publica o evento e permite acesso a todas as partes interessadas. Em ambos os casos, o produtor publica o evento e o consumidor recebe esse evento, reagindo de acordo. Observe que, em alguns casos, esses dois atores também podem ser chamados de *publisher* (produtor) e *subscriber* (consumidor).

#### Para que serve?

Uma arquitetura orientada a eventos oferece várias vantagens sobre o REST, que incluem:

*  **Asynchronous** - as arquiteturas baseadas em eventos são assíncronas sem bloqueio. Isso permite que os recursos se movam livremente para a próxima tarefa quando a unidade de trabalho estiver concluída, sem se preocupar com o que aconteceu antes ou que acontecerá a seguir. Eles também permitem que os eventos sejam enfileirados ou armazenados em buffer, o que impede que os consumidores pressionem os produtores ou os bloqueiem.

*  **Loose Coupling** - os serviços não precisam (e não deveriam ter) conhecimento ou dependências de outros serviços. Ao usar eventos, os serviços operam independentemente, sem o conhecimento de outros serviços, incluindo seus detalhes de implementação e protocolo de transporte. Os serviços em um modelo de evento podem ser atualizados, testados e implantados de forma independente e mais fácil.

*  **Easy Scaling** - Como os serviços são dissociados em uma arquitetura orientada a eventos e, como os serviços normalmente executam apenas uma tarefa, rastrear gargalos para um serviço específico e escalonar esse serviço (e somente esse serviço) se torna fácil.

*  **Recovery support** - Uma arquitetura orientada a eventos com uma fila pode recuperar o trabalho perdido "repetindo" eventos do passado. Isso pode ser valioso para evitar a perda de dados quando um consumidor precisar se recuperar.

Obviamente, as arquiteturas orientadas a eventos também têm desvantagens. Eles são fáceis de projetar demais, separando preocupações que podem ser mais simples quando intimamente acopladas; pode exigir um investimento inicial significativo; e geralmente resultam em complexidade adicional em infraestrutura, contratos ou esquemas de serviço, sistemas de construção poliglota e gráficos de dependência.

Talvez a maior desvantagem e desafio seja o gerenciamento de dados e transações. Devido à sua natureza assíncrona, os modelos controlados por eventos devem manipular cuidadosamente dados inconsistentes entre serviços, versões incompatíveis, observar eventos duplicados e normalmente não suportam transações ACID, ao invés disso, oferecem suporte a uma consistência eventual que pode ser mais difícil de rastrear ou depurar.

Mesmo com essas desvantagens, uma arquitetura orientada a eventos geralmente é a melhor opção para sistemas de microsserviço de nível corporativo. Os pros - design amigável, escalável, com pouco acoplamento e design amigavel para *dev-ops*  - superam os contras.

### Jhipster e o Event-driven

Não foi encontrado muitas coisas nas pesquiesas de 'Jhipster + Event-driven'. Única coisa importante que foi encontrado foi uma *issue* aberta no projeto do jhipster no github. Link [Implement Asyncapi for Event-driven architecture](https://github.com/jhipster/generator-jhipster/issues/11112) 

![image](/uploads/8c81f28baa2f9764f69c6c76a92d1b4e/image.png)

Depois dessa conversa, decidir procurar sobre o 'Jhipster + Kafka', que foi mencionado no texto. Achei diversos sites sobre a implementação, inclusive uma página do próprio Jhipster que menciona o [kafka](https://www.jhipster.tech/using-kafka/). Resolvi iniciar um projeto jhipster com Kafka.

Seguindo a página do próprio jhipster, temos os seguintes comandos:

![image](/uploads/94e283464ab2a70c44b2d12982a6cebc/image.png)

Segui esses passos:

```
? Which *type* of application would you like to create? Monolithic application (recommended for simple pr
ojects)
? [Alpha] Do you want to make it reactive with Spring WebFlux? No
? What is the base name of your application? myapp
? What is your default Java package name? com.mycompany.myapp
? Do you want to use the JHipster Registry to configure, monitor and scale your application? No
? Which *type* of authentication would you like to use? JWT authentication (stateless, with a token)
? Which *type* of database would you like to use? SQL (H2, MySQL, MariaDB, PostgreSQL, Oracle, MSSQL)
? Which *production* database would you like to use? PostgreSQL
? Which *development* database would you like to use? H2 with disk-based persistence
? Do you want to use the Spring cache abstraction? Yes, with the Ehcache implementation (local cache, for
 a single node)
? Do you want to use Hibernate 2nd level cache? Yes
? Would you like to use Maven or Gradle for building the backend? Maven
? Which other technologies would you like to use? Asynchronous messages using Apache Kafka
? Which *Framework* would you like to use for the client? Angular
? Would you like to use a Bootswatch theme (https://bootswatch.com/)? Default JHipster
? Would you like to enable internationalization support? Yes
? Please choose the native language of the application Portuguese (Brazilian)
? Please choose additional languages to install (Press <space> to select, <a> to toggle all, <i> to inver
t selection)
? Besides JUnit and Jest, which testing frameworks would you like to use? (Press <space> to select, <a> t
o toggle all, <i> to invert selection)
? Would you like to install other generators from the JHipster Marketplace? No

```

### Spring Integration & Spring Cloud Stream

A jornada da Spring na integração de dados começou com a Spring Integration. Com seu modelo de programação, ele forneceu uma experiência consistente ao desenvolvedor para criar aplicativos que podem adotar os Padrões de Integração Corporativa para conectar-se a sistemas externos, como bancos de dados, *message brokers* e outros.

Acançando rapidamente para a era da nuvem, onde os microsserviços se tornaram proeminentes no cenário corporativo. O Spring Boot transformou a maneira como os desenvolvedores criam aplicativos. Com o modelo de programação do Spring e as responsabilidades de tempo de execução tratadas pelo Spring Boot, tornou-se fácil o desenvolvimento de microsserviços autônomos e baseados em Spring com nível de produção.

Para estender isso às cargas de trabalho de integração de dados, o Spring Integration e o Spring Boot foram reunidos em um novo projeto, o Spring Cloud Stream.

Com o Spring Cloud Stream, os desenvolvedores podem: 
* Criar, testar, iterar e implantar aplicativos centrados em dados isoladamente. 
* Aplique padrões modernos de arquitetura de microsserviços, incluindo composição através de mensagens. 
* Dissocie as responsabilidades do aplicativo com o pensamento centrado no evento. Um evento pode representar algo que aconteceu com o tempo, para o qual os aplicativos de consumidor a jusante podem reagir sem saber onde se originou ou a identidade do produtor. 
* Coloque a lógica de negócios para os *message brokers* (como RabbitMQ, Apache Kafka, Amazon Kinesis).

O Spring Stream parece ser ótimo. Com ele é possivel abstrair a configuração de qualquer *message broker*, isso quer dizer, nós podemos trocar de *message broker* sem mudar nosso sitema.

São tantos beneficios que é dificil descrever todos aqui, mas por que o Jhipster não utiliza o Spring Stream?

#### Spring Stream é muito abstrato

Ao explorar o projeto criado, vi que a implementação do kafka estava lá, porem uma coisa me deixou pensativo. O kafka estava implementado, porem sem o uso do Spring Stream, era um pacote avulso. Então resolvi realizar uma nova pesquisa, 'Jhipster Spring Kafka'. Após alguns cliques, consigo achar o motivo por não usarem Spring Stream comentada nesta issue [Migrate from spring-cloud-stream to native Apache Kafka client](https://github.com/jhipster/generator-jhipster/issues/9287).

![image](/uploads/31f8b09f36838a8481a509c6cf71d397/image.png)

### Mas o que é Kafka?

O Apache Kafka é uma plataforma de streaming distribuída. Foi inicialmente concebido como uma fila de mensagens e de código aberto pelo LinkedIn em 2011. Sua comunidade desenvolveu o Kafka para fornecer os principais recursos:

*  ***Publish and Subscribe*** stream de registros, como uma fila de mensagens.

*  ***Storage system*** para que as mensagens possam ser consumidas de forma assíncrona. Kafka grava dados em uma estrutura de disco escalável e replica para tolerância a falhas. Os produtores podem esperar pelos reconhecimentos de gravação.

*  ***Stream processing*** com a API Kafka Streams permite agregações ou junções complexas de fluxos de entrada em um fluxo de saída de dados processados.

Os modelos de mensagens tradicionais são *queue* e *publish-subscribe*. Em uma *queue*, cada registro vai para um consumidor. Na *publish-subscribe*, o registro é recebido por todos os consumidores.

O *Consumer Group* em Kafka é uma abstração que combina os dois modelos. O processamento de registros pode ser balanceado por carga entre os membros de um grupo de consumidores, e o Kafka permite transmitir mensagens para vários grupos de consumidores. É a mesma semântica de *publish-subscribe* em que o assinante é um cluster de consumidores em vez de um único processo.

Os casos de uso populares do Kafka incluem:

*  O sistema de mensagens tradicional, para separar os *producers* dos processadores com melhor latência e escalabilidade.

*  Rastreamento de atividade do site com *feeds* de *publish-subscribe* em tempo real

*  Como um substituto para a agregação de log baseada em arquivo, em que os dados do evento se tornam um fluxo de mensagens

*  *Pipelines* de dados em que os dados consumidos dos tópicos são transformados e alimentados para novos tópicos

*  Como um *log* de confirmação externo para um sistema distribuído

*  Como um armazenamento de *log* de *back-end* para aplicativos de fornecimento de eventos, onde cada alteração de estado é registrada na ordem do tempo.

### E o RabbitMQ?

O RabbitMQ é muito falado como um das melhores ferramentas de event-driven e de fácil compreenção. Vamos aprender um pouco sobre ele. 

#### Entendo um pouco de RabbitMQ

O RabbitMQ é um software de enfileiramento de mensagens, também conhecido como intermediário de mensagens ou gerenciador de filas. Simplesmente falando, é um software onde as filas são definidas, às quais os aplicativos se conectam para transferir uma mensagem ou mensagens.

![image](/uploads/79a5d6124f901b1ca82e11649096d1eb/image.png)

Uma mensagem pode incluir qualquer tipo de informação. Pode, por exemplo, ter informações sobre um processo ou tarefa que deve iniciar em outro aplicativo (que pode até estar em outro servidor) ou pode ser apenas uma simples mensagem de texto. O software gerenciador de filas armazena as mensagens até que um aplicativo receptor se conecte e retire uma mensagem da fila. O aplicativo de recebimento processa a mensagem.

#### Exchanges

As mensagens não são publicadas diretamente em uma fila; em vez disso, o produtor envia mensagens para uma *exchange*. Uma *exchange* é responsável por rotear as mensagens para diferentes filas com a ajuda de *binding* e *routing keys*. Uma *binding* é um link entre uma fila e uma *exchange*.


#### Fluxo de mensagens no RabbitMQ

1. O produtor publica uma mensagem em uma *exchange*.

1. A *exchange* recebe a mensagem e agora é responsável pelo roteamento da mensagem.

1. Os *binding* (ligações) devem ser criadas da *exchange* para as filas.

1. As mensagens permanecem na fila até serem tratadas por um consumidor

1. O consumidor lida com a mensagem.

![image](/uploads/536b10ec72351a8a3c49f70ffb343036/image.png)

#### Tipos de Exchanges

*  ***Direct***: a mensagem é roteada para as filas cuja chave de ligação corresponde exatamente à chave de roteamento da mensagem.

*  ***Fanout***: uma *exchange* de fanout roteia mensagens para todas as filas ligadas a ele. *Broadcast*.

*  ***Topic***: A *exchange* de tópicos faz uma correspondência curinga entre a chave de roteamento e o padrão de roteamento especificado na ligação.

*  ***Headers***: as *exchange* de cabeçalhos usam os atributos de cabeçalho da mensagem para roteamento.

#### CONCEITOS RABBITMQ E SERVIDOR

Alguns conceitos importantes precisam ser descritos antes de nos aprofundarmos no RabbitMQ. Vamos examinar os elementos e conceitos:

*  ***Producer***: Aplicativo que envia as mensagens.

*  ***Consumer***: Aplicativo que recebe as mensagens.

*  ***Queue***: Buffer/Fila que armazena mensagens.

*  ***Message***: Informações enviadas do *producer* para um *consumer* através do RabbitMQ.

*  ***Connection***: Uma conexão TCP entre seu aplicativo e o *broker* RabbitMQ.

*  ***Channel***: Uma conexão virtual dentro de uma conexão. Ao publicar ou consumir mensagens de uma fila, tudo é feito em um canal. É necessário para uma conexão duplex, veja mais em [What is the difference between simplex and duplex multiplexers?
](https://specialties.bayt.com/en/specialties/q/7465/what-is-the-difference-between-simplex-and-duplex-multiplexers/)

*  ***Exchange***: recebe mensagens dos *producers* e as empurra para as *queues*, dependendo das regras definidas pelo tipo de *exchange*. Para receber mensagens, uma *queues* precisa estar vinculada a pelo menos uma *exchange*.

*  ***Binding***: É um link entre uma *queue* e uma *exchange*.

*  ***Routing key***: uma chave que a *exchange* analisa para decidir como rotear a mensagem para as filas. Pense na *routing key* como um endereço para a mensagem.

*  ***AMQP***: Advanced Message Queuing Protocol é o protocolo usado pelo RabbitMQ para envio de mensagens.

*  ***Users***: É possível conectar-se ao RabbitMQ com um nome de usuário e senha. Cada usuário pode receber permissões como direitos de leitura, gravação e configuração de privilégios na instância. Os usuários também podem receber permissões para hosts virtuais específicos.

*  ***Vhost, virtual host***: fornece uma maneira de segregar aplicativos usando a mesma instância RabbitMQ. Usuários diferentes podem ter permissões diferentes para diferentes vhost e filas e trocas podem ser criadas, portanto, elas existem apenas em um vhost.


#### Spring AMQP

O projeto Spring AMQP aplica os principais conceitos do Spring ao desenvolvimento de soluções de mensagens baseadas em AMQP. Nós fornecemos um "modelo" como uma abstração de alto nível para enviar e receber mensagens. Também fornecemos suporte para POJOs baseados em mensagens. Essas bibliotecas facilitam o gerenciamento de recursos AMQP, promovendo o uso de injeção de dependência e configuração declarativa. Em todos esses casos, é possível ver semelhanças com o suporte ao JMS no Spring Framework. Para outras informações relacionadas ao projeto, visite a página inicial do projeto Spring AMQP.

### Spring AMQP x Spring Cloud Stream

O Spring Cloud Stream é um framework mais abstrato, não sendo especifico ao protocolo AMQP, o qual o RabbitMQ trabalha. Alguns dizem ainda que o Spring Cloud Stream foi feita para trabalhar com stream e não com mensagem, exemplo [What benefits does Spring AMQP have over Spring Cloud Stream for Microservices Architecture](https://stackoverflow.com/questions/44275033/what-benefits-does-spring-amqp-have-over-spring-cloud-stream-for-microservices-a)

![image](/uploads/f8513a3aefecc63a938bb46ac8560330/image.png)

Porem ele é bem mais fácil de trabalhar e integrar ao sistema.

Já o framework Spring AMQP reflete totalmente o RabbitMQ. Nele teríamos como utilizar todas as funcionalidades do RabbitMQ.

### Conclusão

No artigo, nós vimos que a arquitetura event-driven traz bastante vantagem ao nosso software. Vimos que o Jhipster recomenda o software Kafka, mas tem suporte aos outros softwares com o framework Spring Cloud Stream. Concluimos que o Spring Cloud Stream tem suas limitações. E que temos o Amqp para uma implementação mais completa.

Temos bastante recurso para montar o event-driven no nosso software, porem as escuras é dificil decidir uma. Então, para implementarmos mensageria no app Spring JHipster, sugiro seguir os seguintes passos:

1.  Definir uma Arquitetura de comunicação;
1.  Escolher qual Ferramenta utilizar (kafka, Rabbitmq); e
1.  Definir o Framework que utilizaremos (Spring Stream, Spring AMQP, kafka-clients)

#### Possível arquitetura

![Event-driven_Arch](/uploads/f1d74e027038aefcdaffe60d90520c65/Event-driven_Arch.png)

Todo o código realizado foi disponibilizado [aqui](https://github.com/mirandarfsm/spring-event-driven/):

*  [Kafka](https://github.com/mirandarfsm/spring-event-driven/tree/kafka)
*  [Spring Cloud Stream + RabbitMQ](https://github.com/mirandarfsm/spring-event-driven/tree/spring-cloud-rabbitmq)

### Referências

[Best Practices for Event-Driven Microservice Architecture](https://hackernoon.com/best-practices-for-event-driven-microservice-architecture-e034p21lk)

[Implement Asyncapi for Event-driven architecture](https://github.com/jhipster/generator-jhipster/issues/11112)

[Jhipster: Using Kafka](https://www.jhipster.tech/using-kafka/)

[Communicate Between Microservices with Apache Kafka](https://developer.okta.com/blog/2020/01/22/kafka-microservices)

[JHipster – Streaming beer with Kafka and Spring Cloud Stream](https://rphgoossens.wordpress.com/2018/05/25/jhipster-streaming-beer-with-kafka-and-spring-cloud-stream/)

[JHipster – Making things a little less hip](https://rphgoossens.wordpress.com/2018/06/18/jhipster-making-things-a-little-less-hip/)

[Spring Book: Spring Cloud Stream](https://cloud.spring.io/spring-cloud-static/Hoxton.RELEASE/reference/htmlsingle/#spring-cloud-stream-2)

[Spring Cloud Stream: Simplificando o uso de Message Broker — Parte 1](https://medium.com/@jvoliveiran/spring-cloud-stream-simplificando-o-uso-de-message-broker-71f1731f5f5)

[Part 1: RabbitMQ for beginners - What is RabbitMQ?](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)

[What is the difference between simplex and duplex multiplexers?
](https://specialties.bayt.com/en/specialties/q/7465/what-is-the-difference-between-simplex-and-duplex-multiplexers/)

[AMQP 0-9-1 Model Explained](https://www.rabbitmq.com/tutorials/amqp-concepts.html)

[Spring Book: Spring AMQP](https://docs.spring.io/spring-amqp/reference/html/)

[Stack Overflow: Spring Cloud Stream Reactive, how to set routing key for producer](https://stackoverflow.com/a/52338664/11562103)

[Spring-Cloud-Stream and Spring-AMQP: the good, the bad and the ugly](https://osoco.es/thoughts/2018/06/spring-cloud-stream-and-spring-amqp-the-good-the-bad-and-the-ugly/)

[What benefits does Spring AMQP have over Spring Cloud Stream for Microservices Architecture](https://stackoverflow.com/questions/44275033/what-benefits-does-spring-amqp-have-over-spring-cloud-stream-for-microservices-a)