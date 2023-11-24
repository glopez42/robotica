from abc import ABC, abstractmethod

class Fitness(ABC):

    @abstractmethod
    def fit(self, population: list):
        pass