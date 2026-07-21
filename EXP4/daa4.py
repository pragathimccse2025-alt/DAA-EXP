import heapq
import networkx as nx #type:ignore
import matplotlib.pyplot as plt #type:ignore


# -----------------------------
# Dijkstra Algorithm
# -----------------------------
def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


# -----------------------------
# Reconstruct Path
# -----------------------------
def reconstruct_path(prev, source, target):
    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# -----------------------------
# Graph
# -----------------------------
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = 0

dist, prev = dijkstra(graph, source)

print("\nShortest Paths\n")

for i in range(len(graph)):
    path = reconstruct_path(prev, source, i)
    print(f"Vertex {i}: Distance = {dist[i]}, Path = {path}")

# -----------------------------
# Draw Graph
# -----------------------------
G = nx.DiGraph()

for u in graph:
    for v, w in graph[u]:
        G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(8, 6))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Draw labels
nx.draw_networkx_labels(G, pos)

# Draw all edges
nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True)

# Edge labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight shortest path tree
tree_edges = []

for v in range(len(prev)):
    if prev[v] is not None:
        tree_edges.append((prev[v], v))

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=tree_edges,
    edge_color="red",
    width=3,
    arrows=True
)

plt.title("Dijkstra's Shortest Path Tree")
plt.axis("off")
plt.show()