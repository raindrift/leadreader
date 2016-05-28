from expects import *
from spec.helper import *
from leadreader.composition import Composition

with description('Composition'):
    with before.each:
        setup(self)

    with context('a valid leadsheet file'):
        with before.each:
            self.composition = Composition('spec/fixtures/test-1-in-c-major.xml')

        with it('creates an entry for the leadsheet in the db'):
            record = self.db.compositions.find_one()
            expect(record).to(have_keys('filename', 'path'))
            expect(record['filename']).to(equal('test-1-in-c-major.xml'))

        with description('setting and getting attributes'):
            with it('returns leadsheet properties as native props'):
                expect(self.composition.filename).to(equal('test-1-in-c-major.xml'))

            with context('when the requested property does not exist'):
                with it('raises an error for now'):
                    expect(lambda: self.composition.missing_thing).to(raise_error(AttributeError))

            with it('setting leadsheet properties'):
                self.composition.foo = 'bar'
                record = self.db.compositions.find_one({'foo': 'bar'})
                expect(record['foo']).to(equal('bar'))
                expect(self.composition.foo).to(equal('bar'))

        with description('running an analysis'):
            with it('runs the named analysis on the sheet'):
                self.composition.analyze('metadata')
                expect(self.composition.metadata['title']).to(equal('Test 1 in C Major'))

            with _it('runs the analysis that generates the prop directly from the getter'):
                expect(self.composition.metadata['title']).to(equal('Test 1 in C Major'))

            with it('throws an error when the analysis does not exist'):
                expect(lambda: self.composition.analyze('missing-thing')).to(raise_error(AttributeError))

        with description('xmldom'):
            with it('returns a parsed xml representation of the leadsheet'):
                dom = self.composition.xmldom()
                notes = dom.getElementsByTagName("note")
                expect(len(notes)).to(equal(46))

    with context('a missing file'):
        with it('raises an exception'):
            expect(lambda: Composition('spec/fixtures/does-not-exist.xml')).to(raise_error(IOError))
