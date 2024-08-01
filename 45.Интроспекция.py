import inspect


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj)]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else '__main__'
    return info


number_info = introspection_info(42)
print(number_info)

