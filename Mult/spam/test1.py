from threading import Thread

def threaded_run(func):
    def wrapped(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
        return thr
    return wrapped