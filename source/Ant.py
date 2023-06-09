import random

import numpy as np


class Ant:
    """The Ant class is responsible for deciding it's path between all the possible alternatives,
            it will trace it's own route based on the fitness matrix and distance matrix, it uses an
            stochastic tournament to decide each step, any route could be taken, but there are some
            that have most weight
    """
    def __init__(self):
        """Only initialize"""
        self.size = 0
        self.route = []
        self.route_distance = np.Inf

    def create(self, distance_matrix, fitness_matrix, size):
        """Create Ant

        Args:
            distance_matrix (list[list[float]]): matrix of distances
            fitness_matrix (list[list[float]]): matrix of fitness
            size (int): number of points to be routed

        Returns:
            Ant: returns self object
        """
        self.size = size
        self.fitness_matrix = np.copy(fitness_matrix)
        self.distance_matrix = np.copy(distance_matrix)
        self.vertice_array = list(range(size))

        self.route_distance = 0
        self.get_path()
        return self

    def get_path(self):
        """Trace route step by step starting from a random initial position
        """
        position = initial_position = random.randint(0, self.size-1)        
        self.route.append(initial_position)
        self.exclude_vertice(initial_position)
        for _ in range(1, self.size):
            position = self.decide_next_step(position)

    def decide_next_step(self, current_vertice):
        """ handles the ant's step: make the tournament, appent to the route and totalize route's 
        distance

        Args:
            current_vertice (int): current position

        Returns:
            int: target vertice position
        """

        target_vertice = self.tournament(current_vertice)
        target_vertice_index = self.vertice_array[target_vertice]
        self.route.append(target_vertice_index)
        self.route_distance += self.distance_matrix[current_vertice,
                                                    target_vertice]

        self.exclude_vertice(target_vertice)
        return target_vertice_index

    def tournament(self, current_vertice):
        """Create the tournament and choose the next target step

        Args:
            current_vertice (int): current position

        Returns:
            int: target's vertice index
        """
        fitnessArr = list(self.fitness_matrix[current_vertice])
        sumFitness = np.sum(fitnessArr)

        tourney_random_value = random.random()
        acumRelativeFitness = 0.0
        for i in range(len(self.vertice_array)):
            acumRelativeFitness += fitnessArr[i]/sumFitness
            if (tourney_random_value <= acumRelativeFitness):
                return i
        return 0

    def exclude_vertice(self, index):
        """exclude column (position already taken in the route)

        Args:
            index (int): column index to be removed from local matrixes
        """
        self.vertice_array = np.delete(self.vertice_array, index)
        self.distance_matrix = np.delete(self.distance_matrix, index, 1)
        self.fitness_matrix = np.delete(self.fitness_matrix, index, 1)
