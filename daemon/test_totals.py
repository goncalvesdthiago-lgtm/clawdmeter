import sys, time
sys.path.append('.')
from codex_usage import CodexUsage

c = CodexUsage()
now = time.time()
start = now - 7 * 86400
ans = 0
for totals in c._all_totals(start):
    if totals:
        val = max(0, totals[-1][1] - 0) # approximation
        if val > 0:
            print("file gave:", val)
        ans += val
print("total:", ans)
