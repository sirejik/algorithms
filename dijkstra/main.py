"""
Description: The algorithm for finding the shortest paths between nodes in a graph.

Average complexity: O(n^2).
"""
import math


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbor_distance = {}

    def set_neighbor_distance(self, neighbor, distance):
        self.neighbor_distance[neighbor] = distance


class Graph:
    nodes = {}

    @staticmethod
    def get_node(name) -> Node:
        return Graph.nodes.setdefault(name, Node(name))

    @staticmethod
    def add_edge(name1, name2, distance):
        node1 = Graph.get_node(name1)
        node2 = Graph.get_node(name2)
        node1.set_neighbor_distance(node2, distance)
        node2.set_neighbor_distance(node1, distance)


def dijkstra(start_node, end_node=None):
    ways = {}
    seen_nodes = []
    current_node = start_node
    ways[current_node] = ([current_node], 0)
    while True:
        if end_node == current_node:
            return ways[current_node]

        current_way, current_distance = ways[current_node]
        for node in current_node.neighbor_distance.keys():
            if node in seen_nodes:
                continue

            node_distance = current_node.neighbor_distance[node]
            new_distance = current_distance + node_distance

            if node in ways:
                way, distance = ways[node]
                if new_distance < distance:
                    ways[node] = current_way + [node], new_distance
            else:
                ways[node] = current_way + [node], new_distance

        seen_nodes.append(current_node)

        next_node, next_node_distance = None, math.inf
        for node, (_, distance) in ways.items():
            if node in seen_nodes:
                continue

            if next_node_distance > distance:
                next_node, next_node_distance = node, distance

        if len(Graph.nodes) <= len(seen_nodes) or next_node is None:
            if end_node is not None:
                raise Exception('The way from {} to {} does not exist.'.format(
                    str(start_node.name), str(end_node.name)
                ))

            return ways

        current_node = next_node


def init_graph():
    for name1, name2, distance in [
        (1, 2, 7),
        (1, 3, 9),
        (1, 6, 14),
        (2, 3, 10),
        (2, 4, 15),
        (3, 4, 11),
        (3, 6, 2),
        (4, 5, 6),
        (5, 6, 9)
    ]:
        Graph.add_edge(name1, name2, distance)


def print_results(ways):
    for way, distance in ways.values():
        print_result(way, distance)


def print_result(way, distance):
    print('-'.join([str(x.name) for x in way]) + ' = ' + str(distance))


init_graph()
result = dijkstra(Graph.get_node(1))
print_results(result)

result = dijkstra(Graph.get_node(1), Graph.get_node(5))
print_result(*result)
