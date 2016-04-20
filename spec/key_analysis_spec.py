from expects import *
from leadreader.key_analysis import Key

with context(Key):
    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key'))
