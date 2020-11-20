//利用贪心算法求解活动选择问题
#include<iostream>
using namespace std;
#define n 5 //商品数量
struct action
{
    int s ;//起始时间
    int f;//结束时间
    int index;//活动的编号
};
//利用二分归并排序对结束时间进行排序
void Merge(action *a,int p, int q, int r)
{
    int n1 = q - p + 1;       //左部分的的元素个数
    int n2 = r - q;           //同上
    int i, j, k;
    action *L = new action[n1+1];
    action *R = new action[n2+1];
    for(i=0;i<n1;i++)
        L[i]=a[p+i];
    for(j=0;j<n2;j++)
        R[j]=a[q+j+1];
    L[n1].f=11111111;
    R[n2].f=11111111;
     // 数组L从0~n1-1存放，第n1个存放int型所能表示的最大数，即认为正无穷，这是为了
     //处理合并时，比如当数组L中的n1个元素已经全部按顺序存进数组a中，只剩下数组R的
     //部分元素，这时因为R中剩下的元素全部小于11111111,则执行else语句，直接将剩下的
     //元素拷贝进a中。
    for(i=0,j=0,k=p;k<=r;k++)
    {
        if(L[i].f<=R[j].f)
            a[k]=L[i++];
        else
            a[k]=R[j++];
    }
 
    delete []L;
    delete []R;
}
 
void MergeSort(action *a, int l, int r)
{
    if(l<r)
    {
        int m = (l+r)/2;
        MergeSort(a,l,m);
        MergeSort(a,m+1,r);
        Merge(a,l,m,r);
    }
}


int main()
{
    action a[n]=
    {
        {0,4,1},
        {12,16,2},
        {3,5,3},
        {8,10,4},
        {3,7,5}

    };
    
    MergeSort(a,0,4);

    for(int i=0;i<n;i++)
    {
        cout<<a[i].f<<" ";
    }
    cout<<endl;

    cout<<"choose action "<<a[0].index<<endl;
    int k=1;
    for(int i=1;i<n;i++)
    {
        if(a[i].s>=a[k].f)
        {
            cout<<"choose action "<<a[i].index<<endl;
            k=i;
        }
       

    }


}
