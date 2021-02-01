from _codecs import utf_8_decode

cdef extern from "wrapper.h":
    cdef int resource_count();
    cdef const char* resource_key_data(int n);
    cdef int resource_key_size(int n);
    cdef const char* resource_value_data(int n);
    cdef int resource_value_size(int n);


def from_utf8(x):
    return utf_8_decode(x)[0]


def count():
    return resource_count()


def key(n):
    return from_utf8(resource_key_data(n)[:resource_key_size(n)])


def value(n):
    return resource_value_data(n)[:resource_value_size(n)]


m = {}


for i in range(0, count()):
    m[key(i)] = i


def value_by_key(key):
    return value(m[key])


def keys():
    return m.keys()
