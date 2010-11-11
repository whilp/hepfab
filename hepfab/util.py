import logging
import math

__all__ = ["NullHandler", "digits", "genrange"]

try:
    NullHandler = logging.NullHandler
except AttributeError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger("hepfab.util").addHandler(NullHandler())

def digits(n, base=10):
    """Return the number of digits in *n*."""
    if n == 0:
        return 1

    n = abs(n)
    if base != 10:
        digits = math.log(n, base)
    else:
        digits = math.log10(n)
    return int(digits) + 1

def genrange(gen, *args):
    start, stop, step = None, None, None
    arglen = len(args)
    if arglen == 3:
        start, stop, step = args
    elif arglen == 2:
        start, stop = args
    else:
        (stop,) = args
        
    spec = "%s%%0%d.d" % (gen, digits(stop))
    for i in xrange(*args):
        yield gen % i
