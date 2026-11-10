"""Clase abstracta base del sistema."""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """Entidad general del sistema (abstracción)."""

    _contador = 0

    def __init__(self):
        Entidad._contador += 1
        self._id = Entidad._contador

    @property
    def id(self) -> int:
        return self._id

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción legible de la entidad."""
