import random
from continuousGA.selection import Selection
from continuousGA.crossover import Crossover
from continuousGA.mutation import Mutation
from continuousGA.fitness import Fitness
from continuousGA.termination import Termination

class ContinuousGA():

    population = []

    def __init__(
            self, 
            N_pop: int, 
            selection: Selection, 
            crossover: Crossover, 
            mutation: Mutation, 
            fitness: Fitness, 
            termination: Termination, 
            genes: dict, 
            optimize_max: bool,
            selection_rate: float,
            mutation_rate: float
        ) -> None:
        
        # create first population, each row of the population matrix will represent an individual
        for _ in range(N_pop):
            individual = []
            # for each gene we get the max/min values and take a random value between them
            for geneName, geneValue in genes.items():
                min = geneValue[0]
                max = geneValue[1]
                individual.append(random.uniform(min, max))

            # append the new individual to the population    
            self.population.append(individual)

        # GA operators
        self.SelectionOperator = selection
        self.CrossoverOperator = crossover
        self.MutationOperator = mutation
        self.FitnessOperator = fitness
        self.TerminationOperator = termination

        # save the limits of each gene
        self.genesLimits = genes

        # set optimization mode: max/min
        self.optimize_max = optimize_max

        self.selection_rate = selection_rate
        self.mutation_rate = mutation_rate

    def print_population(self):
        n = 1
        for indv in self.population:
            print(f"Indv: {n} - {indv}")
            n = n + 1

    def get_best_individual(self, actualFitness):
        return actualFitness

    def run(self):
        
        actualFitness = self.FitnessOperator.fit(self.population)
        print(actualFitness)
        iter = 1
        while not self.TerminationOperator.isFinished(actualFitness, iter):
            print(f"***** GA - iter: {iter} *****")
            # Selection
            new_population = self.SelectionOperator.performSelection(self.population, actualFitness, self.optimize_max, self.selection_rate)

            # Crossover
            new_population = self.CrossoverOperator.performCrossover(len(self.population), new_population)    

            # Mutation
            new_population = self.MutationOperator.performMutation(new_population, self.mutation_rate, self.genesLimits)
            self.population = new_population

            # Fitness
            actualFitness = self.FitnessOperator.fit(self.population)

            iter = iter + 1
        
        return self.get_best_individual(actualFitness)
    

