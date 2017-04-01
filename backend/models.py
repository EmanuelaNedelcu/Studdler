
from models import Student, Subject
# from models import Todo
from db import session

from flask.ext.restful import reqparse
from flask.ext.restful import abort
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with

todo_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'uri': fields.Url('todo', absolute=True),
}


student_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'subjects': fields.String, # marshal subjects into a string
}



parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class StudentResource(Resource):
    @marshal_with(student_fields)
    def get(self, id):
        student = session.query(Student).filter(Student.id == id).first()
        if not student:
            abort(404, message="Student {} doesn't exist".format(id))
        return student
    
    def delete(self, id):
        student = session.query(Student).filter(Student.id == id).first()
        if not student:
            abort(404, message="Student {} doesn't exist".format(id))
        session.delete(student)
        session.commit()
        return {}, 204

    @marshal_with(Student_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        student = session.query(Student).filter(Student.id == id).first()
        student.subject = parsed_args['subject']
        session.add(student)
        session.commit()
        return student, 201

class StudentListResource(Resource):
    @marshal_with(student_fields)
    def get(self):
        students = session.query(Student).all()
        return students

class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        return todo

    def delete(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        session.delete(todo)
        session.commit()
        return {}, 204

    @marshal_with(todo_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        todo = session.query(Todo).filter(Todo.id == id).first()
        todo.task = parsed_args['task']
        session.add(todo)
        session.commit()
        return todo, 201




class TodoListResource(Resource):
    @marshal_with(todo_fields)
    def get(self):
        todos = session.query(Todo).all()
        return todos

    @marshal_with(todo_fields)
    def post(self):
        parsed_args = parser.parse_args()
        todo = Todo(task=parsed_args['task'])
        session.add(todo)
        session.commit()
        return todo, 201

from models import Student, Subject
# from models import Todo
from db import session

from flask.ext.restful import reqparse
from flask.ext.restful import abort
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with

todo_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'uri': fields.Url('todo', absolute=True),
}


student_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'subjects': fields.String, # marshal subjects into a string
}



parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class StudentResource(Resource):
    @marshal_with(student_fields)
    def get(self, id):
        student = session.query(Student).filter(Student.id == id).first()
        if not student:
            abort(404, message="Student {} doesn't exist".format(id))
        return student
    
    def delete(self, id):
        student = session.query(Student).filter(Student.id == id).first()
        if not student:
            abort(404, message="Student {} doesn't exist".format(id))
        session.delete(student)
        session.commit()
        return {}, 204

    @marshal_with(Student_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        student = session.query(Student).filter(Student.id == id).first()
        student.subject = parsed_args['subject']
        session.add(student)
        session.commit()
        return student, 201

class StudentListResource(Resource):
    @marshal_with(student_fields)
    def get(self):
        students = session.query(Student).all()
        return students

class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        return todo

    def delete(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        session.delete(todo)
        session.commit()
        return {}, 204

    @marshal_with(todo_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        todo = session.query(Todo).filter(Todo.id == id).first()
        todo.task = parsed_args['task']
        session.add(todo)
        session.commit()
        return todo, 201




class TodoListResource(Resource):
    @marshal_with(todo_fields)
    def get(self):
        todos = session.query(Todo).all()
        return todos

    @marshal_with(todo_fields)
    def post(self):
        parsed_args = parser.parse_args()
        todo = Todo(task=parsed_args['task'])
        session.add(todo)
        session.commit()
        return todo, 201

