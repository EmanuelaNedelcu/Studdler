
#!/usr/bin/env python

from flask import Flask
from flask.ext.restful import Api

app = Flask(__name__)
api = Api(app)

from resources import TodoListResource, TodoResource, StudentListResource, StudentResource


api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')

api.add_resource(StudentListResource, '/students', endpoint='students')
api.add_resource(StudentListResource, '/students/<student:id>', endpoint='student')

if __name__ == '__main__':
    app.run(debug=True)

