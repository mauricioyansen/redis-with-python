from src.models.sqlite.repository.interfaces.products_repository import IProductsRepo
from src.models.redis.repository.interfaces.redis_repository import IRedisRepo
from src.http_types.http_req import HttpReq
from src.http_types.http_res import HttpRes


class ProductCreator:
    def __init__(self, redis_repo: IRedisRepo, product_repo: IProductsRepo) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo

    def create(self, req: HttpReq) -> HttpRes:
        body = req.body
        name = body.get("name")
        price = body.get("price")
        quantity = body.get("quantity")

        self.__insert_product_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)

        return self.__format_response()

    def __insert_product_in_sql(self, name: str, price: float, quantity: int) -> None:
        self.__product_repo.insert_product(name, price, quantity)

    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:
        product_key = name
        value = f"{price},{quantity}"
        self.__redis_repo.insert_ex(product_key, value, ex=60)

    def __format_response(self) -> HttpRes:
        return HttpRes(
            status_code=201,
            body={
                "type": "PRODUCT",
                "count": 1,
                "message": "Product created successfully",
            },
        )
