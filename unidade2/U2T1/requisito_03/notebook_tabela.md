# Tabela com metricas dos grafos estudados

⬅️ [Readme principal](../u2t1.md)
⬅️ [Readme tabela](./tabela.md)

```python
!pip install networkx
!pip install pandas
!pip install matplotlib
!pip install seaborn
```

    Requirement already satisfied: networkx in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (3.3)
    Requirement already satisfied: pandas in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (2.2.2)
    Requirement already satisfied: numpy>=1.26.0 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from pandas) (2.0.1)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from pandas) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from pandas) (2024.1)
    Requirement already satisfied: tzdata>=2022.7 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from pandas) (2024.1)
    Requirement already satisfied: six>=1.5 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
    Requirement already satisfied: matplotlib in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (3.9.1)
    Requirement already satisfied: contourpy>=1.0.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (1.2.1)
    Requirement already satisfied: cycler>=0.10 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (4.53.1)
    Requirement already satisfied: kiwisolver>=1.3.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (1.4.5)
    Requirement already satisfied: numpy>=1.23 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (2.0.1)
    Requirement already satisfied: packaging>=20.0 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (24.1)
    Requirement already satisfied: pillow>=8 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (10.4.0)
    Requirement already satisfied: pyparsing>=2.3.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (3.1.2)
    Requirement already satisfied: python-dateutil>=2.7 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib) (2.9.0.post0)
    Requirement already satisfied: six>=1.5 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
    Requirement already satisfied: seaborn in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (0.13.2)
    Requirement already satisfied: numpy!=1.24.0,>=1.20 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from seaborn) (2.0.1)
    Requirement already satisfied: pandas>=1.2 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from seaborn) (2.2.2)
    Requirement already satisfied: matplotlib!=3.6.1,>=3.4 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from seaborn) (3.9.1)
    Requirement already satisfied: contourpy>=1.0.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.2.1)
    Requirement already satisfied: cycler>=0.10 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (4.53.1)
    Requirement already satisfied: kiwisolver>=1.3.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.4.5)
    Requirement already satisfied: packaging>=20.0 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (24.1)
    Requirement already satisfied: pillow>=8 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (10.4.0)
    Requirement already satisfied: pyparsing>=2.3.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (3.1.2)
    Requirement already satisfied: python-dateutil>=2.7 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from pandas>=1.2->seaborn) (2024.1)
    Requirement already satisfied: tzdata>=2022.7 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from pandas>=1.2->seaborn) (2024.1)
    Requirement already satisfied: six>=1.5 in /home/eduardo09/gabriel/ufrn/semestres/2024.1/aed2/aedii_dca0209/venv/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib!=3.6.1,>=3.4->seaborn) (1.16.0)

```python
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

```python
# Funções auxiliares

def create_graph(dataframe):
    """
        função para criar o grafo de co-autoria

        args:
            - dataframe: dataframe relacionado a ODS
          
        return:
            - graph: grafo de co-autoria
    """
    graph = nx.Graph()

    for index, row in dataframe.iterrows():
        autores = row["Authors"].split(";")
        for autor in autores:
            # criando os nós do grafo sobre a ods_1
            graph.add_node(autor)
  
        for i, autor1 in enumerate(autores):
            for j, autor2 in enumerate(autores):
                if j != i:
                    graph.add_edge(autor1,autor2)
      
    return graph

def calculate_network_metrics(G):
    """
        Função para calcular as métri
        cas da rede

        args: 
            - G: grafo a ser obtido as metricas

        return: 
            - dicionario com todas as informações do grafo G.
    """
  
    # Número de vértices (nós)
    num_vertices = G.number_of_nodes()

    # Número de arestas
    num_edges = G.number_of_edges()

    # Degree assortativity coefficient
    assortativity = nx.degree_assortativity_coefficient(G)

    # Número de componentes conectados
    num_connected_components = nx.number_connected_components(G)

    # Tamanho do maior componente conectado (GCC)
    largest_cc = max(nx.connected_components(G), key=len)
    size_largest_cc = len(largest_cc)

    # Coeficiente de clustering médio
    avg_clustering = nx.average_clustering(G)

    return {
        "Qtd Vértices": num_vertices,
        "Qtd Arestas": num_edges,
        "Degree Assortativity Coefficient": assortativity,
        "Qtd Comp. Conectados": num_connected_components,
        "Tamanho do Comp. Gigante (GCC)": size_largest_cc,
        "Coef. de Clustering": avg_clustering
    }


```

```python
# obtendo os dataframes
data_frame1 = pd.read_csv('../datasets/ods_1.csv')
data_frame2 = pd.read_csv('../datasets/ods_2.csv')
data_frame9 = pd.read_csv('../datasets/ods_9.csv')
data_frame11 = pd.read_csv('../datasets/ods_11.csv')

# criando os grafos
ods1_graph = create_graph(data_frame1)
ods2_graph = create_graph(data_frame2)
ods9_graph = create_graph(data_frame9)
ods11_graph = create_graph(data_frame11)

# obtendo as metricas dos grafos
metrics_ods1_graph = calculate_network_metrics(ods1_graph)
metrics_ods2_graph = calculate_network_metrics(ods2_graph)
metrics_ods9_graph = calculate_network_metrics(ods9_graph)
metrics_ods11_graph = calculate_network_metrics(ods11_graph)
```

```python
# Criar um DataFrame para apresentar as métricas
df_metrics = pd.DataFrame([metrics_ods1_graph, metrics_ods2_graph, metrics_ods9_graph, metrics_ods11_graph],
                          index=['ODS 1', 'ODS 2', 'ODS 9', 'ODS 11'])

print(df_metrics)
```

    Qtd Vértices  Qtd Arestas  Degree Assortativity Coefficient
    ODS 1            432         1622                          0.900929
    ODS 2           1869        45126                          0.988612
    ODS 9           1825         6119                          0.079773
    ODS 11          2095        39679                          0.997434

    Qtd Comp. Conectados  Tamanho do Comp. Gigante (GCC)
    ODS 1                     60                              54
    ODS 2                    117                            1052
    ODS 9                    184                             404
    ODS 11                   206                             247

    Coef. de Clustering
    ODS 1              0.882728
    ODS 2              0.945777
    ODS 9              0.910081
    ODS 11             0.911539
