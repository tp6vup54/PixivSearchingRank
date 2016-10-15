from website.pixiv import PixivParser
import website.worker as worker

class ImagesController:
    def __init__(self, username, password):
        self.pixiv = PixivParser(username, password)
        self.favorite_count_str = ['100000users', '50000users', '10000users', '5000users', '1000users', '500users', '100users']
        worker.session = self.pixiv
        self.progress_callback = None
        self.images = []
        self.default_sort_type = 3
        self.sort_func = {
            1: self.sort_descend_time,
            2: self.sort_ascend_time,
            3: self.sort_descend_bookmark,
        }

    def search_works(self, keywords, favorite_count):
        self.images = []
        rq = [worker.search_works(keywords + ' ' + self.favorite_count_str[i], self.progress_callback) for i in range(favorite_count + 1)]
        ret = worker.map(rq)
        for r in ret:
            self.images.extend(r)

    def sort_ascend_time(self):
        return sorted(self.images, key=lambda image: image.last_modified_time)

    def sort_descend_time(self):
        return sorted(self.images, key=lambda image: image.last_modified_time, reverse=True)

    def sort_descend_bookmark(self):
        return sorted(self.images, key=lambda image: image.favorite_count, reverse=True)
