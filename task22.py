from bottle import route, run
from datetime import datetime
@route('/hello')
def hello():
    return datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

run(host='localhost', port=8080, debug=True)
