from expects import *
from spec.helper import *
from leadreader.analyses.base import BaseAnalysis

# you can't instantiate BaseAnalysis directly
# this class has stubs to implement all the abstract methods
# so that it's possible to get an instance
class MockAnalysis(BaseAnalysis):
    def name(self):
        return 'mock'

    def description(self):
        return 'mock description'

    def analyze(self):
        return 'mock analysis'

with context('base analysis'):
    with before.each:
        setup(self)
        composition = None
        self.subject = MockAnalysis(composition)

    with description('abstract methods'):
        with it('has a name'):
            expect(self.subject.name()).to(equal('mock'))

