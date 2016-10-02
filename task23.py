from bottle import route, run
import getpass
@route('/hello')
def hello():
    return getpass.getuser(); datetime.now()

run(host='localhost', port=8080, debug=True)
