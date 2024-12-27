
#include <iostream>
using namespace std;
int fact(int n)
{
    if(n == 1 || n == 0)
    {
        return 1;
    }
    else
    {
        return n*fact(n-1);
    }
}

int main()
{
    int n;
    cout<<"enter number: ";
    cin>>n;
    int a = n;
    int b = 0;
    int c = 0;
    int d;
    cout<<"\nenter the number of digit present in given number"<<endl;
    cin>>d;
    for(int i = 0; i < d; i++)
    {
        c = a%10;
        a = a/10;
        b = b + fact(c);
    }
    if(b == n)
    {
        cout<<"given number is strong number"<<endl;
        
    }
    else
    {
        cout<<" given number is not strong number "<<endl;
    }

    return 0;
}