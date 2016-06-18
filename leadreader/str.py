"""
String utilities.
"""

def camelize(value):
    """
    Return the camel-cased version of a string.
    Used for analysis class names.
    """
    def _camelcase():
        while True:
            yield type(value).capitalize
    c = _camelcase()
    return "".join(next(c)(x) if x else '_' for x in value.split("_"))
