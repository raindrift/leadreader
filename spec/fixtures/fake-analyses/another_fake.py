from leadreader.analyses.base import BaseAnalysis

class AnotherFake(BaseAnalysis):
    def name(self):
        return 'another_fake'

    def description(self):
        return 'this is yet another fake analysis.'

    def analyze(self):
        pass
