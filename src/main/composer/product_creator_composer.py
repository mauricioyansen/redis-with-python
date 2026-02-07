from src.main.server.server import redisCH, sqliteCH
from src.models.sqlite.repository.products_repository import ProductsRepo
from src.models.redis.repository.redis_repository import RedisRepo
from src.data.product_creator import ProductCreator


def product_creator_composer():
    redis_conn = redisCH.get_connection()
    sqlite_conn = sqliteCH.get_connection()

    redis_repo = RedisRepo(redis_conn)
    products_repo = ProductsRepo(sqlite_conn)

    return ProductCreator(redis_repo, products_repo)
