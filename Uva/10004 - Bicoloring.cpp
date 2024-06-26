#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;

int main()
{
    int n;
    while (scanf("%d", &n), n != 0)
    {
        vector<vi> AL(n, vi());
        int edg;
        scanf("%d", &edg);
        while (edg--)
        {
            int a, b;
            scanf("%d %d", &a, &b);
            AL[a].push_back(b);
            AL[b].push_back(a);
        }

        int s = 0;
        queue<int> q;
        q.push(s);
        vi color(n, INT_MAX);
        color[s] = 0;
        bool isBipartite = true;
        while (!q.empty() && isBipartite)
        {
            int u = q.front();
            q.pop();
            for (auto &v : AL[u])
            {
                if (color[v] == INT_MAX)
                {
                    color[v] = 1 - color[u];
                    q.push(v);
                }
                else if (color[v] == color[u])
                {
                    isBipartite = false;
                    break;
                }
            }
        }
        printf("%sBICOLORABLE.\n", (isBipartite) ? "" : "NOT ");
    }

    return 0;
}