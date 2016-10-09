from datetime import datetime

class Image:
    def __init__(self, json):
        self.image_urls = ImageUrls(json['image_urls'])
        self.title = json['title']
        self.url = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(json['id'])
        self.user = User(json['user'])
        self.favorite_count = json['stats']['favorited_count']['public'] + json['stats']['favorited_count']['private']
        self.last_modified_time = datetime.strptime(json['reuploaded_time'], '%Y-%m-%d %H:%M:%S')


class ImageUrls:
    def __init__(self, json):
        self.px_128x128 = json['px_128x128']
        self.px_480mw = json['px_480mw']
        self.px_240mw = json['px_480mw'].replace('480x960', '240x480')
        self.large = json['large']


class User:
    def __init__(self, json):
        self.url = 'http://www.pixiv.net/member.php?id=' + str(json['id'])
        self.name = json['name']
        px_50 = json['profile_image_urls']['px_50x50']
        px_170 = px_50.replace('_50', '_170')
        self.image_url = px_170