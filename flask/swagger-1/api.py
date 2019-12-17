# from https://flask-restplus.readthedocs.io/en/stable/example.html
from flask import Flask
from flask_restplus import Resource, Api, fields
# from werkzeug.contrib.fixers import ProxyFix
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='API test', description='Simple API Doc')

ns = api.namespace('test', description='TODO and hello world API')

todo = api.model('Model TODO', {
    'id': fields.Integer(readonly=True, description='task uuid'),
    'task': fields.String(required=True, description='task detail')
})

class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []
    
    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, 'Todo {} does not exist'.format(id))
    
    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo
    
    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo
    
    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)

DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})

@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'msg': 'hello, world!'}

@ns.route('/todo')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201

@ns.route('/todo/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)
