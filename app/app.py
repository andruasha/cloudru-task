import os
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    return jsonify({'hostname': os.uname().nodename})

@app.route('/author', methods=['GET'])
def get_author():
    author = os.getenv('AUTHOR', 'Unknown')
    return jsonify({'author': author})

@app.route('/id', methods=['GET'])
def get_uuid():
    uuid = os.getenv('UUID', 'Unknown')
    return jsonify({'uuid': uuid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
