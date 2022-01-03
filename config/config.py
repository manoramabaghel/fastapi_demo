import secrets

HOST = 'localhost'
PORT = '3306'
USER = 'manoj'
PASSWORD = 'Manoj@123'
DB = 'demo'
DBTYPE = "mysql+pymysql"
JWT_ALGORITH = 'HS256'
SECRET_KEY = secrets.token_urlsafe(16)
