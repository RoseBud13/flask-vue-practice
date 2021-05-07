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


@app.route('/flask')
def flask():
    return jsonify('flask test and say hello')

@app.route('/test')
def test():
    return 'test'


if __name__ == '__main__':
    app.run()

