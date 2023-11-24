from abc import ABC, abstractmethod

class Mutation(ABC):

    @abstractmethod
    def performMutation(self):
        pass