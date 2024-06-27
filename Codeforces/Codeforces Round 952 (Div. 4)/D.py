def solve():
    for _ in range(int(input())):
        n,m = map(int,input().split())
        li = []
        for i in range(n):
            li.append(input())
        top = (1e400,1e400)
        bottom = (-1e400, -1e400)
        for i in range(n):
            for j in range(m):
                if li[i][j] == '#':
                    top = min(top, (i,j))
                    bottom = max(bottom, (i,j))
        assert top[1] == bottom[1]
        result_row = (top[0] + bottom[0]) // 2 + 1
        result_col = top[1] + 1
        print(result_row, result_col)

solve()