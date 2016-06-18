"""
key_manual.py
Key analysis: Manual input.
"""
import music21

from leadreader.analyses.base import BaseAnalysis


class KeyManual(BaseAnalysis):
    """ Analysis which just prompts user for manual input of key. """
    # TODO: Extend the modes.
    VALID_MODES = ['major', 'minor']
    VALID_KEYS = 'ABCDEFG'

    """
    Ask user to manually input key for a composition.
    """
    def name(self):
        return 'key_manual'

    def description(self):
        return 'Manually input key for a composition.'

    def validate_key(self, recv):
        """ Given some key a user inputted, ensure it's valid. """
        recv = recv.replace(' ', '')  # Remove all white space
        tonic = recv[0].upper()
        if self.VALID_KEYS.find(tonic) == -1:
          print('Received tonic:', tonic)
          print('Invalid. Please input valid tonic (C,D,E,F,G,A,B)')
          return '', ''
        mode = recv[1:].lower()
        if not mode in self.VALID_MODES:
          print('Received mode:', mode)
          print('Currently accepting these modes:', self.VALID_MODES)
          return '', ''
        return tonic, mode

    def input_key(self):
        """ Ask the user for input, ensure it's valid. """
        tonic = ''
        while tonic == '':
            recv = prompt_for_key()
            tonic, mode = self.validate_key(recv)
        print("Tonic: ", tonic)
        print("Mode: ", mode)
        return tonic, mode

    def analyze(self):
        # Ask for user input.
        # Could potentially expose this in a nice interface in the future.
        # Expects a key (between A-G), maybe a space, and then the mode.
        tonic, mode = self.input_key()
        self.composition.key_manual = {
            'name': tonic,
            'mode': mode,
        }


def prompt_for_key():
    """ Blocks on and returns cli input. """
    return input('Input the key (i.e. "G minor"):')

