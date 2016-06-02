def camelize(value):
    def camelcase():
        while True:
            yield type(value).capitalize

    c = camelcase()
    return "".join(next(c)(x) if x else '_' for x in value.split("_"))
