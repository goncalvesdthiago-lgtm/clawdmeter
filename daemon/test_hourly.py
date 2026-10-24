import sys
sys.path.append('.')
from codex_usage import CodexUsage
import time

c = CodexUsage()
now = time.time()
print("hourly:", c.hourly(now))
print("cache keys:", c.cache.keys() if hasattr(c, 'cache') else None)
