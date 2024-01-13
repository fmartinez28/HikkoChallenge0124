# Desarrollador Full Stack - Prueba técnica - Hikko

## Prerequisitos:

- Python 3.11.0 o superior
- Pipenv 2023.11.15 o superior
- PostgreSQL 16.0 o superior

## Instrucciones:

1. Crear una base de datos con PostgreSQL y obtener:
  - nombre de usuario
  - contraseña
  - host
  - puerto
  - nombre de la base de datos
2. Crear un archivo .env dentro del directorio "hikko_challenge_project", con el siguiente formato:
```env
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
```
3. Completar el .env con los valores correspondientes
4. Abrir la terminal y ubicarse en la raíz del repositorio
5. Inicializar el entorno virtual escribiendo ```pipenv shell```
6. Instalar las dependencias con ```pipenv install```
7. Realizar las migraciones con ```python3 hikko_challenge_project/manage.py migrate```
8. Ejecutar el proyecto con ```python3 hikko_challenge_project/manage.py runserver```
9. El proyecto debería estar corriendo en localhost:8000

## Endpoints
Endpoint 1: localhost:8000/users/

Formato de cuerpo de respuesta:
```json
[
{
"user_id": "1",
"followers": ["2", "3", "4"]
},
]
```
Endpoint 2: localhost:8000/users/leastfollowers/

Formato de cuerpo de respuesta:
```json
{
"user_id": "1",
"amount_of_followers": 0
}
```

## Opcional
Si se requiere testear con un conjunto de datos diferente al originalmente propuesto, pero siguiendo el mismo formato de usuarios de:
```json
{
    "user_id": "1",
    "users_following": ["2", "3"]
}
```
Se deben remplazar los jsons en el directorio ```/hikko_challenge_project/users/migrations/data/``` con el nuevo conjunto. Consecuentemente, se deben eliminar las migraciones, eliminar y recrear la base de datos, y finalmente, aplicar nuevamente las migraciones con 
```python3 hikko_challenge_project/manage.py migrate```
