from abc import ABC, abstractmethod

class Selection(ABC):

    @abstractmethod
    def performSelection(self):
        pass