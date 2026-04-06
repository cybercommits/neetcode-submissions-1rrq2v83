class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0; //count the number of unique elements
        for(int i = nums.size() - 1; i >= 1; i--){
            //set element to 101 if it is duplicated when it is being compared to the next element
            if(nums[i] == nums[i-1]){
                nums[i] = 101; //to say that the element is removed since nums[i] <= 101   
                //ensures this removes duplicated values when iterating from end to start
            }
        }
        //sort the array again, so 101 is move to the end
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                if(nums[i] < nums[j]){
                    //swapping
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp; 
                }
            }
        }
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 101){
                count++;
            }
        }
        return count; 
    }
};