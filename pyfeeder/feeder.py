import numpy as np
import pandas as pd
import redis

db = redis.StrictRedis(host='redis', port=6379)
db.flushdb()


def feed_db(cache):
    last = pd.Timestamp.now() - pd.Timedelta(seconds=3)

    while True:
        now = pd.Timestamp.now()
        if now - last >= pd.Timedelta(seconds=3):
            cache.set(now, np.random.random())
            # cache.set(now, 10)
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
