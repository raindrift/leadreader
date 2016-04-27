from expects import *
from spec.helper import *
from leadreader.analyses.key import Key

with context('key analysis'):
    with before.each:
        setup(self)
        self.subject = Key('foo')

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key'))
