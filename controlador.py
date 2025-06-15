from basededatos import conexionsql, usuario, personal_unet

class Controlador:
    def __init__(self):
        self.conexion = conexionsql(host="localhost", user="root", password="", database="infancia_unet", port=3306)
        self.conexion.conectar()
        self.usuario = usuario(self.conexion)
        self.personal = personal_unet(self.conexion)
    
    def verificacion(self, usser, password):
        resultado = self.usuario.verificar_user(usser, password)
        return resultado

    def mostrar_personal(self, op, vari, id2):
        resultado = self.personal.mostrar_per(op, vari, id2)

        resultado_texto = ""
        for dato in resultado:
            resultado_texto += str(dato) + "\n"

        return resultado_texto
    
    def registrar_personal(self, id, ced, nom, ap, grup, tel):
        result = self.personal.registrar_per(id, ced, nom, ap, grup, tel)
        return result 
        self.conexion.cerrar()  
    
    """def modificar_personal(self, id, sus):
        result = self.personal.modificar_per(id, sus)
        return result

    def eliminar_personal(self, id):
        result = self.personal.eliminar_per(id)
        return result
    
    def pasiva_personal(self, id):
        result = self.personal.pasiva_per(id)
        return result 
    
    def activacion_personal(self, id):
        result = self.basededatos.activacion_per(id)
        return result"""

