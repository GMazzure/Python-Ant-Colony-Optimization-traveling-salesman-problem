# Ant Colony Optimization (ACO)
  **Author: Gustavo Mazzure**

  *Travelling Salesman Problem*


  ACO is a metaheuristic algorithm based on the natural skill of ant colonies to form routes to food source, when something worth taking is found, they return to the colony dropping pheromone through its path.
  In this implementation, is given a set of coordinates in which form a country (Djibouti,Luxembourg and Oma), the problem is to trace a route passing through every coordinate without repeating, and returning back to the start with the smallest distance possible, so this is an optimization problem.
  In every iteration, n ants will be set in random coordinates, trace their routes and leave pheromon proportionally to their route fitness. Ants will tend to take paths in which are closer and with more pheromone

## Arguments:
| Argument    | Name  | Description |
| ----------- | -------------------- | ----------- |
|-h           | Help                 | Show this help message and exit |
|-l           | Localization {1,2,3} | Localization between [1:Djibouti, 2:Luxembourg, 3:Oma] |
|-ants        | Ant count            | Number of ants, default: same as quantity of coordinates |
|-i           | Initial pheromone    | Initial pheromone value |
|-e           | Evaporation rate     | Evaporation percentage by iteration |
|-a           | Alpha                | Increases pheromone weight on fitness calculation |
|-b           | Betha                | Increases distance weight on fitness calculation |
|-m           | Max iterations without optimization | Stop criterium, number of iterations in which the algorithm will try to optimize result |

## Requirements
  - Python 3.6+
  - numpy
  - pylab

## Usage

  > Run the algorithm within the app folder.

  Example running on Djibouti dataset with 100 ants
  ```
    python3 main.py -l 1 -a 100
  ```
  
 
 Iteration 1:
     ![Iteration1](https://github.com/GMazzure/Python-Ant-Colony-Optimization-traveling-salesman-problem/assets/135989764/2757af55-060d-40ae-81d5-45bc59000208)
 Iteration 11:
     ![Iteration11](https://github.com/GMazzure/Python-Ant-Colony-Optimization-traveling-salesman-problem/assets/135989764/0a699052-2e95-43c8-bdf9-e3f1308ff4cd)

  
