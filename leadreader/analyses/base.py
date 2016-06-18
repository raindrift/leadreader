"""
base.py

Base class for all analysis.
"""
from abc import ABCMeta, abstractmethod

class BaseAnalysis(metaclass=ABCMeta):
    """ Base class for all analysis to run on a composition."""

    def __init__(self, composition):
        self.composition = composition

    @abstractmethod
    def name(self):
        """ Return the analysis name as a string. """
        pass

    @abstractmethod
    def description(self):
        """ Return string describing the analysis. """
        pass

    @abstractmethod
    def analyze(self):
        """ Run the analysis defined by the subclass. """
        pass
