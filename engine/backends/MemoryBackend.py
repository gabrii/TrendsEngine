from collections import Counter

from . import AbstractBackend


class MemoryBackend(AbstractBackend):

    def __init__(self):
        self.counter = Counter()

    def incr(self, key, value=1):
        self.counter[key] += value

    def get(self, key):
        return self.counter[key]
