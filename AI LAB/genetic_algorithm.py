import random

def random_solution(length):
    return [random.randint(0,1) for _ in range(length)]

def fitness(sol):
    return sum(sol)

def mutate(sol, rate=0.1):
    return [bit ^ 1 if random.random() < rate else bit for bit in sol]

def crossover(a, b):
    i = random.randrange(1, len(a))
    return a[:i] + b[i:]

def genetic(nbits=10, pop=20, generations=50):
    population = [random_solution(nbits) for _ in range(pop)]
    for _ in range(generations):
        population.sort(key=fitness, reverse=True)
        next_pop = population[:2]
        while len(next_pop) < pop:
            a, b = random.sample(population[:10], 2)
            child = mutate(crossover(a,b))
            next_pop.append(child)
        population = next_pop
    return max(population, key=fitness), fitness(max(population, key=fitness))

if __name__ == "__main__":
    best, score = genetic()
    print("Genetic best:", best, "score:", score)
