from abc import ABCMeta, abstractmethod

class BaseAnalysis():
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        pass
