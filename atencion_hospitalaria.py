class Node:
    """
    Clase para crear cada nodo de la lista enlazada
    
    ENTRADAS
    ----------
    Value: Es el valor de cada nodo y es un objeto de tipo paciente 
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Paciente:
    """
    Clase para crear objetos de tipo paciente con los atributos "nombre", "edad", "condición/descripción" y "prioridad"
    
    ENTRADAS
    ----------
    nombre: Nombre de cada paciente 
    edad: Edad actual del paciente
    condición/descripción: Pequeña descripcion de los sintomas o de la condicion del paciente
    prioridad: Segun la condición, prioridad que tendra en paciente en la lista enlazada
    """

    def __init__(self, nombre: str, edad: int, descripcion: str, prioridad: int):
        self.nombre: str = nombre
        self.edad: int = edad
        self.descripcion: str = descripcion
        self.prioridad:int = prioridad

    def __repr__(self):
        return str(f"paciente: {self.nombre} \n condicion: {self.descripcion} \n prioridad: {self.prioridad} \n ")

class Hospital:
    """
    Clase que será la lista doblemente enlazada, la cual se tratará como una cola de prioridad 
    
    ENTRADAS
    ----------
    nombre: Nombre de cada paciente 
    edad: Edad actual del paciente
    condición/descripción: Pequeña descripcion de los sintomas o de la condicion del paciente
    prioridad: Segun la condición, prioridad que tendra en paciente en la lista enlazada
    """
    def __init__(self):
        #Esta variable guarda el primer nodo de la lista enlazada
        self.head = None

        #Esta variable guarda el ultimo nodo de la lista enlazada
        self.tail = None

        #Esta variable guarda el el tamaño de la lista enlazada, basandose en la cantidad de nodos que haya en esta
        self.size = 0


    #Metodo para recorrer la lista enlazada e imprimir el valor de cada nodo
    def traverse(self, node):
        if self.size == 0:
            return
        elif node == None:
            return
        else:
            print(node.value)
            self.traverse(node.next)

    #Metodo para insertar pacientes a la lista enlazada
    def Inserción(self, paciente_en_fila, nombre, edad, descripcion, prioridad):
        paciente_a_ingresar = Paciente(nombre, edad, descripcion, prioridad)
        new_node = Node(paciente_a_ingresar)

        #Condicional para saber si es la primera vez que se va a insertar un paciente a la lista enlazada
        if self.size == 0:

            #Si es la primera vez que se va a insertar un paciente, este seria el primero y el ultimo al mismo tiempo
            self.head = new_node
            self.tail = new_node

            #Como se agregó un paciente a la lista, el size aumenta en uno
            self.size += 1
            return
        
        #Condicional para saber si hay solo un paciente en la lista enlazada
        if self.size == 1:
            
            #Condicional interno, para comprobar si la prioridad del paciente que se va a ingresar es menor que la prioridad del que ya está
            if paciente_a_ingresar.prioridad < self.head.value.prioridad:

                #Si la condicion anerior se cumple, se guarda el paciente que ya está en una variable para poder moverlo
                paciente_a_mover = self.head

                #Se conectan los dos pacientes en la lista enlazada
                new_node.next = paciente_a_mover
                paciente_a_mover.prev = new_node
                
                #Se actualiza el head, haciendo que su value sea el paciente que se va a ingresar
                self.head = new_node

                #Como se agregó un paciente a la lista, el size aumenta en uno
                self.size += 1
                return
            
            #Si la condición anterior no se cumple, el paciente que se va a ingresar debe quedar al final de la lista enlazada
            else:

                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

                self.size += 1
                return

        #Si hay mas de un paciente en la lista enlazada
        else:
            
            #Condicional para evaluar si la prioridad del paciente que se va a ingresar es menor que la prioridad del head
            if paciente_a_ingresar.prioridad < self.head.value.prioridad:

                #Si la condicion anerior se cumple, se guarda el paciente que ya está en una variable para poder moverlo
                paciente_a_mover = self.head

                #Se conectan los dos pacientes en la lista enlazada
                new_node.next = paciente_a_mover
                paciente_a_mover.prev = new_node

                #Se actualiza el head, haciendo que su value sea el paciente que se va a ingresar
                self.head = new_node

                #Como se agregó un paciente a la lista, el size aumenta en uno
                self.size += 1
                return
        
            #Como el software es recursivo, se crea un caso base para detener la recursión
            #Condicional que será en caso base, para evaluar si ya se recorrio la lista enlazada y llegamos al ultimo nodo
            if paciente_en_fila.next == None:

                #Condicional para evaluar si la prioridad del paciente que se va a agregar es menor a la prioridad del ultimo nodo
                if paciente_a_ingresar.prioridad < paciente_en_fila.value.prioridad:

                    #Si la condicion anterior se cumple, se conectan los dos nodos
                    paciente_en_fila.prev.next = new_node
                    new_node.prev = paciente_en_fila.prev
                    paciente_en_fila.prev = new_node
                    new_node.next = paciente_en_fila

                    #Como se agregó un paciente a la lista, el size aumenta en uno
                    self.size += 1
                    return
                
                
                #si la prioridad del paciente que se va a agregar no es menor a la prioridad del ultimo nodo
                else:

                    #Se agrega el paciente al final de la lista enlazada y este se convertiria en el tail
                    self.tail.next = new_node
                    new_node.prev = paciente_en_fila
                    self.tail = new_node

                    #Como se agregó un paciente a la lista, el size aumenta en uno
                    self.size += 1
                    return
            
            #Condicional para evaluar si la prioridad del paciente a agregar es menor a la prioridad de algun nodo de la lista enlazada
            if paciente_a_ingresar.prioridad < paciente_en_fila.value.prioridad:

                #Cuando la condición anterior se cumpla, se ingresa el paciente conectandolo con el nodo anterior y el siguiente
                paciente_en_fila.prev.next = new_node
                new_node.prev = paciente_en_fila.prev
                paciente_en_fila.prev = new_node
                new_node.next = paciente_en_fila

                #Como se agregó un paciente a la lista, el size aumenta en uno
                self.size += 1
                return
            
            #Llamado recursivo para cambiar de nodo
            self.Inserción(paciente_en_fila.next, nombre, edad, descripcion, prioridad)

    def Atencion(self):
        """
        Metodo para atender al primer paciente que se encuentre en la lista enlazada
        """

        print("------------------------------------")
        print(f"PACIENTE ATENDIDO CORRECTAMENTE:")
        #Se hace un print del paciente que se encuentra en el head, ya que este es el que tiene la prioridad menor
        print(self.head.value)
        print("------------------------------------")

        #Se eliminan las conexiones entre el head y el nodo que sigue, para luego volver este nodo el nuevo head
        paciente_a_atender = self.head
        paciente_que_sigue = self.head.next
        paciente_que_sigue.prev = None
        paciente_a_atender.next = None

        self.head = paciente_que_sigue

        #Como se eliminó un paciente a la lista, el size disminuye en uno
        self.size -= 1
        return

    def ActualizarPrioridad(self, paciente_a_actualizar, nombre_paciente_a_actualizar, nueva_prioridad):
        """
        Metodo para actualizar la prioridad de un paciente que se encuentre en la lista enlazada

        ENTRADAS
        --------
        paciente_a_actualizar: Es donde se guardará el paciente de cada nodo, su valor inicial es el head
        nombre_paciente_a_actualizar: Es donde se guardará el nombre del paciente que se desea actualizar
        nueva_prioridad: Es en donde se guardará la nueva prioridad con la que quedará el paciente
        """
        
        #Condicional para evaluar si el paciente que se va a actualizar es el primero de la lista enlazada(head)
        if nombre_paciente_a_actualizar == self.head.value.nombre:
            
            #Si la condicion anerior se cumple, se guarda el head en una variable
            paciente_a_actualizar = self.head

            #Se eliminan las conexiones del head, y se actualiza la lista dejando como el nuevo head el nodo siguiente 
            self.head.next.prev = None
            self.head = self.head.next
            paciente_a_actualizar.next = None

            #Como se eliminó un paciente a la lista, el size disminuye en uno
            self.size -= 1

            #Se llama al metodo "Insercion", para agregar los datos del mismo paciente pero con la nueva prioridad
            self.Inserción(self.head, paciente_a_actualizar.value.nombre, paciente_a_actualizar.value.edad, paciente_a_actualizar.value.descripcion, nueva_prioridad)

        #Condicional para evaluar si el paciente que se va a actualizar es el ultimo de la lista enlazada(tail)
        if nombre_paciente_a_actualizar == self.tail.value.nombre:

            #Si la condicion anerior se cumple, se guarda el tail en una variable
            paciente_a_actualizar = self.tail

            #Se eliminan las conexiones del tail, y se actualiza la lista dejando como el nuevo tail el nodo anterior 
            self.tail = self.tail.prev
            self.tail.next = None
            paciente_a_actualizar.prev = None

            #Como se eliminó un paciente a la lista, el size disminuye en uno
            self.size -= 1

            #Se llama al metodo "Insercion", para agregar los datos del mismo paciente pero con la nueva prioridad
            self.Inserción(self.head, paciente_a_actualizar.value.nombre, paciente_a_actualizar.value.edad, paciente_a_actualizar.value.descripcion, nueva_prioridad)
        
        #Si el paciente a actualizar no está en las eaquinas
        else:
            
            #Condicional para comparar el nombre que se busca con el nodo en el que nos encontramos
            if paciente_a_actualizar.value.nombre.lower() == nombre_paciente_a_actualizar.lower():
                
                #Si la condicion anterior se cumple, guardamos en paciente en una variable y le quitamos las conexiones a su nodo
                paciente_a_actualizar.prev.next = paciente_a_actualizar.next
                paciente_a_actualizar.next.prev = paciente_a_actualizar.prev
                paciente_a_actualizar.next = None
                paciente_a_actualizar.prev = None

                #Como se eliminó un paciente a la lista, el size disminuye en uno
                self.size -= 1

                #Se llama al metodo "Insercion", para agregar los datos del mismo paciente pero con la nueva prioridad
                self.Inserción(self.head, paciente_a_actualizar.value.nombre, paciente_a_actualizar.value.edad, paciente_a_actualizar.value.descripcion, nueva_prioridad)
            
            else:

                #Llamado recursivo que se utiliza para saltar al siguiente nodo
                self.ActualizarPrioridad(paciente_a_actualizar.next, nombre_paciente_a_actualizar, nueva_prioridad)

H = Hospital()

H.Inserción(H.head, "juan", 15, "dolor", 2)
H.Inserción(H.head, "samuel", 15, "dolor", 2)
H.Inserción(H.head, "alejandro", 15, "dolor", 1)
H.traverse(H.head)
print("----------------------------------------------------------------")
print("\n")

H.ActualizarPrioridad(H.head, "alejandro", 3)
H.traverse(H.head)
print("----------------------------------------------------------------")
print("\n")

H.Atencion()
H.traverse(H.head)