from leadreader.analyses.base import BaseAnalysis
import music21

class KeyKrumhansl(BaseAnalysis):
    def name(self):
        return 'key_krumhansl'

    def description(self):
        return "Determine key using Krumhansl's algorithm and Krumhansl-Shmuckler weighting"

    def analyze(self):
        # using music21 for this for now, but I can see us switching away from it
        # when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('KrumhanslSchmuckler')
        self.composition.key = {
            'name': key.tonic.name,
            'mode': key.mode,
            'correlationCoefficient': key.correlationCoefficient
        }
