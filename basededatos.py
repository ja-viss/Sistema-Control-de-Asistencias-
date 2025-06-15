import mysql.connector
from datetime import datetime
import subprocess
#import pdfkit
from reportlab.pdfgen import canvas 
hora = datetime.now().time()
op = 0
id2 = 0
ope = 0

class conexionsql:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conexion = None
        
    def conectar(self):
        self.conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "infancia_unet",
            port = 3306,)
        
    def cerrar(self):
        if self.conexion is not None:
            self.conexion.close()
            
    def ejecutar_consulta(self, consulta, parametros=None):
        cursor = self.conexion.cursor()
        if consulta and consulta.lower().startswith("select"):
            cursor.execute(consulta,parametros)
            resultado = cursor.fetchall()
            
        elif consulta:
            cursor.execute(consulta, parametros)
            resultado = None
            self.conexion.commit()
            
        else:
            resultado = None
        cursor.close()
        return resultado
    
    def commit(self):
        self.conexion.commit()

class usuario():
    def __init__(self, conexion):
        self.conexion = conexion 

    def verificar_user(self, usser, password):
        consulta = """SELECT nom_usser, pass_usser FROM usuarios WHERE nom_usser = %s AND pass_usser = %s"""
        parametros = (usser, password)
        resultado = self.conexion.ejecutar_consulta(consulta, parametros)
        if resultado:
            vari = 1
            return vari
        else:
            vari = 0
            return vari  
               
               
class personal_unet():
    def __init__(self, conexion):
        self.conexion = conexion

    def mostrar_per(self, op, vari=None, id2=None):
        if op == 1:
            if vari == 1:
                personal = "admi_unet"
            elif vari == 2:
                personal = "doce_unet"
            elif vari == 3:
                personal = "obre_unet"
            elif vari == 4:
                personal = "direc_unet"

            if personal == "direc_unet":
                atributo = "estatus_direc"
            elif personal == "obre_unet":
                atributo = "estatus_obre"
            elif personal == "doce_unet":
                atributo = "estatus_docente"
            elif personal == "admi_unet":
                atributo = "estatus_admi"

            consulta = f"SELECT * FROM {personal} WHERE {atributo} = 'ACTIVO'"

        elif op == 2:
            var = id[-1].upper()
            if var == "A":
                personal = "admi_unet"
            elif var == "P":
                personal = "doce_unet"
            elif var == "O":
                personal = "obre_unet"
            elif var == "D":
                personal = "direc_unet"

            if personal == "direc_unet":
                atributo = "id_direc"
            elif personal == "obre_unet":
                atributo = "id_obre"
            elif personal == "doce_unet":
                atributo = "id_docente"
            elif personal == "admi_unet":
                atributo = "id_admi"

            consulta = f"SELECT * FROM {personal} WHERE {atributo} = '{id}'"

        resultado = self.conexion.ejecutar_consulta(consulta)
        return resultado

    def registrar_per(self, id, ced, nom, ap, grup, tel):     
        var = id[-1].upper()
        if var == "A":
            personal = "admi_unet"
        elif var == "P":
            personal = "doce_unet"
        elif var == "O":
            personal = "obre_unet"     
        elif var == "D":
            personal = "direc_unet"

        if var == "A":
            tipo = "Administrativo"
        elif var == "P":
            tipo = "Docente"
        elif var == "O":
            tipo = "Obrero"     
        elif var == "D":
            tipo = "Directivo"

        if personal == "direc_unet":
            atributo = " ,".join(("id_direc", "ced_direc", "nom_direc", "ape_direc", "estatus_direc", "tel_direc"))
        elif personal == "obre_unet":
            atributo = " ,".join(("id_obre", "ced_obre", "nom_obre", "ape_obre", "estatus_obre", "tel_obre"))   
        elif personal == "admi_unet":
            atributo = " ,".join(("id_admi", "ced_admi", "nom_admi", "ape_admi", "estatus_admi", "tel_admi"))
        elif personal == "doce_unet":
            atributo = " ,".join(("id_docente", "ced_docente", "nom_docente", "ape_docente", "grup_docente", "estatus_docente", "telefono"))

        esta = "Activo"

        if personal == "doce_unet":
            consulta = """INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s)""".format(personal, atributo) 
            parametros = (id, ced, nom, ap, grup, esta, tel)
            self.conexion.ejecutar_consulta(consulta, parametros)
        else:
            consulta = """INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s)""".format(personal, atributo)
            parametros = (id, ced, nom, ap, esta, tel)
            self.conexion.ejecutar_consulta(consulta, parametros)

        print("Consulta SQL:", consulta)
        print("Parámetros:", parametros)

        consulta = """ INSERT INTO personal (id_personal, tipo_personal) VALUES (%s, %s)"""
        parametros = (id, tipo)
        self.conexion.ejecutar_consulta(consulta, parametros) 
        return "Registro Exitoso"
    
    def eliminar_per(self):
        id = input("Ingrese el ID del personal a eliminar: ")
        var = id[-1].upper()
        if var == "A":
            personal = "admi_unet"
        elif var == "P":
            personal = "doce_unet"
        elif var == "O":
            personal = "obre_unet"     
        elif var == "D":
            personal = "direc_unet"
      
        if personal == "doce_unet":
            tipo = "id_docente"
        elif personal == "admi_unet":
            tipo = "id_admi"
        elif personal == "obre_unet":
            tipo = "id_obre"
        elif personal == "direc_unet":
            tipo = "id_direct"  
        
        print("¿Esta seguro en Eliminar al personal con el identificador",id,"?: ")
        print("     1. Si")
        print("     2. No")
        deci = int(input("Elija su Opcion: "))
        
        if deci == 1:
            consulta = """DELETE FROM {} WHERE {} = %s""".format(personal, tipo)
            parametros = (id, )
            self.conexion.ejecutar_consulta(consulta, parametros)
            self.conexion.commit()
            print("Eliminacion ejecutada correctamente, el personal con el ID: ",id," ha sido eliminado")
        
        if deci == 2:
            print("Retrocediendo...")

        self.conexion.cerrar()   
            
    def pasiva_per(self):
        
        id = input("Ingrese el ID del personal a eliminar: ")
        var = id[-1].upper()
        if var == "A":
            personal = "admi_unet"
        elif var == "P":
            personal = "doce_unet"
        elif var == "O":
            personal = "obre_unet"     
        elif var == "D":
            personal = "direc_unet"
      
        if personal == "doce_unet":
            tipo = "id_docente"
        elif personal == "admi_unet":
            tipo = "id_admi"
        elif personal == "obre_unet":
            tipo = "id_obre"
        elif personal == "direc_unet":
            tipo = "id_direct"  
            
             
        if personal == "doce_unet":
            esta = "estatus_docente"
        elif personal == "admi_unet":
             esta = "estatus_admi"
        elif personal == "obre_unet":
             esta = "estatus_obre"
        elif personal == "direc_unet":
             esta = "estatus_direc"
            
        consulta = """ UPDATE {} SET {} = "Inactivo" WHERE {} = %s""".format(personal, esta, tipo)
        parametros = (id, )
        self.conexion.ejecutar_consulta(consulta, parametros)
        self.conexion.commit()
        print("Eliminacion Paiva ejecutada correctamente, el personal con el ID: ",id," ha sido eliminado")
    
        consulta = """SELECT * FROM {} WHERE {} = "ACTIVO" """.format(personal, esta)
        resultado = self.conexion.ejecutar_consulta(consulta)
        for dato in resultado:
            print(dato)
        self.conexion.cerrar()   
            
    def activacion_per(self):
        id = input("Ingrese el ID del personal a ACtivar")
        var = id[-1].upper()
        if var == "A":
            personal = "admi_unet"
        elif var == "P":
            personal = "doce_unet"
        elif var == "O":
            personal = "obre_unet"     
        elif var == "D":
            personal = "direc_unet"
      
        if personal == "doce_unet":
            tipo = "id_docente"
        elif personal == "admi_unet":
            tipo = "id_admi"
        elif personal == "obre_unet":
            tipo = "id_obre"
        elif personal == "direc_unet":
            tipo = "id_direct"  
            
             
        if personal == "doce_unet":
            esta = "estatus_docente"
        elif personal == "admi_unet":
             esta = "estatus_admi"
        elif personal == "obre_unet":
             esta = "estatus_obre"
        elif personal == "direc_unet":
             esta = "estatus_direc"
            
        consulta = """ UPDATE {} SET {} = "ACTIVO" WHERE {} = %s""".format(personal, esta, tipo)
        parametros = (id, )
        self.conexion.ejecutar_consulta(consulta, parametros)
        self.conexion.commit()
        print("Activacion ejecutada correctamente, el personal con el ID: ",id," ha sido activado")
    
        consulta = """SELECT * FROM {} WHERE {} = "ACTIVO" """.format(personal, esta)
        resultado = self.conexion.ejecutar_consulta(consulta)
        for dato in resultado:
            print(dato)
        self.conexion.cerrar()   
            
        
        
class asistencias:
    def __init__(self, conexion):
        self.conexion = conexion
        
    def registro_asistencia(self):
        op = 0
        print("    Registro de asistencias\n")
        print("    1. Registrar Hora de Entrada")
        print("    2. Registrar Hora de salida")
        op = int(input("    Escoja su opcion[1..2]: "))
        if op == 1:
            id_asis = input("Ingrese el ID que le desea asignar a la Asistencia: ")
            id_re  = input("Ingrese el ID del personal a registrar las asistencias: ")
            fecha= datetime.now().date()
            hora_entrada = datetime.now().time().strftime("%H:%M:%S")
            consulta = """INSERT INTO asistencia_unet (id_asistencia, id_personal, fecha_asis, hora_entrada) VALUES (%s, %s, %s, %s)"""
            parametros = (id_asis, id_re, fecha, hora_entrada)
            self.conexion.ejecutar_consulta(consulta, parametros)
            
        if op == 2:
            fecha= datetime.now().date()
            id_re  = input("Ingrese el ID del personal a registrar las asistencias: ")
            hora_salida = datetime.now().time().strftime("%H:%M:%S")
            consulta = """ UPDATE asistencia_unet SET hora_salida = %s WHERE id_personal = %s AND fecha_asis = %s"""
            parametros = (hora_salida, id_re, fecha)
            self.conexion.ejecutar_consulta(consulta, parametros)
            self.conexion.commit()
            
        print("Registro de asistencia completado exitosamente..")
        self.conexion.cerrar()   
        
        
    from datetime import datetime, date, time
    def mostrar_asistencias(self):
        consulta = """SELECT * FROM asistencia_unet"""
        resultado = self.conexion.ejecutar_consulta(consulta)
        for registro in resultado:
            id_asistencia = registro[0]
            id_personal = registro[1]
            fecha = registro[2]#.strftime("%d-%m-%y")
            hora_entrada = registro[3]
            hora_salida =  registro[4]
            print(id_asistencia, id_personal, fecha, hora_entrada, hora_salida)
        self.conexion.cerrar()   
    
    def eliminar_asistencias(self):
        id = input("Ingrese el ID la asistencia: ")
        consulta = """DELETE FROM asistencia_unet WHERE id_asistencia = %s""".format(id)
        parametros = (id, )
        self.conexion.ejecutar_consulta(consulta, parametros)
        self.conexion.commit()
        print("Eliminacion ejecutada correctamente, el personal con el ID: ",id," ha sido eliminada su asistencia")
        self.conexion.cerrar()   
        
    def actualizar_asistencias(self):
        print("    Ingrese la opcion deseada")
        print("    1. Actualizar Fecha")
        print("    2. Actualizar Hora de entrada")
        print("    3. Actualizar Hora de salida")
        ope = int(input("    Escoja su opcion[1..3]: "))
            
        if ope < 1 or ope > 3:
            print("Opcion Invalida... Ingresa de nuevo tu eleccion..")
        
        if ope == 1:
            atributo = "fecha_asis"
        elif ope == 2:
            atributo = "hora_entrada"
        elif ope == 3:
            atributo = "hora_salida"
        
        id2= input("Ingrese el Identificador de la asistencias la cual desea Modificar: ")
        sus = input("Ingrese el Valor que deseas sustituir: ")
        consulta = """ UPDATE asistencia_unet SET {} = %s WHERE id_asistencia = %s""".format(atributo)
        parametros = (sus, id2)
        self.conexion.ejecutar_consulta(consulta, parametros)
        self.conexion.commit()
        print("Actualizacion completada Exitosamente...")
        consulta = """SELECT * FROM asistencia_unet WHERE id_asistencia = {} """.format(id2)
        resultado = self.conexion.ejecutar_consulta(consulta)
        for dato in resultado:
            print(dato)
        self.conexion.cerrar()   

class estudiante_unet():
    def __init__(self, conexion):
        self.conexion = conexion
    
    def registro_asis(self):
        print("    Registro de asistencias a Estudiantes\n")
        id_asis = input("Ingrese el ID que le desea asignar a la Asistencia: ")
        mascu = input("Ingrese la cantidad de estudiantes masculinos: ")
        feminas = input("Ingrese la cantidad de estudiantes feminas: ")
        fecha= datetime.now().date()
        consulta = """INSERT INTO asistencias_infantes (id_asis, fecha_asis, n_masculinos, n_femeninas) VALUES (%s, %s, %s, %s)"""
        parametros = (id_asis, fecha, mascu, feminas)
        self.conexion.ejecutar_consulta(consulta, parametros)
        print("Registro de asistencia completado exitosamente..")
        self.conexion.cerrar()   
        
    from datetime import datetime, date, time
    def mostrar_asis(self):
        consulta = """SELECT * FROM asistencias_infantes"""
        resultado = self.conexion.ejecutar_consulta(consulta)
        for registro in resultado:
            id_asistencia = registro[0]
            fecha = registro[1]#.strftime("%d-%m-%y")
            masculino = registro[2]
            femeninas = registro[3]
            
            print(id_asistencia, fecha, masculino, femeninas)
        self.conexion.cerrar()   

    def eliminar_asis(self):
        id = input("Ingrese el ID la asistencia: ")
        consulta = """DELETE FROM asistencias_infantes WHERE id_asis = %s""".format(id)
        parametros = (id, )
        self.conexion.ejecutar_consulta(consulta, parametros)
        self.conexion.commit()
        print("Eliminacion ejecutada correctamente, el personal con el ID: ",id," ha sido eliminada su asistencia")
        self.conexion.cerrar()   

    def actualizar_asis(self):
        print("    Ingrese la opcion deseada")
        print("    1. Actualizar Fecha")
        print("    2. Actualizar Numero de Estudiantes masculinos")
        print("    3. Actualizar Numero de estudiantes femeninos")
        ope = int(input("    Escoja su opcion[1..3]: "))
            
        if ope < 1 or ope > 3:
            print("Opcion Invalida... Ingresa de nuevo tu eleccion..")
        
        if ope == 1:
            atributo = "fecha_asis"
        elif ope == 2:
            atributo = "n_masculinos"
        elif ope == 3:
            atributo = "n_femeninas"
        
        id2= input("Ingrese el Identificador de la asistencias la cual desea Modificar: ")
        sus = input("Ingrese el Valor que deseas sustituir: ")
        consulta = """ UPDATE asistencias_infantes SET {} = %s WHERE id_asis = %s""".format(atributo)
        parametros = (sus, id2)
        self.conexion.ejecutar_consulta(consulta, parametros)
        self.conexion.commit()
        print("Actualizacion completada Exitosamente...")
        consulta = """SELECT * FROM asistencias_infantes WHERE id_asis = {} """.format(id2)
        resultado = self.conexion.ejecutar_consulta(consulta)
        for dato in resultado:
            print(dato)
        self.conexion.cerrar()   
            
class exportacion():
    def __init__(self, conexion):
        self.conexion = conexion
        

    def generacion_pdf(self):
        print("Elija la Nomina que deseas generar")
        print("     1. Generar Nomina del Personal Administrativo")
        print("     2. Generar Nomina del Personal Docente")
        print("     3. Generar Nomina del Personal Obrero")
        print("     4. Generar Nomina del Personal Directivo")
        op = int(input("Escoja su opcion : "))
        
        if op == 1:
            personal = "admi_unet"
        elif op == 2:
            personal = "doce_unet"
        elif op == 3:
            personal = "obre_unet"     
        elif op == 4:
            personal = "direc_unet"
        
        consulta = """SELECT * FROM {}""".format(personal)
        resultado = self.conexion.ejecutar_consulta(consulta)
        fecha = datetime.now().date()
        
        if personal == "admi_unet":
            nombre = "Administrativo\administrativo_{}.pdf".format(fecha)
            
        elif personal == "doce_unet":
            nombre = "Docente\docente_{}.pdf".format(fecha)
        
        elif personal == "obre_unet":
            nombre = "Obreros\obrero_{}.pdf".format(fecha)
            
        elif personal == "direc_unet":
            nombre = "Directivo\directivo_{}.pdf".format(fecha)
            
        pdf = canvas.Canvas(
          nombre)
        y = 800
        for resul in resultado:
            x = 90
            for item in resul:
                pdf.drawString(x, y, str(item))
                x += 90
            y-= 20
       
        pdf.save()
        
        #archivo = "obreros.pdf"
        
        #subprocess.call(["start", archivo])

        self.conexion.cerrar()   

    def generacion_asistencia(self):
        consulta = """SELECT * FROM asistencia_unet"""
        resultado = self.conexion.ejecutar_consulta(consulta)
        
        pdf = canvas.Canvas(
           "asistencia.pdf")
        
        y = 700
        for resul in resultado:
            x = 100
            for item in resul:
                pdf.drawString(x, y, str(item))
                x += 100
            y-= 20
       
        pdf.save()
        self.conexion.cerrar()   
        
    def generacion_asistencia_infantes(self):
        
        consulta = """SELECT * FROM asistencias_infantes"""
        resultado = self.conexion.ejecutar_consulta(consulta)
        
        pdf = canvas.Canvas(
           "asistencia_infantes.pdf")
        
        y = 700
        for resul in resultado:
            x = 100
            for item in resul:
                pdf.drawString(x, y, str(item))
                x += 100
            y-= 20
       
        pdf.save()
        self.conexion.cerrar()   
    
        

        
#print(hora)



