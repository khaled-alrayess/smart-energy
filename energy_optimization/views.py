from django.shortcuts import render
from django.http import JsonResponse
import random

# Sample data for demand, supply, and transport losses
consumption_demand = [50, 60, 70]
supply_capacity = [100, 80]
transport_loss = [
    [2, 3, 4],
    [3, 2, 5]
]

# Fitness function to calculate energy loss
def fitness(individual):
    total_loss = 0
    total_supply = [0] * len(supply_capacity)
    for i, source in enumerate(individual):
        for j, allocation in enumerate(source):
            total_loss += allocation * transport_loss[i][j]
            total_supply[i] += allocation
    # Ensure supply doesn't exceed capacity
    if any(total_supply[i] > supply_capacity[i] for i in range(len(supply_capacity))):
        return float('-inf')
    return sum(consumption_demand) - total_loss

# Initialize the population with random solutions
def create_individual():
    return [[random.randint(0, min(supply_capacity[i], consumption_demand[j])) for j in range(len(consumption_demand))] for i in range(len(supply_capacity))]

# Genetic algorithm implementation
def genetic_algorithm(iterations=100, population_size=10):
    population = [create_individual() for _ in range(population_size)]
    for generation in range(iterations):
        population = sorted(population, key=lambda ind: fitness(ind), reverse=True)
        next_generation = population[:5]
        for _ in range(5):
            parent1, parent2 = random.sample(population[:5], 2)
            child = [random.choice(pair) for pair in zip(parent1, parent2)]
            next_generation.append(child)
        population = next_generation
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

def index(request):
    return render(request, 'index.html')

def optimize(request):
    solution, fitness_value = genetic_algorithm()
    return JsonResponse({
        'solution': solution,
        'fitness': fitness_value
    })
