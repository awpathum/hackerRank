// #include <bits/stdc++.h> 
// using namespace std; 

// int main(int argc, char const *argv[])
// {
//     vector<string> s(100);
// for ( int i=0; i<s.size(); ++i ){
//     cin>>s[i];
// }


//     int n;
//     cin >> n;
//     int count = 0;



//     if(s.size() < n){
//         for (int i = 0; i < s.size(); i++)
//         {
//             if(s[i] == "a"){
//                 count++;
//             }
//         }

//         }else{
//             while(s.size() < n){
//                 s.push_back("s");
//             }
//             for (int i = 0; i < s.size(); i++)
//         {
//             if(s[i] == "a"){
//                 count++;
//             }
//         }

//     }
    
//     //cout << s << endl;
//     return 0;
// }


    #include <bits/stdc++.h> 
    using namespace std; 

    int main(int argc, char const *argv[])
    {

        string s;
        //cout << "Enter a string : " << endl;
        cin >> s;

        int n;
    // cout << "Enter a number : " << endl;
        cin >> n;
    //  cout << "s.length()"<< s.length() << endl;
        if(s.length() >= n){
        cout << "*" << endl;
        cout << s.find("a") << endl;
        }else{
            int count = 0;
            while (s.length() < n)
            {
                s.append(s);
            }
            //cout << s.length() << endl;
                int found = -1;
            // cout << s << endl;
                for (int i = 0; i < n; i++)
                {
                    if(s[i] == 'a'){
                        count++;
                    }
                    //cout << "count inf for loop" << count << endl;
                
                }
            

            cout << count;
        // cout << "a count = "<<count << endl;
            
        }
        return 0;
    }