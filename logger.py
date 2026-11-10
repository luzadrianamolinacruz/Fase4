"""Registro de eventos y errores en un archivo de logs."""

import logging
import os

RUTA_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "software_fj.log")


def crear_logger() -> logging.Logger:
    log = logging.getLogger("software_fj")
    if not log.handlers:
        log.setLevel(logging.INFO)
        archivo = logging.FileHandler(RUTA_LOG, mode="w", encoding="utf-8")
        archivo.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
        )
        log.addHandler(archivo)
    return log


log = crear_logger()

