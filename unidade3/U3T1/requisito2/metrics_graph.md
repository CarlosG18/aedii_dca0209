# Analizando algumas métricas do grafo

> Com o auxilio do gephi, foi possivel calcular algumas métricas importantes sobre o grafo tanto quantitativamente quanto visualmente.

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

filtros aplicados (seção **filters**: `Library/Attributes/Range/`) nas métricas para ser possivel observar alguns nós individualmente:

|        Métrica        | Mínimo | Máximo |
| :--------------------: | :-----: | :-----: |
| Eigenvector Centrality |  0.923  |  1.00  |
|  Closeness Centrality  |  1.00  |  1.00  |
| Betweenness Centrality |  0.39  |  1.00  |
|   Degree Centrality   |   604   |  1005  |

## 🔍 Algumas interpretações e observações sobre as imagens das métricas acima

### [1/4] 🔹 Degree Centrality

Analizando o imagem da rede usando o **grau do nó** como métrica principal, podemos ver que **musica romântica** é a pagina que possui mais vizinhos (maior grau), isso significa que a musica romantica tem uma boa influência no mundo musical. outras páginas também são bem relevantes como:

    - Richard Wagner;
    - Franz Schubert;
    - Johannes Brahms;
    - Robert Schumann;
    - Nikolai Rimsky-Korsakov

Podemos ver que as páginas citadas são compositores de musicas clássicas, e isso esta coerente com as SEEDS ultilizadas, pois os acordes dimninutos, harmonial funcional e acordes aumentados possuem uma grande relevância e influência na música classica. A página **the beach boys** se contrapoẽ e sai um pouco dessa linha de compositores de música clássica partindo para um gênero Rock pop, voltado para uma cultura mais estadunidense e praiana.

### [2/4] 🔹 Closeness Centrality

O closeness centrality é a propriedade do grafo que indica o quanto o nó está próximo dos outros nós da rede, ou seja, é uma propriedade essencial para entender se aquele nó é um agente de disseminação de informação ou se possui um bom acesso a outros nós. Analisando a imagem sobre o Closeness Centrality, podemos observar que varios páginas possuem um valor alto referente a essa métrica. as páginas que possuem os maiores valores são:

    - 1º Dido e Enéias (ópera);
    - 2º Cadência;
    - 3º Hermann von Helmholtz (matemático, médico e físico alemão);
    - 4º Delta Lady - Música
    - 5º Louis Vierne - compositor

podemos analisar que diferentemente do Degree Centrality não se tem um "grupo" especifico, ou seja, as 5 páginas que possuem os maiores valores para a métrica do Closeness Centrality não possuem um grupo em particular, e sim grupos diferentes como compositores, musica, ópera...

### [3/4] 🔹 Betweenness Centrality

### [4/4] 🔹 Eigenvector Centrality
