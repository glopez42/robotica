# Robotics proyect

This repository contains the implementation of a Genetic Algorithm with the objective of evolving the movement of a snake-like robot (ACM-R5). The individuals should learn how to move in a straight line.

## Dependencies

The project has been programmed under Python 3.10 and uses the `CoppeliaSim` to perform the simulations with the ACM-R5 snake-like robot. It can be downloaded in the following [link](https://www.coppeliarobotics.com/downloads).

## Execution

The script `startGA.py` contains an example of how to execute the algorithm:

```python
algorithm = ContinuousGA(
    N_pop = 50, # population size
    selection = ElitistSelection(), # selection operator
    crossover = BlendingCrossover(), # crossover operator
    mutation = RemakeGeneMutation(), # mutation operator
    fitness = FitnessDistance(), # fitness function to optimize
    termination = LowerThanSimulation(value=1, max_iter=60), # termination criteria
    genes = genes, # genes and their ranges
    optimize_max = False, # optimization mode: max (True) / min (False)
    selection_rate = 0.5, # selection rate to apply to the population
    mutation_rate = 0.075 # mutation rate to apply to the population
)

algorithm.run()
```

The `selection`, `crossover`, `mutation`, `fitness`, `termination` parameters should be existing classes inside the `continuousGA` package.

After modifying its parameters, it can be launched directly with:
```
python startGA.py
```

Before launching the algorithm, `CoppeliaSim` should be running and loaded with the scene provided in `/scenes`.

## Results

During the algorithm execution, a JSON will be generated and stored in the folder `/reports` cointaining information about the evolution of the population, best individual, execution time, etc. In order to analyse these reports, a Jupyter Notebook is provided in the folder `/analysis`, showing different metrics and diagrams to visualize the results provided by the algorithm.
