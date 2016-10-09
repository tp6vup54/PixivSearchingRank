from flask import Flask, render_template, session, redirect, request
from website.image import Image
from website.module import ImagesController

app = Flask(__name__)
app.config.from_object('websiteconfig')
imgs = ImagesController(app.config.get('PIXIV_USERNAME'), app.config.get('PIXIV_PASSWORD'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/sort', methods=['GET'])
def sort():
    sort_mode = request.args.get('Sort', 1, type=int)
    return jsonify(result=a + b)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['Search-text']:
            imgs.search_works(request.form['Search-text'], int(request.form['Favorite']))
            items = imgs.sort_func[imgs.default_sort_type]()
            return render_template('index.html', items=items)
    else:
        return render_template('index.html')
