import math

import numpy
from numpy import *
from source.Ant import Ant

# from source.dataSourceHandler import *


class ACO:
    """Ant Colony Optimization is a ant-colony based metaheuristic algorithm used to solve routing 
            problem such as the travelling salesman, which is solved in this implementation
        this class is responsible for managing the pheromone for each individual route step (point A 
            to point B),calculate distances and fitness heuristic
    """

    def __init__(self, positions_arr, initial_pheromone, alpha, betha, evapaporation_rate) -> None:
        ACO.alpha = alpha
        ACO.betha = betha
        ACO.evapaporation_rate = evapaporation_rate

        self.positions_arr = positions_arr
        self.size = len(positions_arr)

        self.distances_matrix = ACO.calculateDistances(positions_arr)
        self.initializePheromoneMatrix(initial_pheromone)
        self.fitness_matrix = None

    def initializePheromoneMatrix(self, initial_pheromone):
        """Initialize Pheromone Matrix

        Args:
            initial_pheromone (int): value to be assigned to each individual route step at the start 
                of the algorithm
        """
        self.feromon_matrix = full(
            self.distances_matrix.shape, initial_pheromone, 'float64')

    def updateFeromon(self, ants: list[Ant], bestAntSoFar: Ant):
        """For each ant, add pheromone to its route based on the quality of the result

        Args:
            ants (list[Ant]): List of ants of the iteration ran
            bestAntSoFar (Ant): Best ant on the problem solving so far (for comparation)
        """
        for ant in ants:
            self.addFeromonToRoute(
                ant.route, ant.route_distance, bestAntSoFar.route_distance)

    def evaporateFeromon(self):
        """Evaporate Pheromone to all routes by a linear value
        """
        self.feromon_matrix = self.feromon_matrix*(1-ACO.evapaporation_rate)

    def addFeromonToRoute(self, routeArr:list[int], distance:float, bestDistanceSoFar:float):
        """Add Pheromone to a route taken by an ant

        Args:
            routeArr (list[int]): List of positions the ant has taken to route
            distance (float): total distance of the route
            bestDistanceSoFar (float): best distance found so far in the algorithm (for comparation)
        """
        pheromoneTrailValue = calcAntPheromoneTrailValue(distance, bestDistanceSoFar)
        for next_step in range(1, len(routeArr)):
            #  add pheromone to each route step
            current_step = next_step - 1
            self.feromon_matrix[int(routeArr[current_step])][int(routeArr[next_step])] += pheromoneTrailValue

        # Pheromone to the last vertice to the first (the route is continuous)
        self.feromon_matrix[len(routeArr)-1][int(routeArr[0])] += pheromoneTrailValue

    def calculateFitnessMatrix(self):
        """Update fitness matrix to an updated one, the fitness calculation is in
                calcFitness function
        """
        self.fitness_matrix = ACO.calcFitness(
            self.feromon_matrix, self.distances_matrix)

    @staticmethod
    def calcFitness(pheromon_matrix, distance_matrix):
        """Uses numpy matrix calculation to result the fitness matrix, which is the calculated 
                weight value for each route step in the current state of the algorithm

        Args:
            pheromon_matrix (matrix[int])
            distance_matrix (matrix[int])

        Returns:
            matrix[int]: fitness matrix
        """
        return 0.1 + ((pheromon_matrix**ACO.alpha) * (VerticeQuality(distance_matrix)**ACO.betha))

    @staticmethod
    def calculateDistances(dataArr):
        """Calculate all distances from any point to any other point

        Args: dataArr (array): Array of points

        Returns: Matrix of distances
        """
        arrLength = dataArr.__len__()
        dM = numpy.zeros((arrLength, arrLength))
        for i in range(arrLength):
            for j in range(arrLength):
                dM[i][j] = ACO.calculateDistance(dataArr[i], dataArr[j])
        return dM

    @staticmethod
    def calculateDistance(p1:list[float], p2:list[float]):
        """Calculates distance between point 1 to point 2

        Args:
            p1 (list[float]): cartesian X and Y for point 1
            p2 (list[float]): cartesian X and Y for point 2

        Returns:
            float: straight distance between the two points
        """
        return math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))


def calcAntPheromoneTrailValue(distance:float, bestDistanceSoFar:float):
    """Calculates pheromone value to be added to each step of Ant's route based on the route 
            distance, the value is inversely proportional to the distance of the route (the less the
            better)

    Args:
        distance (float): distance of the full route
        bestDistanceSoFar (float): best distance of the full route found so far

    Returns:
        float: Ant's Pheromone left to it's trail
    """
    return 10/(1+(distance-bestDistanceSoFar)**(1/3))


def VerticeQuality(distance:float):
    """Evaluates vertice quality for the fitness function (less distance the better)
    
        Args:
            distance (float): distance between two points
    """
    return (1 + (10/(1+sqrt(distance))))
