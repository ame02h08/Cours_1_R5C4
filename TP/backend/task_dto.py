
task_dto = {
    "type":"object",
    "properties":{
    "categorie" : {"type": "string"},
    "description": {"type": "string"},
    "nom":{"type": "string"},
    "priorite": {"type": "integer"},
    "statut": {"type": "string", "enum" : ["TODO", "IN_PROGRESS", "DONE"]},
    "utilisateur": {"type": "string"}
    },
    "required": ["categorie", "description", "nom", "priorite", "statut", "utilisateur"],  
    "additionalProperties": True
}

patch_task_dto = {
    **task_dto,
    "required": []
}