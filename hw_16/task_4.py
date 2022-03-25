# Ex.4
# Класс-контейнер хранит экзепмляры класса Shape.
# Реализациями Shape могут быть 'Rectange', 'Triangle', 'Circle'
# Shape должен предоставлять интерфейс square
# Предусмотреть проверки
# Контейнер должен иметь свойство square - возвращающее общую площадь всех фигур


from task_3 import Rectangle, Triangle, Circle


class ContainerShapeTypes:

    _possible_shape_type = ['Rectangle', 'Triangle', 'Circle']
    _inst_storage = []

    def __init__(self, containerized_cls):
        if containerized_cls.__name__ not in self._possible_shape_type:
            raise ValueError('Wrong class type')

        self.inst = containerized_cls()
        self._add_inst_storage(self.inst)

    @classmethod
    def _add_inst_storage(cls, cls_inst):
        cls._inst_storage.append(cls_inst)

    @classmethod
    def get_storage(cls):
        return cls._inst_storage

    @classmethod
    def general_square(cls):
        if cls._inst_storage:
            square_sum = 0
            for inst in cls._inst_storage:
                cls_name = inst.__class__.__name__
                if cls_name == 'Rectangle':
                    square_sum += inst.rectangle_square()
                elif cls_name == 'Triangle':
                    square_sum += inst.triangle_square()
                elif cls_name == 'Circle':
                    square_sum += inst.circle_square()
            return square_sum


rectangle_1 = ContainerShapeTypes(Rectangle)
triangle_1 = ContainerShapeTypes(Triangle)
circle_1 = ContainerShapeTypes(Circle)


def test_add_to_storage():
    assert rectangle_1.inst and triangle_1.inst and circle_1.inst in ContainerShapeTypes.get_storage()


def test_correct_general_square_val():
    a, b, c, = rectangle_1.inst.rectangle_square(), triangle_1.inst.triangle_square(), circle_1.inst.circle_square()
    square_sum_result = a + b + c
    assert square_sum_result == ContainerShapeTypes.general_square()
