from flask import Flask, render_template, session, redirect, request
from website.image import Image
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
            items = imgs.search_works(request.form['Search-text'], int(request.form['Favorite']))
            return render_template('index.html', items=items)
    else:
        return render_template('index.html')
