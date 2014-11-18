class Cinema():
    cinema_slots = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

    def __init__(self, movies):
        self.movies = movies

    def show_free_slots(self, movie):
        free_slots_count = 0
        for row in self.cinema_slots:
            for slot in row:
                if slot == '.':
                    free_slots_count += 1
        return free_slots_count
