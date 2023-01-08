class GrandParent:

    def method(self):
        print('call from GrandParent')


class ParentOne(GrandParent):

    def method(self):
        super().method()
        print('call from ParentOne')


class ParentTwo(GrandParent):

    def method(self):
        super().method()
        print('call from ParentTwo')


class Child(ParentOne, ParentTwo):

    def method(self):
        super().method()
        print('call from Child')


obj = Child()
obj.method()
print(obj.__class__.__mro__)  # так можно посмотреть в каком порядке будут искаться методы method resolution order
