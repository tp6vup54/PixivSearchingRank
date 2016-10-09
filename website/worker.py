import gevent
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all(thread=False, select=False)

session = None

class AsyncWorker():
    def __init__(self, keyword):
        self.response = None
        self.keyword = keyword

    def send(self):
        if session:
            self.response = session.search_works(self.keyword)
            return self
        else:
            return None


search_works = AsyncWorker


def send(r, pool=None):
    """Sends the request object using the specified pool. If a pool isn't
    specified this method blocks. Pools are useful because you can specify size
    and can hence limit concurrency."""
    if pool is not None:
        return pool.spawn(r.send)

    return gevent.spawn(r.send)


def map(requests, size=None, exception_handler=None, gtimeout=None):
    """Concurrently converts a list of Requests to Responses.
    :param requests: a collection of Request objects.
    :param stream: If True, the content will not be downloaded immediately.
    :param size: Specifies the number of requests to make at a time. If None, no throttling occurs.
    :param exception_handler: Callback function, called when exception occured. Params: Request, Exception
    :param gtimeout: Gevent joinall timeout in seconds. (Note: unrelated to requests timeout)
    """

    requests = list(requests)

    pool = Pool(size) if size else None
    jobs = [send(r, pool) for r in requests]
    gevent.joinall(jobs, timeout=gtimeout)

    ret = []

    for request in requests:
        if request.response is not None:
            ret.append(request.response)
        elif exception_handler and hasattr(request, 'exception'):
            ret.append(exception_handler(request, request.exception))
        else:
            ret.append(None)

    return ret