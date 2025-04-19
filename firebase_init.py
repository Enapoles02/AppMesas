import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al JSON de credenciales (lo subes como secreto en GitHub luego)
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

# Cliente Firestore
db = firestore.client()
