from flask import Flask
from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandle

redisCH = RedisConnectionHandler()
sqliteCH = SqliteConnectionHandle()

redisCH.connect()
sqliteCH.connect()

app = Flask(__name__)

from src.main.routes.products_routes import product_routes_bp

app.register_blueprint(product_routes_bp)
