from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from task_dto import task_dto, patch_task_dto
import task_service as ts

task_bp = Blueprint("tasks", __name__)



### 2. **Routes à Implémenter**
#### a. **Liste de toutes les tâches** ()

@task_bp.get('/')
def find_many():
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 1000)
    tasks = ts.find_many_tasks(int(offset), int(limit))
    return tasks, 200

#### b. **Trouver une tâche par ID** ()
@task_bp.get('/<string:id_task>')
def find_one(id_task):
    task = ts.find_task_by_id(id_task)
    if task is None:
        return {"error" : f"Task {id_task} Not Found "}, 404
    return jsonify(task), 200

#### c. **Créer une nouvelle tâche** ()
@task_bp.post('')
@expects_json(task_dto)
def create():
    body = request.json   
    if body is None :
        return {"error": "Missing Data"},400
    task = ts.create_task(body)
    return jsonify(task), 201
   
#### d. **Modifier une tâche existante** ()
@task_bp.put('/<string:id_task>')
@expects_json(patch_task_dto)
def update(id_task):
    body = request.json
    task = ts.update_one(id_task, body)
    if task is None: 
        return {"error": "Task Not Found"}, 404
    return jsonify(task)

#### e. **Supprimer une tâche** ()
@task_bp.delete('/<string:id_task>')
def delete(id_task): 
    response, status_code = ts.delete_one(id_task)
    return jsonify(response), status_code

