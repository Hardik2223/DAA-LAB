from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return order

if __name__ == "__main__":
    g = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}
    print("BFS order:", bfs(g, 0))
