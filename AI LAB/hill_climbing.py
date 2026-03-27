def hill_climbing(func, start, step=1, max_iter=100):
    current = start
    current_val = func(current)
    for _ in range(max_iter):
        neighbors = [current + step, current - step]
        next_state = current
        next_val = current_val
        for n in neighbors:
            v = func(n)
            if v > next_val:
                next_state, next_val = n, v
        if next_val <= current_val:
            break
        current, current_val = next_state, next_val
    return current, current_val

if __name__ == "__main__":
    f = lambda x: -(x-3)**2 + 10
    best, score = hill_climbing(f, 0, step=0.1)
    print("Hill climbing best:", best, "score:", score)
