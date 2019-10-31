from util import NUM_NODES, read_file, get_initial_state, open_nodes, calc_heuristics


def pathfinding():
    open_states = []
    closed_states = []

    initial_state = get_initial_state(nodes)
    open_states.append(initial_state)

    while len(open_states) > 0:
        current_state = open_states[0]

        if len(current_state.path) == NUM_NODES:
            return current_state

        open_states = open_nodes(nodes, current_state, open_states)

        closed_states.append(current_state)
        open_states.pop(0)
        open_states.sort(key=lambda x: x.node.h)

    return None


nodes = read_file()
calc_heuristics(nodes)
final_state = pathfinding()

print()
print("FINAL_PATH:")
for n in final_state.path:
    print(n.index)
