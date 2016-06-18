"""
key_bellman_budge.py
Key analysis: Bellman Budge
"""
import music21

from leadreader.analyses.base import BaseAnalysis


class KeyBellmanBudge(BaseAnalysis):
    """
    http://web.mit.edu/music21/doc/moduleReference/moduleAnalysisDiscrete.html
    """
    def name(self):
        return 'key_bellman_budge'

    def description(self):
        return ("Determine key using Krumhansl's algorithm and "
                "Bellman-Budge weightings")

    def analyze(self):
        """ Run the analysis. """
        # using music21 for this for now, but I can see us switching away from
        # it when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('BellmanBudge')
        self.composition.key_bellman_budge = {
            'name': key.tonic.name,
            'mode': key.mode,
            'correlationCoefficient': key.correlationCoefficient
        }
