from expects import *
from leadreader.base_analysis import BaseAnalysis

# you can't instantiate BaseAnalysis directly
# this class has stubs to implement all the abstract methods
# so that it's possible to get an instance
class MockAnalysis:
    def name(self):
        return 'mock'

with context(MockAnalysis):
    with description('example'):
        with it('is a test'):
            expect(self.subject.name()).to(equal('mock'))


