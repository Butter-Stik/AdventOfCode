from aocd import get_data; import networkx as nx
G = nx.Graph()
x = [G.add_edge(connection[0], connection[1]) for connection in [[group for group in line.split('-')] for line in get_data(day=23,year=2024).splitlines()]]
print(",".join(sorted(nx.approximation.max_clique(G))))
