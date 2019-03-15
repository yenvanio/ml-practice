# 8 - Queens Problem

### Genetic Algorithm
1. Generating Population
    - Generate 8 Queens on the board, track the position in a column
        - Because it's a given that all queens are in different columns
2. Fitness Function
    - To evaluate the population you need a function
    - Estimates the success of the individual
    - Check number of horizontal collisions and diagonal collisions
        - Less collisions = higher fitness
        - Total fitness = 28 (max number of collisions)
            - Fitness Value = 28 - # of collisions
3. Selection
    - Parent chromosomes are selected with a probability related to their fitness
        - Weighted Random Probability
5. Mutation
    - Probability = 0.03
 
