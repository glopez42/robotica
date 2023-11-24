from abc import ABC, abstractmethod

class Termination(ABC):

    @abstractmethod
    def isFinished(self, fitness: list) -> bool:
        pass