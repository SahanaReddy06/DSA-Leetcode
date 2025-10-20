class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 🧱 Step 1: Use a stack to store opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # 🔑 Step 2: Map closing → opening brackets

        # 🔁 Step 3: Loop through each character in the string
        for char in s:
            if char in mapping:  # If it's a closing bracket
                # Step 3a: Check if top of stack matches its pair
                if stack and stack[-1] == mapping[char]:
                    stack.pop()  # ✅ Matched → remove from stack
                else:
                    return False  # ❌ Mismatch or stack empty → invalid
            else:
                stack.append(char)  # Step 3b: If it's an opening bracket → push to stack

        # ✅ Step 4: If stack empty → all brackets matched correctly
        return True if not stack else False
