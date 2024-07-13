import networkx as nx
import matplotlib.pyplot as plot
import math
from itertools import permutations

# This function takes
# 1. a list of 2-tuples which represent the coordinates of the given points
# 2. and a cycle to be visualized.
def plot_cycle(coordinates, cycle):
    # Compute the x and y coordinates in the order according to the cycle
    x_coordinates = [coordinates[i][0] for i in cycle]
    y_coordinates = [coordinates[i][1] for i in cycle]

    # Add the first vertex of the cycle (to close the cycle)
    x_coordinates.append(coordinates[cycle[0]][0])
    y_coordinates.append(coordinates[cycle[0]][1])

    plot.plot(x_coordinates, y_coordinates, 'xb-', )
    plot.show()


# This function computes the weight of the given cycle.
def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    return sum(g[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1)) + g[cycle[0]][cycle[-1]]['weight']


def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

coordinates = [
    (174, 25),
    (129, 99),
    (268, 212),
    (211, 209),
    (156, 82)
    ]
# Create a corresponding graph.
g = get_graph(coordinates)


def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
          if g[current_node][v]['weight'] < min_edge and v not in path:
            next_node = v
            min_edge = g[current_node][v]['weight']
            # Write your code here: decide if v is a better candidate than next_node.
            # If it is, then update the values of next_node and min_edge

        assert next_node is not None
        print(next_node)
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight


print(nearest_neighbors(g))


# This function iterates through all permutations and returns an optimal cycle.
# You can implement any other algorithm here and visualize it.
#
# Note that in the previous questions you were asked to compute the length of an optimal cycle only,
# while this function returns an optimal cycle itself (so that we could plot it later).
def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    opt = float('inf')

    # Iterate through all permutations of n vertices
    for p in permutations(range(n)):
        if cycle_length(g, p) < opt:
            opt = cycle_length(g, p)
            opt_perm = p

    return opt_perm


# Example 1
# Consider the following 3 points.
coordinates = [
    (166, 282),
    (43, 79),
    (285, 44)
    ]
# Create a corresponding graph.
g = get_graph(coordinates)
# Compute an optimal Hamiltonian path using some algorithm (e.g., the all_permutations algorithm).
cycle = all_permutations(g)
# Plot the resulting cycle
plot_cycle(coordinates, cycle)


# Example 2
# Consider the following 5 points.
coordinates = [
    (284, 87),
    (183, 254),
    (113, 185),
    (159, 38),
    (271, 257)
    ]
# Create a corresponding graph.
g = get_graph(coordinates)
# Compute an optimal Hamiltonian path using some algorithm (e.g., the all_permutations algorithm).
cycle = all_permutations(g)
# Plot the resulting cycle
plot_cycle(coordinates, cycle)


# Example 3
# Consider the following 7 points.
coordinates = [
    (231, 72),
    (68, 9),
    (11, 90),
    (237, 116),
    (168, 112),
    (141, 69),
    (17, 18)
    ]
# Create a corresponding graph.
g = get_graph(coordinates)
# Compute an optimal Hamiltonian path using some algorithm (e.g., the all_permutations algorithm).
cycle = all_permutations(g)
# Plot the resulting cycle
plot_cycle(coordinates, cycle)
