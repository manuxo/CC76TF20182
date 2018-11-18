class CentroPoblado:
    def __init__(self,codigo,nombre,departamento,provincia,distrito,capital,coordX, coordY):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.capital = capital
        self.coordX = coordX
        self.coordY = coordY
    def __str__(self):
        return "%s D: %s P: %s D: %s Cap: %d Cod: %s  X: %f Y: %f" % (self.nombre, self.departamento, self.provincia, self.distrito, self.capital, self.codigo,self.coordX,self.coordY)
        