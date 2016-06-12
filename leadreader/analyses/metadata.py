from leadreader.analyses.base import BaseAnalysis

# determine basic metadata of a composition
class Metadata(BaseAnalysis):
    def name(self):
        return 'metadata'

    def description(self):
        return 'Extract and store basic composition metadata'

    def analyze(self):
        dom = self.composition.xmldom()
        # the value is actually in the text node, which is the first child
        title = dom.getElementsByTagName('work-title')[0].childNodes[0].nodeValue
        self.composition.metadata = {'title': title}
