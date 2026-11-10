"""Excepciones personalizadas de Software FJ."""


class SoftwareFJError(Exception):
    """Excepción base de la aplicación."""


class ValidacionError(SoftwareFJError):
    """Datos inválidos o parámetros faltantes."""


class ClienteError(SoftwareFJError):
    """Problemas al registrar o buscar clientes."""


class ServicioNoDisponibleError(SoftwareFJError):
    """El servicio no está disponible para reservar."""


class ReservaError(SoftwareFJError):
    """Intento de reserva incorrecto u operación no permitida."""


class CalculoError(SoftwareFJError):
    """Cálculo de costos inconsistente."""
    



    
