import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = data[idx:idx + n]
        a = list(map(int, a))
        idx += n

        res = ['0'] * n

        cur_min = float('inf')
        for i in range(n):
            if a[i] < cur_min:
                cur_min = a[i]
                res[i] = '1'

        cur_max = 0
        for i in range(n - 1, -1, -1):
            if a[i] > cur_max:
                cur_max = a[i]
                res[i] = '1'

        out.append(''.join(res))

    print('\n'.join(out))

main()