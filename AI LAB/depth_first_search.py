def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for nbr in graph.get(start, []):
        if nbr not in visited:
            dfs(graph, nbr, visited, order)
    return order

if __name__ == "__main__":
    g = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}
    print("DFS order:", dfs(g, 0))
