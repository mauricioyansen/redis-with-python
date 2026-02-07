import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductsRepo

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()


@pytest.mark.skip(reason="database interaction")
def test_insert_product():
    repo = ProductsRepo(conn)
    name = "Kartana"
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)


@pytest.mark.skip(reason="database interaction")
def test_find_product():
    repo = ProductsRepo(conn)
    name = "Kartana"

    res = repo.find_product_by_name(name)
    print()
    print(res)
    print(type(res))
