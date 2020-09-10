from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        # determine root path of documents
        cwd = os.getcwd()
        cwd += "\\"

        if self.path == "/":

            self.path = "index.html" 

        filename=cwd+self.path

        try:

            with open(filename,"rb") as f:
                content = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content)
        except:

            print("File not found: {}".format(filename))
            self.send_response(404)
            
httpd = HTTPServer(("localhost", 80), Serv)
httpd.serve_forever()