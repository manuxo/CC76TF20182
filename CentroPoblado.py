class CentroPoblado:
    def __init__(self,codigo,nombre,departamento,provincia,distrito,coordX, coordY):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.coordX = coordX
        self.coordY = coordY
    def __str__(self):
        return "%s D: %s P: %s D: %s Cod: %s  X: %f Y: %f" % (self.nombre, self.departamento, self.provincia, self.distrito, self.codigo,self.coordX,self.coordY)
        