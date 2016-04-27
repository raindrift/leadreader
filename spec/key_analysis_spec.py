from expects import *
from spec.helper import *
from leadreader.key_analysis import Key

with context(Key):
    with before.each:
        setup(self)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key'))
