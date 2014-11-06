class DirectedGraph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node_from, node_to):
        if node_from not in self.edges:
            self.edges[node_from] = [node_to]
        elif node_from in self.edges:
            if node_to in self.edges[node_from]:
                return "Edge already exists."
            else:
                self.edges[node_from].append(node_to)
        if node_to not in self.edges:
            self.edges[node_to] = []
        return self.edges

    def get_neighbours_for(self, node):
        if node not in self.edges:
            return "Node does not exist."
        return self.edges[node]

    def path_between(self, node_from, node_to):
        if node_from not in self.edges or node_to not in self.edges:
            return False
        neighbours = self.get_neighbours_for(node_from)
        if node_to in neighbours:
            return True

        for neighbour in neighbours:
            if self.path_between(neighbour, node_to):
                return True
        return False
