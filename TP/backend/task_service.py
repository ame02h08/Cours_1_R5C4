from grand_dataset_taches import base_de_donnees_taches, next_id
from datetime import datetime

def find_many_tasks(offset: int = 0, limit: int = 10):
    return list(base_de_donnees_taches.values())[offset:offset + limit]

def find_task_by_id(id_tache):
    return base_de_donnees_taches.get(id_tache)

def create_task(body):        
        global next_id
        global base_de_donnees_taches
        current_id = int(next_id)
        body['id_tache'] = str(current_id)
        body['date_creation'] = datetime.now()
        base_de_donnees_taches[str(current_id)] = body
        next_id = str(current_id + 1)
        return base_de_donnees_taches[str(current_id)]

def update_one(id_tache, body):
    tache = base_de_donnees_taches.get(id_tache)
    if tache is None:
        return {"error": "Tâche non trouvée"}, 404
    body["date_modification"] = datetime.now()
    tache.update(body)
    return tache

def delete_one(id_tache):
    tache = base_de_donnees_taches.get(id_tache)
    if tache is None:
        return {"error": "Tâche non trouvée"}, 404
    base_de_donnees_taches.pop(id_tache)
    return {}, 204

def get_task_statistics():

    stats = {
        "En attente": 0,
        "En cours": 0,
        "Terminées": 0
    }
    for tache in base_de_donnees_taches.values():
        statut = tache.get('statut')
        if statut == 'TODO':
            stats["En attente"] += 1
        elif statut == 'IN_PROGRESS':
            stats["En cours"] += 1
        elif statut == 'DONE':
            stats["Terminées"] += 1
    
    return stats