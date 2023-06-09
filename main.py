import argparse
import sys

from source.Trainer import ACOTrainer


def main():
    """ feed arguments and start algorithm

    Args:
        args (): algorithm start args
    """
    args = parse_arguments(sys.argv[1:])
    
    print("Args: \n{")
    for arg, value in vars(args).items():
        print(f"  '{arg}': {value}")
    print("}")

    aco = ACOTrainer(args)
    aco.run()


def parse_arguments(argv):
    """Parse args
    """
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--localization', type=int,
                        help='Localization [1:Djibouti, 2:Luxembourg, 3:Oma]', default=1, choices=[1, 2, 3])
    
    parser.add_argument('-ants', '--ant_number', type=int,
                        help='Number of ants, default: same as points', default=None)

    parser.add_argument('-i', '--initial_pheromone', type=int,
                        help='Initial pheromone value', default=10)

    parser.add_argument('-e', '--evapaporation_rate', type=float,
                        help='evaporation percentage by iteration', default=0.15)

    parser.add_argument('-a', '--alpha', type=float,
                        help='Increases pheromone weight on fitness calculation', default=2)

    parser.add_argument('-b', '--betha', type=float,
                        help='Increases distance weight on fitness calculation', default=5)

    parser.add_argument('-td', '--time_debug', type=bool,
                        help='Enables time debug', default=1)

    parser.add_argument('-m', '--max_it_without_optimization', type=int,
                        help='Number of iterations in which the algorithm will try to optimize result', default=20)

    return parser.parse_args(argv)


if __name__ == "__main__":
    main()
