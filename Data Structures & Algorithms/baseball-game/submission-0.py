class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #1. Create a new int list, total, that stores the updated values from the operations
        #2. Iterate through the operations list from start to finish
            #3. If it is a value, you append it 
            #4. If it is not a value, + you add 2 values
            #5. If it is D, you double the last score
            #6. If it is C, you remove it -> You just increase the element count by one
            #Conditoinal if else statement
        #7. After the loop is finished, I will iterate the total to return the sum
            #8. First declare a int variable called sum out side the loop
        total = []
        for element in range(len(operations)):
            if operations[element] == 'C':
                total.pop()
            elif operations[element] == 'D':
                total.append(2 * total[len(total) - 1])
            elif operations[element] == '+':
                total.append(total[len(total) - 1] + total[len(total) - 2])
            else:
                total.append(int(operations[element]))
        sum_t = 0
        for index in range(len(total)): 
            sum_t += int(total[index])
        return sum_t