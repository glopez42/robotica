import random
from selection import Selection
from crossover import Crossover
from mutation import Mutation
from fitness import Fitness
from termination import Termination

class ContinuosGA():

    population = []
    SelectionOperator = None
    CrossoverOperator = None
    MutationOperator = None
    FitnessOperator = None
    TerminationOperator = None
    genesLimits = {}

    def __init__(self, N_pop: int, sel: Selection, cross: Crossover, mut: Mutation, fit: Fitness, termination: Termination, genes: dict) -> None:
        
        # create first population, each row of the matrix will represent an individual
        for _ in range(N_pop):
            individual = []
            # for each gene we get the max/min values and take a random value between them
            for geneName, geneValue in genes.items():
                min = geneValue[0]
                max = geneValue[1]
                individual.append(min + random.random()*max)

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

    def get_best_individual(self):
        return

    def run(self):
        
        actualFitness = self.FitnessOperator.fit(self.population)
        while not self.TerminationOperator.isFinished(actualFitness):
            self.SelectionOperator.performSelection(self.population)
            self.CrossoverOperator.performCrossover(self.population)
            self.MutationOperator.performMutation(self.population)
            actualFitness = self.FitnessOperator.fit(self.population)
        
        return self.get_best_individual()
    

