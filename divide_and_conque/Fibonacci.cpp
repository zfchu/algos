//求解F(n),必须先计算F(n-1)和F(n-2),计算F(n-1)和F(n-2)，
//又必须先计算F(n-3)和F(n-4)。。。。。。以此类推，
//直至必须先计算F(1)和F(0),然后逆推得到F(n-1)和F(n-2)的结果，
//从而得到F(n)要计算很多重复的值，在时间上造成了很大的浪费，
//算法的时间复杂度随着N的增大呈现指数增长，时间的复杂度为O(2^n)，即2的n次方
#include <iostream>

using namespace std;

int64_t Fib(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return Fib(n - 1) + Fib(n - 2);
}

int main(int argc, char const *argv[])
{
    for (int i = 0; i < 100; i++)
    {
        cout << "Fib(" << i << ")"
             << "=" << Fib(i) << endl;
    }

    return 0;
}
