from flask import Flask, send_from_directory, send_file
from group_api import group_api
from user_api import user_api


app = Flask(__name__)

app.register_blueprint(group_api)
app.register_blueprint(user_api)



@app.route('/apidocs/<path:path>')
def send_js(path):
    return send_from_directory('apidocs', path)


@app.route('/', methods=['GET'])
def home():
    return send_file('index.html')

if __name__ == "__main__":
    app.run(debug=True)
