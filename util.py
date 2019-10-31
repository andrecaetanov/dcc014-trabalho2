from math import sqrt
from copy import deepcopy


FILE_PATH = 'burma14.tsp'
NUM_NODES = 10
INDEX_INITIAL_NODE = 0


class Node:
    def __init__(self, index, x, y, h):
        self.index = index
        self.x = x
        self.y = y
        self.h = h


class State:
    def __init__(self, node, distance, path, nodes_in_path):
        self.node = node
        self.distance = distance
        self.path = path
        self.nodes_in_path = nodes_in_path


def read_file():
    infile = open(FILE_PATH)

    name = infile.readline().strip().split()[1]  # NAME
    print("NAME:", name)
    file_type = infile.readline().strip().split()[1]  # TYPE
    print("TYPE:", file_type)
    comment = infile.readline().strip().split()[1]  # COMMENT
    print("COMMENT:", comment)
    dimension = int(infile.readline().strip().split()[1])  # DIMENSION
    print("DIMENSION:", dimension)
    edge_weight_type = infile.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
    print("EDGE_WEIGHT_TYPE:", edge_weight_type)
    edge_weight_format = infile.readline().strip().split()[1]  # EDGE_WEIGHT_FORMAT
    print("EDGE_WEIGHT_FORMAT:", edge_weight_format)
    display_data_type = infile.readline().strip().split()[1]  # DISPLAY_DATA_TYPE
    print("DISPLAY_DATA_TYPE:", display_data_type)
    infile.readline()  # NODE_COORD_SECTION
    print("NODE_COORD_SECTION")

    nodelist = []
    for i in range(NUM_NODES):
        x, y = infile.readline().strip().split()[1:]
        node = Node(i, float(x), float(y), 0)
        nodelist.append(node)
        print("node: {} x: {} y: {}".format(i, x, y))
    print()

    return nodelist


def get_initial_state(nodes):
    initial_path = [nodes[INDEX_INITIAL_NODE]]
    initial_nodes_in_path = [False] * NUM_NODES
    initial_nodes_in_path[INDEX_INITIAL_NODE] = True
    initial_state = State(nodes[INDEX_INITIAL_NODE], 0, initial_path, initial_nodes_in_path)
    return initial_state


def get_distance(current_node, next_node):
    return sqrt((next_node.x - current_node.x) ** 2 + (next_node.y - current_node.y) ** 2)


def open_nodes(nodes, current_state, open_states):
    for node in nodes:
        if not current_state.nodes_in_path[node.index]:
            distance = get_distance(current_state.node, node)
            print("{} - {}: {}".format(current_state.node.index, node.index, distance))
            current_distance = distance + current_state.distance

            path = deepcopy(current_state.path)
            path.append(node)

            nodes_in_path = deepcopy(current_state.nodes_in_path)
            nodes_in_path[node.index] = True

            if len(path) == NUM_NODES:
                current_distance = current_distance + get_distance(node, nodes[INDEX_INITIAL_NODE])

            new_state = State(node, current_distance, path, nodes_in_path)
            open_states.append(new_state)

    return open_states


def calc_heuristics(nodes):
    for node in nodes:
        distances = []
        for adjacent_node in nodes:
            if node.index != adjacent_node.index:
                distance = get_distance(node, adjacent_node)
                distances.append(distance)

        distances.sort()
        node.h = (distances[0] + distances[1] + distances[2])/3
