from leadreader.analyses.base import BaseAnalysis
import music21

class KeyKrumhansl(BaseAnalysis):
    def name(self):
        return 'key'

    def description(self):
        return "Determine overall key using Carol Krumhansl's algorithm"

    def analyze(self):
        # using music21 for this for now, but I can see us switching away from it
        # when we want to do things it won't let us do
        score = music21.converter.parse(self.composition.path)
        key = score.analyze('Krumhansl')
        self.composition.key = {
            'name': key.tonic.name,
            'mode': key.mode
        }
