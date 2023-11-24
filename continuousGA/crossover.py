from abc import ABC, abstractmethod

class Crossover(ABC):

    @abstractmethod
    def performCrossover(self):
        pass