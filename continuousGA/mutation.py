from abc import ABC, abstractmethod
import random
import math

class Mutation(ABC):

    @abstractmethod
    def performMutation(self, population, rate, gene_limits):
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class RemakeGeneMutation(Mutation):

    def name(self) -> str:
        return "Remake Gene Mutation"

    def performMutation(self, population, rate, gene_limits):
        n_genes = len(population[0])
        n_individuals = len(population)
        n_mutations = int(n_genes * n_individuals * rate)

        mutations = [ [int(random.random()*n_individuals), int(random.random()*n_genes)] for _ in range(n_mutations)]
        # print("Mutations to perform:")
        # print(mutations)
        
        for m in mutations:
            individual = m[0]
            gene = m[1]
            limits = list(gene_limits.values())[gene]
            min = limits[0]
            max = limits[1]
            population[individual][gene] = random.uniform(min, max)

        return population