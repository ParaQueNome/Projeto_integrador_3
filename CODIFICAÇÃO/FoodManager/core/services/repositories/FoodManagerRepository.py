from core.services.ConnectionService import ConnectionService


class FoodManagerRepository:
    def __init__(self, conexao: ConnectionService) -> None:
        self.conexao = conexao

    def insert(self, collection, **kwargs):
        self.conexao.insert(collection, **kwargs)

    def find(self, collection, **kwargs):
        return self.conexao.find(collection, **kwargs)

    def update(self, collection, **kwargs):
        self.conexao.update(collection, **kwargs)

    def delete(self, collection, **kwargs):
        self.conexao.delete(collection, **kwargs)
