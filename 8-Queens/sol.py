import random
import sys

# Selection Function
def select(population, fitness, goal_fit):
	current_amount = 0
	fitness_total = []
	for i in range(len(population)):
		current_amount += fitness(population[i], goal_fit)
		fitness_total.append(current_amount)
	prob = random.uniform(0, fitness_total[-1])
	for i in range(len(population)):
		if fitness_total[i] > prob:
			return population[i]

# Mutation Function
def mutation(child):
	return switch(1, child)

# Reproduction Function
def reproduce(x):
	return switch(2, x)


def compute_goal_fit(n):
	goal_fit = 0
	for i in range(n):
		goal_fit += i
	return goal_fit

def switch(n, target):
	for i in range(n):
		j = random.randint(0, len(target) - 1)
		k = random.randint(0, len(target) - 1)
		target[j], target[k] = target[k], target[j]
	return target

# Genetic Algorithm
def solve(population, fitness):
	nmax = 100000
	n = nmax
	goal_fit = compute_goal_fit(len(random.choice(population)))
	while n > 0: 
		new_population = []
		for i in range(len(population)):
			x = select(population, fitness, goal_fit)
			child = reproduce(x)
			if random.uniform(0,1) < 1.0:
				child = mutation(child)
			if fitness(child, goal_fit) >= goal_fit:
				print child," found in ", nmax - n, " generations.\n"
				return child	
			new_population.append(child)
		population = new_population	
		n -= 1
	print "Solution not found in ", nmax, " generations, try again.\n"
	return None


# Fitness Function
def fitness(individual, goal_fit):
	fitness_value = goal_fit
	for i in range(len(individual)):
		j = 1
		while j < len(individual)-i:
			if (individual[i] == individual[i+j]+j) or (individual[i] == individual[i+j]-j):
				fitness_value -= 1
			j += 1
	return fitness_value

# Main Function
n = 8
population = []
base = range(n)
for i in range(100):
	population.append(switch(5, base))
solve(population, fitness)
