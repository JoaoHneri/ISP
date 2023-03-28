from impressora_mult_funcional import ImpressoraMultifuncional
from impressora_simples import ImpressoraSimples


class Main:
    def run(self):
        # Criando uma instância de ImpressoraSimples e chamando o método imprimir
        impressora_simples = ImpressoraSimples()
        impressora_simples.imprimir("documento")

        # Criando uma instância de ImpressoraMultifuncional e chamando os métodos imprimir, digitalizar, enviarEmail, copiar e fax
        impressora_multifuncional = ImpressoraMultifuncional()
        impressora_multifuncional.imprimir("documento")
        impressora_multifuncional.digitalizar("documento")
        impressora_multifuncional.enviarEmail("documento", "destinatario@example.com")
        impressora_multifuncional.copiar("documento")
        impressora_multifuncional.fax("documento", "fax@example.com")

if __name__ == '__main__':
    Main().run()
