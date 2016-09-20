from website.pixiv import PixivParser
from website.image import image

class ImagesController:
    def __init__(self, username, password):
        self.pixiv = PixivParser(username, password)
        self.images = []

    def search_works(self, keywords):
        self.images.append(self.pixiv.search_works(keywords))