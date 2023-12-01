from abc import ABC, abstractmethod

class Termination(ABC):

    @abstractmethod
    def isFinished(self, fitness: list, actual_iter: int) -> bool:
        pass

class LowerThan(Termination):

    def __init__(self, value, max_iter) -> None:
        self.value = value
        self.max_iter = max_iter
        self.optimize_max = False

    def isFinished(self, fitness: list, actual_iter: int) -> bool:
        return (min(fitness) <= self.value) or (actual_iter == self.max_iter)