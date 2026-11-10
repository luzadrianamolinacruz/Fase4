"""Clase Reserva: integra cliente, servicio, duración y estado."""

from cliente import Cliente
from entidades import Entidad
from excepciones import (
    CalculoError,
    ReservaError,
    ServicioNoDisponibleError,
    SoftwareFJError,
    ValidacionError,
)
from logger import log
from servicios import Servicio


class Reserva(Entidad):
    PENDIENTE, CONFIRMADA, CANCELADA, PROCESADA = "pendiente", "confirmada", "cancelada", "procesada"

    def __init__(self, cliente: Cliente, servicio: Servicio, horas: float):
        if not isinstance(cliente, Cliente):
            raise ReservaError("La reserva necesita un cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaError("La reserva necesita un servicio válido.")
        if not servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{servicio.nombre}' no está disponible.")
        servicio.validar_parametros(horas)
        super().__init__()
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = self.PENDIENTE

    def confirmar(self):
        if self.estado != self.PENDIENTE:
            raise ReservaError(f"No se puede confirmar una reserva {self.estado}.")
        self.estado = self.CONFIRMADA
        log.info(f"Reserva #{self.id} confirmada para {self.cliente.nombre}")

    def cancelar(self):
        if self.estado in (self.CANCELADA, self.PROCESADA):
            raise ReservaError(f"No se puede cancelar una reserva {self.estado}.")
        self.estado = self.CANCELADA
        log.info(f"Reserva #{self.id} cancelada")

    def procesar(self, impuesto: bool = True, descuento: float = 0.0) -> float:
        """Procesa la reserva con try/except/else/finally y encadenamiento de excepciones."""
        try:
            if self.estado != self.CONFIRMADA:
                raise ReservaError(f"Solo se procesan reservas confirmadas (estado: {self.estado}).")
            costo = self.servicio.costo_total(self.horas, impuesto, descuento)
        except (CalculoError, ValidacionError) as causa:
            # Encadenamiento: se conserva la causa original
            raise ReservaError(f"No se pudo calcular el costo de la reserva #{self.id}") from causa
        else:
            self.estado = self.PROCESADA
            log.info(f"Reserva #{self.id} procesada, total ${costo:,.2f}")
            return costo
        finally:
            log.info(f"Intento de procesar la reserva #{self.id} (estado final: {self.estado})")

    def describir(self) -> str:
        return (
            f"Reserva #{self.id} [{self.estado}] {self.cliente.nombre} -> "
            f"{self.servicio.nombre}, {self.horas} h"
        )
