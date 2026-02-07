from flask import Flask
from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from src.main.routes.products_routes import product_routes_bp

redis = RedisConnectionHandler()
sqlite = SqliteConnectionHandle()

redis.connect()
sqlite.connect()

app = Flask(__name__)


app.register_blueprint(product_routes_bp)
