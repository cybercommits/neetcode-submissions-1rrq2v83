class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int longestLength;
        string combinedStr; 
        if(word1.length() < word2.length()){
            longestLength = word2.length();
        }
        else{
            longestLength = word1.length();
        }
        for(int i = 0; i < longestLength; i++){
            if(i < word1.length()){
                combinedStr += word1[i];
            }
            if(i < word2.length()){
                combinedStr += word2[i];
            }
        }
        return combinedStr;
    }
};