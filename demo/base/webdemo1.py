from  wsgiref.simple_server import  make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
httpd=make_server('',8000,application)
print(" Service Http on port 8000")

