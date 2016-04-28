from expects import *
from spec.helper import *
from leadreader.str import camelize

with description('String Utils'):
    with description('camelize'):
        with it('converts underscore to camelcase'):
            expect(camelize('foo_bar')).to(equal('FooBar'))
