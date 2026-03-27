def monkey_banana(n):
    # find minimum moves to swap monkey and bananas positions with rules
    # simple model with one banana and one monkey
    return 2*n - 1

if __name__ == "__main__":
    n = 3
    print("Monkey banana moves for", n, "steps:", monkey_banana(n))
