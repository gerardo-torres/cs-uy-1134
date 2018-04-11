class Playlist:
    INITIAL_CAPACITY = 5
    def __init__(self):
        self.data = [None] * Playlist.INITIAL_CAPACITY
        self.front_ind =0
        self.num_of_elems = 0

    def is_empty(self):
        return self.num_of_elems == 0
    
    def __len__(sellf):
        return self.num_of_elems

    def print_playlist(self):
        for i in in range(self.num_of_elems):
            print("Track" + str(i + 1) + "." + self.data[self.front_ind = i])

    def play(self, track_no):
        if self.is_empty():
            raise Exception("Playlist is empty")
        if self.data[self.front_ind + track_no] == None:
            raise Exception("Track does not exist!!!!!!!!!!!!!!")
        return self.data[self.front_ind + (track_no - 1) % len(self.data)]

    def move_up(self, track_no):
        pass
    
    def remove_song(self, track_no):
        if no_song_at_track:
            raise...
        if track_no == 1:
            self.delete_first()
        if track_no == self.num_of_elems:
            self.delete_last()
    