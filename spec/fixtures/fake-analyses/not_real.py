from leadreader.analyses.base import BaseAnalysis

class NotReal(BaseAnalysis):
    def name(self):
        return 'not_real'

    def description(self):
        return 'this is not a real analysis.'

    def analyze(self):
        pass
