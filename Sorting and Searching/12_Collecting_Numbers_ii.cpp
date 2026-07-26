#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> arr(n);
    vector<int> pos(n + 1);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        pos[arr[i]] = i;
    }

    int rounds = 1;
    for (int i = 1; i < n; i++) {
        if (pos[i + 1] < pos[i]) rounds++;
    }

    auto check = [&](int x) {
        if (x < 1 || x >= n) return 0;
        return (pos[x + 1] < pos[x]) ? 1 : 0;
    };

    while (m--) {
        int a, b;
        cin >> a >> b;
        --a;
        --b;

        int u = arr[a];
        int v = arr[b];

        vector<int> affected = {u - 1, u, v - 1, v};
        sort(affected.begin(), affected.end());
        affected.erase(unique(affected.begin(), affected.end()), affected.end());

        for (int x : affected)
            rounds -= check(x);

        swap(arr[a], arr[b]);
        swap(pos[u], pos[v]);

        for (int x : affected)
            rounds += check(x);

        cout << rounds << '\n';
    }

    return 0;
}