class Coche:
    
    #atributos o propiedades, caracteristicas
    color = 'rojo'
    marca = 'ferrari'
    modelo = 'aventador'
    velocidad = 300
    caballos = 500
    puestos = 0
    
    def __init__(self, color, marca, modelo, velocidad, caballaje, puestos):
        self.color = color 
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.puestos = puestos
    
    #metodos
    #son acciones que hace el objeto(coche)
    #antes llamadas funciones
    def setColor(self,color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo
        
    def getModelo(self):
        return self.modelo
    
    def setMarca(self,marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def acelerar(self):
        self.velocidad += 10
        
    def frenar(self):
        self.velocidad -= 10
        
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = '--------Informacion del coche------\n'
        info += self.getColor()+'\n'
        info += self.getMarca()+'\n'
        info += self.getModelo()+'\n'
        info += str(self.getVelocidad())
        
        return info
#fin class

#crear obejetos / intanciar class
# =============================================================================
# coche = Coche()
# 
# print(coche) 
# print(coche.marca,coche.color)   
# print('velocidad',coche.velocidad)
# 
# coche.acelerar()
# coche.acelerar()
# coche.acelerar()
# coche.acelerar()
# print('velocidad actual',coche.getVelocidad())
# 
# 
# print('\n--------------------')
# print('uso de set y get\n')
# 
# coche.setModelo('renault')
# coche.setColor('azul')
# 
# print('nuevo modelo',coche.getModelo())
# print('nuevo color',coche.getColor())
# 
# 
# print('\n--------------------')
# print('nuevo objeto usando la misma clase\n')
# 
# cochesito = Coche()
# 
# print(cochesito.marca,cochesito.color,cochesito.modelo)
# 
# cochesito.setColor('morado')
# cochesito.setModelo('audi')
# 
# print(cochesito.getColor())
# print(cochesito.getModelo())
# 
# print('\n--------------------')
# print('constructor\n')
# =============================================================================


carro = Coche("morado","mazda","nitro",150,200,4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro1.getInfo())








