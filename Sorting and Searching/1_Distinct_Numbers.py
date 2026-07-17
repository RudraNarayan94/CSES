import sys
from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM

data = sys.stdin.buffer.read().split()

s = set()
for x in data[1:]:
    s.add(Wrapper(int(x)))

print(len(s))