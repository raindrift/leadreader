from leadreader.analyses.base import BaseAnalysis
import music21

class KeyTemperleyKostkaPayne(BaseAnalysis):
    def name(self):
        return 'key_temperley_kostka_payne'

    def description(self):
        # http://web.mit.edu/music21/doc/moduleReference/moduleAnalysisDiscrete.html
        return "Determine key using Krumhansl's algorithm and Temperley-Kostka-Payne weightings"

    def analyze(self):
        # using music21 for this for now, but I can see us switching away from it
        # when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('TemperleyKostkaPayne')
        self.composition.key = {
            'name': key.tonic.name,
            'mode': key.mode
        }
