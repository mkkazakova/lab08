import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 56665), handler) as httpd:
   httpd.serve_forever()
