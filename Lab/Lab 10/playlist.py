class Playlist:
    INITIAL_CAPACITY = 5
    def __init__(self):
        self.data = [None] * Playlist.INITIAL_CAPACITY
        self.front_ind = 0
        self.num_of_elems = 0

    def print_playlist(self):
        for i in range(self.num_of_elems):
            print("track " + str(i + 1) + ":" self.data[self.front_ind + i])

        