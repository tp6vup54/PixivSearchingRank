from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from website.image import Image
from website.module import ImagesController
from json import dumps

app = Flask(__name__)
app.config.from_object('websiteconfig')
socketio = SocketIO(app)
global_current = 0
global_total = 0
imgs = ImagesController(app.config.get('PIXIV_USERNAME'), app.config.get('PIXIV_PASSWORD'))

@socketio.on('sort')
def handle_sort_event(json):
    sort_mode = int(json['data'])
    items = imgs.sort_func[sort_mode]()
    emit('sort', dumps({'images': render_template('image-frame.html', items=items),
                        'mode': sort_mode}))

@socketio.on('search')
def handle_search_event(json):
    keyword = json['key']
    favorite = int(json['favor'])
    imgs.search_works(keyword, favorite)
    global global_current, global_total
    global_total = 0
    global_current = 0
    items = imgs.sort_func[imgs.default_sort_type]()
    emit('search', dumps({'images': render_template('image-frame.html', items=items)}))

def update_progress(current=0, total=0):
    with app.test_request_context('/'):
        global global_current, global_total
        global_current += current
        global_total += total
        socketio.emit('update-progress', dumps({'current': global_current, 'total': global_total}))

imgs.progress_callback = update_progress

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
