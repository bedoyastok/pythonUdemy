#herencias, comparte atributos y metodos entre clases
#y diferentes clases hereden otras

class Persona:
#    nombre
#    apellidos
#    altura
#    edad
    
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self,name):
        self.nombre = name
    
    def setApellidos(self,lastname):
        self.apellidos = lastname
    
    def setAltura(self,estatura):
        self.altura = estatura
    
    def setEdad(self,años):
        self.edad = años
        
    def hablar(self):
        return 'estoy hablando'
    
    def caminar(self):
        return 'estoy caminando'
    
    def dormir(self):
        return 'estoy durmiendo'
    
    #hereda la clase persona
class Informatico(Persona):
#   lenguajes
#   experiencia

    def __init__(self):
        self.lenguajes = 'html, css, javascript, php'
        self.experiencia = '5 años'
        
    def getlenguajes(self):
        return self.lenguajes
    
    def aprender(self,lengprog):
        self.lenguajes = lengprog
        return  self.lenguajes
    
    def programar(self):
        return 'estoy programando'
    
    def reparar(self):
        return 'estoy reparando el pc'
    

class TecnicoRedes(Informatico):
    
    def __init__(self):
        super().__init__()#para invocar el constructor de 
        #la clase padre informatico
        self.auditarRedes = 'experto'
        self.experienciaRedes = '15 años'
        
    def auditoria(self):
        return 'estoy auditando una red'
    
    
    
    
    
    
    
    
    
    
    
    
    
    