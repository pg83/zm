import functools


def iter_uniq_list(lst):
    v = set()

    for l in lst:
        if l not in v:
            v.add(l)

            yield l


def uniq_list(lst):
    return list(iter_uniq_list(lst))


def singleton(f):
    @functools.wraps(f)
    def wrapper():
        while True:
            try:
                return f.__cache__
            except AttributeError:
                f.__cache__ = f()

    return wrapper


def cached_method(m):
    key = '__cache_' + m.__name__ + '__'

    @functools.wraps(m)
    def wrapper(self):
        while True:
            try:
                return self.__dict__[key]
            except KeyError:
                self.__dict__[key] = m(self)

    return wrapper
