class Mesa:

    def __init__(self, numero:int, lugares:int, ocupada: bool):
        self.__numero = numero
        self.__lugares = lugares
        self.__ocupada = ocupada

    @property
    def numero(self):
        return self.__numero

    @property
    def lugares(self):
        return self.__lugares

    @property
    def ocupada(self):
        return self.__ocupada

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @lugares.setter
    def lugares(self, lugares: int):
        self.__lugares = lugares

    @ocupada.setter
    def ocupada (self, ocupada: bool):
        self.__ocupada = ocupada