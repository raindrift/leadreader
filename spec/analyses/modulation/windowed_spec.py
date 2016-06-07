from expects import *
from spec.helper import *
from leadreader.analyses.modulation.windowed import *
from leadreader.composition import Composition
import music21

with context('key modulation detection'):
    with before.each:
        setup(self)
        self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')
        self.subject = ModulationWindowed(self.composition)

    with it('identifies itself'):
        expect(self.subject.name()).to(equal('modulation_windowed'))

    with it('windowing'):
        expect(self.subject.window_size).to(equal(8))

    with it('can use a custom window size'):
        small = ModulationWindowed(None, 3)
        expect(small.window_size).to(equal(3))

    with it('can return a measure window'):
        small = ModulationWindowed(self.composition, 4)

        # Slide window from beginning to end.
        expect(len(small.getWindow(0))).to(equal(2))
        expect(len(small.getWindow(1))).to(equal(3))
        expect(len(small.getWindow(2))).to(equal(4))
        expect(len(small.getWindow(3))).to(equal(4))
        expect(len(small.getWindow(4))).to(equal(4))
        expect(len(small.getWindow(5))).to(equal(4))
        expect(len(small.getWindow(6))).to(equal(4))
        expect(len(small.getWindow(7))).to(equal(3))
        expect(len(small.getWindow(8))).to(equal(2))
        expect(len(small.getWindow(9))).to(equal(1))
        expect(len(small.getWindow(10))).to(equal(0))

    with it('finds modulation'):
        self.subject.analyze()
        # expect(self.composition.metadata['title']).to(equal('Test 1 in C Major'))
