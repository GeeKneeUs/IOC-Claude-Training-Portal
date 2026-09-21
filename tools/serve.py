import http.server
import os
import socketserver

os.chdir(os.path.join(os.path.dirname(__file__), "..", "src"))
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
