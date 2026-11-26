import sys
from collections import defaultdict
 
def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx + n]
        idx += n
        a = list(map(int, a))
        mp = defaultdict(int)
        arr = []
        ans = 0
        for i in range(n - 4):
            cur = a[i] + a[i + 2] - a[i + 4]
            ans += mp[cur]
            if i >= 2 and arr[i - 2] == cur:
                ans -= 1
            if i >= 4 and arr[i - 4] == cur:
                ans -= 1
            mp[cur] += 1
            arr.append(cur)
        out.append(str(ans))
    print("\n".join(out))
 
main()