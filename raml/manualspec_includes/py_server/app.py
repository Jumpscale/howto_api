from flask import Flask, send_from_directory, send_file
from network_api import network_api
from self_api import self_api
from status_api import status_api


app = Flask(__name__)

app.register_blueprint(network_api)
app.register_blueprint(self_api)
app.register_blueprint(status_api)



@app.route('/apidocs/<path:path>')
def send_js(path):
    return send_from_directory('apidocs', path)


@app.route('/', methods=['GET'])
def home():
    return send_file('index.html')

if __name__ == "__main__":
    app.run(debug=True)
