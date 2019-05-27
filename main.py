import http.server


def run():
    server_address = ('', 8001)
    httpd = http.server.HTTPServer(server_address, http.server.BaseHTTPRequestHandler)
    print(httpd.server_name, httpd.server_address, httpd.server_port)
    httpd.serve_forever()


run()
