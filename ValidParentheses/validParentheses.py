# problem 20

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # initialize an empty stack
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            # iterate through every character in the string s
            if c in closeToOpen:
                # if c is a closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # if stack is not empty and the top of the stack is 
                    # the corresponding opening bracket to c

                    stack.pop() # removes the opening bracket from the stack if both the conditions are true
                else:
                    return False # return false if stack is empty
                
            else:
                stack.append(c) # push c onto the stack if it is an opening bracket

        return True if not stack else False
    