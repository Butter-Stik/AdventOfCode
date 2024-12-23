from aocd import get_data
import networkx as nx
G = nx.Graph()
inp = get_data(day=23,year=2024).splitlines()
connections = [[group for group in line.split('-')] for line in inp]

groups = []
found = []
p1 = 0
map = {}
for connection in connections:
    a, b = connection
    G.add_edge(a, b)
    if a not in map:
        links = []
        for c in connections:
            if a in c:
                link = c[0]
                if a == link:
                    link = c[1]
                links.append(link)
        map[a] = links
    if b not in map:
        links = []
        for c in connections:
            if b in c:
                link = c[0]
                if b == link:
                    link = c[1]
                links.append(link)
        map[b] = links
for connection in map:
    connected_nodes = map[connection]
    for node in connected_nodes:
        for n in connected_nodes:
            if node in map[n]:
                found.append((connection, node, n))
p1 = 0
for f in found:
    a, b, c = f
    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
        p1 += 1
print(p1 // 6)
set = nx.approximation.max_clique(G)
print(",".join(sorted(set)))
