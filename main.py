import statsd
from time import sleep


c = statsd.StatsClient()
#c = statsd.TCPStatsClient(port=8126)
c.incr('foo')  # Increment the 'foo' counter.
c.gauge("bar", 0)
sleep(1)

for _ in range(10000):
    c.gauge("bar", 1, delta=1000)
