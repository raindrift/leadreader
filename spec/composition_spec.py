from expects import *
from spec.helper import *
from leadreader.composition import Composition

with description('Composition'):
    with before.each:
        setup(self)

    with context('a valid leadheet file'):
        with before.each:
            self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')

        with it('creates an entry for the leadsheet in the db'):
            record = self.db.compositions.find_one()
            expect(record).to(have_keys('filename', 'path'))
            expect(record['filename']).to(equal('test-1-in-c-major.xml'))

        with it('returns leadsheet properties as native props'):
            expect(self.composition.filename).to(equal('test-1-in-c-major.xml'))

        with context('when the requested property does not exist'):
            with it('raises an error for now'):
                expect(lambda: self.composition.missing_thing).to(raise_error(AttributeError))

            with _it('eventually runs the analysis that generates the prop'):
                pass

    with context('a missing file'):
        with it('raises an exception'):
            expect(lambda: Composition('spec/fixtures/does-not-exist.xml')).to(raise_error(IOError))
