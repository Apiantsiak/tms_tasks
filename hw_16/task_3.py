# Ex.3
# Реализовать мета-класс фабрику, которая
# в зависимости от атрибута shape_type = ['Rectange', 'Triangle', 'Circle']
# возвращает нужный класс с свойством square (площадь фигуры)


from typing import Dict, Any
from random import randint


def rectangle_square(self):
    square_res = self.side_a * self.side_b
    return square_res


def triangle_square(self):
    half_perimeter = (self.side_a + self.side_b + self.side_c) / 2
    square_res = (half_perimeter *
                  (half_perimeter - self.side_a) *
                  (half_perimeter - self.side_b) *
                  (half_perimeter - self.side_c)
                  ) ** 0.5
    return square_res


def circle_square(self):
    square_res = 3.14 * self.radius ** 2
    return square_res


shape_type: Dict[str, Dict[str, Any]] = {
    'Rectangle': {
        'side_a': randint(1, 5),
        'side_b': randint(1, 5),
        'square': rectangle_square,

    },
    'Triangle': {
        'side_a': randint(5, 10),
        'side_b': randint(5, 10),
        'side_c': randint(5, 10),
        'square': triangle_square,
    },
    'Circle': {
        'radius': randint(1, 5),
        'square': circle_square,
    },
}


class MetaClsFactory(type):

    def __new__(mcs, class_name, parents, attributes):
        attributes.update(attributes)
        return super().__new__(mcs, class_name, parents, attributes)


Rectangle = MetaClsFactory('Rectangle', (), shape_type['Rectangle'])
Triangle = MetaClsFactory('Triangle', (), shape_type['Triangle'])
Circle = MetaClsFactory('Circle', (), shape_type['Circle'])


def test_correct_creation_cls():
    rectangle = Rectangle()
    triangle = Triangle()
    circle = Circle()

    assert isinstance(rectangle, Rectangle)
    assert isinstance(triangle, Triangle)
    assert isinstance(circle, Circle)
    assert 'square' in Rectangle.__dict__
    assert 'square' in Triangle.__dict__
    assert 'square' in Circle.__dict__
