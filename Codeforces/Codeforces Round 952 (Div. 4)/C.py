def solve():
    for _ in range(int(input())):
        n = int(input())
        li = map(int, input().split())
        total = mx = ans = 0

        for x in li:
            total +=x
            mx = max(mx,x)
            if total - mx == mx:
                ans += 1

        print(ans)


solve()