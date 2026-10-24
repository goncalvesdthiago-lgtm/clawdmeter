import sys
sys.path.append('.')
from codex_usage import CodexUsage
import time

c = CodexUsage()
print("get(now):", c.get(time.time()))
print("cache keys:", c.cache.keys() if hasattr(c, 'cache') else None)
