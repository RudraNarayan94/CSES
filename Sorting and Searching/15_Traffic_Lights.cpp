#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, n;
    cin >> x >> n;
    vector<int> pos(n);
    for (int i = 0; i < n; i++) cin >> pos[i];

    // Store traffic light positions
    set<int> lights;
    lights.insert(0);
    lights.insert(x);

    // Store segment lengths (multiset allows duplicates)
    multiset<int> segments;
    segments.insert(x);

    for (int p : pos) {
        // Find neighbors around new light
        auto it = lights.lower_bound(p);
        int right = *it;
        int left = *prev(it);

        // Remove old segment
        segments.erase(segments.find(right - left));

        // Add new segments
        segments.insert(p - left);
        segments.insert(right - p);

        // Insert new light
        lights.insert(p);

        // Longest segment is the largest element in multiset
        cout << *segments.rbegin() << " ";
    }
    cout << "\n";
    return 0;
}
