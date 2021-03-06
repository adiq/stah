from lib.dateutil.relativedelta import relativedelta
import hashlib


# Time convert usage
# date(relativedelta(seconds=1207509))
attrs = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
date = lambda delta: [
    '%d %s' % (
        getattr(delta, attr), getattr(delta, attr) > 1 and
        attr or attr[:-1]
    ) for attr in attrs if getattr(delta, attr)]


def relative(**kwargs):
    return date(relativedelta(**kwargs))


def hash(string):
    return str(hashlib.md5(string).hexdigest())


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]
