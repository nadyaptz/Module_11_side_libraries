import inspect


# возьмем для примера классы из предыдущих заданий
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


def introspection_info(obj):
    obj_type = type(obj)
    obj_type = str(obj_type).replace("<class '", '')
    obj_type = str(obj_type).replace("'>", '')

    all_attrs = [arg for arg in dir(obj) if not callable(getattr(obj, arg))]  #
    public_attrs = [arg for arg in dir(obj) if not arg.startswith('_') and not callable(getattr(obj, arg))]

    all_methods = [arg for arg in dir(obj) if callable(getattr(obj, arg))]
    public_methods = [arg for arg in dir(obj) if not arg.startswith('_') and callable(getattr(obj, arg))]

    module = inspect.getmodule(obj)

    result_to_print = {'type': obj_type, 'attributes': all_attrs, 'public attributes': public_attrs,
                       'methods': all_methods, 'public methods': public_methods, 'module': module}
    return result_to_print


eagle1 = Eagle()
pegasus1 = Pegasus()

print('Про строку:')
print(introspection_info('sting'))
print('Про класс:')
print(introspection_info(Eagle))
print('Про объект класса:')
print(introspection_info(pegasus1))
