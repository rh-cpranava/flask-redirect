# -*- coding: UTF-8 -*-
"""
flask_redirect: Redirects requests to appropriate URL
"""
import os
import requests
import socket
from datetime import datetime
from flask import Flask, redirect, render_template  
app = Flask(__name__)    
port=5000
@app.route('/')
def base_function():
    return {"ip_address": socket.gethostbyname(socket.gethostname()), "hostname": socket.gethostname(), "port": port, "date": datetime.now().strftime("%d%m%y") }

@app.route('/status/<redirect_url>')
def status(redirect_url):
    return redirect('https://'+redirect_url.replace('-','.'))
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=True)
