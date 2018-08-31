import numpy as np
import pandas as pd
import redis

from id_access import Client
cl = Client()

db = redis.StrictRedis(host='redis', port=6379)
db.flushdb()


def feed_db(cache):
    last = pd.Timestamp.now() - pd.Timedelta(seconds=3)

    while True:
        now = pd.Timestamp.now()
        if now - last >= pd.Timedelta(seconds=3):
            # what = np.random.random()
            what = cl.get_orderbook(grids='BE', products='Hour')
            cache.set(now, what)
            now, last = pd.Timestamp.now(), now


def foo():
    last = pd.Timestamp.now() - pd.Timedelta(seconds=3)
    while True:
        now = pd.Timestamp.now()
        if now - last >= pd.Timedelta(seconds=3):
            print(now, np.random.random())
            now, last = pd.Timestamp.now(), now


if __name__ == "__main__":
    feed_db(db)
    # foo()
