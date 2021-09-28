#include <iostream>

using namespace std;

void Hanoi(int n, char A, char B, char C)
{
	if (n == 1)
	{
		//圆盘只有一个时，只需将其从A塔移到C塔
		cout << "move " << n << " from " << A << " to " << C << endl;
	}
	else
	{
		Hanoi(n - 1, A, C, B);//递归，把A塔上编号1~n-1的圆盘移到B上，以C为辅助塔
		cout << "move " << n << " from " << A << " to " << C << endl;//把A塔上编号为n的圆盘移到C上
		Hanoi(n - 1, B, A, C);//递归，把B塔上编号1~n-1的圆盘移到C上，以A为辅助塔
	}
}

void Hanoi(int n)
{
	if (n <= 0)
		return;
	Hanoi(n, 'A', 'B', 'C');
}

int main()
{
	int a = 0;
	cout << "输入盘数： " << endl;
	cin >> a;
	Hanoi(a);
	return 0;
}
