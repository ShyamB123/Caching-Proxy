# 🌐 Simple Caching HTTP Proxy in Python

This project is a simple HTTP proxy server written in Python using the built-in `http.server` module. It forwards `GET` requests to a specified origin server and caches the responses using `cachetools.TTLCache` to improve performance and reduce repeated API calls.

---

## 🧰 Features

- ✅ Forwards `GET` requests to an origin API
- ⚡ Caches responses for 5 minutes (TTL)
- 🧹 Optional cache clearing via CLI
- 🛠️ Customizable port and origin via command-line arguments

---

## 🐍 Requirements

Install the necessary packages using `pip`:

```bash
pip install requests cachetools
pip install requests argparse
pip install requests requests
```

---
## Start the Server

```
python server.py --port <number> --origin <url>
```
--port: The port on which the proxy server should run.

--origin: The origin server to forward requests to.

---

## Clear the Cache

```
python server.py --clear-cache
```


## Project Link
https://roadmap.sh/projects/caching-server
