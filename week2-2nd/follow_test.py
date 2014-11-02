import unittest
from follow import DirectedGraph


class Test_Graph(unittest.TestCase):
    def setUp(self):
        self.testgraph = DirectedGraph()

    def tearDown(self):
        self.testgraph.points.clear()
        self.testgraph.links.clear()

    def test_add_edge_when_graphs_dont_exist(self):
        output = {"2": ["1"], "1": []}
        result = self.testgraph.add_edge("2", "1")
        self.assertEqual(output, result)

    def test_add_edge_when_graphs_exist(self):
        output = {"2": ["1"], "1": ["2"]}
        self.testgraph.add_edge("1", "2")
        result = self.testgraph.add_edge("2", "1")
        self.assertEqual(output, result)

    def test_get_neighbors_when_graph_doesnt_exist(self):
        output = "Node does not exist."
        result = self.testgraph.get_neighbors_for("1")
        self.assertEqual(output, result)

    def test_get_neighbors_when_graph_doesnt_have_ones(self):
        output = []
        self.testgraph.add_edge("1", "2")
        result = self.testgraph.get_neighbors_for("2")
        self.assertEqual(output, result)

    def test_get_neighbors_when_graph_has_1_or_more_neighbors(self):
        output = ["2", "3"]
        self.testgraph.add_edge("1", "2")
        self.testgraph.add_edge("1", "3")
        result = self.testgraph.get_neighbors_for("1")
        self.assertEqual(output, result)

    def test_path_between_when_graphs_dont_exist(self):
        self.assertFalse(self.testgraph.path_between("2", "1"))

    def test_path_between_2_existing_graphs_when_path_exists(self):
        self.testgraph.add_edge("1", "2")
        result = self.testgraph.path_between("1", "2")
        self.assertTrue(result)

    def test_path_between_2_existing_graphs_when_path_doesnt_exist(self):
        self.testgraph.add_edge("1", "2")
        result = self.testgraph.path_between("2", "1")
        self.assertFalse(result)

    def test_path_between_2_or_more_existing_graphs_when_path_exists(self):
        self.testgraph.add_edge("1", "2")
        self.testgraph.add_edge("2", "3")
        self.testgraph.add_edge("3", "6")
        self.testgraph.add_edge("6", "4")
        result = self.testgraph.path_between("1", "4")
        self.assertTrue(result)

    def test_path_between_2_or_more_existing_graphs_when_path_doesnt_exist(self):
        self.testgraph.add_edge("1", "2")
        self.testgraph.add_edge("2", "3")
        self.testgraph.add_edge("3", "6")
        self.testgraph.add_edge("6", "4")
        result = self.testgraph.path_between("4", "1")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
