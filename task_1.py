# Applying Uniform Cost Search Al
mygraph = {
    "S": [("1", 2), ("3", 5)],
    "3": [("1", 4), ("G", 6), ("4", 2)],
    "1": [("G", 1)],
    "G": [("4", 7)],
    "4": [("5", 3), ("2", 4)],
    "2": [("1", 4)],
    "5": [("G", 3), ("2", 6)],
}


def path_cost(path):
    total_cost = 0
    for(node, cost) in path:
        total_cost = total_cost+cost
    return total_cost, path[-1][0]


def myucs(mygraph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                neighbour_nodes = mygraph.get(node, [])
                for (node2, cost) in neighbour_nodes:
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)
        else:
            continue


answer_path = myucs(mygraph, "S", "G")
a, b = path_cost(answer_path)
print(answer_path)
print("Total Path cost = ", a)
print("Shortest path = ", [node for node, cost in answer_path])
