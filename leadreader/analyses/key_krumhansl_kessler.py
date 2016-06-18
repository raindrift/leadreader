"""
key_krumhansl_kessler.py
Key analysis: Krumhansl Kessler
"""
import music21

from leadreader.analyses.base import BaseAnalysis


class KeyKrumhanslKessler(BaseAnalysis):
    """
    http://web.mit.edu/music21/doc/moduleReference/moduleAnalysisDiscrete.html
    """
    def name(self):
        return 'key_krumhansl_kessler'

    def description(self):
        return ("Determine key using Krumhansl's algorithm and "
                "Krumhansl-Kessler weightings")

    def analyze(self):
        """ Run the analysis. """
        # using music21 for this for now, but I can see us switching away from
        # it when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('KrumhanslKessler')
        self.composition.key_krumhansl_kessler = {
            'name': key.tonic.name,
            'mode': key.mode,
            'correlationCoefficient': key.correlationCoefficient
        }
