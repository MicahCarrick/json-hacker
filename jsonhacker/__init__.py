from app import JsonHacker

VERSION = (0, 1, 0)

def get_version():
    return "%s.%s.%s" % (VERSION[0], VERSION[1], VERSION[2])
