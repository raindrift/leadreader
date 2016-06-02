from expects import *
from spec.helper import *
from leadreader.analyses.key_aarden_essen import KeyAardenEssen
from leadreader.composition import Composition

with context('key analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = KeyAardenEssen(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key_aarden_essen'))

    with it('fetches the composition title'):
        self.subject.analyze()
        expect(self.composition.key_aarden_essen['name']).to(equal('F'))
        expect(self.composition.key_aarden_essen['mode']).to(equal('major'))
