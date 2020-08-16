#include<bits/stdc++.h>

using namespace std;

int main()
{
    int num[100], n = 5;

    for(int i = 0; i < n ; ++i)
    {
        cin >> num[i];
    }

    for(int i = 1 ; i < n ; ++i)
    {
        int x = num[i];
        int j = i - 1;
        while(j >= 0 && num[j] > x)
        {
            num[j+1] = num[j];
            j--;
        }
        num[j+1] = x;
    }

    for(int i = 0; i < n ; ++i)
    {
        cout << num[i];
    }

    return 0;
}
