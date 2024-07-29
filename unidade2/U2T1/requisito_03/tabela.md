# Tabela de Caracteristicas da Rede

> Visualizando e Interpretando as informações advindas da Tabela de Caracteristicas da Rede

⬅️ [Readme principal](../u2t1.md)

[![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/CarlosG18/aedii_dca0209/blob/main/unidade2/U2T1/requisito_03/notebook_tabela.ipynb) - Notebook com os códigos sobre as metricas de cada grafo.

## 📈 Tabela com as metricas dos grafos

| Rede   | Qtd Vértices | Qtd Arestas | Degree Assortativity Coefficient | Qtd Comp. Conectados | Tamanho do Comp. Gigante (GCC) | Coef. de Clustering avg_clustering() |
|:------:|:------------:|:-----------:|:--------------------------------:|:--------------------:|:-------------------------------:|:-------------------------------------:|
| ODS  1 |    432       |    1622     |         0.900929                 |         60           |            54                   |                 0.882728              |
| ODS  2 |    1869      |    45126    |         0.988612                 |         117          |            1052                 |                 0.945777              |
| ODS  9 |    1825      |    6119     |         0.079773                 |         184          |            404                  |                 0.910081              |
| ODS 11 |    2095      |    39679    |         0.997434                 |         206          |            247                  |                 0.911539              |

# Análise das Redes de Colaboração nos ODS

A análise da tabela com as métricas dos grafos revela informações importantes sobre a estrutura de colaboração entre os pesquisadores nessas áreas das ODS. A análise será feita item por item para que o entendimento seja breve e direto.

## 🔹 Quantidade de Vértices e Arestas

O número de vértices representa o número de autores na rede, enquanto o número de arestas representa as coautorias ou colaborações entre eles. Redes com mais vértices e arestas indicam uma comunidade maior e mais colaborativa. Dessa forma, ao verificar a densidade das conexões, percebe-se que as redes de ODS 2 e ODS 11 são as mais densamente conectadas, com números elevados de vértices e arestas, indicando uma colaboração extensa e ativa. ODS 2, em particular, apresenta 1869 vértices e 45126 arestas, refletindo um alto grau de interação entre pesquisadores.

## 🔹 Coeficiente de Assortatividade de Grau

O coeficiente de assortatividade de grau é uma métrica que indica se autores com números semelhantes de coautorias tendem a colaborar entre si. Valores próximos de 1, como os encontrados nas redes de ODS 2 (0.988612) e ODS 11 (0.997434), mostram uma forte assortatividade positiva, sugerindo que autores altamente produtivos preferem colaborar com outros igualmente produtivos. Por outro lado, ODS 9, com um coeficiente de 0.079773, demonstra pouca preferência, indicando uma mistura mais diversa de colaborações.

## 🔹 Quantidade de Componentes Conectados e Tamanho do Componente Gigante (GCC)

Ambos fornecem uma visão sobre a fragmentação da rede. Sendo assim, ODS 2 possui um GCC de 1052, o maior entre as redes analisadas, indicando uma grande coesão entre os pesquisadores. Em contraste, ODS 1 tem um GCC de apenas 54, sugerindo uma maior fragmentação e menos coesão. ODS 9 e ODS 11 têm valores intermediários, com o GCC de ODS 9 sendo 404 e o de ODS 11 sendo 247.

## 🔹 Coeficiente de Clustering

O coeficiente de clustering médio indica a tendência dos pesquisadores de formarem grupos fechados de colaboração. Todas as redes apresentam altos valores de clustering, com ODS 2 liderando com 0.945777. Isso significa que é altamente provável que os coautores de um autor também colaborem entre si, formando subgrupos coesos.





