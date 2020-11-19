#include <iostream>
#include <vector>
using namespace std;

int knapsack(int count,int capacity,vector<int>& weights,vector<int>& values,vector<vector<int>>& res)
{
    for(int i=1;i<=count;i++)   
    {
        for(int j=1;j<=capacity;j++)
        {
            if(weights[i] > j)
            {
                res[i][j]=res[i-1][j];
            }
            else
            {
                res[i][j] = max( res[i-1][j-weights[i]] + values[i] , res[i-1][j]);            
            }
            
        }
    }
    return res[count][capacity];
}

int main()
{
    int count,capacity;
    cout << "please input products count and knapsack's capacity: " << endl; // 输入商品数量和背包容量
    cin>>count>>capacity;
    vector<int> weights(count + 1,0);
	vector<int> values(count + 1,0);
    cout << "please input weight array for " << count << " products" << endl;
    for(int i=1;i<=count;i++)
		cin>>weights[i];
    cout << "please input value array for " << count << " products" << endl;
	for(int i=1;i<=count;i++)
		cin>>values[i];
    vector<vector<int>> res(count + 1,vector<int> (capacity + 1,0));
    knapsack(count,capacity,weights,values,res);
    cout << "knapsack result is " << res[count][capacity] << endl;
		
	return 0;


}