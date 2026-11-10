"""Software FJ - simulación de 10+ operaciones sin base de datos."""

from cliente import Cliente
from excepciones import SoftwareFJError
from logger import RUTA_LOG, log
from reserva import Reserva
from servicios import AlquilerEquipo, Asesoria, ReservaSala


class GestorFJ:
    """Guarda clientes, servicios y reservas en listas internas."""

    def __init__(self):
        self.clientes: list[Cliente] = []
        self.servicios = []
        self.reservas: list[Reserva] = []

    def registrar_cliente(self, *args) -> Cliente:
        cliente = Cliente(*args)
        if any(c.documento == cliente.documento for c in self.clientes):
            raise SoftwareFJError(f"Ya existe un cliente con documento {cliente.documento}.")
        self.clientes.append(cliente)
        log.info(f"Cliente registrado: {cliente.describir()}")
        return cliente

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
        log.info(f"Servicio creado: {servicio.describir()}")
        return servicio

    def reservar(self, cliente, servicio, horas) -> Reserva:
        reserva = Reserva(cliente, servicio, horas)
        self.reservas.append(reserva)
        log.info(f"Reserva creada: {reserva.describir()}")
        return reserva


def operacion(numero: int, titulo: str, funcion):
    """Ejecuta una operación; si falla, registra el error y el programa sigue."""
    print(f"\n[{numero}] {titulo}")
    try:
        resultado = funcion()
    except SoftwareFJError as e:
        causa = f" (causa: {e.__cause__})" if e.__cause__ else ""
        print(f"    ERROR controlado: {e}{causa}")
        log.error(f"Operación {numero} - {titulo}: {e}{causa}")
    except Exception as e:  # cualquier error inesperado tampoco detiene el sistema
        print(f"    ERROR inesperado: {type(e).__name__}: {e}")
        log.critical(f"Operación {numero} - error inesperado: {type(e).__name__}: {e}")
    else:
        print(f"    OK: {resultado.describir() if hasattr(resultado, 'describir') else resultado}")
        return resultado
    finally:
        log.info(f"Operación {numero} finalizada")


def main():
    fj = GestorFJ()
    print("=== Software FJ ===")

    # --- Clientes ---
    ana = operacion(1, "Registrar cliente válido (Ana Torres)",
                    lambda: fj.registrar_cliente("Ana Torres", "1012345678", "ana@correo.com", "3101234567"))
    luis = operacion(2, "Registrar cliente válido (Luis Pérez)",
                     lambda: fj.registrar_cliente("Luis Pérez", "79876543", "luis@correo.com", "3209876543"))
    operacion(3, "Registrar cliente con correo inválido",
              lambda: fj.registrar_cliente("Carlos Ruiz", "1098765432", "correo-malo", "3001112233"))
    operacion(4, "Registrar cliente con documento repetido",
              lambda: fj.registrar_cliente("Ana Clon", "1012345678", "clon@correo.com", "3101112222"))

    # --- Servicios ---
    sala = operacion(5, "Crear sala de reuniones válida",
                     lambda: fj.agregar_servicio(ReservaSala("Sala Ejecutiva", 50000, 10)))
    equipo = operacion(6, "Crear alquiler de equipo válido",
                       lambda: fj.agregar_servicio(AlquilerEquipo("Portátil Pro", 12000, "Portátil")))
    asesoria = operacion(7, "Crear asesoría válida",
                         lambda: fj.agregar_servicio(Asesoria("Asesoría en Python", 80000, "Python")))
    operacion(8, "Crear servicio con tarifa inválida",
              lambda: fj.agregar_servicio(ReservaSala("Sala Rota", -100, 5)))

    # --- Reservas ---
    r1 = operacion(9, "Reserva exitosa: Ana reserva la sala 3 horas",
                   lambda: fj.reservar(ana, sala, 3))
    operacion(10, "Confirmar y procesar la reserva (con IVA)",
              lambda: (r1.confirmar(), f"total ${r1.procesar(impuesto=True):,.2f}")[1])
    operacion(11, "Reserva fallida: horas fuera de rango en la sala",
              lambda: fj.reservar(luis, sala, 20))
    equipo.disponible = False
    operacion(12, "Reserva fallida: equipo no disponible",
              lambda: fj.reservar(luis, equipo, 5))
    equipo.disponible = True
    r2 = operacion(13, "Reserva exitosa: Luis reserva una asesoría de 2 horas",
                   lambda: fj.reservar(luis, asesoria, 2))
    operacion(14, "Procesar reserva sin confirmar (operación no permitida)",
              lambda: r2.procesar())
    operacion(15, "Confirmar y procesar con descuento del 10%",
              lambda: (r2.confirmar(), f"total ${r2.procesar(impuesto=True, descuento=0.10):,.2f}")[1])
    r3 = operacion(16, "Reserva de equipo por 10 horas",
                   lambda: fj.reservar(ana, equipo, 10))
    operacion(17, "Cancelar la reserva anterior",
              lambda: (r3.cancelar(), r3.describir())[1])
    operacion(18, "Cancelar de nuevo (debe fallar)", lambda: r3.cancelar())
    operacion(19, "Procesar con descuento inválido (error encadenado)",
              lambda: fj.reservar(ana, asesoria, 1).confirmar() or fj.reservas[-1].procesar(descuento=2))
    operacion(20, "Reserva con cliente nulo (parámetro faltante)",
              lambda: fj.reservar(None, sala, 2))

    # --- Resumen ---
    print("\n=== Resumen ===")
    print(f"Clientes: {len(fj.clientes)} | Servicios: {len(fj.servicios)} | Reservas: {len(fj.reservas)}")
    for s in fj.servicios:                      # polimorfismo
        print(" -", s.describir())
    for r in fj.reservas:
        print(" -", r.describir())
    print(f"\nEl programa terminó sin caerse. Log en: {RUTA_LOG}")


if __name__ == "__main__":
    main()
