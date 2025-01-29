class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de horas asignadas

    def asignar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
            return True
        return False


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []  # Lista de horarios asignados
        self.conductores_asignados = {}  # {hora: conductor}

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def asignar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
            return True
        return False

    def asignar_conductor(self, conductor, hora):
        if hora in self.conductores_asignados:
            return False  # Ya hay un conductor en este horario
        if conductor.asignar_horario(hora):
            self.conductores_asignados[hora] = conductor
            return True
        return False


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa):
        self.buses.append(Bus(placa))

    def agregar_conductor(self, nombre):
        self.conductores.append(Conductor(nombre))

    def buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        return None

    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

    def menu(self):
        while True:
            print("\n1. Agregar Bus\n2. Agregar Ruta a Bus\n3. Registrar Horario a Bus\n4. Agregar Conductor")
            print("5. Asignar Horario a Conductor\n6. Asignar Bus a Conductor\n7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                self.agregar_bus(placa)
            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ")
                bus = self.buscar_bus(placa)
                if bus:
                    ruta = input("Ingrese la ruta del bus: ")
                    bus.asignar_ruta(ruta)
                else:
                    print("Bus no encontrado.")
            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                bus = self.buscar_bus(placa)
                if bus:
                    hora = input("Ingrese el horario (hh:mm): ")
                    if bus.asignar_horario(hora):
                        print("Horario asignado.")
                    else:
                        print("Horario ya existe.")
                else:
                    print("Bus no encontrado.")
            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)
            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                conductor = self.buscar_conductor(nombre)
                if conductor:
                    hora = input("Ingrese el horario (hh:mm): ")
                    if conductor.asignar_horario(hora):
                        print("Horario asignado.")
                    else:
                        print("Horario ya está ocupado.")
                else:
                    print("Conductor no encontrado.")
            elif opcion == "6":
                placa = input("Ingrese la placa del bus: ")
                bus = self.buscar_bus(placa)
                if bus:
                    nombre = input("Ingrese el nombre del conductor: ")
                    conductor = self.buscar_conductor(nombre)
                    if conductor:
                        hora = input("Ingrese el horario (hh:mm): ")
                        if bus.asignar_conductor(conductor, hora):
                            print("Conductor asignado.")
                        else:
                            print("Horario ya está ocupado.")
                    else:
                        print("Conductor no encontrado.")
                else:
                    print("Bus no encontrado.")
            elif opcion == "7":
                break
            else:
                print("Opción no válida.")


admin = Admin()
admin.menu()