import sys, time
sys.path.append('.')
from claude_usage_daemon import _CODEX_USAGE
now = time.time()
print("get:", _CODEX_USAGE.get(now))
print("hourly:", _CODEX_USAGE.hourly(now, 24))
