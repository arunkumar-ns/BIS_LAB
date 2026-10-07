import random
import math

points = {
    "Depot": (0, 0),
    "C1": (2, 3),
    "C2": (5, 2),
    "C3": (1, 5),
    "C4": (6, 4),
    "C5": (3, 1)
}

customers = ["C1", "C2", "C3", "C4", "C5"]

def distance(a, b):
    x1, y1 = points[a]
    x2, y2 = points[b]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def fitness(route):
    total = distance("Depot", route[0])
    for i in range(len(route)-1):
        total += distance(route[i], route[i+1])
    total += distance(route[-1], "Depot")
    return total

N = 30
W = 0.75
C1 = 2
C2 = 1.75
ITER = 200

particles = []

for i in range(N):
    route = customers.copy()
    random.shuffle(route)
    particles.append(route)

pbest = [route.copy() for route in particles]
gbest = min(pbest, key=fitness).copy()

for iteration in range(ITER):
    for i in range(N):
        route = particles[i].copy()

        if random.random() < C1 / (C1 + C2):
            a = random.randint(0, len(route)-1)
            b = route.index(pbest[i][a])
            route[a], route[b] = route[b], route[a]

        if random.random() < C2 / (C1 + C2):
            a = random.randint(0, len(route)-1)
            b = route.index(gbest[a])
            route[a], route[b] = route[b], route[a]

        particles[i] = route

        if fitness(route) < fitness(pbest[i]):
            pbest[i] = route.copy()

        if fitness(route) < fitness(gbest):
            gbest = route.copy()

print("N =", N, "W =", W, "C1 =", C1, "C2 =", C2, "ITER =", ITER)
print("Best Route:")
print("Depot ->", " -> ".join(gbest), "-> Depot")
print("Minimum Distance:", round(fitness(gbest), 2))
