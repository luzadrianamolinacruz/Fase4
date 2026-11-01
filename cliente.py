import re
from excepciones import ClienteInvalidoError


class Cliente:
    """Representa un cliente de Software FJ con datos encapsulados."""

    def _init_(self, nombre, documento, correo, telefono):
        self.__nombre = None
        self.__documento = None
        self.__correo = None
        self.__telefono = None
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener al menos 3 caracteres."
            )
        self.__nombre = valor.strip().title()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        valor = str(valor).strip()
        if not valor.isdigit() or not (5 <= len(valor) <= 12):
            raise ClienteInvalidoError(
                "El documento debe tener entre 5 y 12 dígitos."
            )
        self.__documento = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not isinstance(valor, str) or not re.match(patron, valor.strip()):
            raise ClienteInvalidoError("El correo electrónico no es válido.")
        self.__correo = valor.strip().lower()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        valor = str(valor).strip()
        if not valor.isdigit() or len(valor) != 10:
            raise ClienteInvalidoError(
                "El teléfono debe tener 10 dígitos."
            )
        self.__telefono = valor

    def _str_(self):
        return (
            f"Cliente: {self._nombre} | Doc: {self._documento} | "
            f"Correo: {self._correo} | Tel: {self._telefono}"
        )
