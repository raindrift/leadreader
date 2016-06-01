from expects import *
from spec.helper import *
from leadreader.analyses.key_bellman_budge import KeyBellmanBudge
from leadreader.composition import Composition

with context('key analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = KeyBellmanBudge(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key_bellman_budge'))

    with it('fetches the composition title'):
        self.subject.analyze()
        expect(self.composition.key['name']).to(equal('F'))
        expect(self.composition.key['mode']).to(equal('major'))
