import random

def initialize_population(size, min_val, max_val):
    return [[random.uniform(min_val, max_val) for _ in range(5)] for _ in range(size)]

def fitness_function(solution):
    # Example fitness function (customize for your needs)
    return sum(solution)

def select_parents(population, fitnesses):
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [ind for ind, _ in sorted_pop[:2]]

def crossover(parent1, parent2):
    point = len(parent1) // 2
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(solution, mutation_rate=0.1):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] += random.uniform(-1, 1)  # Adjust mutation logic as needed
    return solution

def genetic_algorithm():
    population_size = 10
    min_val, max_val = 0, 100
    population = initialize_population(population_size, min_val, max_val)
    generations = 50

    for _ in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]
        parents = select_parents(population, fitnesses)
        population = []

        for _ in range(population_size // 2):
            child1, child2 = crossover(parents[0], parents[1])
            population.append(mutate(child1))
            population.append(mutate(child2))

    return max(population, key=fitness_function)
