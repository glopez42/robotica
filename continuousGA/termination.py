from abc import ABC, abstractmethod
from continuousGA.fitness import FitnessDistance

class Termination(ABC):

    @abstractmethod
    def isFinished(self, best_individual: list, actual_iter: int) -> bool:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

'''
Checks if best fitness is below a specific value
'''
class LowerThan(Termination):

    def __init__(self, value, max_iter) -> None:
        self.value = value
        self.max_iter = max_iter
        self.optimize_max = False

    def name(self) -> str:
        return "LowerThan" + str(self.value)

    def isFinished(self, best_individual: list, actual_iter: int) -> bool:
        return (best_individual[1] <= self.value) or (actual_iter == self.max_iter)

'''
Checks if best fitness is below a specific value.
If so, runs another simulation to check fitness again.
This is made to minimize 'lucky' simulations.
'''
class LowerThanSimulation(Termination):

    def __init__(self, value, max_iter) -> None:
        self.value = value
        self.max_iter = max_iter
        self.optimize_max = False
        self.fitnessFunction = FitnessDistance()
    
    def name(self) -> str:
        return "LowerThan" + str(self.value) + "Simulation"

    def isFinished(self, best_individual: list, actual_iter: int) -> bool:
        if (actual_iter == self.max_iter):
            return True            
        # if the condition is achieved, checks fitness again
        if (best_individual[1] <= self.value):
            distance = self.fitnessFunction.run_simulation(best_individual[0])
            return (distance <= self.value)
        return False
