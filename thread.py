from threading import Thread # Importando classe a Built-in 'Thread' do python


class ArquiteturaThread(Thread): # criando classe Thread que herda a classe Thread importada na linha 1
    """Captura o valor de retorno da função target."""
    def __init__(self, target=None, args=()):
        super().__init__(target=target, args=args)
        self._return = None

    def run(self):
        """Executa a função target e armazena o resultado no _return."""
        if self._target is not None:
            self._return = self._target(*self._args)

    def getResult(self, *args):
        """Entra na thread e retorna o valor após o processamento da função."""
        super().join(*args)
        return self._return

