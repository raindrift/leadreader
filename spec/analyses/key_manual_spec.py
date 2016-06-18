from expects import *
from spec.helper import *
from leadreader.analyses.key_manual import KeyManual
from leadreader.composition import Composition

with context('key analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = KeyManual(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('key_manual'))

    with it('validates key'):
        tonic, _ = self.subject.validate_key('not good')
        expect(tonic).to(equal(''))
        tonic, _ = self.subject.validate_key('C bad')
        expect(tonic).to(equal(''))
        tonic, mode = self.subject.validate_key('C major')
        expect(tonic).to(equal('C'))
        expect(mode).to(equal('major'))
