from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(6000)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Python server!")

HOST = "0.0.0.0"
PORT = 8000

server = HTTPServer((HOST, PORT), MyHandler)

print(f"Server running at http://{HOST}:{PORT}")
server.serve_forever()
