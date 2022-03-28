class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1 
        self._control = ""
        TV._numTV +=1
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca

    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control = control

    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio = precio 

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        if self._estado == True:
            if volumen > 7 or volumen <0:
                return 
            else:
                self._volumen = volumen

    def getCanal(self):
        return self._canal
    def setCanal(self, canal):
        if self._estado == True:
            if canal >120 or canal < 1:
                return
            else:
                self._canal = canal

    @classmethod 
    def getNumTV(cls):
        return cls._numTV
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    def turnOn(self):
        self._estado = True 
    def turnOff(self):
        self._estado = False
    
    def getEstado(self):
        return self._estado
    def canalUp(self):
        if self._estado == True:
            if self._canal >120 or self._canal < 1 or self._canal +1 >120:
                return
            else:
                self._canal += 1

    def canalDown(self):
        if self._estado == True:
            if self._canal >120 or self._canal < 1 or self._canal -1 < 1:
                return
            else:
                self._canal -= 1
    
    def volumenUp(self):
        if self._estado == True:
            if self._volumen > 7 or self._volumen <0 or self._volumen +1 > 7:
                return 
            else:
                self._volumen += 1
    def volumenDown(self):
        if self._estado == True:
            if self._volumen > 7 or self._volumen <0 or self._volumen -1 <0:
                return 
            else:
                self._volumen -= 1
