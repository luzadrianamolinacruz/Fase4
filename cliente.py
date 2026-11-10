"""Clase Cliente con validaciones y datos personales encapsulados."""

import re

from entidades import Entidad
from excepciones import ValidacionError


class Cliente(Entidad):
    """Cliente con datos personales encapsulados y validados."""

    _PATRON_CORREO = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")

    def __init__(self, nombre: str, documento: str, correo: str, telefono: str):
        super().__init__()
        self.__nombre = self._validar_nombre(nombre)
        self.__documento = self._validar_documento(documento)
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)

    # --- validaciones ---
    @staticmethod
    def _validar_nombre(nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ValidacionError("El nombre debe tener al menos 3 caracteres.")
        return nombre.strip()

    @staticmethod
    def _validar_documento(documento):
        if not isinstance(documento, str) or not documento.isdigit() or not 6 <= len(documento) <= 12:
            raise ValidacionError("El documento debe tener entre 6 y 12 dígitos.")
        return documento

    @classmethod
    def _validar_correo(cls, correo):
        if not isinstance(correo, str) or not cls._PATRON_CORREO.match(correo):
            raise ValidacionError(f"Correo inválido: {correo!r}")
        return correo

    @staticmethod
    def _validar_telefono(telefono):
        if not isinstance(telefono, str) or not telefono.isdigit() or len(telefono) != 10:
            raise ValidacionError("El teléfono debe tener 10 dígitos.")
        return telefono

    # --- acceso controlado ---
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def documento(self) -> str:
        return self.__documento

    @property
    def correo(self) -> str:
        return self.__correo

    @property
    def telefono(self) -> str:
        return self.__telefono

    @correo.setter
    def correo(self, valor):
        self.__correo = self._validar_correo(valor)

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = self._validar_telefono(valor)

    def describir(self) -> str:
        return f"Cliente #{self.id}: {self.__nombre} (doc. {self.__documento}, {self.__correo})"
