class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []

        for char in s:
            if char in hashmap.values():
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False

                if stack[-1] != hashmap[char]:
                    return False
                
                stack.pop()

        return len(stack) == 0




        