class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        
        if len(s) % 2 != 0:
            return False

        stack = []

        for char in s:
            if char in hashmap.values():
                stack.append(char)

            else:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0
