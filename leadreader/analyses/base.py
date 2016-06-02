from abc import ABCMeta, abstractmethod

class BaseAnalysis(metaclass=ABCMeta):
    def __init__(self, composition):
        self.composition = composition

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def analyze(self):
        pass
