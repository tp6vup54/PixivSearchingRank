from pixivpy3 import *

class pixiv_parser:
    def __init__(self, username, password):
        self.api = PixivAPI()
        self.api.login(username, password)

    def search_works(self, keywords):
        json_result = self.api.search_works(keywords, page=1, per_page=1, mode='text')
        print(json_result)