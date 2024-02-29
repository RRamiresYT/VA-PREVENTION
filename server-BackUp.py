import http.server
import socketserver
import os
from PrimaryUser import PrimaryUser

PORT = 8000
DIRECTORY = "Html/Avaliacao"

web_dir = os.path.join(os.path.dirname(__file__), DIRECTORY)

os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at port {PORT}")
    httpd.serve_forever()
