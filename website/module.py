from website.pixiv import PixivParser
from website.image import Image

class ImagesController:
    def __init__(self, username, password):
        self.pixiv = PixivParser(username, password)
        self.favorite_count_str = ['100000users', '50000users', '10000users', '5000users', '1000users', '500users', '100users']
        self.images = []

    def search_works(self, keywords, favorite_count):
        self.images = []
        keywords = 'ピカチュウ'
        for i in range(2, favorite_count + 1):
            imgs = self.pixiv.search_works(keywords + ' ' + self.favorite_count_str[i])
            if imgs != 'failed':
                self.images.extend(self.pixiv.search_works(keywords + ' ' + self.favorite_count_str[2]))
        return self.images