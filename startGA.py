from continuousGA.continuousGA import ContinuousGA
from continuousGA.crossover import *
from continuousGA.fitness import *
from continuousGA.mutation import *
from continuousGA.selection import *
from continuousGA.termination import *


genes = {
    "a": [-10, 10],
    "b": [-10, 10],
    "c": [-2, 2],
    "w": [-6, 6]
}

algorithm = ContinuousGA(
    N_pop = 50, # population size
    selection = ElitistSelection(), # selection operator
    crossover = BlendingCrossover(), # crossover operator
    mutation = RemakeGeneMutation(), # mutation operator
    fitness = FitnessDistance(), # fitness function to optimize
    termination = LowerThanSimulation(value=0.5, max_iter=50), # termination criteria
    genes = genes, # genes and their ranges
    optimize_max = False, # optimization mode: max (True) / min (False)
    selection_rate = 0.5, # selection rate to apply to the population
    mutation_rate = 0.05 # mutation rate to apply to the population
)

print("******* Initial Population *******")
algorithm.print_population()
algorithm.run()
