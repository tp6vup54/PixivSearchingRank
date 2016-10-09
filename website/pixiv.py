from pixivpy3 import *
from website.image import Image

class PixivParser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def login(self):
        self.api = PixivAPI()
        self.api.login(self.username, self.password)

    def search(self, keywords, **kwargs):
        again = True
        ret = None
        while again:
            again = False
            result = self.api.search_works(keywords, **kwargs)
            ret = result
            if result['status'] != 'success':
                if result['error']['system']['message'] == 'The access token provided is invalid.':
                    self.login()
                    again = True
                else:
                    ret = 'failed'
        return ret


    def search_works(self, keywords):
        result = self.search(keywords, page=1, per_page=1, mode='tag')
        if result == 'failed':
            return result
        total = result['pagination']['total']
        if total == 0:
            return []
        page, perpage = self.get_page_perpage(total)
        result = self.search(keywords, page=page, per_page=perpage, mode='tag')
        if result == 'failed':
            return result
        return [self.generate_image(i) for i in result['response']]

    def get_page_perpage(self, perpage):
        if perpage <= 1000:
            return 1, perpage
        page = perpage // 999 + (1 if perpage % 999 > 0 else 0)
        return page, 999


    def generate_image(self, json):
        return Image(json)