from abc import ABC, abstractmethod
import random
import math

class Crossover(ABC):

    @abstractmethod
    def performCrossover(self, population_size, parents):
        pass


class BlendingCrossover(Crossover):

    def recombine(self, father, mother):
        # number of genes to mix
        n_genes = len(father)
        crossover_point = math.floor(random.random() * n_genes)
        print(crossover_point)
        beta = random.random()
        father_gene = father[crossover_point]
        mother_gene = mother[crossover_point]
        son1_gene = mother_gene - beta * (mother_gene - father_gene)
        son2_gene = father_gene + beta * (mother_gene - father_gene)
        son1 = father[0:crossover_point] + [son1_gene] + mother[crossover_point+1:n_genes]
        son2 = mother[0:crossover_point] + [son2_gene] + father[crossover_point+1:n_genes] 
        return son1, son2


    def performCrossover(self, population_size, parents):
        new_population = parents
        n_parents = len(parents)

        # randomly mix the parents
        mixed_parents = random.sample(parents, k=n_parents)

        # offspring needed to achieve population size
        offspring_needed = population_size - n_parents

        offspring_count = 0
        # takes two indivuals and cross them
        for i in range(n_parents-1):
            father = mixed_parents[i]
            mother = mixed_parents[i+1]
            # recombination
            son1, son2 = self.recombine(father, mother)
            new_population.append(son1)
            new_population.append(son2)
            offspring_count += 2

        # if there is still more offspring needed
        while offspring_needed > offspring_count:
            # take random parents and generate one offspring
            print("Extra offspring")
            mixed_parents = random.sample(parents, k=2)
            father = mixed_parents[0]
            mother = mixed_parents[1]
            son1, son2 = self.recombine(father, mother)
            new_population.append(son1 if random.random() >= 0.5 else son2)
            offspring_count += 1

        return new_population