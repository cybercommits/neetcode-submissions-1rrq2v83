class Solution {
    public boolean hasDuplicate(int[] nums) {
        int[] sortedArray = new int[nums.length];
        for(int i = 0; i <= nums.length-1; i++)
        {
            int least = i;
            //want to sort the array from least to greatest
            for(int n = i; n < nums.length; n++)
            {
               if(nums[n] < nums[least])
               {
                    least = n;
                    sortedArray[i] = nums[i];
               }
            //    else if(nums[n] < nums[i])
            //    {
            //         sortedArray[i] = nums[n];
            //    }
            //    else
            //    {
            //         sortedArray[i] = nums[i];
            //    }
            }
            //swap values
            int temp = nums[i];
            nums[i] = nums[least];
            nums[least] = temp;
        }
        //check to see if value is equal to the next through repeating
        for(int i = 0; i < nums.length-1; i++)
        {
            if(nums[i] == nums[i+1])
            {
                return true;
            }
        }
        return false;
    }
}