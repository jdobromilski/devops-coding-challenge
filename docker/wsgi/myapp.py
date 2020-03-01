# !/bin/python3
import datetime

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes(datetime.datetime.now().strftime('%H:%M:%S'),'utf-8')]
