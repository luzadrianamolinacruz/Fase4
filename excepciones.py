class ErrorSistema(Exception):
    """Excepción base del sistema Software FJ."""


class ClienteInvalidoError(ErrorSistema):
    """Se lanza cuando los datos de un cliente no son válidos."""
