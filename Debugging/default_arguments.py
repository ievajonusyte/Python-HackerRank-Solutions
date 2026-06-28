class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
'''
Task: debug print_from_stream so it works with both its default
and explicit arguments.
 
Rules:
the function prints the first n values returned by stream.get_next()
one value per line
if called without a stream argument, it should use a fresh instance
of EvenStream as the default
 
Bug found: the original code wrote "stream=EvenStream()" directly in
the function signature. In Python, default argument values are
evaluated only once, when the function is defined, not on every call.
So every call that left out stream reused the exact same EvenStream
instance, and its internal counter kept advancing instead of
resetting back to 0.
 
Fix: use "stream=None" as the default, then check "if stream is None"
inside the function body and create a new EvenStream there. This way
a brand new instance is made fresh on every call that does not supply
its own stream.
'''
def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
