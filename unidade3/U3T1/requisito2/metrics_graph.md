# Analizando algumas métricas do grafo

> Com o auxilio do gephi, foi possivel calcular algumas métricas importantes sobre o grafo tanto quantitativamente quanto visualmente.

## 🛠️ Usando o Gephi

Apos importar os dados do grafo no formato **graphml** para o gephi, foi aplicado o **layout**: ``ForceAtlas2``. Foi ativada a opção ``dissuade hubs`` para melhorar a visualização, já que existiam hubs que estavam sobrepondo outros. Na aba **Metrics** foi possivel calcular as seguintes métricas:

## 🔶 Degree Centrality, Closeness Centrality, Betweenness Centrality e Eigenvector Centrality

<p align="center">
    <img width=700 src="./imgs/degree_centrality/degree.svg"/>
    <img width=700 src="./imgs/closeness_centrality/closeness.svg"/>
</p>

<p align="center">
    <img width=700 src="./imgs/betweenness_centrality/betweenness.svg"/>
    <img width=700 src="./imgs/eigenvector_centrality/eigenvector.svg"/>
</p>

filtros aplicados (seção **filters**: `Library/Attributes/Range/`) nas métricas para ser possivel observar alguns nós individualmente:

|        Métrica         |      Mínimo       |      Máximo        |
| :--------------------: | :---------------: | :----------------: |
| Eigenvector Centrality |       0.923       |        1.00        |
|  Closeness Centrality  |        1.00       |        1.00        |
| Betweenness Centrality |       0.39        |        1.00        |
|   Degree Centrality    |        604        |        1005        |

##  🔍 Algumas interpretações e observações sobre as imagens das métricas acima

### [1/4] 🔹 Degree Centrality

Analizando o imagem da rede usando o 

### [2/4] 🔹 Closeness Centrality

### [3/4] 🔹 Betweenness Centrality

### [4/4] 🔹 Eigenvector Centrality
