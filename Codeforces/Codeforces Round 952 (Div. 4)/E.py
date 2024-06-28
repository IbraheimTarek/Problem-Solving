def solve():
    for _ in range(int(input())):
        x, y, z, k = list(map(int, input().split()))
        ans = 0
        for a in range(1,  x + 1):
            for b in range(1, y + 1):
                if(k %(a * b)): # it will give a float number skip those a , b
                    continue
                c = k //(a * b)
                if c > z: # unvalid c
                    continue
                ways = (x - a + 1) * (y - b + 1) * (z - c + 1)
                ans = max(ans,ways)
        
        print(ans)

solve()