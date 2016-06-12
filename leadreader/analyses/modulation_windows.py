# windowed.py
# Predict modulation points by using sliding windows.

from leadreader.analyses.base import BaseAnalysis
import music21
import math

# Determine which measures likely have a key modulation.
class ModulationWindowed(BaseAnalysis):

    # Using default window size of 8.
    def __init__(self, composition, window_size=8):
        super(ModulationWindowed, self).__init__(composition)
        self.window_size = window_size
        if composition:
            self.score = music21.converter.parse(self.composition.path)

    def name(self):
        return 'modulation_windows'

    def description(self):
        return 'Determine key modulations using sliding measure windows'

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
        modulations = []
        print('Analyzing key modulations with window size', self.window_size)
        # Run through each measure window, apply default Krumhansl.
        # TODO: Expose key detection algorithm as parameter.
        i = 0
        end = self.numMeasures()
        tonic = mode = None
        while i <= end:
            window = self.getWindow(i)
            key = window.analyze('KrumhanslSchmuckler')
            # Notice when the tonic or mode changes.
            if (not tonic == None and not tonic == key.tonic.name) or \
                (not mode == None and not mode == key.mode):
                modulations.append(i)
            tonic = key.tonic.name
            mode = key.mode
            # TODO: Logging verbosity levels.
            print('measure', i, '-', tonic, mode)
            i += 1
        self.composition.modulations = modulations
        print('measures of suspected key modulation:', modulations)
