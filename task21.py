from bottle import route, run
from datetime import datetime
start_time = datetime.now()
@route('/hello')
def hello():
    return("---%s---" % (start_time))

run(host='localhost', port=8080, debug=True)
