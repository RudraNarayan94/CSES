#include<bits/stdc++.h>
using namespace std;


class FT
{
    public:

    vector<int>arr;
    int n;

    FT(int nn)
    {
         n = nn;
        arr.assign(n+1,0);
    }

    void update(int ind, int val)
    {
        while(ind <= n)
        {
            arr[ind] += val;
            ind += (ind&(-ind));
        }
    }

    int getsum(int ind)
    {
        int s=0;

        while(ind>0)
        {
            s += arr[ind];
            ind -= (ind&(-ind));
        }

        return s;
    }

    int find_by_order(int k)
    {
        int ind=0;
        int mask = 1<<20;

        while(mask)
        {
            int next = ind+mask;
            if(next<= n && arr[next]<k)
            {
                k -= arr[next];
                ind= next;
            }

            mask = mask>>1;
        }

        return ind+1;

    }
};

int main()
{
    int n,k;
    cin>>n>>k;

    FT ft(n);

    for(int i=1; i<=n; i++)
    {
        ft.update(i,1);
    }

    vector<int>ans;
    int pos=0;
    int rem=n;
    for(int i=1; i<=n; i++)
    {
        pos = (pos +k)%rem;
        int tp = ft.find_by_order(pos+1);
        ans.push_back(tp);
        ft.update(tp,-1);
        rem--;
    }

    for(int i=0; i<ans.size(); i++)
    {
        cout<<ans[i]<<" ";
    }
}