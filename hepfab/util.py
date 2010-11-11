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
    """genrange(gen, [start,] stop[, step]) -> xrange object

    Generate a range of hostnames.

    *gen* is a generation prefix (like 'g10'). It will be joined with suffixes
    generated from :func:`xrange(*args)`, producing hostnames like 'g10n01'.

    .. note::
        
        Unlike :func:`xrange`, this function generates an *inclusive* series.
    """
    log = logging.getLogger("hepfab.util.genrange")

    start, stop, step = 1, None, 1
    arglen = len(args)
    if arglen == 3:
        start, stop, step = args
    elif arglen == 2:
        start, stop = args
    else:
        (stop,) = args
    stop += 1

    log.debug("genrange(%r, %r, %r, %r)", gen, start, stop, step)
    spec = "%sn%%0%d.d" % (gen, digits(stop))
    log.debug("Produced spec %r", spec)

    for i in xrange(start, stop, step):
        yield spec % i
