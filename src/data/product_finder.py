from src.models.sqlite.repository.interfaces.products_repository import IProductsRepo
from src.models.redis.repository.interfaces.redis_repository import IRedisRepo
from src.http_types.http_req import HttpReq
from src.http_types.http_res import HttpRes


class ProductFinder:
    def __init__(self, redis_repo: IRedisRepo, product_repo: IProductsRepo) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo

    def find_by_name(self, req: HttpReq) -> HttpRes:
        product_name = req.params["product_name"]
        product = None
        product = self.__find_in_cache(product_name)
        if not product:
            product = self.__find_in_sql(product_name)
            self.__insert_in_cache(product)

        return self.__format_response(product)

    def __find_in_cache(self, product_name: str) -> tuple:
        product_info = self.__redis_repo.get(product_name)
        if product_info:
            product_info_list = product_info.split(
                ","
            )  # price, quantity -> [price, quantity]
            return (0, product_name, product_info_list[0], product_info_list[1])
        return None

    def __find_in_sql(self, product_name: str) -> tuple:
        product = self.__product_repo.find_product_by_name(product_name)
        if not product:
            raise FileNotFoundError("Product not found")
        return product

    def __insert_in_cache(self, product: tuple) -> None:
        product_name = product[1]
        value = f"{product[2]}, {product[3]}"
        self.__redis_repo.insert_ex(product_name, value, ex=60)

    def __format_response(self, product: tuple) -> HttpRes:
        return HttpRes(
            status_code=200,
            body={
                "type": "PRODUCT",
                "count": 1,
                "attributes": {
                    "name": product[1],
                    "price": product[2],
                    "quantity": product[3],
                },
            },
        )
