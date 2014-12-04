class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0

    def _add_points(self, points):
        self.points = points*points
        return self.points

    def _get_points(self):
        return self.points
