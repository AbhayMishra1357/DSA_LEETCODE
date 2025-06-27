'''Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.'''

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res=[]
        self.previous=0
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit() :
                res.append(int(operations[i]))
            # print(res)
            # print(self.previous)

            elif operations[i] == "C":
                res.pop()
            # print(res)
            # print(self.previous)
            
            elif operations[i] == "D":
                res.append( 2 * res[-1])
            # print(res)
            # print(self.previous)

            elif operations[i] == "+":
                res.append( res[-1] + res[-2])

        return sum(res)

a=Solution()
print(a.calPoints(["5","2","C","D","+"]))
print(a.calPoints(["5","-2","4","C","D","9","+","+"]))

