from .repositories.FoodManagerRepository import FoodManagerRepository


class CadastroProdutoService:
    def __init__(self, repository: FoodManagerRepository) -> None:
        self.repository = repository

    def insert(self, data):
        return self.repository.insert("Produtos", **data)


class CadastroRequerenteService:
    def __init__(self, repository: FoodManagerRepository) -> None:
        self.repository = repository

    def insert(self, data):
        return self.repository.insert("Requerentes", **data)

    def update(self, data):
        return self.repository.update("Requerentes", **data)

    def delete(self, data):
        return self.repository.delete("Requerentes", **data)
