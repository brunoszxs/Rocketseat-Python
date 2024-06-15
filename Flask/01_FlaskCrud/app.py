from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get('title'), description=data.get("description", ""))
    task_id_control =+ 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_task": len(task_list)
    }
    
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict()) 
    
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    found_task = None
    for t in tasks:
        if t.id == id:
            found_task = t
            break

    if found_task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

    data = request.get_json()
    # Assegura que a atualização só ocorre se os dados necessários estão presentes no JSON enviado
    if 'title' in data:
        found_task.title = data['title']
    if 'description' in data:
        found_task.description = data['description']
    if 'completed' in data:
        found_task.completed = data['completed']

    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    found_task = None
    for t in tasks:
        if t.id == id:
            found_task = t

    if found_task is None:
        return jsonify({"message": "Não foi possível deletar a atividade."}), 404
    
    tasks.remove(found_task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)

#