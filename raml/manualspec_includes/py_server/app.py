from flask import Flask, send_from_directory, send_file
import wtforms_json
from network import network_api
from self import self_api
from status import status_api


app = Flask(__name__)

app.config["WTF_CSRF_ENABLED"] = False
wtforms_json.init()

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
