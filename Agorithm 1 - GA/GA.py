import random

N = 10
Pc = 0.8
Pm = 0.1
MaxGen = 100

print("Arun Kumar N S")
print("1WN24CS050")
print()
def fitness(chromosome):
    x, y, z = chromosome
    score = 0

    if x > 50:
        score += 1
    if y < 20:
        score += 1
    if x + y > 100:
        score += 1
    if z == 25:
        score += 1

    return score

def create_chromosome():
    return [
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100)
    ]

def select(population):
    a = random.choice(population)
    b = random.choice(population)

    if fitness(a) > fitness(b):
        return a
    else:
        return b

def crossover(parent1, parent2):
    point = random.randint(1, 2)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

def mutate(chromosome):
    for i in range(3):
        if random.random() < Pm:
            chromosome[i] = random.randint(0, 100)

    return chromosome

population = [create_chromosome() for _ in range(N)]

for generation in range(MaxGen):

    new_population = []

    best = max(population, key=fitness)
    new_population.append(best[:])

    while len(new_population) < N:

        parent1 = select(population)
        parent2 = select(population)

        if random.random() < Pc:
            child1, child2 = crossover(parent1, parent2)
        else:
            child1 = parent1[:]
            child2 = parent2[:]

        child1 = mutate(child1)
        child2 = mutate(child2)

        new_population.append(child1)

        if len(new_population) < N:
            new_population.append(child2)

    population = new_population

    best = max(population, key=fitness)

    if fitness(best) == 4:
        break

best = max(population, key=fitness)

x, y, z = best

print("Generated Test Input:")
print("x =", x)
print("y =", y)
print("z =", z)

print("\nFitness =", fitness(best), "/ 4")

print("\nBranches Covered:")

if x > 50:
    print("1. x > 50 : Covered")

if y < 20:
    print("2. y < 20 : Covered")

if x + y > 100:
    print("3. x + y > 100 : Covered")

if z == 25:
    print("4. z = 25 : Covered")