#include <bits/stdc++.h>
using namespace std;
char line[101], grid[101][101];
int R, C;
int dr[] = {1, 1, 0, -1, -1, -1, 0, 1};
int dc[] = {0, 1, 1, 1, 0, -1, -1, -1}; // S/SE/E/NE/N/NW/W/SW
int floodfill(int r, int c, char c1, char c2)
{
    if ((r < 0) || (r >= R))
        return 0;
    if ((c < 0) || (c >= C))
        return 0;
    if (grid[r][c] != c1)
        return 0;
    int ans = 1;
    grid[r][c] = c2;
    for (int d = 0; d < 8; ++d)
        ans += floodfill(r + dr[d], c + dc[d], c1, c2);
    return ans;
}
int main()
{
    int tc;
    sscanf(gets(line), "%d", &tc);
    gets(line); // dummy
    while (tc--)
    {
        R = 0;
        while (1)
        {
            gets(grid[R]);
            if (grid[R][0] != 'L' && grid[R][0] != 'W')
                break;
            R++;
        }
        C = (int)strlen(grid[0]);
        strcpy(line, grid[R]); // the cell location
        while (1)
        {
            int r, c;
            sscanf(line, "%d %d", &r, &c);
            r--, c--; // location stars form zero
            printf("%d\n", floodfill(r, c, 'W', '.'));
            floodfill(r, c, '.', 'W'); // restore cells
            gets(line);
            if (strcmp(line, "") == 0 || feof(stdin))
            {
                break;
            }
        }
        if (tc)
        {
            printf("\n");
        }
    }
    return 0;
}