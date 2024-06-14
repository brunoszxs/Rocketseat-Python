from flask import Flask, request
from models.task import Task

app = Flask(__name__)

task = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    return "Teste"

if __name__ == "__main__":
    app.run(debug=True)