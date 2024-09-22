from flask import Flask
from flask_cors import CORS
from task_controller import task_bp
from statistics_controller import stats_bp


app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["*"], 
        "methods":["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    }
})
app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(stats_bp, url_prefix='/statistics')

### Route hello world fonctionnelle 
@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello_World!", 200
