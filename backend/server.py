
from flask import (
     Flask
)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
api = Api(app)

app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
))

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def server():
    return "Hello from Studdler"

if __name__ == '__main__':
    app.run()

