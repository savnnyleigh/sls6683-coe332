from jobs import q

@q.worker
def do_work(item):
    # do something with item...

do_work()
