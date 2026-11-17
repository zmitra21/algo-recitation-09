# Zack Mitra

from collections import defaultdict
from heapq import heappush, heappop 
from math import sqrt

def prim(graph):
    """
    ### TODO:
    Update this method to work when the graph has multiple connected components.
    Rather than returning a single tree, return a list of trees,
    one per component, containing the MST for each component.

    Each tree is a set of (weight, node1, node2) tuples.    
    """

    def prim_helper(visited, frontier, tree):
        if len(frontier) == 0:
            return tree
        else:
            weight, node, parent = heappop(frontier)

            if node in visited:
                return prim_helper(visited, frontier, tree)
            else:
                print('visiting', node)

                tree.add((weight, node, parent))
                visited.add(node)

                for neighbor, w in graph[node]:
                    heappush(frontier, (w, neighbor, node))

                return prim_helper(visited, frontier, tree)

    visited = set()
    trees = []

    # Run Prim's algorithm on every unvisited component
    for source in graph:
        if source not in visited:
            frontier = []
            heappush(frontier, (0, source, source))

            tree = set()
            prim_helper(visited, frontier, tree)

            trees.append(tree)

    return trees
        
    # pick first node as source arbitrarily
    source = list(graph.keys())[0]
    frontier = []
    heappush(frontier, (0, source, source))
    visited = set()  # store the visited nodes (don't need distance anymore)
    tree = set()
    prim_helper(visited, frontier, tree)
    return tree

def mst_from_points(points):
    """
    Return the minimum spanning tree for a list of points, using euclidean distance 
    as the edge weight between each pair of points.
    See test_mst_from_points.

    Params:
      points... a list of tuples (city_name, x-coord, y-coord)

    Returns:
      a list of edges of the form (weight, node1, node2) indicating the minimum spanning
      tree connecting the cities in the input.
    """

    graph = defaultdict(set)

    for city, x, y in points:
        graph[city] = set()

    for i in range(len(points)):
        for j in range(i + 1, len(points)):

            city1 = points[i][0]
            city2 = points[j][0]

            distance = euclidean_distance(points[i], points[j])

            graph[city1].add((city2, distance))
            graph[city2].add((city1, distance))

    trees = prim(graph)

    return list(trees[0]) if trees else []


def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83
