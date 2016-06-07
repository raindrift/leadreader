# windowed.py
#
# Predict modulation points by using sliding windows.

from leadreader.analyses.base import BaseAnalysis
from leadreader.analyses.key_krumhansl import KeyKrumhansl
import music21
import math

# determine key of a composition
class ModulationWindowed(BaseAnalysis):

    # Using default window size of 8.
    def __init__(self, composition, window_size=8):
        super(ModulationWindowed, self).__init__(composition)
        self.window_size = window_size
        if composition:
            self.score = music21.converter.parse(self.composition.path)

    def name(self):
        return 'modulation_windowed'

    def description(self):
        # http://web.mit.edu/music21/doc/moduleReference/moduleAnalysisDiscrete.html
        return "Determine key using Krumhansl's algorithm and Aarden-Essen weightings (not recommended for minor)"

    def numMeasures(self):
        return len(self.score.parts[0].getElementsByClass('Measure'))

    # Obtain a window of size |window_size| centered on a measure number.
    def getWindow(self, measure):
        start = measure - math.floor(self.window_size/2)
        end = start + self.window_size - 1
        # Assume leadsheet only has 1 part.
        measures = self.score.parts[0].measures(start, end, ignoreNumbers=True)
        measures = measures.getElementsByClass('Measure')
        return measures

    def analyze(self):
        # Use default Krumhansl.
        # TODO: Expose key detection algorithm as parameter.
        algo = KeyKrumhansl(self.composition)
        key = algo.analyze()
        self.composition.modulations = {
            # 'name': key.tonic.name,
            # 'mode': key.mode,
        }
