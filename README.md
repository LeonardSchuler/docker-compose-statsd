# Usage

```
docker-compose up
```


```
pip3 install statsd
```
```
python3 main.py
```

# Problems
TIME_ZONE environment variable is not picked up by Grafana correctly

# Architecture
- statsd exposes udp port 8125 for metrics mapped to port 8126 on the host
- statsd exposes port 8126 for simple inspections
- graphite-web exposes its web server on port 8000
- carbon backend for graphite, data is exposed via a shared volume to the web server


