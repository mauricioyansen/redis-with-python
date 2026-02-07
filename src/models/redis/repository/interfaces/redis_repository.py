from abc import ABC, abstractmethod


class IRedisRepo(ABC):

    @abstractmethod
    def insert(self, key: str, value: any) -> None:
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        pass

    @abstractmethod
    def insert_hash(self, key: str, field: str, value: any) -> None:
        pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> any:
        pass

    @abstractmethod
    def insert_ex(self, key: str, value: any, ttl: int) -> None:
        pass

    @abstractmethod
    def insert_hash_ex(self, key: str, field: str, value: any, ttl: int) -> None:
        pass
