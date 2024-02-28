//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
    public:
    int DivisibleByEight(string s){
        //code here
        int sum=0;
        if(s.size()<4){
            for (int i=0;i<s.size();i++){
                sum = (sum*10)+(s[i]-'0');
            }
        }
        else 
        {
            for(int i=s.size()-3;i<s.size();i++){
                sum = (sum*10)+(s[i]-'0');
            }
        }
        if (sum%8==0)
        return 1;
        else 
        return -1;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin>>S;
        Solution ob;
        cout<<ob.DivisibleByEight(S)<<"\n";
    }
}
// } Driver Code Ends