#include <iostream>
#include <vector>
using namespace std;
int bag(int count,int cap,vector<int>& weights,vector<int>& values,vector<vector<int>>& res)
{
    for(int i=1;i<=cap;i++)
    {
        for(int j=1;j<=count;j++)
        {
            if(weights[j]>i)
            {
                res[j][i]=res[j-1][i];
            }
            else
            {
                res[j][i]=max(res[j-1][i-weights[j]]+values[j],res[j-1][i]);
            }
        }
    }
    return res[count][cap];
}

int main()
{
    int count,cap;

    cin >>count>>cap;
    vector<int> weights(count+1,0);
    for(int i=0;i<count;i++)
    {
        cin>>weights[i];
    }
    vector<int> values(count+1,0);
    for(int i=0;i<count;i++)
    {
        cin>>values[i];
    }
    vector<vector<int>> res(count+1,vector<int> (cap+1,0));
    bag(count,cap,weights,values,res);
    cout << res[count][cap];
    return 0;
}