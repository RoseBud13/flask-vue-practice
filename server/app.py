from flask import Flask
from flask import jsonify
from flask_cors import CORS


# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def test():
    return jsonify('test')


if __name__ == '__main__':
    app.run()

