# Autor: Janer Bustillo
# Descripción: Programa para gestionar una cola de pacientes en un hospital, considerando la gravedad y edad del paciente.
# El programa permite registrar pacientes, atender al paciente con mayor gravedad y mostrar la lista de pacientes en espera.
# Se utiliza una lista para almacenar los pacientes y se ordena según la gravedad y edad.
# Se implementa un menú para interactuar con el usuario y realizar las operaciones deseadas.


class Paciente:
    # Se define la clase Paciente con los atributos nombre, edad, enfermedad, gravedad y prioridad.
    def __init__(self, nombre, edad, enfermedad, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad
        self.gravedad = gravedad
        self.prioridad = self.calcular_prioridad()
    
    def calcular_prioridad(self):
        # Método para calcular la prioridad del paciente según su edad.
        # Se asigna una prioridad diferente según la edad del paciente.
        if self.edad < 12:
            return 1  # Niño
        elif self.edad > 65:
            return 2  # Adulto mayor
        else:
            return 3  # Adulto normal

    def __repr__(self):
        # Método para representar el paciente como una cadena.
        # Se muestra el nombre, edad, enfermedad, gravedad y prioridad del paciente.
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Enfermedad: {self.enfermedad}, Gravedad: {self.gravedad}, Prioridad Edad: {self.prioridad}"

def registrar_paciente(pacientes):
    # Función para registrar un nuevo paciente.
    # Se solicita al usuario el nombre, edad, enfermedad y gravedad del paciente.
    # Se valida la gravedad y edad ingresadas.
    try:
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        enfermedad = input("Ingrese la enfermedad del paciente: ")
        gravedad = int(input("Ingrese la gravedad del paciente (1-5): "))

        if gravedad < 1 or gravedad > 5:
            raise ValueError("Gravedad inválida. Debe ser un número entre 1 y 5.")
        if edad < 0:
            raise ValueError("Edad inválida. Debe ser un número positivo.")

        paciente = Paciente(nombre, edad, enfermedad, gravedad)
        pacientes.append(paciente)
        # Se ordena la lista de pacientes según la gravedad, prioridad y edad.
        # La gravedad tiene mayor prioridad, luego la prioridad por edad y finalmente la edad.
        pacientes.sort(key=lambda x: (x.gravedad, x.prioridad, x.edad))

        print(f"Paciente {nombre} registrado con éxito.")

    except ValueError as e:
        print(f"Error: {e}")

def atender_paciente(pacientes):
    # Función para atender al paciente con mayor gravedad.
    # Se verifica si hay pacientes en la lista y se atiende al primero de la lista.

    if not pacientes:
        print("No hay pacientes en la cola.")
        return

    # Se atiende al paciente con mayor gravedad y se elimina de la lista.
    # Se utiliza el método pop(0) para eliminar el primer paciente de la lista.
    paciente_atendido = pacientes.pop(0)
    print(f"Atendiendo a {paciente_atendido}")
    print("Paciente atendido con éxito.")

def mostrar_pacientes(pacientes):
    # Función para mostrar la lista de pacientes en la cola.
    # Se verifica si hay pacientes en la lista y se imprime la información de cada uno.
    if not pacientes:
        print("No hay pacientes en la cola.")
        return
    print("\nLista de pacientes en la cola:")
    for i, paciente in enumerate(pacientes):
        print(f"{i + 1}. {paciente}")

def main():
    # Función principal que ejecuta el programa.
    # Se inicializa una lista vacía para almacenar los pacientes.
    # Se muestra un menú con las opciones disponibles y se llama a las funciones correspondientes según la opción seleccionada.
    # Se utiliza un bucle infinito para permitir múltiples operaciones hasta que el usuario decida salir.
    pacientes = []
    while True:
        print("\nOpciones:")
        print("1. Registrar paciente")
        print("2. Atender paciente")
        print("3. Mostrar lista de pacientes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_paciente(pacientes)
        elif opcion == "2":
            atender_paciente(pacientes)
        elif opcion == "3":
            mostrar_pacientes(pacientes)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()