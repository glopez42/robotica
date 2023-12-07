from abc import ABC, abstractmethod
from robot import ACMR
from coppelia import Coppelia
import math


class Fitness(ABC):

    @abstractmethod
    def fit(self, population: list):
        pass

    @abstractmethod
    def name(self) -> str:
        pass

class FitnessDistance(Fitness):

    # simulation seconds per individual
    seconds = 20
    # coppelia simulation
    coppelia = Coppelia()
    # reference to the robot
    snake = ACMR(coppelia.sim, 'ACMR')
    # goal's position, the snake should get as closer as it can
    goalPosition = coppelia.sim.getObjectPosition(coppelia.sim.getObject(f'/goal'))

    def name(self) -> str:
        return "FitnessDistance"

    # euclidean distance between individual and goal
    def get_euclidean_distance(self, pos):
        return math.sqrt((self.goalPosition[0]-pos[0])**2 + (self.goalPosition[1]-pos[1])**2)

    def fit(self, population: list) -> list:
        fitness = []
        self.coppelia.start_simulation()

        for individual in population:
            # set individual parameters to the snake movement
            self.snake.set_movement_params(individual)
            start = self.coppelia.sim.getSimulationTime()
            t = 0
            # executes simulation during the amount of time in self.seconds
            while (t) < self.seconds:
                angles = self.snake.calculate_angles(t)
                self.snake.set_joint_angles(angles)
                t = self.coppelia.sim.getSimulationTime() - start

            # calculates the distance between the goal and the snake
            distance = self.get_euclidean_distance(self.snake.get_actual_position())
            fitness.append(distance)
            self.snake.reset_position()


        self.coppelia.stop_simulation()
        return fitness