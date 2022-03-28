class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1 
        self.control = ""
        TV.numTV +=1
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio 

    def getVolumen(self):
        return self.volumen
    def setVolumen(self, volumen):
        if self.estado == True:
            if self.volumen > 7 or volumen <0:
                return 
            else:
                self.volumen = volumen

    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        if self.estado == True:
            if canal >120 or canal < 1:
                return
            else:
                self.canal = canal

    @classmethod 
    def getNumTv(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    def turnOn(self):
        self.estado = True 
    def turnOff(self):
        self.estado = False
    
    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        TV.setCanal(self.canal + 1)

    def canalDown(self):
        TV.setCanal(self.canal -1)
    
    def volumenUp(self):
        TV.setVolumen(self.volumen +1)
    def volumenDown(self):
        TV.setVolumen(self.volumen -1)