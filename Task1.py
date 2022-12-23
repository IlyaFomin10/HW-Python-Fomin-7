"""
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение
между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.
"""

from time import sleep


class TrafficLight:
    _color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for color, switch_time in self._color.items():
            self._color = color

            print(f"Светофор горит - {self._color} "
                  f"в течении {switch_time} секунд")

            sleep(switch_time)


example = TrafficLight()
example.running()
