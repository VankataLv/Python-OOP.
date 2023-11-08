from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List] = [[]]
