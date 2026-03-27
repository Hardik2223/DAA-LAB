def fractional_knapsack(weights, values, capacity):
    items = sorted([(v/w, w, v) for w, v in zip(weights, values)], key=lambda x: x[0], reverse=True)
    total_value = 0.0
    for ratio, w, v in items:
        if capacity <= 0:
            break
        take = min(w, capacity)
        total_value += take * ratio
        capacity -= take
    return total_value

if __name__ == "__main__":
    w = [10, 20, 30]
    v = [60, 100, 120]
    print("Fractional knapsack max value:", fractional_knapsack(w, v, 50))
