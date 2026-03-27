import heapq

def dijkstra(graph, source=0):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in enumerate(graph[u]):
            if w > 0 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

if __name__ == "__main__":
    graph = [
        [0, 10, 0, 0, 5],
        [0, 0, 1, 0, 2],
        [0, 0, 0, 4, 0],
        [7, 0, 6, 0, 0],
        [0, 3, 9, 2, 0],
    ]
    print("Dijkstra distances:", dijkstra(graph, 0))
