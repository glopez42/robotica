import random
import json
import time
from datetime import datetime
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

        # execution time stamp
        self.timestamp = datetime.now().strftime("%Y:%m:%dT%H:%M:%S")

        # report with information about the execution
        self.report = {}

    def print_population(self):
        n = 1
        for indv in self.population:
            print(f"Indv: {n} - {indv}")
            n = n + 1

    def get_best_individual(self, actualFitness):
        best_fitness = max(actualFitness) if self.optimize_max else min(actualFitness)
        position = actualFitness.index(best_fitness)
        return [self.population[position], best_fitness]


    def dump_report(self):
        with open(f'reports/report_{self.timestamp}.json', 'w+') as outfile:
            json.dump(self.report, outfile)
    
    def create_report(self, actualFitness):
        self.report = {
            "operators": {
                "crossover": self.CrossoverOperator.name(),
                "fitness": self.FitnessOperator.name(),
                "mutation": self.MutationOperator.name(),
                "selection": self.SelectionOperator.name(),
                "termination": self.TerminationOperator.name(),
            },
            "genes_limits": self.genesLimits,
            "selection_rate": self.selection_rate,
            "mutation_rate": self.mutation_rate,
            "initial_population": self.population,
            "initial_fitness": actualFitness,
            "start_time": self.timestamp,
            "algorithm_execution": {}
        }

    def update_report(self,actualFitness,iter):
        # actual iteration report including population and its fitness
        self.report["algorithm_execution"].update({
            iter: {
                "population": self.population,
                "fitness": actualFitness,
            },
        })
    
    def finish_report(self, best):
        self.report.update({
            "results" : {
                "best_individual": best[0],
                "fitness": best[1],
            },
            "end_time": datetime.now().strftime("%Y:%m:%dT%H:%M:%S"),
        })
        self.dump_report()


    def run(self):
        actualFitness = self.FitnessOperator.fit(self.population)
        self.create_report(actualFitness)
        iter = 1
        best = self.get_best_individual(actualFitness)
        while not self.TerminationOperator.isFinished(best, iter):
            print(f"***** GA - iter: {iter} *****")
            start = time.time()
            print(f"population len: {len(self.population)}")
            # Selection
            new_population = self.SelectionOperator.performSelection(self.population, actualFitness, self.optimize_max, self.selection_rate)
            # Crossover
            new_population = self.CrossoverOperator.performCrossover(len(self.population), new_population)
            # Mutation
            new_population = self.MutationOperator.performMutation(new_population, self.mutation_rate, self.genesLimits)
            self.population = new_population
            # Fitness
            actualFitness = self.FitnessOperator.fit(self.population)

            # update values
            best = self.get_best_individual(actualFitness)
            self.update_report(actualFitness, iter)
            print(f"***** End iter: {iter} in {time.time() - start} seconds *****")
            iter = iter + 1



        self.finish_report(best)
        return 
    

