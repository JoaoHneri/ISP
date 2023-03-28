from abc import ABC, abstractmethod


class Funcionalidade(ABC):
    @abstractmethod
    def executar(self):
        pass