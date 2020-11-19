//利用贪心算法求解部分背包问题
#include<iostream>
using namespace std;
#define n 5 //商品数量
struct bag
{
    int p ;//商品价值
    int v;//商品体积
    double c ;//商品的性价比
    int index;//商品编号
};
//利用二分归并排序对性价比进行排序
void Merge(bag *a,int p, int q, int r)
{
    int n1 = q - p + 1;       //左部分的的元素个数
    int n2 = r - q;           //同上
    int i, j, k;
    bag *L = new bag[n1+1];
    bag *R = new bag[n2+1];
    for(i=0;i<n1;i++)
        L[i]=a[p+i];
    for(j=0;j<n2;j++)
        R[j]=a[q+j+1];
    L[n1].c=-11111111;
    R[n2].c=-11111111;
     // 数组L从0~n1-1存放，第n1个存放int型所能表示的最大数，即认为正无穷，这是为了
     //处理合并时，比如当数组L中的n1个元素已经全部按顺序存进数组a中，只剩下数组R的
     //部分元素，这时因为R中剩下的元素全部小于11111111,则执行else语句，直接将剩下的
     //元素拷贝进a中。
    for(i=0,j=0,k=p;k<=r;k++)
    {
        if(L[i].c<=R[j].c)
            a[k]=R[j++];
        else
            a[k]=L[i++];
    }
 
    delete []L;
    delete []R;
}
 
void MergeSort(bag *a, int l, int r)
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
    bag a[n]=
    {
        {20,1,20,1},
        {10,2,5,2},
        {30,3,10,3},
        {60,5,12,4},
        {30,2,15,5}

    };
    
    MergeSort(a,0,4);

    int  c=5;
    int i=0;
    double ans=0;
    while(c>0&&i<n)
    {
        if(a[i].v<c)
        {
            cout<<"choose "<<a[i].index<<endl;
            ans=ans+a[i].p;
            c=c-a[i].v;
        }
        else
        {
            cout<<"choose bag "<<c<<" volume "<<a[i].index<<endl;
            ans=ans+a[i].p*(1.0*c/a[i].v);
            c=0;
        }
        i=i+1;
    }
    cout<<"the most value is "<<ans<<endl;


}
