import random
from continuousGA.selection import Selection
from continuousGA.crossover import Crossover
from continuousGA.mutation import Mutation
from continuousGA.fitness import Fitness
from continuousGA.termination import Termination

class ContinuousGA():


    def __init__(
            self, 
            N_pop: int, 
            sel: Selection, 
            cross: Crossover, 
            mut: Mutation, 
            fit: Fitness, 
            termination: Termination, 
            genes: dict, 
            optimize_max: bool = True
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
        self.SelectionOperator = sel
        self.CrossoverOperator = cross
        self.MutationOperator = mut
        self.FitnessOperator = fit
        self.TerminationOperator = termination

        # save the limits of each gene
        self.genesLimits = genes

        # set optimization mode: max/min
        self.optimize_max = optimize_max

    def print_population(self):
        n = 1
        for indv in self.population:
            print(f"Indv: {n} - {indv}")
            n = n + 1

    def get_best_individual(self, actualFitness):
        return actualFitness

    def run(self):
        
        actualFitness = self.FitnessOperator.fit(self.population)
        while not self.TerminationOperator.isFinished(actualFitness):
            """
            self.SelectionOperator.performSelection(self.population, actualFitness, self.optimize_max)
            self.CrossoverOperator.performCrossover(self.population)
            self.MutationOperator.performMutation(self.population)
            """
            actualFitness = self.FitnessOperator.fit(self.population)
        
        return self.get_best_individual(actualFitness)
    

