import sys
sys.path.append('.')
from codex_usage import CodexUsage
import time

c = CodexUsage()
now = time.time()
print("totals:", c._all_totals(now - 24*3600))
