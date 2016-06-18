"""
key_krumhansl.py
Key analysis: Basic Krumhansl
"""
import music21

from leadreader.analyses.base import BaseAnalysis


class KeyKrumhansl(BaseAnalysis):
    """
    http://web.mit.edu/music21/doc/moduleReference/moduleAnalysisDiscrete.html
    """
    def name(self):
        return 'key_krumhansl'

    def description(self):
        return ("Determine key using Krumhansl's algorithm and "
                "Krumhansl-Shmuckler weighting")

    def analyze(self):
        """ Run the analysis. """
        # using music21 for this for now, but I can see us switching away from
        # it when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('KrumhanslSchmuckler')
        self.composition.key_krumhansl = {
            'name': key.tonic.name,
            'mode': key.mode,
            'correlationCoefficient': key.correlationCoefficient
        }
