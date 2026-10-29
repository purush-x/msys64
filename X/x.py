#simple genetic algorithm

import numpy as np

# Parameters
population_size = 6
chromosome_length = 5
generations = 20
mutation_rate = 0.1

# Initial Population
population = np.random.randint(
    0, 2, (population_size, chromosome_length)
)

# Convert Binary Chromosome to Decimal
def decode(chromosome):
    value = 0
    for bit in chromosome:
        value = value * 2 + bit
    return value

# Fitness Function
def fitness(chromosome):
    x = decode(chromosome)
    return x ** 2

# Genetic Algorithm
for generation in range(generations):
    fitness_values = np.array([
        fitness(chromosome) for chromosome in population
    ])

    # Selection: Choose the Two Best Chromosomes
    best_indices = np.argsort(fitness_values)[-2:]
    parent1 = population[best_indices[0]].copy()
    parent2 = population[best_indices[1]].copy()

    # Crossover
    crossover_point = np.random.randint(1, chromosome_length)

    child1 = np.concatenate((
        parent1[:crossover_point],
        parent2[crossover_point:]
    ))

    child2 = np.concatenate((
        parent2[:crossover_point],
        parent1[crossover_point:]
    ))

    # Mutation
    for child in [child1, child2]:
        for i in range(chromosome_length):
            if np.random.rand() < mutation_rate:
                child[i] = 1 - child[i]

    # Create New Population
    population = np.array([
        parent1,
        parent2,
        child1,
        child2,
        population[np.random.randint(population_size)],
        population[np.random.randint(population_size)]
    ])

# Find Best Solution
fitness_values = np.array([
    fitness(chromosome) for chromosome in population
])

best_index = np.argmax(fitness_values)
best_chromosome = population[best_index]
best_x = decode(best_chromosome)
best_fitness = fitness(best_chromosome)

print("Best Chromosome:", best_chromosome)
print("Best Value of x:", best_x)
print("Maximum Fitness:", best_fitness)