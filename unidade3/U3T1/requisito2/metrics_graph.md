# Analizando algumas métricas do grafo

> Com o auxilio do gephi, foi possível calcular algumas métricas importantes sobre o grafo tanto quantitativamente quanto visualmente.

## 🛠️ Usando o Gephi

Apos importar os dados do grafo no formato **graphml** para o gephi, foi aplicado o **layout**: ``ForceAtlas2``. Foi ativada a opção ``dissuade hubs`` para melhorar a visualização, já que existiam hubs que estavam sobrepondo outros. Na aba **Metrics** foi possivel calcular as seguintes métricas:

## 🔶 Degree Centrality, Closeness Centrality, Betweenness Centrality e Eigenvector Centrality

<p align="center">
    <img width=500 src="./imgs/degree_centrality/degree.svg"/>
    <img width=500 src="./imgs/closeness_centrality/closeness.svg"/>
</p>

<p align="center">
    <img width=500 src="./imgs/betweenness_centrality/betweenness.svg"/>
    <img width=500 src="./imgs/eigenvector_centrality/eigenvector.svg"/>
</p>

Foram aplicados os seguintes filtros (seção **filters**: `Library/Attributes/Range/`) nas métricas para ser possivel observar alguns nós individualmente:

|        Métrica        | Mínimo | Máximo |
| :--------------------: | :-----: | :-----: |
| Eigenvector Centrality |  0.923  |  1.00  |
|  Closeness Centrality  |  1.00  |  1.00  |
| Betweenness Centrality |  0.39  |  1.00  |
|   Degree Centrality   |   604   |  1005  |

### [1/4] 🔹 Degree Centrality

Analizando o imagem da rede usando o **grau do nó** como métrica principal, podemos ver que **música romântica** é a pagina que possui mais vizinhos (maior grau), isso significa que a música romântica tem uma boa influência no mundo musical. outras páginas também são bem relevantes como:

    - Richard Wagner;
    - Franz Schubert;
    - Johannes Brahms;
    - Robert Schumann;
    - Nikolai Rimsky-Korsakov

Podemos ver que as páginas citadas acima são compositores de musica clássica, e isso está coerênte com as SEEDS ultilizadas, pois os acordes dimninutos, harmonial funcional e acordes aumentados possuem uma grande relevância e influência na música classica. A página **the beach boys** se contrapoẽ e sai um pouco dessa linha de compositores de música clássica partindo para um gênero Rock pop, voltado para uma cultura mais popular e praiana.

### [2/4] 🔹 Closeness Centrality

O closeness centrality é a propriedade do grafo que indica o quanto o nó está próximo dos outros nós da rede, ou seja, é uma propriedade essencial para entender se aquele nó é um agente de disseminação de informação ou se possui um bom acesso a outros nós. Analisando a imagem sobre o Closeness Centrality, podemos observar que várias páginas possuem um valor alto referente a essa métrica. as páginas que possuem os maiores valores são:

    - 1º Dido e Enéias (ópera);
    - 2º Cadência;
    - 3º Hermann von Helmholtz (matemático, médico e físico alemão);
    - 4º Delta Lady - Música
    - 5º Louis Vierne - compositor

podemos analisar que diferentemente do Degree Centrality essas páginas não possuem um "grupo" em comum, indicando que os nós centrais do grafo pertence a "grupos váriados" e não esta relacionado apenas a um grupo específico.

### [3/4] 🔹 Betweenness Centrality

O Betweenness Centrality é uma métrica usada para definir a importância que um nó possui no menor caminho entre dois nós, ou seja, uma página que contem o valor do Betweenness Centrality elevado é uma página ponte que liga várias outras páginas, sendo considerada uma página bem relevânte para o tema geral que no nosso caso seria "música". Observando o imagem podemos observar que as páginas com os maiores valores para o Betweenness Centrality são:

    - 1º Rock Music
    - 2º Argument Triad
    - 3º the beach boys

A página "Rock Music" aparece como um nó central, o que pode indicar que a música popular, e especificamente o rock, possui uma interconexão significativa com tópicos sobre harmonia e acordes. Isso pode indicar que as páginas relacionadas a música popular agem como "pontes" conectando comunidades de interesse musical mais acadêmico ou especializado.

Com isso podemos levantar a hipotese de: **"se você quiser estudar Harmonial e acordes, um bom gênero para você começar seus estudos seria o Rock"**

### [4/4] 🔹 Eigenvector Centrality

O Eigenvector Centrality é uma métrica usada para analisar se uma página importante também está relacionado com outras páginas importantes. A Eigenvector Centrality neste grafo reflete a centralidade dos conceitos musicais em uma rede de conhecimento, destacando que páginas como tônica, dominante e acordes são fundamentais não apenas por si próprios, mas também por sua conexão com outros conceitos chave na teoria musical. Esses nós são cruciais para a estrutura do conhecimento musical, servindo como hubs de informação que conectam múltiplos subdomínios.
