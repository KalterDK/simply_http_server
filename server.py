#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HttpProcessor(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.wfile.write("OK")

	def do_POST(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		file = open('data.txt', 'a')
		file.write(post_data + '\n')
		file.close()
		self.wfile.write("OK" + '\n')


serv = HTTPServer(("192.168.19.14", 9090), HttpProcessor)
serv.serve_forever()
