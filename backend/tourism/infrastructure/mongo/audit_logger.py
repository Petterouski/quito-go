from datetime import datetime
from pymongo import MongoClient

# Conexión al contenedor de Mongo (en docker-compose, el servicio "mongo")
client = MongoClient("mongodb://mongo:27017/")
# Selecciona la base de datos de auditoría
db = client["quitogo_audit_db"]
# Selecciona la colección donde se guardarán los logs
collection = db["audit_logs"]

# Función para registrar acciones realizadas en el sistema
def log_action(action: str, entity: str, entity_id: int, user: str, details: dict):
    
    from datetime import datetime 
    log = {
        "action": action,
        "entity": entity,
        "entity_id": entity_id,
        "timestamp": datetime.utcnow().isoformat(),
        "user": user,
        "details": details
    }
    collection.insert_one(log)
