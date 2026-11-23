import sys

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos]); pos += 1
    out = []
    for _ in range(t):
        n = int(data[pos]); k = int(data[pos + 1]); pos += 2
        S = []
        E = []
        cap = float('inf')
        for i in range(n):
            a = int(data[pos]); b = int(data[pos + 1]); c = int(data[pos + 2])
            pos += 3
            s = a + b + c
            if a == b == c:
                cap = min(cap, s)
                e = 0
            elif a <= b <= c:
                e = min(b - a, c - b) + 1
            else:
                e = 0
            S.append(s)
            E.append(e)
        lo = min(S)
        hi = min(cap, lo + k)
        # find max m in [lo, hi] that is feasible
        while lo < hi:
            mid = (lo + hi + 1) // 2
            total = 0
            ok = True
            for i in range(n):
                s = S[i]
                if s >= mid:
                    continue
                total += (mid - s) + 2 * E[i]
                if total > k:
                    ok = False
                    break
            if ok:
                lo = mid
            else:
                hi = mid - 1
        out.append(str(lo))
    print("\n".join(out))

main()