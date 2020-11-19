#include<iostream>
using namespace std;

int Partition (int *a,int p,int r)
{
    int x=a[r],q;
    int i,j,temp;
    i=p-1;
    for(j=p;j<r;j++)
    {
        if(a[j]<=x)
        {
            temp=a[i+1];
            a[i+1]=a[j];
            a[j]=temp;
            i++;
        }
    }
    temp=a[i+1];
    a[i+1]=a[r];
    a[r]=temp;
    q=i+1;
    return q;
}
void  Quicksort(int *a,int p,int r)
{
    if(p<r)
    {
        int q;
        q=Partition(a,p,r);
        Quicksort(a,p,q-1);
        Quicksort(a,q+1,r);
    }
    

}

int main()
{
    int a[8]={2,6,7,1,3,5,6,4};
    for(int i=0;i<8;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;
    Quicksort(a,0,7);
    for(int i=0;i<8;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<endl;

}
