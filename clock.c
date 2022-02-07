#include <time.h>
#include <stdio.h>

void code()
{
	for(int i=0; i<5; i++)
	{
		printf(".");
	}
	printf("\n");
}

int main()
{
	int runs;
	
	printf( "Enter the number of times you would like the code to be run: ");
	scanf("%d", &runs);
	
	clock_t t;
	printf("start: %d \n", (int) (t=clock()));
	
	for(int i=0; i<runs; i++)
	{
		code();
	}
	
	printf("stop: %d \n", (int) (clock()));
	t = clock()-t;
	printf("Elapsed: %f seconds\n", (double) t / CLOCKS_PER_SEC);
	printf("Number of runs: %d \n", runs);
	printf("Average per run: %f seconds\n", ((double) t / CLOCKS_PER_SEC)/ runs);
	
	return 0;
}
