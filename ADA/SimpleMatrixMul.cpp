#include<iostream>
#include<conio.h>
using namespace std;

void main()
{
	int a[2][2] = { {1,2},{1,2} };
	int b[2][2] = { {2,3},{2,3} };
	int c[2][2] = { {0,0},{0,0} };
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 2; j++)
			for (int k = 0; k < 2; k++)
				c[i][j] += a[i][k] * b[k][j];

	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			cout << c[i][j] <<" ";
		}
		cout << endl;
	}
	_getch();
}