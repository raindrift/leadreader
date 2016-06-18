"""
windowed.py

Predict modulation points by using sliding windows.
"""
import math
import music21

from leadreader.analyses.base import BaseAnalysis


class ModulationWindowed(BaseAnalysis):
    """ Determine which measures likely have a key modulation. """

    def __init__(self, composition, window_size=8):
        """ Using default window size of 8. """
        super(ModulationWindowed, self).__init__(composition)
        self.window_size = window_size
        if composition:
            self.score = music21.converter.parse(self.composition.path)

    def name(self):
        return 'modulation_windows'

    def description(self):
        return 'Determine key modulations using sliding measure windows'

    def num_measures(self):
        """ Return integer of total number of measures in the composition. """
        return len(self.score.parts[0].getElementsByClass('Measure'))

    def get_window(self, measure):
        """
        Given measure number |measure|, obtain a window of size |window_size|
        centered on |measure|.
        """
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
        end = self.num_measures()
        tonic = mode = None
        while i <= end:
            window = self.get_window(i)
            key = window.analyze('KrumhanslSchmuckler')
            # Notice when the tonic or mode changes.
            if (not tonic is None and not tonic == key.tonic.name) or \
                (not mode is None and not mode == key.mode):
                modulations.append(i)
            tonic = key.tonic.name
            mode = key.mode
            # TODO: Logging verbosity levels.
            print('measure', i, '-', tonic, mode)
            i += 1
        self.composition.modulations = modulations
        print('measures of suspected key modulation:', modulations)
