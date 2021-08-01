#   ABC stands for Abstract Base Class
from abc import ABCMeta, abstractmethod


class Houses(metaclass=ABCMeta):
    @abstractmethod
    def big(self):
        return True

    @abstractmethod
    def smart(self):
        return True


class Myhouse(Houses):
    def big(self):
        print('Welcome to my house')

#    def smart(self):
#        pass

# If you forget to declare the smart method
# Python will throw this error:
# TypeError: "Can't instantiate abstract class Myhouse with abstract methods smart


h = Myhouse()
h.big()
