# Last updated: 5/18/2025, 1:47:07 PM
#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        # check if string contains open to close 
        # stack 
        opens = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for charac in s: 
            if charac in closeToOpen: 
                # if top element is close's corresponding open
                if opens and opens[-1] == closeToOpen[charac]:
                    opens.pop()
                else: 
                    return False
            else: 
                opens.append(charac)

        return len(opens) == 0

        

                