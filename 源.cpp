#define  _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<math.h>
void main () {
	double x, y,z,l,s;
	scanf("%1f,%1f,%1f", &x, &y, &z);
	l = (x + y + z) / 2;
	s = sqrt (l * (l - x) * (l - y) * (l - z));
	printf("%d", s);

}