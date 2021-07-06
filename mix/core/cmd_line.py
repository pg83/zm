import os


def parse_pkgs(ctx):
    args = ctx['args']
    binary = ctx['binary']
    where = os.path.join(os.path.dirname(binary), 'pkgs')

    if len(args) > 0:
        pkgs = args
    else:
        pkg = os.getcwd()

        if pkg.startswith(where):
            pkg = pkg[len(where) + 1:]
        else:
            raise Exception('should run from pkg dir')

        pkgs = [pkg]

    return binary, where, pkgs
