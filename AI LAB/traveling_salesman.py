from itertools import permutations

def tsp(dist):
    n = len(dist)
    best = None
    best_cost = float('inf')
    for order in permutations(range(1,n)):
        cost = dist[0][order[0]]
        for i in range(len(order)-1):
            cost += dist[order[i]][order[i+1]]
        cost += dist[order[-1]][0]
        if cost < best_cost:
            best_cost = cost
            best = (0,) + order + (0,)
    return best, best_cost

if __name__ == "__main__":
    d = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    route, cost = tsp(d)
    print("TSP route:", route, "cost:", cost)
