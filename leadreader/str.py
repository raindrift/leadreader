def camelize(value):
    def camelcase():
        while True:
            yield type(value).capitalize

    c = camelcase()
    return "".join(c.next()(x) if x else '_' for x in value.split("_"))
