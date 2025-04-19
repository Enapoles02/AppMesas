from firebase_init import db
from datetime import datetime

# Usuarios base
users = [
    {"nombre": "Chris", "email": "chris@porfirio.com", "rol": "Mesero", "activo": True},
    {"nombre": "Cocina", "email": "cocina@porfirio.com", "rol": "Cocina", "activo": True},
    {"nombre": "Bebidas", "email": "bebidas@porfirio.com", "rol": "Bebidas", "activo": True},
    {"nombre": "Helados", "email": "helados@porfirio.com", "rol": "Helados", "activo": True},
    {"nombre": "Inventario", "email": "inventario@porfirio.com", "rol": "Inventario", "activo": True}
]

for user in users:
    db.collection("users").add(user)

# Menú base
menu = [
    {"nombre": "Churros Tradicionales", "tipo": "Cocina", "precio": 39, "stock": 120, "activo": True},
    {"nombre": "Café Americano", "tipo": "Bebidas", "precio": 29, "stock": 80, "activo": True},
    {"nombre": "Carlota", "tipo": "Helados", "precio": 45, "stock": 60, "activo": True}
]

for item in menu:
    db.collection("menu").add(item)

# Ejemplo de orden
orden = {
    "mesa": "Mesa 1",
    "productos": [
        {"nombre": "Churros Tradicionales", "cantidad": 2, "tipo": "Cocina"},
        {"nombre": "Café Americano", "cantidad": 1, "tipo": "Bebidas"}
    ],
    "estado": "Pendiente",
    "fecha": datetime.now().isoformat(),
    "usuario": "chris@porfirio.com"
}

db.collection("ordenes").add(orden)
