from typing import List
import networkx as nx

def minimum_cost(N: int, M: int, A: List[int], C: List[int]) -> int:
    G = nx.DiGraph()
    # source node
    source = 0
    # target node
    target = N + M + 1
    # add edges from source to each item
    for i in range(1, N + 1):
        G.add_edge(source, i, weight=A[i-1], capacity=1)
    # add edges from each customer to target
    for i in range(N + 1, N + M + 1):
        G.add_edge(i, target, weight=0, capacity=1)
    # add edges from item to customer
    for i in range(1, N + 1):
        for j in range(N + 1, N + M + 1):
            G.add_edge(i, j, weight=C[j-N-1], capacity=1)
    # get minimum cost maximum flow
    flow_value, flow_dict = nx.network_simplex(G)
    # get minimum cost
    min_cost = sum(flow_dict[e]['flow'] * G[e[0]][e[1]]['weight'] for e in flow_dict)
    return min_cost