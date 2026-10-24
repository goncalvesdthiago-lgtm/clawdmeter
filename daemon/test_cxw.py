import sys, time
sys.path.append('.')
from codex_usage import CodexUsage

c = CodexUsage()
now = time.time()
c.get(now)
print(c.tokens)
