from typing import List
from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List] = self.__create_matrix()

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count/4))

    def __create_matrix(self) -> List:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    def add_photo(self, label: str):
        for page in range(0, self.pages):
            if len(self.photos[page]) < 4:
                position_label = len(self.photos[page])
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {position_label + 1}"
        return "No more free slots"

    def display(self):
        result = ""
        for page in range(0, self.pages):
            result += f'{11 * "-"}\n'
            result += len(self.photos[page]) * "[]"
            result += "\n"
        result += f'{11 * "-"}'
        return result.rstrip()

    # def __str__(self):
    #     return f"{self.pages}, {self.photos}"


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
