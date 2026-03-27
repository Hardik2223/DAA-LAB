def tower_of_hanoi(n, source='A', target='C', aux='B', moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target)); return moves
    tower_of_hanoi(n-1, source, aux, target, moves)
    moves.append((source, target))
    tower_of_hanoi(n-1, aux, target, source, moves)
    return moves

if __name__ == "__main__":
    for m in tower_of_hanoi(3):
        print(m)
