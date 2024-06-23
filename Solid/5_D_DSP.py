# O Princípio de Inversão de Dependência (DIP) afirma que módulos de alto nível não devem depender de módulos de baixo nível, ambos devem depender de abstrações.

from abc import ABC, abstractmethod

class DataStorage(ABC):
    @abstractmethod
    def save_data(self, data):
        pass

class CloudStorage(DataStorage):
    def save_data(self, data):
        print(f"Data saved to cloud: {data}")

class LocalStorage(DataStorage):
    def save_data(self, data):
        print(f"Data saved locally: {data}")

class DataManager:
    def __init__(self, storage: DataStorage):
        self.storage = storage
    
    def store_data(self, data):
        self.storage.save_data(data)

# Injeção de dependência usando abstrações
cloud_storage = CloudStorage()
local_storage = LocalStorage()
manager = DataManager(cloud_storage)
manager.store_data("Example Data")

manager = DataManager() #local_storage
manager.store_data("Example Data 2")