from expects import *
from spec.helper import *
from leadreader.analyses.metadata import Metadata
from leadreader.composition import Composition

with context('metadata analysis'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = Metadata(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('metadata'))

    with it('fetches the composition title'):
        self.subject.analyze()
        expect(self.composition.metadata['title']).to(equal('Test 1 in C Major'))
