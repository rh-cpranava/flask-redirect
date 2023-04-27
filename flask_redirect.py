# -*- coding: UTF-8 -*-
"""
flask_redirect: Redirects requests to appropriate URL
"""
import os
import requests
from flask import Flask, redirect, render_template  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')
def base_function():
    if "POD_NAME" in os.environ:
        pod_name = os.environ.get('POD_NAME')
    else:
        return render_template('error.html')
    
    if "NODE_NAME" in os.environ:
        node_name = os.environ.get('NODE_NAME')
    else:
        return render_template('error.html')
    
    if "POD_NAMESPACE" in os.environ:
        namespace_name = os.environ.get('POD_NAMESPACE')
    else:
        return render_template('error.html')
    
    if "POD_IP" in os.environ:
        pod_ip = os.environ.get('POD_IP')
    else:
        return render_template('error.html')
    
    if "POD_SERVICE_ACCOUNT" in os.environ:
        pod_service_account = os.environ.get('POD_SERVICE_ACCOUNT')
    else:
        return render_template('error.html')
    
    return {
        "pod_name": pod_name,
        "node_name": node_name,
        "namespace_name": namespace_name,
        "pod_ip": pod_ip,
        "pod_service_account": pod_service_account,
    }


@app.route('/status')
def status():
    base_url = os.environ.get('BASE_URL')
    return_value = requests.get(base_url)
    return return_value.json()
    
if __name__ == '__main__':
    app.run(host="::", port=5000, debug=True, use_reloader=True)
