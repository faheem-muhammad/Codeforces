import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    MOD = 998244353
    out = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); r = int(data[idx+2]); c = int(data[idx+3])
        idx += 4
        e = n * m - (n - r + 1) * (m - c + 1)
        out.append(str(pow(2, e, MOD)))
    print("\n".join(out))

main()