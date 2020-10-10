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


def dijkstra(start_node):
    ways = {}
    seen_nodes = []
    current_node = start_node
    ways[current_node] = ([current_node], 0)
    while True:
        current_way, current_distance = ways[current_node]
        next_node, next_node_distance = None, math.inf
        for node in current_node.neighbor_distance.keys():
            if node in seen_nodes:
                continue

            node_distance = current_node.neighbor_distance[node]
            new_distance = current_distance + node_distance

            if next_node_distance > node_distance:
                next_node, next_node_distance = node, node_distance

            if node in ways:
                way, distance = ways[node]
                if new_distance < distance:
                    ways[node] = current_way + [node], new_distance
            else:
                ways[node] = current_way + [node], new_distance

        seen_nodes.append(current_node)
        if len(Graph.nodes) <= len(seen_nodes) or next_node is None:
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


def print_result(ways):
    for way, distance in ways.values():
        print('-'.join([str(x.name) for x in way]) + ' = ' + str(distance))


init_graph()
result = dijkstra(Graph.get_node(1))
print_result(result)
