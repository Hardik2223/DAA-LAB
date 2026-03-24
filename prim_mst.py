import heapq

def prim_mst(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start)]
    mst_weight = 0
    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += w
        for v, cost in enumerate(graph[u]):
            if cost > 0 and not visited[v]:
                heapq.heappush(min_heap, (cost, v))
    return mst_weight

if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    print("Prim MST weight:", prim_mst(graph))
