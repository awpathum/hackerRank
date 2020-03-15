#include <bits/stdc++.h> 
using namespace std; 

int main(int argc, char const *argv[])
{
    int n;
    //cout << "Enter number of clouds : ";
cin>>n; // how many numbers;
vector<int> clouds(n);
//cout << "Enter Cloud Array" << endl;
for ( int i=0; i<n; ++i ){
    cin>>clouds[i];
}

int curCloud = 0;
int jumps = 0;
for (int i = 0; i < clouds.size(); i++)
{
    i = curCloud;
   // cout << "Current Cloud : "<< i << endl;

    if (clouds[i+2] == 0)
    {
        curCloud = curCloud + 2;
        jumps++;
    }else if(clouds[i + 1] == 0){
        curCloud = curCloud + 1;
        jumps++;
    }
    
}
cout << jumps-1<< endl;

    return 0;
}

