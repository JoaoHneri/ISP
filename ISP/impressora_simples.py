from fotocopia import FotoCopia
from imprimir import Imprimir
from scanner import Scanner


class ImpressoraSimples:
    def __init__(self, impressao: Imprimir) -> None:
        self.impressao = impressao

    def imprimir(self):
        self.impressao.executar()