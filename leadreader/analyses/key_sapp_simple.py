"""
key_sapp_simple.py
Key analysis: Sapp
"""
import music21

from leadreader.analyses.base import BaseAnalysis

class KeySappSimple(BaseAnalysis):
    """
    http://web.mit.edu/music21/doc/moduleReference/moduleAnalysisDiscrete.html
    """
    def name(self):
        return 'key_sapp_simple'

    def description(self):
        return ("Determine key using Krumhansl's algorithm and "
                "Craig Sapp's simple weights")

    def analyze(self):
        """ Run the analysis. """
        # using music21 for this for now, but I can see us switching away from
        # it when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('SimpleWeights')
        self.composition.key_sapp_simple = {
            'name': key.tonic.name,
            'mode': key.mode,
            'correlationCoefficient': key.correlationCoefficient
        }
