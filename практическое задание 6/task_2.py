class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, hight):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.hight = hight

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        h = self.hight
        total = leng * wid * w * h / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {h} см = ", total, "т")


r = Road(20, 5000, 25, 5)
print(r.mass())

