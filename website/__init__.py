from flask import Flask, render_template, session, redirect, request
from website.image import image
from website.module import ImagesController

app = Flask(__name__)
app.config.from_object('websiteconfig')
imgs = ImagesController(app.config.get('PIXIV_USERNAME'), app.config.get('PIXIV_PASSWORD'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['Search-text']:
            imgs.search_works(request.form['Search-text'])
            items = [image('http://i2.pixiv.net/c/240x480/img-master/img/2016/09/16/17/18/33/59009629_p0_master1200.jpg', '君の名は。'),
                      image('http://i4.pixiv.net/c/240x480/img-master/img/2016/09/16/00/39/48/59002107_p0_master1200.jpg', 'アッシュ＆ダスト'),
                      image('http://i4.pixiv.net/c/240x480/img-master/img/2016/09/16/00/39/48/59002107_p0_master1200.jpg', 'アッシュ＆ダスト'),
                      image('http://i4.pixiv.net/c/240x480/img-master/img/2016/09/16/00/39/48/59002107_p0_master1200.jpg', 'アッシュ＆ダスト'),
                      image('http://i4.pixiv.net/c/240x480/img-master/img/2016/09/16/00/39/48/59002107_p0_master1200.jpg', 'アッシュ＆ダスト')]
            return render_template('index.html', items=items)
    else:
        return render_template('index.html')
