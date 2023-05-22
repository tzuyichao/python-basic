import config
from celery_app import func1
from flask import Flask, request, jsonify, url_for, redirect


# Your API definition
app = Flask(__name__)
app.config.from_object('config.FlaskConfig')

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def longtask():
    task = func1.delay('testing')
    return redirect(url_for('taskstatus', task_id=task.id))
    
@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = func1.AsyncResult(task_id)
    if task.state == 'PENDING':
        time.sleep(config.SERVER_SLEEP)
        response = {
            'queue_state': task.state,
            'status': 'Process is ongoing...',
            'status_update': url_for('taskstatus', task_id=task.id)
        }
    else:
        response = {
            'queue_state': task.state,
            'result': task.wait()
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')