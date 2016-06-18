"""
metadata.py

Key analysis: just returning basic metadata
"""
from leadreader.analyses.base import BaseAnalysis


class Metadata(BaseAnalysis):
    """ determine basic metadata of a composition """
    def name(self):
        return 'metadata'

    def description(self):
        return 'Extract and store basic composition metadata'

    def analyze(self):
        dom = self.composition.xmldom()
        # the value is actually in the text node, which is the first child
        title_node = dom.getElementsByTagName('work-title')[0]
        title_text = title_node.childNodes[0].nodeValue
        self.composition.metadata = {'title': title_text}
