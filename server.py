from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import os

PORT = 8081

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

Handler.extensions_map['.yaml'] = 'application/json'
Handler.extensions_map['.json'] = 'application/json'

httpd = SocketServer.TCPServer(("", PORT), Handler)

source = '../../pim-api-docs/content/swagger'
os.chdir(source)
print("serving from", source, " at localhost:", PORT)
httpd.serve_forever()
