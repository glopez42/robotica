from abc import ABC, abstractmethod
import math 

class Selection(ABC):

    @abstractmethod
    def performSelection(
            self, 
            population: list, 
            fitness: list, 
            optimize_max: bool,
            selection_rate: float
        ):
        pass
    
    @abstractmethod
    def name(self) -> str:
        pass

class ElitistSelection(Selection):

    def name(self) -> str:
        return "Elitist Selection"

    def performSelection(
            self, 
            population: list, 
            fitness: list, 
            optimize_max: bool,
            selection_rate: float
        ) -> list:

        n_pop = len(population)
        n_selects = math.floor(n_pop * selection_rate)
        best = sorted(fitness,key=float, reverse=optimize_max)[:n_selects]
        indexes = [ fitness.index(elem) for elem in best ]
        return [population[idx] for idx in indexes]