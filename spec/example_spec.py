from expects import *

with description('example'):
  with it('is a test'):
    expect(True).to(be_true)
