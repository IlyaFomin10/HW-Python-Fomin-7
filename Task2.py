"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
width (ширина). Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы
асфальта, необходимого для покрытия всего дорожного полотна. Использовать
формулу: длина, ширина, масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = None
    _width = None

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print('Строим дорогу!')

    def mass_calculation(self, weigth, tickness):
        self.weigth = weigth
        self.tickness = tickness
        need = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'Нам нужно {need} т асфальта!')


road_to_village = Road(20, 5000)
road_to_village.mass_calculation(25, 5)
