class Paciente:
    def __init__(self, nombre: str, edad: int, descripcion: str, prioridad: int):
        self.nombre: str = nombre
        self.edad: int = edad
        self.descripcion: str = descripcion
        self.prioridad:int = prioridad
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(f"paciente: {self.nombre} \n condicion: {self.descripcion} \n prioridad: {self.prioridad} \n ")

class Hospital:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self, paciente):
        if paciente == None:
            return
        else:
            print(paciente)
            self.traverse(paciente.next)

    def Inserción(self, paciente_en_fila, nombre, edad, descripcion, prioridad):
        paciente_a_ingresar = Paciente(nombre, edad, descripcion, prioridad)

        if self.size == 0:

            self.head = paciente_a_ingresar
            self.tail = paciente_a_ingresar

            self.size += 1
            return
        
        if self.size == 1:

            if paciente_a_ingresar.prioridad < self.head.prioridad:

                paciente_a_mover = self.head

                paciente_a_ingresar.next = paciente_a_mover
                paciente_a_mover.prev = paciente_a_ingresar

                self.head = paciente_a_ingresar

                self.size += 1
                return
            
            else:

                self.tail.next = paciente_a_ingresar
                paciente_a_ingresar.prev = self.tail
                self.tail = paciente_a_ingresar

                self.size += 1
                return


        else:
            
            if paciente_a_ingresar.prioridad < self.head.prioridad:

                paciente_a_mover = self.head

                paciente_a_ingresar.next = paciente_a_mover
                paciente_a_mover.prev = paciente_a_ingresar

                self.head = paciente_a_ingresar

                self.size += 1
                return
        
            if paciente_en_fila.next == None:
                if paciente_a_ingresar.prioridad < paciente_en_fila.prioridad:
                    paciente_en_fila.prev.next = paciente_a_ingresar
                    paciente_a_ingresar.prev = paciente_en_fila.prev
                    paciente_en_fila.prev = paciente_a_ingresar
                    paciente_a_ingresar.next = paciente_en_fila
                    self.size += 1
                    return
                
                else:
                    self.tail.next = paciente_a_ingresar
                    paciente_a_ingresar.prev = paciente_en_fila
                    self.tail = paciente_a_ingresar
                    self.size += 1
                    return
            
            if paciente_a_ingresar.prioridad < paciente_en_fila.prioridad:
                paciente_en_fila.prev.next = paciente_a_ingresar
                paciente_a_ingresar.prev = paciente_en_fila.prev
                paciente_en_fila.prev = paciente_a_ingresar
                paciente_a_ingresar.next = paciente_en_fila
                self.size += 1
                return
            self.Inserción(paciente_en_fila.next, nombre, edad, descripcion, prioridad)

    def Atencion(self):
        paciente_a_atender = self.head
        paciente_que_sigue = self.head.next

        paciente_que_sigue.prev = None
        paciente_a_atender.next = None

        self.head = paciente_que_sigue

        self.size -= 1
        return

    def ActualizarPrioridad(self, paciente_a_actualizar, nombre_paciente_a_actualizar, nueva_prioridad):
        
        if nombre_paciente_a_actualizar == self.head.nombre:

            paciente_a_actualizar = self.head

            self.head.next.prev = None
            self.head = self.head.next
            paciente_a_actualizar.next = None

            self.size -= 1
            self.Inserción(self.head, paciente_a_actualizar.nombre, paciente_a_actualizar.edad, paciente_a_actualizar.descripcion, nueva_prioridad)

        if nombre_paciente_a_actualizar == self.tail.nombre:

            paciente_a_actualizar = self.tail

            self.tail = self.tail.prev
            self.tail.next = None
            paciente_a_actualizar.prev = None

            self.size -= 1
            self.Inserción(self.head, paciente_a_actualizar.nombre, paciente_a_actualizar.edad, paciente_a_actualizar.descripcion, nueva_prioridad)
            
        else:
                
            if paciente_a_actualizar.nombre.lower() == nombre_paciente_a_actualizar.lower():

                paciente_a_actualizar.prev.next = paciente_a_actualizar.next
                paciente_a_actualizar.next.prev = paciente_a_actualizar.prev

                paciente_a_actualizar.next = None
                paciente_a_actualizar.prev = None

                self.size -= 1
                self.Inserción(self.head, paciente_a_actualizar.nombre, paciente_a_actualizar.edad, paciente_a_actualizar.descripcion, nueva_prioridad)
            
            else:
                self.ActualizarPrioridad(paciente_a_actualizar.next, nombre_paciente_a_actualizar, nueva_prioridad)

H = Hospital()

H.Inserción(H.head, "juan", 15, "dolor", 2)
H.Inserción(H.head, "samuel", 15, "dolor", 2)
H.Inserción(H.head, "alejandro", 15, "dolor", 1)
H.traverse(H.head)
print("\n")

H.ActualizarPrioridad(H.head, "alejandro", 3)
H.traverse(H.head)
print("\n")