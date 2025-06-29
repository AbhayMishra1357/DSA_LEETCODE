'''A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ischar=""
        for i in sentence:
            if ord(i)>= 97 and ord(i) <= 122:
                if i not in ischar:
                    ischar+=i 
        return len(ischar) == 26
            
a=Solution()
print(a.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))