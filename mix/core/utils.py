def iter_uniq_list(lst):
    v = set()

    for l in lst:
        if l not in v:
            v.add(l)

            yield l


def uniq_list(lst):
    return list(iter_uniq_list(lst))
