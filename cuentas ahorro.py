from Cuentas import Cuentas_Bancarias


class Cuenta_ahorro(Cuentas_Bancarias):
    def __init__(self, intereses: float = 0, numero=None, nombre=None, saldo: float = 0):
        self._intereses = intereses
        super(Cuenta_ahorro, self).__init__(numero=numero, nombre=nombre, saldo=saldo)

    @property
    def intereses(self):
        return self._intereses

    @intereses.setter
    def intereses(self, intereses):
        self._intereses = intereses

    def pagar_interes(self):
        self._saldo = self._saldo + ((float(self._saldo) * int(self._intereses)) / 100)
        return self._saldo


if __name__ == '__main__':
    ca = Cuenta_ahorro(20, '0957752322', 'elizabeth', '5000')

    ca.mostrar_saldo()

    ca.credito(5000)

    ca.mostrar_saldo()

    ca.debito(200)

    ca.mostrar_saldo()

    print(ca)