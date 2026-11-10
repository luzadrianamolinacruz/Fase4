# Software FJ – Fase 4

Sistema orientado a objetos en Python para gestionar clientes, servicios y reservas de la empresa Software FJ. No usa base de datos: todo vive en objetos y listas, y solo se escribe un archivo para el registro de eventos y errores (`software_fj.log`).

## Archivos
- `excepciones.py`: excepciones personalizadas (todas heredan de `SoftwareFJError`).
- `entidades.py`: clase abstracta `Entidad` (abstracción).
- `cliente.py`: `Cliente`, con atributos privados y validaciones (encapsulación).
- `servicios.py`: clase abstracta `Servicio` y tres servicios que heredan de ella: `ReservaSala`, `AlquilerEquipo` y `Asesoria` (herencia y polimorfismo, métodos sobrescritos para costo, descripción y validación).
- `reserva.py`: `Reserva` (cliente, servicio, duración y estado) con confirmar, cancelar y procesar.
- `logger.py`: configuración del archivo de logs.
- `main.py`: simula 20 operaciones, entre válidas e inválidas.

## Cómo se cumple lo que pide la guía
- Método "sobrecargado": `Servicio.costo_total(horas, impuesto=False, descuento=0.0)` acepta parámetros opcionales (Python no tiene sobrecarga real).
- Manejo de excepciones: `try/except` en `main.operacion`, `try/except/else/finally` en `Reserva.procesar`, y encadenamiento con `raise ... from ...`.
- Cada error se registra en `software_fj.log` y el programa sigue funcionando.

## Ejecutar
    python main.py
