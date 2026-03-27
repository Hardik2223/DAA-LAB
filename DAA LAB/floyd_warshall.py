def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    inf = float('inf')
    g = [
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf, inf, 0, 1],
        [inf, inf, inf, 0],
    ]
    m = floyd_warshall(g)
    print("All-pairs shortest path matrix:")
    for row in m:
        print(row)
