from expects import *
from spec.helper import *
from leadreader.base_analysis import BaseAnalysis

# you can't instantiate BaseAnalysis directly
# this class has stubs to implement all the abstract methods
# so that it's possible to get an instance
class MockAnalysis:
    def name(self):
        return 'mock'

with context(MockAnalysis):
    with before.each:
        setup(self)

    with description('abstract methods'):
        with it('has a name'):
            expect(self.subject.name()).to(equal('mock'))


