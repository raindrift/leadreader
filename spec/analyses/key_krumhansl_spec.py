from expects import *
from spec.helper import *
from leadreader.analyses.key_krumhansl import KeyKrumhansl
from leadreader.composition import Composition

with context('key analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = KeyKrumhansl(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key_krumhansl'))

    with it('fetches the composition title'):
        self.subject.analyze()
        expect(self.composition.key_krumhansl['name']).to(equal('C'))
        expect(self.composition.key_krumhansl['mode']).to(equal('major'))
