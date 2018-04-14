### HTTP dialog

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import logging
import threading
import webbrowser

# based on https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
class RequestHandler(BaseHTTPRequestHandler):
    def shutdown(self):
        threading.Thread(target=httpd.shutdown).start()

    def set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def write(self, response):
        self.wfile.write(response.encode('utf-8'))

    def file(self, path):
        f = open(path, 'rb')
        self.wfile.write(f.read())

    def req_path(self):
        return parse.urlparse(self.path).path

    def args(self):
        return parse.parse_qs(parse.urlparse(self.path).query)

    def do_GET(self):
        #logging.debug("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self.set_response()
        self.fields = {}
        self.get()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self.set_response()
        self.fields = parse.parse_qs(post_data.decode('utf-8'))
        self.post()



def http_dialog(handler=RequestHandler, port=8080):
    webbrowser.open('http://localhost:' + str(port))

    global httpd
    server_address = ('', port)
    httpd = HTTPServer(server_address, handler)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')



