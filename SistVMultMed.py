from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n
        
    def existeMedicamento(self, nombre_medicamento):
        return any(med.verNombre()== nombre_medicamento for med in self.__lista_medicamentos)
    
class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
        
    
    def verificarExiste(self,historia):
        return historia in self.__caninos or historia in self.__felinos
        
    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos) 
    
    def ingresarMascota(self,mascota):
        tipo = mascota.verTipo().lower()
        historia = mascota.verHistoria()
        
        if tipo == "canino":
            self.__caninos[historia] = mascota
            
        elif tipo == "felino":
            self.__felinos[historia] = mascota
            
    def buscarMascota(self, historia):
        if historia in self.__caninos:
            return self.__caninos[historia]
        
        elif historia in self.__felinos:
            return self.__felinos[historia]
        
        return None
   

    def verFechaIngreso(self,historia):
        mascota = self.buscarMascota(historia)
        if mascota:
            return mascota.verFecha()
        return None

    def verMedicamento(self,historia):
        mascota = self.buscarMascota(historia)
        if mascota:
            return mascota.verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False

def main():
    servicio_hospitalario = sistemaV()
    
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nIngrese la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            
            if not servicio_hospitalario.verificarExiste(historia):
                
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo = input("Ingrese el tipo de mascota (felino o canino): ")
                if tipo != "canino" and tipo != "felino":
                    print("Tipo inválido. Solo se permiten 'canino' o 'felino'.")
                    continue

                peso=int(input("Ingrese el peso de la mascota: "))
                while True:
                    fecha = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                    try:
                        datetime.strptime(fecha, '%d/%m/%Y')
                        break
                    except ValueError:
                        print("Fecha inválida. Ingrese nuevamente.")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                
                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                
                lista_med=[]
                mas.asignarLista_Medicamentos(lista_med)
                for i in range(nm):
                    while True:
                        nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                        if mas.existeMedicamento(nombre_medicamento):
                            print("Ese medicamento ya fue registrado. Intente con otro.")
                        else:
                            break
                    dosis = int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Gracias por usar el sistema")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

