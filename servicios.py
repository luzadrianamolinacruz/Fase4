"""Clase abstracta Servicio y tres servicios especializados."""

from abc import abstractmethod

from entidades import Entidad
from excepciones import CalculoError, ValidacionError


class Servicio(Entidad):
    """Servicio abstracto: define el contrato que cumplen todos los servicios."""

    IVA = 0.19

    def __init__(self, nombre: str, tarifa_hora: float, disponible: bool = True):
        super().__init__()
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValidacionError("El servicio necesita un nombre.")
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora <= 0:
            raise ValidacionError("La tarifa por hora debe ser un número positivo.")
        self._nombre = nombre.strip()
        self._tarifa_hora = float(tarifa_hora)
        self._disponible = bool(disponible)

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = bool(valor)

    @abstractmethod
    def calcular_costo(self, horas: float) -> float:
        """Costo base según el tipo de servicio."""

    @abstractmethod
    def validar_parametros(self, horas: float) -> None:
        """Valida las horas solicitadas según las reglas del servicio."""

    # Sobrecarga simulada: un solo método con parámetros opcionales
    def costo_total(self, horas: float, impuesto: bool = False, descuento: float = 0.0) -> float:
        """Costo con impuesto (IVA) y/o descuento opcional (0 a 1)."""
        if not 0 <= descuento < 1:
            raise CalculoError(f"Descuento fuera de rango: {descuento}")
        self.validar_parametros(horas)
        total = self.calcular_costo(horas)
        total -= total * descuento
        if impuesto:
            total += total * self.IVA
        if total < 0:
            raise CalculoError("El cálculo dio un costo negativo.")
        return round(total, 2)

    def describir(self) -> str:
        estado = "disponible" if self._disponible else "no disponible"
        return f"{self._nombre} ({estado}, ${self._tarifa_hora:,.0f}/hora)"


class ReservaSala(Servicio):
    def __init__(self, nombre: str, tarifa_hora: float, capacidad: int, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValidacionError("La capacidad de la sala debe ser un entero positivo.")
        self._capacidad = capacidad

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or not 1 <= horas <= 8:
            raise ValidacionError("Una sala se reserva entre 1 y 8 horas.")

    def calcular_costo(self, horas):
        return self._tarifa_hora * horas

    def describir(self):
        return f"{super().describir()}, sala para {self._capacidad} personas"


class AlquilerEquipo(Servicio):
    RECARGO_SEGURO = 0.05

    def __init__(self, nombre: str, tarifa_hora: float, equipo: str, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not equipo or not equipo.strip():
            raise ValidacionError("Debe indicar el equipo a alquilar.")
        self._equipo = equipo.strip()

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or not 1 <= horas <= 72:
            raise ValidacionError("Un equipo se alquila entre 1 y 72 horas.")

    def calcular_costo(self, horas):
        base = self._tarifa_hora * horas
        return base + base * self.RECARGO_SEGURO  # incluye seguro

    def describir(self):
        return f"{super().describir()}, alquiler de {self._equipo} con seguro del 5%"


class Asesoria(Servicio):
    def __init__(self, nombre: str, tarifa_hora: float, especialidad: str, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not especialidad or not especialidad.strip():
            raise ValidacionError("Debe indicar la especialidad de la asesoría.")
        self._especialidad = especialidad.strip()

    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or not 0.5 <= horas <= 6:
            raise ValidacionError("Una asesoría dura entre 0.5 y 6 horas.")

    def calcular_costo(self, horas):
        # Tarifa mayor por ser trabajo especializado
        return self._tarifa_hora * horas * 1.30

    def describir(self):
        return f"{super().describir()}, asesoría en {self._especialidad}"
