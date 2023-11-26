from continuousGA.continuousGA import ContinuousGA
from continuousGA.crossover import *
from continuousGA.fitness import *
from continuousGA.mutation import *
from continuousGA.selection import *
from continuousGA.termination import *

# Selection
s = ElitistSelection()
# Crossover
c = None
# Fitness function
f = FitnessDistance()
# Mutations
m = None
# Termination criteria
t = LowerThan(value=35, max_iter=100)

# gene intervals
genes = {
    "a": [-10, 10],
    "b": [-10, 10],
    "c": [-4, 4],
    "w": [-20, 20]
}
# optimization mode: max (True) / min (False)
optimize_max = False

algorithm = ContinuousGA(5,s,c,m,f,t,genes,optimize_max)
algorithm.print_population()
result = algorithm.run()

print(result)