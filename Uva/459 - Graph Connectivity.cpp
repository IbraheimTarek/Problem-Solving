#include <bits/stdc++.h>
using namespace std;
enum
{
    UNVISITED = -1,
    VISITED = -2
};
char line[101];
typedef vector<int> vi;
vi dfs_num;
vector<vi> AL;
void dfs(int u)
{
    dfs_num[u] = VISITED;
    for (auto &v : AL[u])
        if (dfs_num[v] == UNVISITED)
            dfs(v);
}
int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    int tc;
    cin >> tc;
    while (tc--)
    {
        char maxchar;
        cin >> maxchar;
        dfs_num.assign(maxchar + 1, UNVISITED);
        AL.assign(maxchar + 1, vi());
        cin.ignore();
        string s;
        while (getline(cin, s) && s != "")
        {
            AL[s[0]].push_back(s[1]);
            AL[s[1]].push_back(s[0]);
        }
        int numcc = 0;
        for (int i = 'A'; i <= maxchar; i++)
        {
            if (dfs_num[i] == UNVISITED)
            {
                numcc++;
                dfs(i);
            }
        }
        cout << numcc << "\n";
        if (tc)
        {
            cout << "\n";
        }
    }
    return 0;
}