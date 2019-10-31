from util import NUM_NODES, read_file, get_initial_state, calc_heuristics, Node, State
from copy import deepcopy
import sys


def pathfinding():
    open_states = []

    initial_state = get_initial_state(nodes)
    open_states.append(initial_state)

    while len(open_states) > 0:
        current_state = open_states[0]

        if len(current_state.path) == NUM_NODES:
            return current_state

        next_node = Node(0, 0, 0, sys.maxsize)
        next_state = (next_node, 0, [], [])

        for node in nodes:
            if not current_state.nodes_in_path[node.index]:
                if next_node.h > node.h:
                    path = deepcopy(current_state.path)
                    path.append(node)

                    nodes_in_path = deepcopy(current_state.nodes_in_path)
                    nodes_in_path[node.index] = True
                    next_node = node
                    next_state = State(node, 0, path, nodes_in_path)

        open_states.append(next_state)
        open_states.pop(0)

    return None


nodes = read_file()
calc_heuristics(nodes)
final_state = pathfinding()

print("FINAL_PATH:")
for n in final_state.path:
    print(n.index)
