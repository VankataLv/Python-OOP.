from project.song import Song
from typing import List
# from song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs: List[Song] = [*songs]
        self.published = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        try:
            song_to_del = next(filter(lambda x: x.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song_to_del)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_info = '\n'.join([f"== {s.get_info()}" for s in self.songs])
        return f"Album {self.name}\n" + songs_info
