from typing import List
from project.album import Album
# from album import Album
from project.song import Song
# from song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            album_to_del = next(filter(lambda el: el.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."
        if album_to_del.published:
            return "Album has been published. It cannot be removed."
        else:
            self.albums.remove(album_to_del)
            return f"Album {self.name} has been removed."

    def details(self) -> str:
        album_info = '\n'.join([f"== {a.details()}" for a in self.albums])
        return f"Band {self.name}\n" + album_info


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
