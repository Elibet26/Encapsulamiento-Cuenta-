from Cuentas import Cuentas_Bancarias


class Cuenta_corriente(Cuentas_Bancarias):
    def __init__(self, numero=None, nombre=None, saldo: float = 0, tiene_Chequera=bool):
        self._tiene_Chequera = tiene_Chequera
        super(Cuenta_corriente, self).__init__(numero=numero, nombre=nombre, saldo=saldo)

    @property
    def tiene_Chequera(self):
        return self._tiene_Chequera

    @tiene_Chequera.setter
    def tiene_Chequera(self, tiene_Chequera):
        self._tiene_Chequera = tiene_Chequera

    def pagar_cheque(self):
        self._saldo = self._saldo + ((float(self._saldo) - int(self.pagar_cheque)))
        return self._saldo