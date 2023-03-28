from fotocopia import FotoCopia
from imprimir import Imprimir
from scanner import Scanner


class ImpressoraMultiFuncional:
    def __init__(self, impressao: Imprimir, scannear: Scanner, fotocopiar: FotoCopia) -> None:
        self.impressao = impressao
        self.scannear = scannear
        self.fotocopiar = fotocopiar

    def imprimir(self):
        self.impressao.executar()

    def scanner(self):
        self.scannear.executar()

    def fotocopia(self):
        self.fotocopiar.executar()