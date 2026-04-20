#!/usr/bin/env python3
"""
Simple HTTP server to host DSO138mini Web Plotter
Required because Web Serial API only works on HTTPS or localhost
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

def start_server():
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Server running on http://localhost:{PORT}")
        print(f"📂 Serving files from: {os.getcwd()}")
        print(f"🔗 Open http://localhost:{PORT}/index.html in your browser")
        print(f"⏹️  Press Ctrl+C to stop\n")
        
        try:
            # Open browser automatically
            webbrowser.open(f"http://localhost:{PORT}/index.html")
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⛔ Server stopped.")

if __name__ == "__main__":
    start_server()
