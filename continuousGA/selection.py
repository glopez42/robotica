from abc import ABC, abstractmethod

class Selection(ABC):

    @abstractmethod
    def performSelection(
            self, 
            population: list, 
            fitness: list, 
            optimize_max: bool
        ):
        pass

class ElitistSelection(Selection):

    def performSelection(
            self, 
            population: list, 
            fitness: list, 
            optimize_max: bool
        ):

        


        return 