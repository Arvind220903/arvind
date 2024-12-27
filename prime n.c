#include<stdio.h>


int main()
{
    int n;
    int p = 0;
    printf(" enter any number: ");
    scanf("%d",&n);
    for(int i = 1 ; i < n-1; )
    {
        if( n % i == 0)
        {
        p++;
        i++;
        }
        else
        {
            i++;
        }

    }
    if(p > 1)
    {
        printf("given number is  no prime");
    }
    else
    {
        printf("given number is prime");
    }
    return 0;
}