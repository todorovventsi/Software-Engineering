class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = [song for song in args] # List of Song objects
        self.published = False

    def add_song(self, song): # Works with Song objects
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name): # Works with songs names (string)
        if self.published:
            return "Cannot remove songs. Album is published."
        if not any([True for song in self.songs if song.name == song_name]):
            return "Song is not in the album."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        songs_to_print = [f"== {song.get_info()}\n" for song in self.songs]
        return f"Album {self.name}\n{''.join(songs_to_print)}"
