"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

#import math
from pympler import asizeof


def show_sizeof(obj):
    print("Объект: {0}, Тип: {1}, Размер: {2}".format(obj, obj.__class__, asizeof.asizeof(obj)))






class Triangle:
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.point_1 = {'x': x_1, 'y': y_1}
        self.point_2 = {'x': x_2, 'y': y_2}
        self.point_3 = {'x': x_3, 'y': y_3}
'''
    def get_side_1_2_length(self):
        return math.sqrt(abs((self.point_2['x']-self.point_1['x'])**2 + (self.point_2['y']-self.point_1['y'])**2))

    def get_side_2_3_length(self):
        return math.sqrt(abs((self.point_3['x']-self.point_2['x'])**2 + (self.point_3['y']-self.point_2['y'])**2))

    def get_side_1_3_length(self):
        return math.sqrt(abs((self.point_3['x']-self.point_1['x'])**2 + (self.point_3['y']-self.point_1['y'])**2))

    def get_square(self):
        return abs((self.point_1['x']-self.point_3['x']) * (self.point_2['y']-self.point_3['y']) -
                          (self.point_2['x']-self.point_3['x']) * (self.point_1['y']-self.point_3['y']) /2)

    def get_altitude_1(self):
        return self.get_square() * 2 / self.get_side_2_3_length()

    def get_altitude_2(self):
        return self.get_square() * 2 / self.get_side_1_3_length()

    def get_altitude_3(self):
        return self.get_square() * 2 / self.get_side_1_2_length()

    def get_perim(self):
        return self.get_side_1_2_length() + self.get_side_2_3_length() + self.get_side_1_3_length()

'''

triangle_1 = Triangle(3, 5, 8, 2, 1, 1)

triangle_2 = Triangle(4, 6, 6, 2, 2, 2)
'''
print("Периметр первого треугольника равен {} см".format(triangle_1.get_perim()))

print("Площадь первого треугольника равна {} см кв".format(triangle_1.get_square()))

print("Длины высот первого треугольника от угла 1: {} см, от угла 2: {} см, от угла 3: "
      "{} см" .format(triangle_1.get_altitude_1(), triangle_1.get_altitude_2(), triangle_1.get_altitude_3()))



print("Периметр второго треугольника равен {} см".format(triangle_2.get_perim()))

print("Площадь второго треугольника равна {} см кв".format(triangle_2.get_square()))

print("Длины высот второго треугольника от угла 1: {} см, от угла 2: {} см, от угла 3: "
      "{} см" .format(triangle_2.get_altitude_1(), triangle_2.get_altitude_2(), triangle_2.get_altitude_3()))
'''
show_sizeof(triangle_1)
show_sizeof(triangle_2)
#Объект: <__main__.Triangle object at 0x000002A7D4EB3390>, Тип: <class '__main__.Triangle'>, Размер: 1328
#Объект: <__main__.Triangle object at 0x000002A7D4EB3438>, Тип: <class '__main__.Triangle'>, Размер: 1264
class Triangle_slots(object):
    __slots__ = ['point_1', 'point_2', 'point_3']



triangle_slots_1 = Triangle_slots()

triangle_slots_1.point_1 = {'x': 3, 'y': 5}
triangle_slots_1.point_2 = {'x': 8, 'y': 2}
triangle_slots_1.point_3 = {'x': 1, 'y': 1}


triangle_slots_2 = Triangle_slots()

triangle_slots_2.point_1 = {'x': 4, 'y': 6}
triangle_slots_2.point_2 = {'x': 6, 'y': 2}
triangle_slots_2.point_3 = {'x': 2, 'y': 2}



show_sizeof(triangle_slots_1)
show_sizeof(triangle_slots_2)
#Объект: <__main__.Triangle_slots object at 0x000002A7D4F0BAC8>, Тип: <class '__main__.Triangle_slots'>, Размер: 1056
#Объект: <__main__.Triangle_slots object at 0x000002A7D4F0BB88>, Тип: <class '__main__.Triangle_slots'>, Размер: 992

# ВЫВОД: использование слотов в классе (значениями атрибутов были словари) дало экономию памяти около 25%.
# 1328 => 1056,  1264 => 992