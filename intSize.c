#include <stdio.h>

int main()
{
	int integerVariable;
	size_t size;
	
	size = sizeof(integerVariable);
	
	printf("Size of Integer Variable is %zu bytes\n", size);
	
	return 0;
	
}
