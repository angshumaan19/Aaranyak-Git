from abc import ABC,abstractmethod
class AbsClass(ABC):
    def print(self,x):
        print("passed value :",x)

    @abstractmethod
    def task(self):
        print("we are inside absClass class")

class test_class(AbsClass):
        def task(self):
            print("we are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(1000)
