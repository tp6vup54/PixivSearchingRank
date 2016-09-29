from pixivpy3 import *
from website.image import Image

class PixivParser:
    def __init__(self, username, password):
        self.api = PixivAPI()
        self.api.login(username, password)

    def search_works(self, keywords):
        result = self.api.search_works(keywords, page=1, per_page=2, mode='tag')
        if result['status'] != 'success':
            return 'failed'
        total = result['pagination']['total']
        result = self.api.search_works(keywords, page=1, per_page=total, mode='tag')
        if result['status'] != 'success':
            return 'failed'
        return [self.generate_image(i) for i in result['response']]

    def generate_image(self, json):
        return Image(json)