# https://www.afternerd.com/blog/python-http-server/
# https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/

import http.server
import socketserver

PORT = 9999
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()