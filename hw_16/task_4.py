# Ex.4
# Класс-контейнер хранит экзепмляры класса Shape.
# Реализациями Shape могут быть 'Rectange', 'Triangle', 'Circle'
# Shape должен предоставлять интерфейс square
# Предусмотреть проверки
# Контейнер должен иметь свойство square - возвращающее общую площадь всех фигур


from task_3 import Rectangle, Triangle, Circle


class ContainerShapeTypes:

    def __init__(self):
        self._inst_storage = []

    def add_inst_storage(self, shape_cls_inst):
        self._inst_storage.append(shape_cls_inst)

    @property
    def inst_storage(self):
        return self._inst_storage

    def general_square(self):
        if self._inst_storage:
            square_sum = 0
            for inst in self._inst_storage:
                cls_name = inst.__class__.__name__
                if cls_name == 'Rectangle':
                    square_sum += inst.rectangle_square()
                elif cls_name == 'Triangle':
                    square_sum += inst.triangle_square()
                elif cls_name == 'Circle':
                    square_sum += inst.circle_square()
            return square_sum


rectangles = ContainerShapeTypes()
triangles = ContainerShapeTypes()
circles = ContainerShapeTypes()

rectangle_1 = Rectangle()
triangle_1 = Triangle()
circle_1 = Circle()

rectangles.add_inst_storage(rectangle_1)
triangles.add_inst_storage(triangle_1)
circles.add_inst_storage(circle_1)


def test_add_to_storage():
    assert rectangle_1 in rectangles.inst_storage
    assert triangle_1 in triangles.inst_storage
    assert circle_1 in circles.inst_storage


def test_correct_general_square_val():
    square_sum_result = rectangle_1.rectangle_square() + triangle_1.triangle_square() + circle_1.circle_square()
    cls_square_result = rectangles.general_square() + triangles.general_square() + circles.general_square()
    assert square_sum_result == cls_square_result
