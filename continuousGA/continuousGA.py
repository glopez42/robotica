import random
import json
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

    def print_population(self):
        n = 1
        for indv in self.population:
            print(f"Indv: {n} - {indv}")
            n = n + 1

    def get_best_individual(self, actualFitness):
        best_fitness = max(actualFitness) if self.optimize_max else min(actualFitness)
        position = actualFitness.index(best_fitness)
        return self.population[position], best_fitness
    
    def dump_report(self, report):
        with open(f'reports/report_{self.timestamp}.json', 'w+') as outfile:
            json.dump(report, outfile)

    def run(self):
        
        actualFitness = self.FitnessOperator.fit(self.population)
        iter = 1

        # generates report
        report = {
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

            # actual iteration report including population and its fitness
            report["algorithm_execution"].update({
                iter: {
                    "population": self.population,
                    "fitness": actualFitness,
                },
            })
            self.dump_report(report)

            iter = iter + 1

        individual, fitness = self.get_best_individual(actualFitness)
        report.update({
            "results" : {
                "best_individual": individual,
                "fitness": fitness,
            },
            "end_time": datetime.now().strftime("%Y:%m:%dT%H:%M:%S"),
        })
        self.dump_report(report)
        
        return 
    

