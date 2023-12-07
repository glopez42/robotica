from continuousGA.continuousGA import ContinuousGA
from continuousGA.crossover import *
from continuousGA.fitness import *
from continuousGA.mutation import *
from continuousGA.selection import *
from continuousGA.termination import *


genes = {
    "a": [-10, 10],
    "b": [-10, 10],
    "c": [-4, 4],
    "w": [-20, 20]
}

algorithm = ContinuousGA(
    N_pop = 5, # population size
    selection = ElitistSelection(), # selection operator
    crossover = BlendingCrossover(), # crossover operator
    mutation = RemakeGeneMutation(), # mutation operator
    fitness = FitnessDistance(), # fitness function to optimize
    termination = LowerThan(value=10, max_iter=2), # termination criteria
    genes = genes, # genes and their ranges
    optimize_max = False, # optimization mode: max (True) / min (False)
    selection_rate = 0.5, # selection rate to apply to the population
    mutation_rate = 0.05 # mutation rate to apply to the population
)

print("******* Initial Population *******")
algorithm.print_population()
algorithm.run()
