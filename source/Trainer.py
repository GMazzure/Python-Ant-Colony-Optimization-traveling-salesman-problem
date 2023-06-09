
import numpy as np
import source.dataSourceHandler as DataSourceHandler
import source.helpers as Helpers
from source.ACO import ACO
from source.Ant import Ant
from source.Log import Log
from source.visu import Visu


class ACOTrainer:
    """ACO Trainer is the class to manages the iterations process and initializes all the objects
            needed for the algorithm to run properly
    """

    def __init__(self, args):
        self.args = args
        self.t_start_execution = Helpers.get_current_time()

        self.log = Log(args.localization)
        self.visu = Visu()
        self.aco = ACO(
            positions_arr=DataSourceHandler.get_data(self.args.localization),
            initial_pheromone=args.initial_pheromone,
            alpha=args.alpha,
            betha=args.betha,
            evapaporation_rate=args.evapaporation_rate)
        self.best_ant_so_far: Ant = Ant()

        self.ant_count = args.ant_number if args.ant_number != None else self.aco.size

        self.min_distance_serie = []
        self.max_distance_serie = []
        self.avg_distance_serie = []
        self.iteration_serie = []
        self.best_so_far_serie = []

    def run(self):
        """ Run iterations until the number of iterations without optimization surpasses the config.
                value setted by the user (arg max_it_without_optimization)
        """
        self.bestRoute = []
        self.best_iteration = 0

        self.iteration = 1
        self.iterations_without_optimization = 0
        while (self.iterations_without_optimization < self.args.max_it_without_optimization):
            self.iterate()

    def iterate(self):
        """Executes a full iteration for the ACO algorithm
                - Calculates the fitness for the whole matrix
                - Creates self.aco.size number of ants (can be set on start with --ant_number param)
                - Evaluates the best ant in the iteration
                - Checks the iteration's best ant is also the best ant so far
                - Evaporate pheromone from the matrix (value set on start with evapaporation_rate)
                - Update pheromone based on every ant's taken routes
        """
        t_iteration_start = Helpers.get_current_time()

        self.aco.calculateFitnessMatrix()

        ants = []
        best_ant = Ant()
        for i in range(0, self.aco.size):
            ants.append(Ant().create(self.aco.distances_matrix,
                        self.aco.fitness_matrix, self.aco.size))

            if ants[i].route_distance < best_ant.route_distance:
                best_ant = ants[i]

        self.iterations_without_optimization += 1
        if best_ant.route_distance < self.best_ant_so_far.route_distance:
            self.best_iteration = self.iteration
            self.best_ant_so_far = best_ant
            self.iterations_without_optimization = 0
            self.visu.plotRoute(best_ant.route, self.aco.positions_arr)

        print(';  Updating Pheromone matrix..', end='')

        self.aco.evaporateFeromon()
        self.aco.updateFeromon(ants, self.best_ant_so_far)

        self.handle_iteration_data(ants, t_iteration_start)
        self.iteration += 1

    def handle_iteration_data(self, ants: list[Ant], t_iteration_start: int):
        """Makes a sum up of the iteration data to show to the user

        Args:
            ants (list[Ant]): iteration's list of ants
            t_iteration_start (int): time of the start of the iteration
        """
        distances = np.array(list(map(lambda ant: ant.route_distance, ants)))
        bestIteration = np.min(distances)
        WorstIteration = np.max(distances)
        AvgIteration = np.mean(distances)

        self.min_distance_serie.append(bestIteration)
        self.max_distance_serie.append(WorstIteration)
        self.avg_distance_serie.append(AvgIteration)
        self.iteration_serie.append(self.iteration)
        self.best_so_far_serie.append(self.best_ant_so_far.route_distance)

        maxF = np.max(self.aco.feromon_matrix)
        minF = np.min(self.aco.feromon_matrix)
        avgF = np.mean(self.aco.feromon_matrix)

        print('#\tExecution time:' +
              str(Helpers.elapsed_time_in_milliseconds(self.t_start_execution)) + 'ms')
        print('#\tIteration time:' + str(Helpers.elapsed_time_in_milliseconds(
            t_iteration_start)) + 'ms')
        print('#\tPheromone: [Highest:'+str(maxF) +
              ' Mean:'+str(avgF) + ';  lesser:'+str(minF)+']')
        print('#\tDistance: [global best:'+str("%0.0f" % self.best_ant_so_far.route_distance)+'; local best:'+str("%0.0f" % bestIteration) +
              'local mean: MediaL:' + str("%0.0f" % AvgIteration)+'; local worst:' + str("%0.0f" % WorstIteration)+']')

        self.visu.plotIndicators(
            xArr=self.iteration_serie,
            y1Arr=self.best_so_far_serie,
            y2Arr=self.min_distance_serie,
            y3Arr=self.max_distance_serie,
            y4Arr=self.avg_distance_serie,
            iteration=self.iteration,
            elapsedTime=Helpers.elapsed_time_in_seconds(self.t_start_execution)
        )

        self.visu.drawChart()
        self.visu.exportChart(
            self.log.logPath+'/Iteration'+str(self.iteration))
