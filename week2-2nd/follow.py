class DirectedGraph():
    points = {}
    links = {}

    def add_edge(self, node_from, node_to):
        if node_from not in self.points and node_to not in self.points:
            self.points[node_from] = [node_to]
            self.points[node_to] = []
            self.links[node_to] = [node_from]
            self.links[node_from] = []
        elif node_from not in self.points and node_to in self.points:
            self.points[node_from] = [node_to]
            self.links[node_to].append(node_from)
        elif node_from in self.points and node_to not in self.points:
            self.points[node_from].append(node_to)
            self.points[node_to] = []
            self.links[node_to] = [node_from]
            if node_to in self.points[node_from]:
                return "Link already exists"
            else:
                self.points[node_from].append(node_to)
                self.links[node_to].append(node_from)
        elif node_from in self.points and node_to in self.points:
            if node_to in self.points[node_from]:
                return "Link already exists"
            elif node_to not in self.points[node_from]:
                self.points[node_from].append(node_to)
                self.links[node_to] = [node_from]
        return self.points

    def get_neighbors_for(self, node):
        if node not in self.points:
            print ("Node does not exist.")
            return "Node does not exist."
        print ("Neighbors of %s: %s" % (node, self.points[node]))
        return self.points[node]

    def path_between(self, node_a, node_b):
        if (node_a not in self.points or node_b not in self.points
                or node_b not in self.links or node_a not in self.links):
            return False
        if node_b in self.points[node_a]:
            return True
        else:
            for link in self.links[node_b]:
                return self.path_between(node_a, link)
        return False

    def __str__(self):
        print (str(self.links))
        return str(self.points)

# new = DirectedGraph()
# new.add_edge('2', '1')
# new.add_edge('2', '4')
# new.add_edge('2', '5')
# new.add_edge('1', '3')
# new.add_edge('5', '6')
# new.add_edge('6', '8')
# new.add_edge('6', '7')
# new.add_edge('7', '10')
# new.add_edge('7', '9')
# new.add_edge('9', '11')


# print (new.path_between('2', '11'))

# print (new.__str__())
