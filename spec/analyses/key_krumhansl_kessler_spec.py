from expects import *
from spec.helper import *
from leadreader.analyses.key_krumhansl_kessler import KeyKrumhanslKessler
from leadreader.composition import Composition

with context('key analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = KeyKrumhanslKessler(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key_krumhansl_kessler'))

    with it('fetches the composition title'):
        self.subject.analyze()
        expect(self.composition.key['name']).to(equal('C'))
        expect(self.composition.key['mode']).to(equal('major'))
