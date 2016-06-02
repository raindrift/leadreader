from expects import *
from spec.helper import *
from leadreader.analyses.key_temperley_kostka_payne import KeyTemperleyKostkaPayne
from leadreader.composition import Composition

with context('key analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = KeyTemperleyKostkaPayne(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key_temperley_kostka_payne'))

    with it('fetches the composition title'):
        self.subject.analyze()
        expect(self.composition.key_temperley_kostka_payne['name']).to(equal('C'))
        expect(self.composition.key_temperley_kostka_payne['mode']).to(equal('major'))
        expect(self.composition.key_temperley_kostka_payne['correlationCoefficient']).to(equal(0.7249239208029984))
