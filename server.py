from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import requests
import argparse
from cachetools import TTLCache

endpoint = "https://dummyjson.com"
Port = 8080

cache = TTLCache(maxsize=100, ttl=300)

class Handle(BaseHTTPRequestHandler):
    def get_response(self,dest):
        response = requests.get(dest)
        return response

    def in_cache(self,dest):
        if dest in cache:
            return True
        return False

    def do_GET(self):
        print(self.path)

        # we need to append http://dummyjson.com to this
        newdest = endpoint + self.path
        response = ""

        if self.in_cache(newdest):
            print("Cache : HIT")
            response = cache[newdest]
        else:
            print("Cache : MISS")
            response = self.get_response(newdest)
            cache[newdest] = response

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response.content)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "get the port and dest add")

    parser.add_argument("--port",help = "port no")
    parser.add_argument("--origin",help = "dest address")
    parser.add_argument("--clear-cache",action='store_true',help = "clear the cache")

    args = parser.parse_args()

    if args.clear_cache:
        print("clearing cache")
        cache.clear()

    if args.port and args.origin:

        Port = int(args.port)
        endpoint = args.origin
    
        server = HTTPServer(('localhost', Port), Handle)
        print(f'Server running on http://localhost:{Port}')
        server.serve_forever()
    




