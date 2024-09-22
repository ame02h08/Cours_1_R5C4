# statistics_controller.py
from flask import Blueprint, jsonify
import task_service as ts

stats_bp = Blueprint("statistics", __name__)

#### f. **Statistiques sur les tâches** ()
@stats_bp.get('/status')
def get_task_statistics():
    stats = ts.get_task_statistics()
    return jsonify(stats), 200