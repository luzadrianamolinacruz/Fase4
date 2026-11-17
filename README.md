# Software FJ

## Descripción

Software FJ es una aplicación de consola desarrollada en Python para gestionar clientes, servicios y reservas de una empresa de soporte y operación, con un enfoque en programación orientada a objetos (POO).

El sistema permite administrar información de manera estructurada y segura. Incluye validación de entradas, gestión de estados de reserva, cálculo de costos con impuestos y descuentos, y registro de eventos importantes en archivos de log para facilitar la auditoría.

Este proyecto fue desarrollado como ejercicio práctico de diseño orientado a objetos, validación de datos y manejo de errores en Python.

## Características principales

- Registro y validación de clientes.
- Gestión de servicios con distinta lógica de negocio.
- Creación y control de reservas por horas.
- Confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos con IVA y descuentos.
- Manejo de errores mediante excepciones personalizadas.
- Registro de eventos y errores en `software_fj.log`.
- Ejecución continua de la aplicación ante errores controlados.

## Arquitectura del proyecto

El proyecto está organizado en módulos con responsabilidades específicas:

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada de la aplicación. |
| `cliente.py` | Modelo de cliente con validaciones y encapsulamiento. |
| `servicios.py` | Jerarquía de servicios: `ReservaSala`, `AlquilerEquipo` y `Asesoria`. |
| `reserva.py` | Lógica de reservas, estados y procesamiento. |
| `entidades.py` | Clase base abstracta para la estructura del sistema. |
| `excepciones.py` | Definición de excepciones personalizadas del dominio. |
| `logger.py` | Configuración del sistema de logging. |
| `software_fj.log` | Historial de eventos y errores de ejecución. |

## Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos (POO).
- Módulo `logging` de Python.
- Excepciones personalizadas.

## Requisitos

- Python 3.9 o superior.

## Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone <url-del-repositorio>
   ```

2. Ingresa al directorio del proyecto:

   ```bash
   cd Fase4
   ```

3. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

## Flujo principal del sistema

1. Se registran clientes mediante validaciones de nombre, documento, correo electrónico y teléfono.
2. Se crean servicios, que pueden estar disponibles o no disponibles.
3. Se realiza una reserva asociando un cliente, un servicio y una cantidad de horas.
4. La reserva puede confirmarse, cancelarse o procesarse.
5. El sistema calcula el costo total aplicando las validaciones correspondientes, IVA y descuentos cuando corresponda.
6. Si ocurre un error, se captura de forma controlada y se registra en el archivo de log sin interrumpir la ejecución.

## Manejo de errores

La aplicación define excepciones específicas para cada caso del dominio, por ejemplo:

- `ValidacionError`
- `ClienteError`
- `ReservaError`
- `ServicioNoDisponibleError`
- `CalculoError`

Esto permite una mejor trazabilidad y una separación clara entre errores de validación, reglas de negocio y cálculos.

## Registro de logs

Los eventos del sistema se almacenan en el archivo:

`software_fj.log`

Se registran tanto las operaciones exitosas como los errores, facilitando la revisión, auditoría y depuración del comportamiento de la aplicación.

## Estado del proyecto

Proyecto académico orientado a la práctica de conceptos fundamentales de programación orientada a objetos, validación de datos y manejo de excepciones en Python.

## Licencia

Este proyecto se distribuye con fines educativos y de aprendizaje.
